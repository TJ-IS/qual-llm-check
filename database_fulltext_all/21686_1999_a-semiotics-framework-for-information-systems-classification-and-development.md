---
otero_id: 21686
otero_key: "4G2VK8WE"
title: "A semiotics framework for information systems classification and development"
authors: "Terence M Barron; Roger H.L Chiang; Veda C Storey"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00088-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A semiotics framework for information systems classification and development

Terence M. Barron <sup>a,)</sup>, Roger H.L. Chiang <sup>b,1</sup>, Veda C. Storey <sup>c,2</sup>

<sup>a</sup> Department of Information Systems and Operations Management, College of Business Administration, UniÕersity of Toledo, Toledo, OH 43606-3390, USA

<sup>b</sup> Information Management Research Centre, School of Accountancy and Business, Nanyang Technological UniÕersity, Nanyang AÕenue, Singapore 639798, Singapore

<sup>c</sup> Department of Computer Information Systems, College of Business Administration, Georgia State UniÕersity, Atlanta, GA 30302-4015, USA

Accepted 16 November 1998

## Abstract

Terms such as ‘data processing system’, ‘management information system’, ‘decision support system’, ‘expert system and ‘executive support system’ are widely used. However, there appears to be no generally accepted way to distinguish among these classes of information systems due to the vagueness that has existed in traditional classification schemes of information systems. The purpose of this research is to establish an analytical framework based on a theoretical foundation, called Semiotics the theory of signs to understand, classify and compare information systems of various generations. SuchŽ . a framework should simplify subsequent discussions and considerations in building new generations of information systems with complicated functions and capabilities. The proposed semiotics framework consists of 10 features that can be used to characterize the relationships between an information system and its users, and represent and organize the system’s contents. The framework is applied to analyze and compare the semiotics features of information systems. Its relevance to system development, particularly system planning and requirements determination, is also discussed. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Semiotics; Information system definitions and classifications; System development

## 1. Introduction

Terms such as ‘data processing system’, ‘management information system’, ‘decision support system’, ‘expert system’ and ‘executive support system’ are used universally, usually with the implication that there are significant differences among them. If these terms really do denote different classes of systems, then one would expect different design issues to arise and different methods and information technologies to be used when developing and implementing them. However, this common classification scheme of information systems according to system evolution is obsolete and confusing. A basic problem is that the terms data, knowledge and information are themselves rarely defined precisely 3,22 , al-<sup>w</sup> <sup>x</sup> though there have been many attempts by researchers in various disciplines to define and distinguish among them 6 . The distinction among the<sup>w</sup> <sup>x</sup> terms data, knowledge, and information is important for understanding what information systems do and why, in many cases, systems do not meet their requirements 1 .<sup>w</sup> <sup>x</sup>

The objective of this research, therefore, is to: establish a better analytical framework to understand, classify and compare Õarious classes of information systems. A semiotics framework comprised of 10 features is developed and presented. The purpose of the framework is to: 1 provide a means of Ž . distinguishing among various classes of systems in order to address system development and implementation issues that will become increasingly important as new generations of information systems with increasingly complicated functions and capabilities are developed. The framework identifies capabilities needed for information systems. These include: acquisition, validation, justification, representation, distribution, and explanation facilities; the ability to represent design information; and means to allow alternative implementation languages to be compared; 2 specify a requirements specificationsŽ . checklist for system development which includes important factors that are commonly omitted or not treated properly by existing development methodologies, such as social level and pragmatic issues in developing information systems.

This paper is divided into five sections. Section 2 surveys the traditional classifications and definitions of information systems. Section 3 introduces the semiotics framework, discusses each of its 10 features, and relates them to each other. Section 4 discusses the framework’s applications to system development. A summary and concluding remarks are found in Section 5.

## 2. Information systems

An abundance of terms have been used to classify computer-based information systems 4,10,11,<sup>w</sup> 15,17,21 . Definitions of common classes of infor-<sup>x</sup> mation systems are given below.

Transaction Processing Systems TPS( ) capture and process data resulting from business transactions such as orders, payments, invoices and sales. They are also called data processing systems. A TPS records data, but does little to convert data into information or knowledge. Early computer-based information systems were primarily TPS.

Management Information Systems MIS( ) supplement transaction processing systems with management reports required to plan, monitor, and control business operations. A MIS takes data recorded by a TPS and converts them into management information and presented in report form. They are also called management reporting systems.

Office Automation Systems OAS( ) combine various technologies to reduce the manual labor required in operating an effective office environment. A typical OAS handles and manages documents Žthrough word processing, desktop publishing, and digital filing , scheduling through electronic calen- . Ž dars , and communication through electronic mail, . Ž voice mail, or video conferencing ..

Decision Support Systems DSS ( ) provide their users with decision-oriented information for decision making. When applied to executive managers, these systems are sometimes called executive information systems. A DSS typically focuses on the future, and is designed to help decision makers with ill-formed or unstructured decisions.

Expert Systems ES( ) are an extension of decision support systems. An ES captures the knowledge, expertise and reasoning capabilities of a human expert and then simulates the ‘thinking’ of that expert.

Group Support Systems GSS ( ) permit people to process and interpret information as a group, even if they are not working face to face. Like a DSS, a GSS supports people working in situations that are not fully structured.

Knowledge Work Systems KWS( ) aid knowledge workers in the creation and integration of new knowledge within an organization.

Executive Information Systems EIS( ) provide critical information in easy-to-use displays to top and middle management. That are also called Executive Support Systems ESS . These systems cut across Ž . functional areas of the organization and provide access to external databases.

Strategic Information Systems SIS ( ) apply information technology to a firm’s products, service, or business processes to help it gain a strategic advantage over its competitors.

Based on the above definitions, these information system classes do overlap with each other. As a result, our view of the classes of information systems is potentially confusing and vague. For example, an information system used as a MIS by company A may be considered as a TPS by company B. Furthermore, an MIS developed in 1980s may be considered a TPS by now. In fact, if you ask a dozen IT professionals to define What is a management information system?, you would likely get a dozen different definitions. Implicitly, systems that support managerial functions are considered to be ‘better’ and more ‘useful’ than systems supporting routine business transactions. However, you may find out that a TPS is more powerful, useful and strategically important than some MISs and DSSs.

## 2.1. Classification schemes

Information systems vary widely in their functions, capabilities, performance and social consequences, as well as in their components, inputs, outputs and the users that they can support. Normally, they are classified in several ways such as: aŽ . organizational levels, b major functional areas, cŽ . Ž . support provided by the system, and d informationŽ . system architecture 20 . Traditionally, information<sup>w</sup> <sup>x</sup> systems have been classified by mirroring to some extent the evolution of information systems 4 . They<sup>w</sup> <sup>x</sup> are TPS, MIS, OAS, DSS, ES, ESS and GSS 20 .<sup>w</sup> <sup>x</sup> Such a classification scheme coincides with the adaptation of information systems for supporting different levels of business operations and management evolving from routine transaction support, knowledge support, and managerial decision support, to strategic management. However, with the redesign and reengineering of business processes, changing requirements for decision making, and the tremendous proliferation of technologies in system development, a classification scheme based on system evolution becomes obsolete, confusing and fuzzy:

Although this traditional classification of systems has been useful, it is beginning to outlive some of its usefulness. It is becoming more and more difficult to classify a specific information system. If we can no longer distinguish a majority of systems with a given scheme, then the benefits of having such a classification scheme are no longer realized. This is what is happening within the realm of information systems. Many systems now have multiple capabilities; no longer is a word-processing system just capable of creating and manipulating text within a document. For this reason, we believe that the scheme we have described is limited in its functionality, and it is time to develop complementary classification schemes 4 <sup>w</sup> <sup>x</sup> p. 164 .

Thus, a better analytical framework is needed to identify and categorize information systems based on certain criteria or common features. We will then be able to understand, classify and compare information systems of various generations based on a shared understanding of these features. In addition, such a framework will simplify our subsequent discussions and considerations of system development. It is also important that the proposed framework must be not only exhaustive in comparing and distinguishing among existing and future information systems, but also comprehensible for non-technical users end Ž users as well as technical users computer profes-. Ž sionals . Simplicity is the best way to make a com-. plex concept comprehensible for the non-technical users. For example, Cats-Baril and Thompson 4<sup>w</sup> <sup>x</sup> proposed a classification scheme, called the information systems I( ) <sup>r</sup> S cube. This scheme is based on the activities and tasks that are supported by information systems rather than the specific capabilities of the systems themselves. There are three dimensions of the I<sup>r</sup>S cube:

<sup>Ø</sup> the scope of the application being supported. The application scope refers to whom the information system supports. It can range from an individual agent at one end, to the inter-organizational unit at the other.

<sup>Ø</sup> the complexity of the task performed. Task complexity refers to the degree of decision structure inherent in the task being performed by the information system. It ranges from structured to unstructured.

<sup>Ø</sup> the information richness required. Information richness refers to how much surplus meaning the information contains, beyond the literal symbols used to express it. It ranges from spare to robust.

This paper strives to improve our understanding of the distinction among information systems based upon a theoretical foundation. We argue that it is better to recognize and identify the essential properties and features of an information system than to know the classification label of the system. To do so, we establish a semiotics framework comprised of 10 features. An investment information system example is used to illustrate our results.

## 3. Semiotics framework

Our previous research has focused on analyzing and synthesizing the literature on the definitions of data, knowledge, and information 6 . The results of<sup>w</sup> <sup>x</sup> previous work revealed five essential themes fea- Ž tures that seem to be well-represented by . Semiotics <sup>w</sup> <sup>x</sup> 13,14 . This paper adapts the original features and further extends our research to develop a 10-feature semiotics framework. These features are discussed and illustrated by an investment information system example. The framework’s relevance to system development is also discussed.

## 3.1. Semiotics: the theory of signs

The input and output of computer-based information systems data, knowledge, and information re-Ž . quire signs for their representation, storage and processing by computers, as well as their uses and interpretations by human and automated agents. The word ‘sign’ is used generally to include the numerical and alphabetical characters, words, sentences, messages, and all actions which, through custom or convention, have acquired some recognizable interpretation 18 . Semiotics, the theory of signs, is<sup>w</sup> <sup>x</sup> concerned with the properties of things in their capacity as signs 13 . These properties remain basi-<sup>w</sup> <sup>x</sup> cally unchanged. An analysis of the properties of signs is then essential to contributing to our understanding of information systems, and potentially useful in differentiating and categorizing them.

Semiotics is traditionally divided into three branches: syntactics, semantics and pragmatics, which deal, respectively with the structures, meanings and usage of signs 13,18 . Stamper 19 adds<sup>w</sup> <sup>x</sup> <sup>w x</sup> another branch, called social leÕel, which deals with the social consequences of signs. It is essential in understanding and classifying information systems.

## 3.1.1. Syntactics

Syntactics analyzes the relationships among signs without regard for the relationships between the signs and subjects that they are presumed to represent i.e.,Ž the signification of the signs nor any regard for the. users and what they intend to do with the signs 19 .<sup>w</sup> <sup>x</sup> In other words, it is only concerned with the formal representation and relationships of signs, and the operations and processes to which they may be subjected 18 . For example, in the investment infor- <sup>w</sup> <sup>x</sup> mation system, all the security instruments are represented by three-letter codes e.g., ‘MOT’ , which can Ž . by sorted alphabetically.

## 3.1.2. Semantics

The study of meaning, called semantics, deals with the relationship between signs and the objects to which they are applicable 13 . In other words,<sup>w</sup> <sup>x</sup> one must know to what the sign can properly be used to refer to in order to grasp its meaning. Semantics deals with relationships between signs and things in the ‘real world’; in particular, the problems of making relationships stable and reliable enough for us to communicate accurately on matters of facts and judgment 13 . Then, the meaning can be considered<sup>w</sup> <sup>x</sup> as a function from signs to reality 19 . The semantic<sup>w</sup> <sup>x</sup> properties of signs deal with meaning in the special sense of how signs relate to reality, how they represent, designate and signify things. For example, in an investment information system, the symbol ‘MOT’ Ž . i.e., a sign is used to represent the stock of Motorola. We can use any sign to represent a particular stock. Normally, there exists a conventional coding scheme for establishing the signs for the corresponding stocks that they represent.

## 3.1.3. Pragmatics

Pragmatics is concerned with relationships between signs and behavior of the responsible agents, e.g., users of an information system in a particular context <sup>w</sup> <sup>x</sup> 19 . The context is essential for understanding the signs in the pragmatic domain. Pragmatics should consider the origin, uses, and effects of signs within the behavior in which they occur 13 . For<sup>w</sup> <sup>x</sup> example, in the stock selection for setting up an investment portfolio, investors should know the characteristics of a stock such as earnings growth both historical and prospective, earnings quality, valuation in terms of prospective and historical price<sup>r</sup>earning ratios, dividend yield, and positive earnings estimate. Then, they will use these characteristics when making a selection. For an investment information system developed to support this task, the following pragmatic issues should be considered:

<sup>Ø</sup> the sources of these characteristics and how they should be obtained and justified the origin is- Ž sues ,.

<sup>Ø</sup> how these characteristics should be used in stock selection the use issues , andŽ .

<sup>Ø</sup> how significant each characteristic is in stock selection, how sensitive users are to these characteristics in making selection, and what suggestions the system should provide to its users theŽ effect issues ..

However, many computer-based information systems are designed without regard for pragmatic issues 2 .<sup>w</sup> <sup>x</sup>

## 3.1.4. Social leÕel

