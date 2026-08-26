---
otero_id: 18004
otero_key: "3VN2FUGT"
title: "Towards better software management through careful analysis of current application systems"
authors: "Ari Heiskanen; Jaana Helanterä"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90024-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards Better Software Management Through Careful Analysis of Current Application Systems

Ari Heiskanen
Everstinkuja 5 C 72, SF-02600 Espoo 60, Finland

and

Jaana Helanterä

Department of Computer Science, University of Helsinki, Tukholmankatu 2, SF-00250 Helsinki 25, Finland

Results are reported of empirical investigations into EDP applications in use. A model for connecting terms of the users of the applications to the consumed hardware resources is proposed. The properties of so-called “application profiling” are studied. Discussions are based on thorough analyses of a few EDP applications and one of them is abridged as a case study.

Keywords: software engineering, software measurements, application profiling, efficiency of EDP applications, EDP education

![](/api/attachments/3VN2FUGT/fulltext/images/b1aaa1bfce8d9f1821a3f9243b1aad97c3aaeed1db41541d3f83b733110240aa.jpg)

Ari Heiskanen is now working in the central government of the University of Helsinki where he is in charge of the development of the software of the new student information system. He was several year in the Department of Computer Science of the University of Helsinki where he gained the Ph.Lic. degree in 1980. He is interested in various measurable properties of application systems in use and is preparing a doctoral dissertation on this subject.

## 1. Introduction

Recent lively discussions on software engineering have mainly concentrated on the problems of system construction and software maintenance (see, e.g., [11]). This is reasonable, because it is evident that the most stringent problems in software engineering are in this area. However, one should not underestimate the importance of the analysis of the hardware resource requirements of the software which is under construction or in use. This hardware resource engineering, a part of the capacity planning process of computer installations, has a close relationship to application management because of the continuously growing hardware resource requirements of the applications [3].

The cost of human work is not yet so high that it prohibits the careful planning of effective hardware systems or the sensible tuning of existing application software in order to reduce the hardware costs. McNeece [10] suggests that every major application (where major application is defined as one that takes more than 10% of the total hardware resources of the installation) deserves a detailed analysis of its resource usage. Waldbaum [13] reports about considerable savings from a project where the CPU usage of application programs was analysed and diminished by some quite straightforward operations.

![](/api/attachments/3VN2FUGT/fulltext/images/31c9c15bf6e08a14e5e75dab3119415e14fd46d11a2c25bf8943306de7612111.jpg)  
Jaana Helanterä graduated from the Department of Computer Science of the University of Helsinki in 1981. She is now in the Finnish State Computing Centre where she is working with a data-entry system for library information using the Finnish minicomputer MIKKO.

These kinds of ideas are being used in practice in several Finnish EDP organizations in order to cut down the excessive hardware resource consumption of critical applications. An insurance company, for example, was able to reduce the running time of an application program by 90% through a slight rearrangement of the program and the disk files it used.

The means of making this improvement were found in a careful analysis of the program behaviour. The reason for the inefficiency of the program was in its file usage. It placed three kinds of records (A, B, and C) into consecutive disk locations. In the construction phase, the physical order of the records was thought to be unimportant. However, over the years the number of B records increased substantially, and so the physical distance between A and C records became large. It was found that most of the time the program needed A and C records together. Thus quite a large number of unnecessarily long disk seeks were eliminated when A and C records were placed near each other.

The reason for the inefficiency was quite trivial in this case, but the explanation required analysis of disk file references. This kind of tuning is a database administrator's duty when database management software is used, but with non-database applications, the physical efficiency easily remains nobody's responsibility - it is thus neglected.

The tools used in the analyses of system's behaviour have traditionally been hardware and software monitors. In this paper, we provide out opinion that (in addition to these methods) it is reasonable to construct the application so that the software itself collects data about the hardware resource usage.

We summarize here our experience in the CAASU (Careful Analysis of Application Systems in Use) project. This project was started by the

