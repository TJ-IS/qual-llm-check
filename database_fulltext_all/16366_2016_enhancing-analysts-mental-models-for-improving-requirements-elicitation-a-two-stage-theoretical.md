---
otero_id: 16366
otero_key: "PK58CPDN"
title: "Enhancing Analysts’ Mental Models for Improving Requirements Elicitation: A Two-stage Theoretical Framework and Empirical Results"
authors: "Padmal Vitharana; Fatemeh Zahedi; Hemant Jain"
year: "2016"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00444"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 17 Issue 12

Article 1

12-28-2016

# Enhancing Analysts’ Mental Models for Improving Requirements Elicitation: A Two-stage Theoretical Framework and Empirical Results

Padmal Vitharana , padmal@syr.edu

Fatemeh "Miriam" Zahedi , zahedi@uwm.edu

Hemant K. Jain , hemant-jain@utc.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

Research Paper

ISSN: 1536-9323

# Enhancing Analysts’ Mental Models for Improving Requirements Elicitation: A Two-stage Theoretical Framework and Empirical Results

Padmal Vitharana

Whitman School of Management, Syracuse University padmal@syr.edu

Fatemeh Mariam Zahedi

Sheldon B. Lubar School of Business, University of Wisconsin - Milwaukee zahedi@uwm.edu

Hemant K. Jain

College of Business, University of Tennessee at Chattanooga Hemant-jain@utc.edu

Abstract:

Research has extensively documented the importance of accurate system requirements in avoiding project delays, cost overruns, and system malfunctions. Requirement elicitation (RE) is a critical step in determining system requirements. While much research on RE has emerged, a deeper understanding of three aspects could help significantly improve RE: 1) insights about the role and impacts of support tools in the RE process, 2) the impact of using support tools in multiple stages of the RE process, and 3) a clear focus on the multiplicity of perspectives in assessing RE outcomes. To understand how using support tools could improve RE, we rely on the theoretical lens of mental models (MM) to develop a dynamic conceptual model and argue that analysts form mental models (MMs) of the system during RE and these MMs impact their outcome performance. We posit that one can enhance analysts’ MMs by using a knowledgebased repository (KBR) of components and services embodying domain knowledge specific to the target application during two key stages of RE, which results in improved RE outcomes. We measured the RE outcomes from user and analyst perspectives. The knowledge-based component repository we used in this research (which we developed in collaboration with a multi-national company) focused on insurance claim processing. The repository served as the support tool in RE in a multi-period lab experiment with multiple teams of analysts. The results supported the conceptualized model and showed the significant impacts of such tools in supporting analysts and their performance outcomes at two stages of RE. This work makes multiple contributions: it offers a theoretical framework for understanding and enhancing the RE process, develops measures for analysts’ mental models and RE performance outcomes, and shows the process by which one can improve analysts’ RE performance through access to a KBR of components at two key stages of the RE process

Keywords: Component-based Development, Requirements Elicitation, Mental Models, Domain Knowledge, Knowledge-based Repository of Components and Services.

## 1 Introduction

Requirement elicitation (RE) constitutes one of requirements analysis’s most challenging aspects (Meth, Mueller, & Maedche, 2015; Rosenkranz, Vranešić, Holten, 2014; Whittenberger, 2014). RE involves “uncovering, extracting, and surfacing” the needs and wants of potential users and other stakeholders (Zowghi & Coulin, 2005, p. 21). Three issues hinder far-reaching improvements in RE. The first issue relates to the method of eliciting requirements and the tools for supporting analysts in the RE process (Blais, 2014; Mathiassen, Tuunanen, Saarinen, & Rossi, 2007). Researchers have suggested various methods for eliciting requirements, including interviewing, prototyping, joint application development (JAD), and protocol analysis (Marakas & Elam, 1998; Moody, Blanton, & Chenery, 1998; Zowghi & Coulin, 2005). Additionally, researchers have developed several tools to either manage the RE process or provide cognitive support to analysts; the latter includes EasyWinWin, Requirement Apprentice, ACME/PRIME, AbstFinder, and AMORE (Christel, Wood, & Stevens, 1993; Grünbacher & Boehm, 2001; Reubenstein & Waters 1991; Zwoghi & Coulin, 2005). However, practitioners do not widely adopt these tools (Zwoghi & Coulin, 2005). Hence, research has yet to fully address analysts’ need for support tools to better understand the domain of the target application and uncover users’ requirements (Zwoghi & Coulin, 2005). One of the reasons for this shortcoming is the lack of adequate research and theoretical insight into the process by which cognitive support tools containing application domain knowledge can assist analysts in the RE process.

The second issue is that, with a few exceptions (e.g., Browne & Ramesh, 2002), most published work treats RE as a single task at the end of which one produces a list of requirements. Although many sources have recognized the complexity of the RE process (ModernAnalyst, 2014; Rosenkranz et al., 2014), no theoretical framework exists to gain insights into the RE process. Investigating the RE process at well-defined stages makes it possible to understand what factors are at play in each stage, how one can assess and improve the outcome of each stage, and the impact of intermediary outcomes’ cascading from one stage to the next.

The third issue is lack of attention to the multiplicity of perspectives in assessing RE outcomes. The need for assessing outcomes from the perspective of multiple stakeholders has been recognized and routinely recommended. However, in most cases the focus has been on users and project owners (e.g., Browne & Rogich, 2001). While analysts are in the front line of performing the RE tasks and have major input in decisions, research has not considered their perspective and assessments and has assumed that they coincide with those of system owners and users.

We address the above issues by investigating the following research questions:

RQ1: Does using cognitive support tools enhance analysts’ RE outcomes, and, if so, what is the process by which this enhancement occurs?

RQ2: Does using cognitive support tools at different stages of RE impact the outcomes, and what are the cascading influences of such impacts?

RQ3: Is there a difference in evaluating RE outcomes from the users’ perspectives vis-à-vis analysts perspectives?

To answer these research questions, we synthesize the theory of mental models and the schema theory to form an overarching theory to conceptualize a dynamic model of analysts’ cognitive process. Our conceptualization integrates three critical parts: 1) analysts’ internal cognitive process, 2) tools that could improve this process, and 3) stages and metrics for assessing the outcome of RE from the perspective of users and analysts.

This paper makes several contributions. First, we contribute to theory by conceptualizing how access to cognitive-support tools (more specifically, knowledge-based repositories of domain specific components and services<sup>1</sup>), could enhance analysts’ cognitive process at various stages of RE and, consequently, augment analysts’ domain knowledge and outcome performance. Our conceptualization provides insight into the RE process and opens a new avenue of research in this area. Second, we add to the literature by focusing on different stages of RE process and present a dynamic model involving two key stages of RE: pre-interview questionnaire development and post-interview requirements list generation. Our dynamic model provides a new conceptualization of analysts’ cognitive process, demonstrates how the outcome of one stage impacts the next, and identifies the stage at which using support tools is most effective. Finally, we propose metrics for RE outcomes from multiple perspectives—users and analysts.

This paper has significant managerial implications as well. Project managers can use the findings to make cognitive support tools available to analysts, which could have a handsome payoff. Our results provide motivations for designing and developing knowledge-based repositories for supporting the RE process. Furthermore, our work informs managers that they should assess perceptions and outcomes at different stages of the RE process and that using supporting tools early on has the best payoffs in terms of improved RE outcomes.

## 2 Literature Review

## 2.1 Requirement Elicitation

Elicitation refers to the process of gathering user requirements that engages the analyst in learning, uncovering, extracting, surfacing, and discovering users’ needs (Hickey & Davis, 2004; Zowghi & Coulin, 2005). Researchers have proposed a vast array of methodologies to elicit requirements, which Tuunanen (2003) and Zwoghi and Coulin (2005) review. However, interviewing has emerged as the most commonly employed RE methodology (Browne & Rogich, 2001; Duggan & Thachenkary, 2003; Hadar, Soffer, & Kenzi, 2014; Marakas & Elam, 1998; Moody et al., 1998), and many other RE methodologies involve some aspect of user interviews (e.g., Zowghi & Coulin, 2005). Compared to other methods, interviewing engages users effectively and is more dynamic and interactive in that analysts can easily alter the line of questioning based on user responses (Agarwal & Tanniru, 1990; Browne & Rogich, 2001; Davis, Dieste, Hickey, Juristo, & Mureno, 2006; Hoffman, Shadbolt, Burton, & Klein, 1995; Zowghi & Coulin, 2005). Davis et al. (2006, p. 182) point out that interviews “appear to be one of the most effective elicitation techniques in a wide range of domains and situations”. Therefore, in this research, we focus on interviews as the method of eliciting requirements.

The RE task entails inherent cognitive challenges (Appan & Browne, 2010; Chakraborty, Sarkar, & Sarkar, 2010; Hadar et al., 2014; Pitts & Browne, 2004), and researchers have proposed RE tools to address them by 1) supporting the management of the RE process (e.g., automation), 2) providing cognitive support for analysts, or 3) both (Zowghi & Coulin, 2005). Research has shown tools that provide cognitive support to improve RE outcomes (Pitts & Browne, 2004; Zwoghi & Coulin, 2005). In this paper, we focus on cognitive support tools because cognitive challenges due to inadequate knowledge about the domain of the target application can create major barriers to communicating with users and eliciting requirements (Pitts & Browne, 2004).

## 2.2 Component/Service Repositories

The recent availability of component/service repositories that provide domain knowledge to analysts could serve as a new class of cognitive support tools for RE (Sabou & Pan, 2007; Vitharana et al. 2012). These repositories contain knowledge relevant to specific target applications and provide useful knowledge such as detailed descriptions of components and their use (Vitharana, Zahedi, & Jain, 2003b; Vitharana et al., 2012). The approach by which one creates a component repository affects its capacity to serve as a cognitive support tool. There are four approaches to composing component repositories. First, some repositories comprise components that their creators have identified from existing applications or business units in one organization and designed them for subsequent reuse (Levi & Arsanjani, 2002). Second, developers who build components on as needed basis and who store them for future reuse populate certain repositories (Herzum & Sims, 2000; Levi & Arsanjani, 2002). Third, some scholars have offered a set of heuristics for identifying components that focuses on attributes such as marketability, granularity, reusability, and autonomy level (Herzum & Sims, 2000). In this case, the repository is built from these components. Organizations have built several commercial repositories such as SAP Enterprise Services Workplace, Salesforce AppExchange, Google Apps Marketplace, and Amazon Web Services using a combination of these three approaches.

The fourth approach has a conceptual and domain-specification focus on component fabrication (De Cesare, Lycett, & Macredie, 2006; Herzum & Sims, 2000; Levi & Arsanjani, 2002). Jang, Kim, and Lee (2003) used a set of objects along with use-cases to identify components by first conducting an affinity analysis among objects and between objects and use-cases to group more cohesive objects into components. We direct interested readers to Birkmeier and Overhage (2009) and Lau and Wang (2007), who comprehensively review component-identification approaches and component repositories.

## 2.3 Knowledge-based Repository

Focusing on the fourth approach, Vitharana, Jain, and Zahedi (2003a, 2012) propose the concept of a knowledge-based repository (KBR) with emphasis on domain-specific components. The KBR has two building blocks: structures as the inter-component architecture and component specifications as the intracomponent architecture. Together, they capture the relevant knowledge of the target domain.

KBR structures capture knowledge about domain-level business processes and business flows and map them to components through 1) business process templates, 2) use-cases, and 3) sequence diagrams. Business process templates exemplify the typical business processes and process flows of the domain. Process templates are organized in a hierarchical fashion such that subprocesses of a higher-level business process are created to embed domain knowledge at multiple-levels of granularity. Process templates embody best practices in the target domain. Use cases depict interactions among actors and typical processes. Sequential relationships between components capture the domain knowledge through preceding and succeeding relationships that depict business processes in which components are used.

KBR component specifications reflect the domain knowledge specific to components at two levels: basic and faceted. Basic information contains key attributes of a component such as its description and business domain. Faceted information contains domain knowledge about component facets such as the business objects, functions, rules, tasks, events, and people associated with the component. For example, facets for an auto insurance “claim-assessment” component might include relevant objects (such as the claim and the police report), rules (such as a description of relevant business rules for damage assessment), events (such as accident and claim dates), and people (such as clients and assessors).

Acquiring knowledge from such repositories requires an appropriate interface. KBRs include a user-friendly interface to search, navigate, and investigate application domain components, use cases, and process templates at several levels of abstraction. One can search components using general keywords that the repository matches against both basic and faceted information to find the related components. Alternatively, one can use keywords corresponding to specific basic or faceted information during the search, which enables analysts to start with a broad search in an industry or business domain and then progressively narrow the search. The iterative and interactive nature of the KBR interface provides flexibility during search. Search results also show the relationships between preceding and succeeding components. One can explore the hierarchical structure of business process templates and corresponding components to further acquire specific information.

Hence, KBR contains application domain knowledge and provides the facility to interrogate the repository to gain insights about the domain that one cannot access as easily otherwise. Vitharana et al. (2012) argue that knowledge-based component repositories can serve as learning tools for analysts. In this study, we use KBR to investigate whether using such tools can provide cognitive support for analysts and improve outcomes at different stages of the RE process.

## 3 Theoretical Framework

The study of the impact of cognitive support tools, specifically KBR, on the RE outcomes requires developing a model that conceptualizes how the impact occurs. In doing so, we rely on the synthesis of the mental models theory and schema theory as our overarching theoretical framework.

## 3.1 Theory of Mental Models

When solving problems, people create a mental model of the problem situation (Savage-Knepshield, 2001). Craik (1943) was the first to argue that individuals form internal models of events and circumstances. Johnson-Laird (1983) coined the term “mental models”. Broadly defined, mental models (MMs) are “representations of objects, events, and processes that people construct through interaction with their environment” (Savage-Knepshield, 2001, p. 2). Mental models (MMs) have a relatively long history in multiple fields of inquiry, including psychology, computer science, cognitive science, neuroscience, and information systems (Appendix A summarizes applications of MMs in information systems). In information systems and human-computer interactions, MMs refer to the internal representation of objects, relationships, and abstract concepts in a system (Gentner & Gentner, 1983; Greeno, 1983; Johnson-Laird, 1983; Staggers & Norcio, 1993).

