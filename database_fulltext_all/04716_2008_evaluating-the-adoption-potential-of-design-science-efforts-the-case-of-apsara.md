---
otero_id: 4716
otero_key: "MBKANHUU"
title: "Evaluating the adoption potential of design science efforts: The case of APSARA"
authors: "Sandeep Purao; Veda C. Storey"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.04.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 44 (2008) 369– 381

www.elsevier.com/locate/dss

# Evaluating the adoption potential of design science efforts: The case of APSARA

Sandeep Purao <sup>a,⁎</sup>, Veda C. Storey <sup>b</sup>

<sup>a</sup> College of Information Sciences and Technology, The Pennsylvania State University, University Park, PA 16802, USA <sup>b</sup> J. Mack Robinson College of Business, Georgia State University, P.O. Box 4015, Atlanta, GA 30302, USA

Received 29 April 2007; accepted 29 April 2007 Available online 5 May 2007

## Abstract

Improving information systems design outcomes requires not only innovations in tools and methodologies, which are design science efforts, but also willingness on the part of potential developers to incorporate these innovations into their design practice. This is particularly true for reuse-based design, because of developers' reluctance to stray from their established modes of work. This research argues that the technology acceptance model (TAM) may be used to assess whether potential systems developers will adopt IT innovations that facilitate reuse-based conceptual design. We use the core technology-acceptance model to assess intent to use, based on the constructs of ‘ease of use’ and ‘usefulness’. One additional construct, compatibility, ensures that a key obstacle, minimizing changes to current design practice, is accounted for. We use a concrete instance of a previously proposed reuse-based design approach, APSARA, implemented in a prototype, as the basis for the study. The results indicate that significant contributors to the developers' willingness to adopt reuse-based design approaches include compatibility with current practice and ease of use of the reuse-based design approach. We discuss implications of these findings for using tools such as APSARA, and for the use of TAM as an evaluation mechanism for design science research efforts.

Keywords: Reuse; Conceptual design; APSARA; Technology acceptance

## 1. Introduction

Reuse, which involves reusing products of previous software projects<sup>1</sup> [42,50], represents the most potent approach to addressing the software development backlog [27,38,5,72]. Reuse, however, is difficult to incorporate into practice because of the resistance from designers to adopt knowledge outcomes that were ‘notinvented-here’ [39], particularly at the conceptual design stage of the system development process, which tends to be unstructured and creative. Although reusable artifacts such as analysis patterns [10] are readily available, developers rarely exploit these during the conceptual design of new applications. The reluctance to employ reuse-based design approaches in general, and for conceptual design in particular, can be traced to the perceived costs associated with reuse. If the perceived cost of reuse exceeds that of creating anew, the latter is preferred [66,67]. These ‘costs’ of reuse are considered significant by the developers when formal reuse<sup>2</sup> involves non-trivial adjustments to design practices [21,50,52]. Requiring such changes can prevent developers from accepting such reuse practices.

Reuse-based design approaches (e.g. [4,58,60]), which can be classified as design science efforts [34] are, therefore, often aimed at lowering these human obstacles to reuse. In this paper, we argue that a possible mechanism to evaluate a key property of such approaches – adoption potential – is the technology acceptance model (TAM) [13]. We employ three constructs from this research stream: perceived usefulness, ease of use, and compatibility with current practice. The first ensures that developers value the contribution of reuse to the design outcomes. The second ensures that developers do not need to expend significant effort to adopt the reuse-based design approach. The third ensures that the adoption of formal reuse does not require significant changes to current design practice. The rich stream of research on the technology acceptance model [9,54] demonstrates how the model can explain technology adoption by individuals and organizations. Hardgrave and Johnson [31] suggest that the model may be used in a predictive manner [15] to understand factors that contribute to adoption of systems development methodologies in general [32]. In this research, we employ the model in a similar manner, to predict the intentions of developers for adopting specific reuse-based conceptual design tools by measuring the antecedents of usefulness, ease of use, and compatibility. A previously developed reusebased conceptual design approach, APSARA [58,59], provides a design science artifact that forms the basis for developing the arguments. A prototype of APSARA is used as the basis for conducting the study described in this paper.

The objective of this research, thus, is to investigate the intentions of systems developers to adopt APSARA, a tool that facilitates reuse-based conceptual design. By doing this, we attempt to demonstrate how the technology-acceptance model may be used as an evaluation mechanism for outcomes from design science efforts.

The reminder of the paper is divided into five sections. Section 2 outlines background for the research, including an overview of design science efforts for reuse-based conceptual design, and a review of research related to the technology acceptance model (TAM). Section 3 develops the research model following TAM, describes the design science artifact used as the basis for the study, and outlines the study procedure. Section 4 describes the results highlighting key interpretations based on the constructs of usefulness, ease of use and compatibility along with intention to adopt. Section 5 discusses the implications for reuse-based design tools and for using TAM as an evaluation mechanism for design science research.

## 2. Background and related research

This section draws on prior work that informs the development of APSARA, a design science approach for facilitating reuse-based design [58,59], evaluation approaches for design science efforts, and the technology acceptance model (TAM) as a possible evaluation mechanism.

## 2.1. Obstacles to reuse-based design

Design with formal reuse involves making use of prior knowledge, often created by others in situations analogous to, although not necessarily identical to, the problem at hand [18]. Analogy making, therefore, is a fundamental cognitive process that aids in the reuse process. Analogy making assumes an intimate understanding of the source domain, the target domain, and a comparison of their structures and features in order to apply the knowledge from the former to the latter [26]. Analogy making can be difficult for developers [35] because it requires understanding a solution created by someone else, and adapting it to the problem at hand [75,40]. For non-trivial problems, analogy-making must be supplemented with the assembly of partial solutions using a compositional<sup>3</sup> approach [17] i.e. the adapted portions of prior knowledge must be integrated to create a new design [78,23,24,50,61]. The expected result of this process is a design produced at the conceptual design phase of an object-oriented application.

## 2.2. Approaches to reuse-based design