No sign can be fully understood without regard for its potential and actual social consequences. The social level consists of norms of many kinds such as ways of behaving, sets of values, and shared models of reality. These define the shape or form of social reality. At the social level, we are concerned with the actual, perlocutionary effects of the signs, whereas at the pragmatic branch, we are interested in the illocutionary or intended effects 19 . For example,<sup>w</sup> <sup>x</sup> each intended task i.e., illocutionary act performedŽ . by an information system should have social consequences achieved by the users performing actions and decisions i.e., perlocutionary acts . Then these Ž . perlocutionary acts should impact the target context. Consider the investment information system example. This system should request the basic requirements of an intended investment portfolio such as the return ratio and risk level, present information on global financial markets, provide suggestions and warnings in terms of stock selection and asset allocation based on the users’ intentions and requirements. All of these are illocutionary acts. Based on the output of the system, users will make decisions such as the exact investment portfolio. These decisions, in turn, will change the target context.

![](/api/attachments/4G2VK8WE/fulltext/images/5e6189ee41ac1f5ba4d674faa7493bc499768e24f68180b59378e90cebba8dd0.jpg)  
Fig. 1. The semiotics framework.

According to the representational triangle 19 ,<sup>w</sup> <sup>x</sup> Fig. 1 shows: 1 four branches of our semioticsŽ . framework, 2 elements under study and 3 rela-Ž . Ž . tionships of signs to observers<sup>r</sup>users of information systems and real world objects relationships. The elements under study by Semiotics are the signs, real world objects that signs can represent and behaviors that can be performed by the users, and users<sup>r</sup>observers that can perform actions and make decisions based on the signs. The rectangle boxes are used to represent semiotics branches. The oval boxes refer to the elements under study. The arrows refer to the relationships among these elements. Note that observers and users can be part of the social level.

## 3.2. Ten semiotics features of information systems

Based on an analysis of the semiotics branches, 10 features are identified as being the most common and appropriate in analyzing information systems’ properties. They are application domain, action complexity, social consequence, acquisition complexity, acquisition scope, input usability, output usability, justification, real world relationship, and representation. The first three features are established based on the social level. The next five are based on pragmatics, the ninth, on semantics, and, the tenth, on syntactics. In the following discussion, the term ‘statement’ is adopted as a generic term to refer to some set of signs that is the subject of analysis or discussion.

It follows immediately from the semiotics framework, particularly the social level, that an information system must be considered within the target context i.e., the application domain for which theŽ . system is built to make an impact as well as the intended users who will take actions based on the output of the information system. The values created by an information system depend upon the context within which it can perform actions and make changes.

The input entered into an information system can represent one observer’s opinion and interpretation of the subject matter of the information system. It may be essential to capture certain characteristics of the observer providing the input, and the user performing the action. Furthermore, semantics requires consideration of how the system signifies the real world objects that it represents. Note that actions and decisions performed by the system in the application domain may or may not directly involve objects that are part of the system’s subject matter.

Fig. 2 shows a generic, high-level view of the components of a ‘decision<sup>r</sup>information system Ž . Ž . DIS . The ‘Information System’ IS represents a broad range of possible systems, including computerized as well as non-computerized systems. From the user’s perspective, the ‘quality’ of the IS’s output clearly depends, not only on the IS itself, but also the input, consisting of the Sensor<sup>r</sup>Observer SO andŽ . Transformation<sup>r</sup>Data entry TD components. TheŽ . ‘Sensor<sup>r</sup>Observer’ in Fig. 2 performs the direct interface with the real world needed to gather observations on the system’s subject matter. These observations may simply be translated into a representation compatible with the storage format of the IS Ž . ‘data entry’ or may also be processed in some way Ž . ‘transformation’ before being stored. For example, scanner data collected by a retail store may be aggregated to produce total sales per day for each product rather than storing each individual sale in the IS. As discussed further below, distinguishing the components in Fig. 2 is particularly significant with respect to the acquisition and justification features because one might need to consider these for statements produced by the Sensor<sup>r</sup>Observer as well as the IS itself.

## 3.2.1. Application domain

The application domain is concerned with the scope, boundary and actual perlocutionary effects of an information system. According to these considerations, an information system is designed to solve problems, support activities and tasks, and<sup>r</sup>or make changes within the domain. There are many ways to specify the spectrum of an application domain. Consider information systems for business organizations. The application domain can range from a single task, a functional unit department , a division, a localŽ . organization, a multiple-country organization, a global organization, or even an industry. In general, the application domain of an information system will determine the system’s complexity and profiles of target users.

## 3.2.2. Action complexity

Action complexity refers to the nature of decisions that users can perform on the application domain by using the output of an information system. The decisions can be structured, semi-structured or unstructured ones. A structured decision is an action for which a process is readily available, well-accepted and can be automated. On the other hand, for unstructured actions, there are many issues and factors to consider in performing the actions decision mak-Ž ing . In general, an unstructured decision requires. human expertise, experience, intuition, judgement and even creativity. Normally, there is no way to automate the process of an unstructured decision. For example, the decision for a fund manager in determining the portfolio and asset allocation of an investment option with respect to the expected return ratio and risk level is an unstructured one. The structure of action complexity is not a discrete scale. It ranges continuously from completely structured such as routine work of document filing to completely unstructured such as the example mentioned above and long term strategic planning.

![](/api/attachments/4G2VK8WE/fulltext/images/8f1717d16c39abbc8788c4a3a26d6b6d52832c0dc3c0f453884e06d8e8c67f1c.jpg)  
Fig. 2. The major components of a decision<sup>r</sup>information system.

## 3.2.3. Social consequence

Many different social consequences can result from the perlocutionary acts performed by the system users on the application domain. We categorize these consequences into the following categories:

<sup>Ø</sup> Strategic: impacts on executing, sustaining and achieving the current business goals and strategies,

<sup>Ø</sup> Tactical: impacts on facilitating the planing, organizing and controlling of business processes,

<sup>Ø</sup> Operational: impacts on running routine business operations.

For an investment firm, there are many potential social consequences from using the investment information system, such as:

<sup>Ø</sup> the awareness of its client that this firm is different from the conventional investment styles which mainly depend on human expertise and experience,

<sup>Ø</sup> the change of attitudes of its employees toward emerging information technologies and systems,

<sup>Ø</sup> the improvements in efficiency, timeliness and quality of investment decisions for its clients, and

<sup>Ø</sup> the improvements of the earning ratio and profit.

An information system can be designed to produce social consequences in more than one category.

Furthermore, the actual consequences produced by an information system depend on the application and its environment. For example, the investment information system used by different firms may result in different impacts on the firms.

## 3.2.4. Acquisition complexity

Acquisition concerns the nature of the processing required to obtain a statement i.e., input for anŽ information system . It is, therefore, potentially ap-. plicable to each of the Sensor<sup>r</sup>Observer, Transformation<sup>r</sup>Data entry and IS components of Fig. 2. There are two features to consider for acquisition: complexity and scope. In the case of a human Sensor<sup>r</sup>Observer, acquisition complexity refers to the degree of skill, knowledge and training needed for the issuer of a statement to be considered credible in making it. Acquisition complexity is not an either<sup>r</sup>or feature. It could range across a continuum from simple to complex.

