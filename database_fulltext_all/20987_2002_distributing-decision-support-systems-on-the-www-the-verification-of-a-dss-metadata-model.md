---
otero_id: 20987
otero_key: "UFCNMC3V"
title: "Distributing decision support systems on the WWW: the verification of a DSS metadata model"
authors: "Dawn G. Gregg; Michael Goul; Andy Philippakis"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00095-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributing decision support systems on the WWW: the verification of a DSS metadata model

Dawn G. Gregg <sup>a,</sup>\*, Michael Goul <sup>b</sup>, Andy Philippakis <sup>b</sup>

<sup>a</sup>School of Management, Arizona State University West, P.O. Box 37100, Phoenix, AZ 85069-7100, USA <sup>b</sup>School of Accountancy and Information Management, Arizona State University, Box 873606, Tempe, AZ 85287-3606, USA

## Abstract

The explosion of information on the World Wide Web (WWW) and on corporate Intranets has made it increasingly important to have methods of organizing and understanding the available content. One method being used to facilitate both the location of specific Web content and the assessment of its quality is metadata. This paper focuses on verifying a metadata model designed for distributing decision support systems (DSS) on the Web. The verification utilizes an experiment to assess endusers’ understanding of specific DSS. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Metadata model; Decision support system; Data quality; Open DSS protocol

## 1. Introduction

Research in the decision sciences has resulted in the development of a variety of Decision Support Systems (DSS) that are useful in solving many decision problems faced by individuals and organizations. It is now possible to access these DSS using the Internet. However, it is often difficult for individuals and organizations to locate specific DSS that could benefit them.

At present, the Internet provides access to thousands of gigabytes of information (including DSS), with more information being added every day. There are numerous indexes and search engines currently available to organize this vast amount of data. However, in spite of the variety of ways information can be discovered on the Web, it is still difficult to find many of the resources that are available and to assess the quality of the information that is found. In March 1997, Scientific American published a special issue on the Internet. It cited the most serious, long-range problem for the Internet is that ‘‘much of the information on the Internet is quirky, transient and chaotically ‘shelved’’’ [19]. The indexes and search engines used to find information on the Internet are tools to deal with the clutter and traffic that are part of today’s Web reality. However, they do not tackle questions about how to better organize information and assess its quality.

Metadata is one mechanism being used to facilitate both the location of specific Web content and the assessment of its quality. Metadata is information about the structure and content of a data resource [11]. Metadata is currently being used on the Web to provide the title, author, and a description of Web pages (e.g., Refs. [10,13,22]). Metadata allows businesses and consumers to locate appropriate resources and judge their fitness.

A metadata model has been developed specifically for distributing DSS on the Web. This metadata model is part of a proposed ‘‘Open DSS’’ protocol. It is designed to fully describe DSS so that appropriate DSS can be located and understood by decisionmakers [15]. The focus of this paper is on evaluating the Open DSS protocol metadata model to determine if it is a useful and adequate mechanism for distributing DSS either on the Web or on a corporate Intranet. The methodology utilizes an experiment to assess a subject’s understanding of specific DSS capabilities based solely on protocol compliant metadata descriptions. Results of the study are used to determine if the metadata model is sufficient and complete to describe a variety of DSS and to obtain feedback on improvements that can be made to the metadata model.

## 2. Metadata models

In the database environment, metadata are descriptions of the structure of the database. They are used to describe the structure of the files, the type and storage format of the data, and the constraints on the data [11]. Metadata are used in the Web environment to identify the content and quality of Web pages [21,22]. Web metadata systems are primarily designed to improve the accessibility and interpretability of Web content. That is, they are designed to improve end-users’ ability to locate specific resources that are available on the Web and to help end users understand the content. The general requirements for Web page metadata systems have been identified in the literature (e.g., Refs. [10,13,14,22]):

1. The metadata must provide specific data related to the page type, subject area, and source,

2. The metadata should be designed to meet the specific needs of the target user population,

3. The metadata must have a consistent format so autonomous agents can readily use it when processing user search requests.

The first two requirements are designed to provide the information necessary for a target population of end-users to understand exactly the purpose, content and source of specific Web information. The third requirement is necessary because the vast resources available on the Web cannot be efficiently searched without the aid of some sort of intelligent agent. Current intelligent agents work much more accurately when they are processing data that is in a predictable format (e.g., Refs. [1,7,12,18]).

Metadata contributes to the disintermediation of the Web. It provides information in a concise, uniform and easily interpretable way. Many of the current metadata systems are general systems that can describe a wide range of information. They are designed to answer questions from the most inexperienced users, yet permit in-depth research as well (e.g., Refs. [10,13, 22]).

Metadata systems can also be defined to meet the need of a specific user population. The Open DSS protocol metadata model is one example of such a system. The first layer in the Open DSS protocol, the Metadata Layer, is a metadata model implemented as a set of HTML headers. This metadata model allows the use of specialized Web search agents (e.g., Robots, Spider, and Wanderers) to provide automated intelligent discovery of DSS pertaining to a specific decision-making or problem-solving situation [14].

