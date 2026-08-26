---
otero_id: 3586
otero_key: "PJ38RG8E"
title: "Decision support for team staffing: An automated relational recommendation approach"
authors: "Jochen Malinowski; Tim Weitzel; Tobias Keim"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.05.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Decision support for team staffing: An automated relational recommendation approach

Jochen Malinowski <sup>a,⁎</sup>, Tim Weitzel <sup>b</sup>, Tobias Keim <sup>a</sup>

<sup>a</sup> Institute for IS, Frankfurt University, Germany

<sup>b</sup> IS and Services, Bamberg University, Germany

Available online 13 May 2007

## Abstract

Selecting individuals for teams is only rarely supported by IS. Existing systems only consider whether a person has the required technical skills and abilities for a job. Another important aspect is neglected — the match between the person and the team members in terms of interpersonal compatibility. We present a decision support system based on a relational recommendation approach for providing an automated pre-selection of candidates that fit best with future team members. The relational recommender contributes to theory by proposing an IS-supported relational approach to team staffing and to practice by offering time and cost savings for HR professionals. © 2007 Elsevier B.V. All rights reserved.

Keywords: Decision support for personnel selection; Recommender system; Human resource management

## 1. Introduction

The selection of persons to configure teams is recognized by many authors as one of the most important aspects of team effectiveness, as the characteristics of the individuals together with their interrelations directly influence team performance [51,80]. In this context, researchers have discussed various factors that determine the fitness of a person with regard to a job and a team [14,29,42,80]. However, there is little research evaluating how existing human resource (HR) information systems need to be extended to support HR decision makers in this task [51,75].

West and Allen [82] note that the prediction of a person's fit with a job is already a very complex process.

Further complexities arise when considering the fitness between an individual and other team members [30]. That is why information systems (IS) have only rarely been used to support this aspect of the selection process. Existing approaches usually consider only unary attributes that are tied directly to an individual (e.g. educational data) and – based on them – assess the aptitude of a candidate in relation to the job requirements [2]. Such approaches are based mainly on standard database queries that do not appropriately tackle the complexity of the task as they focus solely on the fitness of the person with the job, neglecting the fitness of the person with the team — which is at least equally important [82]. This is understandable in the context of external recruitment, as in this case usually no relational data is available. However, in an internal team staffing scenario, such data can be retrieved from, for example, past performance evaluations or project history information. But these data are not yet leveraged in existing

Human Resource Information Systems (HRIS) [51]. We argue, therefore, that a decision support system for the selection of individuals for teams also needs to consider relational attributes, such as interpersonal trust, to determine the fitness between the candidate and existing team members.

Theoretical considerations reveal an analogy between the personnel selection problem and tasks in the information retrieval field. Information retrieval techniques deal with the problem of information overload as they try to find the ‘right’ information [9]. For this, recommender systems, used especially in E-commerce applications to assist customers in finding the products or services that match with their individual preferences, have recently received broad attention [61,66]. However, such recommender systems have only been used to recommend objects such as books or CDs based on similarities between the items or the respective users. They have not been used extensively in another potential field of application: the recommendation of subjects. We argue that some of the concepts of recommender systems can be used to recommend candidates to teams. In this paper, we address the following research questions:

1. How can the selection of individuals for teams be supported by IS?

2. Can recommender systems, originally used to recommend objects to users, also be used to recommend subjects?

3. Can the selection quality be improved by incorporating relational aspects such as trust, and how can this be supported by IS?

The relevance of these research questions is shown in recent organizational trends. Many corporations face fast-changing organizational structures, flexible working styles, and the increasing importance of project– and teambased work structures [2,49,81]. Notably, the use of teams as work design has spread through all kinds of organizations in all types of industries [7,51,73,75,82]—

a trend facilitated by the ongoing globalization of companies and huge improvements in information and communication technologies (ICT) [13]. Based on the findings that work in changing projects and organizational settings gains importance, Malone and Laubacher developed their vision of an “e-lance economy” [48], leading to the challenge of matching individuals to new colleagues more frequently and ensuring that the candidates selected not only fit with job requirements but also with team members in terms of interpersonal compatibility or goal-congruence [30]. Companies that focus on project-based work, such as consulting or ITservice businesses, have already established this kind of team-based work structure as the standard way of working. In such companies, employees are frequently staffed to project teams and dispersed as soon as the project ends. The literature confirms that this trend is likely to spread to other companies, and many authors expect an even more prominent role for team-based work structures in the future [21,51]. Hence, the effectiveness of work teams becomes crucial for company success [73].

We conclude that team staffing is gaining importance and that individuals are more frequently staffed with new colleagues. To process the associated volumes of candidate profiles efficiently and find the person tha fits best with the job and the team, firms seek adapted IS support for the selection stage [45]. Motivated by this, we assume that an automated relational recommendation approach has important implications. First, it contributes to the information systems literature by developing a novel method for the selection of individuals for teams. We also provide an instantiation of this method by developing a prototype that can be considered an expertise recommender according to [31]. Second, from a practitioner's perspective, the approach can help HR professionals in pre-selecting candidates that fit best not only to the job but also to the team, especially as compared to the common keyword-based search and filter techniques that focus solely on a candidate's technical skill set. At the same time, this can increase the productivity of HR managers, implying time and cost savings as it eliminates the need to screen all employee profiles manually. In this context, it could be shown that the use of information system technology in other areas of personnel attraction and selection has already led to those time and cost savings. Empirical research with the Top 1000 companies in Germany showed that using information systems in personnel marketing can result in cost savings of more than 30% and reduced process times of averaged 26% for those companies that could achieve reductions [37]. The need for IS-supported selection was also confirmed by our case studies conducted with several HR professionals from large German companies [44].

In the next section, we present theoretical findings from personnel selection research and identify drawbacks of current systems to derive requirements for an IS-supported team staffing approach. Based on this, in Section 3 we develop a novel relational recommendation model aimed at supporting team staffing by considering relational aspects. The model and its applicability are validated in Section 4 using empirical data gained from a student experiment. The paper closes with a discussion of the implications for theory and practice, gives concrete answers to the research questions and identifies areas for future research.

## 2. Selecting individuals for teams — A review of the literature

From the motivations that (1) staffing individuals for teams gains importance due to organizational trends and (2) decision support systems for the matching of individuals to teams are rather scarce and normally do not consider the complexity of the task, we develop a system to recommend people based on their predicted fit with their immediate team members, extending existing approaches by also considering relational aspects. In the following, we derive requirements for such a recommendation approach based on findings from the human resource management, personnel selection, and personnel psychology literature.

## 2.1. A fit perspective on personnel selection

The literature usually refers to the challenges of finding a good match between person and job and between person and team as task-related and social aspects [32], human and social capital [6,69], or person– job (P-J) and person–team (P-T) fit [68]. The latter two constructs belong to the overarching concept of person– environment (P-E) fit, which – in addition to P-J and P-T fit – also consists of person–organization (P-O) and person–vocation or occupation (P-V) fit [42,68]. Here, we focus on the fit concept and use findings from related literature to derive requirements for an IS-supported personnel selection approach.

Various research fields, including vocational psychology, recruitment and selection research and management research, have dealt with the P-E fit framework [14,42,72,74]. The concept of P-E fit is one form of person–environmental psychology (PEP) that is based on the interactionist theory of behavior [55]. This theory, in turn, is grounded on research done by Lewin [43], who argued that behavior is a function of the person and the environment that surrounds that same person [68]. It is not the person or the environment alone that determines the variance in behavioral and attitudinal variables, but the interaction between their characteristics. Thus, P-E fit defines the degree of congruence between the characteristics of an individual and the characteristics of the environment in which the individual has to act [72]. In general, it is assumed that a high level of fit leads to positive outcomes for the individual (e.g., satisfaction and performance) as well as for the team and finally for the organization as a whole [14,42,73,74]. We distinguish between three different perspectives of how P-E fit can be conceptualized [42,44,72].

1) Supplementary versus complementary fit: Supplementary fit is found when an individual “supplements, embellishes, or possesses characteristics which are similar to other individuals” in an environment [55]. Supplementary fit is high if an individual has characteristics (e.g., values, tastes, and interests) similar to other members of the environment and, therefore, represents a person–person fit. In contrast, complementary fit is high if a person's characteristics supplement the environment or add what wasn't there before [55]. The need of the environment is offset by the individual's abilities and vice versa. It is noteworthy that both fit concepts use slightly different definitions of environment, though [72].

2) Needs–supplies versus demands–abilities fit: Needs– supplies describes the fit between an individual's needs, desires, or preferences and the respective environmental supplies. In contrast, the demands–abilities perspective is concerned with the fit between environmental demands and individual abilities [14,42]. Thereby, these two distinctions extend the conceptualization of complementary fit [42].

3) Perceived (subjective) versus actual (objective) fit: Perceived fit is based on human judgment of whether a fit exists. It is usually evaluated by directly asking individuals to what extent they perceive a fit [42]. The actual fit, in contrast, results from explicitly comparing individual and environmental characteristics, mostly using indirect measures like interactions, difference scores, or polynomial regressions [14].

The three perspectives are widely used in the literature. More recently, there have also been suggestions aimed at incorporating the three perspectives into one integrated fit approach [42]. Fig. 1 shows the relation between the different perspectives.

We argue that an IS-supported approach for selecting individuals for teams needs to consider two dimensions: (1) the match between the individual and the job (person– job fit) and (2) the match between the individual and the future team members (person–team fit) [80]. We assume that P-O and P-V fit have already been assessed when the employee was initially hired. Thus, we restrict ourselves to P-J and P-T fit, as the focus of this paper is on a company-internal team staffing scenario. These two concepts are briefly described below.