A statement is acquisition-simple if a person having common sense knowledge and an average education would be credible in making it. A statement is acquisition-complex if a person must have specific training, knowledge and experience to make it. In other words, it is valuable to identify situations where human interpretation is inherent in the input entered into a system. Consider, for example, an investment fund manager or financial consultantŽ . who can examine a stock, bond, or currency and make many correct statements about it; for example, a stock has an AAA earning quality, and is of a particular prospective price<sup>r</sup>earning ratio and growth potential. The manager plays the role of Observer inŽ Fig. 2, and might also play the roles of Transformation and IS if, say, the user is a client consulting the manager for an investment decision. These observa-. tions may be effortless for the manager, but only because of his or her training, investment knowledge and experience. Such statements are, therefore, acquisition-complex.

In contrast, consider a data entry clerk for an investment information system who is required to make observations on the change of stocks’ prices such as how many have increased more than 5% within a day. Since anyone having an ordinary education could make credible observations of this type, they are acquisition-simple. Note that the results of both kinds of observations are unlikely to require processing other than data entry before being stored in the information system, in which case they would both be acquisition-simple for the Transformation<sup>r</sup>Data entry component. In the case of a non-Ž human Sensor. <sup>r</sup>Observer, operating specifications such as its accuracy, error rate, etc., would be relevant to describing acquisition. Non-human sensorproduced data is mainly considered acquisition-simple. For example, the above example for identifying stocks having more than 5% price increment can be obtained automatically as non-human sensor-produced data by the investment information system.

With respect to both the Transformation<sup>r</sup>Data entry and IS components, the issue is the complexity of the processing required to produce that component’s output. For example, if data entry is done without any other transformation, a statement so produced is acquisition-simple; otherwise it is acquisition-complex. For the IS component, if elementary formatting and retrieval e.g., equivalent to relationalŽ algebra operations are all that are required to pro-. duce the statement in question, it is acquisition-simple. If consolidation, integration, or complicated transformation process is needed to form the statement, then it is acquisition-complex.

## 3.2.5. Acquisition scope

Acquisition scope refers to the range of sources for the formation of a statement. A statement is acquisition-narrow, if a single source is needed. If a statement must be formed based on the input from multiple sources, then it is acquisition-broad. The spectrum of acquisition scope can range, starting from one end, at an individual person or machine Ž . i.e., a single source , to workgroup, department, enterprise i.e., multiple homogeneous sources , andŽ . further extend at the other end, to inter-organizational and global i.e., multiple heterogeneousŽ . sources.

In general, an acquisition-narrow statement tends to be acquisition-simple. Likewise, an acquisitionbroad statement is normally acquisition-complex. However, an acquisition-narrow statement may be acquisition-complex due to the requirement of a complicated transformation of statements from a single source. For example, to determine the degree of attractiveness of a stock, the factors to consider might have been stored in a single resource, a security database system, but, the output statement must be obtained through a complicated assessment process of the investment information system. In addition, this assessment process may need human involvement and judgement. On the other hand, an acquisition-board statement may be acquisition-simple due to the homogeneous sources of the statement. For example, to present the global stock price movement, data should be obtained from global financial markets, e.g., New York, London, Japan, Hong Ž Kong, etc. . However, data from these sources is. most likely homogeneous.

## 3.2.6. Justification

The focus of justification is why a statement should be believed, in contrast to acquisition’s focus on how a statement came to be known. In some cases, knowing the latter can also suffice as justification. Consider the investment manager example. An explanation for the acquisition of the ‘earning quality’ characteristic for a particular investment instrument such as a stock, currency, or bond, might be Determined by Jane Jones on 24 October 1997, while one possible justification might be Jane Jones is a Chartered Financial Analyst CFA with 15( ) years’ experience, and has shown good inÕestment performance in the past. Alternatively, Jane Jones’s description of the particular characteristic of the investment instrument that led her to make the conclusion would also be considered a justification.

Basically, justification considers how much effect is needed by referring to the subject matter, how certain validity and confidence a statement is, andŽ . therefore how costly it would be to validate it. A statement is justification-simple if its justification rests on simple grounds such as direct observation by ordinary sensors eyes, thermometers, etc. , or theŽ . acquisition manner providing adequate justification. As with acquisition, the user may be interested in justifications for the output of any of the IS components.

Propositional statements such as ‘The stock price for Motorola is 67.5 on February 19, 1998’ and ‘The Dow Jones Industrial Average increases 125 points in the week, February 16–20, 1998’ are simple in these aspects. A few examples that are complex on this feature are:

<sup>Ø</sup> there exists Ž . ' , without referring to a corresponding specific individual; e.g., there exists at least one global financial market that has 15% annual growth rate within past 2 years.

<sup>Ø</sup> universally quantified statements for allŽ Ž .. ; ; e.g., all major currencies—French francs, Swiss francs, British pounds, German marks, and Japanese yen will rise against the US dollar over the next year or two.

<sup>Ø</sup> disjunctions of two propositions; e.g., either Singapore or Taiwan will have the best economic performance in Asia for the second half of 1998.

<sup>Ø</sup> probabilistic statements; e.g., the probability that US dollar will be depreciated against Japanese yen in the next 3 months is 0.15.

## 3.2.7. Input usability

According to our generic DIS model, the usability of a statement can be considered from both input and output. The usability of an input statement, or set of statements, is concerned with whether a statement is directly useful with regard to satisfying a particular inquiry to provide the output. If processing of the set of statements is needed beyond what is required for retrieval and formatting purposes, then those statements are said to be usability-low with respect to that query. If, however, an input statement can be employed directly, then it is usability-high. For example, in a query for the monthly average price of a stock, the daily stock prices are usability-low since processing of the statements in the set is required. If the query is for daily prices rather than an average one, then the daily prices are usability-high because Ž no additional processing is required . Based on the. above discussion, it is obvious that the usability of an input statement depends on the required query. Therefore, it is essential to define the appropriate application domain and the illocutionary effects of an information system in order to assess the usability of input statements.

## 3.2.8. Output usability

The usability of an output statement is assessed based on the illocutionary effects of the statement on the system users. An output statement is usabilityhigh, if the statement generates more informative and pragmatic impacts on a user for the intended usage. Otherwise, an output statement is considered to be usability-low. For a fund manager in adjusting asset allocation of an Asian mutual fund comprised of only Asian currencies and stocks, some usabilityhigh examples are: the currency exchange rate between US dollar and Japanese Yen is increasing 25% in last week, and the stock index of Singapore decreased 30% in the last quarter. On the other hand, the statement, the price of Motorola’s stock has decreased 7% in the last month is relatively usability-low, since it is not directly related to the subject matter, i.e., the Asian mutual fund.

## 3.2.9. Real world relationship