A list of the Open DSS protocol metadata attributes is presented in Appendix A. This model includes selected functional attributes from model management research. The goal of much of this research has been to develop techniques to select or construct appropriate models to be utilized so as to provide the appropriate answer [9]. Researchers like Blanning [6] and Chari and Krishnan [8] have conducted research on the storage, representation, utilization and manipulation of models. To date, there has been no universally agreed upon method for representing and specifying DSS models. However, at a minimum, a DSS representation scheme should include descriptions of the stimuli (inputs) and responses (outputs), state (data structures), and procedures (control structures) [4]. The Open DSS protocol metadata currently includes functional attributes related to the problem domain of the DSS, the solution options, the inputs, the outputs, and the assumptions made.

The Open DSS metadata model also includes metadata on the resources required to execute the DSS. These include information on the hardware requirements (e.g., computing platform), software requirements (e.g., operating system or application needs), and any specific user skills required to use the DSS. Finally, the metadata model contains all other information necessary to purchase and download the DSS. This includes information on the DSS’s cost, its references, related DSS, and source/author information.

## 3. Verification of metadata systems

To verify the claim that a given metadata model supports end-users’ ability to locate appropriate resources and judge their fitness, it is important to test the usefulness of the information they provide. One definition of verification is that it is a method for evaluating the effectiveness of a process and its contribution to accomplishing the objectives of the system. This type of verification is based on an assessment of the quality of the system and the support it provides the process [23]. Verification can also be defined from an end-user perspective. The conceptual hierarchy of objectives views verification or effectiveness as the ability of end users to use the system for accomplishing their goals [16].

One method of verifying metadata systems is to determine if they are sufficient to allow end-users to assess the quality of the content available on a given Web site. This is appropriate for metadata systems because one of the requirements of many metadata models is that they assist end-users in assessing the information quality specific Web sites [21,22]. In practice, information is viewed as data that has been processed in some manner. However, the terms data quality and information quality are often used synonymously in information systems literature [26]. This paper will use ‘‘information quality’’ interchangeably with ‘‘data quality.’’

Many researchers have attempted to define the dimensions upon which data quality should be measured. Studies have defined data in terms of accuracy (recorded value in agreement with the actual value), currency (recorded value is not out of date), completeness (all values for certain variables are recorded), and consistency, (the representation of the data value is complete in all cases) (e.g., Refs. [3,17, 25,27]). One study used a survey to assess the data quality dimensions that mattered most to data consumers. This survey resulted in 15 principal data quality dimensions that were grouped into four broad data quality categories, Intrinsic DQ (data quality), Accessibility DQ, Contextual DQ, and Representation DQ [24,28]. These principal data quality dimensions make up a conceptual framework of data quality (shown in Fig. 1).

One study has attempted to verify five different metadata systems by mapping the metadata attributes to information quality requirements that have been identified in prior research [20]. The researchers were interested in determining if current metadata models provide sufficient information to allow endusers to analyze the quality of the content retrieved from the Web. The researchers compared data quality requirements identified by Wang and Strong [28] with five common metadata models. Their study showed how information quality criteria could be derived from existing metadata by mapping the metadata attributes to specific information quality requirements.

As an initial step in the verification of the Open DSS protocol metadata model, a similar mapping of model attributes to information quality requirements was conducted. For this study, the four data quality categories identified by Wang and Strong [28] were used for the mapping. Two of these categories, intrinsic data quality and accessibility data quality can be directly mapped to the Open DSS protocol metadata attributes.

Intrinsic data quality includes not only accuracy and objectivity, but also includes believability and reputation [28]. It is possible to assess intrinsic data quality using attributes in the Open DSS protocol metadata model. For example, believability and reputation can be assessed based on the author/source information. In addition, the Open DSS protocol metadata allows DSS suppliers to provide a list of references for the DSS, a list of other people who have used the DSS, warranty information, licensing information, and liability information. It also allows for assumptions made by the model and system constraints to be specified. All of these attributes contribute to an end-user’s ability to evaluate the intrinsic quality of a given DSS offering.

![](/api/attachments/UFCNMC3V/fulltext/images/0b582c5238f8871c70624ed334d9981febe3eb3f144b662bb387d4a7a565fe88.jpg)  
Fig. 1. Conceptual framework of data quality (from Wang and Strong [28]).

Accessibility data quality refers to end-users’ ability to find and use a given resource. It includes how the resource can be accessed and any access security constraints for the resource [28]. The Open DSS protocol metadata model improves accessibility for DSS distributed via the Web by making it easier to locate DSS as opposed to textual Web resources that mention a DSS but provide no software solution. In addition, the metadata model provides an access mode attribute that allows end-users to determine how the given DSS can be obtained and run.

The remaining two data quality categories are not as straightforward in their mapping to the Open DSS protocol metadata model. Representational data quality includes aspects related to the format of the data and the meaning of the data. It includes criteria like representational consistency, concise representation, interpretability, and ease of understanding [28]. Contextual data quality depends on the context of the task at hand. It includes completeness and timeliness as well as value-added, relevancy, and appropriate amount of data [28]. In the context of DSS distribution via the Web only a few of these attributes have relevance. The Open DSS metadata model should promote end-users’ understanding of specific DSS capabilities. It should allow end-users to assess whether a given DSS is relevant for a given problem situation and whether it will completely solve a problem or only solve a portion of it.