Design science research [34] efforts to overcome these obstacles are found in research on automated conceptual modeling [7], which formalizes approaches that assist developers in overcoming obstacles to reuse by, for example, generating the conceptual specification of an application from the users’ requirements, stated as natural language assertions [47]. The assertions can be used to build a conceptual schema [8] incrementally, through an interactive dialog with the developer. Tools have been developed that act as assistants to the developer, keeping track of details and making suggestions based upon embedded knowledge [43,46,71,52]. The process that most automated approaches use is a linear sequence of tasks with user requirements as the starting point [75]. These approaches struggle to achieve an expert level, even for logical design [6], and rarely come close to representing expertise for conceptual design [70,74]. Expert designers, however, employ behaviors not considered by these approaches. They categorize problem descriptions into standard abstractions [4], apply contextual rules [12], use abstractions of real world situations [45] and pattern-oriented mental models [69,70], and reason by analogy [57]. An approach that incorporates support for such behaviors is proposed by Purao and Storey [59], and Purao [58].

![](/api/attachments/MBKANHUU/fulltext/images/1a3ef168186ed2a38dd6b1ade1753ed3f72be914c281439a1ccd425e3cebd09a.jpg)  
Fig. 1. The APSARA methodology for reuse-based design.

## 2.3. The APSARA methodology<sup>4</sup> for conceptual design with analysis patterns

This research uses as an exemplar the approach suggested by Purao and Storey [59] and Purao [58]. The approach simulates analogy-making [48] and design by assembly during reuse-based design following a hybrid process that combines top-down and bottom-up development. Concepts from natural language requirements are used to decompose the requirements into smaller chunks (top-down) and reuse analysis patterns to constrain and guide this decomposition (bottom-up). The resulting process contains the phases: 1) retrieval of appropriate patterns, 2) instantiation of the patterns for the problem, and 3) synthesis of the instantiated patterns.

Fig. 1 shows the hybrid design process, as an extension of the process used in automated conceptual modeling [75]. The approach uses heuristics meant to support reuse-based design, grouped into three phases: Retrieval, Instantiation and Synthesis. The methodology has been implemented as a research prototype [2].

## 2.4. Evaluation of design science research effort

Evaluation is a crucial component of the design science process. Hevner et al [34] describe two different, although overlapping approaches and corresponding reasons for engaging in evaluation of design science efforts. The first posits evaluation as formative, i.e. as ‘essential feedback to the construction phase’ contributing to the generate-test cycle. The second posits evaluation as summative with approaches that include: observational, analytical, experimental, testing and descriptive [34]. As described, neither approach addresses an essential evaluation element, the potential for adoption of the artifact that may result from the design science efforts. While this is implicit in two methodologies (field study and case study) suggested for the category ‘observational evaluation’, there are several reasons why these two alternatives may be difficult to achieve in practice.

First, in several cases, the design science efforts result in artifacts that represent a ‘proof-of-concept’, which may not be sufficiently robust to insert into organizational environments [55]. Second, linkages with other components, necessary to insert the artifact in a technological complex, may not be in place; particularly if the effort represents a direction that is different and novel compared to current practice (consider, for example, the proposal for relational databases by Codd [11]). Third, depending upon the focus on the design research effort, finding the target set of organizations that are receptive to change or potential users who are knowledgeable can require significant investments of time and efforts (see, for example, participative action research approaches such as Iversen et al. [37] focusing on software process improvement).

A key concern, therefore, is how to evaluate design research outcomes, when the artifact cannot be immediately deployed in an organizational setting. While internal properties of the artifact may be assessed with analytical approaches, a useful alternative for external assessment is the technology acceptance model (TAM), which focuses on assessing the potential for adoption.

## 2.5. TAM as an evaluation mechanism for APSARA

The Technology Acceptance Model (TAM) [13], hypothesizes that system use is affected by behavioral intentions, which are themselves affected by attitudes towards use. These, in turn, are affected by beliefs about the system, specifically, Perceived Usefulness (PU) and Perceived Ease of Use (EOU). It, therefore, suggests that the correlation of PU and EOU with system use explains why people may accept or reject a new technology. The model draws on the theory of planned behavior/reasoned action [19] to understand the rational choices individuals make in choosing to use or discard an innovation [49]. The value of TAM as a model for explaining usage is evident in the consistency with which it has been applied [13,14,1,9,54,76]. Extensions to the core TAM model in recent years include TAM2 [73] as well as adaptations such as ISDAM [31] that apply TAM2 to object-oriented systems development methodologies.

![](/api/attachments/MBKANHUU/fulltext/images/1dfa229c0ed3329a40e4a6c9b431154a1e9f6eb7286f91e3306915284345f2be.jpg)  
Fig. 2. Research model for assessing adoption potential.

<table><tr><td>Table 1Hypotheses posited</td></tr><tr><td>Hypothesis</td></tr><tr><td>Perceived usefulness will have a positive influence on Intent to adopt.Ease of use will have a positive influence on Intent to adopt.Compatibility will have a positive influence on Intent to adopt.</td></tr></table>

In spite of the consistent and frequent use of TAM to explain the acceptance or rejection of information technology innovations [64, pp. 1137-1139], few have used TAM to predict the adoption potential of specific IT innovations. Such use of TAM is appropriate for our research because we are interested in evaluating the adoption potential of innovative reuse-based design tools such as APSARA.<sup>5</sup> Lacking an a priori reason for why TAM would not apply to assessing adoption intention<sup>6</sup>, we posit that TAM will allow us to predict the intention of developers to adopt APSARA. Because deploying APSARA in an organizational setting can require significant organizational commitment, our use of TAM is necessarily restricted. For example, we do not include constructs such as ‘subjective norm’ posited in the extended version (TAM2), and must rely on ‘potential’ instead of ‘actual’ users of APSARA. The next section elaborates on these choices and develops the research model.

## 3. Research model and procedure

To investigate potential developers' intentions to adopt APSARA [58], we use the core TAM model and devise an experimental procedure following prior research (e.g., Nance and Straub [54], Chin and Gopal [9]).

## 3.1. The research model

We consider an implementation of a reuse-based approach such as APSARA an IT innovation that facilitates reuse-based design (similar to a CASE tool that facilitates modeling). Here, it is necessary to make a distinction between a methodology and a tool. Fichman and Kemerer [20] describe a process innovation as one that changes the way a job is performed. Hardgrave and Johnson [31], drawing on this description and Ivari et al [36], argue that adopting a process innovation requires a much more radical change than adopting tools or technologies [56]. APSARA represents a tool that requires minimal change to the way in which software design is done.

