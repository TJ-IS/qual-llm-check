---
otero_id: 5050
otero_key: "3K8HRC8X"
title: "Toward Predicting Software Development Success from the Perspective of Practitioners: An Exploratory Bayesian Model"
authors: "J Drew Procaccino; June M Verner; Marvin E Darter; William J Amadio"
year: "2005"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000044"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research article

# Toward predicting software development success from the perspective of practitioners: an exploratory Bayesian model

J Drew Procaccino<sup>1</sup>, June M Verner<sup>2</sup>, Marvin E Darter<sup>1</sup>, William J Amadio<sup>1</sup>

<sup>1</sup>Department of Computer Information Systems, College of Business Administration, Rider University, Lawrenceville, NJ, USA; <sup>2</sup>Empirical Software Engineering Programme, National Information and Communications Technology Australia, Australian Technology Park, Sydney, Australia

Correspondence: JD Procaccino, Department of Computer Information Systems, College of Business Administration, Rider University, 2083 Lawrenceville Road, Sweigart Hall, Room #315, Lawrenceville, NJ 08648, USA.

Tel: þ 1 609 896 5259

Fax: þ 1 609 896 5304

E-mail: jdproc@aol.com

## Abstract

Software development project managers may need to focus on particular issues during the development process for a variety of reasons, including limited resources. This study utilized a survey to ask software practitioners, who are at the core of development, to provide insight into some of the important early non-technical issues of software development, including those related to sponsor/senior management, customer/users and requirements management. Proposed relationships among these early items, and their relationship to software practitioners’ perception of project success, were quantitatively represented through a proposed Bayesian Belief Network. The concept of ‘success’ was derived from a pilot study of practitioners and was ‘defined’ as (a) there is a project plan, (b) the project is well planned, (c) practitioners have a sense of achievement while working on a project, (d) practitioners have a sense of doing a good job (i.e. delivered quality) while working on a project, and (e) requirements are accepted by the development team as realistic/achievable. The proposed causal model provided quantitative evidence that reaching agreement with customers/users on requirements, a high level of customer/ user participation, and users who make adequate time for requirements gathering have the largest direct impacts on project success among the investigated items. The proposed model identified the following as the critical chain of events for success: (1) Having a sponsor throughout the project, (2) users who make adequate time for requirements gathering, (3) a high level of customer/user participation in the development process, and (4) agreement on requirements between customer/users and the development team. Journal of Information Technology (2005) 20, 187–200. doi:10.1057/palgrave.jit.2000044 Published online 10 May 2005

Keywords: software; success; practitioners; motivation; team

## Introduction

he purpose of this study is to propose a model of software development project success based on data collected from software practitioners (programmers, database developers, systems analysts, etc.). Our study examines some early, non-technical aspects of the development process that may affect project success from the perspective of practitioners. Although we focus on practitioners, we certainly recognize that other project stakeholders (including senior management, project managers, customers and end-users) will perhaps have different, but certainly important, views of not only what constitutes project success, but also what specific process-related factors contribute to that success. However, the survey instrument and associated model we developed are not intended to evaluate these other perspectives.

The importance of our proposed model is that it can assist project managers in early project evaluation as it assists in the identification of those development issues that are potentially at-risk. Our research seeks to focus management attention on the importance of development process issues at an early stage. Although there is a ‘pressing’ need in industry for metrics related to improving the process of software development, ‘much academic work has concentrated on detailed code metrics’ (Fenton and Neil, 1999). Downstream problems can be avoided, or at least minimized, if problematic components receive more managerial attention early in the software development process.

Since practitioners do the development work, we have developed and utilized a definition of project success based on the perceptions of practitioners. In contrast, the widely used organizational/managerial success criteria includes meeting agreed upon business objectives/requirements on time and within budget (Pinto and Slevin, 1988; Baccarini, 1999; Linberg, 1999). (For comparison purposes, we have also included these traditional measures in our investigation.) The organizational/managerial definition has been traditionally used because, in part, it is relatively easy to measure (Pinto and Slevin, 1988), but is not always useful because quantitative measures such as schedule and budget estimates can be padded to create the illusion of success (Saarinen, 1996). In addition to shedding some light on practitioners’ perceptions of successful project development, our research has implications for the motivation of the development team, as our working definition of success includes components that are related to developer motivation, which we discuss in more detail in the section on research methods.

While some research suggests that software practitioners value ‘meeting of agreed upon business objectives’ (Linberg, 1999; Procaccino and Verner, 2002), they do not necessarily include completing a project on time and within budget as part of their project success definition (McConnell, 1996; Linberg, 1999; Procaccino and Verner, 2001). A practitioner’s perception of project success, in contrast to that of their management, tends to take a more micro-level view, as practitioners are not necessarily aware of, or involved in, all aspects of a project. At times, practitioners may even find considerable value and success in a project that is delivered late and over-budget (McConnell, 1996; Linberg, 1999). This view can be at least partially explained by an awareness that most practitioners have a general need to create things, particularly things that other people may find useful (Brooks, 1995), as the nature of development work is creative (Pressman, 1998). Defining software project success is a complicated undertaking. While there have been some studies addressing success from the perspective of software practitioners (McConnell, 1996; Linberg, 1999; Procaccino et al., 2004), this perspective has not widely explored.

In order to construct our proposed model, we investigated several other related studies in order to frame the concept of ‘success’. Several studies suggested that, in general, software development can be framed in terms of both the software development process (which contributes to or drives a ‘successful’ project), and the product/ outcome of that process (the resulting system) (McConnell, 1996; Saarinen, 1996; Baccarini, 1999; Linberg, 1999). Not surprisingly, a complete evaluation of system success requires multiple measures (Linberg, 1999), and this, of course, is a complicated undertaking. The process perspective includes the quality of project management itself and the satisfaction of project stakeholders needs as they relate to the development process (Boehm, 1981; Baccarini, 1999). The product (or outcome) perspective includes effects of the final product as they relate to meeting the goals and purpose of the system (Boehm, 1981; Baccarini, 1999), business outcomes (includes organizational items related to meeting cost, schedule and requirement goals), technical performance of the system, efficiency of the product’s operations (considering cost, time and productivity) (Subramanian and Lacity, 1997), end-user satisfaction with the completed system and the personal satisfaction of development staff (including professional growth, and being involved with challenging and interesting work) (McConnell, 1996; Linberg, 1999; Jiang and Klein, 2000). Of course, the components of process and product are intertwined, as the final product is the ultimate result of the development process itself. Saarinen (1996) conducted a particularly extensive study into evaluating information system success, which aimed to measure the ‘quality of the IS product and related services’, the ‘success of the development process’ and ‘the impact of the IS on the organization’. Saarinen’s survey instrument built on the user information satisfaction [UIS] scale, as he evaluated the development process, the use process, quality of the IS product and impact of the IS on the organization. The first two categories are associated with the process, and the second two with the product.

Importance of non-technical issues of software development Several studies suggest that failed projects suffer from poor management of non-technical, people-related problems that often occur early in the development process (McConnell, 1996; Linberg, 1999; DeMarco and Lister, 1999; Drummond and Hodgson, 2003) and the majority of unsuccessful projects tend to repeat problems that were outlined by Frederick Brooks as early as 1975 (Brooks, 1995). The importance of these early components for successful software development is reflected in studies by the Standish Group (1994) and others (Subramanian and Lacity, 1997; Keil et al., 1998; Verner et al., 1999; Schmidt et al., 2001; Procaccino et al., 2002). Non-technical, largely peoplerelated, factors can be broadly categorized as:

\- sponsor/management support and participation (people and process-related),

\- customer/user support and participation (people and process-related),

\- requirements management (people and process-related),