The functional attributes in the Open DSS metadata model are designed to do this. Whether or not these attributes are sufficient for end-users to understand the capabilities of a given DSS can only be determined in the context of their use. That is, they must meet the needs of the end-user population in order for their quality and completeness to be judged acceptable. The next section describes an experimental study conducted to determine whether the Open DSS protocol metadata model meets the requirements of DSS developers and end-users.

## 4. Experimental validation

For the metadata model of the Open DSS protocol to meet contextual information quality requirements, it needs to describe DSS such that potential users can accurately determine if the DSS meet their decision-making needs. This can only be accomplished by developing specific DSS metadata instances and determining if the metadata is complete enough for potential end-users to evaluate the DSS capabilities.

We conducted an experiment to ascertain if users can determine the functionality of a DSS based solely on the metadata specified in a proposed Open DSS protocol metadata model. In this experiment, two subject groups were used: DSS developer subject and end-user subjects. The DSS developer subjects generated Open DSS protocol compliant metadata for a specific DSS. Then, the DSS developer subjects were asked to determine whether their DSS could be applied in a set of business decision-making situations. Finally, end-user subjects were asked to determine the suitability of the DSS for the same set of business situations. The end-user subjects only had access to the metadata descriptions of the DSS. The following hypothesis was offered (stated in alternate form):

## $\mathbf { H } _ { \mathbf { A } }$ . Answers for end-user subjects will be positively correlated with those for DSS developer subjects.

To determine if the metadata model of the Open DSS protocol meets representational quality requirements, it is necessary that DSS developers and endusers can interpret and easily understand the specific metadata attributes. The Open DSS protocol has 37 variables that describe the conditions for which the DSS will be potentially useful. For the metadata to meet data quality requirements, each metadata attribute must be understandable to the subjects. To gauge whether the Open DSS protocol metadata model is understandable, the percentage of the DSS developers subjects specifying a given metadata attribute correctly was measured. In addition, to get an overall measure of the representational data quality, the median number of attributes correctly defined by the DSS developer subjects was also determined.

## 4.1. Method

The study was conducted using 36 student subjects that were either masters students or Ph.D. students in the College of Business at Arizona State University. The use of student subjects in the experiment was deemed appropriate because the subjects had an average of 7 years of work experience as well as experience developing and using DSS. Prior to beginning the experiment, the DSS developer subjects were divided into 17 groups of 1 –4 students and were asked to design and build (program) a specific DSS. This DSS task was an assignment for the DSS course these subjects were enrolled in. The experiment required the DSS developer subjects to understand the DSS they were creating for the class sufficiently well that they could create metadata for it. The experiment took place in three stages and each stage lasted about 30 min.

In the first stage, the DSS developer subjects were given a list of the metadata attributes with examples as shown in Appendix A. These subjects were asked to generate metadata for the DSS their group was creating for the class. The DSS developer subjects generated the metadata descriptions individually.

In the second stage of the experiment, the DSS developer subjects were given a set of five short business situations that were related to their DSS in some way. They were asked how applicable their DSS would be for solving or contributing to the solution of the business problem. The five case scenarios were selected from a set of 49 cases that describe situations where the DSS might or might not be useful. Sample cases are presented in Appendix B. The DSS developer subjects were asked to rank the applicability of the DSS from 0 to 5 where the ranks were:

5: Very applicable, could be used to solve this problem

4: Applicable, could be modified to solve this problem

3: Partially applicable, could be used to solve a portion of this problem

2: Somewhat applicable, DSS could be used to provide a guide for development for the entire problem

1: Minimally useful, DSS could be used to provide a guide for development for a portion of the problem

0: Not at all useful for this problem

Each subject was then given another subject’s DSS metadata and was asked how applicable it was for a set of five business problems specifically targeted to that DSS. The subjects were now acting as end-user subjects. The end-user subjects were given no information about the DSS that they were being asked to evaluate other than the metadata generated by the DSS developer subjects. The answers were then compared for each subject pair (DSS developer and end-user).

Finally, in the third stage, all of the subjects answered questions aimed at gathering data about the metadata creation process, the completeness of the specification, and the clarity of the specification.

## 4.2. Data analysis and results

To ascertain if users can determine the functionality of a DSS based solely on the metadata, the applicability of each DSS to five simple business problems was evaluated by both the DSS developer and by a potential end-user. Thirty-six different DSS specifications were evaluated for five different problems to determine if there was agreement between the answers for the DSS developers and those for the potential end-users. Possible answers ranged between 0 (not at all applicable) and 5 (perfectly applicable). Agreement was assessed by calculating the measurement of agreement between the two sets of answers [2].

A kappa value of 0.108, resulted for assessing agreement between the answers for the DSS developer subjects and those for the end-user subjects. Due to the large sample size (170 useable individual situation pairings) the significance of this Kappa was estimated to be 0.003. Thus, the directional alternative hypothesis: Answers for end-user subjects will be positively correlated with those for DSS developer subjects, is supported at the 0.05 level. This indicates that the metadata was adequate to completely describe the capabilities of the 17 different DSS used in the study.

