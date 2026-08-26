---
otero_id: 7028
otero_key: "GA3UH9VQ"
title: "Performance analysis of filtering software using Signal Detection Theory"
authors: "Ashutosh Deshmukh; Balaji Rajagopalan"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.08.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 1015 – 1028

www.elsevier.com/locate/dsw

# Performance analysis of filtering software using Signal Detection Theory

Ashutosh Deshmukh <sup>a,\*</sup>, Balaji Rajagopalan <sup>b</sup>

<sup>a</sup> Sam and Irene Black School of Business, Pennsylvania State University-Erie, Erie, PA 16563, USA <sup>b</sup> School of Business Administration, Oakland University, Rochester, MI 48309, USA

Received 1 June 2005; received in revised form 4 August 2005; accepted 7 August 2005 Available online 8 September 2005

## Abstract

Software filters are increasingly being touted as a solution to restrict access to inappropriate information in a variety of settings. Families want to protect young children from pornographic sites, corporations are searching for ways to minimize trivial use of the Internet by their employees, and non-profit organizations look to control information access to reflect the value system of their communities. Despite the exponential increase in software filter usage, its effectiveness is not clear. In addition, critics of the approach argue that mandated use of filtering software on public computers like libraries may result in denial of vital information to poorer sections of the society who do not have independent access to the Internet, thereby curbing intellectual freedom and creating inequity in access to information. The purpose of this study is to analytically evaluate the performance of software filters using the Signal Detection Theory (SDT) framework. Two types of software filters are modeled and analyzed —simple software filter (single method) and a sequence of software filters (multiple methods). Analysis shows the limited capability of both types of filters, with the multiple-method filter outperforming the simple filter. Results of this study caution proponent of filter-based solution to be realistic with expectations of the benefits of filtering based solutions. Implications of the findings for proper use and design of software filters are discussed. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Software filters; Signal Detection Theory; Efficiency and effectiveness

## 1. Introduction

The phenomenal growth and diffusion of the Internet has provided individuals, communities and businesses with unprecedented access to information. Today, individuals face less of a problem caused by lack of information, as in the pre-Internet era, but more of information overload and lack of the ability to control the flow of information. Families want to protect young children from pornographic sites, corporations are searching for ways to minimize trivial use of the Internet by their employees, and non-profit organizations wish to control information access to reflect the value system of their communities [15,17,18,26]. Information content on the Internet, however, is largely unregulated and accessing information is only a click away. Lately, filtering software based solutions to control access to information have been explored [3,9].

However, the use of filtering software has been controversial. The US Congress passed Children’s Internet Protection Act (CIPA) in 2001 that was upheld by the Supreme Court in 2003 [11,23]. CIPA mandates the use of filtering software in public libraries and schools as a condition for federal aid. This act was challenged by various stakeholders including librarians, civil liberties groups, and even parents [23]. Critics of filtering argue that mandated use of it may result in denial of vital information to poorer sections of the society who do not have independent access to the Internet thereby curbing intellectual freedom and creating inequity in access to information. The primary concern was that the filtering software may filter sites that contain useful information for library users thus violating their First Amendment rights [11].

Recognizing the need to balance the full access to information and content deemed inappropriate for a particular group, courts have specified two criteria that software filters need to use [16]. First, the reasonableness criterion, which states that legitimate uses of the forum should not be substantially interfered due to the proposed restrictions. Second, the strict scrutiny criterion, which requires that in meeting the compelling government interest, the necessary restrictions should be narrowly tailored. There are a number of empirical studies that have evaluated the performance of filtering software [3,9,16,17]. These studies recognize that filtering software makes two different types of errors: filtering out legitimate websites and not filtering out unacceptable websites.<sup>1</sup> Additionally, they report that the software filters are not CIPA compliant; the requirements of CIPA and capabilities of the software filters are not synchronized [11].

In many cases, the use of filtering software may provide a false sense of security. Hence, many researchers suggest that filtering software is just one mechanism in controlling content on the Internet and not a panacea [11,16,23]. However, the societal expectations and dependence on the filtering mechanisms are on the rise and software filters are already in use in a large number of schools, families, and libraries. With a proliferation of websites which are considered inappropriate, it is important to critically assess the performance of filtering software.

The purpose of this paper is to analytically evaluate performance of filtering software based on Signal Detection Theory (SDT). SDT is used to model how decision makers (humans or machines) detect signals in the presence of interference or noise, i.e., when the signals are ambiguous [8,25,27]. SDT assumes that the decision maker behaves like a rational economic player and evaluates costs and consequences of various outcomes. The theory enables us to evaluate relationships between incorrect acceptance of unacceptable websites, incorrect rejection of legitimate or acceptable websites, costs associated with these errors, and base rates of unacceptable websites in the population. Prior studies in the area have not considered all these factors concurrently. Our analysis will offer insights into the performance of filtering software and provide guidance for its proper design and use.

The rest of the paper is organized as follows. In the next section, the SDT framework is discussed following which the use of a single software filter in blocking unacceptable websites is evaluated using the SDT framework. Next, a sequence of software filters is modeled and analyzed using SDT and a comparative performance analysis is presented. Finally, the implications of this study are discussed.

## 2. Signal Detection Theory (SDT)

## 2.1. SDT background

SDT is a probability-based theory that can be used to quantify performance of the diagnostic systems. Gigerenzer et al. [7] traced the roots of the contemporary SDT to Neyman and Pearson’s [14] work on hypothesis testing and statistical inference. Early works that influenced the development of SDT include Bayes and Gauss as chronicled in [7] and [13]. Applications of SDT first surfaced in psychology and medical fields, especially in the areas of information retrieval, aptitude testing, psychiatric diagnosis, and disease diagnosis [8,24,25,27]. Wickens [27] provided three examples of complex decisions where SDT is applicable: (1) a doctor or psychologist is attempting to correctly diagnose a patient; however, the symptoms are ambiguous and contradictory, and the patient is confused and cannot describe the symptoms accurately; (2) a seismologist is trying predict a major earthquake, but the data is vague and conflicting; some data from the historical records is inaccurate; and (3) a witness is trying to identify a suspect, but the event happened in the dark, the witness was confused, and the witness had been interrogated repeatedly making his statements suspect. Clearly, the underlying commonality in all the three situations is that decisions in these contexts are to be made with uncertainty about the variables influencing the decision.