\- project manager and relationships with development staff (people and process-related),

\- estimation and scheduling (people and process-related),

\- the software development process itself and

\- software development personnel (people-related).

This study focuses on the first three categories in the above list: sponsor/management support and participation, customer/user support and participation, and requirements management. The Standish Group’s often-cited software development reports (1994) suggest that aspects of the development process related to these three categories are major contributors to whether a project met customer/user requirements within budget and on time, failed to meet one or more of these criteria or was cancelled. Similarly, other studies have pointed to the importance within the software development process of issues related to:

\- sponsor/senior management (Humphrey, 1989; McConnell, 1996; McKeen and Guimaraes, 1997; Subramanian and Lacity, 1997; Keil et $a l . ,$ 1998),

\- customer/users (McConnell, 1996; Amoako-Gyampah and White, 1997; Keil et al., 1998; McKeen and Guimares, 1997; Tackett and Van Doren, 1999; Schmidt et al., 2001) and,

\- requirements management (Boehm, 1981; Brooks, 1995; McConnell, 1996; Nidumolu, 1996; Keil et al., 1998; Boehm and Basili, 2001; Schmidt et al., 2001).

As a result, we consider each of these categories to include specific contributors (drivers) for the relative success of the development process. The following is a brief discussion of some of the specific items (variables) included in our investigation within each of these three categories.

Our investigation of sponsor/management support and participation included the support of a committed upperlevel (management) sponsor/champion throughout a project. A committed sponsor is important and can affect a project early and throughout the development process (McConnell, 1996; Keil et al., 1998; Schmidt et al., 2001; Procaccino et al., 2002). Keil et al. (1998) found that lack of commitment of top management was the highest ranked risk factor by ‘experienced software project managers’. Sponsor commitment can be reflected by that person’s participation in the decision-making process, which, in turn, can encourage buy-in, commitment and participation from other stakeholders, including customer/users (McKeen and Guimaraes, 1997; Procaccino et al., 2002). Sponsor participation can support more realistic scheduling and resource planning by helping to stop uppermanagement from forcing the project manager/development team to accept unrealistic schedules, changes to those schedules or other such undermining changes (McConnell, 1996; McKeen and Guimaraes, 1997). For a similar reason, participation can also help with adequate change control practices and the beneficial introduction of new development methods (McConnell, 1996). Sponsorship that does not last right through a project may contribute to delaying the project’s completion (McConnell, 1996), which can particularly be the case when the sponsorship is strong, but then does not last throughout (Rainer and Watson, 1995).

We investigated user support and participation, including a high level of confidence by the customer/users in the project manager/development team, high level of customer/ users participation during the development process, participating customers/users that stay throughout the project and customers/users that made adequate time available for requirements gathering. These components are related to the general need for ‘effective working relationships between IS professionals and their business counterparts’ (Taylor-Cummings, 1998). Practitioners have been found to consider a high level of confidence by customer/users in the project manager and team to be important to the development process and their perspective of success (Verner et al., 1999). Specifically, they mentioned that if customer/users do not have confidence in the project manager, customer/users might resist dealing with the project manager and participating in the development process (Verner et al., 1999). Conversely, a high level of confidence can support adequate communication between the project manager/team and customer/users (Verner et al., 1999), as well as realistic expectations regarding system functionality by customer/users (Procaccino et al., 2002). User participation should occur in all phases of system development (Amoako-Gyampah and White, 1997), and has been found to be related to user satisfaction (McKeen and Guimaraes, 1997) and meeting various project objectives, particularly as they relate to requirements (Ginzberg, 1981; McConnell, 1996; Hunton and Beeler, 1997; Tackett and Van Doren, 1999; Verner et al., 1999). This assertion is based on participative decision-making theory (Saleem, 1996) and the TQM philosophy of stakeholder participation (Ravichandran and Rai, 2000). Lastly, customer/users that make adequate time available for requirements gathering has implications for the quality and completeness of requirements (Glass, 1998).

Our investigation of requirements management included relative change in functional scope, agreement on requirements between customer/users and the development team, clear and complete requirements, and well-defined software deliverables. Prior work has noted the importance of a welldefined functional scope (requirements) (Rainer and Watson, 1995; McConnell, 1996; Ewusi-Mensah, 1997; Subramanian and Lacity, 1997; Glass, 1998; Keil et al., 1998; Schmidt et al., 2001). Further, Glass (2001) suggested that unstable requirements and overly optimistic schedule estimates are the two most common causes of runaway projects (i.e., those projects that far exceed their budget and time estimates, and fail to meet functionality needs). In general, changing requirements specifications is a major cause of projects that are difficult to manage (Nidumolu, 1996) and end up being over budget and late (Subramanian and Lacity, 1997). If practitioners incorrectly assume that agreement on requirements regarding project scope and functionality has been achieved between the development team and customer/users, the result is that users are dissatisfied with the completed system (Ginzberg, 1981). As noted earlier, the development team must strive to keep users in the requirements development loop, as users have the best perspective for the determination of appropriate system functionality (Clavadetscher, 1998). It is then reasonable to expect such participation will facilitate agreement on requirements between customer/users and the development team. Encouraging such participation also helps to more completely and accurately define requirements, which results in a better overall understanding of the system to be developed (McKeen and Guimaraes, 1997). Further, clear and complete requirements underpin the development of a project that ultimately meets customer needs (Nidumolu, 1996; Glass, 1998; Procaccino et al., 2002). In contrast, there is evidence that inadequate requirements gathering can be found in most project failures (Glass, 1998). Requirements management affects the cost of developing software (money, time and talent)

because adequate requirements gathering and management helps to alleviate costly rework (Boehm and Basili, 2001). Problems such as missing functionality are considerably more expensive to correct later in the development process (Boehm, 1981; McConnell, 1996). To make matters worse, unrealistic customer and user expectations often arise because projects start with incomplete requirements (Verner et al., 1999). Lastly, clear and complete requirements support well-defined software deliverables (including system functionality, screens, reports and system utilities).

The studies mentioned above all illustrate the importance of people-related non-technical components of software development, particularly those related to the early phases. Further, they support Boehm’s suggestion that, in general, ‘good people, with good skills and good judgment, are what make projects work’ (Boehm, 1991). McConnell (1996) also suggested that people are the most important element in successful development projects, as practitioners create, modify and apply the software while they interact with their management and customer/users of the system. However, people also represent the largest single cost in software development (Brady and DeMarco, 1994). Poor software development practices, particularly related to the nontechnical aspects of software development, place organizational resources, such as time, money and the talent pool of software practitioners, at risk. Practitioners become professionally unfulfilled, burned out, de-motivated and, as a result, are likely to have decreased personal productivity. This may lead to increased staff turnover, which again leads to lower (team) productivity. The end-result is that time, money and organizational goodwill are placed at further risk. Hence, it is important that management understand what is important in motivating practitioners in order to support a productive and creative work environment (McConnell, 1996). Supporting such an environment, in turn, can lower the overall risk associated with successful software development. All of this research points to the need for project managers to have some understanding of the development process from the software practitioner perspective.

We have already alluded to the people and organizational resources that can be placed at risk during software development. Managers need to be conscious of, and to attempt to remove, obstacles that may inhibit their development team’s ability to work. Managers also need to be skilled at shielding their staff from administrative concerns, acting as buffers between those doing work and other project-related concerns (Pressman, 1998). Yet, research also suggests that there is a tendency among project managers to under-manage the people-related aspects of software development and to instead focus on the technical issues, including those related to hardware and software (such as programming language and compilers) (DeMarco and Lister, 1999). Consider the following:

1. Software project managers are generally not trained to manage the job, but rather are trained, and have experience, in how the job is done (DeMarco and Lister, 1999).