The success of DSS developer subjects in creating the specifications was also evaluated. Success was based on the accuracy of the DSS developer subjects’ responses for each of the 37 metadata attributes. Each response could take one of three values: correct, blank, or incorrect. A response was determined to be appropriate if it was syntactically correct or if it was ‘‘n/a’’ (not applicable). Metadata attributes that were given a ‘‘?’’ (not understood) or that were not of the correct type were considered incorrect. Attributes that were left blank were scored as a different type since they could have been skipped because they were not applicable or because they were not understood.

The interpretability of each metadata attribute definition was evaluated by determining the percentage of DSS developer subjects who defined a given attribute correctly. The proportion of correct answers was calculated for each of the 37 metadata attributes and is presented in Table 1. Thirty percent of the attributes (11) were not defined correctly even 70% of the time. The types of errors made for these 11 attributes were evaluated further. Five of these attributes were left blank more often than they were incorrectly answered. These five attributes, Constraints, References, Related<sub></sub>DSS, Limited<sub></sub>liability, and Licensing<sub></sub>agreement, were designed to support commercially available DSS and were not applicable to the DSS being developed by the student subjects. Thus, it is likely that these attributes were left blank because they were not applicable as opposed to being not understood.

Table 1  
Percent correct for each metadata attribute

<table><tr><td>Metadata attribute</td><td>% Correct</td><td>Metadata attribute</td><td>% Correct</td><td>Metadata attribute</td><td>% Correct</td></tr><tr><td>Computing_platform</td><td>100.00%</td><td>Input_type</td><td>83.78%</td><td>References</td><td>67.57%</td></tr><tr><td>Operating_system</td><td>100.00%</td><td>Disk_storage</td><td>83.78%</td><td>Licensing_agreement</td><td>67.57%</td></tr><tr><td>Problem_domain</td><td>97.30%</td><td>Output_data_type</td><td>81.08%</td><td>Limited_liability</td><td>67.57%</td></tr><tr><td>Model_types</td><td>97.30%</td><td>Fee</td><td>81.08%</td><td>Input_valid_range</td><td>64.86%</td></tr><tr><td>User_skill_require</td><td>97.30%</td><td>Warrantee</td><td>81.08%</td><td>Constraints</td><td>62.16%</td></tr><tr><td>Title</td><td>94.59%</td><td>Input_units</td><td>78.38%</td><td>Output_valid_range</td><td>59.46%</td></tr><tr><td>Model_benefits</td><td>94.59%</td><td>Status</td><td>78.38%</td><td>Model_options</td><td>54.05%</td></tr><tr><td>Description</td><td>91.89%</td><td>Keywords</td><td>75.68%</td><td>Related_DSS</td><td>54.05%</td></tr><tr><td>Input_data_type</td><td>91.89%</td><td>Output_type</td><td>75.68%</td><td>Output_function</td><td>43.24%</td></tr><tr><td>RAM</td><td>91.89%</td><td>Output_units</td><td>75.68%</td><td>Input_function</td><td>40.54%</td></tr><tr><td>Programming_lang</td><td>89.19%</td><td>Potential_user_prob</td><td>75.68%</td><td>Function_libraries</td><td>40.54%</td></tr><tr><td>Other_hardware</td><td>86.49%</td><td>Access_mode</td><td>72.97%</td><td></td><td></td></tr><tr><td>Application_names</td><td>86.49%</td><td>Assumptions</td><td>70.27%</td><td></td><td></td></tr></table>

The remaining six attributes, Model options, Input function, Output function, Inputvalid range, Output<sub></sub>valid<sub></sub>range, and Function<sub></sub>libraries, were answered incorrectly more often than they were left blank. This indicates the DSS developer subjects had difficulty understanding what was expected for these attributes and that the information provided for these attributes should be improved.

All of the subjects’ opinions about the usefulness and adequacy of the protocol were assessed using a post experiment questionnaire. The subjects were asked whether they believed the protocol would be useful, if they believed it allowed all major capabilities of the DSS they were evaluating to be described completely, and if they believed the individual Open DSS attribute definitions were clearly presented. Overall, the subjects’ responses indicate that although they believed the protocol is useful, they did not feel it allowed all of the major capabilities of their DSS to be described. This perception was not supported by the experiment, since the results indicated that the metadata was adequate for the end-user subjects to evaluate the functionality of the DSS.

The subjects’ perceptions about the clarity of the DSS attribute definitions were evaluated. The subjects did not feel that all of the attributes were adequately defined. This is consistent with the fact that 11 of the attributes were not defined correctly even 70% of the time.

The subjects also indicated that while the metadata allowed most relevant information to be specified it did not allow all of the major capabilities of the DSS to be described. Some of the subjects suggested the addition of attributes including Typical<sub></sub>users, Target<sub></sub>industry, Prior<sub></sub>users and Examples<sub></sub>of<sub></sub>uses.

## 5. Discussion

The present study tested an Open DSS protocol metadata model to determine if it would be a useful and adequate mechanism for distributing specific DSS either on the Web or on a corporate Intranet. The verification began with an examination of the Open DSS protocol metadata model that showed the metadata attributes did allow both the intrinsic quality and accessibility of a given DSS offering to be assessed by end-users. The experimental study then evaluated the adequacy of this metadata to describe specific DSS such that new protocol users could determine the functionality of a DSS based solely on the metadata provided. The results of the experiment indicate the Open DSS protocol does provide an effective mechanism for describing DSS capabilities.