Green and Swets [8], in their seminal work applied SDT in the area of human perception and decision making. In this study, the participants discriminated between stimuli with some particular target characteristic (signal) and stimuli without the characteristic (noise). SDT was used to separate sensitivity (the ability to detect signal) from response bias (the general tendency to choose signal or noise, irrespective of the perception), and compute estimates of each. This sensitivity/response bias approach in the SDT framework was extended to many areas including recognition memory (old and new items), lie detection (lies and truths), personnel selection (desirable and undesirable applicants), jury decision making (guilty versus innocent), medical diagnosis (disease or no disease), industrial inspection (unacceptable and acceptable items), and information retrieval (irrelevant and relevant) information [22].

As evident from the applications of the theory, SDT can be characterized as a model to help decision makers discriminate between <sup>b</sup>signal<sup>Q</sup> and <sup>b</sup>noise<sup>Q</sup>. The decision maker analyzes a particular observation and categorizes the observation as signal or noise. The theory assumes that there is an

![](/api/attachments/GA3UH9VQ/fulltext/images/5685f9a468d4dd149843a070f92f972d8482df190ee3afcaff6f3781d3a643c1.jpg)  
Fig. 1. Signal Detection Theory model.

![](/api/attachments/GA3UH9VQ/fulltext/images/a1032f84bb1e9e8750e7663d52a59f6be09ffdef267651e8f8f2b6b03ebbac62.jpg)  
Fig. 2. Hits and false alarms in Signal Detection Theory.

overlap between distributions of signal and noise, and that any particular observation may arise from either distribution (see Fig. 1).<sup>2</sup> The vertical axis shows probability and horizontal axis represents a variable used by the decision maker to make a decision. For a given observation, if the value of the decision variable is high then the decision maker will respond with <sup>b</sup>signal is present<sup>Q</sup> and if the value is low then the decision maker will respond with <sup>b</sup>noise is present.<sup>Q</sup> The value that is sufficiently high enough to make a <sup>b</sup>signal is present<sup>Q</sup> decision is called criterion (shown by a thick black line between the distributions in Fig. 1). The decision rule is: if the value of the decision variable <sup>N</sup> criterion, then respond yes and if the value of the decision variable - <sup>b</sup> criterion, then respond no. For example, if a psychologist is evaluating whether a child has attention deficit hyperactivity disorder (ADHD) then for a particular child a score of 10 or higher will indicate ADHD is present and a lower score will indicate that ADHD is absent.

The signal and noise distributions overlap and as such decisions have four outcomes. As shown in Part I in Fig. 2, if the observation comes from signal distribution and is identified as a signal then the decision is termed a hit. If this observation is identified as noise then the decision is a miss. Part II shows decisions made when the observation comes from noise distribution. If such observation is identified as noise then this decision is called correct identification and if it is identified as signal then the decision is a false alarm. The frequency of hits (false alarms) is called a hit rate (false alarm rate), for example, hit rate is equal to the total number of times a signal detector identifies signal as signal divided by the total number of correct signal observations and false alarm rate is equal to the total number of times a signal detector identifies noise as signal divided by the total number of noise observations. And analogously we have miss rate (1 - hit rate) and correct identification rate (1 - false alarm rate).

![](/api/attachments/GA3UH9VQ/fulltext/images/d2aeda1321183ece594830fbf5cd88e1587aa72efb14127305db56ac467ddd53.jpg)  
Fig. 3. Placement of the criterion for decision making.

As shown in Fig. 3—Part I, if the criterion value is lowered to the left most edge of signal distribution then we get a hit rate of 100% but a large false alarm rate. On the other hand, if the criterion value is raised to the right most edge of noise distribution then we get a low hit rate but zero false alarm rates. Since signal and noise distributions overlap, we cannot achieve 100% hit rate and zero false alarm rates. The choice of criterion value depends on the underlying distributions and there are many methods proposed in the SDT. This paper uses a Bayesian decision theoretic approach provided in the SDT to model decision making. This is a general approach applicable to any type of underlying signal and noise distributions [8,25]. This method uses hit rates, false alarm rates, benefits and costs of decisions, and prior probabilities to make a decision. The decision matrix for the decision maker is shown in Fig. 4.

In sum, the four outcomes possible when evaluating the decision as shown in the matrix format in Fig. 4 are hit, miss, false alarm and correct identification. A hit is when the decision maker classifies the event as signal when the event is in fact signal. A miss occurs when the decision maker classifies the event as noise when the event is signal. A false alarm is when the decision maker classifies the event as signal when the event is noise. Finally, correct identification results when the decision maker classifies the event as noise when the event is noise. The conditional probabilities for these four events are Pr (SV | S), Pr (NV | S), Pr $( S ^ { \prime } \mid N )$ , and $P r \left( N ^ { \prime } \mid N \right)$ , respectively. These probabilities form the basis to specify the SDT based decision rules.

Under the Bayesian method, the decision maker classifies an event as signal or noise in two steps [8,25,27]. A likelihood ratio is first calculated and then compared with the criterion value. The decision maker has to choose between two hypotheses, for example, signal or noise. The decision maker calculates two likelihoods $L \left( S \right)$ and $L \left( N \right)$ . The hypothesis with the larger likelihood is chosen by applying the decision rule:

Signal Detector