2. The ‘High Tech’ illusion, prevalent in the information technology field, which suggests that anyone who is professionally involved in a relatively new technology, such as software development, believes that he or she is in an ‘intrinsically high-tech business’. As a result, there is a tendency to over-manage technical issues and to lose sight of the critical and on-going role that people play in these ‘high-tech’ businesses, particularly software practitioners. (DeMarco and Lister, 1999).

3. Managing technical issues tends to be more straightforward than managing people-related issues (DeMarco and Lister, 1999).

4. Software development is, by its very nature, a difficult, conceptual undertaking (Brooks, 1995).

Overall, the literature suggests that well-managed development projects are more likely to be perceived as successful by all stakeholders, including end-users. Further, project management affects both the current project (shortterm) and subsequent projects whose processes are influenced from lessons learned (or not) from the current project (long-term). Additionally, the success (or otherwise) of an organization’s most recently developed software projects can have an immediate effect on software practitioners and a longer-term impact on the end-users who work with the developed system on a daily basis.

In the next section, we present a brief discussion of our survey instrument, our working definition of software project success, details of our distribution method, the statistical methods we used to analyze the data collected and an evaluation of the validity and reliability of our work.

## Research methods

As mentioned earlier, our findings are based on information gathered through surveying software practitioners about recently completed development projects with which they were involved. Our review of the software project management literature suggested early, non-technical items that are important to the development process, as well as possible causal relationships amongst these items. We then investigated whether our data were in agreement with the literature through analysis of correlation, which we detail in the Data Analysis section. Next, we constructed a (admittedly simplified) Bayesian model that included items we investigated. We also explain how we chose the items included in the model in the Data Analysis section. The model is intended to serve as a mathematical representation of early software development issues that can be used to model the impact of specific items related to sponsor management support and participation, customer/user support and participation, and requirements management on project success. Through mathematically holding constant the value of a particular component(s) within our proposed model, we can isolate the impact of that item(s), and thereby demonstrate the potential ‘downstream’ implications of the actions (or inactions) of management on the development process through propagation of the associated probabilities. Such analysis facilitated the following determinations:

1. The ‘critical path’ of components that may lead to project success,

2. The general category of component (sponsor/management, customer/users or requirements management) that has the largest collective impact (both direct and indirect) on project success, and

3. The single component that has the largest impact on project success.

## Survey instrument

As noted earlier, our focus is on some of the important non-technical components of the software development process. Our survey instrument (see Appendix A) builds on work carried out by Boehm (1981), McConnell (1996), Glass (1998), Glass (1999), Linberg (1999); Procaccino and Verner (2001) and Procaccino et al. (2002), among others. Questionnaire respondents were instructed to consider a specific completed development project in which they had been professionally involved.

An analysis of the inter-correlations between our items helped us determine appropriate candidate items for inclusion in the proposed causal model used to predict project success. We point out that through our exploratory work, we are only suggesting potential causal relationships, as any analysis of correlation is certainly not sufficient to propose if causal relationships exist or not. Appropriate methodology calls for evidence that (a) the proposed cause happened prior to the effect, (b) the effect cannot be explained by one or more other influences (variables), and (c) there is a correlation between the cause and effect (i.e., when either the cause or effect ‘occurs or changes’, there is a corresponding change in the other) (Babbie, 2001).

In the sub-section, ‘Importance of non-technical issues of software development’, we included citations from the literature, as well as our previous work, as evidence of causal relationships between the specific items. These proposed causal relationships provide project managers with insight into some of the risks that can threaten the development process, as well as the resultant product (Procaccino et al., 2002); we are not evaluating the product after the project has been completed or abandoned but during its development. Our survey instrument includes components of both the software process and product from the perspective of practitioners, but has a strong emphasis on process. Our unit of measure is the software project, not the organization doing the development work, nor the individual practitioner.

## Working definition of project success

We conducted a pilot study in 2001 to identify items related to sponsor/management support and participation, customer/user support and participation and requirements management that would ‘define’ the dependent variable ‘success’ in our model. The variables identified would then represent our working definition of project success from the perspective of software practitioners. Our pilot study considered 54 project items in order to assess those components of the software development process that most affect practitioners’ perception of project success. These items were gathered through literature review and interviews with practitioners. In all, 43 IT industry professionals from the greater Philadelphia area (Pennsylvania, USA) responded to the survey. Each survey question began with the phrase, ‘It is important to your perception of project success thaty’. Responses were given on a five-point Likert scale, ranging from ‘Agree’ (5) to ‘Disagree’ (1). Our goal was to discover the following:

What are the five most important components of the software development process that practitioners consider important to project success?

We evaluated what an ‘important’ component of project success is by calculating each item’s coefficient of variation (COV), which is its standard deviation divided its mean. We then ranked the items by ascending COV, which provides a measure of relative ‘stability’ of the mean associated with each item. We acknowledge that individual items measured on a Likert scale should only be considered ordinal measures and, as a result, the calculation of standard deviation and mean is technically inappropriate. However, we used means and COVs to provide an approximate measure of relative importance. We used the items with the five lowest coefficients of variation to form a working definition of project success from the perception of software practitioners. The items include the following:

It is important to your perception of project success thaty

\- there is a project plan. (related to project management) (Standish Group, 1994; Verner et al., 1999),

\- the project is well planned (related to project management) (Standish Group, 1994, Pressman, 1998; Verner et al., 1999),

\- you have a sense of achievement while working on a project (related to personal/professional) (Boehm, 1981; Herzberg, 1987; Couger, 1988; McConnell, 1996; Taylor-Cummings, 1998; Procaccino and Verner, 2002),

\- you do a good job (i.e. delivered quality) while working on a project (related to personal/professional) (Procaccino and Verner, 2002), and

\- requirements are accepted by the development team as realistic/achievable (related to personal/professional, as well as customer/users, as they presumably supply the requirements and expect the associated functionality in the completed system) (McConnell, 1996; Pressman, 1998).

Our working definition of success points out a couple of interesting themes. Developers seem to value a wellplanned project, with some structure from start to finish, but not to the point of stifling creativity and doing quality work. Further, a few of the components mentioned above have direct implications for developer motivation. Several studies have noted the importance of having a sense of achievement as a source of motivation (Boehm, 1981; Herzberg, 1987; Couger, 1988; McConnell, 1996), as achievement is an intrinsic need that is typical of developers (McConnell, 1996). Also, it has been suggested that having a sense of doing a good job (delivering quality) is related to motivation in that developers can be motivated by ‘pride of ownership’ (McConnell, 1996). However, this means, in part, that there needs to be ‘pride in work’, and ‘most developers are motivated more by quality than by sheer output’ (McConnell, 1996). These motivating components are important to both the developing organization and the customer. There is some evidence to suggest that motivation is the single greatest contributor to staff productivity (Boehm, 1981; McConnell, 1996). Moreover, productivity has direct implications for the time needed to develop software and its associated cost. (As noted earlier, people represent the single largest cost in software development (Brady and DeMarco, 1994)).

In addition to this working definition of projects success, our proposed model also included another set of dependent variables, namely three project outcome-related aspects intended to evaluate the traditional organizational/managerial perspective of project success. These included the project was delivered on time, delivered within budget, and met customer/users requirements. We were interested in these items, which can only be evaluated after the project is completed, in order to investigate correlations between practitioners’ perception of project success (measured through our five process-related success items) and these organizational/managerial (outcome-related) aspects for the same projects (both collected through practitioners).

## Sampling frame