Department of Computer Science at the University of Helsinki in 1978. Two to three researchers were the major staff of the project; they were also supported by several undergraduate students. The work was done in collaboration with several Finnish EDP organizations, the main supporter being the Finnish State Computer Centre.

The project was started with rather indefinite objectives. We began with an indepth study of the operations of some of the EDP applications. During this period, it was concluded that, by investigating running EDP systems, we could accomplish at least the following objectives:

1. Obtain empirical material to be used in the curriculum of the Department of Computer Science;

2. Develop methods in the description and analysis of EDP applications;

3. Develop methods for the efficient use of control information gathered during the normal use of application software;

4. Analyse the possibility of tuning the existing application software for better performance; and

5. Achieve improvement in the co-operation of the different groups working with information systems.

Detailed analyses are too lengthy to be presented here, but a short case will be described in section 4.

## 2. The Transfer of Craftsmanship

The need to transfer experience from practitioners to students is obvious – and computer science is no exception [2]. Such transfer at the University of Helsinki is being promoted in two ways: (i) students working on our project get a close picture of real systems, and (ii) others are able to read the comprehensive reports and obtain up-to-date descriptions of the systems which have been produced as a basis for our analyses.

We have obtained positive results by using this kind of teaching material in several of our courses. The principal advantages over the use of traditional documentation are that: the texts are more readable; students can concentrate on important features and omit insignificant details; the material contains practical experience of the use of the documented system; and the reports discuss possible pitfalls in the design (these are seldom recorded in traditional documentation).

Case studies of EDP applications in periodicals (see e.g. [6,8,9]) give good summaries, but they are too short to be used in teaching the architecture of the systems. The descriptions produced by CAASU fall somewhere between these case studies and the traditional documentation that is produced for the purpose of maintenance, etc.

Starting with documentation is natural. In many organizations, documentation is neglected. Students participating in the CAASU project helped to provide descriptions of important applications with minimal expenditure of resources by the organizations. From our point of view, the preparation of readable documentation was the first phase in the investigation; it was found impractical to work with the standard documentation.

The work was performed in groups of two to three undergraduate students. Each group got acquainted to a system and typically produced a description 200 to 300 pages in length. Each student spent 300 to 400 working hours just prior to starting a master's thesis. The systems were of moderate size (10000 to 50000 lines of source code) and the application areas varied from the text processing system of a major Finnish Newspaper Publisher to several Social Wellfare systems run by the government. Several students continued the work as a basis for their masters' theses. Many of the theses proved useful, and contained suggestions for practical improvement of the systems.

## 3. Who Should Bother With Computer Usage?

We divide the people concerned with EDP application into three different categories:

1. The users of the application.

2. The people who run and maintain the application (the application administrators).

3. The people that operate and manage the computer on which the system is run (the computer resource administrators).

The users see the application system as a black box. The user is very seldom interested in knowing the amount of CPU usage or memory occupation but mainly sees the cost. To the user, the resource usage is best expressed in the cost as a function of the volume of inputs and outputs. These are called key volume indicators [12], natural business units [1] or natural forecast units [3].

The users are most of all interested in “effectiveness” [5]. This involves the effects on, benefits of, or disadvantages to the environment. The money by which the computer installation is run comes ultimately from the users as payment for services, and thus the users must be interested in cost-effective applications. However, the users are not in a good position to judge whether the application software is properly designed.

The application system administrator knows the technical details of the application, is in charge of the production runs of the system, and takes care of the routine maintenance of software. Using Bronner's [3] terminology: he has the responsibility of application management and he is the best person to analyse the resource consumption.

Resource requirements should be estimated throughout the life cycle. But often estimates are based on imprecise information about anticipated usage. During the operational phase, it is possible to gather statistics about real inputs, and the internal structure of the system (file organization, access paths, ...) can sometimes be optimized for the changed environment. Such changes are difficult or impossible to predict in the planning phase, and so flexibility of application software is essential for long-life systems. The “tailor-made” programs of traditional applications are not generally easy to tune, yet there is nearly always potential for improvement.