The results of the study also suggest that several of the metadata attributes need to be clarified or dropped from the metadata set. For example, many of the subjects had difficulty with the attributes Input<sub></sub>valid<sub></sub>range and Output<sub></sub>valid<sub></sub>range. These attributes were included in the metadata so that users could determine the range for which the variable produces a valid answer (e.g., an integer has a valid range from  32,767 to + 32,767, and a floating point variable restricted to positive values has valid a range of 0 to + 3.40282347E + 38). The valid range attributes were two of the attributes that were included in the data set to allow for the automatic integration of DSS that might be possible using intelligent agents. The set of integration attributes has now been labeled as ‘‘model integration attributes for use with intelligent agents’’. This will allow developers the option of using them if they feel their DSS is suitable for integration.

Other attributes that need to be clarified or dropped include the attributes Input<sub></sub>function, Output<sub></sub>function, and Function<sub></sub>libraries. Input<sub></sub>function and Output<sub></sub>function have been renamed to Input<sub></sub>variables and Output<sub></sub>variables. The description of these attributes specifies that they refer to a text description of the function of the inputs and outputs of the DSS. For example, common financial input and output variables are interest<sub></sub>rate, revenue, and gross<sub></sub>margin. The attribute Function<sub></sub>libraries was removed because if a DSS required the user to have the Function<sub></sub>libraries for a programming language, it would likely also require the programming language, which is a separate metadata attribute. Appendix C contains an updated description of the metadata layer of the Open DSS protocol that reflects these and other changes.

Finally, the subject’s perceptions about the protocol were evaluated to determine their opinions about the usefulness and adequacy of the protocol. The majority of subjects believed having a protocol that would facilitate their finding DSS on the Web would be useful to them as future decision makers. However, the subjects also reported having difficulty understanding what was expected for several of the metadata attributes. To address this problem, the basic metadata requirements have been rewritten to describe the different attributes more clearly. The updated version of the metadata is presented in Appendix C.

The subjects also indicated that while the metadata allowed most relevant information to be specified it did not allow all of the major capabilities of the DSS to be described. Some of the subjects suggested the addition of attributes including: Typical<sub></sub>users, Target<sub></sub>industry, Prior<sub></sub>users and Examples of uses. These four attributes all included relevant information that was not described with the original metadata attributes. The updated metadata in Appendix C includes these four additional attributes.

## 6. Conclusion

The World Wide Web (Web) was designed to be a ‘‘pool of human knowledge, which would allow collaborators to share their ideas and all aspects of a common project’’ [5]. This goal for the Web makes it an ideal distribution system for DSS. However, a decision-maker must be able to locate and interpret the DSS that are made available. The results of this study indicate that:

1. The metadata model specified in the Open DSS protocol includes sufficient information for potential users to determine if the DSS described has specific capabilities.

2. Deploying DSS on the Web using the Open DSS protocol would facilitate decision-makers ability to locate appropriate DSS for their given decision problems.

The ability of the Open DSS protocol to improve end-users’ ability to locate specific DSS on the Web was not explicitly tested in the experiment. However, since the Open DSS protocol’s effectiveness in helping end-users understand the capabilities of specific DSS has been verified, and, the ability of intelligent agents to efficiently search the Web when they are processing data that is in a predictable format has been demonstrated, it is possible to conclude that implementation of the Open DSS protocol would facilitate the sharing of specific DSS via the Web (e.g., Refs. [1,7,12,18]).

While results of this experiment indicate the current Open DSS protocol metadata model is sufficient to describe most DSS, it also allowed identification of areas where the protocol might be improved. This experiment resulted in the clarification of several of the metadata attributes as well as the addition of four new attributes that were not included in the original metadata model.

Finally, with the explosion of information on the Web and the increased used of Intranets within corporations, it is becoming increasingly important to have methods of organizing and understanding the information that is available. This paper presents a novel experimental methodology allowing metadata models to be validated. This validation method involves the creation of specific metadata instances and interpretation of these metadata instances by the target end-user population. The strength of this validation approach is that it assesses whether the proposed metadata model is sufficient for its intended use: that is, whether it allows end-users to better understand the content of a given Web site. In addition, this method provides feedback to metadata model creators, facilitating the improvement of their models to better meet end-user needs.

Although this paper addresses several important issues related to the adequacy of an Open DSS protocol and the validation of its metadata, there are several technical issues that remain unexplored. The next phase of this research will involve the development of an autonomous Web search agent. The search agent will identify and index the protocol compliant Web pages produced by the student subjects. Next, an end-used search-tool that allows appropriate DSS to be identified will be developed and validated.

Appendix A. Open DSS protocol metadata