Real world relationship deals with semantic issues. It contains a variety of mappings meanings Ž . from statements to the real world objects. Stamper <sup>w</sup> <sup>x</sup> 19 identifies three semantic principles in terms of how the real world relationships are established and used.

3.2.9.1. ObjectiÕist meaning. If users of statements share a well established consensus or norms about the real world objects, ways of behaving, experiences and knowledge, and even values and culture, then the meanings are stable mappings from statements into the real world objects. All the users know these mappings and which ones are the same for everyone. For example, ‘male’ and ‘female’ are used to indicate two different genders. Everyone understands these stable mappings.

3.2.9.2. ConstructiÕist meaning. When the users do not have a well established consensus about these mappings from the statements to real world objects, then the mappings must be established through discussion, negotiation and reconciliation among users. In this case, the mappings are changeable. For example, the two-letter codes representing Airlines in the airline reservation and booking systems are wellaccepted and adapted by the Travel industry. However, they can be changed through negotiation and reconciliation.

3.2.9.3. Mentalistic meaning. In this case, a person establishes the mappings from the statements to real world objects and expects other users to accept these mappings in using them. For example, in the application of the Entity–Relationship conceptual model 5 ,<sup>w</sup> <sup>x</sup> users are expected to represent a real world object by a rectangle symbol and to use a diamond to represent the real work associations among objects.

Each of these semantic principles is applicable for a different range of tasks that can be performed by information systems. For example, the objectivist principle can be applied to routine and well-accepted business processes. In addition, some information systems may employ more than one principle to provide semantics. Consider the investment information system example. It is better to employ all three principles to support different tasks involved in the system. However, a common problem of legacy systems is that the underlying principle s and map- Ž . pings have not been stated explicitly and system users need to establish the relationships themselves.

## 3.2.10. Representation

Representation is expressed relative to a particular language for representing and manipulating signs. Examples of representation languages are natural languages, conceptual modelling languages, data and knowledge representation languages, and implementation programming languages. A representation Ž . language is defined syntactically by a set of primitive symbols and a set of grammatical rules which define new configurations in terms of old ones 8 .<sup>w</sup> <sup>x</sup> For example, the language of first order logic is defined as a collection of symbols and rules for building well-formed formulas. A first-order language represents the real world in terms of constants, variables, predicates, logical connectives, and quantifies 7 . An information system normally needs at<sup>w</sup> <sup>x</sup> least two languages to represent both its contents and processes, respectively. The representation of an information system’s contents can be assessed based on the complexity and structural richness of the required representation languages. However, objectoriented programming attempts to combine the presentation of contents and processes by a unified language. Consider again the investment example introduced earlier. Note that, on the representation feature, there is no conceptual difference in the representation language between ‘expected return ratio’ and ‘risk level’ being characteristics of an investment policy and ‘price’ of a stock for the structure complexity of the resulting statements and their storage in an information system. This illustrates that features other than syntax are important in distinguishing among different kinds of output statements.

Table 1 summarizes the semiotics framework’s 10 features.

## 4. Applications of the framework

This section categorizes the potential applications of the semiotics framework into two perspectives. They are: 1 value, cost and benefit assessment ofŽ . an information system, and 2 the information sys-Ž . tem development checklist.

Table 1 Semiotics framework

<table><tr><td>Semiotics branches</td><td>Ten features</td><td>Interpretations</td></tr><tr><td rowspan="3">Social level</td><td>Application domain</td><td>The scope and boundary within which an information system is designed to make perlocutionary effects.</td></tr><tr><td>Action complexity</td><td>The structure of an action that users can perform by using the system&#x27;s output.</td></tr><tr><td>Social consequence</td><td>The types of consequences that can result from the perlocutionary acts performed by the system users.</td></tr><tr><td rowspan="3">Pragmatics (Origin)</td><td>Acquisition complexity</td><td>The nature of the process by which a statement is acquired.</td></tr><tr><td>Acquisition scope</td><td>The range of the sources by which a statement is formed.</td></tr><tr><td>Justification</td><td>How the statement is justified or made evident.</td></tr><tr><td>Pragmatics (Use)</td><td>Input usability</td><td>The degree to which a statement is directly usable with regard to a query.</td></tr><tr><td>Pragmatics (Effect)</td><td>Output usability</td><td>The illocutionary effects of an output statement on the system users.</td></tr><tr><td>Semantics</td><td>Real world relationship</td><td>The nature of a statement&#x27;s relationship to the object(s) to which it refers.</td></tr><tr><td>Syntactics</td><td>Representation</td><td>The complexity and structural richness of a language that can be used to represent the system&#x27;s contents and processes.</td></tr></table>

## 4.1. Value, cost and benefit assessment

The framework has practical relevance and usefulness since it provides an expanded view of an information system. This, is turn, enables us to relate the framework’s 10 features to the system’s net value. System developers traditionally have assessed information systems focusing mainly on the technical aspects such as hardware, application programs, and data management of the ‘Information System Ž . IS component in Fig. 2, with less attention paid to the social, pragmatic and semantic aspects of the entire DIS. To solve this problem, we suggest adapting the framework for the cost and benefits analysis of information systems, and discuss how it might be done.

It is difficult to ascribe a net value to the IS by itself. The perlocutionary effects made by system users and especially social consequences which are influenced by the IS, are the source of gross value,Ž . and all of the components, including the user, are, in general, sources of costs. <sup>4</sup> The complexity of actions that can be performed by the systems’ users depends upon the acquisition scope and justification. If the acquisition scope is adequate to cover the required information sources with acceptable justifications, then the system can facilitate users in making semi- or unstructured decisions. In turn, these decisions should produce significant consequences on the system’s application domain.

Viewed from this perspective, input usability is concerned with the net value of a set of statements for system users with respect to a particular query .Ž . For example, consider a query for the monthly average price of a stock or mutual fund. The gross value will be the same regardless of whether the information system calculates and returns the average usa- Ž bility-simple , or returns only the daily stock prices . Ž . usability-complex to the user, who is then responsible for calculating the monthly average price. However, the net value as seen by the user will likely be much higher when the average is returned as the answer. Thus, in general, usability-simple statements will require less processing on the part of the user, causing him or her to incur lower costs to extract the desired statement. From the perspective of the DIS as a whole, however, there is a question as to whether it is the user or some other system component that should do the processing, since it is the total cost of the whole system, not just the cost generated by the user, that matters. For our investment information system example, the IS is almost certainly the least-cost processor. For other kinds of information, the user may be the least-cost processor. Since processing can be done by several different components in Fig. 2, costs attributable to acquisition can arise from any of them. As noted above, the allocation of particular kinds of processing among system components is a crucial factor in maximizing the net value of a DIS.

Justification is related to both output usability and acquisition scope. The point of justification is to capture properties of the entire communication channel in Fig. 2 all components to the right of the userŽ . that the user finds relevant to judging the ‘quality’ of the output of the information system. Thus, output usability is concerned with the net value of the information provided to the user, giÕen that it is the product of a particular channel. The same statement provided by two different channels having differentŽ justifications can yield very different net values for. the user due to the different levels of confidence he or she will have in them.