Requirement elicitation (RE) is a problem-solving process in which analysts develop an understanding of users’ needs and desires and create MMs of the proposed system (Kudikyala & Vaughn, 2005; Zmud, Anthony, & Stair, 1993). MMs enable individuals to describe, explain, and predict a system’s<sup>2</sup> behaviors in terms of its “purpose (why the system exists)”, “function (how the system operates)”, “state (what the system is doing)”, and “form (what the system looks like)” (Rouse & Morris, 1986, p. 351). Following Rouse and Morris, we define viable MMs as those that represent the purpose, functions, states, and forms of the target computer system. Literature in RE contains studies that are well suited for operationalizing analysts’ viable MMs (Browne & Rogich, 2001; Yadav, Bravoco, Chatfield, & Rajkumar, 1988). While these authors do not refer to analysts’ MMs directly, they note the need to analyze RE problems in terms of the goals, processes, tasks, and information of proposed systems. In synthesizing the theory of MMs and research on RE, we argue that, during the RE process, analysts examine organizational goals and needs in terms of the following aspects of a system: 1) fulfilling relevant organizational goals through suitable system goals (purpose), 2) supporting salient business processes (functions), (3) supporting tasks to be performed in the business processes (state), and 4) providing information or data needed to perform such tasks (forms). We use these aspects to measure analysts’ MMs<sup>3</sup>.

## 3.2 Schema Theory

While MMs contain knowledge about the target system, they differ from domain knowledge (Rouse & Morris, 1986). MMs are specific, while domain knowledge is broad and general (Kieras & Bovair, 1984). MMs are local to the target system, whereas domain knowledge is global and encompasses various situations (Hegarty & Just, 1993). However, MMs and domain knowledge interact dynamically. The schema theory elucidates the distinction between MMs and domain knowledge and explains their interactions<sup>4</sup>.

According to schema theory, knowledge is structured and stored in memory in the form of schemata (Schmidt, 1975). Schemata are abstracted inner representations of individual experiences and connected in a network of subschemata and other related schemata that collectively represent a person’s domain knowledge (Rumelhart & Ortony, 1977; Rumelhart, 1980). Individuals use schemata to interpret events, sensory data, and information, to retrieve past memory, determine goals, plan for actions, and solve problems (Satzinger & Oldfman, 1998).

Researchers view MMs as simple, robust, and parsimonious packets of knowledge for dealing with a specific situation (Stubbart, 1989; Vandenbosch & Higgins, 1996; Walsh, 1988). MMs also have schemata, but schemata in MMs are specific to a situation (in this case, the target application). The schemata representations of domain knowledge are far more abstract, generalized, and networked. Learning from a given experience (i.e., exploring the KBR during RE) takes place when the schemata in MMs (specific to the target system) are adjusted, which are then abstracted and incorporated into the schemata in domain knowledge to become part of the updated general knowledge (Bartlett, 1932; Rumelhart & Norman, 1978). Researchers have shown that individuals with more viable MMs have better performance outcomes in terms of accuracy, efficiency, or other salient measures (Satzinger & Olfman, 1998). In the research model we present in Section 4, we argue that KBR as a cognitive support tool enhances analysts’ MMs and, thus, leads to superior RE outcomes.

## 4 Model Conceptualization

We synthesize the theory of MMs and schema theory to develop dynamic mental models in RE (DMMs-RE). DMMs-RE is a two-stage model that conceptualizes the dynamics of the RE process and theorizes the impact of using KBR on analysts’ MMs and domain knowledge. Figures 1 and 2 present DMMs-RE for Stages 1 and 2, respectively. In DMMs-RE, hypotheses for Stages 1 and 2 are identified by Q (questions) and R (requirements). For the sake of model parsimony, we treat analysts’ profiles, including prior experience, as control variables.

## 4.1 Dependent Variables

There are two pivotal stages in which assisting analysts could enhance the viability of their MMs. Stage 1 refers to the pre-interview stage when individuals retrieve salient schemata from their prior domain knowledge to form MMs of the system being developed in preparation of interview questions.

![](/api/attachments/PK58CPDN/fulltext/images/8457b51c8fa28cfdcbcad85a238ce8842d6d3c66ec2182c20b785c2459ff8503.jpg)  
Figure 1. Dynamic Mental Models in RE (DMMs-RE): Stage 1

![](/api/attachments/PK58CPDN/fulltext/images/20f566807cdf4f7232d7153bd02f9d9edbc951de3a2bc082360b9c97fd1d4859.jpg)  
Figure 2. Dynamic Mental Models in RE (DMMs-RE): Stage 2

Performance metrics for evaluating the two stages of RE should be based on outcomes at the evaluation points: the interview questions (Stage 1) and the list of elicited requirements (Stage 2). Therefore, outcome metrics constitute the dependent variables in the two stages of the RE process. We argue that outcomes should be evaluated from multiple perspectives: analysts themselves and others including users, the software development organization, and project team leaders. In this research, we focus on two major perspectives for outcome evaluation: self-evaluation by analysts and other-assessed evaluation based on a set of objective dimensions. Browne and Pitts (2004) use the quantity and quality of requirements as a measure of analyst’s ability to employ certain stopping rules during information search. We adopt this approach to measure other-assessed outcomes in terms of the quantity and quality of outcomes at Stages 1 and 2.

Scholars such as Napier, Mathiassen, and Johnson (2009) demonstrate the effectiveness of using multiple stakeholder perceptions and judgments in RE process improvement efforts. With the exception of Guinan, Cooprider, and Faraj (1998) who employed self-reported and stakeholder-reported measures for the RE performance evaluation, using multiple perspectives in performance evaluation is uncommon and is rarely measured at different stages of the RE process. We argue that self-evaluation of analysts is critical to encourage the use of supporting tools to enhance the analysts’ MMs. Following the main argument in the technology adoption model (Venkatesh, 2000), if analysts do not find a cognitive support tool useful in increasing their performance at different stages of RE, they have little motivation to use it. Furthermore, studies on intrinsic and extrinsic motivations have highlighted the distinction between self- versus otherfocused motivations and perspectives (Calder & Staw, 1975; Deci & Ryan, 1987; Ryan & Deci, 2000; Osterloh & Frey, 2000; Vallerand, 1997), both of which could be useful in improving outcomes.

## 4.2 Hypotheses

Research has found that people form initial MMs and then continually adjust them as they engage in solving problems (Braverman 1997; Chua, Storey, & Chiang, 2012; Moore & Engel, 2001; Satzinger & Olfman, 1998; Thiel, Bagdasarow, Harkrider, Johnson, & Mumford, 2012; van de Ven & Sun, 2011; Vandenbosch & Higgins, 1996; Waern, 1990). Studies in decision support systems indicate that spending time exploring the relevant procedures and cues available in support tools promote deep learning and MM enhancement (Kayande, de Bruyn, Lilien, Rangaswamy, & van Bruggen, 2009). It is shown that analysts form MMs during the RE process (Dawson & Swatman, 1999). As the RE proceeds and new information emerges, analysts adjust their MMs and, as a result, update their domain knowledge because, as research has shown, prior domain knowledge may not be adequate or relevant and prior experience may not fit the problem at hand (Krause, Kelly, Corkins, & Tasooji, 2009; McCloskey, 1983; Rouse & Morris, 1986). Various sources such as documents, observations, and discussions can provide new information. Exposure to varied and relevant experiences improves the viability of analysts’ MMs and, as a result, enhances their domain knowledge (Kelso & Norman, 1978; Schmidt, 1975; Shayo & Olfman, 2000).

One’s ability to identify parts of a system and understand their causal relationships plays a key role in shaping one’s MMs of the system (Kriz & Hegarty, 2004). Moray (1987) argues that individuals could make MMs of complex systems more viable if they decompose the system into smaller, simpler, and independent functional units to reduce their cognitive loads in perceiving and forming MMs. Some model of the target system is often used to help individuals understand associated stakeholders, events, processes, parts, and relationships (Wand & Weber, 2002). Research has shown that exposure to such models of the target system helps individuals create more viable MMs (Borgman, 1986; Cardinale, 1991; Savage-Knepshield, 2001).

Since KBR as a cognitive support tool contains components encompassing “parts” of the business domain in which the target system resides, we argue that using KBR enhances analysts’ MM. Each component in KBR conveys objects, events, and people associated with the domain in terms of basic and faceted information and, therefore, salient to the target system. As analysts engage in the cognitively challenging RE task, they could navigate the KBR to understand key aspects such as business processes involved, objects, relevant events, critical tasks, business rules, and use cases to garner a better understanding of the target system’s domain. This insight enhances their MMs of the target system and helps them formulate user interview questions.

Recall that MMs refer to “representations of objects, events, and processes that people construct” (Savage-Knepshield, 2001, p. 2). KBR enhances MMs because it provides analysts with explicit information through its components and structures salient to the target system, which include specific objects, events, and processes, and relationships among components. Hence, using KBR could assist analysts by enhancing their MMs to move closer to what users may need or desire.

Furthermore, we argue that using KBR enhances analysts’ MMs in both Stages 1 and 2. At Stage 1, analysts acquire insights by searching KBR to formulate their questions prior to interviews with stakeholders. Such exposure allows them to become aware of specifics such as goals, processes, tasks, and information salient to the target system. At Stage 2, the increased awareness of users’ needs and wants through interviews allows analysts to use the KBR to formulate requirements in a more precise fashion. Thus, at both stages of the RE process, analysts’ use of KBR improves their MMs. Hence:

H1(Q): Greater use of the KBR at Stage 1 is positively associated with better MMs at Stage 1.

H1(R): Greater use of the KBR at Stage 2 is positively associated with better MMs at Stage 2.

The theory of MMs argues that prior knowledge and experience formulate individuals’ initial MMs in problem solving (Vandenbosch & Higgins, 1996). The schema theory supports this argument in dealing with a given situation when individuals first draw salient schemata from the network of schemata in their memory. This is further confirmed by empirical studies, which show that individuals rely on prior experiences and domain knowledge to form MMs in dealing with the current situation (Bartlett, 1932; Vandenbosch & Higgins, 1996). Kriz and Hegarty (2004) further claim that individuals with higher domain knowledge form MMs that incorporate a high-level functional understanding of the system but that those lacking domain knowledge form MMs that focus only at the local level. Moreover, they found that those with higher domain knowledge have an information advantage for meaningfully assessing their MMs and adjusting them as necessary when new information becomes available (such as access to KBR). Similarly, analysts with higher prior domain knowledge and experience at the start of Stage 1 are better positioned to form enhanced MMs of the target system as they engage in developing interview questions, especially with exposure to cues available from KBR. This argument is based on the schemata revision in the theory of MMs and the corresponding memory update in the schema theory.

At Stage 2, analysts start with prior knowledge as well. However, prior knowledge at the start of Stage 2 corresponds to domain knowledge updated when one completes Stage 1 because pre-interview activities including using KBR modify analysts’ MMs. Schema theory posits that the modified MMs dynamically influence domain knowledge, which leads individuals to revise their abstracted and generalized schemata, subschemata, and their networks. This updated domain knowledge corresponds to prior knowledge at Stage 2. Therefore, analysts start Stage 2 with the updated domain knowledge obtained at the end of Stage 1, which forms a foundation for analysts’ MMs in developing the list of requirements at Stage 2. Therefore, at Stage 2, the updated domain knowledge plays a role similar to that of prior domain knowledge at Stage 1. Hence:

H2(Q): Higher level of prior domain knowledge is positively associated with better MMs at Stage 1.

H2(R): Higher level of updated domain knowledge at Stage 1 is positively associated with better MMs at Stage 2.

When people encounter a situation, they retrieve the relevant schemata from their existing network of schemata in the memory, which represents their current domain knowledge. MMs represent a set of schemata activated and applied to a specific situation or condition. Individuals modify specific schemata either through adjusting them, completely re-structuring them, or adding new schemata (Rumelhart & Norman, 1978). Experiencing KBR that contains information salient to the target system can facilitate such schema adjustments. Adjusted schemata that are part of MMs are abstracted and incorporated into the network of schemata in the memory, and so become part of the updated domain knowledge (Bartlett, 1932). Thus, MM is activated from the domain knowledge, and updated MM is abstracted and incorporated as updated domain knowledge. Hence:

H3(Q): Better MMs at Stage 1 are positively associated with higher updated domain knowledge at Stage 1.

H3(R): Better MMs at Stage 2 are positively associated with higher updated domain knowledge at Stage 2.

The key question is whether the updated MMs could improve analysts’ performance at the end of each stage. Research has shown that more viable MMs improve outcome performance (Rouse & Morris, 1986; Savage-Knepshield, 2001; Vandenbosch & Higgins, 1996). We examine performance from two perspectives: self-evaluation by analysts and other assessed based on a set of objective dimensions.

Following the theory of MMs, we argue that analysts’ enhanced MMs result in higher self-assessed performance in terms of the questions and requirements list they generate. Mental models enhanced with cues from KBR give analysts deeper insights into the probable users’ requirements by providing them with the means to understand the goals, processes, tasks, and information entailed in the target system. Enhanced MMs allow one to make better inferences and predictions about potential behavior (Borgman, 1986). This ability to better understand, infer, and predict makes analysts more confident and satisfied with their task outcomes (Balijepally, Nerur, & Mahapatra, 2015; He, Erdelez, Wang, & Shyu, 2008; Kulesza, Stumpf, Burnett, & Kwan, 2012). Moreover, MMs influence task self-efficacy (Kulesza et al., 2012; Ramalingam, LaBelle, & Wiedenbeck, 2004) and create an overall positive experience in performing the task (Savage-Knepshield, 2001). Greater insights into the target system from enhanced MMs improve analysts’ perceptions about the outcomes at each stage of the RE process. Hence:

H4(Q): Better MMs at Stage 1 are positively associated with higher self-evaluation of questions at Stage 1.

H4(R): Better MMs at Stage 2 are positively associated with higher self-evaluation of the requirements list at Stage 2.

Mental models enhanced by a cognitive support tool also impact other-assessed outcomes at Stages 1 and 2 because using KBR enables analysts to formulate questions and identify requirements that are salient to the domain of the target system, which increases the specificity and relevance of the interview questions and requirements list. This argument is also in line with the task technology fit (TTF) theory, which postulates that workers’ performances improve when there is a good fit between a task and the technology supporting workers as they perform the task (Goodhue & Thompson, 1995; Teo & Men, 2008). In RE, the task is to develop the interview questions and requirements list, and the technology is KBR.