The computer resource administrator considers all the applications as a workload and is very seldom aware of the architecture of the applications. The computer equipment and operating system can be tuned to remove bottlenecks, but application software tuning is outside the scope of this work. The computer resource administrator can use precise models of the major applications in forecasting requirements for installation resources, but producing these models is the application administrator's responsibility.

The need of a simple and reliable method to accomplish the connection of the resource usage of an application and the terms that are understandable to the user is urgent (see [7]). There are numerous complaints that charging the users according to the consumed hardware resources leads to unpredictable and disadvantageous costs to the users. The tendency towards a charging scheme that contains only terms in the user's realm is obvious, e.g. the current payroll application of the Finnish State Offices and Hospitals (run by the State Computer Centre) bills back according to the number of pay-slips, etc., while older version of the same application charged according to the consumed hardware resources as measured by the operating system.

Howard [7] advocates the use of standard costing at the computer installation level. We present a simple procedure to connect user terms to the usage of computer components; it is a modification of the application profiling approach described by Artis [1] and Sarna [12].

There are some problems in the use of application profiling. Artis [1] mentions that a model based only on historical data may be quite insensitive to some essential predictor variables; e.g. the number of records in the main file. This occurs because there is not enough variation among the values of the variables in the data. The predictor behaves like a constant and this hides its effects on the model (as obtained through regression analysis). Another problem with application profiling is general in regression analysis: iterating to the final regression model and interpreting its coefficients presuppose thorough familiarity with the modeled phenomenon.

## 4. The Student Information System of the University of Helsinki

The student information system (SISUH) is a traditional batch oriented application, which contains data on the students' background and progress. SISUH produces various reports and statistics required by the government of the University, Ministry of Education, and student organizations.

The main file is divided in two parts. ACTRE (the register of active students) contains records of those students that are actively pursuing their studies, and REMRE is the register of ex-students. There are about 26000 records in ACTRE and 27000 in REMRE. Both files contain records of the same fixed length (about 1000 bytes). SISUH has about twenty programs (40000 lines of source code). Most of the programs are written in COBOL. SISUH is run on the Burroughs B6700 computer in the Computing Centre of the University.

![](/api/attachments/3VN2FUGT/fulltext/images/ec2aa58ae1afb21b6341f9894e0e367c46a8736e1f923d647c243be64ab28d3f.jpg)  
Fig. 1. The System Flowchart of the UPDATER program.

We present here the results of the analysis of a major program of SISUH. This program is one of the two that update the main file, descriptively called the UPDATER (see fig. 1).

In the case of SISUH and UPDATER there are three natural business units: the number of records in ACTRE and REMRE, and the number of transaction records. These quantities are pertinent to the solution of the following two questions of cost-effectiveness:

How often should the UPDATER be run? (i.e. how big a batch of transaction records is needed);

How much does it cost to keep old records in REMRE instead of removing them into an archive file?

The charging formula of B6700 entails CPU usage, IO time, the use of main memory, the number of printed lines, and the on-line terminal connect time. In the case of UPDATER, only the CPU and IO time appeared to be relevant; they were therefore selected as the dependent variables in our models.

There were two phases of regression analysis. The first (almost a paper and pencil study) assumed that dependent variables were dependent on only one natural business unit: the number of transaction records. The second was a comprehensive investigation using stepwise multiple regression analysis with several independent variables among which a good predictor was sought. The first study was included because of its simplicity.

The results of the first study are presented in figure 2. It can be seen that there is substantial variation in the number of transaction records in the historical data upon which the regression is based. However, the explanation power (multiple correlation coefficient squared) of the regression equations is poor. Obviously, other factors than the number of transactions dominate the consumption of resources, especially as far as the IO time is concerned. But in spite of the fact that the results of the regression analysis are not very reliable, they can be used as rough estimates.