In an effort to contact software practitioners around the United States for our main study, we mailed requests to software project managers from 2000 organizations (randomly selected from a National database of 3714) in the spring of 2002. We asked them to encourage their development staff to respond to our Web-based survey. In addition, e-mail requests to participate in our study were sent to project managers at 168 organizations that were members of a Philadelphia-area technology council. Unique passwords were issued to contacted organizations to help insure the collection and analysis of only valid responses.

## Validity and reliability

Face validity was achieved for this study by developing the survey instrument through literature review and by piloting the survey instrument. The items categorized within management/sponsor support and participation, customer/users support and participation, and requirements management, have been widely documented in the literature as they represent important early components of the software development process (see sub-section, Importance of non-technical issues of software development). As a result, they can be considered valid predictors of project success. Since the items included in this study were based on prior relevant studies and pilot studies, we propose that there was a high level of construct validity associated with our survey instrument in regard to practitioner’s perspective of project success.

Particular considerations of external validity include the use of a large, nationwide sampling frame. However, due to our low response rate, we must conclude that our sample is not random in nature, but thorough analysis and development of our survey and pilot testing, we were able to identify and prevent post-test, researcher-based effects (bias) within the final survey instrument. There were no researcher-based effects largely because our respondents completed the survey independently of our research team. Similarly, there were no subject-related effect threats because of this independence and the assurance that their responses would be analyzed with complete confidentiality regarding both themselves and their organizations.

Our data set does not meet statistical requirements for generalizability, as it represents a single snapshot of various projects. In addition, in the interest of simplicity, we investigated process-related aspects of the software development process largely through single-item items, as opposed to the multi-item items that would support an acceptable level of reliability. As a result, we present our findings as exploratory in nature in order to test the utilization of a Bayesian model to predict the relative success of software development.

Content validity, a measure of ‘how much a measure (item) covers the range of meanings included within a concept’ (Babbie, 2001), was limited in this study due to the single-item measurement of concepts (as opposed to multiple items).

## Results

We now present our results including demographic analysis of our respondents, an analysis of investigated items, proposed causal relationships between items and Bayesian model.

## Respondents and organizational demographics

Our organizational response rate was approximately 6%, resulting in 126 responding organizations. A total of 168 usable responses from practitioners were collected. In all, 74% of respondents were male and 26% were female. This gender ratio appears to be a fair representation of the domestic software practitioner population, as an unpublished 2001 Annual Report by the Bureau of Labor Statistics indicated that nationwide, 73% of computer programmers and computer systems analysts/scientists were male. About 71% of respondents reported being between 49 years of age or less. This, too, seems to be a reasonable representation, as the Bureau of Labor Statistics reported in 2001 that nationwide, 76% of computer programmers and computer systems analysts/scientists were 44 years age or less. The mean number of years of experience of respondents as a software practitioner was about 19 years with a median of 20 (minimum 1 and maximum 42).

About 91% of respondents reported that they did not have a financial interest in the organization doing the development work (including any ownership in the organization) beyond earning a paycheck. We asked this question as we felt that respondents’ perception of project success might be influenced if a large percentage had such a financial interest. However, we found no statistical evidence of a correlation between having a financial interest and our working definition of project success. Respondents’ gender, age range and years of experience were also tested as a potential source of bias through w<sup>2</sup> analysis (Jiang and Klein, 2000). There was no evidence of a significant relationship between any of the demographic items and project success, which is an indication that no such bias was introduced by our respondents’ characteristics.

The most frequently cited developer-related (as opposed to management) project responsibilities were programming analyst (27%), programmer (21%), systems analyst (20%) and database developer (18%). Respondents could have more than one responsibility on a given project, including management. A total of 46% reported being a project manager/leader and 27% were part of senior management. (However, responses from those practitioners that reported that they had only managerial responsibilities on a given project were not included in our analysis.)

Most of the responding organizations were in the manufacturing/service industry (40%) or in educational organizations (18%). The mean number of IT employees of our organizations was 85 and the median was 50 (minimum of 15 and maximum of 1000). Projects were developed in 35 US States, plus the District of Columbia. The mean number of people (fulltime, part-time and consultants) who worked on the project was about 18 and the median was six (minimum of one and maximum of 400). The mean number of fulltime people who worked on the project was about 14 with a median of five (minimum of one and maximum of 300). About 72% of projects were new development efforts, about 25% were enhancements to existing projects and about 3% were maintenance of existing projects. About 70% of projects were intended for an in-house ‘customer’, about 16% for both an in-house and outside customer, and about 14% for only outside customers. The mean number of months to project completion was about 16 and the median was 12 (minimum of one and maximum of 73). Most of the customers were business (58%) or government (20%). Most developed systems were management information/business applications (74%) or e-commerce (15%). The mean number of project function points was about 451 and the median was 10 (minimum of three and maximum of 10,000). The mean number of project source lines of code was about 845,802 with a median of 20,000 (minimum of 75 and maximum of 10,000,000).

The next section presents details of our data analysis and findings of the study, including overviews of the analytical methods we used and results, including the proposed model.

## Data analysis

We used an analysis of bivariate correlation and ordinal regression to investigate the appropriateness of our proposed Bayesian model. These methods are briefly discussed below, along with associated results. We recognize that such an analysis only provides evidence to support an association between items, and not direct evidence of causality. However, the results of this analysis, combined with our literature review, provide the basis for our proposed probable causal relationships between specific items. The complexity of our proposed model became exponentially more complicated and more difficult to understand as we added additional items. As a result, we sought to limit the complexity of the proposed model. Several of the items investigated were not included in our model because they either had relatively weak support in the literature, were only related to the organizational/ managerial perception of success and/or resulted in causal ‘dead ends’ (i.e. did not relate, either directly or indirectly, to practitioner’s overall perception of success Q6.01).

## Bivariate correlation analysis

Items included in this model are discrete and (as noted previously) measured on a five-point (ordinal) scale. One of the appropriate tests of correlation between two ordinal items is Spearman’s test. Each set of proposed causal pairs of items included within the model were entered into the SPSS bivariate correlation analysis with two-tailed significance and any missing cases ‘excluded pairwise’. Another bivariate correlation analysis revealed a significant relationship between each of the five ‘success’ items (sense of achievement, did a good job, there was a project plan, project was well planned and requirements were accepted by team as realistic/achievable) and practitioners’ overall perception of project success. We interpreted this to mean that respondents read, understood and followed the instructions that they should only consider the five items mentioned above when considering how successful they judged a particular project.

Analysis of bivariate correlation and ordinal regression provided support for the eight proposed causal relationships. We found significant bivariate correlations between each of the proposed causal pairs of items within the model (see Figure 1). (However, most of the causal relationships embedded within the Bayesian model resulted in low to moderate levels of explained variance of the dependent items, ranging from 0.18 to 0.64, depending on the particular calculation of R<sup>2</sup>.) We then ran ordinal regressions for each of our eight proposed causal sets of items, which produced eight $R ^ { \frac { \ l } { 2 } }$ values. (SPSS provided three $R ^ { 2 }$ calculations, which in order of least conservative to most conservative was Nagelkerke, Cox and Snell, and McFadden. This study uses Nagelkerke because it has been reported to be the best representation of $R ^ { 2 }$ (Maddala, 1983)). The item sets were as follows (with associated $R ^ { \overset { . } { 2 } }$ values):

\- [Q3.03, Q4.08, Q5.05]-Q4.01 (customer/users had high level of confidence in team; 0.28).

\- [Q3.02, Q3.03, Q4.08]-Q4.02 (high level of customer/ users participation; 0.46).

\- [Q3.02, Q4.02]-Q4.03 (participating customer/users stayed throughout; 0.43).

\- [Q3.02]-Q4.08 (customers/users made adequate time for requirements gathering; 0.15).

\- [Q4.02, Q4.08, Q5.03]-Q5.02 (agreement on requirements was reached; 0.49).

