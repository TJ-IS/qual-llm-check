---
otero_id: 24778
otero_key: "JGT6G582"
title: "Improved Decision Making through Better Integration of Human Resource and Business Process Factors in a Hospital Situation"
authors: "Tony Holden; Paul Wilhelmij"
year: "1995"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1995.11518089"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improved Decision Making through Better Integration of Human Resource and Business Process Factors in a Hospital Situation

Tony Holden & Paul Wilhelmij

To cite this article: Tony Holden & Paul Wilhelmij (1995) Improved Decision Making through Better Integration of Human Resource and Business Process Factors in a Hospital Situation, Journal of Management Information Systems, 12:3, 21-41, DOI: 10.1080/07421222.1995.11518089

To link to this article: http://dx.doi.org/10.1080/07421222.1995.11518089

![](/api/attachments/JGT6G582/fulltext/images/691db71a662f189ff3d9eb143c512df83cb03b93ce512083005c1e76d3f8c2bf.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/JGT6G582/fulltext/images/d672ae6a48496e3a68afc6c3d698e4d1cfabbf0cb28be0d64baecc408fd29eab.jpg)

Submit your article to this journal ↗

![](/api/attachments/JGT6G582/fulltext/images/2619bfecc380ffee54c1524bb28de03f6e2df696eea7c119312062c228292779.jpg)

View related articles ↗

![](/api/attachments/JGT6G582/fulltext/images/74ac75901327f810af2b864f28fe58e8d4a0685dbebab466c92baa89e433274b.jpg)

Citing articles: 8 View citing articles ↗

# Improved Decision Making through Better Integration of Human Resource and Business Process Factors in a Hospital Situation

TONY HOLDEN AND PAUL WILHELMIJ

TONY HOLDEN leads the Decision Support Group at the University of Cambridge. He has a Ph.D. in artificial intelligence from the University of London. His employment and consultancy experience covers the defense manufacturing, telecommunications, energy, and financial industries. Dr. Holden has produced and contributed to many publications on the application and theory of advanced CAD, artificial intelligence, and industrial process modeling. He has been co-chair of the International Conference on Intelligent CAD, a review panelist for the Applications of Artificial Intelligence in Engineering Conference, and is a member of both the IFIP Working Group 5.2 on information standards for design support and the UK CALS Industry Council Education, Research and Training Committee.

PAUL WILHELMIJ has worked for several years in the petrochemical industry since completing a doctoral program in design systems and decision support at the University of Cambridge. He is currently responsible for project and consultancy work in decision support, organizational design, and corporate knowledge management, including the application of computer-aided acquisition and logistic support (CALS). His publications include a book on artificial intelligence techniques for decision support and various papers on safety management, process redesign, and acoustic techniques for remote sensing. He is also an Industrial Fellow in Decision Support at the University of Cambridge where he maintains an active research role.

ABSTRACT: Business process models are designed in isolation but must be applied in real organizational and business situations. A key management concern is how to identify the nonprocess factors that allow a business process to achieve maximum performance. In this paper, we demonstrate the application of the KNOVA (KNOwledge Value-Added) technique to the problem of making visible the hitherto intangi-

Acknowledgments: The initial KNOVA application framework was developed collaboratively with British Petroleum; the work was initiated with Professor Jack Betteridge (presently with the London Business School) of the Information Strategy team as part of a broader corporate initiative on knowledge networking. It would not have been possible to develop and refine KNOVA without the contribution of a range of individuals internal and external to BP, including Richard Reiley, manager of BP Exploration's Stuck Pipe Awareness Campaign; Ian Pitkethly also with the Stuck Pipe Awareness Campaign, Sandra Dawson and Katie Stewart from the Imperial College Management School who kindly provided the data for the drilling team comparison, and Michael Glykas, Rita Schade, Wai-Yin Chow, and Justin Cross of Cambridge University who helped develop the team BPM and knowledge aspects.

ble people, culture, and knowledge factors that can easily influence the success or failure of a business process. We illustrate its application to the processes of a diagnostic team within a department of a large hospital. Two benefits ensue: (1) the articulation of a common understanding of the factors that affect team performance and, (2) the pinpointing of resource investment to maintain performance and reduce risk or cost.

KEY WORDS AND PHRASES: business process modeling, business reengineering, organizational knowledge, team-oriented management.

## Introduction: Where Business Process Engineering Fails

BUSINESS PROCESS MODELING (BPM) AND REENGINEERING (BPR) are currently the subject of major commercial and academic attention. Many different methods are appearing, each one shedding a different light on the business problem. Some favor an “accounting” emphasis on flow charting and costs $[1, 3, 8, 11, 12, 19, 20, 26]$ . Others stem from an information technology systems pedigree $[5, 15, 16, 17, 29]$ and focus on data and control, whereas others look to apply a more organizational theory-oriented approach $[22, 23]$ .

Each approach has its merits but all tend to have in common the fact that the resulting models typically are delivered as “stand-alone” artifacts and are seen in isolation from the environment within which they are to be employed.