We measure the constructs in TAM that would allow us to predict whether the proposed IT innovation (APSARA) may be accepted or rejected by the user population, which consists of potential designers. We identify three constructs as determinants of intention to use. These include the two original constructs in TAM, perceived usefulness (PU), and perceived ease of use (EOU), and the compatibility (CO) construct added in later research. The choice is dictated by two factors that are crucial for adopting formal reuse: (a) reducing the effort a developer must undertake for reusing artifacts created by someone else; and (b) ensuring that reuse does not require new ways of working [21,50]. Additional constructs such as trialability, visibility or image [51], are, therefore, not considered relevant for the purpose of this research. The three constructs are defined below.

Perceived Ease of Use (PEU) is “the degree to which a person believes that using a particular system would be free of effort” [13, p. 320].

Perceived Usefulness (PU) is “the degree to which a person believes that using a particular system would enhance his or her performance” [19, p. 320].

Compatibility (CO), is “the degree to which an innovation is perceived as being consistent with the existing values, needs and past experiences of potential adopters” [51].

Table 2  
Constructs and measures

<table><tr><td>Construct</td><td>Measure</td><td>Items</td><td>Type of Variable</td></tr><tr><td>Perceived Usefulness</td><td>Adapted from [13]</td><td>2</td><td>Likert (7)</td></tr><tr><td>Ease of Use</td><td>Adapted from [13]</td><td>4</td><td>Likert (7)</td></tr><tr><td>Compatibility</td><td>Adapted from [51]</td><td>4</td><td>Likert (7)</td></tr><tr><td>Intent to Use</td><td>Adapted from [13]</td><td>4</td><td>Likert (7)</td></tr></table>

Fig. 2 shows the model used to assess developers’ intention to adopt (use) a reuse-based design approach following the technology-acceptance model. The following hypotheses were expected to be true (Table 1).

The constructs are operationalized following specific items summarized in Chin and Gopal [[9], p. 48]. The items used in the survey appear in Appendix C. Table 2 summarizes the constructs and corresponding items.

## 3.2. The design research artifact used in the study

The implementation available in a prototype called APSARA (Automated Pattern Synthesis and Retrieval Assistant) [58,60] was used for this research. The artifact was seen as a tool, i.e. a concrete, reified instance of the underlying methodology. The intent of the study, thus, was not to assess whether the developers would adapt their work to the APSARA methodology, but rather, whether they would incorporate the APSARA tool in their design practice. The example below shows how the APSARA methodology, as implemented in the APSARA tool, could be applied to a large set of requirements represented as a set of use cases [62]. The example contained three use cases.<sup>7</sup> The APSARA tool was applied to each use case separately. The resulting designs could then be combined manually to construct the overall design.

Fig. 3 illustrates use of the prototype. It shows a separate ‘package’ for each of the three use cases (shown in Appendix A) within Rational Rose [62]. The largest class diagram, generated for use case 2, contained 11 classes and 10 relationships. Some objects were not instantiated (e.g., the ‘Actor’ object); others were instantiated differently (e.g. the ‘Participant’ object was instantiated as ‘clerk’ for use cases 1 and 3, and as ‘worker’ for use case 2).

Fig. 4 shows the progression from use cases to conceptual design with and without the use of the APSRA tool. The figure shows that the use of APSARA requires minimal changes to the task of constructing the conceptual design.

## 3.3. Study procedure

The procedure used in this research was an enhanced version of the procedure suggested by Chin and Gopal [9]. The subjects were shown a short written description of APSARA, followed by a demonstration of the research prototype (see Appendix B). The demonstration resulted in conceptual models of individual use cases. The subjects were then shown the merged model (mimicking the outcomes shown in the previous subsection), and asked to respond to a questionnaire. The procedure was, thus, similar to a free simulation exercise, where subjects are asked to make decisions by simulating a real-world situation as part of the experiment [22]. Since there are no preprogrammed treatments, the experiment allows the values of independent variables to range over the natural range of the subject's experience. In effect, the experimental tasks induce subject responses, which are then measured via the research instrument. [[25], p. 12].

![](/api/attachments/MBKANHUU/fulltext/images/13640398494f42095d65ff94a3706c27881b920c5ddb015a849c1c6f92770984.jpg)  
Fig. 3. Applying APSARA to a set of use cases.

Two examples were used for demonstration (see Appendix A for one of the examples). Data was gathered on multiple occasions from students, who were majoring in computer information systems or related disciplines, and completing specialized courses in object-oriented systems analysis and design at different public universities. A total of 69 respondents participated in the experiment over three separate occasions over a period of seven months. No compensation was provided to the subjects for participating in the experiment. Of the 69 respondents, 12 were dropped because they either did not complete the survey or gave inappropriate responses such as providing the same answer on all questions. The urban campus of the university, where the survey was conducted, meant that the students were non-traditional, exhibited a strong commitment to the IT profession with an average of 1.56 years of experience in industry, and were older than the younger, traditional students. Table 3 shows these demographic characteristics.

![](/api/attachments/MBKANHUU/fulltext/images/b1a18890d164249086798573a3246a395e884848d0134785008dd69f44bdd019.jpg)  
Fig. 4. The Conceptual design task with and without APSARA.

There is no reliable way to assess exactly how representative our participants are of the larger population of developers (see similar arguments from Guindon [30]). There is no standard type of individual who becomes a software developer. They can differ in education, experience and attitude. The participants had some prior experience in the IS industry. Many were continuing work while obtaining a specialized degree in MIS. They were, thus, representative of at least some segment of the population of actual developers. It is, indeed, possible to argue that the results may be more robust if the sample were to include developers, who are surveyed or interviewed at their workplace. Our choice of the sample was, thus, dictated by access to a pool of potential developers, who were enrolled in a specialized degree in MIS.

Demographic characteristics of respondents (Based on 57 usable surveys)

<table><tr><td>Feature</td><td>Descriptive statistics</td></tr><tr><td>Age</td><td>Average: 23.3 Low: 19, High: 31</td></tr><tr><td>Gender</td><td>Male: 39, Female: 18</td></tr><tr><td>Experience</td><td>Average (number of years): 1.56</td></tr></table>

Table 4  
Descriptive Statistics (see Appendix I)