<table><tr><td>Functional information</td><td>User requirements</td><td>Other information</td></tr><tr><td>Problem_domain(e.g., Budgeting,Insurance Risk Prediction, etc.)</td><td>Hardware requirements:</td><td>Fee or Donation(e.g. $25 or None)</td></tr><tr><td>Model_types(e.g., Statistical, Genetic Alg.,Neural Net., etc.)</td><td>Computing_platform(e.g., PC, Mac, Unix, etc.)</td><td></td></tr><tr><td>Model options(e.g., portfolio analysis andtracking of stocks)</td><td>RAM (e.g., 8MB recommended)</td><td>Warrantee(e.g., Thirty-day limitedwarranty on disks.)</td></tr><tr><td>Model_benefits(e.g., improves inventorymanagement etc.)</td><td>Disk_storage (e.g., 25MB)</td><td>References(e.g., http://www.abc.com)</td></tr><tr><td>Input_type(e.g., variable/time series)</td><td>Other_hardware_requirements(e.g., CD_ROM, Monitor,Printer, Multimedia, Fax)</td><td>Related_DSS(e.g., The Auditing Expert)</td></tr><tr><td>Input_function(e.g., annual_interest_rate)</td><td></td><td>Other_accessors(e.g., jdoe@newco.com)</td></tr><tr><td>Input_units(e.g., inches/second)</td><td>Software requirements:</td><td>Status(e.g., released, beta, etc.)</td></tr><tr><td>Input_data_type(e.g., integers vs. float)</td><td>Operating_system(e.g., Win95, Unix, etc.)</td><td>Access_mode(e.g., Whether the DSS isdownloadable or if usersare allowed to use the DSSat the vendors site)</td></tr><tr><td>Input_valid_range(e.g., 0 to 32,767)</td><td>Application_names and version(e.g., Excel/4.0)</td><td>Licensing_agreement(e.g., This software is licensedfor use on a single machine...)</td></tr><tr><td>Output_type(e.g., variable/time series)</td><td>Programming_languages(e.g., Java, C++)</td><td>Limited liability(e.g., This software issold “as is”. All warrantieseither expressed or implied aredisclaimed as to the softwareand its quality, performanceor fitness for any particularpurpose...)</td></tr><tr><td>Output_function(e.g., annual_interest_rate)</td><td>Functions_libraries(e.g., Java Class Libraries)</td><td></td></tr><tr><td>Output_units(e.g., inches/second)</td><td>File_transfer_software(e.g., ftp)</td><td>Vendor/Author information:</td></tr><tr><td>Output_data_type(e.g., integers vs. float)</td><td></td><td>Name</td></tr></table>

D.G. Gregg et al. / Decision Support Systems 32 (2002) 233–245

<table><tr><td>Functional information</td><td>User requirements</td><td>Other information</td></tr><tr><td>Output_valid_range(e.g., 0 to 99)</td><td>Other requirements:</td><td>Address</td></tr><tr><td>Assumptions(e.g., contiguous data)</td><td>User_skill_requirements(e.g., Mathematical AI/knowledge engineeringFunctional/industrial knowledge)</td><td>Phone</td></tr><tr><td>Constraints(e.g., US only)</td><td>Potential_User_Problems(e.g., if variables not defined correctly, the program crashes)</td><td>E-mail</td></tr></table>

## Appendix B. Sample DSS metadata study business situations

Case 1: You are responsible for obtaining a DSS that will assist your company in managing multiple cash flows such that they are immunized from interest rate fluctuations. The program must be capable of obtaining spot interest rates automatically from the Web and noti fying the user of a need to make a transaction.

Case 2: You run a company that builds computers based on a customers’ specifications. You are looking for a DSS that can help manage a Web-based database that will allow both employees and customers to track orders through the assembly process. The database tool must control access to information such that a customer’s privacy is not violated.

Case 3: You run an employment agency specializing in retraining workers to meet current local industry needs. You are looking for a DSS that can track local employment patterns and predict the probable job openings and salary ranges for the upcoming year.

Case 4: You are a geologist responsible for predicting whether there will be sufficient titanium, tantalum, vanadium and uranium to meet growing industry demands. You have output data from the mines currently producing these metals and demand predictions based on order backlogs. You are looking for a DSS tool to help you compile the information and help make a prediction of future shortfalls.

Case 5: You are a software manufacturer interested in creating a legal expert system. This system should be capable of scanning large legal databases and automatically selecting cases that meet a set of requirements selected by a lawyer. The system will be designed to dramatically reduce the amount of time it takes to research legal cases.

## Appendix C. Revised open DSS protocol metadata

The following is a list of the metadata attributes for the Open-DSS protocol. Not all of these metadata attributes are necessary to define a given specific DSS. The individual attributes can be defined in any order and unknown attributes are ignored by the search agents. Metadata attributes are defied as follows:

$$
\begin{array}{l l} \text { Attribute\_type } 1 = & \text { value1,   value2,...valueN; } \\ \text { Attribute\_type } 2 = & \text { value1;   etc. } \end{array}
$$

The metadata attributes should be defined in a standard HTML document.

Attribute List:

Title: The name of the DSS

Keywords:

Description:

Functional Information:

Problem<sub></sub>domain: The types of problems instances the DSS is designed to support, e.g., budgeting, insurance risk prediction, investment planning.

Model<sub></sub>types: The type or types of models included in the DSS, e.g., Data Driven, Parametric/Non-Parametric Statistics, Genetic Algorithm, Neural Network, Rule Based System, Fuzzy Logic, etc.

Model options: The different solution options available with the DSS, e.g., portfolio analysis and tracking of individual stocks or

Model<sub></sub>benefits: Why someone should choose to use this DSS, e.g., improves inventory management and automates product reordering.

Typical<sub></sub>users: The users most likely to benefit from this DSS, e.g., accounting manager, chemical engineer, etc.

Target industry: The industry the DSS was designed to support, e.g., retail, home builder, manufacturer.

Examples<sub></sub>of<sub></sub>uses: Used to project revenues for the next year or used to predict costs based on material and schedule requirements.

Assumptions: Any assumptions the DSS requires the user to make, e.g., continuous data, or any proceeds are collected at the time of sale.

Constraints: Any constraints imposed by the system, e.g., date cannot exceed 2000, maximum of 5000 records, etc.

Inputs and Outputs:

Input and output attributes specify the information requirements and solutions provided by the DSS.

Each input or output variable has a variable name, units, data type, valid range, and input type. If there are three input variables, each variable must have each of the five attributes specified, as shown in the example below:

Input<sub></sub>variables = period<sub></sub>interest<sub></sub>rate, payment, number<sub></sub>periods

Input<sub></sub>units = percent, dollars, whole number

Input<sub></sub>data<sub></sub>types: float, float, integer

Input<sub></sub>valid<sub></sub>ranges: 0 to 100, 0 to 1,000,000, 1 to 360

Input<sub></sub>types: variable, variable, variable

These attributes are included to facilitate the integration of multiple models using intelligent agents.

## Model Integration Attributes:

Input<sub></sub>variables or Output<sub></sub>variables: refer to: a text description of the function of the inputs and outputs of the DSS, e.g., common financial input and output variables are: interest<sub></sub>rate, revenue, and gross<sub></sub>margin.

Input<sub></sub>units or Output<sub></sub>units: The units of the variables, e.g., inches/second, dollars, years.

Input<sub></sub>data<sub></sub>types or Output<sub></sub>data<sub></sub>types: The data type of the i/o variable, e.g., integers, float, or string.

Input valid ranges or Output valid ranges: The range for which the variable produces a valid answer, e.g., an integer has a valid range from  32,767 to + 32,767, and a floating point variable restricted to positive values has a valid range of 0 to + 3.40282347E + 38.

Input<sub></sub>types or Output<sub></sub>types: The type of information the DSS expects/provides, e.g., variable or time series.

User/Site Requirements:

Hardware Requirements: Computing<sub></sub>platform: e.g., PC, Mac, HP, Sun, etc.

RAM: e.g., 8MB recommended/4 MB required Disk<sub></sub>storage: e.g., 25MB minimum

## Software Requirements:

Operating<sub></sub>system: e.g., Win95, Unix, etc. Application<sub></sub>names and version: Any other applications required for use with this DSS, e.g., Excel/4.0, Sybase, any spreadsheet.

Programming<sub></sub>languages: Any programming languages required by the user to run the DSS (might be required if the DSS requires customization), e.g., Java, C++.

File<sub></sub>transfer<sub></sub>software: e.g., ftp.

## Other Requirements:

User<sub></sub>skill<sub></sub>requirements: Any specialized skills users would require, e.g., Mathematical AI/knowledge engineering Functional/industrial knowledge.

Potential<sub></sub>User<sub></sub>Problems: Any known bugs or problems users report having with the DSS, e.g., if variables not defined correctly, the program crashes.

## Other Information:

Fee or Donation: e.g., 500£, \$25 or None.

Warrantee: e.g., Thirty-day limited warranty on disks.

References: References used in developing the DSS.

Related<sub></sub>DSS: Other DSS that solve similar problems or that could be used in conjunction with this DSS, e.g., Strategy at http://www.strategy.com.

Prior<sub></sub>users: Other people/companies that use this DSS, e.g., john.doe@asu.edu, Intel, General Dynamics.

Status: Status of the software, e.g., released, beta, out of service

Access<sub></sub>mode: Whether the DSS is downloadable or if users are allowed to use the DSS at the vendors site, e.g., available for download, discs shipped within 2 working days.

Licensing<sub></sub>agreement: This software is licensed for use on a single machine.

Limited liability: This software is sold ‘‘as is’’. All warranties either expressed or implied are disclaimed as to the software and its quality, performance, or fitness for any particular purpose.

## Vendor/Author Information:

Name Address Phone E-mail

## References

[1] Andy Acerman, Billsus, Gaffney, Hettich, Khoo, Kim, Klefstad, Lowe, Ludeman, Muramatsu, Omori, Pazzani, Semler, Starr, Yap, Learning probabilistic user profiles-applications for finding interesting web sites, notifying users of relevant changes to web pages, and locating grant opportunities, Al Magazine 18 (2) (1997) 47 – 56.

[2] A. Agresti, An Introduction to Categorical Data Analysis, Wiley, New York, NY, 1996.

[3] P. Ballou, H.L. Pazer, Modeling data and process quality in multi-input, multi-output information systems, Management Science 31 (2) (1985) 150– 162.

[4] S. Banerjee, A. Basu, Model type selection in an integrated DSS environment, Decision Support Systems 9 (1) (1993) 75 – 89.

[5] T. Berners-Lee, R. Cailliau, A. Luotonen, H.F. Neilsen, A. Secret, The World Wide Web, Communications of the ACM 37 (8) (1994) 76 – 82.

[6] R.W. Blanning, An entity-relationship approach to model management, Decision Support Systems 1 (2) (1986) 65 – 72.

[7] R.D. Burke, K.J. Hammond, V. Kulyukin, S.L. Lytinen, N. Tomuro, S. Schoenberg, Question answering from frequently asked question files, AI Magazine 18 (2) (1997) 57 – 66.

[8] S. Chari, R. Krishnan, Towards a logical reconstruction of structured modeling, Decision Support Systems 10 (2) (1993) 301– 317.

[9] D.R. Dolk, Model integration and a theory of models, Decision Support Systems 9 (1) (1993) 51– 63.

[10] Dublin Core Metadata Initiative http://purl.oclc.org/dc/(accesed November 15, 1999).

[11] R. Elmasri, S. Navathe, Fundamentals of Database Systems, The Benjamin/Cummings Publishing, Redwood City, CA, 1994.

[12] O. Etzioni, Moving up the information food chain: deploying softbots on the World Wide Web, AI Magazine 18 (2) (1997) 11 – 18.

[13] GILS, The Government Information Locator Service, Report to the Information Infrastructure Task Force, May 2, 1994 ftp://www.usgs.gov/pub/gils/gils1295.doc (accessed Novem ber 24, 1999).

[14] M. Goul, A. Philippakis, M. Kiang, D. Fernandes, R. Otondo, Requirements for the design of a protocol suite to automate DSS development on the World Wide Web: a client/server approach, Decision Support Systems 19 (3) (1997) 151–170.

[15] D. Gregg, M. Goul, A proposal for an open DSS protocol, Communications of the ACM 42 (11) (1999) 91–96.

[16] S. Hamilton, N.L. Chervany, Evaluating information system effectiveness — Part I, MIS Quarterly 5 (1981) 55 – 69.

[17] Y.U. Huh, F.R. Keller, T.C. Redman, A.R. Watkins, Data Quality, Information and Software Technology 38 (2) (1990) 559 – 565.

[18] B. Krulwich, Lifestyle finder: intelligent user profilling using large-scale demographic data, AI Magazine 18 (2) (1997) 37 – 56.

[19] P. Lynch, Searching the Internet, Scientific American — Special Issue: The Internet: Bringing Order from Chaos 276 (3) (1997) 50 – 51.

[20] F. Naumann, C. Rolker, Do metadata models meet IQ requirements? Proceedings of the Conference on Information Quality, 1999, pp. 99 – 114.

[21] P. Resnick, Filtering information on the Internet, Scientific American 276 (3) (1997) 26– 32.

[22] P. Resnick, J. Miller, PICS: Internet access control without censorship, Communications of the ACM 39 (10) (1996) 87– 93.

[23] M. Schriven, The methodology of evaluation: formative and summative evaluation, in: C.H. Weiss (Ed.), Evaluating Action Programs, Allyn and Bacon, Boston, MA, 1972.

[24] D.M. Strong, Y.W. Lee, R.Y. Wang, Data quality in context, Communications of the ACM 40 (5) (1997) 103 – 110.

[25] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Communications of the ACM 39 (11) (1996) 86– 95.

[26] R.Y. Wang, A product perspective on total data quality management, Communications of the ACM 41 (2) (1998) 58 – 65.

[27] R.Y. Wang, M.P. Reddy, H.B. Kon, Toward quality data: an attribute-based approach, Decision Support Systems 13 (3) (1995) 349– 372.

[28] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996) 5 – 34.