As already stated, a problem in the use of regression analysis is that the models may be insensitive to some essential variables that had only small variation during the experiment. This occurred in our work: the number of records in ACTRE and REMRE are nearly constant. There is another problem: the natural business units (chosen as variables in the model) may be strongly correlated. This brings about unfavourable redundancy. In our case there is dependence between the number of records in the two main files: almost all of the records removed from ACTRE are added to REMRE. In other situations there may be different correlations: e.g. the number of printed lines may depend on the number of transactions.

The best model we could obtain by multiple stepwise regression analysis is shown in eqs. (1) and (2). The original set of variables was at first larger (e.g., containing the number of printed lines and the number of records in several auxiliary files). The final model was obtained through iteration where the number of variables was reduced and new, transformed variables were made by adding some old ones together. Several outliers were identified and found to be caused by abnormal runs, e.g. program errors. These were removed from the data that finally consisted of sixty normal production runs. The residuals obeyed sufficiently normal distribution and showed no apparent defects in the models for CPU and IO time:

$$
\begin{array}{r l} \text {CPU - TIME} & = 0. 0 1 4 N _ {\mathrm{T}} \\ & + 0. 0 0 2 9 (N _ {\mathrm{A}} + N _ {\mathrm{R}}) [ \text {seconds} ] \end{array}\tag{1}
$$

Explanation power: 0.991; standard deviation of the regression coefficients: 0.001 and 0.00006

$$
\text { IO - TIME } = 0. 0 2 3 N _ {\mathrm{T}} + 0. 0 2 4 (N _ {\mathrm{A}} + N _ {\mathrm{R}}) [ \text { seconds } ]\tag{2}
$$

Explanation power: 0.999; standard deviation of the regression coefficients: 0.003 and 0.0002.

$N_{T}$ is the number of transaction records; $N_{A}$ and $N_{R}$ denote the number of records in ACTRE and REMRE.

We forced the constant term of the model to be zero, because the interpretation of a negative constant term would have been impossible in terms of the real world. However, nearly all intermediate phases produced models with a negative constant.

The models (1) and (2) can easily be explained, but they are unable to show the reasons for CPU and IO time usage, i.e. where and why the computing resources are spent when processing transactions and producing outputs.

A better understanding of the behaviour of UPDATER was further achieved with extra effort in data gathering. Several counters were inserted into UPDATER. These accumulated the CPU and IO time consumption and measured the effects of various kinds of input. The extensive instrumentation was of course a tedious task, but the basic results could have been obtained by only a few lines of added code.

<table><tr><td rowspan="2">Number of the run</td><td rowspan="2">Number of all transactions</td><td rowspan="2">Total CPU time</td><td rowspan="2">Total IO time</td><td colspan="4">HEADER section</td><td colspan="5">UPDATEIT section</td></tr><tr><td>CPU time</td><td>CPU time per transaction</td><td>IO time</td><td>IO time per transaction</td><td>Number of correct transactions</td><td>CPU time</td><td>CPU time per correct transaction</td><td>IO time</td><td>IO time per correct transaction</td></tr><tr><td>1</td><td>389</td><td>200</td><td>1168</td><td>5</td><td>0.014</td><td>3.4</td><td>0.009</td><td>359</td><td>173</td><td>0.48</td><td>1153</td><td>3.21</td></tr><tr><td>2</td><td>1605</td><td>199</td><td>1123</td><td>17</td><td>0.011</td><td>8.3</td><td>0.005</td><td>1482</td><td>163</td><td>0.11</td><td>1103</td><td>0.74</td></tr><tr><td>3</td><td>4077</td><td>250</td><td>1119</td><td>51</td><td>0.013</td><td>24.8</td><td>0.006</td><td>3743</td><td>177</td><td>0.05</td><td>1081</td><td>0.29</td></tr><tr><td>4</td><td>4241</td><td>245</td><td>1135</td><td>46</td><td>0.011</td><td>20.3</td><td>0.005</td><td>4005</td><td>178</td><td>0.04</td><td>1103</td><td>0.28</td></tr><tr><td>5</td><td>4721</td><td>280</td><td>1197</td><td>60</td><td>0.013</td><td>31.2</td><td>0.007</td><td>4449</td><td>197</td><td>0.04</td><td>1153</td><td>0.26</td></tr><tr><td>mean</td><td>3007</td><td>235</td><td>1148</td><td>35.8</td><td>0.0124</td><td>17.6</td><td>0.0064</td><td>2808</td><td>177.6</td><td>0.144</td><td>1119</td><td>0.956</td></tr><tr><td>st.dev.</td><td>1899</td><td>34.9</td><td>33.3</td><td>23.6</td><td>0.0013</td><td>11.5</td><td>0.0017</td><td>1786</td><td>12.4</td><td>0.190</td><td>32.6</td><td>1.28</td></tr></table>