One driver for the rise in BPR techniques has been the desire to cut out unnecessary organizational bureaucracy and levels of management. In the classical management model, both these roles are concerned with manipulating information for the benefit of the directorial and operational business units. With the availability of information and communication technology, the temporal and spatial foundations of business are changing and these traditional roles are also changing, or disappearing altogether. For example, workers in a company can now be geographically far apart and send (electronic) documents in real time; the associated removal of administrative layers means that core profit-making business processes and their effectiveness are being forced into sharper focus.

Given the pressure to reduce costs and increase performance, there is an interest in making new business processes maximally efficient. Although much effort is expended on developing elegant and ingenious BPM techniques, it is often overlooked that factors concerning the process environment (e.g., culture, shared knowledge) and the agents that support the processes (i.e., people and their level of skill and knowledge) can have a significant influence on their success and acceptance.

This paper is linked to work done by Glykas, Holden, and Wilhelmij [10] using the ARMA (Agent Relationship Modeling Analysis) BPM technique for safety-critical situations in the petrochemical industry. ARMA provides a structured way of modeling the roles and responsibilities of people and other agents along with the information and knowledge resources that support decision making. Further experience with ARMA confirmed its value as a way of formally validating business process (to find potentially unsafe situations) and managing information flows, and as a way of developing a commonly agreed understanding of collaboration within a team. However, it became clear that in such environments, two intangible and pervasive factors are found to have a major effect on risk and performance. These are knowledge and culture. For example, safety on oil rigs [14] is an area where people and environmental factors are acknowledged to influence safety in a profound way [25].

Operational performance and risk management are frequently the concern of team leaders. “Risk” may refer to the risk to financial success, human safety, or simply the uncertainty of future outcomes. Certain types of business activities lend themselves well to orthodox BPM. Manufacturing, administrative, and accounting procedures are examples. These have clear steps and performance is easily measured or uncontentious (e.g., unit of output/hour). In other areas, “soft” human factors, culture, or the ability to apply knowledge are of prime importance.

The problem is one of articulating the link between the “hard” factors of investment, performance, and benefit that can be measured in tangible (e.g., financial) terms and the “soft” and more pervasive, intangible factors relating to knowledge, people, and culture. And, even more important, where in the organization are the levers of control—those organizational focal points that managers can target to initiate and influence change—and how should investment be designed to effect a positive change in a team’s performance?

To increase the chances for success of the proposed reengineering, one must also consider subtleties that are often not addressed by conventional BPR techniques. It has long been known that it is often not the resultant model that is useful but the team building and shared appreciation that emerge from the BPR exercise. Activities leading to these benefits typically include the externalization of tacit knowledge about what makes the organization work or fail, the development of a consensus about what can be done and the assuaging of early fears relating to possible changes. The issue of computer tools to support consensus development through shared development of a business model has been pursued elsewhere. Dennis et al. [4] and Nunamaker [21] describe electronic meeting rooms where group members work together to share the task of business reengineering. Through such a shared interaction, the softer factors governing business process performance can be expressed implicitly, although KNOVA, in contrast, aims to make these explicit.

This paper describes the KNOVA (KNOwledge Value-Added) technique and how it was applied to elucidate a model of a complex medical diagnostic/patient care process in a department of a large hospital.

First we outline the underpinning philosophy and objectives of KNOVA. We then describe the hospital situation that is the subject of the case study, along with an overview of the contemporary change-related and other factors of concern to managers. Next, we describe the process by which KNOVA is applied in the context of the case study. This includes a description of a computer-based modeling aid used to shed light on the dynamic aspects of the organizational and team situation. We conclude with some of the implications of our approach.

KNOVA was originally developed from an in-depth assessment of practical knowledge requirements facing management in the oil and gas industry with British Petroleum (BP), a major international oil company. KNOVA was used by BP to understand how knowledge affects business performance, and how to improve best practice regarding knowledge investment and management.

Applications of KNOVA have included a postproject appraisal of the drilling team performance improvement campaign $[27]$ , and a comparison of the culture of drilling teams in Alaska, the Gulf of Mexico, and the North Sea $[28]$ . These applications and other industrial work have helped ensure that KNOVA addresses practical, rather than theoretical, management needs. For information about the origins of KNOVA and its theoretical basis, the interested reader is referred to $[27, 28, 29]$ .

## What Is KNOVA?

KNOVA IS A TOOL THAT ALLOWS MANAGERS TO IMPROVE their understanding of the factors influencing the performance and direction of a working group or team. This improved understanding increases confidence in decision making and overall group operations. Specifically, KNOVA is particularly useful in identifying performance measures and areas for investment (such as training, technology, or resources) to improve weak points or change the style of work.

However, organizations are traditionally viewed and assessed within a quantitative, structural framework, with poor integration of the “soft” people and cultural issues. There is no recognized practical management framework that integrates the interrelationships between people, performance, costs/investment, culture, structure, and soft resources such as knowledge. As a result, there is no decision procedure to identify investment options for performance improvement that considers the overall context.