<table><tr><td></td><td>Signal (S&#x27;)</td><td>Noise (N&#x27;)</td></tr><tr><td>Signal (S)</td><td>Pr (S&#x27; | S)Hit Rate</td><td>Pr (N&#x27; | S)Miss Rate</td></tr><tr><td>Noise (N)</td><td>Pr (S&#x27; | N)False Alarm Rate</td><td>Pr (N&#x27; | N)Correct Identification</td></tr></table>

Fig. 4. Decision matrix for the signal detector.

$$
\text {   If   } L (S) \geq L (N), \text {   then   select   } S
$$

If $L ( S ) { < } L ( N )$ ; then select N:

This comparison can be converted into the likelihood ratio. Note that this ratio does not represent probability. The likelihood ratio is given by:

$$
\operatorname{LR} (S: N) = L (S) / L (N).\tag{1}
$$

The decision to accept a hypothesis is taken by comparing this likelihood ratio with to a criterion C:

If $\operatorname { L R } ( S ; N ) { \ge } C$ ; then select S

If $\operatorname { L R } ( S { \mathrm { : } } N ) { \mathrm { < } } C ,$ ; then select N:

The likelihood ratio in the SDT framework is given by the following formula.

$$
\begin{array}{r l} \text { Likelihood   ratio   (LR) } & = \frac {\text { Hit   rates }}{\text { False   alarm   rates }} \\ & = \frac {P r (S ^ {\prime} | S)}{P r (S ^ {\prime} | N)}. \end{array}\tag{2}
$$

This likelihood ratio formula, as required in SDT, is for nonnested complementary hypotheses; the derivation of this formula is given in Refs. [8,25]. LR is then compared with the criterion value. The decision maker sets the criterion value based on the prior probabilities of the observation being signal or noise and the benefits associated with hits and correct identifications and costs associated with misses and false alarms [25]. Consistent with prior work [8,25] we assume that the decision maker (human or machine) behaves as a rational decision maker, and evaluates costs and benefits of various outcomes in order to optimize performance. The prior probabilities of an observation being signal or noise are represented as Pr (S) and Pr (N). Let the benefits associated with hits $\left( P r \ \left( S ^ { \prime } \mid S \right) \right)$ ) and correct identifications $\left( P r \left( N ^ { \prime } \mid N \right) \right)$ be $B _ { S ^ { \prime } S }$ and $B _ { N ^ { \prime } N }$ and the costs associated with misses $\left( P r \left( N ^ { \prime } | S \right) \right)$ and false alarms $\left( P r \ \left( S ^ { \prime } \ | \ N \right) \right)$ be $C _ { N ^ { \prime } S }$ and $C _ { S ^ { \prime } N }$

The criterion value is then given by:

$$
= \frac {P r (N)}{P r (S)} \times \frac {\text {(Benefits of a correct identification - Costs of a false alarm)}}{\text {(Benefits of a hit - Costs of a miss)}}\tag{3}
$$

$$
\text { Criterion   Value } = \frac {P r (N)}{P r (S)} \times \frac {(B _ {N ^ {\prime} N} - C _ {S ^ {\prime} N})}{(B _ {S ^ {\prime} S} - C _ {N ^ {\prime} S})}.\tag{4}
$$

The decision rule is to treat the event as signal if the likelihood ratio (given in Eq. (2)) is greater than or equal to the criterion value and to treat the event as noise if the likelihood ratio is lesser than the criterion value.

Eq. (4) has many interesting applications. This equation captures benefits and costs of four outcomes and can help in decisions where costs of misses and false alarms differ greatly. For example, low probability and high consequence events such as management fraud or earthquake have a very high cost of misses. On the other hand, certain events such as disease detection also have high costs of false alarms. These costs can be formalized in the Eq. (4). Additionally, if the event has a low prior probability then the costs of false alarms can affect decisions. Bayesian framework thus allows the decision maker to consider various tradeoffs and costs involved in the decision. This brief description of SDT provides background for our study. However, for a comprehensive understanding of various techniques of SDT please refer to Refs. [8], [25], and [27].

There are numerous applications of SDT in the business area, for example, quality control, marketing, work safety, and audit areas. Davis and Parasuraman [5] showed that quality inspectors detect fewer faulty items as their work shift progresses. Such behavior stems from response bias and not sensitivity decline; this research led to remedies that addressed response bias to improve detection rate. Stanislaw [21] used SDT to successfully predict how repeated inspections improve performance. Singh and Churchill [19] and Cradit et al. [4] used this method in marketing, advertisement, and recognition testing. These studies tested the recall of advertisements and estimated the effects of memorability of an advertisement and response bias (tendency to say yes to fictitious advertisements) in such recall. These studies estimated the memorability of an advertisement independent from the response bias. Abdelhamid et al. [1] applied SDT to safeguarding of construction workers from occupational hazards. The worker <sup>b</sup>at the edge<sup>Q</sup>, that is, on the boundary of safe and unsafe condition, had to identify the condition in which he/she is working. The SDT framework provided ways to provide training, which in turn helped workers in identifying the type of condition in which he/she was working. Recently, Barkan [2] used SDT to investigate managerial decision making in discriminating hazardous and secure cues in the environment. This study suggested ways to reduce risky behavior on the part of managers.

Studies discussed thus far largely used experimental data and used the SDT framework to investigate research questions. However, SDT framework has also been applied to analytically investigate phenomena where empirical data is scarce or unavailable. For example, Sorkin and Dai [20] analyzed efficiency and detection performance of group decisions. This study derived theorems based on SDT for the behavior of an ideal group. The purpose was to achieve the highest detection performance for a group wherein each member has certain detection capability. The paper also discussed application of these theorems to juries and committees. Deshmukh et al. [6] analyzed efficiency and effectiveness of auditing to detect management fraud. The authors used SDT to evaluate the ability of an audit to detect fraud and costs incurred due to limitations of such detection ability.

## 2.2. SDT and filtering software