Table 1
Data of the five measurement runs.

The instrumented version of the program was used in five runs. Results are given in Table 1. The resource usage of the initialize block and FINISH section was nearly a constant in all runs (20 seconds of CPU time and 11 seconds of IO time) and the analysis of these portions of the program is excluded.

The resource usage of the HEADER section of UPDATER is dependent on the number of transactions, while browsing the main files takes the most resources of the UPDATEIT section. By counters at the beginning and end of HEADER in the five runs it could be seen that HEADER uses, on average, 12 milliseconds of CPU time and 6 milliseconds of IO time per transaction. The variation of the resource usage is rather small and the relationship between the number of transactions and CPU and IO time seem to be linear.

The resource consumption of the UPDATEIT section was analysed by inserting counters that registered the usage of CPU and IO time as the number of processed transaction records grew up. The total amount of sorted transactions was thus broken into batches of increasing size.

The result of a run of 4500 transaction records is shown in equations (3) and (4) which represent the combined effect of the transaction, ACTRE and REMRE records on CPU and IO time. By applying the same measurement procedure to different runs it is possible to obtain a set of equations about which an average can be calculated.

It is clear that the effect of short transaction records (80 bytes) on the IO time is negligible compared to the effect of ACTRE and REMRE records. It is also evident that the number of the transactions does not dominate the CPU time usage of the UPDATEIT section. The transaction records are distributed uniformly across the main file records; thus the equations

$$
\text { CPU - TIME } = 0. 0 0 3 5 \left(N _ {\mathrm{A}} + N _ {\mathrm{R}}\right) [ \text { seconds } ]\tag{3}
$$

![](/api/attachments/3VN2FUGT/fulltext/images/256be12fe1df110f17a6cb4bc4dd6698f35ed601444816f5d6e79940413533e4.jpg)  
Fig. 2. The Resource Consumption of UPDATER as a Function of the Number of Transaction Records. Data is obtained about 39 Runs During the Years 1978 and 1979. Fig. 2a: CPU Time as a Function of the Number of Transactions. Fig. 2b. IO Time as a Function of the Number of Transactions.

$$
\text { IO - TIME } = 0. 0 2 2 (N _ {\mathrm{A}} + N _ {\mathrm{R}}) [ \text { seconds } ]\tag{4}
$$

based on $N_{A}$ and $N_{R}$ are suitable predictors of the resource consumption, even though it is impossible to separate the effects of the transaction records from the effects of main file records.

Lets now put the discussion into formal and precise terms in order to clarify the measurements and analysis. In a straightforward regression analysis, an attempt is made to achieve the formula:

$$
R = a _ {0} + a _ {1} x _ {2} + \dots + a _ {n} x _ {n},\tag{5}
$$