The KNOVA framework described here addresses this need by developing a model of the factors influencing team performance, along with a decision procedure for applying this model to identify investment options for improved performance. The performance model is based on the interactions among people, knowledge, and organizational culture. An important aspect is explicit identification of the knowledge resources of the team, in both active and latent form. This provides a conceptual basis for an integrated model.

Critical managers might say, “But I already understand my team’s situation.” KNOVA does not negate existing skills but allows them to be applied more quickly and with less mental effort. This is useful when operating pressures allow insufficient time to give full consideration to all factors. KNOVA is complementary to and can be used alongside conventional business process reengineering approaches. It is an unfortunate fact that a high proportion of BPR projects fail. Often this is because the projects take a view of the organizational situation that does not include the softer and more pervasive issues that govern performance and risk. It this latter dimension that KNOVA is designed to address. The complementarity between KNOVA and existing BPR is discussed further in later sections.

The elements of a KNOVA review are expressed in the condensed influence diagram shown in Figure 1. The arrows show influencing relationships between the factors with which KNOVA is concerned that affect team performance.

![](/api/attachments/JGT6G582/fulltext/images/07e6d6ed2004d4670b61a5eca9d7bd89affee19af018a6d07348acb1440e800e.jpg)  
Figure 1. The KNOVA Top-Level Influence Diagram

By progressively expanding this model using the techniques to be described, a detailed representation of the situation under examination is produced. In essence, KNOVA explicitly identifies and integrates:

\- Knowledge possessed by the team.

• People factors such as staff turnover and motivators.

\- Culture of the organization in terms of the informal microculture and the formal macroculture.

\- Investment in the team and its environment for improved performance.

• Performance of the team, such as the quality of decisions or actions.

\- Benefits of the investment and improved performance, for example, operational cost savings.

\- Time over which the investment takes place, and performance is tracked.

Time is treated as an implicit factor, while the environment of the team, or the team context, is accommodated within the culture factors. Microcultural factors reflect the way things are done in the immediate team, the local environment of the team, and the overall organizational environment. Macroculture reflects wider organizational issues such as monetary reward.

## When Is KNOVA Useful?

Typical circumstances that might motivate the use of KNOVA are when:

\- A group's external environment is changing.

\- A group's own composition is changing, say, through staff changes.

• A group is redefining its role.

\- Operating and cost efficiency must be improved.

\- Senior management must be reassured that a group is contributing to corporate profit and performing efficiently.

All these situations require the identification, reassessment, or redirection of individual and group strengths. New channels and modes of communication with the outside world may need to be defined. Resource usage and procedures may need to be tightened. Staff turnover means loss of useful skills and the need to integrate new people in a way that is least disruptive to operations.

Without investing in resources such as training, technology, procedures, or infrastructure, it is not possible to adapt to change. Uncertainty about where to invest implies a risk. KNOVA increases the confidence of operational and senior managers by providing a tool for highlighting areas where investment can be made beneficially and where ongoing performance can be monitored.

## The KNOVA Knowledge Framework

GOOD OPERATIONAL PERFORMANCE COUPLED WITH REDUCED RISK of poor decisions require a decision-making framework for staff that is aligned with the organizational policies and environment. This framework must address, in an integrated way, management factors such as systems and procedures; team factors such as knowledgeable and informed staff and the culture of the work environment; information factors such as the quality and accessibility of operating procedures and documentation; and technology factors such as automated systems and information technology presented in a way comfortable to the operational user.

In order to provide an overall view that integrates these factors and can accommodate both formal and informal aspects of operational decision making, a knowledge-based framework is needed. “Knowledge” in this context includes knowhow, expertise, information, and data. A KNOVA review provides a systematic approach to identifying the various factors that influence risk and performance in the organizational situation. The outcome of KNOVA can be regarded as a knowledge investment plan.

A KNOVA review provides three main deliverables: (1) the identification of strengths and weaknesses in the team situation that are affecting performance--these highlight the management "levers of control" at which investment can be targeted; (2) a static influence diagram customized to the organizational situation under review that provides a graphical representation of the interrelating factors; and (3) a dynamic computer model to improve insight into the time-based features of the situation. To facilitate this process, we have developed a computer decision-support tool (Figure 2) constructed from a commercial package called EXTEND. The details of how this package is applied are elaborated later, but in essence, the tool helps speed the process of data gathering, provides an automated graphical means of communicating the KNOVA review process, and allows for "what-if" analysis of investment options. Its use as a means of communicating and making visible the review process and keeping it "open" for all to see is particularly worthwhile.

The objectives and, by consequence, benefits of a KNOVA study are:

Figure 2. The KNOVA Decision Support Tool Desktop

File Edit Library Model Text Define Run Window

![](/api/attachments/JGT6G582/fulltext/images/d311ae755c45e2300c70f435cad59be03b7222f5b4badf3ba02d0215c4d02ad8.jpg)

\- Clarification of the links between hard factors such as costs, and soft “people” issues such as culture and knowledge.

\- Reduced risk—for example, of erroneous expenditure, false patient diagnoses, or safety.

• Better cost management.

\- Better use and sharing of team knowledge resources.