\- [Q4.02, Q4.08]-Q5.03 (requirements were clear and complete; 0.28).

\- [Q4.02, Q5.01, Q5.03]-Q5.05 (requirements gathering resulted in well-defined deliverables; 0.44).

\- [Q3.02, Q4.01, Q4.03, Q5.02, Q5.05]-Q6.01 (project success; 0.32).

This analysis was followed by a goodness-of-fit test to determine if the proposed chain of eight causal pairs was more effective at predicting project success (the final dependent variable) than was simply simultaneously regressing all eight pairs of items (i.e., without regard to any correlated pairs of items). This was determined by comparing the generalized squared multiple correlation to the overall $R ^ { 2 }$ derived from running an overall ordinal regression analysis of all items (Schumacker and Lomax, 1996). The generalized squared multiple correlation utilized each of the eight $R ^ { 2 }$ values, and was calculated using Eq. (1) (subscript indicates item number from survey).

$$
\begin{array}{r l} = & 1 - (1 - R _ {4. 0 1} ^ {2}) (1 - R _ {4. 0 2} ^ {2}) (1 - R _ {4. 0 3} ^ {2}) (1 - R _ {4. 0 8} ^ {2}) \\ & \times (1 - R _ {5. 0 2} ^ {2}) (1 - R _ {5. 0 3} ^ {2}) (1 - R _ {5. 0 5} ^ {2}) (1 - R _ {6. 0 1} ^ {2}) \end{array}\tag{1}
$$

![](/api/attachments/3K8HRC8X/fulltext/images/897df65bdc58c7940b80a1c2299ddb9b901faa75d404a7b73a90cfe65285dcb2.jpg)  
Figure 1 Proposed Bayesian belief network (dotted line indicates ‘critical path’).

We found that the chain of proposed causal relationships did indeed do a better job of predicting the values of their associated dependent items than did simultaneously regressing all items in the model on the final dependent item (i.e., practitioners’ overall perception of project success) because the generalized squared multiple correlation (0.97) was greater than the overall R<sup>2</sup> (0.44). This infers that our proposed model has more predictive power than simply regressing all items on practitioners’ overall perception of project success (Q6.01).

## Bayesian belief networks

Bayesian Belief Networks (BBNs), also known as belief networks, causal networks or influence diagrams, are acyclic graphs based on conditional independence (Fenton and Neil, 2001; Neapolitan, 2004). Noted software management researchers, Norman Fenton and Martin Neil, suggest that BBN are ‘by far the best solution’ for modeling risk assessment (Fenton and Neil, 2000). A BBN is a graphic technique for displaying and identifying probabilistic relationships among proposed causal sets of items (variables). A completed BBN represents a proposed model of one or more ‘paths’ through a series of items. Probability distributions are calculated across these items. BBNs include both qualitative (dependencies among proposed causal pairs of items) and quantitative (calculated probabilities) aspects through their graphic representation. Owing to their inherent interdependencies, a change to the information (frequency) of any particular item within a Bayesian network can potentially affect other items depending on the associated relationships, whether or not they are directly or indirectly related to the updated item. One of the strengths of BBNs comes from their ability to include uncertainty (unknown information) in decision support models (reflected in correspondingly higher levels of uncertainty).

BBN’s contain nodes, their associated conditional probability tables (CPT) and arcs. A node represents an item (variable). Each node has an associated CPT, which contains a probability for each state (or value) of the item being represented, given the state(s) of its ‘parent’ node(s). As a result, the sum of all probabilities within each node (item) must be 1.0 (100%) because every possible state of that item must be represented. The probabilities associated with each dependent node are based on the conditional probabilities of the particular combined state of each parent node (Neapolitan, 2004). These probabilities can come from empirical data and/or expert opinion. Our model was populated with empirical data (provided by respondents of our survey), but as noted previously, its structure is based on expert opinion (i.e., literature review). The CPT of a node that is not directly dependent on any other items (i.e., represent a ‘root’ node) is simply the frequency of that item taking on each possible value (again, all probabilities totaling 1.00).

Through propagation, all conditional probabilities are recalculated when any of the associated probabilities are changed, either through the inclusion of additional information or through ‘artificially’ holding constant the probability of a particular item(s) for purposes of isolating the impact of that item(s) on other items within the model. This is sometimes referred to as ‘what-if’ analysis. (For example, if we assume that all projects did indeed have a sponsor throughout the project, we could isolate its effect on the amount of time users make for requirements gathering or participating customer/users staying throughout the project.) The final graphical component of a BBN is a directional arc (arrow), which is used to represent a proposed causal relationship between sets of items. The arc originates at a ‘parent’ node (shown as an oval) and end at (point to) a dependent item (also shown as an oval). For example (see Figure 1), changes in the functional scope of the project (Q5.01, which is an example of root node) influences whether requirements gathering resulted in welldefined software deliverables (Q5.05). Well-defined software deliverables, in turn, influence whether customer/ users have a high level of confidence in the project manager/development team (Q4.01). For further information on BBNs, see Neapolitan (2004).

The resulting Bayesian model is shown in Figure 1. The eleven (11) model items (each measured on a five-point scale), related through eight proposed causal relationships, resulted in 18,415 frequencies (cells). As discussed previously, our components of success include a sense of achievement, a sense of doing good job, a project with a plan, a well-planned project and a development team that accepted the requirements as being realistic and achievable. Therefore, when there was evidence in the literature that a particular component of the development process contributes to the relative success or failure of the project, we inferred a probable causal relationship between that component (acting as a ‘parent’ item) and project success (the five ‘success factors’).

The overall propagated probabilities from the model and relative frequencies from the sample are shown in Table 1. Note should be made of the relatively low counts (N) associated with responses 1, 2 and 3. In order to provide a baseline measure of the variability of the estimates in our proposed model, we constructed 95% probability intervals for each of the relative frequencies in the table. The probability interval is a Bayesian construct similar to the confidence interval of traditional statistics (Neapolitan, 2004). We began the construction assuming no prior information about the relative frequencies, that is, the frequencies of Table 1 follow the Dirichlet distribution and all combinations of relative frequencies that sum to one are equally likely. We then updated our prior distribution using the sample data and calculated the boundaries of the middle 95% of the posterior distribution for each response (also included in Table 1).

Next, we present the findings that were derived from the Bayesian model as follows:

1. An analysis was conducted to determine the composition of a ‘critical path’, that is, the causal series of items that exhibited the greatest impact on project success.

2. An investigation into which of the model’s individual items exhibited the greatest impact on project success, as measured by the probability of the item, Q6.01, equating to either 4 or 5 on a five-point Likert scale.

3. An investigation into which of the three categories of items (management/sponsor, customer/user or requirements management) exhibited the greatest impact on whether a project would be considered successful or not.

4. An evaluation of our model’s ability to predict project success from early events within the software development process.

## Identification of critical path

It is valuable to investigate which specific chain within the proposed Bayesian network demonstrated the greatest impact on practitioners’ overall perception of project success (Q6.01). This is accomplished by determining which item had the greatest impact on Q6.01 by tracing backwards through the network. This finding was made through isolating the effect of each ‘parent’ item on practitioners’ overall perception of project success. The candidate ‘parent’ items included Q3.02, Q4.01, Q4.03, Q5.02 and Q5.05. Specifically, the value of each ‘parent’ item was held to a particular value (1, 2, 3, 4 or 5) for all cases. The effect of this constraint on the final dependent item, Q6.01, was then recorded. The focus was on results associated with ‘parent’ items held to four and five (agree) and the dependent item, Q6.01, equaling four or five (‘successful’ projects).