where R is the resource consumption, the variables $x_{i}$ represent properly chosen natural business units (the units themselves or simple transformations of them, say logarithmic or exponential); the coefficients $a_{i}$ are computed through the regression. The method treats the application as a black box.

In the analysis of UPDATER, the structure of the program was taken into account so that the resource consumption could be expressed as:

$$
R = a _ {0} + \sum_ {i} F _ {i} (x _ {1}, \dots , x _ {n}),\tag{6}
$$

where i denotes a section of the program and $F_{i}(x_{1},\ldots,x_{n})$ is the resource consumption of that section expressed as a function of natural business units. The partition of programs to sections is, of course, application dependent, but according to our experience, the majority of business oriented batch applications are amenable to this kind of partition. The realization of (6) would be, in the case of UPDATER:

$$
\begin{array}{r l} \text { CPU - TIME } & = a _ {0} ^ {\text { CPU }} + F _ {\text { HEADER }} ^ {\text { CPU }} (N _ {\Gamma}, N _ {\mathrm{A}}, N _ {\mathrm{R}}) \\ & \quad + F _ {\text { UPDATEIT }} ^ {\text { CPU }} (N _ {\mathrm{T}}, N _ {\mathrm{A}}, N _ {\mathrm{R}}), \end{array}\tag{7}
$$

$$
\begin{array}{r l} \text {IO - TIME} & = a _ {0} ^ {\mathrm{IO}} + F _ {\text {HEADER}} ^ {\mathrm{IO}} (N _ {\mathrm{T}}, N _ {\mathrm{A}}, N _ {\mathrm{R}}) \\ & \quad + F _ {\text {UPDATEIT}} ^ {\mathrm{IO}} (N _ {\mathrm{T}}, N _ {\mathrm{A}}, N _ {\mathrm{R}}) \end{array}\tag{8}
$$

where $N_{T}$ , $N_{A}$ and $N_{R}$ are as in eqs. (1) and (2). The constant term $a_{0}^{CPU}$ was directly measured to be about 20 seconds. The term $F_{\mathrm{HEADER}}^{\mathrm{CPU}}(N_{\mathrm{T}}, N_{\mathrm{A}}, N_{\mathrm{R}})$ is independent of $N_{A}$ and $N_{R}$ , and its value can be estimated by Table 1; thus

$$
\begin{array}{r l} F _ {\text {HEADER}} ^ {\mathrm{CPU}} \left(N _ {\mathrm{T}}, N _ {\mathrm{A}}, N _ {\mathrm{R}}\right) & = F _ {\text {HEADER}} ^ {\mathrm{CPU}} \left(N _ {\mathrm{T}}\right) \\ & = 0. 0 1 2 N _ {\mathrm{T}} [ \text {seconds} ] \end{array}\tag{9}
$$

The behaviour of $F_{\text{UPDATEIT}}^{\text{CPU}}(N_{\text{T}}, N_{\text{A}}, N_{\text{R}})$ is given in eq. (3) which represents the combined effect of $N_{T}$ , $N_{A}$ , and $N_{R}$ on the CPU time. The key factor in the UPDATFIT section is the total number of records in ACTRE and REMRE, $N_{A} + N_{R}$ . The effect of the number of transaction records (which varies between 20–6000 in runs of UPDATER) is small. It is almost impossible to separate the CPU time used in handling transactions for the time used in handling main file records, because the precessing of transaction and main file records are so interdependent in the updating algorithm. From the figures in Table 1, it seems that the effect of the number of transaction records on the CPU time in the UPDATEIT section is (at most) 20 to 30 seconds.

The goal of our investigations was to find a good predictor for the usage of CPU time in the UPDATEIT section. It seems that $N_{A} + N_{R}$ is quite natural for predicting, and so by eq. (3), we approximate $F_{\text{UPDATEIT}}^{\text{CPU}}(N_{\text{T}}, N_{\text{A}}, N_{\text{R}}) \approx 0.0035(N_{\text{A}} + N_{\text{R}})$ . So eq. (7) can be written