Past research in many fields in myriad contexts has also revealed the link between MMs and other-assessed outcome performance. Some have argued MMs and performance are “intimately linked” (Baecker & Buxton, 1987). Studies report that enhanced MMs lead to higher quality, are more effective, and are less error-prone solutions (Balijepally et al., 2015; He et al., 2008; Hester et al., 2012; Rouse & Morris, 1986; Savage-Knepshield, 2001; Satzinger & Olfman, 1998; Staggers & Norcio, 1993). Mental models also help individuals find creative solutions to complex and ill-defined problems (Hester et al., 2012). Creative solutions manifest from MMs’ ability to influence the execution of critical cognitive processes such as searching for information, generating and evaluating ideas, and monitoring solutions (Ellis & David, 2005; He et al., 2008; Staggers & Norcio, 1993; Weick, 1995). Requirements elicitation is inherently a complex, ill-defined task and, therefore, KBR-enhanced MMs should lead to higher quality interview questions at Stage 1 and requirements list at Stage 2. Hence:

H5(Q): Better MMs at Stage 1 are positively associated with higher other-assessed quality of questions at Stage 1.

H5(R): Better MMs at Stage 2 are positively associated with higher other-assessed quality of the requirements list at Stage 2.

Enhanced MMs result in outcomes not only with higher quality but also in higher quantity—more questions at the end of Stage 1 and a more detailed requirements list at the end of Stage 2. Exposure to details of salient components and well-organized structures among components give analysts more ideas about the processes, tasks, and goals of the target system, which motivates them to ask creative questions and create a more informed requirements list. Moreover, in comparison to their counterparts, those with enhanced MMs are less likely to remember facts irrelevant to the task at hand (Mayer & Gallini, 1990). Considering irrelevant facts can hinder one from completing the task, which results in fewer interview questions and a shorter requirements list. With greater insights into the target system through cues from KBR on salient components and structures among them, analysts should recall more relevant information about the target system, which will result in more interview questions and a longer requirements list. Hence:

H6(Q): Better MMs at Stage 1 are positively associated with higher other-assessed quantity of questions at Stage 1.

H6(R): Better MMs at Stage 2 are positively associated with higher other-assessed quantity of the requirements list at Stage 2.

The enhanced performance outcomes of Stage 1 (interview questions) improve the performance outcomes at Stage 2. When analysts construct superior questionnaires (whether it is perceived (self-assessed) or otherwise (other-assessed)), they will be more effective in interviewing users to obtain the most relevant information necessary for constructing the requirements list (Agarwal & Tanniru, 1990; Browne & Rogich,

2001; Marakas & Elam, 1998). In contrast, when analysts produce fewer questions or questions irrelevant to the target system or the users’ needs and wishes, the effectiveness of interviews suffers, which results in a lower performance at Stage 2. Hence:

H7(R): Higher self-evaluation of questions at Stage 1 is positively associated with higher selfevaluation of the requirements list at Stage 2.

H8(R): Higher other-assessed quality of questions at Stage 1 is positively associated with higher other-assessed quality of the requirements list at Stage 2.

H9(R): Higher other-assessed quantity of questions at Stage 1 is positively associated with higher other-assessed quantity of the requirements list at Stage 2.

## 5 Research Methodology and Data Collection

## 5.1 Instrument Development

Based on well-established published studies, we developed the instrument to collect data for the model constructs. Table 1 reports the definitions of constructs and corresponding references. Appendix B reports the instrument. We developed the second-order latent construct for MMs for this work based on the original definition by Rouse and Morris (1986) and systems aspects defined by Yadav et al. (1988), Browne and Rogich (2001), Browne and Pitts (2004), and Pitts and Browne (2004).

Table 1. Construct Definitions

<table><tr><td>Construct</td><td>Definition</td><td>References</td></tr><tr><td>Domain knowledge</td><td>Expertise in and understanding of various aspects and key issues of the domain of the target system.</td><td>Coughlan &amp; Macredie (2002), Havelka (2002), Larsen &amp; Naumann (1992), Schenk, Vitalari, &amp; Davis (1998), Vitharana et al. (2012)</td></tr><tr><td>Mental models</td><td>The schemata of the target system in terms of purpose, functions, processes, and forms. It has four subdimensions: goals: purposes, advantages and benefits of the system processes: business processes and flows incorporated in the system tasks: rules, outcomes and reasons for tasks that support business processes and goals in the system, and information: information and data needed to perform tasks and create reports</td><td>Browne &amp; Rogich (2001), Browne &amp; Pitts (2004), Pitts &amp; Browne (2004), Rouse &amp; Morris (1986), Yadav et al. (1988), developed for this study</td></tr><tr><td>Self-evaluation of interview questions</td><td>Analysts&#x27; self-evaluation of the interview questions in revealing all aspects of users&#x27; needs and desires.</td><td>Duggan &amp; Thachenkary (2004), Yadav, Adya, Sridhar, &amp; Nath (2009)</td></tr><tr><td>Self-evaluation of requirements lists</td><td>Analysts&#x27; self-evaluation of the completeness of requirements list and their confidence in its accuracy, quality, and clarity.</td><td>Duggan &amp; Thachenkary (2004), Yadav et al. (2009)</td></tr><tr><td>Other-assessed quality and quantity of questions and requirements list</td><td>Judges&#x27; assessment of the quality and number of interview questions and requirements in the list evaluated based on salient dimensions of the target system.</td><td>Duggan &amp; Thachenkary (2003), Gilliland &amp; Landis (1992), Pitts &amp; Browne (2004)</td></tr></table>

In RE, analysts need to understand users’ goals for the proposed system, relevant business processes, corresponding tasks, and information necessary to perform those tasks (Browne & Rogich, 2001; Yadav et al., 1988). Therefore, we identified four subdimensions of MMs that cover specific aspects of the target system: goals, processes, tasks, and information. We developed items for these subdimensions based on the definitions of each subdimension. We used three rounds of card sorting to ensure the constructs’ validity and reliability. Each round involved two sorters. Following Ebel (1951), the calculated inter-sorter reliability for the third round of card sorting resulted in 0.94—a value that is considered quite acceptable.

## 5.2 The Experimental Design and Protocol

We used a two-stage controlled experiment for testing DMMs-RE. The stimulus for the experiment was a KBR of components in the auto insurance claim-processing domain that we developed in collaboration with a large multi-national corporation. We used this KBR (called the “tool” for brevity) to support analysts at Stages 1 and 2 of the RE process. Appendix C provides the details of the tool. We developed a protocol for collecting data in Stages 1 and 2 with an RE scenario (see Appendix D). The experimental treatment was having access to the tool at Stages 1 and 2. The control was lack of access to the tool. The design of the experiment was full factorial design with respect to the use of the tool at Stages 1 and 2: 2 x 2 = 4. Thus, we randomly assigned the subjects to four groups<sup>5</sup>. Group 1 had no access to the tool at both stages (control group), Group 2 had access to the tool only at Stage 1, Group 3 had access to the tool only at Stage 2, and Group 4 had access to the tool at both stages<sup>6</sup>. We built an experiment website to provide access to the tool, to administer the survey questions, and to collect the groups’ questions and requirements lists at the end of Stages 1 and 2.

Prior to conducting the main study, we carried out a pilot study using 11 graduate students enrolled in an information systems course. In this pilot study, we focused on testing the experiment website, the survey instrument at three points (start of Stage 1, end of Stage 1, and end of Stage 2), the access to the tool, and the overall flow of the experiment. Based on results of the pilot study, we made a few minor changes to the instrument and the website. For the main experiment, we recruited students from two large universities in the US with a background in system analysis and design. We carried out the experiment over one semester. We collected data over three consecutive semesters. We gave subjects course credit for participating in the study. In addition, we offered four randomly drawn cash prizes of \$100 each as an additional incentive.

## 5.3 Data Collection

We collected data in three stages. At the start of the experiment, all subjects answered online survey questions about their personal profiles (demographics and prior experiences) and prior domain knowledge. At Stage 1, subjects in groups 2 and 4 had access to the tool. After creating interview questions, subjects uploaded them to the experiment website and took the survey to answer questions about MMs at Stage 1, updated domain knowledge at Stage 1, self-assessment of the uploaded interview questions, and use of the tool if applicable.

Subsequently, subjects interviewed the user (see Appendix D for details). We (i.e., all three authors, who were all familiar with the domain) performed the user role, which we did to control for user variability across subjects. The users followed a standard detailed script to provide answers to subject’s questions during interviews. This approach ensured consistency across subjects and avoided introducing bias due to variability of user answers. We also took measures to achieve consistency among users (see Appendix E for details). We set up interview schedules in advance based on subjects’ and users’ schedules. Users were unaware of the grouping of subjects (whether they had access to the tool at the time of the interview or not), which minimized potential bias. After they finished the interview, subjects prepared the list of requirements. Subjects in groups 3 and 4 had access to the tool during this stage. After uploading the list of requirements to the experiment website, subjects completed the survey to answer questions about MMs at Stage 2, updated domain knowledge at Stage 2, self-assessment of the uploaded requirements list, and use of the tool if applicable. In total, 154 subjects completed all phases of the study.

A panel of paid professional judges acted as the external raters, who evaluated the quality and quantity of questions and requirements. The judges based their assessments on ten objective dimensions. We developed these dimensions based on an existing auto insurance claim-handling system. Appendix F reports the dimensions, their definitions, and the process we used to train the judges. One judge was the chief information officer of a company and an adjunct professor who taught systems analysis and design courses at a university in the northeastern United States. The other judge was the chief executive officer of an IT-driven mobile services company. Both had extensive experience in system analysis and design in general and requirements analysis in particular. Between them, they had 37 years of systems analysis and design, and 20 years of requirements analysis experience. Appendix G provides the details of inter-rater reliability checks.

## 6 Analysis

Subjects’ average age was 27 years, and 32 percent of the subjects were female. The average length of their experience in system analysis and design, computer programming, and software testing/debugging was 4.8, 9.3, and 6.2 months, respectively. On a 0-100 scale, the means (standard deviations) for the selfreported survey of subjects’ knowledge about insurance claim handling, information systems development, and requirements analysis were 29 (23), 51 (26), and 49 (26), respectively.

Table 2 reports the reliability checks for Stages 1 and 2. Composite reliability (CR) in excess of 0.70 is considered acceptable for establishing reliability (Hair, Anderson, Tatham, & Black, 1998).

Table 2. Reliability Checks: Stage 1 and Stage 2

<table><tr><td colspan="2">Model constructs at Stage 1</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>CR</td></tr><tr><td colspan="2">1. Prior domain knowledge</td><td>0.93</td><td></td><td></td><td></td><td></td><td>0.95</td></tr><tr><td colspan="2">2. Use of the tool: Stage 1</td><td>0.20</td><td>0.95</td><td></td><td></td><td></td><td>0.97</td></tr><tr><td colspan="2">3. Analysts&#x27; MMs: Stage 1</td><td>0.58</td><td>0.41</td><td>0.88</td><td></td><td></td><td>0.93</td></tr><tr><td colspan="2">4. Updated domain knowledge: Stage 1</td><td>0.76</td><td>0.37</td><td>0.71</td><td>0.96</td><td></td><td>0.97</td></tr><tr><td colspan="2">5. Self-evaluation of questions: Stage 1</td><td>0.38</td><td>0.22</td><td>0.58</td><td>0.52</td><td>0.91</td><td>0.93</td></tr><tr><td>Model constructs at Stage 2</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>CR</td></tr><tr><td>1. Updated domain knowledge: Stage 1</td><td>0.96</td><td></td><td></td><td></td><td></td><td></td><td>0.97</td></tr><tr><td>2. Use of the tool: Stage 2</td><td>0.17</td><td>0.96</td><td></td><td></td><td></td><td></td><td>0.97</td></tr><tr><td>3. Analysts&#x27; MMs: Stage 2</td><td>0.45</td><td>0.20</td><td>0.90</td><td></td><td></td><td></td><td>0.94</td></tr><tr><td>4. Updated domain knowledge: Stage 2</td><td>0.54</td><td>0.17</td><td>0.78</td><td>0.96</td><td></td><td></td><td>0.98</td></tr><tr><td>5. Self-evaluation of questions: Stage 1</td><td>0.52</td><td>0.06</td><td>0.61</td><td>0.52</td><td>0.91</td><td></td><td>0.94</td></tr><tr><td>6. Self-evaluation of requirements list: Stage 2</td><td>0.38</td><td>0.15</td><td>0.83</td><td>0.60</td><td>0.67</td><td>0.95</td><td>0.97</td></tr></table>

\* Diagonal elements in bold are the square root of average variance extracted (AVE); off diagonal elements are correlations among constructs. CR = composite reliability.

All CR values exceeded the acceptable threshold. For sufficient convergent and discriminant validity, the square root of the average variance extracted (AVE) must exceed construct correlations for all constructs (Gefen, Straub, & Boudreau, 2000). Table 2 indicates support for this criterion. We examined factor loadings to further investigate convergent and discriminant validity. Except for two items loading marginally lower (both at 0.69), all other loadings were above 0.70 with no evidence of significant cross loadings (Appendix H). Hence, the results indicated support for the reliability and validity of constructs.

Several data-collection features reduced the threat of common method variance. First, we collected it over multiple time periods and from multiple sources (subjects and judges). Further, we designed scales to be neutral over a continuous scale (Podsakoff, MacKenzie, Lee, & Podsakoff, 2003). To minimize the potential threat of common method variance, we followed Podsakoff et al. (2003) and purified the data by using a marker item, which we did not include in the analysis. A marker item is a data item that one measures but does not use in the model. The purification process involved regressing each item on the marker item, and we captured and used the regression residuals as the purified data for the item. We used the purified data in the model estimations.

We used SEM as our analysis approach and Mplus statistical software (ver. 6.12) to analyze the data. Appendix I reports factor loadings in the measurement model for Stages 1 and 2. Construct items and MM dimensions had loadings above 0.90, high t-values with all p < 0.0001, and R<sup>2</sup> values at or above 0.81, which provides support for the indicators and MM dimensions as appropriate measures of their respective constructs (Bollen, 1989; Gefen et al. 2000). Table 3 reports the fit indices for the measurement model and model estimation. The indices for the measurement model indicate good fit. The indices for the estimated model also show a satisfactory fit.