![](/api/attachments/PJ38RG8E/fulltext/images/e72f123ab3aed2a5f81bf69000a14ae24554f083f7f5dbf01c86b152fdd0e3c3.jpg)  
Fig. 1. Relationship among different conceptualizations of P-E fit [72].

## 2.1.1. Person–job fit

Edwards [14] defines P-J fit to consist of two classes of corresponding person and job constructs: the fit between an employee's desires and job supplies and the fit between job demands and an employee's abilities; [87] provide an example in a law enforcement context where a police sergeant needs to assign suitable detectives to a case and has, among others, to consider the assignee's perspective on the task and possibly recommend another person “when the potential assignee is reluctant to take on the case”. This is equivalent to the above-described conceptualization of the person–environment framework, in which the needs–supplies fit and the demands–abilities fit perspectives are distinguished. P-J fit has been the traditional approach in the recruitment and selection literature for matching individuals and jobs [2]. Through an extensive review of the industrial and organizational psychology and organizational behavior literature, Edwards found a person's desire to consist of psychological needs, goals, values, interests, and preferences [8,17]. Even though one can identify differences between those aspects, Edwards notes that they all refer to the attractiveness of the job in the eyes of the person. Job supplies consist of general occupational characteristics [29], specific organizational attributes, and job attributes such as pay, participation in decision-making, and characteristics comprising enriched jobs [14].

Focusing on the aspects that influence the fit between the demands of a job and the abilities of an individual, Edwards found abilities being typically described as employee aptitudes or aptitude proxies such as experience, education, or knowledge, skills, and abilities (KSAs) [17]. Job demands are typically discussed in the literature in terms of workload, requirements for job performance, and activities instrumental to the receipt of valued outcomes [14].

## 2.1.2. Person–team fit

As teamwork requires interaction among the team members and not just co-action [21,80], person–team fit in addition to person–job fit needs to be considered when composing teams [11,44,76]. Following the general P-E fit conceptualization, authors usually stress the separation between supplementary and complementary types of fit [76]. Some authors argue that a good fit occurs if team members have supplementary attitudes and preferences [55]. This means that a candidate should share similar characteristics with the existing team members in terms of beliefs, values, and group norms [57]. Various authors state that supplementary fit can lead to higher group cohesiveness and faster decision processes [15,80]. Other authors argue instead that too much compatibility leads to a loss of creativity and group thinking, thus promoting complementary fit [77]. This means that a candidate should have distinctive characteristics that complement and support the characteristics of the existing team members. In general, diverse skills are supposed to increase the possibility for innovation and creativity and to compensate for the deficiencies of one team member with the strength of others [77,79].

Werbel and Johnson [80] conclude that both supplementary and complementary fit need to be considered when selecting individuals for teams. Through a review of the literature, the authors found that homogeneity of goals, values, and sometimes personality has been found by most researchers to be positively correlated with performance, whereas heterogeneity might be desired for knowledge, skills, and abilities [40,42]. Werbel and Johnson, therefore, stress that the presence of one fit perspective without the other may lead to dysfunctional teams. They incorporate into their model of person– team fit both perspectives and show how person–team fit can influence individual and group members' performance. The authors conclude that a high level of supplementary and complementary fit has an impact on the quality of interpersonal interaction and thus affects the performance of the entire team [80]. It is important to stress that a high level of complementary P-T fit requires both a fit between the individual's needs and the team's supplies and the individual's abilities and the team's demands.

After initially identifying the requirements for the defined role within the team, employees can be chosen based on their individual abilities [40]. However, focusing only on the individual's abilities is insufficient for measuring and predicting team effectiveness. As discussed above, P-T fit also requires more broad-based teamworking skills. The individual needs to be able to work together effectively with the immediate workgroup comprising coworkers and supervisors. Researchers frequently note that team effectiveness depends strongly on interpersonal relations existing among team members. While in traditional individual-based work environments the interpersonal demands of employees are much less relevant, interaction among the members has a much greater performance impact in a team-based setting [71]. Team members need to collaborate effectively, communicate with each other, and solve problems and conflicts together — all of which stress the importance of interaction processes [22].

By reviewing literature in the area of group behavior and group performance, Stevens and Campion [75] determined the knowledge, skills, and abilities (KSAs) required for effective teamwork, such as conflict resolution, collaborative problem solving, and communication. Those general teamworking capabilities all require a high level of interpersonal cooperation.

## 2.2. Drawbacks of current IS-supported approaches

As employers increasingly attract large numbers of candidates over the internet, they also generate more and more applications in a digital and even more structured format. These applications then are stored in an internal database that serves as the cornerstone of many socalled applicant management systems [37]. The importance of such internal candidate databases or skill marketplaces for the internal staffing of teams within businesses such as consultancies was also shown by selected case studies conducted by ourselves in the relevant field [44]. Existing HRIS mainly use such internal candidate databases to pre-select candidates based on standard database queries. Such queries define concrete skill demands for a specific job profile to identify those individuals that meet the criteria. The required common skill ‘language’ allows for executing a skill matching algorithm to calculate the fit between person and job [14]. Numerous Human Resource information systems, such as SP-Expert from Astrum or SAP R/3 Human Resources, apply this kind of skill searching and matching. More innovative approaches are discussed in the literature. Bhargava, for example, provides an approach to support the allocation of people to jobs by developing a recruit distribution model to assign new Marine Corps recruits to entry-level schools [4]. However, the actual assessment of the fit between new recruits and available schools is still based on standard fit calculation procedures and subsequent keyword-based search queries.

We formulate three major drawbacks of existing ISsupported approaches for the selection of individuals for teams (see also Ref. [44]). A first drawback of the existing systems is that simple keyword-based search and filter techniques are insufficient to capture the complexity of the selection process, for several reasons [9]. First, not all aspects of the person and the job can be captured in a common skill language [42]. Muchinsky and Monahan [55] note that “the language of individual and environmental assessment is often different, which further retards our attempts to achieve congruence”. Also, selection decisions often depend on underlying attributes such as personal characteristics or social skills [32] that cannot be easily operationalized. In their study of human resource staffing decisions, Judge and Ferris [35] asked HR professionals for the criteria they use when assessing the aptitude of a candidate for a job. Nearly all respondents articulated that they are looking for candidates that ‘fit’. However, the respondents were hard pressed to define ‘fit’ more precisely. The authors quote one HR professional, who said: “I can't articulate it, but I'll know when I see it.” This statement underlines the existing difficulties of clearly specifying the criteria used in selection decisions. Färber et al. [16] recently presented a more innovative approach to this problem. The authors developed an automated recommender system able to model the latent aspects that underlie selection decisions. The system is trained with CV data of applicants and recruiters' past rating decisions. Based on these training data, the system then is able to predict the aptitude of candidates for a specific job. Other authors propose using neural networks for this purpose [83].

A second drawback of existing IS-supported solutions is that they usually focus only on the demands– abilities fit perspective of P-J fit, and do not consider the preferences of the candidates (needs–supplies fit). With regard to this, a probabilistic approach that recommends jobs to candidates based on past job preference ratings was recently presented [44,47].

While the literature discusses these two drawbacks and offers some more innovative approaches compared to standard-database queries, none of those approaches address the third drawback. Despite the importance of person–team fit for the selection of individuals for teams, this aspect is usually not considered in existing approaches. Motivated by this, we present requirements for an IS-supported team staffing approach below that aims to fill this gap.

## 2.3. Requirements for an IS-supported team staffing approach

Based on the two described types of fit, we conclude that a decision support system for team staffing needs to account for two dimensions and therefore consider

1. unary attributes like individual skills, mental abilities, and personality that determine the fit between an individual and tasks to be accomplished and

2. relational attributes that determine the fit between an individual and future team members.

In both cases, the needs of the candidate must fit the supplies of the job or the team (needs–supplies fit perspective) and the candidate's abilities must fit the demands of the job or the team (demands–abilities fit perspective). Based on this theoretical foundation, we derive the following three major functional requirements when recommending candidates to form effective teams (see also Ref. [44]):

1. Since recommending a person is a multilateral process, not only the preferences of a single person (e.g., the HR professional or the recruiter) but of several persons (e.g., the candidate and existing team members) need to be considered.

2. Hence, recommendations cannot be solely based on the attributes tied to an individual person but need to consider relational aspects determining the fit between the person and other team members as well.

3. As individuals are unique and cannot be multiplied and selected several times for different teams at the same time, “content aspects” ensuring that only available candidates are selected need to be considered ([44]).

Existing approaches only consider the person–job fit. Next, we present a novel recommendation approach aimed at supporting the selection of individuals for teams by considering trust as an influencing factor for a high level of person–team fit.

## 3. A relational recommendation approach

Thus far, we have shown that existing information systems supporting personnel selection processes neglect relational aspects that are important for predicting the level of person–team fit. There is a consensus in the literature that interpersonal cooperation and communication are important aspects for the effectiveness of teamwork [33]. Section 2.1.2 showed that essential team working skills include conflict resolution, collaborative problem solving and communication which all require a high level of interpersonal cooperation. MacAllister [50] and Jones and George [33] argue that a high level of interpersonal cooperation requires, in turn, a high level of trust among the team members. Thereby, trust is an important indicator of P-T fit. As it appears to be part of human nature that individuals exhibit higher commitment and involvement if they trust each other, Korsgaard, Brodt, and Sapienza [41] conclude that trust is a vital precondition for teams to cooperate successfully.