$$
\begin{array}{r l} \text { CPU - TIME } & = 2 0 + 0. 0 1 2 N _ {\mathrm{T}} \\ & + 0. 0 0 3 5 (N _ {\mathrm{A}} + N _ {\mathrm{R}}) [ \text { seconds } ] \end{array}\tag{10}
$$

Eq. (8) can be analysed in a similar way. The constant term $a_0^{\mathrm{IO}}$ which describes the amount of IO time used in initializing and finishing the activities of UPDATER was measured to be about 11 seconds. The second term $F_{\mathrm{HEADER}}^{\mathrm{IO}}(N_{\mathrm{T}}, N_{\mathrm{A}}, N_{\mathrm{R}})$ is independent of $N_{\mathrm{A}}$ and $N_{\mathrm{R}}$ , and thus it can be written as $F_{\mathrm{HEADER}}^{\mathrm{IO}}(N_{\mathrm{T}})$ . It was measured to be between 3.4 and 31.2 seconds, which is small compared to the total amount of IO time (whose mean was 1254 seconds in the data).

The number of records in the error file has a very small effect on the $F_{\text{HEADER}}^{\text{IO}}(N_T)$ ; according to our measurements the IO time of error file is less than one second. The main IO activities are applied to transactions and sorting files. The value of $F_{\text{HEADER}}^{\text{IO}}(N_T)$ is $0.006N_T$ by the measurements. The value of the third term of (8), $F_{\text{UPDATEIT}}^{\text{IO}}(N_T, N_A, N_R)$ , can be obtained from eq. (4). By the same kind of argument as that of $F_{\text{UPDATEIT}}^{\text{CPU}}$ , we can approximate $F_{\text{UPDATEIT}}^{\text{IO}}(N_T, N_A, N_R) \approx 0.022(N_A + N_R)$ . Thus (8) takes the form:

$$
\begin{array}{r l} \text { IO - TIME } & = 1 0 + 0. 0 0 6 N _ {\mathrm{T}} \\ & + 0. 0 2 2 (N _ {\mathrm{A}} + N _ {\mathrm{R}}) [ \text { seconds } ] \end{array}\tag{11}
$$

Eqs. (10) and (11) resemble the corresponding equations obtained through regression analysis. The only major difference is that the coefficient of $N_{T}$ is 0.023 in eq. (2) while the corresponding coefficient of eq. (11) is 0.006. The value 0.023 must be considered wrong. It results from the fact that the usage of IO time is dominated by $N_{A}$ and $N_{R}$ , and casual fluctuations in the historical data produce this result. The omission of the constant term in the regression analysis may also contribute to this error. Other coefficients in the equations obtained in both ways seem to be about the same. However, the measurements presented here are only experimental and illustrative. More data must be obtained to establish the actual models on which real decision can be based.

We conclude from our experiments with SISUH that the two methods, regression analysis and modeling with measurements are complementary to one another. Regression analysis must be based on large historical data gathered by the operating system during the normal use of the application. Measurements can be made during the production runs of the application, but it is not sensible to use an instrumented version of the software for all runs. Gathering data from normal runs of the application is essential. The resource consumption in test runs may be very misleading, because good atest material contains all kinds of peculiar cases that reveal the faults of programs in rare situations, while in production runs, the bulk of the resources is consumed in processing normal cases.

## 5. Discussion

Here, we briefly discuss the consequences of adopting a modeling and measuring approach, and outline directions for future research.

Instrumentation of programs requires some additional effort. The rather extensive measuring instrumentation of UPDATER consisted of about 200 lines of inserted COBOL code, and the instrumentation took about two person months of an author who was totally unfamiliar with the program. Most of the time was spent in getting acquainted with the program. The essential instrumentation to produce the data presented in this article requires only about a hundred lines of code, and inserting these lines is not a difficult task for a person who knows the software. A good estimate would be a working week on a medium size program (say 2000 to 3000 lines of COBOL), and if the instrumentation is done when the program is coded for the first time, the extra effort is negligible.