Table 3. Fit Indices for the Measurement Model and Model Estimation

<table><tr><td rowspan="2">Fit index</td><td colspan="2">Measurement models</td><td colspan="2">Model estimations</td><td rowspan="2">Threshold*</td></tr><tr><td>Stage 1</td><td>Stage 2</td><td>Stage 1</td><td>Stage 2</td></tr><tr><td>Normed chi-square</td><td>1.39</td><td>1.54</td><td>1.55</td><td>1.89</td><td>&lt;3.0</td></tr><tr><td>CFI (comparative fit index)</td><td>0.985</td><td>0.979</td><td>0.971</td><td>0.954</td><td>&gt;0.90</td></tr><tr><td>TLI (Tucker-Lewis index)</td><td>0.982</td><td>0.976</td><td>0.967</td><td>0.949</td><td>&gt;0.90</td></tr><tr><td>RMSEA (root mean square error of approximation)</td><td>0.050</td><td>0.059</td><td>0.060</td><td>0.076</td><td>&lt;0.06</td></tr><tr><td colspan="6">* Threshold values are based on Bentler (1992), Bentler and Bonnet (1980), Browne and Cudeck (1993) and Hu and Bentler (1999)</td></tr></table>

Figures 3 and 4 show the estimation results for Stages 1 and 2.  
![](/api/attachments/PK58CPDN/fulltext/images/1617c11dd39f7d1623a557830adf709bd6422c09992e1a5b857d2eadee7f2a36.jpg)

Figure 3. Estimation of Dynamic Mental Models in RE (DMMs-RE): Stage 1  
![](/api/attachments/PK58CPDN/fulltext/images/fa7dcdfdd002a52e759a8413baaac3c6a4988d4b68684ad8962586fe22d445bf.jpg)  
Figure 4. Estimation of Dynamic Mental Models in RE (DMMs-RE): Stage 2

The examination of the construct $\mathsf { R } ^ { 2 }$ values showed strong explanatory power for MMs in Stage 1 and Stage 2 (0.65 and 0.53, respectively; both significant at $\mathsf { p } < 0 . 0 0 1 )$ . This result indicates that use of the tool and prior domain knowledge significantly explained the viability of analysts’ MMs in both stages. At Stage 1, updated domain knowledge had an ${ \dot { \mathsf { R } } } ^ { 2 }$ value of 0.72 and self-evaluation of outcome had an $\bar { \mathsf { R } } ^ { 2 }$ value of 0.67, which indicated a relatively high explanatory power. These ${ \mathsf { R } } ^ { 2 }$ values were even higher at Stage 2. Updated domain knowledge had an ${ \mathsf { R } } ^ { 2 }$ value of 0.84 and self-evaluation of requirements list had an R<sup>2</sup> value of 0.92, which indicates that analysts’ MMs at Stage 2 and performance at Stage 1 in developing a quality questionnaire explained almost all variability of self-reported performance at Stage 2. The other-assessed outcomes had lower but still statistically significant ${ \mathsf { R } } ^ { 2 }$ values. At Stage 1, the ${ \mathsf { R } } ^ { 2 }$ values for other-assessed quality and quantity of questions were 0.16 and 0.17, respectively. At Stage 2, the ${ \mathsf { R } } ^ { 2 }$ values for other assessed quality and quantity of requirements list doubled to 0.32 and 0.34, respectively. It is interesting to note that the explanatory power of all outcomes improved markedly from Stage 1 to Stage 2, which indicates increased role of MMs as the RE progressed.

We expected the somewhat lower R<sup>2</sup> values for other-assessed outcomes since the other-assessed evaluations of outcomes were based on a relatively large set of objective dimensions (as we report in Appendix F), which might have differed from analysts’ self-evaluation criteria. This result confirms the research that has found that perceptual metrics do not necessarily correspond to objective metrics (Lilien, Rangaswamy, Van Bruggen, & Starke, 2004) and indicates two different perspectives for evaluating RE outcomes. Collectively, the fit indices and ${ \dot { \mathsf { R } } } ^ { 2 }$ values showed excellent fit and statistically significant explanatory power at both stages of the conceptualized model.

The path coefficients in both stages were highly significant. At Stage 1, the results support all six hypotheses (Figure 3). At Stage 2, the results support all nine hypotheses (Figure 4). The impact of analysts’ using the tool at Stage 1 had a significant path coefficient $( 0 . 3 0 ; \mathsf { p } < 0 . 0 0 1 )$ on MMs at Stage 1. Analysts’ use of the tool continued to influence their MMs at Stage 2 (path coefficient = 0.14; p < 0.05). However, the magnitude of this coefficient was less than half of that in Stage 1, which indicates the critical importance of using the tool at early stages of RE. Prior domain knowledge at Stage 1 and updated domain knowledge at the start of Stage 2 had a significant impact on MMs at both stages $( \mathsf { p } < 0 . 0 0 1 )$ as hypothesized. Interestingly, the path coefficients of this impact were almost identical at both stages (0.65 vs. 0.67), which indicates the continued importance of domain knowledge and its updates throughout the RE process.

The results for MMs’ influence on outcome variables at both stages were impressively strong. MMs at Stage 1 impacted the updated domain knowledge with a path coefficient of 0.84 $( \mathsf { p } < 0 . 0 0 1 )$ . This impact was even higher at Stage 2, with a path coefficient of 0.91 $( { \mathsf { p } } < 0 . 0 0 1 ) ^ { 7 }$ . MMs’ role in analysts’ performance was equally impressive and almost identical for self-assessed outcome evaluations with a path coefficient of 0.80 $( { \mathsf p } <$ 0.001) at Stage 1 and 0.78 $( \mathsf { p } < 0 . 0 0 1 )$ at Stage 2. MMs had also strong influence on other-assessed quality and quantity during Stage 1: both had a path coefficient of 0.33 $( \mathsf { p } < 0 . 0 0 1 )$ , which indicates their equal impact on both other-assessed quality and quantity of questions. MMs’ impact on other-assessed quality and quantity outcomes continued at Stage 2 with path coefficients of 0.53 and 0.55 (both $\mathsf { p } < 0 . 0 0 1 )$ respectively. The path coefficients for MMs  other assessed outcomes increased by more than 60 percent. This result indicates the increasing importance of MMs in the later stages of RE. Together, the above results further support the theory of mental models and schema theory and explain how MMs mediate the impact of using the tool on performance outcomes.

Finally, the outcomes of Stage 1 in terms of self-evaluation of questions and other-assessed quality and quantity of questions had a significant impact on the corresponding outcomes of Stage 2. Stage 1 selfevaluation of questions had a strong impact on self-evaluation of requirements list at Stage 2 with a path coefficient of 0.27 $( \mathsf { p } < 0 . 0 0 1 )$ . The path coefficients for other-assessed quality and quantity of questions were 0.09 $( \mathsf { p } < 0 . 0 1 )$ and 0.11 (p < 0.001), respectively. This indicated that superior questions in terms of quality and quantity significantly impacted multiple perspectives of outcome evaluations.

Of control variables, experience was statistically significant on self-evaluation of questions $( \mathsf { p } < 0 . 0 5 )$ at Stage 1. It also was significant on other-assessed quality and quantity of questions (p < 0.01 and p < 0.001) at Stage 1 and those of requirements (both at $\mathsf { p } < 0 . 0 1 )$ at Stage 2. These results indicate the importance of experience in producing high-quality outcomes in the RE process.

## 7 Discussions, Contributions, and Implications

Our conceptualized research model posits that analysts’ mental models (MMs) play a critical role in both stages of RE in terms of self-assessed and other-assessed outcomes. Our results support this premise.

This finding is novel since it shows how analysts’ MMs influence the interview questions and list of requirements assessed from two important perspectives.

Our results showed that the use of KBR directly influenced analysts’ MMs, which, in turn, impacted their domain knowledge and RE outcomes. The use of KBR positively influenced analysts’ understanding of salient users’ needs and desires as manifested in its mediated impact (through MMs) on self-assessed and other-assessed quality and quantity of questions and requirements lists. This finding is significant since it not only shows that using such tools could improve RE outcomes but also uncovers the process by which such improvements occur. As the strong coefficient indicates, tool use had more influence on MMs during Stage 1 than Stage 2 (path coefficients of 0.30 vs. 0.14). Hence, analysts’ MMs underwent greater enhancement after the first exposure to the tool during Stage 1 (vis-à-vis Stage 2).

The tool’s use during Stage 1 indirectly affected the other-assessed outcome (list of requirements) in Stage 2 because of the quality and quantity of interview questions. These findings show the importance of effective interview preparation via access to KBR at Stage 1 of RE. Collectively, these results provide insights into the cognitive processes through which using KBR influences both the process and outcome of RE—an important finding that opens the door for using research in cognition to design effective cognitive support tools.

Our results also uncovered the role of domain knowledge and the process by which domain knowledge influences RE and, in turn, gets updated. This finding supports the commonly held belief that analysts accumulate domain knowledge as they proceed through RE’s stages. Our findings strongly support the following progression: starting knowledge plus KBR support  enhanced MMs  higher performance and updated schemata of domain knowledge. This progression shows up in both stages of RE, which indicates that this progression repeats through the RE process. Our results confirm the arguments in the schema theory that mental model formation is a progressive process (Savage-Knepshield, 2001).

In summary, we address the three research questions we state earlier in the paper. First, we show that using cognitive support tools, specifically KBR, enhances analysts’ RE outcomes (questionnaire and requirements list) by enhancing their MMs. Second, we show that KBR impacts RE outcomes at two key stages (interview question and requirements list generation) and that tools such as KBR have a greater impact earlier in the RE lifecycle than they do later, which highlights the cascading effect. Finally, we show that user and analyst perspectives are distinct but collectively important in evaluating RE outcome performance.

## 7.1 Theoretical Contributions

This study makes several significant theoretical contributions. First, it provides a theoretical framework for studying the effectiveness of tool support in facilitating RE. Second, it contributes to the RE field by showing how the theory of mental models and the related schema theory form a suitable framework for investigating the cognitive aspects of the RE process and open the door for using cognitive science research in effective tool design. Third, it synthesizes behavioral research based on mental models for assessing RE tools—a novel approach in requirements analysis that makes it possible to investigate how a tool could change users’ cognition, knowledge, and behaviors as well as process outcomes. Such investigations make it possible to pinpoint the features of the tool that are effective in producing desirable outcomes.

This work is the first to investigate the two crucial stages of RE from the perspective of analysts’ cognitive process and the use of cognitive support tools (specifically, how KBR can enhance this process). It shows the difference between various stages of RE and the ways through which analysts’ domain knowledge and mental models influence the outcomes of the RE process. The conceptual model we propose in this study— dynamic mental models in RE (DMMs-RE)—offers a novel framework to study the dynamics of the RE process in various domains and organizational settings. Our findings that using the tool in Stage 1 is more effective than Stage 2 is a novel theoretical contribution and indicates the importance of a dynamic approach in tool assessments. We show that when one uses a tool in the RE process matters. Therefore, studies must consider when one uses tools to maximize their positive impacts on outcomes.

This study also empirically measures MMs during the RE process. We conceptualize the MMs construct as a second-order factor by synthesizing the theory of mental models and schema theory with systems development in information systems. The validated instrument for this construct will facilitate research in the cognitive aspects of RE and systems development.

Further, this work offers a multiple-perspective approach to evaluating RE outcomes at two key stages. It challenges the assumption of single uniform perspective of outcome assessment and shows that selfevaluation and other-assessment perspectives are distinct and that they should be accounted for separately.

One needs to consider analysts’ own perceptions of outcomes since their self-evaluation could motivate further improvements in interviewing user interviews and eliciting their requirements.

Finally, this research has implications for elicitation methods and user-analyst interaction during RE. Although we used interviews to elicit requirements from our participants, one could use the KBR repository in concert with other approaches such as joint application design (JAD) and prototyping. In essence, the use of KBR is not bound by the RE method and would enhance analysts’ MMs throughout the process. As analysts use KBR during RE, their enhanced MMs facilitate their interaction with users. User-analyst interaction plays an important role in RE (Zowghi & Coulin, 2005), and, hence, by providing the support tools they need to enhance their interaction, the KBR offers analysts the cognitive support they need to improve their RE performance.

## 7.2 Managerial Implications

This work has several implications for managers. The most important insight is that one can improve RE by providing analysts’ access to cognitive support tools (particularly KBR). With a growing number of such repositories becoming available from major vendors such as SAP and Salesforce, it is critical to invest in the architecture of such repositories to conform to KBR that can be made available for use by analysts. Using KBR could have a significant payoff in terms of RE outcomes and the entire system development lifecycle because improvements in RE outcomes upstream in the system development process are shown to have a multiple positive consequence downstream in system design and implementation. Furthermore, access to such tools during the RE process may enable the analyst to assist the system designers in identifying candidate components and services available in the repository that one can reuse when implementing the system.

Further, managers should introduce KBR at the early stages of the RE process. KBR had greater impact on MMs at Stage 1 when compared to Stage 2, which, in turn, influenced the four outcome variables. We also found that interview questions significantly affected the final outcome of the RE process—the requirements list. This finding is in line with previous research that has highlighted the significance of the user interviews in RE (Appan & Browne, 2010; Browne & Rogich, 2001; Marakas & Elam, 1998). Finally, our work shows that the RE process has two distinct stages—questionnaire development for user interviews and requirement generation—and that one should evaluate the outcome of each stage from multiple perspectives to enhance the final outcome of the process.

## 8 Limitations and Future Research

This study has several limitations that could pose threats to its validity. Although all the participants in our study had taken a systems analysis and design course and had a varying degree of IT-related experiences in the field, they had far less field experiences in systems analysis and design than industry professionals. In this respect, this study mirrors similar RE studies (e.g., Appan & Browne, 2010) who have also used students in systems analysis and design as their participants.

The subjects in this study could relate to the problem domain (auto insurance claims). Almost all college students have driving experience and are familiar with auto insurance, which helped them relate to the concept of insurance claim handling and facilitated their understanding of the requirements analysis task and the filing process that we discuss in Section 5X. However, researchers should replicate this work in field experiments with analysts involved in RE.