The next step was to determine which ‘parent’ item had the greatest impact on that ‘upstream’ item, and so on. No single item exhibited an overwhelming impact on a project success. However, given the data, Q5.02, ‘Agreement on requirements reached between customer/users’ had the largest impact on Q6.01 (measured by taking the average of the probability that Q6.01 ¼ 4 and that Q6.01 ¼ 5 or 74.13%). The next step was to trace which item is the largest influencer of Q5.02. No single item exhibited an overwhelming impact on agreement between customer/ users and the development team on requirements. However, Q4.02, ‘High level of customer/user participation’ had the largest impact on Q5.02 (78.77% average probability that $\bar { \mathsf Q 5 . 0 2 } = \bar { 4 } \ \mathrm { ~ o r ~ } \ 5 )$ . Continuing in this manner, we identified five items on the critical path, which were consistent with previous studies. These items are as follows:

Table 1 Overall propagated probabilities for Q6.01, ‘Practitioners’ overall perception of success

<table><tr><td>Response</td><td>Probability</td><td>Count (N)a</td><td>Frequency percent</td><td>95% probability intervals</td></tr><tr><td>1 (disagree)</td><td>11.62%</td><td>1</td><td>0.62%</td><td>(0.0%, 2.8)</td></tr><tr><td>2</td><td>11.64%</td><td>3</td><td>1.85%</td><td>(0.2%, 4.6%)</td></tr><tr><td>3</td><td>13.25%</td><td>11</td><td>6.79%</td><td>(3.4%, 11.0%)</td></tr><tr><td>4</td><td>29.68%</td><td>82</td><td>50.62%</td><td>(42.1%, 57.3%)</td></tr><tr><td>5 (agree)</td><td>33.81%</td><td>65</td><td>40.12%</td><td>(31.9%, 47.1%)</td></tr><tr><td>Totals</td><td>100.00%</td><td>162</td><td>100.00%</td><td></td></tr></table>

<sup>a</sup>Six missing values.

\- Sponsor throughout the project (Q3.02).

\- Customers/users made adequate time for requirements gathering (Q4.08).

\- Level of customer/user participation was high (Q4.02).

\- Agreement on requirements was reached between customer/users (Q5.02).

\- Practitioners’ overall perception of project success (Q6.01).

Based on ordinal regression analysis, we determined that the critical path (shown as a dashed line in Figure 1) is composed of items that were significant predictors of their respective dependent items. This analysis was done to further test the ‘integrity’ of our proposed critical path.

## Item with largest impact on success

We then determined which single item in the model had the greatest impact (direct or indirect, ‘parent’ or dependent ‘child’ relationship) on Q6.01 (project success). We performed the same calculations of ‘average’ probability in this part of our investigation as we did when identifying the critical path (above). No single item exhibited an overwhelming impact on practitioners’ perception of project success. However, Q5.02, ‘Agreement on requirements reached between customer/users and the development team’ had the largest impact on project success, which also happened to have a direct causal connection in our model to Q6.01 (see Figure 1).

## Category of items with largest impact on success

We were also interested to know if one of the categories of items (i.e., management/sponsor, customer/user or requirements management), taken as a group, would exhibit a higher impact on project success) than the others. To make this determination, all associated items for a given category were forced to a value of ‘4’ within the Bayesian Network and then the resulting percentages of projects that were successful (equating to either ‘4’ or ‘5’) were summed. Then, each of these same items was forced to a value of ‘5’ and the resulting percentages of projects that were successful were summed. Finally, the two summed percentages were averaged to arrive at an ‘overall’ impact on project success. Using this methodology, the items associated with requirements management-related items exhibited the greatest overall impact on project success (average of 88% of the projects were considered to be a success when the associated items were held at either ‘4’ or ‘5’). Items associated with requirements management included ‘Change in functional scope’ (smaller, larger, didn’t change), ‘Agreement on requirements was reached between customer/users and the development team’, ‘Requirements were clear and complete (scope of project’s functionality was well-defined)’, and ‘Requirements gathering resulted in well-defined software deliverables (forms, reports, utilities, etc.)’. Customer/user-related items had the next highest ranking (84%) and management/sponsorrelated items (70%).

## Evaluation of model’s ability to predict project success

We evaluated our critical path model’s ability to predict project success from early events within the software development process using 10-fold cross validation (Witten and Frank, 2000). (Responses of 1, 2 and 3 were collapsed into one response category.) The model achieved a 71% average accuracy rate. To put this result in perspective, consider Table 1, which shows that 50.62% of our sample projects were rated at 4. A naı¨ve model that predicts 4 for every project will achieve 50% accuracy, so we can say our critical path model provides a 40% increase in accuracy compared with informed guessing.

## Conclusions

In general, the results produced by our proposed model agree with the current body of published, largely anecdotal research. Although the fact that our model supports these findings may not surprise many researchers and project managers, the quantitative nature of this study represents additional validation of earlier qualitative research. Further, our proposed Bayesian model proved to be a useful analytic tool for graphically depicting the probabilities associated with the components of the software development process. The model was particularly useful in isolating the impact (both direct and indirect) of specific component(s) on the likelihood of practitioners considering a project to be successful. Our model is a first step toward quantifying identified potential ‘downstream’ implications of managerial actions (or inactions) during the software development process. Combined with recent software engineering literature, the model suggests that the management (or lack of management) of components related to sponsor/champion, customer/users and requirements management can have major implications later in the development process. Our analysis identified a series of components (a ‘critical path’) that had the greatest impact on project success. In general, chronological order, this path was made up of the following factors:

1. Having a sponsor (or a ’champion of the cause’) throughout the project encourages

2. users to make adequate time for requirements gathering, which is related to

3. high level of customer/user participation in the development process (encouraged by the project manager), which makes more likely

4. agreement on requirements between customer/users and the development team. Our model suggested that this was the single most important contributor to project success. Early and on-going communication among the project manager, development team and customer/users is closely related to customer/users reaching an agreement with the development team regarding system functionality.

This critical path suggests the relative importance of an upper-management sponsor, which generally supports previously cited work by Humphrey (1989), McConnell (1996), Keil et al. (1998), Schmidt et al. (2001) and Procaccino et al. (2002). User participation, including its relationship to requirements gathering, has also been noted in several studies, including Ginzberg (1981), McConnell (1996), Amoako-Gyampah and White (1997), Hunton and Beeler (1997), Keil et al. (1998), Tackett and Van Doren (1999), Verner et al. (1999) and Schmidt et al. (2001). The importance of agreement on requirements between customers/users and the development team supports other studies, including Ginzberg (1981), and McKeen and Guimares (1997). These user-related items speak to the importance of the relationship between the development team and representatives of the business (Taylor-Cummings, 1998), which we also previously alluded to in our introductory section.

Further analysis of our proposed Bayesian model provides further evidence of the critical nature of effective requirements management, which can help alleviate some of the uncertainty associated with software development. This supports requirements management as ‘the most important of all (development) phases’ and the one that has ‘the greatest impact on future phases’ (Nidumolu (1996). Other studies have found that requirements specification and managing user requirements were the two biggest problems associated with software development (Leffingwell and Widrig, 2000) and, indeed, inadequate requirements gathering can be found in most project failures (Glass, 1998). In short, as cited previously, these requirements-related findings agreed with those of Boehm (1981), Brooks (1995), McConnell (1996), Nidumolu (1996), Keil et al. (1998), Boehm and Basili (2001) and Schmidt et al. (2001).

The results of this study can also contribute to project managers’ understanding of the importance of software practitioners’ perception of project success. As mentioned previously, practitioners do not necessarily place the same value on aspects of a given development project as does the organization or its management. In particular, management traditionally tends to place emphasis on delivering a product on time and within budget, and meeting customer/users’ requirements. However, practitioners have been shown to not place as much weight on meeting budget and scheduling goals. Rather, they tend to value aspects of the development process that are related to the following:

\- Their professional/personal experience and growth, including a sense of achievement and of doing a good job,

\- Project planning and requirements, including having a well-planned project and requirements that are accepted by the development team as being realistic and achievable).