<table><tr><td>Construct</td><td>Item</td><td>Mean</td><td>S.D.</td><td>Average</td></tr><tr><td rowspan="2">Intent to Use</td><td>IU1</td><td>2.3</td><td>0.829</td><td>2.56</td></tr><tr><td>IU2</td><td>2.82</td><td>0.956</td><td></td></tr><tr><td rowspan="4">Perceived Usefulness</td><td>PU1</td><td>2.29</td><td>0.825</td><td>2.74</td></tr><tr><td>PU2*</td><td>4.98</td><td>1.382</td><td></td></tr><tr><td>PU3</td><td>2.46</td><td>0.934</td><td></td></tr><tr><td>PU4*</td><td>4.82</td><td>1.309</td><td></td></tr><tr><td rowspan="4">Ease of Use</td><td>EU1</td><td>2.61</td><td>0.908</td><td>2.69</td></tr><tr><td>EU2</td><td>3.04</td><td>1.206</td><td></td></tr><tr><td>EU3</td><td>2.55</td><td>0.913</td><td></td></tr><tr><td>EU4</td><td>2.57</td><td>1.024</td><td></td></tr><tr><td rowspan="4">Compatibility</td><td>CO1</td><td>2.84</td><td>1.108</td><td>3.01</td></tr><tr><td>CO2*</td><td>4.91</td><td>1.133</td><td></td></tr><tr><td>CO3*</td><td>4.89</td><td>1.330</td><td></td></tr><tr><td>CO4</td><td>3.02</td><td>1.183</td><td></td></tr></table>

Asterisk indicates reverse worded items. Average adjusts for the reversed scale.

## 4. Results

Initial descriptive statistics were computed to provide an indication of whether the data confirms to the general notions captured by the items for each construct. Table 4 shows these statistics. The responses show that on the scale that varied from extremely likely (1) to extremely unlikely (7), all items exhibit a tendency towards agreement; that is, potential adopters indicate they are likely to use it (2.56 on a scale of 1–7), and they perceive it to be useful (2.74), easy to use (2.69), and compatible with their work (3.01).

Table 5  
Rotated component matrix

<table><tr><td>Components</td><td>CO</td><td>EU</td><td>IU</td><td>PU</td></tr><tr><td>IU1</td><td>.189</td><td>.238</td><td>.846</td><td>3.547E-02</td></tr><tr><td>IU2</td><td>.374</td><td>.199</td><td>.676</td><td>8.202E-02</td></tr><tr><td>PU1</td><td>.381</td><td>-4.318E-03</td><td>.554</td><td>.443</td></tr><tr><td>PU2</td><td>-.155</td><td>-7.468E-02</td><td>-.286</td><td>-.701</td></tr><tr><td>PU3</td><td>.276</td><td>.180</td><td>.550</td><td>.522</td></tr><tr><td>PU4</td><td>-.341</td><td>6.085E-02</td><td>.120</td><td>-.734</td></tr><tr><td>EU1</td><td>.172</td><td>.651</td><td>.214</td><td>.320</td></tr><tr><td>EU2</td><td>.274</td><td>.535</td><td>.210</td><td>.446</td></tr><tr><td>EU3</td><td>.111</td><td>.891</td><td>4.958E-02</td><td>-.152</td></tr><tr><td>EU4</td><td>.121</td><td>.905</td><td>.170</td><td>-5.529E-03</td></tr><tr><td>CO1</td><td>.791</td><td>.124</td><td>.232</td><td>.235</td></tr><tr><td>CO2</td><td>-.841</td><td>-5.138E-02</td><td>-.257</td><td>-.281</td></tr><tr><td>CO3</td><td>-.787</td><td>-.216</td><td>-.269</td><td>-.237</td></tr><tr><td>CO4</td><td>.767</td><td>.285</td><td>.192</td><td>.151</td></tr></table>

Table 6  
Summary of regression results

<table><tr><td></td><td>Unstandardized coefficients B</td><td>S.E.</td><td>Standardized coefficients beta</td><td>t</td><td>Sig.</td></tr><tr><td>(Constant)</td><td>2.386</td><td>.556</td><td></td><td>4.295</td><td>.000</td></tr><tr><td>PU</td><td>-4.829E-02</td><td>.091</td><td>-.067</td><td>-.533</td><td>.597</td></tr><tr><td>EU</td><td>.265</td><td>.123</td><td>.268</td><td>2.156</td><td>.036</td></tr><tr><td>CO</td><td>.306</td><td>.108</td><td>.399</td><td>2.839</td><td>.006</td></tr></table>

Additional analysis was performed to understand whether the items map to the underlying constructs, and whether the causal relationships postulated in TAM can be predicted from the data gathered. The responses were factor analyzed fixing the number of factors at four. The principal component analysis was conducted with the Varimax method with Kaiser Normalization. Table 5 shows the rotated component matrix.

All items loaded as expected (shaded and bold-faced) except PU1 and PU3 (shaded but not bold-faced). These were, therefore, dropped from subsequent analysis. With the remaining items, the research model was tested using a multiple regression analysis. A test of this model yielded an adjusted R-squared of 33.9%; thus, it explained 33.9% of the variance in the dependent variable, Intent to Use (IU). An ANOVA was performed to test for significance. The F-test indicated that the result was significant. The results were significant at the alpha = 0.05 level $( p = ~ 0 . 0 0 0$ $F { = } 1 0 . 5 8 3$ , df = 56). Individual t-tests conducted on the constructs revealed that Ease of Use (EU) and Compatibility (CO) were significant predictors of Intent to Use (IU). The corresponding values were t=2.156, $\scriptstyle { p = 0 . 0 3 6 }$ for Ease of Use (EU), and t=2.839, $_ { p = 0 . 0 0 6 }$ for Compatibility (CO). However, Perceived Usefulness (PU) was not found to be a significant predictor of Intent to Use (IU) with the values t = 0.533, $p { = } 0 . 5 9 7$ . Table 6 summarizes these results.

The hypotheses posited as true following TAM were, therefore, partially supported. The antecedents posited in the causal model yielded the values expected (Table 4); the causal relationships (Table 6) among the constructs were supported for H2 and H3, but not for H1.

## 5. Discussion

The results provide interesting insights into the rationale software developers might employ in their decision to adopt tools such as APSARA that support formal reuse. The results of the survey show that potential developers exhibit a strong intention towards adoption. Two constructs appear to determine their intent to adopt. These are ‘ease of use’ and ‘compatibility’. The ease of use construct refers to the extent to which a potential system developer expects the use of a reuse-based design approach to be free of effort. The compatibility construct refers to the degree to which the reuse-based design approach is perceived as being consistent with the existing design practice. These are greater contributors to the intent to use than perceived usefulness. Conceptual design is a difficult task. Although reusable artifacts such as analysis patterns are available, they have not lead to extensive reuse during conceptual design. A key obstacle to realizing this benefit has been the high perceived ‘cost of reuse' [66]. Prima facie, our results confirm the importance of overcoming this cost. It is, however, possible that the usefulness construct becomes significant if professional developers are used as subjects. Interestingly, the results are compatible with findings from Riemenschneider et al. [64], who found that usefulness was not a significant construct in determining acceptance of object-oriented systems development methodologies.