\- Facility for tracking soft factors, performance, and variations over time.

By providing a computer-based realization of KNOVA, the process of performing a KNOVA analysis is made accessible to the line manager. Also, analyses can be performed at regular intervals and the results stored. This means performance trends can be followed and corrective action taken.

The time element and its relationship to knowledge are an original aspect of KNOVA. Both active knowledge (knowledge used on the job) and latent knowledge (knowledge possessed but not employed directly) become obsolete and decay with time. Ongoing investment is needed to maintain the active knowledge at a level sufficient to ensure adequate performance. The computer-based model provides a dynamic dimension allowing managers to see how these two types of knowledge are affected by investment (or neglect) and how they grow or decay with time. KNOVA allows an organization to value people in terms of the knowledge they possess and begin to quantify knowledge as a real corporate resource.

It is worth pointing out that, from a corporation tax perspective, knowledge, or knowhow, is a legally recognized term. For tax purposes, “knowhow” is defined as industrial information and techniques likely to assist in manufacturing or processing goods or materials or in working (or searching for) mineral deposits or in agricultural, forestry, or fishing operations $[24]$ . Capital allowances for knowhow expenditure are available to industry and primary producers. The effect of this is to reduce the corporation tax liability. Anything that helps make a corporation’s knowledge assets more identifiable can have financial benefits.

## The Team Situation under Consideration

## The Hospital Department

THE DEPARTMENT USED AS THE CASE STUDY IS A RADIOLOGY UNIT in a large hospital. The two main roles of the department are (1) to provide a diagnostic service to hospital doctors (clinicians) and general practitioners, and (2) to perform therapeutic interventional procedures. The diagnostic service involves the production and interpretation of medical data.

Figure 3 is a business process model of the service and the key players. The main task of investigation is shown in the central shaded box. All the other operations are necessary to support the key task. Key players passing on the supporting tasks (shown in the rounded “communication” box) are connected to the other personnel by the symbol “connector for person.” The diagram is divided into vertical columns with the actions associated with each job role appearing under the same column.

![](/api/attachments/JGT6G582/fulltext/images/08ea590c1787370401d144da8596af7155f7ec79a717175dc7d5c311763258a8.jpg)  
Figure 3. The Business Process under Review

Tasks in the radiology department are highly specialized, requiring highly trained personnel (radiologists and radiographers), professional staff (nurses), and medically unskilled personnel (orderlies, secretaries, and clerks). All personnel are assigned specific tasks associated with every investigation. For the investigation of each patient, a group of personnel (one from each discipline) assemble to form a team. Each member of the team will carry out the team's task and pass the duty down to the next member. Feedback on tasks is generally done only through informal channels.

For example, during an investigation, a radiographer, who is the technical expert, will generate the radiograph, sometimes aided by a nurse who will help with the patient. Radiologists, who are physicians, are responsible for interpreting the radiographs. When on-hand diagnosis is possible, as is the case with much of the modern equipment, a radiologist will be present to interpret the images in situ. Orderlies are required to accompany patients (a bedridden patient may require two orderlies) from the wards to the department. Secretaries are responsible for typing, filing, and sending reports. Clerks store interpreted radiographs with a copy of the report in the radiograph library and are there to retrieve them when necessary.

The department has a continual inflow of investment to replace worn-out or old equipment as well as to purchase new equipment with more modern features that will allow the department to keep abreast of the latest technology and other hospitals. The department also spends considerable resources in training students (student radiographers and doctors who are training to become radiologists) and staff (radiologists) to ensure that their active knowledge is up to date. The situation lends itself to a KNOVA case study for the following reasons:

\- While cost and expenditure, together with their monitoring and control, are the subject of much management attention, an overriding priority is concern for the soft issues associated with environments and people. Traditional manufacturing or accountancy performance measures are inappropriate for large sections of the health sector.

\- Medical teams are made up of individuals who are each highly skilled in their field and temporarily brought together for each investigation on a patient. Effective knowledge sharing is therefore an issue.

\- Medical teams are extended teams that cross departmental boundaries and involve not only staff from the radiological department but also staff from the rest of the hospital.

\- Traditional management approaches do not provide the means to assess this type of situation, and a framework such as KNOVA is necessary.

\- Management guidelines are needed for investment in the people-oriented, soft context of the team, particularly since the emphasis in a medical team together with its support is traditionally skill based.

## Management, Decision Making, and Cultural Change

Health services in the United States and Europe are the subject of scrutiny and publicity. Costs are high and continually rising. Patients are more critical of the treatment they receive. In some countries, a more “market-driven” approach to the provision and consumption of health services has been adopted. All these factors mean that more attention is being given to risk and performance issues in health management and that much of the culture in hospitals is changing.

Since the radiology department is varied in its composition, its management structure is complex. The department budget has traditionally been decided by the health authority for the governmental region where the hospital is located, although this is now arranged by the hospital management. In the past, decisions about the future of the department have been made by radiologists. Ultimate responsibility for the department is given to one of the more senior radiologists (the clinical director). Recently, however, a radiology services manager whose background is in radiography has been appointed. The manager's role is to manage the departmental budget, and most of the manager's dealings are with the radiographers. Radiologists continue to make the major strategic decisions. Income is generated for the department by performing diagnostic services for general practitioners and other hospitals.