By basing the concept of project success on what practitioners report is important to their perception of success, this research has identified those aspects of the development process that make working on a project more pleasurable and motivating for developers. Further, as mentioned in our introduction, some studies have suggested that motivation is the single greatest contributor to software development productivity (Boehm, 1981; McConnell, 1996). Productivity, in turn, has direct implications for the organization’s ability to effectively and efficiently develop software, which includes delivering completed systems that meet customer/user requirements in the shortest time and lowest cost possible. Project managers can use the findings of this study to increase the probability that the projects they manage will be successful, both from an organizational and practitioner perspective.

The logical next step will be to test our model by applying it to larger number of recently completed successful and unsuccessful development projects. If the model performs as we hope, we will then be one step closer to demonstrating causality and having a usable normative model to assist project managers along the path to reducing the risk to successful project development. Our work can also be expanded to include some of the post-project perceptions of other project stakeholders, including senior management, customers and end-users.

## References

Amoako-Gyampah, K. and White, K.B. (1997). When is user involvement not user involvement, Information Strategy: The Executive’s Journal 13(4): 40–45.

Babbie, E. (2001). The Practice of Social Research, 9th edn, Belmont, California: Wadsworth/Thomson Learning.

Baccarini, D. (1999). The logical framework method for defining project success, Project Management Journal 30(4): 25–32.

Boehm, B.W. (1981). Software Engineering Economics, Englewood Cliffs, NJ: Prentice-Hall.

Boehm, B.W. (1991). Software Risk Management: Principles and practices, IEEE Software 8(1): 32–41.

Boehm, B.W. and Basili, V.R. (2001). Software defect reduction top 10 list, IEEE Computer 34(1): 135–137.

Brady, S. and DeMarco, T. (1994). Management-aided software engineering, IEEE Software 11(6): 25–32.

Brooks Jr, F.P. (1995). The Mythical Man-Month, Reading, MA: Addison-Wesley.

Clavadetscher, C. (1998). User Involvement: Key to success, IEEE Software 15(2): 30, 32.

Couger, D. (1988). Motivators vs. demotivators in the IS environment, Journal of Systems Management 39(6): 36–41.

DeMarco, T. and Lister, T. (1999). Peopleware: Productive projects and teams, 2nd edn., New York, NY: Dorset House Publishing Co.

Drummond, H. and Hodgson, J. (2003). The Chimpanzees’ Tea Party: A new metaphor for project managers, Journal of Information Technology 18(3): 151–158.

Ewusi-Mensah, K. (1997). Critical numbers in abandoned information systems development projects, Communications of The ACM 40(9): 74–80.

Fenton, N.E. and Neil, M. (1999). Software Metrics: Successes, failures and new directions, Journal of Systems and Software 47(2–3): 149–157.

Fenton, N.E. and Neil, M. (2000). Software Metrics: A roadmap, International Conference On Software Engineering, Limerick, Ireland.

Fenton, N.E. and Neil, M. (2001). Making Decisions: Using Bayesian nets and MCDA, Knowledge-Based Systems 14(7): 307–325.

Ginzberg, M.J. (1981). Early diagnosis of MIS implementation failure promising results and unanswered questions, Management Science 27(4): 459–478.

Glass, R.L. (1998). Software Runaways, Upper Saddle River, NJ: Prentice-Hall.

Glass, R.L. (1999). Evolving a new theory of project success, Communications of The ACM 42(11): 17–19.

Glass, R.L. (2001). Frequently forgotten fundamental facts about software engineering, IEEE Software 18(3): 110–112.

Herzberg, F. (1987). One More Time: How do you motivate employees? Harvard Business Review 65(5): 109–120.

Humphrey, W.S. (1989). Managing The Software Process, New York, NY: Addison-Wesley.

Hunton, J.E. and Beeler, J.D. (1997). Effects of User Participation in Systems Development: A longitudinal field experiment, MIS Quarterly 21(4): 359–388.

Jiang, J. and Klein, G. (2000). Software development risks to project effectiveness, Journal of Systems and Software 52(1): 3–10.

Keil, M., Cule, P.E., Lyytinen, K. and Schmidt, R.C. (1998). A framework for identifying software project risks, Communications of The ACM 41(11): 76–83.

Leffingwell, D. and Widrig, D. (2000). Managing Software Requirements: A unified approach, New York, NY: Addison-Wesley.

Linberg, K.R. (1999). Software Developer Perceptions About Software Project Failure: A case study, The Journal of Systems and Software 49(2/3): 177–192.

Maddala, G.S. (1983). Limited-Dependent and Qualitative Variables In Economics, Cambridge, UK: Cambridge University Press.

McConnell, S. (1996). Rapid Development, Redmond, Washington: Microsoft Press.

McKeen, J.D. and Guimaraes, T. (1997). Successful strategies for user participation in systems development, Journal of Management Information Systems 14(2): 133–150.

Neapolitan, R.E. (2004). Learning Bayesian Networks, Upper Saddle River, NJ: Pearson Prentice Hall.

Nidumolu, S.R. (1996). Standardization, requirements uncertainty and software project performance, Information & Management 31(3): 135–150.

Pinto, J.K. and Slevin, D.P. (1988). Project Success: Definitions and measurement techniques, Project Management Journal 19(1): 67–72.

Pressman, R. (1998). Fear of Trying: The plight of rookie project managers, IEEE Software 15(1): 50–51, 54.

Procaccino, J.D. and Verner, J.M. (2001). Early risk factors for software development, in K. Maxwell, S. Oligny, R. Kusters and E. van Veenendaal (eds.) Proceedings of the 12th European Software Control and Metrics Conference in London, 2–4th April, 107–116.

Procaccino, J.D. and Verner, J.M. (2002). Software Practitioner’s Perception of Project Success: A pilot study, International Journal of Computers, The Internet & Management 10(1): 20–30.

Procaccino, J.D., Verner, J.M., Overmyer, S.P. and Darter, M.E. (2002). Case Study: Factors for early prediction of software development success, Journal of Information & Software Technology 44(1): 53–62.

Procaccino, J.D., Verner, J.M., Shelfer, K.M. and Gefen, D. (2004). What do software practitioners really think about project success: an exploratory study, Journal of Systems and Software, accepted.

Rainer, R.K. and Watson, H.J. (1995). The keys to executive information systems success, Journal of Management Information Systems 12(2): 83–98

Ravichandran, T. and Rai, A. (2000). Quality Management In Systems Development: An organizational system perspective, MIS Quarterly 24(3): 381–416.

Saarinen, T. (1996). An expanded instrument for evaluating information system success, Information & Management 31(2): 103–118.

Saleem, N. (1996). An empirical test of the contingency approach to user participation in information systems development, Journal of Management Information Systems 13(1): 145–166.

Schmidt, R., Lyytinen, K., Keil, M. and Cule, P. (2001). Identifying Software Project Risks: An international Delphi study, Journal of Management Information Systems 17(4): 5–36.

Schumacker, R.E. and Lomax, R.G. (1996). A Beginner’s Guide To Structural Equation Modeling, Mahwah, NJ: Lawrence Erlbaum Associates.

Standish Group, CHAOS,http://www.standishgroup.com/sample\_research/ chaos\_1994\_1.php,1994 (accessed 12th January 2005).