In general, trust controls the way people interact with each other and is a central component of effective working relationships [52] that is often discussed in the context of B2B [58] and B2C electronic business relationships [39]. By focusing on trust as a social attribute describing the relation between two individuals, we build on concepts from social network analysis (SNA). SNA is a rather young discipline that provides various measures to describe and analyze network structures. Among others, SNA measures are used to examine interactions, connectedness and information sharing in networks [70].

For personnel selection, Granovetter [19] shows that social networks play an important role when searching for new jobs. Existing employees usually know best who fits with a company and who does not. Complementing these relational aspects, research on search and filter techniques to, for instance, recommend social contacts previously unknown is quite scarce. Some social networking platforms such as LinkedIn (www.linkedin.com) or OpenBC/Xing (www.openbc.com) allow for modeling relations between participants on those platforms. However, they do not allow specifying type (e.g., private, commercial) or intensity of a relationship. Furthermore, one can only browse through existing networks or search for new partners using simple keyword-based searches. The systems rarely use the existing individual and relational data to recommend new social contacts. A possible reason is a problem inherent in social match making; the preferences of both partners need to be considered as has been elaborated earlier in the two perspectives of fit, i.e. demands–abilities and needs–supplies. In this paper, we address these drawbacks as we propose a trust computational model aimed at predicting trust relations between previously unknown individuals. We thus consider the social capital of candidates in addition to their human capital [6,69].

![](/api/attachments/PJ38RG8E/fulltext/images/9e09fe04399c1f6b199adb44018ed7b9bd14c9d011988f45d41a9f689346582c.jpg)  
Fig. 2. Collaborative trust prediction [46].

## 3.1. A trust computational model

In keeping with the literature and despite acknowledging the multifaceted nature of the construct, we assume that trust can be expressed as a singular value [1,62,86]. Social scientists usually distinguish between three different types of trust: interpersonal trust, impersonal trust, and dispositional trust [52,58]. For our purpose, interpersonal trust defined as context-specific (here: work environment) trust one agent directly has to another is relevant. As this type of trust is a subjective impression that differs from person to person, all members build their own personal ‘web of trust’ [20,38,62,86]. This is important, as we need to calculate trust values between the candidate and all team members and vice versa. We cannot assume that person A trusts person B just because this is true the other way around.

Before presenting the model in more detail, we define the key terms. Let $t _ { A B }$ be the trust user A holds for user B [1], with values of $\dot { t } _ { A B }$ between 0 and 1 and $t _ { A B } { = } 0$ indicating that user A distrusts user $B ,$ whereas 1 indicates that B is fully trustworthy (in the eyes of A). The notation $t _ { A C } ^ { \prime } { = } t _ { A { \mathrm { - } } { > } B { \mathrm { - } } { > } C }$ indicates that A trusts C using a path via $B ,$ which is usually referred to as trust path. See Ref. [34] for a similar trust transitivity principle and the difference between trust and reputation and [44] for further elaborations on the trust computational model.

In the following we want to discuss three scenarios (see also Refs. [24,46,44]) where a previously unknown trust relation (depicted by a dotted line) is predicted based on existing trust relations (Figs. 2 and 3) or based on attribute similarities (Fig. 4). The discussion is based on the three requirements for an IS-supported team staffing approach as defined in Section 2.3 and on related findings in the literature [20,85].

Figs. 2 and 3 address the first two requirements, requesting that recommending people must be a multilateral process (the graphs are direct graphs, stressing the proposition that trust is a subjective impression) and that relational aspects – in this case trust – need to be considered (the relations in the figures are valued, with the value being defined as the trust the source of the relation assigns to the receiver).

Fig. 4 stresses our aim to incorporate content elements into the recommendation process. A candidate who has already been selected for a team cannot be selected again for another team, as every individual is unique. Based on existing similarities between user attributes (the content), it must be possible to predict trust relations even if no direct or indirect trust relations among those users exist.

As already mentioned, we believe that from a theoretical perspective it is promising to incorporate concepts of automated recommender systems adapted to the context of personnel selection. While these systems usually recommend objects like books or movies [10], we propose to adapt the systems to recommend subjects. The underlying idea is that recommender systems could use existing unary and relational data to predict user preferences and previously unknown relations. This information could then be used to recommend individuals for teams. In the next section, we use a brief introduction to recommender systems to show how these concepts can be applied to the three scenarios aimed at supporting the selection of individuals for teams

![](/api/attachments/PJ38RG8E/fulltext/images/e6a0816e75d757721aeff5482c7971d0665830c75a5c60576a83121a6a4c3b4d.jpg)  
Fig. 3. Direct trust propagation [46].

![](/api/attachments/PJ38RG8E/fulltext/images/02df88047fb6595194f3d89bdd56076347ce03a2415d8f5bfe1c38bb3577f0ad.jpg)  
Fig. 4. Similarity-based trust prediction [24].

## 3.2. Incorporating recommender systems into the relational modelling approach

The two most prominent filter techniques used for recommender systems are content-based and collaborative filtering [10]. Content-based filtering models use information about objects the user has already rated to recommend similar objects [3,61]. Collaborative filtering methods, on the other hand, try to identify users that have a taste similar to the taste of the actual user to recommend objects to the actual user that those similar users preferred. In general, two types of collaborative filtering techniques can be distinguished: memory-based and model-based methods [5]. The main difference between these types is that memory-based methods take the entire rating data as the basis to generate recommendations, whereas model-based methods try to predict some parameters in advance (i.e., to train the model) before beginning the recommendation generation process [66].

The literature includes an intensive discussion of the disadvantages of pure content-based and pure collaborativebased filtering. Pure content-based filtering techniques can be used only if features (such as categories, author names, title, etc.) can be extracted from the objects easily and they do not produce good recommendations if these features are very diverse. In addition, only those items are recommended that consist of the same features as items previously rated positively by users. This can lead to overspecialization, as no diverse items can be recommended [3]. Pure collaborative-based filtering techniques suffer from the sparsity of the original rating matrix, as the overlap of rated objects usually is very small. It also suffers from what is usually referred to as cold-start problem, i.e., recommendations for new items cannot be made if no rating data from the past is available [67]. To address these issues, hybrid models have been developed that combine content-based and collaborative filtering techniques [18,53,66].

Färber et al. [16] apply a probabilistic latent aspect (PLSA) model to recommend persons to jobs in an external recruitment scenario. The PLSA model is based on a probabilistic approach that originally belongs to the class of model-based collaborative filtering techniques. A good introduction to the base PLSA model can be found in Hofmann [27] and Hofmann and Puzicha [28]. In this probabilistic model, the preferences of users are seen as a convex combination of underlying latent aspects [28]. The different aspects that underlie a rating decision can be modelled, which led to very good recommendation results [27,53]. Applied to the recommendation of persons and their match with job requirements, this approach allows the modelling of latent aspects that underlie personnel selection decisions. In their approach, Färber et al. [16] focus solely on the demands–abilities fit perspective by predicting the aptitude of candidates based on the congruence between the candidates' abilities and job requirements.

In the following, we discuss how these recommender system concepts can be applied to the three defined trust propagation and prediction scenarios. We focus on each scenario separately before describing how to combine the scenarios into an integrated relational recommendation approach.

## 3.3. Collaborative trust prediction

Given nodes A and C are consumers, B and D objects (e.g., books), and the relations are product ratings of the consumers, Fig. 2 would show a typical collaborative filtering situation [44]. Based on rating similarities between consumer A and C (as they both have rated D), a collaborative filtering system would find those users similar to each other, leading to a recommendation of object B to consumer C [3,26,27,53]. As discussed above, it sounds appealing to utilize automated recommender systems to recommend subjects for this purpose. Based on the three given trust relations and assuming that $t _ { A D } \approx t _ { C D } ,$ , the model would conclude that candidate A and C have similar preferences — as they both trust D with similar values. This information can then be used to predict the missing relation between C and B. As precondition for such a calculation, we need to have explicit trust ratings defined (in the small example, this would be $t _ { A B } , t _ { A D } \mathrm { a n d } t _ { C D } )$ . We define explicit trust ratings as those that have been explicitly stated by, for example, conducting a survey regarding interpersonal relationships among team members. In this paper, we do not focus on how to conduct such a survey, but instead assume that the ratings have already been assessed. For insights into how to assess and analyze interpersonal trust, we refer the reader to [63] or [64]. To model these trust relations, we adapt a PLSA model to the context of relational recommendation. This approach allows us to capture the latent aspects that underlie a rating decision $[ 1 6 , 4 7 ]$ . It can be visualized graphically as shown in Fig. 5. In this model, we consider the trust ratings of the team members for the candidates with $y \in Y { = } \{ y _ { 1 } , . . . , y _ { n } \}$ and $x \in X = \{ x _ { 1 } , . . . , x _ { m } \}$ , where Y is a set of existing team members and X is a set of candidates. The latent aspects (the underlying aspects upon which we assume the trust rating to be based) are considered in the model using the latent variable $z { \in } Z { = } \left\{ z _ { 1 } , . . . , z _ { k } \right\}$ . The probability model can then be formulated as $P ( x , y , \nu ) { = } P ( y ) { \cdot } P ( z | y ) { \cdot } P ( \nu | z , x )$

The model parameters are estimated using the Expectation Maximization (EM) algorithm [12], which is the standard algorithm for maximum likelihood estimation in latent variable models. The algorithm alternates two steps: The first is an expectation step in which posterior variables for the latent variable z are computed. The second is a maximization step in which parameters are updated for given posterior probabilities that were computed in the Expectation step:

$$
\begin{array}{l} \text {E - step:} P (z | x, y, v) = \frac {P (z) \cdot P (y | z) \cdot P (v | x , z)}{\sum_ {z ^ {\prime} \in Z} P (z ^ {\prime}) \cdot P (y | z ^ {\prime}) \cdot P (v | y , z ^ {\prime})} \\ \text {M - steps:} P (v | x, z) = \frac {\sum_ {y \in Y} r _ {x , y , v} ^ {\prime} \cdot P (z | x , y , v)}{\sum_ {v ^ {\prime} \in V , y \in Y} r _ {x , y , v ,} ^ {\prime} \cdot P (z | x , y , v ^ {\prime})} \quad P (y | z) = \frac {\sum_ {x \in X , v \in V} r _ {x , y , v} ^ {\prime} \cdot P (z | x , y , v)}{\sum_ {y ^ {\prime} \in Y , x \in X , v \in V} r _ {y ^ {\prime} , x , v} ^ {\prime} \cdot P (z | x , y ^ {\prime} , v)} \\ P (z) = \frac {\sum_ {x \in X , y \in Y , v \in V} r _ {x , y , v} ^ {\prime} \cdot P (z | x , y , v)}{\sum_ {z ^ {\prime} \in Z , x \in X , y \in Y , v \in V} r _ {x , y , v} ^ {\prime} \cdot P (z ^ {\prime} | x , y , v)} \end{array}
$$

The rating $r _ { x , y , \nu } ^ { \prime }$ is the trust that person y assigns to candidate x with value $\mathrm { v } { = \{ \mathrm { ^ { 6 4 } f u l l ~ t r u s t ^ { 3 9 } = 1 | \mathrm { ^ { 6 } f u l l } } } \Omega $ distrust” = 0}. The algorithm is initialized with randomly chosen variable values. The current estimates of the parameters are used iteratively in the E-Step to compute the posterior probabilities for the latent variable z. The parameters are then updated in the three M-Steps for the given posterior parameters. The iterations run until a local maximum of the log likelihood is reached (Further information how to use the EM algorithm for PLSA models can be found in [27,60]). Using the algorithm, we can finally calculate $\begin{array} { r } { P ( \nu | x , y ) { = } \sum _ { z } P ( \nu | x , z ) \cdot P ( z | y ) } \end{array}$ , which is the likelihood that person y rates candidate x with rating value v. The results can be written to a $m \times n$ rating matrix $E T ^ { \prime } { = } t _ { x y , \nu } ^ { \prime }$ containing all the predicted trust ratings that could be calculated with the described automated recommendation approach (see also Ref. [44]).

![](/api/attachments/PJ38RG8E/fulltext/images/d08592743bc56ed2c723a3c608e25af1fb777c156e69de10400331bbe680177c.jpg)  
Fig. 5. The probabilistic relational recommender [44]

![](/api/attachments/PJ38RG8E/fulltext/images/490581c9e8ae99b4b9b69bd007815e96e068a1466cef38dbb947a10b1f8026ef.jpg)  
Fig. 6. The probabilistic job recommender [47].

## 3.4. Direct trust propagation

Fig. 3 shows a scenario that is similar to what Guha et al. discuss under the term “direct propagation” since the trust propagates directly along an edge [20]. Applied to our example and assuming that candidate A trusts B with value $t _ { A B }$ and B trusts C with value $t _ { B C } ,$ this means that the direct propagation model infers that A trusts C as well [62,85]. To then calculate the trust path $t _ { A C } ^ { \prime } { = } t _ { A - > B - > C } ,$ multiplication is the preferred way [20,36,62], leading to the simple equation: $t _ { A C } ^ { \prime } { = } t _ { A B } \cdot t _ { B C } .$

It should be noted that the underlying assumption of this trust propagation calculation is that trust is transitive [44]. The literature sometimes refers to this as state of balance. It is argued that if there is a positive trust relation between two persons A and B as well as B and C, but a negative relation between A and C, this likely leads to a strain in the relation between A and B and the graph becomes ‘unbalanced’ [70]. Balance theory now suggests that individuals would find such an unbalanced network structure uncomfortable and would therefore try to restore a balance through resolving the tension they experience. This could be achieved by adjusting the assigned trust values [70].

## 3.5. Similarity-based trust prediction

We define trust values that are based on similarities between individuals as similarity-based trust. Research finds a positive correlation between user similarity and established trust [1,54]. Jones and George [33] note that people tend to trust others more if they share the same values and attitudes. Ziegler and Lausen [88], using data from an online bookreading community, conclude that the more similar two users are, the greater their established trust. Thus, by calculating existing similarities we can predict trust values between individuals [44].

When using recommender systems to recommend objects, similarities between users are typically calculated based on preference similarities. Those are usually derived from previous ratings for the objects in question. The common techniques used for this purpose are Pearson correlation, cosine vector similarity, or Spearman correlation methods [5,25]. As we use a recommender systems approach for recommending subjects we follow a model recently presented, where an adapted probabilistic latent aspect model is used to recommend jobs to candidates based on previous job preference ratings [47]. We utilize this model to calculate similarities among employees based on those previously stated job preferences (see also Ref. [44]). The probabilistic job recommender follows the same basic principle as the probabilistic relational recommender discussed in the previous section. In this case, the candidates and the job profiles are modeled with $y \in Y { = } \{ y _ { 1 } , . . . , y _ { n } \}$ and $x \in X = \{ x _ { 1 } , . . . , x _ { m } \}$ , with Y being the set of candidates and X the set of job profiles (for details about this model, the reader is referred to [47]) (Fig. 6).

To calculate user similarities we build segments of candidates with similar preference structures based on the latent aspects retrieved from previously rated job profiles [27]. This is similar to the approach followed by Xin et al. [84]. The authors use information about visited pages to build segments of similar web users.

As we use latent aspects for deriving user similarities, it should be noted that one user can belong to several segments. This is different to clustering techniques where each user belongs to exactly one class of persons [27,28,44]. The similarity between two users is calculated as follows:

$$
\operatorname{sim} _ {A B} = \left\{ \begin{array}{l l} \frac {1}{n _ {z}} \sum_ {z \in Z} | P (A | z) - P (B | z) | & \text { if } n (I _ {A} \cap I _ {B}) \neq 0 \\ 0 & \text { otherwise } \end{array} \right.
$$

where $P ( A | z )$ is the ‘proximity’ of person A to latent aspect $z , n _ { z }$ is the number of z variables and $n ( I _ { A } \cap I _ { B } )$ is the number of co-rated job profiles between candidate A and B.

Put simply, we start by calculating the difference of the probabilities that two users belong to the same segment constituted by a latent variable z. The differences are summed up for all latent aspects and divided through the number of segments. In case we have no co-rated job profiles between two users, the similarity value is 0. This is due to the fact that the EM algorithm would not generate valuable results because it starts with random values that cannot be correctly adjusted if no co-rated job profiles are found [28,44]. Based on the assumption that a positive correlation between user similarity and trust exists, we finally get $t _ { A B } ^ { \prime } { = } \sin _ { A B }$

In our case the number of co-rated job profiles is an indicator for the accuracy of the predicted trust value. Thus, we use it as a weight factor to calculate the similarity-based trust. This should be illustrated by the following example. Assuming there exist three individual profiles A, B and C that have no explicit trust ratings assigned to each other. However, A and B as well as B and C have a common preference structure in relation to their co-rated job profiles. These similarities in the preference structures are used to calculate similarity-based trust values as described above. This allows us to estimate a trust relation between A and C that is so far unknown, as follows [59]:

$$
t _ {A C} ^ {\prime} = t _ {A \rightarrow B \rightarrow C} = \frac {n (I _ {A} \cap I _ {B})}{n (I _ {A} \cap I _ {B}) + n (I _ {B} \cap I _ {C})} t _ {A B} + \frac {n (I _ {B} \cap I _ {C})}{n (I _ {A} \cap I _ {B}) + n (I _ {B} \cap I _ {C})} t _ {B C}
$$

In other words, to compute the inferred trust $t _ { A C } ^ { \prime } ,$ trust $t _ { A B } ,$ , and $t _ { B C }$ are totaled. As weight the number of co-rated job profiles of each direct association is used. Thus, the calculated trust value is changing dynamically depending on the number of co-rated job-profiles. This has also been discussed by Abdul-Rahman and Hailes [1], who argue that additional evidence “… may increase or decrease our degree of trust in another agent.”

Applied to the previously introduced scenario that is depicted in Fig. 4, this means that – based on the existing individual profiles A, B, C, and D together with the existing trust relation $t _ { A B } - \mathrm { w e }$ can calculate similarities between user profile pairs $( d ( x , y ) )$ . With this information it is possible to predict a trust rating for the unknown relation $t _ { C D } ^ { \prime }$

## 3.6. Trust path aggregation

In reality, the scenarios described above will occur concurrently and in a combined way [44]. Therefore, more than one trust path might exist between individuals and the individual trust values need to be aggregated. Richardson et al. [62] distinguish three different types of aggregation: maximum value (i.e. taking the path with the highest trust and neglecting all other paths), minimum value (i.e. taking only the trust path with the lowest trust value) and average (i.e. calculating an average using the trust values of all available paths) [20,36].

We apply the latter approach in our model whereas we utilize the user's confidence in the trustworthiness of the various paths as weight [59]. Confidence is defined as reliability the user assigns to the association. Hence, even if the calculated trust value $t _ { A B }$ is equal to $t _ { B A }$ (which is the case when processing similarity-based trust values, as they are calculated using preference similarities), each user might have a different confidence in the relationship. This reinforces the idea of a subjective impression of trust [1]. It sounds reasonable that a candidate's predicted trust in another candidate is more reliable if the number of co-rated job profiles is high. We, therefore, assume the degree of confidence to rise if the number of co-rated job profiles increases. The most confident association, i.e., the one with the most corated job profiles, is therefore initialized with 1. All other direct associations are set in relation to this maximum value.

This leads to the formulation [59]: $\begin{array} { r } { C _ { A B } = \frac { n \left( I _ { A } \cap I _ { B } \right) } { n \left( I _ { A } \cap I _ { X _ { \mathrm { M A X } } } \right) } } \end{array}$

The confidence $C _ { A B }$ is the confidence candidate A assigns to the trust relation $t _ { A B } . \ X _ { \mathrm { M A X } }$ is the user with the maximum confidence assigned by A. It is worth mentioning that this only makes sense for similarity-based trust that is calculated based on the number of co-rated job-profiles. In the case of explicit trust, we can assume that the individuals have full confidence in their own explicit trust ratings. Thus, for explicit trust ratings the confidence value is always set to 1.

Building up on these assumptions, the overall aggregation of trust paths can be formalized as follows. Let $p \in P = \{ p _ { 1 } , . . . , p _ { q } )$ be a trust path between two persons, $N = \{ N _ { i } ; i { = } 1 , 2 , . . . , k \}$ all intermediate nodes in the trust path $p ,$ and $E T ^ { \prime } = t _ { y , x , z } ^ { \prime }$ the matrix containing the explicit trust ratings as predicted by the probabilistic latent aspect model. Using the confidence values as trust paths weights and combining the explicit and similarity-based trust calculation models, this leads to the following formula for predicting a previously unknown trust rating $t _ { A B } ^ { \prime } \ [ 4 4 ] $

$$
\begin{array}{l} t _ {A B} ^ {\prime} = \sum_ {p \in P} \left(\frac {C _ {A N _ {1}} \cdot C _ {N _ {1} N _ {2}} \cdots \cdot C _ {N _ {K} B}}{\sum_ {p \in P} C _ {A N _ {1}} \cdot C _ {N _ {1} N _ {2}} \cdots \cdot C _ {N _ {K} B}} t _ {A N _ {1}} \diamond t _ {N _ {1} N _ {2}} \diamond \dots \diamond t _ {N _ {K} B}\right) \text {with} \\ C _ {X Y} = \left\{ \begin{array}{c c} 1 & \text {if} t _ {X Y} \in E T ^ {\prime} \\ \frac {n (I _ {X} \cap I _ {Y})}{n (I _ {X} \cap I _ {X _ {\text {MAX}}})} & \text {otherwise} \end{array} \right\} \text {and} \\ t _ {(X - 1) X} \diamond t _ {X (X + 1)} = \left\{ \begin{array}{l l} \frac {n (I _ {X - 1} \cap I _ {X})}{n (I _ {X - 1} \cap I _ {X}) + n (I _ {X} \cap I _ {X + 1})} t _ {(X - 1) X} + \frac {n (I _ {X} \cap I _ {X + 1})}{n (I _ {X - 1} \cap I _ {X}) + n (I _ {X} \cap I _ {X + 1})} t _ {X (X + 1)} & \text {if} t _ {(X - 1) X} \text {and} t _ {X (X + 1)} \notin E T ^ {\prime} \\ t _ {(x - 1) X} \cdot t _ {X (X + 1)} & \text {otherwise} \end{array} \right. \end{array}
$$

In the context of person–team fit, where we want to predict the candidate's overall fit to a whole team and not to a single person, we could now calculate the trust values $t _ { M } { ^ { * } } _ { A }$ where $M ^ { * } = \{ M _ { i } ; i = 1 , 2 , . . . , k \}$ is a set of all existing team members. The calculated trust values could then be averaged to get the trust

$$
t _ {M ^ {*} A} = \frac {\sum_ {M _ {i} \in M ^ {*}} t _ {M _ {i} A}}{n _ {M ^ {*}}}, \text {   with   } n _ {M ^ {*}} \text {   being   the   number   of   existing   team   members. }
$$

In addition, we also need to calculate the fit from the candidate's perspective, as person–team fit requires a consideration of both, the needs–supplies and demands–abilities perspectives of fit [77,79]. For a discussion how to aggregate the trust values from the different fit perspectives, the reader is referred to [44].

## 4. Application and validation of the approach

This section presents results from test runs conducted with empirical data gained from a student experiment aimed at verifying the applicability of the approach presented for the selection of individuals for teams. The section first describes which metrics are used to evaluate the quality of the approach before the student experiment and the results of the test runs are discussed in detail. The section closes with a description of the chosen validation approach and discusses limitations and areas for future research.

## 4.1. Metrics for evaluating the quality of the approach

In a real-life setting, person–team fit is usually directly assessed by HR professionals $\mathrm { o r \mathrm { ~ - ~ } i d e a l l y \mathrm { ~ - ~ } }$ team members [40]. To assess the prediction quality of the approach, we assume that candidate evaluations as stated by team members are the best possible way to assess the candidate's aptitude to work in the respective team. To make sense, an IS-supported system must, therefore, generate results that are as close as possible to the results generated by those team members. The assumption of this validation approach is that we can replace aspects of human judgment with an automated IS-supported system. The team members effectively serve as proxy for predicting the level of fit between an individual and an existing team. The approach presented could be used for the pre-selection of candidates by generating a list of best-fitting persons, which can then be used to make final staffing decisions based on traditional human judgment. The research goal is not to outperform human judgment by finding better matches, but rather to generate a list of best-fitting-candidates that is as close as possible to the list that would have been created manually by HR professionals and team members. This is supposed to increase the productivity of HR professionals as it eliminates the need to manually screen all employee profiles.

It is common practice to evaluate recommender systems by dividing the dataset of user/item ratings into a testing set and a training set [26,66]. Usually, the training set data are removed from consideration in testing. The system is trained with the training set data and is supposed to predict the ratings in the testing set. As the original ratings are available, one can compare the predicted ratings with the actual ones.

To evaluate the quality of the results from the test runs, we use a receiver operating characteristic (ROC) curve analysis. The system is, generally, supposed to classify the candidates correctly as relevant or nonrelevant and rank them accordingly. If the best-fitting candidates are ranked at the top of the recommended list, the concrete predicted value does not matter. We assume that the team members or HR professionals will view the recommended candidates starting at the top of the list and work down until a sufficient number of candidates can be found [26,44].

As the presented system should support only the preselection and not replace the entire selection process, the classification into relevant and non-relevant candidates must be as accurate as possible so that relevant ones are on top and non-relevant ones are on the bottom of the list, i.e., ranked below the relevant candidates. The actual order among those relevant or non-relevant candidates seems to be less important. The HR professional is not supposed to find the single best-fitting candidate, but instead aims to create a list of good-fitting ones — which is then used to make the final selection decision. Therefore, it makes sense to use a classification accuracy metric such as ROC. In this context, sensitivity (hit rate) is the probability that a relevant candidate is recommended [25]. 1-Sensitivity (miss rate) is defined as the probability that an irrelevant candidate is selected. The ROC curve plots the miss rate on the x-axis against the hit rate on the y-axis [26], where the points on the curve correspond to the predicted level of relevance. This cutoff value defines the search length and thus determines how many of the top candidates in the list are actually considered when evaluating the classification accuracy of the system. For each cut off, the actual hit rate and the miss rate are different.

## 4.2. A student workshop

We conducted a multi-step experiment with a group of 21 students from two German universities (N = 21). The participants in the experiment were supposed to simulate existing team members and candidates whose fitness to the team should be evaluated. Students' disciplinary ranged from Economics over Business Administration and Industrial Engineering to Business Education. All students were about one year from their final degree (for further information see Ref. [44]).

The experiment was divided into two different phases. In a first phase, students were provided with 100 real-life job profiles that were randomly selected prior to the experiment and downloaded from a large

German internet job portal (www.jobpilot.de). Students were asked to rate the job profiles based on their preferences to apply for the given job offer. The prototype presented a 5-point scale ranging from 1 (“does not fit my preferences at all”) to 5 (“perfectly fits my preferences”). Students were asked to evaluate whether the profiles appealed to them with regard to their mid- or long-term career perspectives and planning. The job ratings gathered from the students were then used as input data for the job recommender. As described above, we use these captured job preference data to calculate similarities between users, with the aim of inferring previously unknown trust relations.

As the final step of the experiment, the students were asked to enter information about their relationships to other participants in the seminar and to fellow students from the two participating universities. The requested relational data was meant to express the trust one student has in another in relation to their life as students. Therefore, the students were asked to input the name of the partner, the date the relationship began and ended, and the intensity of the relationship on a 5-point scale ranging from 1 (very low intensity) to 5 (very high intensity). All rating data captured throughout the experiment were normalized to the preference values $\nu \in V = \{ 0 . 2 , 0 . 4 , 0 . 6 ,$ 0.8, 0.10}. The collected relational data were then used as input for the relational recommender.

Based on the above data and ratings, we began first test runs and validation activities. To evaluate the quality of the recommendations generated by the system, we considered the list of recommendations as a list of top-N items. We expected the system to generate for each student a list of top-N candidates that fit best in terms of trust. The resulting list is based on calculated predictions of whether the user will “like” an item (i.e. a candidate profile). The quality of the recommender system can, therefore, be assessed in terms of the quality of the predictions generated.

## 4.3. Results from test runs with the relational recommender

The relational recommender system was trained with a subset of the available data, as obtained from 21 students (see also Ref. [44]). The system then used (1) the existing relational data as provided by the students and (2) the similarities as gained from the job preference ratings, which is used as a trust proxy. Based on these data, the system calculated the likelihood of previously unknown trust relations. The generated results could then be compared with the original values to verify the prediction quality of the system. The result should be a list of top-N students in which the order should express the predicted level of fit [44]. Table 1 shows the training and testing dataset used in the test run.

Table 1  
The relational recommender test scenario for the student experimen

<table><tr><td colspan="2">Test data for the relational recommender</td></tr><tr><td colspan="2">Training dataset</td></tr><tr><td>Number of candidates</td><td>21</td></tr><tr><td>Number of trust relations</td><td>272</td></tr><tr><td colspan="2">(40 ratings from the testing set were excluded)</td></tr><tr><td colspan="2">Testing dataset</td></tr><tr><td>Number of candidates</td><td>4</td></tr><tr><td>Number of trust relations</td><td>10</td></tr><tr><td>Number of ratings</td><td>40</td></tr></table>

It must be noted, that lots of the given relational data could not be used within the relational recommendation process. The students did not only enter relationships with other participants in the seminar but also with other students. However, the separate networks of fellow students had only a few overlaps leading to the fact that the system could detect only very few similarities among the given trust relations. To reduce the sparsity problem we, therefore, selected the four students with the densest relational network. For each of these students, we removed the relational data of 10 randomly chosen fellow students. The removed students were thus seen as candidates for establishing a trust relationship and the system generated a ranked list of candidates based on their predicted level of fit towards the student in question. Due to the very small test dataset, we aggregated the intensity level students assigned to each relationship as we interpreted an intensity level of 3, 4, or 5 as ‘candidate is relevant’ and an intensity level of 1 or 2 as ‘candidate is irrelevant’.

Fig. 7 shows the ROC curve as generated by considering the aggregated results of the generated recommendations of all four students. The number of relevant candidates within the dataset $( N _ { r } )$ was 11 and the number of irrelevant candidates (N ) was 29. The true positive rate (Sensitivity) is plotted in function of the false positive rate (100-specificity) for different criterion values. Increasing the criterion value means that we include more results from the generated recommendations [26]. The recommender predicts a rating value between 0 and 1 for each team member-candidate trust rating pair depending on the predicted level of fit. A criterion value of <sup>N</sup>0.5, for example, means that we consider as result only those predicted team member-candidate ratings that have a predicted rating value of more than 0.5.

By increasing the level of the criterion value, we thus increase the length of the returned candidate list that is considered relevant. The table to the right of the graphic shows some of the criterion values, which are used to actually plot the points on the ROC curve. The table lists the belonging sensitivity and specificity for each of the example criterion values and also shows the criterion value with the highest accuracy. If we consider as relevant all team member-candidate rating pairs that received a predicted rating of more than 0.35, we get the most accurate result, i.e., minimal false negative and false positive results.

The area under the curve is A = 0.95 (SD: 0.05, CI 95%: 0.83 to 0.99). This means that a randomly selected team member-candidate rating pair from the group of relevant team member-candidate pairs has a predicted rating value that is larger than that from a randomly selected rating pair from the non-relevant group in 95% of the time. The 95% confidence interval (CI) is the interval in which the true (population) area under the ROC curve lies. Using the test of Hanley and McNeil

![](/api/attachments/PJ38RG8E/fulltext/images/5bdf558289a1a2dfb47906f9efb1423032eb4d1a0f666cce3718d9dc54f247a5.jpg)

<table><tr><td>Criterion</td><td>Sensitivity</td><td>Specificity</td></tr><tr><td>&gt;0.6</td><td>9.10</td><td>100.00</td></tr><tr><td>&gt;0.5</td><td>45.50</td><td>96.60</td></tr><tr><td>&gt;0.4</td><td>81.80</td><td>93.10</td></tr><tr><td>&gt;0.3</td><td>100.00</td><td>79.30</td></tr><tr><td>&gt;0.2</td><td>100.00</td><td>48.30</td></tr><tr><td colspan="3">Value with the highest accuracy:</td></tr><tr><td>&gt;0.35</td><td>90.90</td><td>89.70</td></tr></table>

Fig. 7. Test results: ROC curve of the relational recommender.

Research questions and answers

[23] shows that the ROC curve as generated from the relational recommender is different from random prediction $\scriptstyle ( p = 0 . 0 0 0 )$ . However, the significance of the difference cannot be assured due to the very small sample size [23,44].

## 4.4. Validation of the approach

For validation purposes, we draw mainly on the work of Sargent [65] and Naylor and Finger [56]. Following [78] we conduct the method validation in three consecutive steps (see also Ref. [44]):

## 4.4.1. Conceptual model validity

The purpose of this step is to determine whether “… the theories and assumptions underlying the model are correct and the model representation of the problem entity and the model's structure, logic, and mathemat ical and causal relationships are reasonable for the intended purpose of the model” [65]. The approach presented is based on validated findings in the literature on personnel selection, person–environment fit, and team staffing. The model's structure and causal relationships were to a large extent supported by our own observations. We also conducted face validations through interviews with HR experts from large consultancies and IT-service companies [44]. Furthermore, the use of traces – which is the tracking of entities through each sub model and the overall model – ensured that the logic of the conceptual model is correct [65].

## 4.4.2. Computerized model verification

This validation step should assure “… that the computer programming and implementation of the conceptual model are correct” [65]. Each sub model and the overall model were first tested with synthetic data. The results of those tests were validated by reprogramming the algorithms through manual calculation, yielding identical results. The sensitivity of the implemented model and the reproducibility of the results were assured by executing multiple synthetic test runs with extreme values.

## 4.4.3. Operational validity

The purpose of this final validation step is to determine whether the “… model's output behaviour has the accuracy required for the model's intended purpose of the domain of its intended applicability” [65]. Historical data validation was used within the student experiment to test for operational validity. The system was trained with part of the data and the remaining data were used to compare the predicted recommendations with the original ones. To evaluate the prediction accuracy of the system, a ROC curve analysis was used, utilizing Microsoft Excel 2003, SPSS 11.5 and MedCalc 8.1.1.0.

## 4.5. Limitations and further research

The results from the student experiment indicate the applicability of the approach presented to support the pre-selection of qualified candidates by considering trust as relational aspect. Such a system could be used to extend existing IS-supported selection approaches by focusing explicitly on the assessment of person–team fit. However, despite the promising results, it must be stated that the relational network data as gained from the 21 participating students were too sparse to generate valid recommendations for all of them — which is why only the four students with the densest trust networks were chosen. Further research with a bigger sample set should be undertaken to validate our findings. Other questions that need to be addressed are: How are the trust relations captured, how can it be assured that all employees specify their social network, and how can the trust values be kept up to date over time? Also, it makes sense to evaluate whether other relational aspects beside trust, or other concepts provided by SNA such as centrality or betweenness, could be used to increase the information density that exists within the social network structures.

<table><tr><td>Research question</td><td>Literature</td><td>Answer</td></tr><tr><td>How can the selection of individuals for teams be supported by IS?</td><td>Existing IS solutions in practice are based mainly on simple keyword-based queries.More innovative approaches do exist in theory.Existing approaches focus solely on P-J fit, neglecting the importance of P-T fit.</td><td>We identify three requirements for an IS-supported solution. This includes considering relational aspects to assess P-T fit.</td></tr><tr><td>Can recommender systems, originally used to recommend objects to users, also be used to recommend subjects?</td><td>Recent innovative approaches prove the applicability of recommender systems for the recommendation of candidates to jobs and of jobs to candidates.</td><td>We develop a trust computational model that incorporates trust as relational attribute into a recommender-based approach.</td></tr><tr><td>Can the selection quality be improved by incorporating relational aspects such as trust, and how can this be supported by IS?</td><td>P-T fit is as important as P-J fit.Relational attributes such as trust need to be considered in addition to unary attributes.</td><td>The results from the student experiment indicate the possibility to extend recommender-based approaches with relational aspects.</td></tr></table>

Further potential areas for future research include the diffusion of such types of decision support systems for personnel selection, the consideration of privacy aspects, and the extension of the approach presented not only to select individuals for existing teams but also to configure new teams from the beginning.

## 5. Conclusion and implications

In this paper, we argue that the increasing importance of team-based work structures demands that the selection of individuals for teams considers two aspects. First, candidates need to fit with the job so that they are able to fulfill all assigned tasks. Second, candidates need to fit with the team members in terms of interpersonal compatibility. We showed that the latter is only rarely supported by IS at present because existing approaches focus solely on the person–job fit. In this regard, the assessment is based only on unary attributes directly tied to an individual. However, these approaches do not consider relational aspects that are important to determine the fitness between an individual and the team members with whom the individual is supposed to work. Pursuant to findings from research on person–job and person–team fit, we conclude that an automated recommendation approach needs to integrate unary candidate attributes as well as relational information such as trust. Some parts of the data required can be derived from personal profiles that are already stored electronically in many human resource information systems.

Based on these findings, we presented a relational recommendation approach that uses existing trust relations among employees and candidates, as well as job preference similarities, to predict trust relations that are previously unknown. This was done because trust is seen by many authors as an important precondition for effective teamworking. A student experiment was conducted where the relational recommendation model was used to recommend students to other students based on the given training data leading to results very close to the original ratings. Table 2 summarizes our concrete research questions, together with related findings from the literature and results from our research. We believe that an IS-supported team staffing approach that includes relational aspects can have important implications. Personnel selection theory explicitly underlines the importance of assessing person–team fit rather than focusing solely on person–job fit when selecting individuals to work in teams. In this paper, we propose a relational recommendation approach that builds on this request by predicting trust relations between team members and candidates. For practitioners, such an approach can lead to faster and better pre-selection results than are achieved today through keyword-based queries that focus only on person–job fit. As we expect an even more prominent role for team-based work in the future, a personnel selection system that considers relational aspects is likely to raise the attention of researchers and practitioners.

## References

[1] A. Abdul-Rahman, S. Hailes, Supporting trust in virtual communities, Proceedings of the 33rd Hawaii International Conference on System Sciences (Maui, Hawaii, USA), 2000.

[2] N. Anderson, F. Lievens, K. van Dam, A.M. Ryan, Future perspectives on employee selection: key directions for future research and practice, Applied Psychology: An International Review 53 (4) (2004) 487–501.

[3] M. Balabanovic, Y. Shoham, Fab: content-based, collaborative recommendation, Communications of the ACM 40 (1997) 66–72.

[4] H.K. Bhargava, K.J. Snoap, Improving recruit distribution decisions in the US Marine Corps, Decision Support Systems 36 (2003) 19–30.

[5] J.S. Breese, D. Heckerman, K. Kadie, Empirical analysis of predictive algorithms for collaborative filtering, Proceedings of the 14th UAI Conference, 1998, pp. 43–52.

[6] N. Brennan, B. Connell, Intellectual capital: current issues and policy implications, Journal of Intellectual Capital 1 (3) (2000) 206–240.

[7] M.A. Campion, G.J. Medsker, A.C. Higgs, Relations between work group characteristics and effectiveness: implications for designing effective work groups, Personnel Psychology 46 (1993) 823–850.

[8] J.A. Chatman, Improving interactional organization research: a model of person–organization fit, Academy of Management Review 14 (1989) 333–349.

[9] M. Chau, Z. Huang, J. Qin, Y. Zhou, H. Chen, Building a scientific knowledge web portal: the NanoPort experience, Decision Support Systems 42 (2) (2006) 1216–1238.

[10] K. Cheung, J.T. Kwok, M.H. Law, K. Tsui, Mining customer product ratings for personalized marketing, Decision Support Systems 35 (2003) 231–243.

[11] T.S. Cho, D.C. Hambrick, M.-J. Chen, Effects of top management team characteristics on competitive behavior of firms, Academy of Management Proceedings, 1994, pp. 5–17.

[12] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum likelihood from incomplete data via the EM algorithm, Journal of the Royal Statistical Society. Series B 39 (1997) 1–38.

[13] G. DeSanctis, P. Monge, Introduction to the special issue: communication processes for virtual organizations, Organization Science 10 (6) (1999) 693–703.

[14] J.R. Edwards, Person–Job Fit: a conceptual integration, literature review, and methodological critique, in: C.L. Cooper, T. Robertson

(Eds.), International Review of Industrial and Organizationa Psychology, Wiley, New York, 1991, pp. 283–357.

[15] C.R. Evans, K.L. Dion, Group cohesion and performance: a meta-analysis, Small Group Research 22 (1991) 175–186.

[16] F. Färber, T. Keim, T. Weitzel, An automated recommendation approach to personnel selection, Proceedings of the 2003 Americas Conference on Information Systems (Tampa, USA), 2003.

[17] J.R.P. French, R.D. Caplan, R.V. Harrison, The Mechanism of Job Stress and Strain, Wiley, London, 1982.

[18] N. Good, J. Schafer, J. Konstan, A. Borchers, B. Sarwar, J. Herlocker, J. Riedl, Combining collaborative filtering with personal agents for better recommendations, Proceedings of the 16th National Conference on Artificial Intelligence, 1999, pp. 439–446.

[19] M. Granovetter, The strength of weak ties: a network theory revisited, Sociological Theory 1 (1983) 201–233.

[20] R. Guha, R. Kumar, P. Raghavan, A. Tomkins, Propagation of trust and distrust, Proceedings of the World Wide Web Conference (New York, USA), 2004.

[21] R.A. Guzzo, Fundamental considerations about work groups, in: M.A. West (Ed.), Handbook of Workgroup Psychology, Wiley, Chichester, UK, 1996, pp. 3–21.

[22] J. Hackman, C.G. Morris, Group task, group interaction process, and group performance effectiveness: a review and proposed integration, in: L. Berkowitz (Ed.), Advances in Experimental Social Psychology, Academic Press, New York, 1975, pp. 45–99.

[23] J.A. Hanley, B.J. McNeil, A method of comparing the area under receiver operating characteristic curves derived from the same cases, Radiology 148 (1983) 839–843.

[24] G. Heinrich, T. Keim, C. Jung, U. Krafzig, S. Noll, Smart collaboration networks — a toolkit and a vision for creating and predicting trusted partnership, eChallenges (Ljubljana, Slovenia), 2005.

[25] J.L. Herlocker, J.A. Konstan, A. Borchers, J. Riedl, An algorithmic framework for performing collaborative filtering, Proc. of the 22nd ACM SIGIR Conference on Research and Development in Information Retrieval, 1999.

[26] J. Herlocker, J. Konstan, L. Terveen, J. Riedl, Evaluating collaborative filtering recommender systems, ACM Transactions on Information Systems 22 (1) (2004) 5–53.

[27] T. Hofmann, Probabilistic latent semantic analysis, Proceedings of the 15th Conference on Uncertainty in Artificial Intelligence, UAI, Stockholm, Sweden, 1999, pp. 289–296.

[28] T. Hofmann, J. Puzicha, Latent class models for collaborative filtering, Proceedings of the 16th International Joint Conference on Artificial Intelligence (Stockholm, Sweden), 1999, pp. 688–693.

[29] J.L. Holland, Making Vocational Choices: A Theory of Careers, 2nd ed. Englewood Cliffs, New York, 1985.

[30] W.W. Huang, K.-K. Wei, R.T. Watson, B.C.Y. Tan, Supporting virtual team-building with a GSS: an empirical investigation, Decision Support Systems 34 (2002) 359–367.

[31] Z. Huang, H. Chen, F. Guo, J.J. Xu, S. Wu, W.-H. Chen, Expertise visualization: an implementation and study based on cognitive fit theory, Decision Support Systems 42 (3) (2006) 1539–1557.

[32] S.E. Jackson, The consequences of diversity in multidisciplinary work teams, in: M.A. West (Ed.), Handbook of Workgroup Psychology, Wiley, Sussex, 1996.

[33] G.R. Jones, J.M. George, The experience and evolution of trust: implications for cooperation and teamwork, The Academy of Management Review 23 (3) (1998) 531–546.

[34] A. Jøsang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decision Support Systems 43 (2) (2007) 618–644.

[35] T.A. Judge, G.R. Ferris, The elusive criterion of fit in human resource staffing decisions, Human Resource Planning 15 (4) (1992) 47–67.

[36] S.D. Kamvar, M.T. Schlosser, H. Garcia-Molina, The eigentrust algorithm for reputation management in P2P networks, Proceedings of the 12th International World Wide Web Conference, 2003, pp. 640–651.

[37] T. Keim, W. König, F. von Westarp, T. Weitzel, O. Wendt, Recruiting Trends 2005-Eine empirische Untersuchung der Top-1.000-Unternehmen in Deutschland und von 1.000 Unternehmen aus dem Mittelstand, Working paper, 2005.

[38] R. Khare, A. Rifkin, Weaving a web of trust, WWW Journal 2 (3) (1997) 77–112.

[39] D.J. Kim, Y.I. Song, S.B. Braynov, H.R. Rao, A multidimensional trust formation model in B-to-C e-commerce: a conceptual framework and content analyses of academia/practitioner perspectives, Decision Support Systems 40 (2) (2005) 143–165.

[40] R.J. Klimoski, R.G. Jones, Staffing for effective group decision making: key issues in matching people and teams, in: R. Guzzo, E. Salas (Eds.), Team Effectiveness and Decision Making in Organizations, Jossey-Bass, San Francisco, 1995, pp. 291–332.

[41] M.A. Korsgaard, S.E. Brodt, H.J. Sapienza, Trust, identity, and individual attachment: promoting individual's cooperation in groups, in: M.A. West, D. Tjosvold, K.D. Smith (Eds.), International Handbook of Organizational Teamwork and Cooperative Working, Wiley, Chichester, UK, 2003, pp. 113–130.

[42] A.L. Kristof, Person–organization fit: an integrative review of its conceptualizations, measurement, and implications, Personnel Psychology 49 (1) (1996) 1–49.

[43] K. Lewin, Field Theory in Social Science, Harper & Row, New York, 1951.

[44] J. Malinowski, Decision Support for Team Staffing — A Probabilistic Approach for Multilevel Fit, (Frankfurt, Germany, Dissertation thesis, University of Frankfurt 2006).

[45] J. Malinowski, T. Keim, T. Weitzel, Analyzing the impact of IS support on recruitment processes: an E-recruitment phase model, The Ninth Pacific Asia Conference on Information Systems (Bangkok, Thailand), 2005.

[46] J. Malinowski, T. Keim, T. Weitzel, O. Wendt, Decision support for team building: incorporating trust into a recommender-based approach, The Ninth Pacific Asia Conference on Information Systems (Bangkok, Thailand), 2005, pp. 604–617.

[47] J. Malinowski, T. Keim, O. Wendt, T. Weitzel, Matching people and jobs — a bilateral recommendation approach, 39th Hawaii International Conference on System Sciences (Hawaii), 2006.

[48] T.W. Malone, R.J. Laubacher, The dawn of the E-lance economy, Harvard Business Review 76 (5) (1998) 144–152.

[49] D. Mankin, S. Cohen, T. Bikson, Teams and Technology: Fulfilling the Promise of the New Organization, Harvard Business School Press, Boston, MA, 1996.

[50] D.J. McAllister, Affect- and cognition-based trust as foundations for interpersonal cooperation in organizations, Academy of Management Journal 38 (1995) 24–59.

[51] A.C. McClough, S.G. Rogelberg, Selection in teams: an exploration of the teamwork knowledge, skills and abilities test, International Journal of Selection and Assessment 11 (2003) 56–66.

[52] D.H. McKnight, N.L. Chervany, The meanings of trust, Technical Report 94-04, Carlson School of Management, 1996.

[53] P. Melville, R.J. Mooney, R. Nagarajan, Content-boosted collaborative filtering for improved recommendations, Proceedings of the 18th National Conference on Artificial Intelligence, 2002, pp. 187–192.

[54] M. Montaner, B. Lopez, J. de la Rosa, Opinion-based filtering through trust, Proceedings of the Sixth International Workshop on Cooperative Information Agents (Madrid, Spain), 2002, pp. 164–178.

[55] P.M. Muchinsky, C.J. Monahan, What is person–environment congruence? Supplementary versus complementary models of fit, Journal of Vocational Behavior 31 (1987) 268–277.

[56] T.H. Naylor, J.M. Finger, Verification of computer simulation models, Management Science 14 (2) (1967) B92–B101.

[57] C. Ostroff, S.W.J. Kozlowski, Organizational socialization as a learning process. The role of information acquisition, Personnel Psychology 43 (1992) 849–867.

[58] N. Panteli, S. Sockalingam, Trust and conflict within virtual interorganizational alliances: a framework for facilitating knowledge sharing, Decision Support Systems 39 (4) (2005) 599–617.

[59] M. Papagelis, D. Plexousakis, T. Kutsuras, Alleviating the sparsity problem of collaborative filtering using trust inferences, 3rd International Conference on Trust Management, iTrust, 2005.

[60] A. Popescul, L.H. Ungar, D.M. Pennock, S. Lawrence, Probabilistic models for unified collaborative and content based recommendation in sparse-data environments, Proceed ings of the Seventeenth Conference on Uncertainty in AI (Seattle, USA), 2001, pp. 437–444.

[61] P. Resnick, H.R. Varian, Recommender systems, Communica tions of the ACM 40 (3) (1997) 56–58.

[62] M. Richardson, R. Agrawal, P. Domingos, Trust management for the semantic web, Proceedings of the Second International Semantic Web Conference (Sanibel Islands, USA), 2003, pp. 351–368.

[63] J. Rotter, A new scale for the measurement of interpersonal trust, Journal of Personality 35 (1967) 651–665.

[64] J. Rotter, Interpersonal trust, trustworthiness, and gullibility, American Psychologist 35 (1980) 1–7.

[65] R. Sargent, Verification and validation of simulation models, Proceedings of the 30th Winter Simulation Conference, 1998, pp. 77–78.

[66] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative filtering recommender algorithms, Proceedings of the 10th International World Wide Web Conference, 2001, pp. 285–295.

[67] A. Schein, A. Popescul, L.H. Ungar, D.M. Pennock, Methods and metrics for cold-start recommendations, Proceedings of the 25th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 2002, pp. 253–260.

[68] B. Schneider, A. Kristof-Brown, H.W. Goldstein, D.B. Smith, What is this thing called fit? in: N. Anderson, P. Herriot (Eds.), International Handbook of Selection and Assessment, 1997, pp. 391–412.

[69] M. Schoemaker, J. Jonker, Managing intangible assets — an essay on organising contemporary organisations based upon identity, competencies and networks, Journal of Management Development 24 (6) (2005) 506–518.

[70] J. Scott, Social Network Analysis, Sage Publications, London, 2000.

[71] A. Seers, Team-member exchange quality: a new construct for role-making research, Organizational Behavior and Human Decision Processes 43 (1989) 118–135.

[72] T. Sekiguchi, Person–organization fit and person–job fit in employee selection: a review of the literature, Osaka Keidai Ronshu 54 (2004) 179–196.

[73] R.D. Smither, The Psychology of Work and Human Performance, 3rd ed. Longman, New York, 1998.

[74] A.R. Spokane, E. Meir, M. Catalano, Person–environment congruence and Holland's theory: a review and reconsideration, Journal of Vocational Behavior 57 (2000) 137–187.

[75] M.J. Stevens, M.A. Campion, The knowledge, skill, and ability requirements for teamwork: implications for human resource management, Journal of Management 20 (1994) 503–530.

[76] L. Tihanyi, A.E. Ellstrand, C.M. Daily, D.R. Dalton, Building of the top management team and form international diversification, Journal of Management 26 (6) (2000) 1157–1177.

[77] W.E. Watson, K. Kumar, L.K. Michaelsen, Cultural diversity's impact on interaction process and performance: comparing homogeneous and diverse task groups, Academy of Management Journal 36 (1993) 58–79.

[78] T. Weitzel, D. Beimborn, W. Koenig, A unified economic model of standard diffusion: the impact of standardization cost, network effects, and network topology, Management Information Systems Quarterly 30 (2006) 489–514 (Special Issue on Standard Making).

[79] J.D. Werbel, S.W. Gilliland, Person–environment fit in the selection process, in: G.R. Ferris (Ed.), Research in Personnel and Human Resource Management, vol. 17, JAI Press, Stamford, CT, 1999, pp. 209–243.

[80] J.D. Werbel, D.J. Johnson, The use of person–group fit for employment selection: a missing link in person–environment fit, Human Resource Management 40 (3) (2001) 227–240.

[81] M.A. West, Effective Teamwork, 2nd edition. The British Psychological Society Blackwell Publishing Ltd., Leicester, UK, 2004.

[82] M.A. West, N.J. Allen, Selecting for teamwork, in: N. Anderson, P. Herriot (Eds.), International Handbook of Selection and Assessment, 1997, pp. 491–505.

[83] B.K. Wong, T.A. Bodnovich, Y. Selvi, Neural network applications in business: a review and analysis of the literature (1988– 95), Decision Support Systems 19 (2003) 301–320.

[84] J. Xin, Z. Yanzan, B. Mobasher, Web usage mining based on probabilistic latent semantic analysis, Proceedings of the 2004 ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (Seattle, WA, USA), 2004, pp. 197–205.

[85] B. Yu, M.P. Singh, Social networks and trust: detecting deception in reputation management, Proceedings of the Second International Joint Conference on Autonomous Agents and Multiagent Systems (Melbourne, Australia), 2003, pp. 73–80.

[86] G. Zacharia, A. Moukas, P. Maes, Collaborative reputation mechanisms for electronic marketplaces, Decision Support Systems 29 (2000) 371–388.

[87] J.L. Zhao, H.H. Bi, H. Chen, D.D. Zeng, C. Lin, M. Chau, Process-driven collaboration support for intra-agency crime analysis, Decision Support Systems 41 (3) (2006) 616–633.

[88] C.N. Ziegler, G. Lausen, Analyzing correlation between trust and user similarity in online communities, Proceedings of the 2nd International Conference on Trust Management, 2004.

![](/api/attachments/PJ38RG8E/fulltext/images/b96fec0feabe5eea845dbf4d769590e17e34bb2e6beeb1286506db88576d9b4e.jpg)  
Dr. Jochen Malinowski submitted his dissertation thesis at the Institute of Information Systems, School of Business and Economics at Goethe University in Frankfurt, Germany. He holds a Master in Information Systems from Essen University in Germany and has worked as IT consultant for several years, with a focus on IT Business Alignment. His current research interests are in the area of Human Resource Management, E-Recruiting and Team Staffing.

![](/api/attachments/PJ38RG8E/fulltext/images/b4c4bec77fcbc2136fb69b4547c8a8644eea40fd6e74e88f206a08d7d33b83d0.jpg)

Tim Weitzel is Professor and Chair in the Information Systems and Services Department at the University of Bamberg. He received his PhD from Goethe University in Frankfurt, Germany, where he was head of numerous research and consulting projects on standardization, E-Finance, E-Recruiting, and outsourcing. Tim is the author of over 60 reviewed articles and four books. His research on standards and networks, outsourcing, IT business

alignment, and Human Resource IS has been published among others in MIS Quarterly, Electronic Markets, Wirtschaftsinformatik, ZfB, JECR.

![](/api/attachments/PJ38RG8E/fulltext/images/cf49bbd2cd8d6301722c80d6a94c0fee0a07b1568ae3c32c7988843bfca0d57e.jpg)

Tobias Keim graduated in business administration from Frankfurt and Paris IX Dauphine Universities. In 2002, he joined the Institute of Information Systems where his research interests include the adoption and value of Human Resource Information Systems (HRIS) for personnel recruitment. As part of the project “Online Partnership Lens (OPAL)”, his research was funded by the European Commission. Currently, Tobias receives a grant from the German Research

Foundation (DFG) for his research within the PhD Program “Enabling technologies for electronic commerce”.