One difficult task that departments such as this face is maintaining the quality of service, given increasingly tight budgets. There is increasing pressure on departments to provide tangible measures of performance and to show how investment will be directed to improve those areas that are weak. These needs exist against a backdrop of increasing cost consciousness due to the increasing resource limitations now being imposed. These limitations have led, for example, to reductions in the number of radiographers and more intensive attempts to save money by reducing waste.

The first major problem in this situation is that performance measures are difficult to apply to this complex system and no generally agreed performance indicators have yet been determined. Second, it is difficult to identify how the components of this system interact with each other and where suitable foci for management intervention exist. It is these types of problems that KNOVA tries to address.

## The KNOVA Application Process

## Initial Scoping

## Step 1: Specify the Scope and Objectives of the Review

A KNOVA review is a cooperative activity involving client and reviewer. It is therefore important that the review begin with commonly agreed upon boundaries and aims. The reviewer should explain the KNOVA technique to the client—for example, its complementarity to conventional BPM and its emphasis on knowledge, communication, and people. The condensed influence diagram presented earlier in Figure 1 can be used to communicate the basic notions of KNOVA. This diagram reflects the knowledge-centric focus of KNOVA and the belief that people and organizational culture factors are influential in the useful application of knowledge.

The rest of the KNOVA review is largely a process of progressively drawing out those factors present in the organizational situation that are blocking or enabling the useful application of knowledge. Once this is done, recommendations for investment in mechanisms may be made that reinforce supporting factors, introduce new ones, or subdue those that are problematic. An advantage of the technique is that it does not simply leave the client with a set of stark recommendations, but may, if desired, provide a computer-based dynamic model to be used as an ongoing guide to any change program based on the investment recommendations of KNOVA. This computer model, built up during the review, will have captured a portion of the client's understanding of the business situation that can be referred to as required.

This first stage takes the form of an initial interview with the manager in the client organization responsible for the KNOVA review to identify the points below.

\- The reason for the review—for example, is there some cause for concern? Have costs been rising? Is performance perceived to be slipping? Does training or the design of team make-up need to be improved? Unless the driving reason is identified, the review has no purpose.

\- The team(s) forming the subject of the review.

\- The teams' mission and the measures (formal and informal, personal and team) used to assess performance in meeting the mission goals.

\- The main business processes the team is required to support.

\- The formal roles and responsibilities of the team members associated with the process.

\- Any organizational changes that may be influencing the situation.

The output of this stage would typically be a definition document of a few pages. Both reviewer and client should agree on its acceptability.

## Refine the Static Model for the Current Situation

## Step 2: Development of a Business Process Model (Optional)

An optional step in the review is the construction of an orthodox process model. The act of elucidating the more easily identifiable “hard” factors can serve to clear them from the situation under consideration and so reduce the complexity of KNOVA’s main purpose—to identify the “softer” issues. Achieving this step also has the confidence-building effect of providing some commonly agreed upon deliverables between the reviewer and client.

The output from this step is typically a process model of the parties involved and the process that they serve (figure 3): in this hospital case, the ARMA technique for developing the BPM. However, KNOVA is largely independent of BPM technique and almost any recognized approach may be adopted. Implicit in this approach is the acknowledgment that no BPM method can completely and satisfactorily address the factors influencing organizational behavior and performance. Recognizing this can relieve the analyst or change team of a burdensome obligation to develop the “perfect” model.

It is possible to use KNOVA without developing a full process model and so save time and money. It may only be necessary to agree on labels for a few formal aspects of the team under examination, such as roles, responsibilities, and processes. Situations where this is the case include those where the users already know their processes well or have them optimized—BPM in this case is an inefficient use of time. This is also true in cases where the processes are complex and difficult to model, very knowledge-dependent (such as medical diagnosis), or where process structures are dynamic and constructed to fit tasks as they arise. Decision-making processes are an example of this latter case.

Step 3: Interview Subjects to Ascertain Key Influencing Factors and Adapt Base Model

In the previous two steps, knowledge about the concerns motivating the review and the business process has been gathered with the help of the client managers. The third step involves eliciting team members' concerns and assessments about the factors influencing performance within the team. A structured list of some 100 questions of the form "how important is . . . (factor) . . . to getting the job done" is used as a guide. A response between 0 and 5, where 0 indicates no importance and 5 indicates significant importance, is used as a measure of the factor's importance within the given context. The following are representative of the questions asked:

• How important are formal team meetings?

• How important are cooperative team leaders?

• How important is trust in leaders?

• How important is background (latent) knowledge?

• How important is information availability?

These questions are categorized according to the headings of Knowledge, Culture, People, Performance, Investment, and Benefits, which together form the KNOVA framework. The expanded KNOVA influence diagram (Figure 4) is a more detailed version of the top-level diagram and provides a visual representation of how the factors interrelate at this level. Again, the arrows reflect influences with O+O and O-O signs at the arrowheads indicating, respectively, a reinforcing and a lowering influence.