The results are also true given what we know about resistance to reuse. Even when it has been demonstrated that reuse can potentially lead to significant benefits, developers are reluctant to engage in formal reuse, a syndrome sometimes referred to as “notinvented-here” [39,29, p. 553]. Studies repeatedly confirm that mere demonstration of benefits of reuse is not sufficient to entice developers to engage in formal reuse [29,50,68,67]. The theme is echoed in studies related to knowledge work, where a significant obstacle to use of knowledge repositories has been adjustments to work practices that deters potential users from engaging with the knowledge repository, when faced with significant time pressure and availability of alternatives such as knowledge networks [3]. A possibility is to consider ‘attitude’ to investigate individual and organizational adoption of technology [77]. A second possible interpretation of the results may be that perceived usefulness is considered as a prerequisite for, but not a significant determinant of, the intent to adopt. This can be true when alternatives are available to a developer such as relying on his/her own expertise or informal networks [3] versus using a tool such as APSARA that facilitates reuse-based design. If all alternatives are perceived to be equally useful, the alternative involving few adjustments to work practices is likely to win. The importance of minimizing disruptions to current work practices has also been emphasized in the specific context of reuse-based design by Frakes and Terry [21], Mili et al. [50], Morisio et al [53], and Ravichandran and Rothenberger [63].

The results also suggest a novel role for tools such as APSARA. These tools may be useful to introduce developers to reuse-based design in a familiar (see ‘compatibility) and non-demanding (see ‘ease of use’) manner. The lack of significance attached to perceived usefulness for deciding about adoption may mean that developers may treat these tools, not as a significant contributor to effective design outcomes, but rather, as a first step towards learning about reusebased design.<sup>8</sup> The significant influence of ‘compatibility’ and ‘ease of use’ on ‘intention to adopt’, on the other hand, suggests that developers may value these tools as vehicles to learn about formal reuse. This is particularly true for conceptual design, which involves codification and abstraction of knowledge such as the analysis patterns that APSARA contains. The reuse of these forms of knowledge can require much learning that tools similar to APSARA can facilitate. Positioning the use of APSARA as learning can overcome the conundrum developers may face while attempting to reuse analysis patterns during conceptual design. As novices, the analysis patterns provide useful codifications of prior knowledge. However, they are difficult to understand and reuse. As experts, the developers may have already internalized the knowledge codified in the analysis patterns making tools such as APSARA superfluous. A novel role that tools such as APSARA can, therefore, play may be helping developers learn the craft of reuse-based design.

For research that focuses on TAM, the results provide different contributions. Much prior work on TAM, which has dealt with general IT applications (e.g. email [41], spreadsheet [49], technology for the disabled [28]), general IT usage [65], or systems development methodologies [31]. In contrast, our work focuses on knowledgeable users of IT (potential information systems developers) for a specific IT innovation (tool) that facilitates the IS development process but does not radically alter it. The results suggest that for the scenarios considered in this work, the constructs of Ease of Use and Compatibility are better predictors of Intent to Use than the muchemphasized constructs of Perceived Usefulness or Relative Advantage [33]. Our results are consistent, though, with those for software development methodologies [31], and provide greater specificity to the argument in Davis and Venkatesh [16] in the context of evaluating design research efforts. Further studies are clearly necessary to shed light on the relative contribution of these constructs. A second contribution to the discourse on research on TAM is the manner in which we have used TAM in our study, namely to explore the adoption potential of an IT innovation. Few studies (e.g. [65,31]) have attempted to apply TAM in this manner. However, in Rose and Straub [65], the constructs measured included actual use of IT, and in Hardgrave and Johnson [31], two out of three respondents had used the object-oriented software development methodology. In contrast, in the study reported in this paper, none of the users had any experience with APSARA because it represents a design science effort that is not widely available. The study, thus, focuses on predicting the potential for adoption of an IT innovation.

The study we have outlined, and the results, suggest a possible role that models such as TAM can play for design science research. As Hevner et al. [34] suggest, a number of criteria may be used to evaluate these efforts. One of these evaluation categories is “experimental” evaluation, which includes evaluating properties such as usability. They are, however, silent on other specific mechanisms that may be of value for evaluating the design science outcomes. A core argument in our paper has been the importance of assessing the willingness of potential adopters of the technology to actually use the technology. We have, therefore, suggested TAM as a possible mechanism to evaluate the outcomes of design science. A large number of design science efforts never proceed beyond the laboratory, ending the research cycle as a research prototype. In spite of calls to move the outcomes into the marketplace [55], academics find it difficult to invest the time required to do so. Convincing the research community and practitioners of the potential for adoption – with TAM or other models – can go a long way towards focusing greater attention to such outcomes.

Like all research, ours has its limitations. First, the participants in the study were recruited from a student population. Similar use of student subjects is, however, reported in other studies (e.g. [60,25]). Second, the result suggesting ‘compatibility’ as a contributor to intention to adopt may be questioned based on the use of student subjects. We recognize this as a limitation but stress that the population from which the sample was drawn consisted of non-traditional students, who had at least some industry experience. Furthermore, the notion of compatibility maps to changes required to a design task, specifically that of constructing the conceptual design, which, arguably, does not change between students and practitioners, except at a cognitive level.

In summary, this research makes two key contributions. First, it identifies the constructs of ease of use and compatibility as significant contributors to the intention to adopt reuse-based design tools. In doing so, it shows that the adoption decision will require more than a demonstration of usefulness or relative advantage. Second, it shows application and use of the technologyacceptance model to assess the adoption potential of IT innovations. Clearly, larger scale studies, including introductions of innovations such as APSARA in the field, are needed to further explore these constructs. The study reported in this paper describes a first step in this direction.

## Acknowledgements

The authors wish to thank the editor and reviewers for their comments on this paper. They also thank Arun Rai for his comments on earlier drafts, Detmar Straub for his counsel on research design, and Cecil Chua for his help in the data analysis. This research was supported by Georgia State University.