Second, some analysts may use components and the knowledge encompassed in them as the basis for generating the requirements list rather than eliciting users’ requirements (Dzida & Freitag, 1998). However, once analysts engage with users through a set of well-developed questions, it will be difficult to ignore users’ needs and wishes. In the process of collecting data, we observed that the interviewers were fully engaged in eliciting requirements to produce the requirements list.

This research offers several opportunities for future research. The theoretical framework in this work opens a new avenue to investigate analysts’ cognitive processes that influence outcomes at different stages of systems development. This line of research can significantly improve systems development in terms of quality, cost, and time to market.

Future research should also examine how using support tools could affect the outcomes of subsequent stages such as design and implementation. Domain knowledge is crucial to analysts’ ability to be effective during system design (Adelson & Soloway, 1985; Burton-Jones & Meso, 2006; Dzida & Freitag, 1998;

Khatri, Vessey, Ramesh, Clay, & Park, 2006; Parsons & Wand, 2008). Our study opens a research avenue for investigating how using support tools could assist designers’ cognitive processes and domain knowledge to produce higher-caliber designs.

## 9 Concluding Remarks

In this study, we provide a theoretical framework to help understand the process by which one can enhance RE outcomes by using cognitive tool support. More specifically, we examine the role of analysts’ mental models and domain knowledge in the RE process and provide insights into how using KBR can enhance analysts’ mental model and domain knowledge. We conceptualize the dynamic mental models in RE in two stages: developing interview questions (Stage 1) and generating requirements (Stage 2). The estimated model provided strong support for this theoretical framework and its hypotheses.

## Acknowledgments

We thank Journal of AIS Senior Editor Roger Chiang and the review team for guidance through the review process. We also thank Michel Benaroch for comments and feedback on an earlier version of the paper. This research was funded by grants from the Robert H. Brethen Operations Management Institute and the Earl V. Snyder Innovation Management Center at the Whitman School of Management, Syracuse University.

## References

Adelson, B., & Soloway, E. (1985). The role of domain experience in software design. IEEE Transactions on Software Engineering, 11(11), 1351-1360.

Agarwal, R., & Tanniru, M. R. (1990). Knowledge acquisition using structured interviewing: An empirical investigation. Journal of MIS, 7(1), 123-140.

Appan, R., & Browne, G. (2010). Investigating retrieval-induced forgetting during information requirements determination. Journal of the AIS, 11(5), 250-275.

Baecker, R. M., & Buxton, W. A. S. (1987). Cognition in human information processing. In R. M. Baecker & W. A. S. Buxton (Eds.), Readings in human computer interaction: A multidisciplinary approach. San Mateo, CA: Morgan Kaufmann.

Balijepally, V., Nerur, S., & Mahapatra, R. (2015). Task mental model and software developers’ performance: An experimental investigation. Communications of the AIS, 36, 53-76.

Bartlett, F. C. (1932). Remembering: A study in experimental and social psychology. Cambridge, UK: Cambridge University Press.

Bentler, P. M. (1992). On the fit of models to covariances and methodology to the bulletin. Psychological Bulletin, 112(3), 400-404.

Bentler. P. M., & Bonnett, D. G. (1980). Significance tests and goodness of fit in the analysis of covariance structures. Psychological Bulletin, 88(3), 588-606.

Birkmeier, D., & Overhage, S. (2009). On component identification approaches—classification, state of the art, and comparison. In G. A. Lewis, I. Poernomo, & C. Hofmeister (Eds.), Component based software engineering (pp. 1-18). Berlin, Germany: Springer.

Blais, S. (2014). How to ask the right questions part 1: The paradox of the right question and how to ask it. BA Times. Retrieved from http://www.batimes.com/steve-blais/how-to-ask-the-right-questions-part-1- the-paradox-of-the-right-question-and-how-to-ask-it.html

Bollen, K. (1989). Structural equations with latent variables. NY: Wiley and Sons.

Borgman, C. L. (1986). The user’s mental model of an information retrieval system: An experiment on a prototype on-line catalog. International Journal of Man-Machine Studies, 24, 47-64.

Braverman, E. P. (1997). Investigating the relationship between trainees’ mental models and the transfer of training (doctoral dissertation). University of Maryland, Maryland.

Browne, M. W., & Cudeck, R. (1993). Alternative ways of assessing model fit. In K. A. Bollen & J. S. Long (Eds.), Testing structural equation models (pp. 445-455). Newbury Park, CA: Sage.

Browne, G. J., & Pitts, M. G. (2004). Stopping rule use during information search in design problems. Organizational Behavior and Human Decision Processes, 95, 208-224.

Browne, G. J., & Ramesh, V. (2002). Improving information requirements determination: A cognitive perspective. Information & Management, 39, 625-645.

Browne, G. J., & Rogich, M. B. (2001). An empirical investigation of user requirements elicitation: Comparing the effectiveness of prompting techniques. Journal of MIS, 17(4), 223-249.

Burton-Jones, A., & Meso, P. N. (2006). Conceptualizing systems for understanding: An empirical test of decomposition principles in object-oriented analysis. Information Systems Research, 17(1), 38-60.

Calder, B. J., & Staw, B. M. (1975). Self-perception of intrinsic and extrinsic motivation. Journal of Personality and Social Psychology, 31(4), 399-605.

Cardinale, L. A. (1991). Computers in human behavior. Computers in Human Behavior, 7(3), 163-169.

Chakraborty, S., Sarkar, S., & Sarkar S. (2010). An exploration into the process of requirements elicitation: A grounded approach. Journal of AIS, 11(4), 212-249.

Christel, M., Wood, D. P., & Stevens, S. (1993). AMORE: The advanced multimedia organizer for requirements elicitation (CMU/SEI-93-TR-012 technical report).

Chua, C. E. H., Storey, V. C., & Chiang, R. H. L. (2012). Deriving knowledge representation guidelines by analyzing knowledge engineer behavior. Decision Support Systems, 54, 304-315.

Coughlan J., & Macredie, R. D. (2002). Effective communication in requirements elicitation: A comparison of methodologies. Requirements Engineering, 7, 47-60.

Craik, K. (1943). The nature of explanation. Cambridge, UK: Cambridge University Press.

Davis, A., Dieste, O., Hickey, A., Juristo, N., & Moreno, A. (2006). Effectiveness of requirements elicitation techniques: Empirical results derived from a systematic review. In Proceedings of the 14th IEEE International Requirements Engineering Conference (pp. 176-185).

Dawson, L., & Swatman, P. (1999). The use of object-oriented models in requirements engineering: A field study. In Proceedings of the 20<sup>th</sup> International Conference on Information Systems (pp. 260-273).

Deci, E. L., & Ryan, R. M. (1987). The support of autonomy and the control of behavior. Journal of Personality and Social Psychology, 53(6), 1024-1037.

De Cesare, S., Lycett, M., & Macredie, R. D. (2006). Development of component-based information systems. New York: Sharpe.

Derry, S. J. (1996). Cognitive schema theory in the constructivist debate. Educational Psychologist, 31(3), 163-174.

Duggan, E. W., & Thachenkary, C. S. (2003). Higher quality requirements: Supporting joint application development with the nominal group technique. Information Technology and Management, 4(4), 391- 408.

Duggan, E. W., & Thachenkary, C. S. (2004). Supporting the JAD facilitator with the nominal group technique. Journal of Organizational and End User Computing, 16(2), 1-19.

Dzida, W., & Freitag, R. (1998). Making use of scenarios for validating analysis and design. IEEE Transactions on Software Engineering, 24(12), 1182-1196.

Ebel, R. L. (1951). Estimation of the reliability of ratings. Psychometrika, 16(4), 407-424.

Ellis, S., & David, I. (2005). After-event reviews: Drawing lessons from successful and failed experience. Journal of Applied Psychology, 90(5), 857-871.

Elfatatry, A. (2007). Dealing with change: Components verves services. Communications of ACM, 50(8), 35-39.

Gefen, D., Straub, D. W., & Boudreau, M. C. (2000). Structural equation modeling and regression: Guidelines for research practice. Communications of AIS, 4, 1-79.

Gefen, D., Karahanna, E., & Straub, D. W. (2003). Trust and TAM in online shopping an integrated model. MIS Quarterly, 27(1), 51-90.

Gentner, D., & Gentner, D. R. (1983). Flowing waters or teeming crowds: Mental models of electricity. In D. Gentner & A. L. Stevens (Eds.), Mental models (pp. 99-129). Hillsdale, NJ: Erlbaum.

Gilliland, S. W., & Landis, R. S. (1992). Quality and quantity in a complex decision task: Strategies and outcomes. Journal of Applied Psychology, 77(5), 672-681.

Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. MIS Quarterly, 19(2), 213-236.

Greeno, J. G. (1983). Conceptual entities. In D. Gentner & A. L. Stevens (Eds.) Mental models (pp. 227- 252). Hillsdale, NJ: Erlbaum.

Grünbacher, P., & Boehm, B. (2001). EasyWinWin: A groupware-supported methodology for requirements negotiation. In Proceedings of the 8<sup>th</sup> European Software Engineering Conference (pp. 320-321).

Guinan, P. J., Cooprider, J. G., & Faraj, S. (1998). Enabling software development team performance during requirements definition: A behavioral versus technical approach. Information Systems Research, 9(2), 101-125.

Hadar, I., Soffer, P., & Kenzi, K. (2014). The role of domain knowledge in requirements elicitation via interviews: An exploratory study. Requirements Engineering, 19, 143-159.

Hair, J. F., Anderson, R. E., Tatham, R. L., & Black, W. C. (1998). Multivariate data analysis (5<sup>th</sup> ed.). Englewood Cliffs, NJ: Prentice Hall.

Havelka, D. (2002). Requirements determination: An information systems specialist perspective of process quality. Requirements Engineering, 6, 220-236.

He, W., Erdelez, S., Wang F., & Shyu, C. (2008). The effects of conceptual description and search practice on users’ mental models and information seeking in a case-based reasoning system. Information Processing and Management, 44(1), 294-309.

Hegarty, M., & Just, M. A. (1993). Constructing mental models of machines from text and diagrams. Journal of Memory and Language, 32(6), 717-742.

Herzum, P., & Sims, O. (2000). Business component factory. New York: Wiley.

Hester, K. S., Robledo, I. C., Barrettm, J. D., Peterson, D. R., Hougen, D. P., Day, E. A., & Mumford, M. D. (2012). Causal analysis to enhance creative problem-solving: Performance and effects on mental models. Creative Research, 24, 115-133.

Hickey, A. M., & Davis, A. M. (2004). A unified model of requirements elicitation. Journal of MIS, 20(4), 65- 84.

Hoffman, R. R., Shadbolt, N. R., Burton, A. M., & Klein, G. (1995). Eliciting knowledge from experts: A methodological analysis. Organizational Behavior and Human Decision Processes, 62(2), 129-158.

Hu, L., & Bentler, P. M. (1999). Cut-off criteria for fit indexes in covariance matrix analysis: Conventional criteria versus new alternatives. Structural Equation Modeling, 6(1), 1-55.

Johnson-Laird, P. N. (1983). Mental models: Towards a cognitive science of language, inference, and consciousness. Cambridge, UK: Cambridge University Press.

Jang, Y., Kim, E., & Lee, K. (2003). Object-oriented component identification method using the affinity analysis technique. In D. Konstantas, M. L´eonard, Y. Pigneur, & S. Patel (Eds.), Object oriented information systems (pp. 317-321). Heidelberg, Germany: Springer.

Kayande, U., de Bruyn, A., Lilien, G. L., Rangaswamy, A., & van Bruggen, G. H. (2009). How incorporating feedback mechanisms in a DSS affects DSS evaluations. Information Systems Research, 20(4), 527- 546.

Kelso, J. A. S., & Norman, P. E. (1978). Motor schema formation in children. Developmental Psychology, 14(2), 153-156.

Khatri, V., Vessey, I., Ramesh, V., Clay, P., & Park, S. (2006). Understanding conceptual schemas: Exploring the role of application and IS domain knowledge. Information Systems Research, 17(1), 81-99.

Kieras, D. E., & Bovair, S. (1984). The role of a mental model in learning to operate a device. Cognitive Science, 8, 255-273.

Kotlarsky, J., & Oshri, I. (2009). Managing component-based development in global teams. New York: McMillan.

Krause, S., Kelly, J., Corkins, J., & Tasooji, A. (2009). Using students' previous experience and prior knowledge to facilitate conceptual change in an introductory materials course. In Proceedings of the 39<sup>th</sup> ASEE/IEEE Frontiers in Education Conference.

Kriz, S., & Hegarty, M. (2004). Constructing and revising mental models of a mechanical system: The role of domain knowledge in understanding external visualizations. In Proceedings of the 26th Annual Conference of the Cognitive Science Society.

Kudikyala, U. K, & Vaughn, R. B. (2005). Software requirement understanding using pathfinder networks: Discovering and evaluating mental models. Journal of Systems and Software, 74, 101-108.

Kulesza, T., Stumpf, S., Burnett, M., & Kwan, I. (2012). Tell me more? The effects of mental model soundness on personalizing an intelligent agent. In J. A. Konstan, E. H. Chi, & K. Höök (Eds.), Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 1-10). New York: ACM.

Larsen, T. J., & Naumann, J. D. (1992). An experimental comparison of abstract and concrete representations in systems analysis. Information & Management, 22, 29-40.

Lau, K., & Wang, Z. (2007). Software component models. IEEE Transactions on Software Engineering, 33(10), 709-724.

Levi, K., & Arsanjani, A. (2002). A goal-driven approach to enterprise component identification and specification. Communications of the ACM, 45(10), 45-52.

Lilien, G.L., Rangaswamy, A., Van Bruggen, G. H., & Starke, K. (2004). DSS effectiveness in marketing resource allocation decisions: Reality vs. perception. Information System Research, 15(3), 216-235.

Lim, K. H., Ward, L. M., & Benbasat, I. (1997). An empirical study of computer system learning: Comparison of co-discovery and self-discovery methods. Information Systems Research, 8(3), 254- 272.

Ma, L., Ferguson, J., Roper, M., & Wood, M. (2007). Investigating the viability of mental models held by novice programmers. In Proceedings of the Technical Symposium on Computer Science Education (pp. 499-503).

Marakas, G. M., & Elam, J. J. (1998). Semantic structuring in analyst acquisition and representation of facts in requirements analysis. Information Systems Research, 9(1), 37-63.