In practice, it is acceptable to omit questions deemed irrelevant and to pursue new lines of inquiry. Using the insight gained in the previous two stages, the reviewer can steer the subject away from fruitless lines and press for elaboration on areas known to be important. Note the subject is not being asked about the quality of a factor as it is in practice, but how important it is, in principle, to getting the job done. Through progressive development and refinement, the basic KNOVA model is molded into a picture of the important factors necessary to support the business process of the particular team and how these influence each other.

The answers can be surprising. In some situations, the popular opinion may be that “cooperative team leaders” are of little importance in getting the job done—contrary to the advice given in management textbooks! Experience shows that answers to questions can vary across different organizations but that there is normally consistency between responses of people in the same team. Current developments for KNOVA include the addition of statistical analysis to more accurately determine parameters such as range, mean, and variance of opinion when a large group is interviewed.

Figure 4. The Dynamic Model for the Case Study  
![](/api/attachments/JGT6G582/fulltext/images/34f3ba6b78625dcbb88a24f44e3bd1f97af65163647ab81369f9bfefcb035516.jpg)

Table 1. The Checklist Formulated for Team Culture

<table><tr><td colspan="2"> $Team\ culture^a$ </td><td> $Weighting^b$ </td><td>Blocker</td><td>Neutral</td><td>Enabler</td><td>Value</td></tr><tr><td>2</td><td>Openness</td><td>4</td><td>√</td><td></td><td></td><td>-1</td></tr><tr><td>2.1</td><td>Team spirit</td><td>4</td><td></td><td></td><td>√</td><td>4</td></tr><tr><td>2.2</td><td>Cooperative team members</td><td>4</td><td></td><td>√</td><td></td><td>0</td></tr><tr><td>2.3</td><td>Trust in team members</td><td>5</td><td></td><td></td><td>√</td><td>5</td></tr><tr><td>2.4</td><td>Team members open to suggestion</td><td>4</td><td>√</td><td></td><td></td><td>-4</td></tr><tr><td>2.5</td><td>Team willing to change</td><td>4</td><td></td><td>√</td><td></td><td>0</td></tr></table>

$^{a}$ Core diagnostic team (clinicians, medical team): the usual way things are done within the team. $^{b}$ 0–5 scale: 0 = no importance, 5 = important.

Step 4 : Determine Significance of Factors in Reality

For each item identified as having significance, the question is asked: "Is this factor blocking, enabling, or neutral in the current situation?" The response is interpreted as a multiplier for the weighting factor (-1 for blocker, 0 for neutral, and 1 for enabler). An example of a checklist and associated values for one section of the influence diagram (team culture) is shown in Table 1. The last column is the product of the weighting and the multiplier. A high positive figure suggests this factor is of major help in supporting the team, whereas a high negative value suggests an area of concern.

Step 3 allows the construction of an “idealized” model of the team situation based on the generalized KNOVA model and the responses of the interviewees. Step 4 tells us how reality compares with this ideal. The comparison of the two identifies points of strength and weakness in the mechanisms for supporting knowledge application and development. It can also highlight other pertinent team issues such as quality of leadership, supportiveness of the organization, and quality of reward.

Clearly, this process of progressive elucidation and assessment can be done without the aid of a computer. However, it is the automation of the process and its accessibility to line managers or project leaders that convey most benefit. Once the client has experienced the process once, a KNOVA review can become a straightforward self-assessment exercise carried out periodically as required.

## Development of the Dynamic Model

## Step 5 : Develop the Dynamic Model

Practical management involves managing change over time. Unfortunately, the time needed for changes to take effect is often difficult to judge correctly. Traditional management checklists of factors to consider are normally “flat,” paper-based representations of influencing factors and therefore are constrained as to how time can be represented. This type of medium can be too inflexible to support the development of a dynamic multidimensional view of a team and its environment as it changes over a period of time. A fuller representation requires the use of the computer. In this instance, we have adapted the EXTEND system $[13]$ .

EXTEND is a PC- or Macintosh-based simulation builder that provides a number of standard numerical simulation blocks (adders, multipliers, accumulators, etc.) from which the user may build a block-and-wire model of her or his system of interest. The graphical appearance of each block may be customized. Various other features such as hierarchical models and a control language for giving blocks sophisticated (e.g., conditional) behavior are also provided. We have used EXTEND more for its graphical and windowing capabilities than for its functional sophistication.

KNOVA leans toward qualitative rather than quantitative reasoning $[8]$ . In the absence of any practical commercial graphical qualitative simulation tool, it was easier to adapt a “traditional” numerical simulation tool such as EXTEND than to try to make use of any qualitative tools such as QSIM $[18]$ . However, the adaptation was a somewhat painful one, requiring many compromises between the principles of the KNOVA philosophy and what was practically possible.