Real world relationship in effect captures the cost of reversing the arrows in Fig. 2, asking how costly it would be to determine or examine the relationship between a particular output statement with the IS’s subject matter. It should be noted that this can interact with justification, since the more difficult it is to verify statements produced by a channel, the less confidence one is likely to have in that channel.

Representation interacts with both acquisition complexity, and input and output usability. The amount of processing and storage required both to store the results of observations and to provide query answers from what is stored are obviously impacted by the chosen representation. Similarly, the degree to which stored statements are usable depends significantly on the nature of their representation.

## 4.2. Requirements analysis in system deÕelopment

The 10 features of the semiotics framework are particularly useful for identifying and understanding activities that need to be carried out during the system planning and requirements analysis phases of system development.

## 4.2.1. Application domain

During the requirements analysis phase, the scope and boundaries of the information system’s application domain should be defined explicitly. It should decide the owner, users, and the particular context within which the system is applicable. Especially, the owner’s interests, the objectives, participation commitment and information requirements of intended users, must be specified. In addition, we should attempt to determine and document the behavior norms of these people involved in the proposed systems. Then, the system designers and builders can develop the proposed system correctly by referring to these specifications.

To do so is better for the subsequent phases of system development in the refinement of the scope. Furthermore, future system users can make inquiries of these specifications to understand upon what the system is originally designed. But, for legacy information systems, these high level specifications have neither been captured completely nor documented in the system for reference. A context diagram is used generally to define a system’s boundaries and scope. It depicts the inputs and outputs of a proposed system and their relationships with other business units and information systems. However, the context diagram cannot capture and represent all of the required specifications, such as the behavior norms, for further development and maintenance tasks.

## 4.2.2. Action complexity

The complexity of actions performed by the proposed system determine what types of design, tools and technologies should be used to build the system. In general, the more structured the decision, the easier the task of requirements analysis. In other words, for the systems to support semi- or unstructured decision making, the requirements analysis is harder and oftentimes, we need to adopt several alternatives, such as prototyping to determine the right requirements. In addition, systems to support these semi- or unstructured decisions should incorporate multiple decision models in order to meet the information requirements. Action complexity has impacts on the interface design as well. For example, to support an unstructured decision, the system must actively interact with the user and provide the flexibility for the user to exploit various combinations of inputs and decision models.

## 4.2.3. Social consequence

In the system planning phase, we need to identify the expected social consequences of the proposed system, and understand how these consequences can align with business goals and what value can be contributed by the system. For example, a bank develops a web-banking system to provide global banking services to its customers. This system is designed to differentiate the bank’s services from its competitors’. This system may give the bank competitive advantages in a particular segment e.g., Ž electronic commerce or niches of the banking indus-. try.

Since the expected social consequences are the source of the gross value of the system, to determine these expected consequences is an appropriate way to justify the budget of the proposed system. However, the actual social consequences can only be known by conducting an empirical study when the system is in use. In addition, the types of social consequences expected to be achieved by the proposed system will also affect the ways the system should be acquired. There are various ways of system acquisition: traditional in-house development, end user computing, using software packages, and outsourcing. For example, in-house development is most appropriate for the above web-banking system example.

## 4.2.4. Acquisition complexity and scope

Acquisition-related features subsume what is traditionally called functional specification, where the focus is to determine the logical functions that the Ž . system must perform in order to produce the desired black box behavior. Acquisition complexity and scope, however, emphasize a broader viewpoint, and a correspondingly broader set of issues, than functional specification.

This is evident from Fig. 2 which emphasizes the qualities of the entire path from observation of the subject matter to the outputs produced by the system under development. The ‘impedance matching’ problem between the output users desire and what can be observed in the domain of subject matter is, therefore, highlighted. Thus, the developer is forced to ask: ‘What kind of operations are to be performed? and, ‘Which components of the DIS are to perform them?’ More specifically, the following issues need to be addressed: 1 where the initial input state- Ž . ments will come from; 2 what types of sensors, Ž . procedures, and training are required to capture it; Ž . 3 where updates will come from and how often; and 4 what procedures e.g., programs, query facili-Ž . Ž ties are required to satisfy the users’ output needs..

The allocation of processing among DIS elements is illustrated by the following. If users are interested in attributes for example, statistics of entire groups Ž . of things as opposed to the underlying, individual statements, then there are two issues. First, should the raw, underlying statements be stored? If so, then processing requirements must be determined in order to satisfy user queries. Note that the stored state-Ž ments are then input usability-low. On the other. hand, instead of storing the underlying statements, it may be possible to store the summaries directly so that queries do not require significant intermediate processing, thereby implying some pre-processing of input data. Therefore, pre-processing requirements must be determined along with appropriate storage structures for the summarized statements. For example, the data warehouse for the investment information system stores summarized data e.g., price mov-Ž ing averages as well as historical and current de- . tailed data e.g., daily prices of stocks . In this case,Ž . the stored processed statements are input usability-Ž . high with respect to user queries.

The other aspect of acquisition issues that is atypical of functional specification is the need to determine what information system users want to know about the acquisition process. This may include information about the input statements to the system, the stored statements, the outputs from the system, or any combination of these. For input statements, such facts as the time of observation and the identity of the observer or sensor, are frequently important. Similarly, for stored statements, the method of data entry, the time of the update, and the identity of data entry personnel may be significant. For a system’s outputs, the inputs and time produced are frequently important, as are the details of the algorithms applied. Typically, as acquisition complexity increases, the more likely it is for user-accessible information about acquisition to be important.

It appears that system developers typically assume that acquisition information is part of the common knowledge of organizational members, and thus outside the project’s scope. This may be a relatively safe assumption in a small organization with low employee turnover, but, in general, relying on common knowledge is likely to decrease user confidence in the system. Furthermore, the availability of acquisition information to users should improve the quality of a system’s information by making statement observers, data entry personnel, and system developers more conscientious since they can be identified and held accountable.

## 4.2.5. Justification

Some ‘knowledge-based’ systems provide a type of justification for their outputs by ‘explaining’ their reasoning processes, which, in essence, amounts to supplying a trace of program execution i.e., proce-Ž dural justifications . In fact, in our framework, such. a trace is primarily acquisition information, and as such may or may not be seen by system users as being the kind of justification they want i.e., declar-Ž ative justifications . More broadly, the idea of pro-. viding declarative justifications does not seem to be reflected in typical system development methodologies. Given past and present technological limita-Ž . tions, this omission is perhaps understandable, but the concept is clearly important and deserves much more attention, from both the design and implementation perspectives.

## 4.2.6. Input usability

Input usability subsumes those activities involved in determining a system’s ‘black box’ behavior; that is, the behavior desired by the system’s eventual users. Thus, a major objective of requirements analysis is to identify the outputs desired by the users. Clearly, the content of these outputs ‘data require- Ž ments’ is a central issue, but the cost. <sup>r</sup>benefit orientation of input usability also emphasizes that a number of other attributes of the outputs may affect their net value, and should be considered. Examples of such properties include user interface and report designs, security and access authorization, correct update frequencies, and the precision and accuracy of observation and recording.