## Appendix A. Applying APSARA to a set of Use Cases

<table><tr><td colspan="2">Domain: human resources</td></tr><tr><td>Use Case 1: create work teams</td><td>Use Case 2: assign teams to projects</td></tr><tr><td>1 clerk enters new team</td><td>1 clerk enters a project</td></tr><tr><td>2 system displays available employees</td><td>2 system displays list of teams</td></tr><tr><td>3 clerk assigns each employee to a team</td><td>3 clerk selects a team</td></tr><tr><td>4 system records employees and teams</td><td>4 systems assigns the team to project</td></tr><tr><td></td><td>5 system updates team status</td></tr><tr><td colspan="2">Use Case 3: record job progress</td></tr><tr><td>1 clerk selects a job</td><td></td></tr><tr><td>2 clerk records worker on a job</td><td></td></tr><tr><td>3 system updates job progress</td><td></td></tr><tr><td>4 system updates job status</td><td></td></tr></table>

## Appendix B. Description and demonstration

The following script was used to introduce the subjects to the APSARA prototype.

B.1. Description of research on reuse-based design and the APSARA prototype

## B.1.1. Reuse-based system development

Development of computer-based information systems requires significant efforts from human analysts and designers. Information technology support in the form of CASE Tools (e.g. Rational Rose) has been available for documenting work products of systems developers for some time now. Automating the process of software development, particularly in the early stages of conceptual design is, however, still difficult.

## B.1.2. Research on improving reuse

One research project aimed at developing such support is being carried out at ABC State University. Currently, it exists, in a limited capacity, as a research prototype under the name APSARA: Automated Pattern Synthesis and Retrieval Assistant. It automates the process of reuse of Analysis Patterns suggested by

![](/api/attachments/MBKANHUU/fulltext/images/c690887459317436d979024cb4070f3648c6c7557b3d1e45630e068897dedaf4.jpg)  
Fig. I.1. Results obtained by applying APSARA to three use cases in the Human Resources Domain.

Coad. Under the covers, it uses several techniques including text parsing, automated reasoning and intelligent heuristics.

## B.1.3. Automated pattern synthesis and retrieval assistant

The tool, APSARA, automates the process of reusebased design by providing computer-based support for three tasks: retrieval, instantiation and synthesis.

1. Retrieval — identification of appropriate analysis patterns based on natural language descriptions provided by the analysts, for example, as use cases.

2. Instantiation — making the retrieved analysis patterns specific to the problem being considered, based on the description contained in the use case.

3. Synthesis — connecting the instantiated patterns to create a preliminary class diagram for each use case.

These tasks are carried out as a sequence of steps, using clearly marked buttons and following instructions shown in the tool. To make the process transparent to the designer, there are several (more than three) steps in the tool. Currently, the tool does not allow the designer to intervene in the process. The outputs are generated in a text format that may then be imported into a CASE tool such as Rational Rose.

## B.1.4. Using APSARA

Using APSARA, system designers may type a use case description into the tool, and follow the instructions to generate a preliminary class diagram for each use case. Since this is an automated tool that cannot possess ‘common-sense’, errors are possible. The designer can check the class diagrams and make any adjustments as necessary. The designer’s job is, then, to combine the individual class diagrams to create the complete class diagram.

## B.1.5. Demonstration

The demonstration will involve using APSARA to create class diagrams based on several use cases. Following the demonstration, the outputs will be shown as published from the CASE tool, where they are imported.

## B.1.6. Feedback

Your feedback is sought following the demonstration. Your impressions and intentions about the tool will help move the research forward. Thank you for your participation!

## Appendix C. Survey instrument

Assuming that any decision to use APSARA would be totally up to you, and APSARA was available

<table><tr><td rowspan="2" colspan="2">Construct and item</td><td colspan="3">Likely</td><td rowspan="2">Neither</td><td colspan="3">Unlikely</td></tr><tr><td>Extremely</td><td>Quite</td><td>Somewhat</td><td>Somewhat</td><td>Quite</td><td>Extremely</td></tr><tr><td>IU1</td><td>How would you rate your potential to use it?</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IU2</td><td>Would you use it often?</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PU1</td><td>I would find APSARA useful on the job.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PU2</td><td>Using APSARA would not enhance my effectiveness on the job.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PU3</td><td>Using APSARA on the job would increase my productivity.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PU4</td><td>Using APSARA would not improve my performance on the job.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EU1</td><td>I would find APSARA easy to use.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EU2</td><td>I would find it easy to get APSARA to do what I want to do.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EU3</td><td>Learning to use APSARA would be easy for me.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EU4</td><td>It would be easy for me to be skillful at using APSARA.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CO1</td><td>Using APSARA would be compatible with my own system design work.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CO2</td><td>Using APSARA would not be compatible with my current work on system design.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CO3</td><td>Using APSARA would not fit well with the way I like to carry out my system design work.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CO4</td><td>Using APSARA would fit my work style for system design.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notes: Items PU2, PU4, CO2, and CO3 are reverse worded. Questions requesting demographic information are not shown.

## References

[1] D.A. Adams, R.R. Nelson, P.A. Todd, Perceived usefulness, ease of use and usage of information technology: a replication, MIS Quarterly 16 (2) (1992) 227–247.

[2] APSARA, Heuristics for automated pattern retrieval and synthesis, 2005 Available at http://purao.ist.psu.edu/APSARA heuristics. Accessed 15 June 2005.

[3] J. Bansler, E. Havn, Sharing best practices: an empirical study of it-support for knowledge sharing, The 9th European Conference on Information Systems, Bled, Slovenia, June 27–29 2001.

[4] D. Batra, J. Davis, Conceptual data modeling in database design: similarities and differences between expert and novice designers, International Journal of Man-Machine Studies, vol. 37, 1992, pp. 83–101.

[5] J. Bosch, Design and Use of Software Architectures: Adopting and Evolving a Product-Line Approach, Addison Wesley, 2000.

[6] M. Bouzeghoub, Using expert systems in schema design, in: P. Loucopoulos, R. Zicari (Eds.), Conceptual Modelling, Databases, and CASE, Wiley, 1992, pp. 465–487.

[7] J.A. Bubenko Jr., B. Wangler, Research directions in conceptual specification development. Chapter 17, in: P. Loucopolous, R. Zicari (Eds.), Conceptual Modeling, Databases, and CASE: An Integrated View of Information Systems Development, Wiley, 1992.