Once we have identified the relevant concerns, their level of importance, and their status (blocker, enabler, or neutral), we are able to develop a dynamic model of the situation. This may be done using the computer model that is part of the complete KNOVA analysis package. Figure 5 shows part of the dynamic model dealing with team microculture. The “+,” “X,” “C,” and “Eqn” symbols represent adders, multipliers, calibration factors, and equation blocks. This whole entity is a subsystem of the “second-level” KNOVA model shown earlier. Having derived qualitative assessments for the various factors (Table 1 shows some of these for team culture), we then put them into the KNOVA model.

## Interpretation of the KNOVA Study

## Step 6: Experiment with Investment Options and Decide Change Needs

The comparison of the idealized team situation from step 3 with the assessment of the actual situation in step 4 highlights those areas in need of attention. Some investment initiatives for addressing these concerns will have a faster or longer-lasting effect than others. Once the dynamic model has been developed, it is possible to experiment in order to see how factors such as active and latent knowledge, cost savings, and effectiveness may change as different investment plans are proposed. Figure 6 shows outputs obtained from one such analysis.

Initial investigations led to the proposition that both costs could be saved and the quality of team actions improved if team communications were improved. A KNOVA model was developed that amplified the understanding behind this proposition and gave some insight into how investment in communications would affect the team (Figure 6). The period of interest is two years, and at the start of this period, an investment in communications is made during the second quarter (initially, the value for this investment is zero). In the background, latent knowledge is decaying with time. Active knowledge rises a little and then falls back to its original value before rising even more. Quality actions and cost saving are improving. The onset of communication-medium investment can be seen to trigger the rise in cost saving. An advantage of using a computer model is that the sensitivity analysis can be carried out by making small changes to investment options (communication-medium investment, in this case), and noting the resulting changes to the model output.

![](/api/attachments/JGT6G582/fulltext/images/85041be2de4daee16e1c0eff5892d4e30ef857e08880807f193f2537347eb23b.jpg)  
Figure 5. The Dynamic Model for Team Microculture

From this exercise, a list of areas of concern and corresponding possible actions will emerge. These may then be assessed for feasibility and prioritized according to the gravity of the concern.

## Step 7: Implement Management and Team Actions

Finally, the conclusions of the KNOVA analysis need to be implemented within the team in order for improvements to be achieved. If desired, the dynamic model can be used as a tool for tracking and assessing changes as they occur.

## Discussion and Conclusions

THE OBJECTIVE OF THE KNOVA KNOWLEDGE VALUE-ADDED FRAMEWORK is to provide a multifaceted and integrated view of the factors affecting knowledge investment decisions for individuals and teams. This assists with the following:

\- Identifying focal points for investment in both hard and soft factors.

\- Tracking the resulting performance and investigate variations.

\- Ensuring that the knowledge resources of the team are adequately managed and shared.

\- Providing explicit links between hard, quantitative factors, such as costs, and soft, people-oriented issues such as culture.

KNOVA has proved successful in identifying key areas of management concern in a hospital radiology department in a systematic way. The process of using KNOVA has articulated an understanding of the knowledge, communication, and people issues in the department and how they influence factors such as cost, decision making, and performance. KNOVA therefore helps to cement team working by making an externalized team understanding visible to all concerned. The model also demonstrates how performance improvements can be brought about by investing in the relevant areas. The forecasts from the models for the future reinforce the need to assess time-based features in the management of change.

The benefit of the KNOVA analysis has provided clearer identification and more focused directions for the department. This has reinforced our confidence in the KNOVA model and approach. In the health services there is interest in better understanding the skills mix of staff required to support operational processes more effectively. KNOVA provides a simple integrated approach to achieving this, and helps make focused investments that build up a knowledge base that directly supports the operational processes. It also provides a decision framework for investing in developing the culture of an organization—a key factor for sustained performance improvement.

![](/api/attachments/JGT6G582/fulltext/images/17dc8f7a8cbdeb5d02d20385eb25450ae0abd8d3c4a8fde60e83cc98ac1bbb16.jpg)

![](/api/attachments/JGT6G582/fulltext/images/509f8e43885395119ff99ef57d4eb80ef65570bdbb41df28e204c1687d9e9d90.jpg)  
Figure 6. Outputs from a KNOVA "What-If" Analysis

The department under examination could also have been analyzed using alternative traditional “hard” systems approaches. Here simulation or simple queuing models are used. This can be done by introducing tracking of key personnel to give an up-to-date snapshot of what happens in the department to pinpoint particular strengths and weaknesses. The problem here is that a lot of data are required to build a model and the relevance of the model to the actual issues being examined in the system may be questionable.

The model is a qualitative one, and forecasts are therefore not rigorous. This is because soft factors are included, and these cannot be specified accurately. The model data are also subjective because of the inclusion of soft factors such as culture. Hence, it is the relative changes over the period of interest rather than absolute values that give the model its value.

As organizations strive to improve business performance by better use of their assets, people and organizational culture are increasingly recognized as key factors. The development of a knowledgeable work force that can react rapidly to changing demands is essential for long-term survival. The KNOVA knowledge investment framework used here promises some ability to manage these factors and is therefore of a wider business interest.

## REFERENCES