## 4.2.7. Output usability

Output usability should be studied to understand the system’s illocutionary effects of the designed outputs on the intended users. The designers should obtain an indication of the benefits the system can provide to the users in actual use. To do so, the designer must also study the behavior norms of the system users. The output usability is mainly determined by the contents of the output statements and the user’s intended usage and purpose. However, the colored graphic user interface, multimedia output format are new ways to improve the illocutionary effects of the information systems. Prototyping can be applied to determine the illocutionary effects in a controlled manner.

## 4.2.8. Real world relationship

This feature has received somewhat more attention than the preceding ones as is evinced by research on semantic data models 9,16 and concep-<sup>w</sup> <sup>x</sup> tual modeling 12 . The developer’s basic responsi-<sup>w</sup> <sup>x</sup> bility in this regard is to ensure that: a the correctŽ . representation of the subject matter, and b theŽ . system users can grasp the consistent meanings of the statements stored in a system or generated by it. Typically, the greater the real world relationship complexity of a system’s stored statements, the greater will be the effort required by the developer to ensure that these two needs are met.

In general, the greater the complexity of the real world relationship, the harder it is for the users to understand various aspects of the system itself. For example, users must understand the design of a relational database well enough to perform the proper joins on relations. Also, in order to formulate queries and understand the system’s outputs, the meanings of attribute and relation names and the meaning of terms used in the system’s outputs must be known by the users. Thus, this type of information should be made available to users by the system. On a technological sense, this need is partially met by data dictionaries. However, as with justification, development methodologies appear to treat such information in a rather unsystematic way. A great deal more could be done to supply useful design-related information to system users.

The following example illustrates the value of knowing the intended meanings of a relational database’s relations and attributes. Without such information, users may be tempted to perform many kinds of syntactically valid, but meaningless, joins.

<sup>Ø</sup> Student–City—refers to the cities in which a student has resided,

<sup>Ø</sup> Student–School—refers to the schools that a student has attended. <sup>5</sup>

<table><tr><td></td><td colspan="2">Student–City</td><td>Student–School</td></tr><tr><td>Id</td><td>City</td><td>Id</td><td>School</td></tr><tr><td>1234</td><td>San-Jose</td><td>1234</td><td>Stanford</td></tr><tr><td>1234</td><td>LA</td><td>1234</td><td>UCLA</td></tr><tr><td>1678</td><td>Seattle</td><td>1234</td><td>USC</td></tr><tr><td>1678</td><td>Minneapolis</td><td>1678</td><td>U Minnesota</td></tr><tr><td>1678</td><td>Carbondale</td><td>1678</td><td>U Washington</td></tr><tr><td></td><td></td><td>1678</td><td>SIU</td></tr></table>

Here, a join on ‘Id’ produces many spurious tuples if a co-occurrence of a city and school in a tuple is taken to mean that a student lived in that city while attending that school.

A somewhat different kind of problem occurs when the rules that govern the behavior of the world are not fully reflected in the system’s design. Such situations arise most commonly when the corresponding rules require complex integrity constraints, implying a large penalty in a system’s performance. This can allow an information system to assume states that do not correspond to any legal states in the real world. This is actually a result of a trade-off between representation capabilities on one hand and real world relationship on another. By making the features explicit, it is hoped that it will be easier for a developer to be aware of and evaluate such tradeoffs.

Table 2  
Implications of features for development and use

<table><tr><td>Features</td><td>Development</td><td>Use</td></tr><tr><td>Application domain</td><td>Scope and boundary of the domain.Owners and users of the system.</td><td>Make inquiries and understand this type of specification.</td></tr><tr><td>Action complexity</td><td>Determine what types of design, tools and technologies should be used to support the intended actions.</td><td>Flexibility to exploit various combinations of inputs and decision models</td></tr><tr><td>Social consequence</td><td>Identify the potential consequences.Align with business goals.Justify the contribution in terms of business value.</td><td>Conduct the empirical study.</td></tr><tr><td>Acquisition scope</td><td>Source of initial data.Source of updates.Training and skill requirements for acquisition.</td><td>Nature of acquisition information desired by users; e.g., timeliness (when observed), accuracy (explicit information or implicit via source identity).</td></tr><tr><td>Acquisition complexity</td><td>Processing requirements to transform stored statements into answers.</td><td>Explanation facility: how the system generated the answer.</td></tr><tr><td>Justification</td><td>Determine the appropriate justification given the application domain and the nature of the users.Determine how to provide the justification.</td><td>Is the statement compatible with or contradicted by some other body of knowledge?</td></tr><tr><td>Input usability</td><td>Understand the nature of user queries and user capabilities vs. stored statements: how the former can be satisfied by the latter.</td><td>Continuously study the users&#x27; ongoing requirements.</td></tr><tr><td>Output usability</td><td>Study illocutionary effects of outputs on the users.</td><td>Feedback from the users is important to maintain the system and meet users&#x27; needs.</td></tr><tr><td>Real world relationship</td><td>Make design and representation decisions that will yield a complete and consistent domain model.</td><td>Ability to understand the design conventions (e.g., meanings of attributes) used in the system in order to receive &#x27;true&#x27; answers to queries.</td></tr><tr><td>Representation</td><td>Select internal representation appropriate to the nature and complexity of the statements to be stored and processed and to performance needs.</td><td>Provide meaningful names of internal system objects.</td></tr></table>

## 4.2.9. Representation

There are two aspects to representation decisions. The first is the system’s internal representation mechanism. The nature or degree of the real world relationship complexity is a major factor in choosing a representation scheme. This suggests the need to have a common language in which the expressive power of alternative implementation schemes e.g.,Ž relational model, object-oriented models, etc. can be. compared. Then, by expressing the statements that need to be stored for an application in this language, a developer could determine which implementation scheme is most appropriate for a given application.

The second aspect relates to those design decisions that affect how the user interacts with the system. For a relational database, examples include the names chosen for relations and attributes. These choices will have a critical impact on the system’s ease of use and understanding of the real world relationship to the system’s output, and in turn impact usability. Table 2 summarizes the implications of the features for the design and use of an information system.

## 5. Summary and conclusion

A semiotics framework, consisting of 10 features, has been presented. Three main benefits of using this framework can be identified. First, the framework provides a coherent way to distinguish among types of systems, thereby highlighting a number of system development and system use issues that should be addressed in an orderly manner during the development process. These issues will become progressively more important as more ambitious and complicated information systems are built. Second, the framework identifies research directions aimed at providing the kinds of semiotics features that appear to be desirable in future generations of information systems. Highly significant among these are: 1Ž . justification and acquisition representation and explanation facilities, 2 the ability to represent design Ž . information and make it available to system users, and 3 the creation of a ‘lingua franca’ for systemŽ . development that would allow the expressive power of alternative implementation languages to be compared and the most appropriate one selected for a given application. Finally, the framework provides a requirements checklist for system development which includes important factors that are commonly omitted or treated haphazardly by existing development methodologies.