The procedures of the data gathering are very dependent on the hardware and operating system software. With the Burroughs B6700 computer, operating system, and COBOL compiler the use of application software in measuring is easy because of the various TIME functions available in COBOL; the overhead caused by the measurements is quite negligible.

We used two sources of information, measurements and data gathered on the normal log-file by the operating system. The use of traditional software monitors (e.g. the SPARK system of Burroughs [4]) was considered unnecessary and uninformative for our purposes. However, the situation may be different with other computers, and the methods of data gathering on the behaviour of application software need further investigation.

The analysis of SISUH has proved useful. SISUH is now being modified, because the structure of studies at the University of Helsinki is changing. One essential question is: What shall be the smallest unit of study to be registered in the student's record? With small units (a course or a part of a course), the size of the files grows larger, but information describing the progress of a student's studies is better. The planner of the new system is in a better position if able to obtain exact figures of the cost. The structure of the application software is quite independent of the number of study units to be registered, and so it is up to the government of the University to make a decision according to its costs and benefits.

The decision makers are clearly better off with cost figures based on natural business units. With new systems, there is nothing to be measured, but information on old systems can be used to estimate the resource consumption of the new ones. By our experience, much of the code remains the same between generations of application systems. Thus, for example, the code used for validating a transaction record may be approximately the same in different versions, and thus data gathered from an old version can be used. But such estimation presupposes detailed information on the old system and proper modeling of the new.

The inclusion of such cost formulas like (10) and (11) to the documentation compels the designers of the system to pay attention to the efficiency of the system. The users can judge if the cost is acceptable, and compare several systems in order to see if some of them seem to be exceptionally efficient or inefficient.

## Acknowledgements

We wish to thank Ph.Lic. Juha Hakola for profound and fruitful discussions and Prof. Martti Tienari for guidance and encouragement. The helpful comments of the Editor and the Referees are gratefully acknowledged. The work was partly supported by the Research Foundation of the Finnish Data Processing Association.

## References

[1] H.P. Artis: Forecasting Computer Requirements: An Analyst's Dilemma, EDP Performance Review, vol. 8 (1980), no. 2.

[2] B.W. Boehm: Software Engineering – As It Is, Proc. of the 4th International Conference on Software Engineering, Munich, Germany, 1979.

[3] L. Bronner: Overview of the Capacity Planning Process for Production Data Processing, IBM System Journal, vol. 19 (1980), no. 1.

[4] Burroughs Corporation: Systems Performance Analysis Review Kit, Sampler & Sample analyzer, B6700 User's Manual, USA, 1975.

[5] J.C. Emery: Costs and Benefits of Information Systems, Information Processing 74, Proc. of IFIP Congress 74, North-Holland, 1974.

[6] H. Hinomoto: An On-line Customer Information System at a Gas Utility Company, Information & Management, vol. 2 (1979), no. 2.

[7] P.C. Howard (ed.): Standard Costing in Data Processing, EDP Performance Review, vol. 9 (1981), no. 6.

[8] O. Kangas: Replanning of Rejected Steel Plates as a Real Time System, NordData 1976.

[9] R. Malik: Real Time Reservations, Data Systems, February 1972.

[10] J.E. McNeece: Computer Workload Forecasting, Proc. of the 15th Meeting of Computer Performance Evaluation Group, National Bureau of Standards Spec. Publ. 500-52, Washington, 1979.

[11] Proceedings of the IEEE, issue on Software Engineering, vol. 68 (1980), no. 9.

[12] D.B. Sarna: Improving Computer Forecasting Using Key Volume Indicators, AFIPS Conference Proc., vol. 48, 1979.

[13] G. Waldbaum: Tuning Computer Users' Programs, RJ2409, IBM Research Laboratory, San Jose, 1978.