The objective of filtering software is to block unacceptable websites from the user.<sup>3</sup> Hence, the decision rule for filtering software should ideally allow the viewing of all acceptable websites and reject all the unacceptable websites. Filtering software in use today applies a variety of techniques to distinguish between acceptable and unacceptable websites. Four commonly used techniques are: platform for Internet content selection (PICS), uniform resource locator (URL) blocking, keyword filtering, and intelligent analysis of the website content [9,12].

World Wide Web consortium created a set of specifications that can be used to construct a platform for content rating systems. Web publishers can associate labels or metadata with their web pages to identify the nature of the website. However, PICS is not mandatory and mislabeling of websites is possible. URL blocking works by comparing URLs with a database of unacceptable URLs and then, by denying access to URL for which there is a match in the database. Another variation of this method is to allow access only to acceptable websites. Keyword filtering works by comparing words and phrases on a web page with a keyword dictionary of prohibited words and phrases. If a match is found, then the web site is blocked. Intelligent content analysis, on the other hand, strives to achieve a semantic understanding of the context of the words and phrases on the web pages. Statistical methods are then applied to into acceptable and unacceptable categories.

Irrespective of the approach used, all software filters operate on the following basic properties [9]. First, it should reject or filter unacceptable websites. Second, it should not reject or filter acceptable websites. Third, it should be difficult for the users to bypass and disable the software. Finally, the filtering software should track and record usage of the machine. It is imperative that filtering software attempt to balance these, often conflicting, objectives.

The first two properties are important for the application of the SDT framework while the other properties, though important, are outside the scope of this study. The first property-blocking of unacceptable websites corresponds to our definition of hit. The second property-blocking of acceptable websites corresponds to our definition of false alarm.<sup>5</sup> Not surprisingly, empirical studies indicate that no software filter has perfect hit rates and zero false alarms rates.<sup>6</sup>

Empirical tests to evaluate the performance of filtering have been inconclusive and provide wide ranging estimates of error rates. For example, Kranich [11] indicated that under real-world conditions software filters have a hit rate of 75% and false alarm rate of 20%. In other studies [3,9,16,17], hit rates varied from 50% to 90% and false alarm rates varied from 1% to 50%, depending on the configurations of the software filter. Consumer Reports (2005) recently reported that hit rates and false alarm rates vary based on the type of unacceptable sites, for example, filters are better in blocking the pornographic websites as compared to hate, illegal drug, and violence type websites. The primary methodological problem with the empirical studies is in choosing the sample data set and configuring the filtering software [16]. In the absence of complete index of the Internet websites, these studies constructed their own sample sets and used different software configurations causing wide variation in results. Resnick et al. [16] noted that methodology of evaluating a website has improved but significant concerns still remain.

Filter performance statistics are not surprising considering the complexity of the signal detection problem. Unacceptable websites often mimic legitimate websites and many legitimate websites contain information that can be mistaken as content for an unacceptable website. Unacceptable websites also actively strive to evade or deceive the filtering software. For example, a simple approach to evade the filters is to add keywords to the site that will bias the results of the filter. A major assumption of the SDT framework that distributions of signal and noise overlap is clearly satisfied in this context.

## 3. Performance analysis of software filters

## 3.1. Simple software filters

First, let us assume that the software is based on a single method of filtering. Most filters are of this type based on one of the methods discussed in Section 2.1 (e.g., URL blocking). The decision matrix for the simple filter is shown in Fig. 5. The possible outcomes are as follows: (1) the software filter signals unacceptable website when the website is unacceptable (hit), (2) the software filter signals acceptable website when the website is unacceptable (miss), (3) the software filter signals unacceptable website when the website is acceptable (false alarm), 4) the software filter signals acceptable website when the website is acceptable (correct identification).

The decision matrix in Fig. 5 can be summarized using hit rates and false alarm rates. For example, $1 - P r \ ( U ^ { \prime } \mid U ) { = } P r \ ( A ^ { \prime } \mid U )$ and $1 - P r \ ( U ^ { \prime } \mid A ) = P r$ $( A ^ { \prime } \mid A ) .$ . The conditional probabilities $P r \left( U ^ { \prime } \mid U \right)$ and $P r \ ( U ^ { \prime } \mid A )$ represent hit rates and false alarm rates and can then be used to analyze the effectiveness and efficiency of the software filter. The term effectiveness is related to the hit rates and indicates successful discrimination among websites. The term efficiency is related to the ability of the software filter to minimize false alarm rates. If the hit rates $\left( P r \left( U ^ { \prime } \mid U \right) \right)$ and false alarm rates $\left( P r \ \left( U ^ { \prime } \mid A \right) \right)$ are close to 0.5 then software filter is as good as random chance. The effectiveness increases as hit rates get closer to 1 and the efficiency increases as false alarm rates move toward 0.

As mentioned earlier, in the SDT framework, the decision maker uses hit rates and false alarm rates to calculate the likelihood ratio (LR). This ratio captures the likelihood that a particular website is unacceptable relative to the likelihood that the same website is acceptable. The likelihood ratio is given by,

$$
\mathrm{LR} = \frac {P r (U ^ {\prime} | U)}{P r (U ^ {\prime} | A)}.\tag{5}
$$

The calculated value of LR is then compared with the fixed criterion value $\mathrm { o f } ^ { 6 6 } \alpha ^ { \mathrm { \mathfrak { p } } }$ . The decision rule used is as follows: if $\mathrm { L R } \geq \alpha$ then classify the website as unacceptable and if LR <sup>b</sup> a then classify the website as acceptable. The criterion value a incorporates the payoffs associated with the decisions of the software filter and the prior probabilities of occurrence of unacceptable websites in the population. Eq. (4) shows the calculation of the criterion value in the