## Acknowledgements

This research was supported by the William E. Simon Graduate School of Business Administration, University of Rochester. Authors wish to thank the Editor-in-chief and anonymous reviewer for very constructive comments in preparing this manuscript.

## References

<sup>w</sup> <sup>x</sup> 1 S. Alter, Information Systems: A Management Perspective, 2nd edn., The Benjamin<sup>r</sup>Cummings Publishing, Reading, MA, 1996.

<sup>w</sup> <sup>x</sup> 2 P.B. Andersen, A Theory of Computer Semiotics: Semiotic Approaches to Construction and Assessment of Computer Systems, 2nd edn., New York, Cambridge Univ. Press, 1997.

<sup>w</sup> <sup>x</sup> 3 J.A. Bubenko, I.P. Orci, Knowledge base management systems: a database view, in: J.W. Schmidt, C. Thanos Eds. ,Ž . Foundations of Knowledge Base Management, Springer-Verlag, New York, 1989, pp. 373–378.

<sup>w</sup> <sup>x</sup> 4 W. Cats-Baril, R. Thompson, Information Technology and Management, Irwin, 1997.

<sup>w</sup> <sup>x</sup> 5 P.P. Chen, The entity relationship model—toward a unified view of data, ACM Transactions on Database Systems 1 1Ž . Ž . 1976 9–36.

<sup>w</sup> <sup>x</sup> 6 R.H.L. Chiang, T.M. Barron, V.C. Storey, Data, knowledge, and information in database and knowledge-based systems, Journal of Database Administration 3 3 1992 12–20.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 M.R. Genesereth, N.J. Nilsson, Logical Foundations of Artificial Intelligence, Morgan Kaufmann Publishers, 1987.

<sup>w</sup> <sup>x</sup> 8 P.J. Hayes, Some problems and non-problems in representation theory, in: R.J. Brachman, H.J. Levesque Eds. , Read- Ž . ing in Knowledge Representation, Morgan Kaufmann Publishers, Los Altos, CA, 1985, pp. 3–22.

<sup>w</sup> <sup>x</sup> 9 R. Hull, R. King, Semantic database modeling: survey applications, and research issues, ACM Computing Surveys 19 3Ž . Ž . 1987 201–260.

<sup>w</sup> <sup>x</sup> 10 K.C. Laudon, J.P. Laudon, Essentials of Management Information Systems: Organization and Technology, 2nd edn., Prentice-Hall, 1997.

<sup>w</sup> <sup>x</sup> 11 L. Long, N. Long, Introduction to Computers and Information Systems, 5th edn., Prentice-Hall, 1997.

<sup>w</sup> <sup>x</sup> 12 P. Loucopoulos, R. Zicari, Conceptual Modeling, Databases, and CASE, Wiley, New York, 1992.

<sup>w</sup> <sup>x</sup> 13 C.W. Morris, Signs, Language and Behavior, Prentice-Hall, New York, 1946.

<sup>w</sup> <sup>x</sup> 14 D. Nauta, The Meaning of Information, Mouton, 1972.

<sup>w</sup> <sup>x</sup> 15 J.A. O’Brien, Introduction to Information Systems, 8th edn., Irwin, 1997.

<sup>w</sup> <sup>x</sup> 16 J. Peckham, F. Maryanski, Semantic data models, ACM Computing Surveys 20 3 1988 153–189.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 J.A. Senn, Information Technology in Business: Principle, Practices, and Opportunities, Prentice-Hall, 1995.

<sup>w</sup> <sup>x</sup> 18 R.K. Stamper, Information in Business and Administrative Systems, C. Tinling, London, 1973.

<sup>w</sup> <sup>x</sup> 19 R.K. Stamper, Signs, Information, Norms and Systems, in: B. Holmqvist, P.B. Andersen, H. Klein, R. Posner Eds. , Ž . Signs at Work, De Gruyter, Berlin, 1996, pp. 349–397.

<sup>w</sup> <sup>x</sup> 20 E. Turban, E. McLean, J. Whtherbe, Information Technology for Management: Improving Quality and Productivity, Wiley, 1996.

<sup>w</sup> <sup>x</sup> 21 J.L. Whitten, L.D. Bentley, Systems Analysis and Design Methods, 4th edn., Irwin<sup>r</sup>McGraw-Hill, 1998.

<sup>w</sup> <sup>x</sup> 22 G. Wiederhold, Knowledge versus data, in: M.L. Brodie, J. Mylopoulos Eds. , On Knowledge Base Management Sys-Ž . tems, Springer-Verlag, New York, 1986, pp. 77–82.

Terence M. Barron is Associate Professor of Information Systems and Operations Management in the College of Business Administration, University of Toledo. He received both his MBA in Finance and his PhD in Information Systems from the University of Washington Seattle . Before joining the University of ToledoŽ . faculty, he was Assistant Professor of Information Systems at the University of Rochester, W.E. Simon School of Business. His research interests include conceptual modeling and logical database design, economics of information and information system management, and the impacts of information technology on organizations and markets. His research has appeared in Information Systems Research, Management Science, IEEE Transactions on Knowledge and Data Engineering, Decision Support Systems, Very Large Data Base Journal, the Journal of Organizational Computing, and Data and Knowledge Engineering.

Roger H.L. Chiang, Senior Lecturer of the Division of Strategy and Information and Technology, Deputy Director of the Information Management Research Centre, and Deputy Director of MBA in Management of Information Technology, Nanyang Business School, Nanyang Technological University, Singapore. He has a BS degree in Management Science from National Chiao Tung University, Taiwan, MS degrees in Computer Science from Michigan State University and in Business Administration from University of Rochester, and PhD degree in Computers and Information Systems from University of Rochester. His research interests are in data and knowledge management, and database integration. His research has been published in ACM Transactions on Database Systems, Data and Knowledge Engineering, Decision Support Systems, and Journal of Database Administration.

Veda C. Storey, Associate Professor of Computer Information Systems, College of Business Administration, Georgia State University. Dr. Storey received her doctorate in Management Information Systems from the University of British Columbia, Canada in 1986. She earned a Master of Business Administration degree from Queen’s University, Canada in 1980, and a Bachelor of Science degree with distinction from Mt. Allison University,Ž . Canada in 1978. Her research interests are in database management systems, knowledge management, and intelligent systems. Her research has been published in ACM Transactions on Database Systems, IEEE Transactions on Knowledge and Data Engineering, Information Systems Research, Management Information Systems Quarterly, Data and Knowledge Engineering, Decision Support Systems, and Very Large Data Base Journal. She was Secretary-Treasurer and Vice President of Information Systems of Meliora Research Associates, Rochester, NY from 1988 to 1998.