Subramanian, A. and Lacity, M.C. (1997). Managing Client/Server Implementations: Today’s technology, yesterday’s lessons, Journal of Information Technology 12(3): 169–186.

Tackett, B.D. and Van Doren, B. (1999). Process Control For Error-Free Software: A software success story, IEEE Software 16(3): 24–29.

Taylor-Cummings, A. (1998). Bridging The User-IS GAP: A study of major information systems projects, Journal of Information Technology 13(1): 29–54.

Verner, J.M., Overmyer, S.P. and McCain, K.W. (1999). In the 25 years since the mythical man-month what have we learned about project management? Information and Software Technology 41(14): 1021–1026.

Witten, I.H. and Frank, E. (2000). Data Mining, San Francisco, CA: Morgan Kaufman.

## About the Authors

J. Drew Procaccino is an Assistant Professor of Computer Information Systems in the College of Business Administration at Rider University (Lawrenceville, NJ USA). His research interests include software engineering, computer interface design, smart cards and biometrics. Dr. Procaccino has taught courses in systems analysis and design, systems development, office productivity software and business graphics.

June M. Verner is a Senior Principal Research Scientist in the empirical software engineering research program at National Information and Computing Technology Australia and conjoint Professor of Software Engineering at the University of New South Wales. Her research interests include software process improvement, software project management and software metrics. Dr. Verner has taught classes in software project management, software metrics and models, and requirements engineering.

Marvin E. Darter is an Associate Professor of Computer Information Systems in The College of Business Administration at Rider University (Lawrenceville, NJ USA) His research interests include electronic commerce, the use of Internet technology in the business environment and systems development. Dr. Darter has taught courses in electronic commerce, multimedia, office productivity software, systems analysis and design, systems development and decision support systems.

William J. Amadio is an Associate Professor of Computer Information Systems in The College of Business Administration at Rider University (Lawrenceville, NJ USA). His research interests include mathematical modelling applied to problems in bioinformatics and information retrieval. Dr. Amadio has taught courses in knowledge management, database and the business of genomics.

## Appendix A

Journal of Information Technology

Survey Instrument:

Unless otherwise noted, responses to questions from Sections 3, 4 and 5 are as follows: (Agree J5 J4 J3 J2 J1 Disagree) J Not applicable J Don’t know

## Section 1: Your Background

The remaining sections are specific to a particular completed project that you have worked on.  
```txt
Section 2: Your Background

2.01 In which state was the developing organization located?
2.02 How many IT (full-time, part-time and consultants) people participated in developing this project?
2.03 How many IT people from the previous question (Q2.03) were full-time employees?
2.04 Did you have a financial interest, other than earning a paycheck, (i.e. ownership/shares in the company, etc.) in the organization that developed this project?
2.05 What was your responsibility(s) on this project? (Check all that apply)
2.06 What was the primary nature of this project? (choose only one)
    ○ Development (of a new system)
    ○ Maintenance (of an existing system)
    ○ Enhancement (adding functionality to existing system)
    ○ Don’t know

2.07 For who was this project intended? (choose only one)
    ○ In-house customer
    ○ Customer(s) outside of your organization
    ○ Both in-house and outside customer
    ○ Don’t know

2.08 This project was: (choose only one)
    ○ Completed
    ○ Completed with reduced functional scope
    ○ Cancelled/abandoned
    ○ Don’t know
    ○ Other (please explain):

2.09 How long (calendar time) did this project take to completion (or abandonment)?
2.10 For which type of organization was this project developed, maintained or enhanced? (choose only one)
    ○ Business (for-profit)    ○ Non-profit organization    ○ Military
    ○ Government agency    ○ Consumers/mass market    ○ Don’t know
    ○ Other (please specify):

2.11 What type of system was being developed, maintained or enhanced? (Check all that apply)
    [ ] E-commerce
    [ ] Embedded
    [ ] Data communications
    [ ] Management information system/business application
    [ ] Scientific
    [ ] Systems software
    [ ] Entertainment/games
    [ ] Don’t know
    [ ] Other (please specify):

2.12 This project had approximately how many function points (as defined by your project/organization)?
2.13 This project had approximately how many source lines of code (SLOC)?
2.14 You had a sense of achievement while you worked on this project.
2.15 You did a good job (i.e. delivered quality) while working on this project.
2.16 This project was completed on time.
2.17 This project was completed within budget.
```

## Section 3: Sponsor/Management Support and Participation and Your Project

3.01 The project had an upper-level (management) sponsor/champion: J At the beginning of the project J During 1st quarter of the project J During 2nd quarter of the project J During 3rd quarter of the project J During 4th quarter of the project

3.02 There was an upper-level (management) sponsor/champion throughout this project (not necessarily the same person). 3.03 The upper-level (management) sponsor/champion was committed to this project. 3.04 The project had a project manager: J At the beginning of the project J During 1st quarter of the project J During 2nd quarter of the project J During 3rd quarter of the project J During 4th quarter of the project J Project manager never acquired J Not applicable J Don’t know

3.05 There was a project manager(s) throughout this project (not necessarily the same person).

3.06 The project manager(s) was knowledgeable/experienced overall in the application area.

3.07 Overall, the project manager(s) supported the development team.

3.08 There was an integrated project plan for this project.

3.09 Overall, this project was well planned (people, available technology, scheduling, etc.).

## Section 4: Customer/User Support and Participation and Your Project

<table><tr><td>4.01</td><td>Overall, customer/users had a high level of confidence in the project manager/development team.</td></tr><tr><td>4.02</td><td>The level of customer/users participation during the development process was high.</td></tr><tr><td>4.03</td><td>Participating customers/users stayed throughout the project.</td></tr><tr><td>4.04</td><td>Customers/users did not have realistic scheduling expectations.</td></tr><tr><td>4.05</td><td>The development team had problems due to too many customers/users participating in decision-making.</td></tr><tr><td>4.06</td><td>Customer/users provided feedback to the development team.</td></tr><tr><td>4.07</td><td>There was adequate communication between the project manager/team and customer/users.</td></tr><tr><td>4.08</td><td>Customers/users made adequate time available for requirements gathering.</td></tr></table>

## Section 5: Requirements Management and Your Project

<table><tr><td rowspan="7">5.01</td><td>How did the functional scope change from requirements gathering through to completion/abandonment?</td></tr><tr><td>○ Got much smaller</td></tr><tr><td>○ Got somewhat smaller</td></tr><tr><td>○ Did not change</td></tr><tr><td>○ Got somewhat larger</td></tr><tr><td>○ Got much larger</td></tr><tr><td>○ Don’t know</td></tr><tr><td>5.02</td><td>Agreement on requirements was reached between customer/users and the development team:</td></tr><tr><td>5.03</td><td>Requirements were clear and complete (scope of project’s functionality was well-defined).</td></tr><tr><td>5.04</td><td>Requirements were accepted by the development team as realistic/achievable.</td></tr><tr><td>5.05</td><td>Requirements gathering resulted in well-defined software deliverables (forms, reports, utilities, etc).</td></tr><tr><td>5.06</td><td>The size/complexity of the project negatively impacted requirements gathering.</td></tr><tr><td>5.07</td><td>The development team understood what customer/users wanted based on gathered requirements.</td></tr><tr><td>5.08</td><td>Overall, requirements were unstable/volatile during the development process.</td></tr><tr><td>5.09</td><td>Requirements of customer/users were met.</td></tr></table>

## Section 6: Project Success

6.01 Research suggests software practitioners often define a successful development project as one in which:

K they had a sense of achievement,

K they believed they did a good job (delivered quality),

K requirements were accepted by the development team as realistic and achievable, and,

K the project had a project plan and was well planned overall.

Overall, how well do you think this project meet the above listed criteria?