Mathiassen, L. Tuunanen, T., Saarinen, T., & Rossi, M. (2007). A contingency model for requirements development. Journal of AIS, 8(11), 569-597.

Mayer, R. E., & Gallini, J. K. (1990). When is an Illustration worth ten thousand words? Journal of Educational Psychology, 82, 715-726.

McCloskey, M. (1983). Naive theories of motion. In D. Gentner & A. L. Stevens (Eds.), Mental models (pp. 299-324). Hillsdale, NJ: Erlbaum.

Meth, H., Mueller, B., & Maedche, A. (2015). Designing a Requirement Mining System. Journal of AIS, 16(9), 799-837.

Minsky, M. (1975). A framework for representing knowledge. In P. Winston (Ed), Psychology of computer vision (pp. 211-277). New York: McGraw-Hill.

ModernAnalyst. (2014). Requirements and the beast of complexity. Retrieved from http://www.modernanalyst.com/Resources/Articles/tabid/115/ID/1354/Requirements-and-the-Beastof-Complexity.aspx

Moody, J. W., Blanton, J. E., & Cheney, P. H. (1998). A theoretically grounded approach to assist memory recall during information requirements determination. Journal of MIS, 15(1), 79-98.

Moore, C., & Engel, S. A. (2001). Mental models change rapidly with implicitly acquired information about the local environment: A two-tone image study. Journal of Experimental Psychology: Human Perception and Performance, 27(5), 1211-1228.

Moray, N. (1987). Intelligent aids, mental models, and the theory of machines. International Journal of an-Machine Studies, 27(5-6), 619-629.

Napier, N. P., Mathiassen, L., & Johnson, R. D. (2009). Combining perceptions and prescriptions in requirements engineering process assessment: An industrial case study. IEEE Transactions on Software Engineering, 35(5), 593-606.

Nassaji, H. (2007). Schema theory and knowledge-based processes in second language reading comprehension: A need for alternative perspective. Language Learning, 57, 79-113.

Osterloh, M., & Frey, B. S. (2000). Motivation, knowledge transfer, and organizational forms. Organizational Science, 11(5), 538-550.

Parsons, J., & Wand, Y. (2008). Using cognitive principles to guide classification in information systems modeling. MIS Quarterly, 32(4), 839-868.

Pitts, M. G., & Browne, G. J. (2004). Stopping behavior of systems analysts during information requirements elicitation. Journal of MIS, 21(1), 203-226.

Podsakoff, S., MacKenzie, B., Lee, J. Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research: A critical review of the literature and recommended remedies. Journal of Applied Psychology, 88(5), 879-903.

Ramalingam, V., LaBelle, D., & Wiedenbeck, S. (2004). Self-efficacy and mental models in learning to program. In Proceedings of the 9<sup>th</sup> Annual SIGCSE Conference on Innovation and Technology in Computer Science Education (pp. 171-175).

Reubenstein, H. B., & Waters, R. C. (1991). The requirements apprentice: Automated assistance for requirements acquisition. IEEE Transactions on Software Engineering, 17(3), 226-240.

Rosenkranz, C., Vranešić, H., & Holten, R. (2014). Boundary interactions and motors of change in requirements elicitation: A dynamic perspective on knowledge sharing. Journal of the Association of Information Systems, 15(6), 306-345.

Rouse, W. B., & Morris, N. M. (1986). On looking into the black box: Prospects and limits in the search for mental models. Psychological Bulletin, 100(3), 349-363.

Rumelhart, D. E. (1980). Schemata: The building blocks of cognition. In R. Spiro, B. Bruce, & W. Brewer (Eds.), Theoretical issues in reading comprehension (pp. 33-58). Hillsdale, NJ: Lawrence Erlbaum.

Rumelhart, D. E., & Ortony, A. (1977). The representation of knowledge in memory. In R. C. Anderson, R. J. Spiro, & W. E. Montague (Eds.), Schooling and the acquisition of knowledge (pp. 99-135). Hillsdale, NJ: Erlbaum.

Rumelhart, V. E., & Norman, D. A. (1978). Accretion, tuning, and restructuring: Three modes of learning. In J. W. Cotton & R. L. Klatzky (Eds.), Semantic factors in cognition. Hillsdale, NJ: Lawrence Erlbaum Associates.

Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. American Psychologist, 55(1), 68-78.

Sabou, M., & Pan, J. (2007). Towards semantically enhanced web service repositories. Journal of Web Semantics, 5(2), 142-150.

Santhanam, R., & Sein, M. K. (1994). Improving end-user proficiency: Effects of conceptual training and nature of interaction. Information Systems Research, 5(4), 378-399.

Satzinger, J. W., & Olfman, L. (1998). User interface consistency across end-user applications: The effects on mental models. Journal of MIS, 14(4), 167-193.

Savage-Knepshield, P. A. (2001). Mental models, issues in construction, congruency, and cognition (doctoral dissertation). Rutgers University, New Jersey.

Schenk, K. D., Vitalari, N. P., & Davis, K. S. (1998). Differences between novice and expert systems analysts: What do we know and what do we do? Journal of MIS, 15(1), 9-50.

Schmidt, R. A. (1975). A schema theory of discrete motor skill learning. Psychological Review, 82(4), 225- 260.

Shayo, C., & Olfman, L. (2000). The role of training in preparing end users to learn related software. Journal of End User Computing, 12(1), 3-13.

Shea, C. H., & Wulf, G. (2005). Schema theory: A critical appraisal and reevaluation. Journal of Motor Behavior, 37(2), 85-101.

Skarlatidou, A., Cheng, T., & Haklay, M. (2012). What do lay people want to know about the disposal of nuclear waste? A mental model approach to the design and development of an online risk communication. Risk Analysis, 32(9), 1496-1511.

Staggers, N., & Norcio, A. F. (1993). Mental models: Concepts for human-computer interaction research. International Journal of Man-Machine Studies, 38, 587-605.

Stubbart, C. I. (1989). Managerial cognition: A missing link in strategic management research. Journal of Management Studies, 26(4), 325-347.

Teo, T. S. H., & Men, B. (2008). Knowledge portals in Chinese consulting firms: A task-technology fit perspective. European Journal of Information Systems, 17, 557-574.

Thiel, C. E., Bagdasarow, Z, Harkrider, L., Johnson, J. F., & Mumford, M. D. (2012). Leader ethical decisionmaking in organizations: Strategies for sensemaking. Journal of Business Ethics, 107, 49-64.

Tuunanen, T. (2003). A new perspective on requirements elicitation methods. Journal of Information Technology Theory and Application, 5(3), 45-72.

Vallerand, R. J. (1997). Toward a hierarchical model of intrinsic and extrinsic motivation. In M. P Zanna (Ed.), Advances in experimental social psychology (vol. 29, pp. 271-360). New York: Academic Press.

van de Ven, A. H., & Sun, K. (2011). Breakdowns in implementing models of organization change. Academy of Management Perspective, 25(3), 58-74.

Vandenbosch, B., & Higgins, C. (1996). Information acquisition and mental models: An investigation into the relationship between behavior and learning. Information Systems Research, 7(2), 198-214.

Venkatesh, V. (2000). Determinants of perceived ease of use: Integrating control, intrinsic motivation, and emotion into the technology acceptance model. Information Systems Research, 11(4), 342-365.

Vitharana, P., Jain, H., & Zahedi, F. M. (2003a). Design, retrieval, and assembly in component based software development. Communications of ACM, 46(11), 97-102.

Vitharana, P., Zahedi, F. M., & Jain, H. (2003b). Knowledge-based repository scheme for storing and retrieving business components: A theoretical design and an empirical analysis. IEEE Transactions on Software Engineering, 29(7), 649-664.

Vitharana, P., Jain, H., & Zahedi, F. M. (2012). A knowledge based component/service repository to enhance analysts’ domain knowledge for requirements analysis. Information & Management, 49(1), 24-35.

Waern, Y. (1990). On the dynamics of mental models. In D. Ackermann & M. J. Tauber (Eds.), Mental Models and human-computer interaction 1. Human factors in information technology no. 3. Amsterdam, Holland: Elsevier Press.

Walsh, J. P. (1988). Selectivity and selective perception: An investigation of managers’ belief structures and information processing. Academy of Management Journal, 31(4), 873-896.

Wand, Y., & Weber, R. (2002). Research commentary: Information systems and conceptual modeling—a research agenda. Information Systems Research, 13(4), 363-376.

Weick, K. E. (1995). Sensemaking in organizations. Thousand Oaks, CA: Sage.

Whittenberger, A. (2014). The top 8 mistakes in requirements elicitation. BA Times. Retrieved from http://www.batimes.com/articles/the-top-8-mistakes-in-requirements-elicitation.html

Yadav, S. B., Bravoco, R. R., Chatfield, A. T., & Rajkumar, T. M. (1988). Comparison of analysis techniques for information requirement determination. Communications of the ACM, 31(9), 1090-1097.

Yadav, V., Adya, M., Sridhar, V., & Nath, D. (2009). Flexible global software development (GSD): Antecedents of success in requirements analysis. Journal of Global Information Management, 17(1), 1-31.

Zmud, R. W., Anthony, W. P., & Stair, R. M. (1993). The use of mental imagery to facilitate information identification in requirements analysis. Journal of Management Information Systems, 9(4), 175-191.

Zowghi, D., & Coulin, C. (2005). Requirements elicitation: A survey of techniques, approaches, and tools. In A. Aurum & C. Wohlin (Eds.), Engineering and managing software requirements (pp. 19-46). New York: Springer.

## Appendix A: Selected Applications of Mental Models in Information Systems

<table><tr><td>Santhanam &amp; Sein (1994)</td><td>Examined the effects of two types of training methods (conceptual model and procedural) and two levels of nature of interaction (novel and simple tasks) on users&#x27; proficiency in forming accurate MMs of an electronic mail system.</td></tr><tr><td>Vandenbosch &amp; Higgins (1996)</td><td>Proposed two types of learning in using executive support systems: 1) MM maintenance in which new information fits into existing MMs and confirms them and 2) mental model building in which MMs are changed to accommodate new information.</td></tr><tr><td>Lim, Ward, &amp; Benbasat (1997)</td><td>Examined two types of computer learning, self-discovery and co-discovery (two users working together) and interpreted results in a mental model framework.</td></tr><tr><td>Satzinger &amp; Olfman (1998)</td><td>Investigated whether the consistency of the user interface across applications affects MM development when a user learns and uses multiple applications.</td></tr><tr><td>Borgman (1999)</td><td>Investigated how to train users to develop mental models of a system while interacting with it.</td></tr><tr><td>Savage-Knepshield (2001)</td><td>Investigated how exposure to information about a system&#x27;s internal operation through an explicit conceptual model led to the construction of a mental model that was more congruent with the system&#x27;s operation.</td></tr><tr><td>Ma, Ferguson, Roper, &amp; Wood (2007)</td><td>Investigated the viability of mental models held by novice computer programmers.</td></tr><tr><td>He et al. (2008)</td><td>Investigated the effects of conceptual description and search practice on users&#x27; mental models in a case-based reasoning retrieval (CBR) system.</td></tr><tr><td>Kayande et al. (2009)</td><td>Evaluated design characteristics that facilitate the alignment of a decision maker&#x27;s MM with the decision model embedded in a decision support system (DSS).</td></tr><tr><td>Chua et al. (2012)</td><td>Applying the theory of mental models, presented a think-aloud verbal protocol study used to understand how knowledge engineers extract domain knowledge from textual sources.</td></tr><tr><td>Kulesza et al. (2012)</td><td>Explored how users&#x27; mental model soundness impacts their ability to personalize an intelligent agent.</td></tr><tr><td>Skarlatidou, Cheng, &amp; Haklay (2012)</td><td>Demonstrated how an approach based on mental models was used in the development of an online information system to select a site for disposing nuclear waste.</td></tr></table>

## Appendix B: Instrument

We measured all construct items on a semantic differential continuous scales: very low (0) to very high (100). We collected prior experience for various categories and number of months. External raters performed external evaluations of quantity and quality of questions and reported this information as objective measures (see Appendix F). All questions started with “I characterize” for constructs and “I rate” for selfevaluation. Items are used in Stages 1 and 2.

## Domain knowledge (DK), prior and updated in Stages 1 and 2

Dk1: My understanding of the various aspects of insurance claim handling as:

Dk2: My understanding of what insurance claim handling involves as:

Dk3: My grasp of the key issues relevant to insurance claim handling as:

## Reported use of the knowledge-based tool (USE)

Use1: The amount of time I spent reading the material available in the KB as:

Use2: The amount of time I spent on navigating through the KB as:

Use3: The number of searches I performed while using the KB as:

## Mental model (MM) subdimensions goal (GOAL)

Goal1: My understanding of the advantages of developing the new system as:

Goal2: My understanding of the benefits of the new system as:

Goal3: My understanding of the purpose the new system should serve as:

## Process (PROC)

Proc1: My understanding of the types of processes (ex. claim registration, claim settlement) involved in the new system as:

Proc2: My understanding of the sequence of processes involved in the new system as:

Proc3: My overall understanding of the processes involved in the new system as:

## Task (TASK)

Task1: My understanding of the business rules for each task (ex. vehicle damage claim is not due to regular wear and tear) in the new system as:

Task2: My understanding of the outcome of each task (ex. the claim is verified to be valid) in the new system as:

Task3: My understanding of the reasons for each task (ex. fraud prevention) in the new system as:

## Information (INFO)

Info1: My understanding of the information in the reports (ex. updated insurance rating of the customer) generated by the new system as:

Info2: My understanding of the information and data saved by the system as:

Info3: My understanding of the input data needed in the new system as:

## Self-evaluation of questions (QE)

Qe1: The quality of the questionnaire I developed as:

Qe2: My confidence that I included enough questions in my questionnaire as:

Qe3: My confidence that my questionnaire covers all aspects of the users' needs as:

## Self-evaluation of requirements list (RE)

Re1: The completeness of my list as:

Re2: My confidence in the accuracy of my list in reflecting the users' requirements as:

Re3: The clarity of items in my list as:

Re4: The quality of my list as:

## Appendix C: Description of the Tool Used in the Experiment