[8] P. Chen, The entity-relationship model-toward a unified view of data, ACM Transactions on Database Systems 1 (1) (March 1976) 9–36.

[9] W. Chin, A. Gopal, Adoption intention in GSS: relative importance of beliefs, DataBase for Advances in Information Systems 26 (2,3) (May/August 1995) 42–64.

[10] P. Coad, et al., Object Models: Strategies, Patterns, & Applications, Prentice Hall, 1995.

[11] E.F. Codd, A relational model of data for large shared data banks, Communications of the ACM 13 (6) (1970) 377–387.

[12] W.G. Cole, Metaphor graphics and visual analogy for medical data, InfoFair, Salt Lake City, April 1988.

[13] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (September 1989) 319–339.

[14] F.D. Davis, User acceptance of information technology: system characteristics, user perceptions and behavioral impacts, International Journal of Man-Machine Studies 38 (1993) 1–13.

[15] F.D. Davis, V. Venkatesh, Toward pre-prototype user acceptance testing of new information systems: implications for software project management, IEEE Transactions on Engineering Management 51 (1) (2004) 31–46.

[16] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Management Science 35 (8) (August 1989) 982–1003.

[17] B. De Sutter, B. De Bus, K. De Bosschere, Sifting out the mud: low level C++ code reuse, ACM SIGPLAN Notices, Proceedings of the 17th ACM Conference on Object-Oriented Programming, Systems, Languages, and Applications, vol. 37(11), 2002.

[18] G. Fischer, Cognitive view of reuse and design, IEEE Software (July 1987) 22–39.

[19] M. Fishbein, I. Ajzen, Belief, Attitude, Intentions and Behavior: An Introduction to Theory and Research, Addison-Wesley, Boston, 1975.

[20] R. Fishman, C. Kemerer, The assimilation of process innovations: an organizational learning perspective, Management Science 43 (10) (1997) 1345–1363.

[21] W.B. Frakes, C. Terry, Software reuse: metrics and models, ACM Computing Surveys 28 (2) (1996) 415–435.

[22] H.L. Fromkin, S. Streufert, Laboratory Experimentation, Handbook of Industrial and Organizational Psychology, Rand McNally Publishing Company, Inc., Chicago IL, 1976.

[23] M. Gaedke, J. Rehse, Supporting compositional reuse in component-based web engineering, 2000 ACM Symposium on Applied Computing (SAC 2000), Villa Olmo, Como, Italy, March 2000, pp. 19–21.

[24] M. Garey, D. Johnson, Computers and Intractability, Freeman, San Francisco, CA, 1979.

[25] D. Gefen, D. Straub, M. Boudreau, Structural equation modeling and regression: guidelines for research practice, Communications of the AIS 4 (7) (August 2000).

[26] D. Gentner, Structure-mapping: a theoretical framework for analogy, Cognitive Science 7 (2) (1983) 155–170.

[27] C.W. Gibbs, Software's chronic crisis, Scientific American (Sept. 1994) 86–95.

[28] T. Goette. Determining Factors in the Successful Use of Adaptive Technology by Individuals with Disabilities: A Field Study. Unpublished Dissertation, Georgia State University (1995).

[29] M.L. Griss, Software reuse: from library to factory, IBM Systems Journal 32 (4) (1993) 548–566.

[30] R.D. Guindon, Designing the design process: exploiting opportunistic thoughts, Human-Computer Interaction 5 (1990) 305–344.

[31] B.C. Hardgrave, R.A. Johnson, Towards an information systems development acceptance model: the case of object-oriented systems development, IEEE Transactions on Engineering Management 50 (3) (August 2003) 322–336.

[32] B.C. Hardgrave, F.D. Davis, C.K. Riemenschneider, Investigating determinants of software developers' intentions to follow methodologies, Journal of Management Information Systems 20 (1) (Summer 2003) 123–151

[33] A.R. Hendrickson, P.D. Massey, T.P. Cronan, On the test–retest reliability of perceived usefulness and perceived ease of use scales, MIS Quarterly 17 (2) (1993) 227–230.

[34] A. Hevner, S. March, J. Park, S. Ram, Design science research in information systems, MIS Quarterly 28 (1) (March 2004) 75–105.

[35] G. Irwin, The role of similarity in the reuse of object-oriented analysis models, Journal of Management Information Systems 19 (2) (2002) 219–248.

[36] J. Iivari, R. Hirschheim, H. Klein, A paradigmatic analysis contrasting information systems development approaches and methodologies, Information Systems Research 9 (2) (1998) 164–193.

[37] J. Iversen, L. Mathiassen, P.A. Nielsen, Managing risks in software process improvement: an action research approach, MIS Quarterly 28 (3) (2004) 395–433.

[38] I. Jacobson, M. Griss, P. Johnsson, Software Reuse: Architecture Process and Organization for Business Success, Addison Wesley, 1997.

[39] K. Joel, The Not-Invented-Here Syndrome in Software Development Practice, http://www.joelonsoftware.com/printerFriendly/articles/ fog0000000007.html. Accessed on 15 September 2004.

[40] P. Johannesson, P. Wohed, The deontic pattern — a framework for domain analysis in information systems design, Data and Knowledge Engineering 31 (2) (1999) 135–153.

[41] E. Karahana. Evaluative Criteria and User Acceptance of End-User Information Technology: A Study of End User Cognitive and Affective Processes. Unpublished Dissertation, University of Minnesota (1993).

[42] C. Krueger, Software reuse, ACM Computing Surveys, vol. 24. No. 2, June 1993, pp. 131–184.

[43] O.B. Kwon, S.J. Park, RMT: a modeling support system for model reuse, Decision Support Systems 16 (2) (February 1996) 131–153.

[44] D. Lenat, et al., CYC: toward programs with common sense, Communications of the ACM. Special Issue on Natural Language Processing, vol. 33. No. 8, Aug. 1990, pp. 30–49.