![](/api/attachments/UFCNMC3V/fulltext/images/c2fa9d738dac9b492b0ff3f87d113ce938051e01559704378ef9a3783dcc93dd.jpg)

Dawn G. Gregg is a visiting Assistant Professor at Arizona State University West. She received her Ph.D. in Computer Information Systems from Arizona State University, her MBA from Arizona State University West, and her BS in Mechanical Engineering from the University of California at Irvine. Prior to her doctoral studies, she was employed for 9 years as a research and development engineer. Her current research

focuses on how to organize and maintain Web-based content so that it can be used to better meet business needs. Her work has been published in Communications of the ACM and Information Systems Frontiers.

![](/api/attachments/UFCNMC3V/fulltext/images/2f253522243225ad35cc18cdf3dc4dca911bfc60c92fb47b6f95243995034501.jpg)

K. Michael Goul, Ph.D. is a Professor at Arizona State University. His research has been published in a wide range of academic and practitioner journals, and his recent research interest integrate the disciplines of decision support, distributed artificial intelligence, and web search agents. Dr. Goul has published papers in Communications of the ACM, Decision Sciences, Electronic Commerce and Organizational Computing, IEEE Expert, Journal of Management Infor-

mation Systems, and other journals. He has also co-edited a special issue of Decision Sciences on decision support and artificial intelligence, and served as conference chair for the Association for Information Systems Sixth Annual Americas Conference.

![](/api/attachments/UFCNMC3V/fulltext/images/d8c88dd4a096346719ac1d6428e46ed9d3d15b1a4a8b2dc65aba27c81f58211c.jpg)

Andy Philippakis is Professor of Information Management and Director of the ASU MBA Online program in the College of Business, Arizona State University. He has taught graduate courses in Information Management, Decision Support Systems and Object-Oriented Systems Design. He has authored several books on software, and his research publications include the Journal of Decision Support Systems, the Journal

of Organizational Computing and Electronic Commerce and the Journal of Intelligent Systems in Accounting, Finance and Management.