In this paper, we use a knowledge-based repository of domain specific components and services developed in collaboration with a multi-national software consulting company. With a multi-national company, we designed this KBR to handle auto-insurance claims, which meets the requirements of a supporting tool for RE. The tool provides opportunities for analysts to learn about major entities, attributes, processes, and business rules related to the domain.

The tool has thirty components and twelve business process templates related to auto insurance claim handling. It has been implemented as a Web-based system and includes following main features:

1. Hierarchical organization of components

2. Representation of component precedence relationships through previous/next buttons

3. Structured attributes of components (i.e., basic information) such as name, description, domain, deployment environment, and

4. The ability to probe deeper into component structures to discover how the components work and their relationships to other components.

For example, analysts can obtain the following description of an auto insurance claim-assessment component<sup>8</sup>:

This component supports the business process of selecting an assessor for a claim and supports the whole assessment process. It gets the details of the accident, searches for various available assessors, helps choose an appropriate assessor and assigns that assessor. The assessor carries out the assessment, enters the details of the report and also estimates the salvage value for the damaged property.

By examining this description, the analyst could discover that claim processing requires searching and selecting appropriate assessor, assessing damages and salvage value, and creating a report.

5. More elaborate methodologies for coding and classifying components (besides components’ textual descriptions). The tool uses the facet-based scheme for describing components. Analysts can use facets such as “functions”, which describe business functions that components perform, “roles” that components could play in a potential application, “business rules” applicable to components, and “actions” that components could initiate. An example of a business rule is: an assessor must be assigned within x days of a claim submission.

6. Process templates representing important processes and subprocesses of the domain represented in business process modeling notation (BPMN). Process templates, for instance, represent the typical “best practice” business workflows showing the process tasks and their relationships (see Figure C1 for an example).

7. Search capability. Analysts could search for a component by typing keywords, selecting one or more fields from basic information, or entering one or more words describing facet information. Analysts can search process templates in a similar fashion, based on various search criteria, including types of application, functions, and other aspects. Users can narrow down search results by searching in previous searches’ results.

![](/api/attachments/PK58CPDN/fulltext/images/e19fcede73cfa35a54f3639b20dbab87b305539b776bbdb49c1be451556e929e.jpg)  
Figure C1. A Typical Business Process for Auto Insurance Claim Handling

## Appendix D: Experiment Protocol and Scenario

## Protocol

The experiment protocol included an RE task description, the sequence of RE process in the experiment, the use of the tool (the knowledge-based repository described in Appendix C), and a research website to manage the multi-period process. We developed a scenario for RE in the experiment. We gave subjects the task of performing RE for a new system based on this scenario. The domain was auto-insurance claim handling. We chose a single domain to control for domain variability.

We created an experiment website to provide assistance to subjects and to manage the data-collection process. We protected the website with a password and varied access to the website depending on the experimental group to which the subject belonged. The experiment website described the project and linked to the tool (access limited based on the experimental group), contained an extensive help file with text and screenshots of the tool (access limited by group type), and linked to survey questions at three stages of the experiment (initial, Stage 1, and Stage 2). Subjects took surveys, accessed the tool, and uploaded their questions and requirements list based on a carefully programmed flow for the experiment.

At the start, subjects received a 20-minute presentation on the research project, its objective, participants role, and incentives. We collected data in three consecutive semesters with different sets of students. Each subject in each semester represented one data point. The study commenced several weeks into the semester and lasted for the remainder of the semester, which we did to simulate real RE environment where RE is performed over a period of time in multiple stages based on the availability of users and analysts. The extended duration of the study allowed the subjects to grasp the experimental scenario, form a mental model about the target system, become comfortable with KBR (if assigned at Stage 1), carry out the interview, use KBR at Stage 2 (if assigned at Stage 2), and develop the list of requirements. We instructed subjects to use only the information provided in this study and not to seek any information from outside sources.

## Experiment Scenario

If you choose to participate, you will assume the role of a systems analyst in order to identify requirements for a new system for auto insurance claim handling. Requirements here refer to the features desired by the users of the new system. The system needs to include all relevant capabilities from customer’s initial submission of the claim to the insurance company to final claim resolution between the insurance company and the customer. Specifically, the new system must support following overarching features: (a) claim investigation, (b) claim assessment, (c) claim settlement, (d) injury treatment, (e) claim subrogation— subrogation is the process by which one insurance company seeks reimbursement from another company or person for a claim it has already paid, (f) salvage processing—bid for or sell the salvage items (e.g., car) that are involved in the claim, and (g) claim dispute—if parties cannot agree on the financial settlement, initiate the arbitration process. Your ultimate objective is generating list of requirements for the new system.

We asked subjects to follow a sequence of steps, briefly described below:

1. After the initial registration on the research website, subjects completed the initial survey about their profiles (including experience) and prior domain knowledge.

2. We asked those who we randomly selected to have access to the knowledge-based tool to carefully browse the tool’s website.

3. We asked all subjects to generate questions for interviews.

4. We gave all subjects sample questions for a hypothetical “student registration” system in order to create a common understanding about the type and format of expected questions for interviews.

5. All subjects uploaded their questions to the research website.

6. After receiving confirmation about the uploaded questions, all subjects were asked to complete the survey questions for Stage 1.

7. We instructed subjects to conduct interviews using their questions to gather user requirements for the new system for handling auto-insurance claims. We instructed them to take notes during the interviews.

8. We scheduled all subjects to interview system users. Three researchers familiar with the car insurance systems met with subjects and played the role of users in the face-to-face interviews.

9. We asked those who we randomly selected to have access to the knowledge-based tool to use the tool prior to developing the list of requirements.

10. We asked subjects to develop the list of requirements. In order to create a common understanding of the type and format of requirements list, we gave all subjects a sample requirements list for a hypothetical “student registration” system. We gave all subjects the categories of requirements that they were expected to identify (system features, action-response sequence, and functions).

11. We asked all subjects to upload their requirements list to the research website.

12. After receiving confirmation about the completion of requirements upload, we asked subjects to complete the survey questions for Stage 2.

## Appendix E: User Consistency Measures

We took measures to maintain consistency among the users. The three users individually created a list of potential interview questions that subjects might ask using the 10 assessment dimensions listed in Appendix F. Then, we synthesized the list of potential questions to create a comprehensive list of potential questions. During multiple iterations, the users worked together in discussing questions, developing responses, and revising questions/responses as appropriate. In users’ views, the list of potential questions in the final document was comprehensive and included essential questions that an analyst would need to know in determining user requirements. We used the final document that contained the list of potential questions (by category) and corresponding responses during the interviews to answer subject analysts’ questions. While the subsequent analysis of interview notes by the three users revealed that there were a handful of questions from a few analysts that were not in the final document developed by the users, these questions were not essential to determining the proposed system’s requirements.

## Appendix F: Other-assessed Evaluation of Outcomes at Stages 1 and 2

Two external judges assessed the quality and quantity of questions (Qs) and requirements (Rs). Over a two-week period, we trained them on how to rate the questions and requirements. We gave them detailed written instructions on the meaning of 10 dimensions. We provided these dimensions to the judges in order for them to rate the overall quality and quantity of each questionnaire and requirement. Based on the rating for the 10 dimensions, we also asked the judges to arrive at an overall quality and quantity rating for Qs and Rs using a 0-10 scale.

The assessment dimensions were: 1) initiation/reporting, 2) claim investigation, 3) claim assessment, 4) claim settlement, 5) injury treatment, 6) claim subrogation, 7) salvage processing, 8) claim dispute, 9) system features, and 10) other. We developed these categories based on an actual auto insurance claim-handling system.

The first dimension refers to those entries that corresponded to customers’ reporting an incident and initiating a claim. The second corresponds to the process of investigating the claim (e.g., is there anything suspicious about the claim that warrants investigation?). The third dimension corresponds to the process of assessing the loss/damages (e.g., how extent of damage/loss is assessed). The fourth dimension corresponds to settling the claim (e.g., how much should we offer the customer to settle the claims?). The fifth dimension corresponds to processes associated with treating injuries. The sixth dimension corresponds to handling claim subrogation (e.g., if the other party is at fault, how will we get money back from other party or its insurance company?). The seventh dimension corresponds to the process of salvaging damaged vehicles (e.g., how is the salvage value of a damaged vehicle recovered? It may involve selling the damaged vehicle.). The eighth dimension corresponds to the process involved in settling any claim disputes (e.g., what is the process to resolve the disputes?). The ninth dimension refers to system features such as availability of the system, system performance, etc. Finally, the “other” dimension that corresponds to processes that the above nine dimensions do not cover.

To train the judges, we used two questionnaires and two requirements from the pilot study and walked them through the rating process. We asked them how they would rate each of the 10 dimensions for quantity and quality as well as overall Qs and Rs quantity and quality. They were then asked to rate the remaining nine Qs and Rs from the pilot study on their own over the next two weeks. Subsequently, judges’ ratings were compared and differences reconciled. Thus, judges learned how to reconcile their rating differences.

## Appendix G: Inter-judge Reliability Checks

We trained two external judges to assess the quality and quantity of questions (Qs) and requirements (Rs) as we describe in Appendix F. After we received the judges’ ratings, we calculated the absolute differences between two judges for the Qs’ and Rs’ quality and quantity. We asked the judges to reconcile the ratings in cases where differences exceeded 2 points (based on the 0-10 scale). During this reconciliation process, judges discussed the differences and came to a consensus in our presence. Following Ebel (1951), we calculated inter-rater reliabilities for ratings prior to and after reconciling differences and report them below. Both raters demonstrated high inter-rater reliability. We used the average of ratings by the two judges after the reconciliation in the analysis.

Table G1. Inter-rater Reliability (Rated by Two External Judges)

<table><tr><td>Other-assessed</td><td>Before reconciliation</td><td>After reconciliation</td></tr><tr><td>Questionnaires (Q)</td><td></td><td></td></tr><tr><td>Quality</td><td>0.88</td><td>0.93</td></tr><tr><td>Quantity</td><td>0.86</td><td>0.93</td></tr><tr><td>Requirements (R)</td><td></td><td></td></tr><tr><td>Quality</td><td>0.95</td><td>0.97</td></tr><tr><td>Quantity</td><td>0.93</td><td>0.96</td></tr></table>

## Appendix H: Exploratory Factor Analysis

Table H1. Factor Loadings at Stage 1 (Questionnaire)

<table><tr><td>Level 1: Antecedents</td><td colspan="2">Factor1</td><td colspan="2">Factor2</td></tr><tr><td>Initial domain knowledge: Dk1-1</td><td colspan="2">0.960</td><td colspan="2">0.075</td></tr><tr><td>Initial domain knowledge: Dk1-2</td><td colspan="2">0.950</td><td colspan="2">0.064</td></tr><tr><td>Initial domain knowledge: Dk1-3</td><td colspan="2">0.941</td><td colspan="2">0.134</td></tr><tr><td>Reported use at Stage 1: Use1-1</td><td colspan="2">0.102</td><td colspan="2">0.974</td></tr><tr><td>Reported use at Stage 1: Use1-2</td><td colspan="2">0.110</td><td colspan="2">0.972</td></tr><tr><td>Reported use at Stage 1: Use1-3</td><td colspan="2">0.064</td><td colspan="2">0.943</td></tr><tr><td>% cumulative variance explained</td><td colspan="2">0.456</td><td colspan="2">0.925</td></tr><tr><td>Level 2: Mental Model</td><td>Factor1</td><td>Factor2</td><td>Factor3</td><td>Factor4</td></tr><tr><td>Goal1: Goal1-1</td><td>0.855</td><td>0.256</td><td>0.211</td><td>0.307</td></tr><tr><td>Goal1: Goal1-2</td><td>0.870</td><td>0.273</td><td>0.226</td><td>0.269</td></tr><tr><td>Goal1: Goal1-3</td><td>0.805</td><td>0.389</td><td>0.201</td><td>0.265</td></tr><tr><td>Process1: Proc1-1</td><td>0.355</td><td>0.766</td><td>0.327</td><td>0.287</td></tr><tr><td>Process1: Proc1-2</td><td>0.337</td><td>0.770</td><td>0.289</td><td>0.322</td></tr><tr><td>Process1: Proc1-3</td><td>0.285</td><td>0.806</td><td>0.234</td><td>0.241</td></tr><tr><td>Task1: Task1-1</td><td>0.245</td><td>0.374</td><td>0.718</td><td>0.478</td></tr><tr><td>Task1: Task1-2</td><td>0.345</td><td>0.414</td><td>0.690</td><td>0.438</td></tr><tr><td>Task1: Task1-3</td><td>0.298</td><td>0.383</td><td>0.688</td><td>0.491</td></tr><tr><td>Information1: Info1-1</td><td>0.284</td><td>0.299</td><td>0.330</td><td>0.802</td></tr><tr><td>Information1: Info1-2</td><td>0.329</td><td>0.258</td><td>0.308</td><td>0.828</td></tr><tr><td>Information1: Info1-3</td><td>0.361</td><td>0.328</td><td>0.347</td><td>0.759</td></tr><tr><td>% cumulative variance explained</td><td>0.254</td><td>0.491</td><td>0.672</td><td>0.926</td></tr><tr><td>Level 3: Outcome</td><td colspan="2">Factor1</td><td colspan="2">Factor2</td></tr><tr><td>Stage 1 updated domain knowledge: Dk2-1</td><td colspan="2">0.945</td><td colspan="2">0.223</td></tr><tr><td>Stage 1 updated domain knowledge: Dk2-2</td><td colspan="2">0.936</td><td colspan="2">0.273</td></tr><tr><td>Stage 1 updated domain knowledge: Dk2-3</td><td colspan="2">0.945</td><td colspan="2">0.245</td></tr><tr><td>Self-reported question evaluation: Qe1</td><td colspan="2">0.218</td><td colspan="2">0.895</td></tr><tr><td>Self-reported questions evaluation: Qe2</td><td colspan="2">0.216</td><td colspan="2">0.927</td></tr><tr><td>Self-reported questions evaluation: Qe3</td><td colspan="2">0.286</td><td colspan="2">0.909</td></tr><tr><td>% cumulative variance explained</td><td colspan="2">0.473</td><td colspan="2">0.918</td></tr></table>

Table H2. Factor Loadings at Stage 2 (Requirements List)