[45] M. Lloyd-Williams, Exploiting domain knowledge during the automated design of object-oriented databases, Proceedings of the 16th International Conference on Conceptual Modeling (ER'97), Los Angeles, Springer-Verlag, November 3–6 1997.

[46] M. Lloyd-Williams, P. Beynon-Davis, Expert systems for database design: a comparative review, Artificial Intelligence Review 6 (3) (1992) 263–283.

[47] M. Lowry and R. McCartney. 1991. eds. Automating Software Design. AAAI Press/MIT Press (1991).

[48] A. Maiden, C. Sutcliffe, Exploiting reusable specifications through analogy, Communications of the ACM, vol. 35. No. 4, April 1993, pp. 55–64.

[49] K. Mathieson, Predicting user intentions: comparing the technology acceptance model with the theory of planned behavior, Information Systems Research 2 (3) (1991) 173–191.

[50] H. Mili, et al., Reusing software: issues and research directions, IEEE Transactions on Software Engineering (June 1995) 528–562.

[51] G.C. Moore, I. Benbasat, Development of an instrument to measure the perceptions of adopting an information technology innovation, Information Systems Research 2 (3) (1991) 192–222.

[52] B. Morel, P. Alexander, Automating component adaptation for reuse, Proceedings. 18th IEEE International Conference on Automated Software Engineering, 2003, Oct. 6–10 2003, pp. 142–151.

[53] M. Morisio, M. Ezran, C. Tully, Success and failure factors in software reuse, IEEE Transactions on Software Engineering 28 (4) (April 2002) 340–357.

[54] W.D. Nance, D.W. Straub, An investigation of task-technology fit and information technology choices in knowledge work, Journal of Information Technology Management (7:3 & 4) (1996) 1–14.

[55] J. Nunamaker, Going the last mile: the opportunity to create valuable knowledge, Keynote speech at the Workshop of Information Technologies and Systems, December 15 2001.

[56] W.J. Orlikowski, CASE tools as organizational change: Investigating incremental and radical changes in systems development, MIS Quarterly 17 (3) (1993) 309–340.

[57] M.J. Prietula, H.A. Simon, The experts in your midst, Harvard Business Review (Jan–Feb. 1989) 120–124.

[58] S. Purao, Aweb-based tool to automate system design via intelligent pattern retrieval and synthesis, Data Base 29 (4) (Fall 1998) 45–57.

[59] S. Purao, V. Storey, Intelligent support for retrieval and synthesis of patterns for object-oriented design, Proceedings of 16th International Conference on Conceptual Modeling- ER'97, Sringer-Verlag, Los Angeles, California, November 2 – 7 1997.

[60] S. Purao, V. Storey, T. Han, Improving analysis pattern reuse in conceptual design: augmenting automated processes with supervised learning, Information Systems Research 14 (3) (Sept. 2003) 269–290.

[61] M. Ramesh, H. Raghav Rao, Software reuse: issues and an example, Decision Support Systems 12 (1) (August 1994) 57–77.

[62] Rational. http://www.ibm.com/rational. Accessed, 15 June 2005.

[63] T. Ravichandran, M.A. Rothenberger, Software reuse strategies and component markets, Communications of the ACM 46 (8) (2003) 109–114.

[64] C.K. Riemenschneider, B.C. Hardgrave, F.D. Davis, Explaining developer acceptance of formal software methodologies: a comparison of five theoretical models, IEEE Transactions on Software Engineering 28 (12) (December 2002) 1135–1145.

[65] G. Rose, D.W. Straub, Predicting general IT use: applying TAM to the Arabic world, Journal of Global Information Management 6 (3) (Summer 1998) 39–46.

[66] M. Rothenberger, Project-level reuse factors: drivers for variation within software development environments, Decision Sciences Journal 34 (1) (Winter 2003).

[67] M. Rothenberger, K.J. Dooley, A performance measure for software reuse projects, Decision Sciences Journal 30 (4) (Fall 1999) 1131–1153.

[68] M. Rothenberger, K.J. Dooley, U.R. Kulkarni, N. Nada, Strategies for software reuse: a principal component analysis of reuse practices, IEEE Transactions on Software Engineering (September 2003).

[69] W.B. Rouse, N.M. Morris, On looking into the black box: prospects and limits in the search for mental models, Psychological Bulletin, vol. 100(3), 1986, pp. 349–361.

[70] V.C. Storey, C. Thompson, S. Ram, Understanding database design expertise, Data and Knowledge Engineering 16 (August 1995) 97–124.

[71] V.C. Storey, R.C. Goldstein, R.L. Chiang, D. Dey, S. Sundaresan, Database design with common sense business reasoning and learning, ACM Transactions on Database Systems 22 (4) (December 1997) 471–512.

[72] M. Szyperski, Component-based Software Engineering, Addison-Wesley, 1999.

[73] V. Venkatesh, F. Davis, A theoretical extension of the technology acceptance model: four longitudinal field studies, Management. Science 46 (2) (2000) 186–204.

[74] A. Vinze, S. Karma, Domain engineering for developing software repositories: a case study, Decision Support Systems 33 (1) (May 2002) 55–69

[75] P. Wohed, Conceptual patterns for reuse in information systems analysis, Proceedings of CAiSE 2000, 2000, pp. 157–175, Stockholm, Sweden.

[76] I. Wu, J. Chen, An extension of trust and TAM model with TPB in the initial adoption of on-line tax: an empirical study, International Journal of Human-Computer Studies 62 (6) (June 2005) 784–808.

[77] H. Yang, Y. Yoo, It's all about attitude: revisiting the technology acceptance model, Decision Support Systems 38 (1) (October 2004) 19–31.

[78] P. Zave, M. Jackson, Conjunction as composition, ACM Transactions on Software Engineering and Methodology 2 (4) (October 1993) 379–411.

Sandeep Purao is an Associate Professor of Information Sciences and Technology at the College of IST, Penn State University, University Park, PA. His research focuses on the design and evolution of complex technoorganizational systems. He is currently the graduate student adviser at the College of IST at Penn State University. His research has been published in several journals including ACM Computing Surveys, IEEE Transactions on Systems, Man and Cybernetics, Information Systems Research, Journal of MIS, Information and Organizations, Decision Support Systems, Information Systems Frontiers, Information and Management.

Veda C. Storey is a Tull Professor of Computer Information Systems, College of Business Administration, and Professor of Computer Science, Georgia State University. She has Research interests in database management systems, intelligent systems, Semantic Web, and ontology development. Her research has been published in ACM Transactions on Database Systems, IEEE Transactions on Knowledge and Data Engineering, Information Systems Research, Management Information Systems Quarterly, Data and Knowledge Engineering, Decision Support Systems, the Very Large Data Base Journal, and Information & Management. She has served on the editorial board of several journals including Information Systems Research, MIS Quarterly, Management Science, DataBase, and Decision Support Systems.