<table><tr><td></td><td>Unacceptable (U*)</td><td>Acceptable (A&#x27;)</td></tr><tr><td>Unacceptable (U)</td><td>Pr (U*| U)Hit Rate</td><td>Pr (A*| U)Miss Rate</td></tr><tr><td>Acceptable (A)</td><td>Pr (U*| A)False Alarm Rate</td><td>Pr (A*| A)Correct Identification</td></tr></table>

Fig. 5. Decision matrix for one software filter.

SDT framework, and is used here to calculate the criterion value.

$$
\alpha = \frac {P r (A)}{P r (U)} \times \frac {\left(B _ {A ^ {\prime} A} - C _ {U ^ {\prime} A}\right)}{\left(B _ {U ^ {\prime} U} - C _ {A ^ {\prime} U}\right)}.\tag{6}
$$

In Eq. (6), $B _ { A ^ { \prime } A }$ is the benefit gained by accepting acceptable website, $C _ { U ^ { \prime } A }$ is the cost incurred by identifying acceptable website as unacceptable, $B _ { U ^ { \prime } U }$ is the benefit gained by identifying unacceptable website as unacceptable, and $C _ { A ^ { \prime } U }$ is the cost incurred due to accepting an unacceptable website,. The prior probabilities of acceptable and unacceptable sites in the population are represented by Pr (A) and Pr (U), respectively.

As suggested earlier, the decision of the software filter is based on criterion value of <sup>b</sup>a<sup>Q</sup>. An increase in the value of a will decrease the false alarm rates and decrease in the value of a will decrease miss rates. If the signals generated by software filter are perfectly diagnostic then both the false alarm rates and miss rates can be eliminated. But as empirical evidence suggests software filters are not perfectly diagnostic. The relatively low base rates of unacceptable web sites in the population also have implications for the effectiveness and efficiency of the software filter. The software filter should enable us to make better deci sions than by simply assuming that all accounts belong to the category with the highest base rates. However, this decision making is complicated due to the costs of false alarm rates and misses. Eqs. (5) and (6) can be used to analyze the relationships between payoffs, base rates, and miss and false alarm rates of the software filter.

Unfortunately, estimates regarding base rates of unacceptable sites in the population are sketchy. Kranich [11] estimates that only about 1.5% of Internet websites are pornographic in nature. However, if the definition of unacceptable websites is broadened then this percentage may be higher but on the other hand, if the definition is more restrictive the value may be lower. For the purposes of this study, we assume the rates of unacceptable websites in the population vary between 1% and 10%. Interestingly, even such a wide range does not alter the basic conclusions of the study.

The next question is how to quantify the payoffs associated with different decisions? This study assumes that benefits associated with correct acceptance and correct rejection are approximately equal. The major difference is in the costs associated with the miss rates and false alarm rates. The primary concern in the literature is with the rejection of acceptable websites and acceptance of unacceptable websites by the filtering software [9,11,15,16]. The rejection of legitimate websites results in violation of first amendment rights of library patrons and also denies access to many health sites for the poorer sections of the society. On the other hand, costs associated with miss rates include disciplinary actions taken by the government against libraries which might include loss of federal funding. The costs of miss rates are more costly for most libraries. Also, for other users such as parents and businesses, costs associated with miss rates of the software are relatively more important than costs associated with the false alarm rates. This study assumes various levels of costs associated with miss and false alarm rates. The first analysis is done where these costs are assumed to be equal. However, additional analysis is also carried out with the costs associated with miss rates assumed to be 10 and 100 times more than the costs associated with false alarm rates.

Various scenarios for miss rates, costs associated with miss rates and false alarm rates, and base rates of unacceptable websites in the population are presented in Table 1. The first column indicates various levels of unacceptable websites in the population, which are assumed to be 1%, 5%, and 10% for analytical purposes. As mentioned earlier, estimates of unacceptable websites vary but are well within the ranges considered in Table 1. The second column indicates prior odds associated with these levels (Pr (A) / Pr (U)). The third column is the likelihood ratio that is calculated based on the values in column four. In column four, the first three rows’ costs associated with miss rates are assumed to be equal to the costs associated with false alarm rates. Then, the costs of miss rates are assumed to be 10 and 100 times more than costs of false alarm rates. Columns five through eight indicate the permissible levels of false alarm rates for correct decision making. In column five, Pr $( U ^ { \prime } \mid U )$ is assumed to be 1, that is, the hit rate is 100%; the software filter is perfect when it comes to identifying unacceptable websites. Then this rate is changed to 0.95, 0.90, and 0.85, respectively. The last four columns of Table 1 show various values of Pr $( U ^ { \prime } \mid A )$ (maximum permissible false alarm rates for correct decision making). The calculation of maximum permissible rates is done by rearranging Eqs. (3) and (4). The rearranged equations are given below.

Table 1  
Calculation of maximum permissible false alarm rates

<table><tr><td>Base rates (%)</td><td>Prior odds</td><td>Likelihood ratio</td><td> $(B_{A'A} - C_{U'A}) / (B_{U'U} - C_{A'U})$ </td><td>Pr  $(U' | U)=1$ </td><td>Pr  $(U' | U)=0.95$ </td><td>Pr  $(U' | U)=0.90$ </td><td>Pr  $(U' | U)=0.85$ </td></tr><tr><td>1</td><td>99:1</td><td>99</td><td>1</td><td>0.0101010</td><td>0.0095960</td><td>0.0090909</td><td>0.0085859</td></tr><tr><td>5</td><td>19:1</td><td>19</td><td>1</td><td>0.0105263</td><td>0.0100000</td><td>0.0094737</td><td>0.0089474</td></tr><tr><td>10</td><td>9:1</td><td>9</td><td>1</td><td>0.0111111</td><td>0.0105556</td><td>0.0100000</td><td>0.0094444</td></tr><tr><td>1</td><td>99:1</td><td>9.9</td><td>1/10</td><td>0.0010101</td><td>0.0009596</td><td>0.0009091</td><td>0.0008586</td></tr><tr><td>5</td><td>19:1</td><td>1.9</td><td>1/10</td><td>0.0010526</td><td>0.0010000</td><td>0.0009474</td><td>0.0008947</td></tr><tr><td>10</td><td>9:1</td><td>0.9</td><td>1/10</td><td>0.0011111</td><td>0.0010556</td><td>0.0010000</td><td>0.0009444</td></tr><tr><td>1</td><td>99:1</td><td>0.99</td><td>1/100</td><td>0.0001010</td><td>0.0000960</td><td>0.0000909</td><td>0.0000859</td></tr><tr><td>5</td><td>19:1</td><td>0.19</td><td>1/100</td><td>0.0001053</td><td>0.0001000</td><td>0.0000947</td><td>0.0000895</td></tr><tr><td>10</td><td>9:1</td><td>0.09</td><td>1/100</td><td>0.0001111</td><td>0.0001056</td><td>0.0001000</td><td>0.0000944</td></tr></table>

LR<sub>z</sub>a

$$
\frac {P r (U ^ {\prime} \mid U)}{P r (U ^ {\prime} \mid A)} \geq \frac {P r (A)}{P r (U)} \times \frac {(B _ {A ^ {\prime} A} - C _ {U ^ {\prime} A})}{(B _ {U ^ {\prime} U} - C _ {A ^ {\prime} U})}\tag{7}
$$

$$
P r (U ^ {\prime} \mid A) \leq \frac {P r (U ^ {\prime} \mid U)}{\frac {P r (A)}{P r (U)} \times \frac {(B _ {A ^ {\prime} A} - C _ {U ^ {\prime} A})}{(B _ {U ^ {\prime} U} - C _ {A ^ {\prime} U})}}.\tag{8}
$$

If we assume the costs associated with miss rates and false alarm rates are equal then the expression $( B _ { A ^ { \prime } A } - C _ { U ^ { \prime } A } ) / ( B _ { U ^ { \prime } U } - C _ { A ^ { \prime } U } )$ will approximately equal unity. Then the relationship between hit rates, miss rates, and decisions of the software filter can be explored as follows. First, the likelihood ratio is calculated, which is now based on the base rates of unacceptable websites in the population. The three levels of base rates considered are 1%, 5%, and 10%. The likelihood ratio or a is 99, 19, and 9 in these three cases, respectively.

The maximum permissible false alarm rates when the base rate of unacceptable websites is 1% varies from 0.01 to 0.008 depending on the hit rate of the software filter. Even if the hit rate is 100% the permissible false alarm rate is still 0.01 or 1%, which becomes smaller as hit rate decreases. As the base rates increase to 5% and 10% the permissible false alarm rate increases by a small margin. The upper bound of permissible false alarm rates is 0.011 or 1.1%. Thus, the required false alarm rate necessary to not reject the acceptable websites is extremely low.

As the cost associated with miss rates increases relative to the cost associated with false alarm rates, the permissible false alarm rates continues to decline. For example, if the cost of miss rates is 10 times more than the cost of false alarm rates, the likelihood ratio falls to 9.9, 1.9, and 0.9 for 1%, 5%, and 10% base rates, respectively. The maximum permissible false alarm rates now are 1/10 of the earlier case where the costs of miss rate and false alarm rates are considered equal. The maximum upper bound for permissible false alarm rates is now 0.0011 or 0.11%.

The same pattern is repeated in the analysis where costs associated with miss rates are assumed to be 100 times of costs associated with false alarm rates. The maximum permissible false alarm rates are now 1/100 of the first case. The likelihood ratio now falls to 0.99, 0.19, and 0.09 for 1%, 5%, and 10% base rates, respectively. The maximum permissible false alarm rates now are extremely low. The upper bound for permissible false alarm rates is now 0.00011 or 0.011%.

What happens when the software filters cannot maintain such extremely low false alarm rates? As the costs of miss rates continue to go up, the software filter is forced to reject acceptable websites due to higher than permissible false alarm rates. Even if the software filter is 100% effective, it cannot be efficient due to the requirement that false alarm rates be extremely low. So the software filter can be used to reject the unacceptable websites but in the process the software filter will always reject acceptable websites. Since the socio-political process determines the costs associated with misses and false alarm rates, the issue is less about the technical underpinnings of filtering but more about social and political dimensions.

## 3.2. Multi-method software filters

Here, we refer to multi-method software filters as those that apply more than one technique (e.g., URL blocking and intelligent analysis of website content based blocking) to evaluate the same websites. The technical and cost considerations of such a filter in the real-world are beyond the scope of this study. Our focus is on the performance of such filters. Interestingly, evaluation using SDT provides somewhat different answers than the earlier analysis.

As shown in Fig. 6, now the filtering process is modeled as a sequence of n filters. It may be noted that the sequence does not preclude a website evaluated by method 1 to be evaluated by method 2 again. Each filter represents application of a new methodology to the same website. The prior odds and the likelihood ratio are modified based on the sequential signals. The primary assumption in this case is that the signals generated by each filter are statistically independent. Let us first assume that all signals are independent of each other and then relax this assumption.

As shown in Fig. 6, the prior odds that a certain site is unacceptable are modified by signal $\mathrm { S } _ { 1 }$ emanating from Filter 1. That results in a likelihood ratio that is given below.

$$
\begin{array}{l} \mathrm{LR} _ {1} = \frac {\operatorname* {P r} (U ^ {\prime} | U)}{\operatorname* {P r} (U ^ {\prime} | A)} \geq \frac {\operatorname* {P r} (A)}{\operatorname* {P r} (U)} \\ \times \frac {(B _ {A ^ {\prime} A} - C _ {U ^ {\prime} A})}{(B _ {U ^ {\prime} U} - C _ {A ^ {\prime} U})}, \text { or } \end{array}\tag{9}
$$

$$
\frac {P r (U ^ {\prime} \mid U)}{P r (U ^ {\prime} \mid A)} \times \frac {P r (U)}{P r (A)} \geq \frac {(B _ {A ^ {\prime} A} - C _ {U ^ {\prime} A})}{(B _ {U ^ {\prime} U} - C _ {A ^ {\prime} U})}.\tag{10}
$$

Then the left hand side of the Eq. (10) becomes the prior odds for the Filter 2. The prior odds keep getting modified through a sequence of n filters. After the sequence of n filters the Eq. (10) becomes:

$$
\prod_ {i = 1} ^ {i = n} \frac {P r (U _ {i} ^ {\prime} | U)}{P r (U _ {i} ^ {\prime} | A)} \times \frac {P r (U)}{P r (A)} \geq \frac {(B _ {A ^ {\prime} A} - C _ {U ^ {\prime} A})}{(B _ {U ^ {\prime} U} - C _ {A ^ {\prime} U})}.\tag{11}
$$

As in the earlier analysis, let us assume that the value of $( B _ { A ^ { \prime } A } - C _ { U ^ { \prime } A } ) / ( B _ { U ^ { \prime } U } - C _ { A ^ { \prime } U } )$ is equal to 1 and then it will be assumed to be less than 1. Now let us assume that the hit rate and false alarm rate for each filter is 75% and 25%, respectively, and the base rates of unacceptable websites are 1% (prior odds 1 : 99). If these numbers are substituted in the Eq. (9) then only five filters are required to make a correct decision. The calculations are as follows: (75 / 25) \* (75 / 25) \* (75 / 25)\*(75/25)\* (75/25)\*1% which is greater than 1.

![](/api/attachments/GA3UH9VQ/fulltext/images/9918e1d0672a9a721782cd9cfea3421c562f83c0f3780627980a8c5f48d73ffe.jpg)  
Fig. 6. Using a sequence of software filters.

If the hit rate is 80% and false alarm rate is 20% then only four filters are required to make a correct decision. Thus, a sequence of four or five independent software filters even with imperfect hit and false alarm rates can make a correct decision. As the costs associated with miss rates increase relative to costs associated with false alarm rates then the value of $( B _ { A ^ { \prime } A } - C _ { U ^ { \prime } A } ) /$ $( { \cal B } _ { U ^ { \prime } U } - { \cal C } _ { A ^ { \prime } U } )$ becomes less than 1. Then the required number of software filters to make correct decisions is less than (or at best equal to) five.

The hit rates (75%) and false alarm rates (25%) already exist in the real-world, as indicated by the empirical studies reviewed earlier [5,10,11]. However, the above results hold only if the statistical independence of software filters is achieved. If this condition is violated then the signals generated by each filter are correlated and there is a minimal or no increase in power after the first filter. In this case, the sequence of filters will behave as equivalent to one filter. Additionally, the correlation between hit rates and false alarm rates also needs to be evaluated separately. If the hit rates are correlated and false alarm rates are independent then the successive filters will reduce the likelihood ratio (and vice versa) resulting in an increased probability of an incorrect decision.

## 4. Discussion and conclusions

This study analytically explores the relationships among hit rates, false alarm rates, costs associated with hit and false alarm rates, and base rates of the unacceptable websites in the population. In general, the low base rate of unacceptable websites and higher costs associated with misses relative to costs associated with false alarm rates point to several limitations of filtering software.

The primary conclusion, when a simple software filter is used, is that even if the software filter has a 100% hit rate, it needs extremely low level of false alarm rates; levels, arguably, practically unachievable in many cases. As the costs associated with miss rates escalate the required level of false alarm rates becomes even lower. Additionally, as the hit rates decline the required level of false alarm rates also declines. The maximum permissible false alarm rate for correct decision making under the most liberal conditions is 1.1%. In the real-world, the hit rates of software filters are measured up to 90% (but can be as low as 50%) and the false alarm rates can be 25% or more. Costs associated with misses are increasing due to legislation and wide use of filters by parents and businesses. As such the software filters need a very low level of false alarm rates to make correct decisions.

The actual false alarm rates for the software filters are higher than the theoretical limits. As such, software filters will continue to reject acceptable websites at a higher rate. Kranich [11] indicate that potentially 600 million acceptable websites can be rejected by the software filters. However, as this study demonstrates, the issue is not technical. In an extremely dynamic environment such as the Internet, it is very difficult for software filters to achieve extremely low level of false alarm rates. In essence, we conclude that single software filters on their own are severely limited in their ability to deliver high performance in providing access to information and blocking inappropriate content.

An alternative suggested by the SDT framework as a better approach is the use of a multi-method based software filters. If the software filters are statistically independent, then even with 75% hit rate and 25% false alarm rate, a sequence of five software filters can lead to highly accurate website classification. These hit rates (75%) and false alarm rates (25%) are already achieved by the filters in the real-world. The design of the existing software filters can be improved using these results. First, a software filter can employ more than one method to evaluate the given website. Second, the software vendors can focus on developing independent or partially independent algorithms that can be employed concurrently or in parallel. Finally, the vendors can provide information concerning the algorithms used in the filters. Then the users can employ two or more software filters that employ different algorithms that may yield better results. Future research can empirically evaluate the value of multiple-method filters.

Software filters are still quite useful in the business and family environment, since violation of rights is not an issue [18,26]. The false alarm rates or rejection of acceptable websites is also not much of a problem. Any website that is really needed can be made available by the system administrator or parent. The same line of reasoning was used by the Supreme Court in mandating software filters for libraries [11]. However, the librarians felt that honoring such requests may take unreasonable time and defeat the purpose of libraries. As such, the use of software filters in libraries does pose a problem. Such use may lead to violation of library patrons’ rights or severely restrict students from accessing necessary information. The answer is social and political in nature, since each group must decide what is important. Our analysis also supports often repeated assertion that the debate should be regarding values, education, and parental involvement. Software filter is not a fix and forget type solution.

The analysis in this study has some limitations. First, the base rates of unacceptable websites are assumed to range up to 10%. Empirical evidence of total number of unacceptable websites is conflicting and unreliable; however, the upper end of our range is higher than that of any empirical study. Second, the claim that multi-method filters are more accurate depends on the statistical independence of these filters. However, the statistical independence or dependence among various software filters cannot be empirically verified. Third, the filtering software can learn over time and improve effectiveness. If the learning algorithms are effective then the software can improve hit rates and minimize false alarm rates. Such learning is not addressed in this paper. We believe the conclusions of this study, in spite of these limitations, are useful in studying the efficacy of the software filters.

## References

[1] T.S. Abdelhamid, B. Patel, G.A. Howell, P. Mitropoulos, Signal detection theory: enabling work near the edge, Proceedings of the 11th Annual Conference for Lean Construction, Blacksburg, Virginia, 2003, pp. 243– 256.

[2] R. Barkan, Using a signal detection safety model to simulate managerial expectations and supervisory feedback, Organizational Behavior and Human Decision Processes 89 (2002) 1005– 1031.

[3] Consumer Reports, Filtering software: better but still fallible, 70, 6 (June 2005), 36–38.

[4] D. Cradit, A. Tashchian, F. Hofacker, Signal detection theory and single observation designs: methods and indices for advertising recognition testing, Journal of Marketing Research (1994 (February)) 117–127.

[5] D.R. Davis, R. Parasuraman, The Psychology of Vigilance, Academic Press, London, 1982.

[6] A. Deshmukh, K. Karim, P. Siegel, An analysis of efficiency

and effectiveness of auditing to detect management fraud: a signal detection theory approach, International Journal of Auditing 2 (2) (1998) 127–138.

[7] G. Gigerenzer, Z. Swijtink, T. Porter, L. Daston, J. Beatty, L. Kruger, The Empire of Chance: How Probability Changed Science and Everyday Life, Cambridge University Press, Cambridge, UK, 1989.

[8] M. Green, A. Swets, Signal Detection Theory and Psychophysics, Wiley, New York, NY, 1966 (Reprinted in 1988, Los Altos, CA, Peninsula Publishers).

[9] P. Greenfield, R. Rickwood, H. Tran, Effectiveness of Internet filtering software products, CSIRO Mathematical and Information Sciences, (2001), Retrieved on September 23, 2004 from http://www.aba.gov.au/internet/research/filtering/ filtereffectiveness.pdf.

[10] A. Hanley, The robustness of the <sup>b</sup>binormal<sup>Q</sup> assumptions in fitting ROC curves, Medical Decision Making 8 (1988) 197– 203.

[11] N. Kranich, Why filters won’t protect children or adults, Library Administration and Management 18 (1) (2004) 14– 18.

[12] P. Lee, S. Hui, A. Fong, A structural and content-based analysis for web filtering, Internet Research 13 (1) (2003) 27– 37.

[13] R. McFall, T. Treat, Quantifying the information value of clinical assessments with signal detection theory, Annual Review of Psychology 50 (1999) 215– 241.

[14] J. Neyman, E.S. Pearson, On the problem of the most efficient tests of statistical hypotheses, Philosophical Transactions of the Royal Society of London, Series A 231 (1933) 289– 337.

[15] N. Oder, Filter study: settings matter, Library Journal 128 (1) (2003) 20.

[16] P. Resnick, D. Hansen, C. Richardson, Calculating error rates for filtering software, Communications of the ACM 47 (9) (2004) 67– 71.

[17] C. Richardson, P. Resnick, D. Hansen, A. Derry, Does pornography-blocking software block access to health information on the Internet? Journal of American Medical Association 22 (2002) 2887– 2894.

[18] C. Simmers, Aligning internet usage with business priorities, Communications of the ACM 45 (1) (2002) 71–74.

[19] N. Singh, A. Churchill, Using the theory of signal detection to improve ad recognition testing, Journal of Marketing Research (1986 (November)) 327– 336.

[20] D. Sorkin, H. Dai, Signal detection analysis of the ideal group, Organizational Behavior and Human Decision Processes 60 (1994) 1 – 13.

[21] H. Stanislaw, Effect of type of task and number of inspectors on performance of an industrial inspection type task, Human Factors 37 (1996) 182– 192.

[22] H. Stanislaw, N. Todorov, Calculation of signal detection theory measures, Behavior Research Methods, Instruments, and Computers 31 (1) (1999) 137– 149.

[23] N. Swartz, Should libraries censor patrons’ surfing? Information Management Journal 37 (3) (2003) 6.

[24] A. Swets, ROC analysis applied to the evaluation of medical imaging techniques, Investigative Radiology 14 (2) (1979) 203– 206.

[25] A. Swets, M. Picketts, Evaluation of Diagnostic Systems: Methods from Signal Detection Theory, Academic Press, New York, NY, 1982.

[26] A. Urbaczewski, L. Jessup, Does electronic monitoring of employee internet usage work? Communications of the ACM 45 (1) (2002) 80– 83.

[27] T. Wickens, Elementary Signal Detection Theory, Oxford University Press, New York, NY, 2002.

Dr. Ashutosh Deshmukh is an Associate Professor of Accounting and Information Systems at Pennsylvania State University-Erie. His research and teaching interests are in accounting information systems and auditing. He has published over 20 articles and made numerous conference presentations in the areas of accounting information systems and auditing. He is a Chartered Accountant, Certified Information Systems Auditor, and Certified Fraud Examiner; and has practical experience in public and industrial accounting.

Dr. Balaji Rajagopalan is an Associate Professor of Management Information Systems and Director of the Executive MBA program at Oakland University. His research has been published or accepted in IEEE Transactions on Systems Man and Cybernetics, Journal of Database Management, European Journal of Operational Research, Communications of the ACM, Decision Support Systems and Journal of Medical Systems. Along with two co-principal investigators he was recently awarded a three year National Science Foundation grant for \$500,000.