1. Butler-Cox Foundation. The role of information technology in transforming the business: management summary. Bulter-Cox Foundation Report Series, no. 79 (January 1991).

2. Ciborra, C. Information Analysis: Selected Readings, ed. by R. Galliers. Sydney: Addison-Wesley, 1987.

3. Davenport, T., and Short, J. The new industrial engineering: information technology and business process redesign. Sloan Management Review, 11 (Summer 1990), 11–29.

4. Dennis, A.R.; Daniels, R.M.; Hayes, G.; and Nunamaker, J.F. Automated support for business process re-engineering: a case study at IBM. Proceedings of the 26th Annual Hawaii International Conference on Systems Science, January 1993.

5. Dubois, E.; Du Bois, P.; and Petit, M. Eliciting and formalizing requirements for CIM information systems. Proceedings 5th Conference in Advanced Information Systems Engineering. London: Springer-Verlag, 1993, pp. 252–275.

6. Eccles, P. Planning for improved performance. Management Accounting (January 1993), 53–54.

7. Financial Times. Knowledge is power. June 3, 1994.

8. Forbus, K.D. Qualitative process theory. Artificial Intelligence, 24 (1984), 85–168.

9. Glykas, M.; Holden, T.; and Wilhelmij, G.P. Modeling the collective behavior of organizational agents in the petrochemical industry using the agent relationship morphism methodology (ARMA). In H. Kilov and B. Harvey (eds.), Proceedings Eighth Annual Conference on Object-Oriented Programming Systems, Languages and Applications, Washington, DC, September 1993.

10. Glykas, M.; Holden, T.; and Wilhelmij, G.P. Modeling safety-critical organizational processes using the agent relationship morphism methodology (ARMA). Proceedings of the 27th Hawaii International Conference on Systems Sciences, January 1994, pp. 693–703.

11. Hand, M. Designing quality into business processes. Management Accounting (January 1991), 40–42.

12. Harrington, H.J. Business Process Improvement. New York: McGraw-Hill, 1991.

13. Hoffman, P. The EXTEND Manual. San Jose, CA: Imagine That Inc., 1992.

14. Holden, T.; Glykas, M.; Wilhelmij, P.; and Reynolds, R. LIFETRACK: organizational modeling for safety-critical decision support. Proceedings of the 2nd Safety-Critical Systems Symposium. London: Springer-Verlag, February 1994, pp. 79–102.

15. Jorysz, H., and Vernadat, F. CIM-OSA part 1: total enterprise modeling and function view. International Journal of Computer Integrated Manufacturing, 3, 4 (1990), 144–152.

16. Jorysz, H., and Vernadat, F. CIM-OSA part 2: information view. International Journal of Computer Integrated Manufacturing, 3, 4 (1990), 152–168.

17. Jorysz, H., and Vernadat, F. CIM-OSA part 3: integrating infrastructure. International Journal of Computer Integrated Manufacturing, 3, 4 (1990), 168–181.

18. Kuipers, B.J. Qualitative simulation. Artificial Intelligence, 29 (1986), 289–338.

19. Lewis, C. A source of competitive advantage. Management Accounting (January 1993), 44–48.

20. Morrow, M., and Hazell, M. Activity mapping for business process redesign. Management Accounting (February 1992).

21. Nunamaker, J.F.; Dennis, A.R.; Valacich, J.S.; Vogel, D.R.; and George, J.F. Electronic meeting systems to support group work. Communications of the ACM, 34, 7 (1991), 40–61.

22. Scherr, A.L. A new approach to business processes. IBM Systems Journal, 32, 1 (1993), 88–99.

23. Sowa, J.F., and Zachman, J.A. Extending and formalizing the framework for information systems architecture. IBM Systems Journal, 31, 3 (1992), 590–616.

24. Stein, N.S. Business Taxation, 5th ed. London: Butterworth Heinmann, 1992

25. U.K. Health and Safety Executive. Human Factors in Industrial Safety. London: U.K. Health and Safety Executive, 1993.

26. Woolfe, R. Managing and redesigning business processes to achieve dramatic performance improvements. European Business Journal (1991), 20–28.

27. Wilhelmij, G.P.; Betteridge, J.; and Holden, T. KNOVA knowledge value-added framework for performance improvement and team investment: case study: team culture on oil rigs in the North Sea, Gulf of Mexico, and Alaska. Technical Report CUED/F-INFENG/TR149. Engineering Department, University of Cambridge, September 1993.

28. Wilhelmij, G.P.; Betteridge, J.; and Holden, T. KNOVA knowledge value-added framework for performance improvement and team investment: case study: the stuck pipe awareness campaign. Technical Report CUED/F-INFENG/TR147. Engineering Department, University of Cambridge, September 1993.

29. Wilhelmij, G.P.; Betteridge, J.; and Holden, T. KNOVA knowledge value-added framework for performance improvement and team investment. Technical Report CUED/F-INFENG/TR145. Engineering Department, University of Cambridge, July 1993.

30. Zachman, J.A. A framework for information systems architecture. IBM Systems Journal, 26, 3, (1987), 276–293.