<table><tr><td>Level 1: Antecedents</td><td colspan="2">Factor1</td><td colspan="2">Factor2</td></tr><tr><td>Stage 1 updated domain knowledge: Dk2-1</td><td colspan="2">0.963</td><td colspan="2">0.117</td></tr><tr><td>Stage 1 updated domain knowledge: Dk2-2</td><td colspan="2">0.974</td><td colspan="2">0.053</td></tr><tr><td>Stage 1 updated domain knowledge: Dk2-3</td><td colspan="2">0.972</td><td colspan="2">0.086</td></tr><tr><td>Reported use at Stage 2: Use2-1</td><td colspan="2">0.070</td><td colspan="2">0.976</td></tr><tr><td>Reported use at Stage 2: Use2-2</td><td colspan="2">0.084</td><td colspan="2">0.979</td></tr><tr><td>Reported use at Stage 3: Use2-3</td><td colspan="2">0.100</td><td colspan="2">0.954</td></tr><tr><td>% cumulative variance explained</td><td colspan="2">0.474</td><td colspan="2">0.948</td></tr><tr><td>Level 2: Mental Model at Stage 2</td><td>Factor1</td><td>Factor2</td><td>Factor3</td><td>Factor4</td></tr><tr><td>Goal2: Goal2-1</td><td>0.839</td><td>0.231</td><td>0.301</td><td>0.245</td></tr><tr><td>Goal2: Goal2-2</td><td>0.838</td><td>0.257</td><td>0.243</td><td>0.275</td></tr><tr><td>Goal2: Goal2-3</td><td>0.746</td><td>0.431</td><td>0.162</td><td>0.320</td></tr><tr><td>Process2: Proc2-1</td><td>0.346</td><td>0.711</td><td>0.401</td><td>0.342</td></tr><tr><td>Process2: Proc2-2</td><td>0.351</td><td>0.733</td><td>0.343</td><td>0.357</td></tr><tr><td>Process2: Proc2-3</td><td>0.297</td><td>0.812</td><td>0.258</td><td>0.255</td></tr><tr><td>Task2: Task2-1</td><td>0.309</td><td>0.329</td><td>0.713</td><td>0.454</td></tr><tr><td>Task2: Task2-2</td><td>0.315</td><td>0.416</td><td>0.723</td><td>0.396</td></tr><tr><td>Task2: Task2-3</td><td>0.319</td><td>0.374</td><td>0.704</td><td>0.430</td></tr><tr><td>Information2: Info2-1</td><td>0.309</td><td>0.281</td><td>0.378</td><td>0.785</td></tr><tr><td>Information2: Info2-2</td><td>0.319</td><td>0.295</td><td>0.292</td><td>0.830</td></tr><tr><td>Information2: Info2-3</td><td>0.295</td><td>0.328</td><td>0.348</td><td>0.793</td></tr><tr><td>% cumulative variance explained</td><td>0.240</td><td>0.465</td><td>0.665</td><td>0.917</td></tr><tr><td>Level 3: Outcome</td><td colspan="2">Factor1</td><td colspan="2">Factor2</td></tr><tr><td>Stage 2 updated domain knowledge: Dk3-1</td><td colspan="2">0.927</td><td colspan="2">0.317</td></tr><tr><td>Stage 2 updated domain knowledge: Dk3-2</td><td colspan="2">0.927</td><td colspan="2">0.306</td></tr><tr><td>Stage 2 updated domain knowledge: Dk3-3</td><td colspan="2">0.931</td><td colspan="2">0.286</td></tr><tr><td>Self-reported requirement evaluation: Re1</td><td colspan="2">0.297</td><td colspan="2">0.914</td></tr><tr><td>Self-reported requirement evaluation: Re2</td><td colspan="2">0.311</td><td colspan="2">0.912</td></tr><tr><td>Self-reported requirement evaluation: Re3</td><td colspan="2">0.299</td><td colspan="2">0.907</td></tr><tr><td>Self-reported requirement evaluation: Re4</td><td colspan="2">0.287</td><td colspan="2">0.929</td></tr><tr><td>% cumulative variance explained</td><td colspan="2">0.420</td><td colspan="2">0.939</td></tr></table>

## Appendix I: Confirmatory Factor Analysis

Table I1. Factor Loadings in the Measurement Model (Stage 1: Questionnaire)

<table><tr><td>Construct</td><td>Items</td><td>Loading</td><td>t-value</td><td> $R^2$ </td></tr><tr><td rowspan="3">Prior domain knowledge at the start of Stage 1</td><td>Dk1-1</td><td>0.96</td><td>110.84</td><td>0.92</td></tr><tr><td>Dk1-2</td><td>0.95</td><td>71.86</td><td>0.90</td></tr><tr><td>Dk1-3</td><td>0.95</td><td>88.65</td><td>0.89</td></tr><tr><td rowspan="3">Reported use of the tool at Stage 1</td><td>Use1-1</td><td>0.99</td><td>96.93</td><td>0.98</td></tr><tr><td>Use1-2</td><td>0.98</td><td>94.08</td><td>0.96</td></tr><tr><td>Use1-3</td><td>0.90</td><td>38.57</td><td>0.81</td></tr><tr><td rowspan="3">Goal1 (GOAL1)(first-order factor for MM1)</td><td>Goal1-1</td><td>0.98</td><td>151.26</td><td>0.95</td></tr><tr><td>Goal1-2</td><td>0.99</td><td>203.75</td><td>0.97</td></tr><tr><td>Goal1-3</td><td>0.96</td><td>115.83</td><td>0.93</td></tr><tr><td rowspan="3">Process1 (PROC1)(first-order factor for MM1)</td><td>Proc1-1</td><td>0.97</td><td>179.53</td><td>0.95</td></tr><tr><td>Proc1-2</td><td>0.97</td><td>106.94</td><td>0.94</td></tr><tr><td>Proc1-3</td><td>0.90</td><td>22.55</td><td>0.82</td></tr><tr><td rowspan="3">Task1 (TASK1)(first-order factor for MM1)</td><td>Task1-1</td><td>0.96</td><td>106.56</td><td>0.93</td></tr><tr><td>Task1-2</td><td>0.98</td><td>253.28</td><td>0.97</td></tr><tr><td>Task1-3</td><td>0.98</td><td>195.55</td><td>0.96</td></tr><tr><td rowspan="3">Information1 (INFO1)(first-order factor for MM1)</td><td>Info1-1</td><td>0.95</td><td>94.39</td><td>0.90</td></tr><tr><td>Info1-2</td><td>0.98</td><td>131.33</td><td>0.95</td></tr><tr><td>Info1-3</td><td>0.98</td><td>192.89</td><td>0.96</td></tr><tr><td rowspan="4">Mental models (MM1)(second-order factor)</td><td>GOAL1</td><td>0.90</td><td>54.00</td><td>0.81</td></tr><tr><td>PROC1</td><td>0.95</td><td>73.50</td><td>0.90</td></tr><tr><td>TASK1</td><td>0.96</td><td>104.64</td><td>0.92</td></tr><tr><td>INFO1</td><td>0.94</td><td>78.69</td><td>0.88</td></tr><tr><td rowspan="3">Updated domain knowledge at the end of Stage 1</td><td>Dk2-1</td><td>0.97</td><td>166.68</td><td>0.93</td></tr><tr><td>Dk2-2</td><td>0.98</td><td>141.53</td><td>0.95</td></tr><tr><td>Dk2-3</td><td>0.98</td><td>225.44</td><td>0.96</td></tr><tr><td rowspan="3">Self-reported question evaluation</td><td>Qe1</td><td>0.94</td><td>81.41</td><td>0.89</td></tr><tr><td>Qe2</td><td>0.97</td><td>134.51</td><td>0.94</td></tr><tr><td>Qe3</td><td>0.97</td><td>173.52</td><td>0.95</td></tr></table>

Table I2. Factor Loadings in the Measurement Model (Stage 2: Requirements List)

<table><tr><td>Construct</td><td>Items</td><td>Loading</td><td>t-value</td><td> $R^2$ </td></tr><tr><td rowspan="3">Updated domain knowledge at the end of Stage 1</td><td>Dk2-1</td><td>0.96</td><td>80.95</td><td>0.93</td></tr><tr><td>Dk2-2</td><td>0.98</td><td>132.10</td><td>0.96</td></tr><tr><td>Dk2-3</td><td>0.98</td><td>174.20</td><td>0.96</td></tr><tr><td rowspan="3">Reported use of the tool at Stage 2</td><td>Use2-1</td><td>0.98</td><td>100.84</td><td>0.95</td></tr><tr><td>Use2-2</td><td>0.99</td><td>213.01</td><td>0.98</td></tr><tr><td>Use2-3</td><td>0.93</td><td>66.34</td><td>0.86</td></tr><tr><td rowspan="3">Goal2 (GOAL2)(first-order factor for MM2)</td><td>Goal2-1</td><td>0.97</td><td>138.41</td><td>0.94</td></tr><tr><td>Goal2-2</td><td>0.98</td><td>194.27</td><td>0.95</td></tr><tr><td>Goal2-3</td><td>0.97</td><td>182.11</td><td>0.95</td></tr><tr><td rowspan="3">Process2 (PROC2)(first-order factor for MM2)</td><td>Proc2-1</td><td>0.99</td><td>337.00</td><td>0.97</td></tr><tr><td>Proc2-2</td><td>0.98</td><td>354.09</td><td>0.97</td></tr><tr><td>Proc2-3</td><td>0.95</td><td>38.47</td><td>0.90</td></tr><tr><td rowspan="3">Task2 (TASK2)(first-order factor for MM2)</td><td>Task2-1</td><td>0.97</td><td>189.82</td><td>0.94</td></tr><tr><td>Task2-2</td><td>0.99</td><td>394.28</td><td>0.98</td></tr><tr><td>Task2-3</td><td>0.99</td><td>227.93</td><td>0.97</td></tr><tr><td rowspan="3">Information2 (INFO2)(first-order factor for MM2)</td><td>Info2-1</td><td>0.98</td><td>221.36</td><td>0.95</td></tr><tr><td>Info2-2</td><td>0.99</td><td>440.41</td><td>0.98</td></tr><tr><td>Info3</td><td>0.99</td><td>352.68</td><td>0.98</td></tr><tr><td rowspan="4">Mental models at Stage 2 (MM2)(second-order factor)</td><td>GOAL2</td><td>0.96</td><td>120.49</td><td>0.93</td></tr><tr><td>PROC2</td><td>0.98</td><td>186.66</td><td>0.96</td></tr><tr><td>TASK2</td><td>0.98</td><td>155.82</td><td>0.95</td></tr><tr><td>INFO2</td><td>0.96</td><td>120.37</td><td>0.92</td></tr><tr><td rowspan="3">Updated domain knowledgeAt the end of Stage 2</td><td>Dk3-1</td><td>0.99</td><td>427.41</td><td>0.98</td></tr><tr><td>Dk3-2</td><td>0.99</td><td>279.06</td><td>0.97</td></tr><tr><td>Dk3-3</td><td>0.98</td><td>193.42</td><td>0.96</td></tr><tr><td rowspan="3">Self-reported question evaluationat the end of Stage 1</td><td>Qe1</td><td>0.96</td><td>109.86</td><td>0.92</td></tr><tr><td>Qe2</td><td>0.97</td><td>157.91</td><td>0.94</td></tr><tr><td>Qe3</td><td>0.97</td><td>147.46</td><td>0.93</td></tr><tr><td rowspan="4">Self-reported requirement evaluation</td><td>Re1</td><td>0.98</td><td>330.75</td><td>0.97</td></tr><tr><td>Re2</td><td>0.99</td><td>322.10</td><td>0.97</td></tr><tr><td>Re3</td><td>0.98</td><td>277.22</td><td>0.97</td></tr><tr><td>Re4</td><td>0.99</td><td>468.97</td><td>0.98</td></tr></table>

## About the Authors

Padmal Vitharana is an associate professor of information systems in the Whitman School of Management at Syracuse University. He received his PhD from the University of Wisconsin – Milwaukee. His research expertise and interests lie in component/service-based development, systems analysis and design, and software quality management. His research has been published in leading journals such as the IEEE Transactions on Software Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Journal of MIS, Marketing Science, Communications of the ACM, Database for Advances in Information Systems, Communications of the AIS, Information Resource Management Journal, Empirical Software Engineering, and Information & Management. He has served as an associate editor of Communications of AIS in the past and currently serves as an associate editor of IEEE Transactions on Services Computing. He served as one of the guest editors for the Special Issue on Architecture & Design for Application Agility in the Information Technology and Management.

Fatemeh Mariam Zahedi is University of Wisconsin-Milwaukee Distinguished Professor and Church Mutual Insurance Faculty Scholar in ITM at the Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee. She has received her doctoral degree from Indiana University. Her research focus is on IT at the service of individuals. Her present areas of research include web-based systems design and issues including security, privacy, culture, trust, loyalty, personalized intelligent interface, web-based healthcare, and web analytics for health. She has served as SE and AE of MIS Quarterly, editorial board of JMIS, and AE of ISR. She has published more than 120 referred papers in premier journals and conferences, including MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Management Science, DSS, Information & Management, IEEE Transactions on Software Engineering, Operations Research, IEEE Transactions on Systems, Man, and Cybernetics, IIE Transactions, Review of Economics and Statistics, and others. She has been the PI of grants funded by NSF and other agencies. She is the author of two books: Quality Information Systems and Intelligent Systems for Business: Expert Systems with Neural Network. She has received several research, teaching and best paper awards.

Hemant Jain is W. Max Finely Chair in American Business: Data Analytics, in College of Business at University of Tennessee Chattanooga. Before this he was Professor of Information Technology Management at University of Wisconsin Milwaukee. His work has appeared in leading journals including Information Systems Research, MIS Quarterly, IEEE Transactions on Software Engineering, Journal of MIS, IEEE Transactions on Systems Man and Cybernetics, Naval Research Quarterly, Decision Sciences, Decision Support Systems, Communications of ACM, and Information & Management. He is on the advising board of IEEE Transactions on Services Computing. He served as Associate Editor-in-Chief of IEEE Transactions on Services Computing and as Associate Editor of Journal of AIS. Recently he served as Program Chair of IEEE International Conference on Big Data and is serving as Program Chair of IOT services conference. He served as Program co-chair of DESRIST 2011.

Copyright © 2016 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints or via e-mail from publications@aisnet.org.
