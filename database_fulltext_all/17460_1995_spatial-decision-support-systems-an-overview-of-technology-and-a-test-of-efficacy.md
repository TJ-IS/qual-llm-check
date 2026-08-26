---
otero_id: 17460
otero_key: "VRND6X7F"
title: "Spatial decision support systems: An overview of technology and a test of efficacy"
authors: "M.D. Crossland; B.E. Wynne; W.C. Perkins"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00018-n"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spatial decision support systems: An overview of technology and a test of efficacy

M.D. Crossland $^{b,*}$ , B.E. Wynne $^{a}$ , W.C. Perkins $^{a}$

$^{a}$ Decision and Information Systems Department, School of Business, Indiana University, Bloomington, IN 47405, USA $^{b}$ Computer Information Systems Department, College of Business Administration, Southwest Missouri State University, 901 So. National Ave., Springfield, MO 65804, USA

## Abstract

A laboratory experiment was used to investigate the effects on decision-maker performance of using geographic information system (GIS) technology as a spatial decision support system (SDSS). GIS are increasingly being used for decision-making, yet research about their contributions to the performance of decision-makers has been lacking. This study makes a contribution to that apparent void. Volunteer subjects completed a site location task that required decisions to be made based upon spatially referenced information. Performance was operationalized as elapsed time and accuracy. The task environment was manipulated in two dimensions. In one dimension, task complexity was varied on two levels. In the other dimension, some subjects were provided a geographic information system as a decision aid; the rest were not. Significant differences were found between task solutions developed by SDSS users and those developed by non-SDSS users. SDSS users experienced shorter solution times and fewer errors for both levels of task complexity. The study builds upon and extends image theory as a basis for explaining efficiency differences resulting from different graphical displays of spatial information.

Keywords: SDSS; GIS; Geographic information system; Spatial DSS

## 1. Introduction

Much of the data used by businesses have one or more spatial components: customer addresses, delivery vehicle locations, site selection criteria, demographic distributions of customers, etc. Business decisions must often be made which require proper interpretation and application of these spatial components (e.g., “Which potential sites meet the size, proximity, and location parameters we have established?"). Geographic information systems (GIS) technology has been developed as a means for organizing and analysing spatial data. However, what business decision-makers actually need for such decisions are spatial decision support systems (SDSS) – “canned” software that is intuitively obvious to use, solves their specific problems efficiently, and delivers immediate results [16].

An SDSS is not the same as a GIS, although both rely on GIS technology. An SDSS is based on spatially referenced data; a GIS, on spatial data. ... Pure spatial data contain information about the relationships of entities in space. It is the information we store on maps, either as lines on paper or bits in a computer. Spatially referenced data are thematic or applied data: addresses coded by ZIP code or distribution routes planned by street address. ... SDSS offers a solution for a specific problem, whereas traditional GIS provides a highly evolved technical toolbox designed to work for multiple applications [16, p. 47].

GIS technology is both a rapidly-growing industry and a significant new approach to data management and analysis. A recent multivendor-sponsored, ten-page advertising supplement in Business Week [9] proclaimed the importance of GIS in its headline:

There's a quiet revolution going on. It's a revolution that impacts each of our lives, although few of us have heard anything about it yet.

The industry and the research community have not yet developed a standard definition of GIS. One definition which has been incorporated into at least one new GIS textbook $[2]$ has been proposed by $[29]$ , who defines a GIS as any information management system which can:

\- collect, store, and retrieve information based on its spatial location

\- Identify locations within a targeted environment which meet specific criteria

\- Explore relationships among data sets within that environment

\- Analyze the related data spatially as an aid to making decisions about that environment

\- Facilitate selecting and passing data to application-specific analytical models capable of assessing the impact of alternatives on the chosen environment

\- Display the selected environment both graphically and numerically either before or after analysis.

It is within the context of this definition that this study was formulated and grounded.

A significant amount of effort has been invested by information systems (IS) researchers in the general area of decision support systems (DSS), including the value added by DSS usage. It has been suggested [42] that the benefits of DSS usage might be divided into three groups: (1) those at the managerial level, (2) those at the operational level, and (3) those at the personal (individual user) level. The results of their study showed that users attached significantly greater importance to the personal level of benefits than to nonpersonal level benefits. If we assume that improving individual decision-maker performance is a personal-level benefit we might ascribe to a DSS, then it is worthwhile to consider to what degree any DSS, including one using GIS technology, makes such a contribution. The problem and questions investigated here involved an assessment of the value, at the individual level, of using GIS technology as a spatial decision support system, or SDSS.

A cursory review of GIS may leave the reviewer with the impression that it is simply another method of displaying information graphically, although in reality it is much more. Researchers have spent considerable effort in examining value contributions and the effects on decision-makers of varying the mode of information presentation. For example, a number of experimental studies $[1,3,4,5,6,18,19,30,31,35,39,40,58]$ have investigated the effects of colour, complexity, and form of information presentation on information extraction and decision-making. However, each of these studies was limited to investigations involving tabular information and various types of business graphs – line graphs, bar charts, pie charts, etc. An area of graphical information processing and usage which has largely been ignored is the graphical analysis of spatial information, or more specifically, computer graphic maps.

Because GIS technology provides an important way to enable such graphical analysis of spatial information, and also because the study of GIS has been ignored in IS research to date, the following problem exists with the current state of IS research:

IS research has not adequately assessed the potential contributions of GIS technology to organizational or individual decision-making.

GIS applications and usage are likely to continue to proliferate, and related research should grow as well. This study contributes to the body of knowledge about GIS in an IS context, and provides findings which support further research about the use of GIS as an SDSS.

## 1.2. The primary question in this research

For various implementations of IS and, more generally, most types of computer systems, questions are almost always asked by those who must pay for them regarding the benefits of the new systems. GIS is no different from traditional IS in this regard.

A type of research question commonly asked in the computer graphics research cited earlier might be stated as: Do decision-makers make different decisions with different types of information displays? More specifically and perhaps more pertinent, one might ask which types of displays enable decision-makers to make better decisions?

As has been pointed out earlier, GIS is not simply another alternative data display tool. It is a comprehensive set of tools for collecting, storing, retrieving, analysing, and displaying spatially referenced information. While a GIS typically includes various graphical display capabilities as part of its analytical tool kit, it is not limited to them. A typical fully-featured GIS includes a wide array of data analysis and display tools.

Commonly-available GIS features included in the experiment in this study are map overlays, thematic mapping, and area buffering. Map overlays are the capability to simultaneously display multiple “layers” of information which are common to a given location. Thematic mapping allows selective shading or colouring of areas or individual items on a map according to values contained in a linked database. Area buffering enables the user to answer, through selective colouring, shading, or highlighting, such proximity questions as, “Where are items or occurrences of a certain type that are located within a given radius of a certain location?”

As an extension of the question from graphics research stated above, the primary question addressed by this study is:

Does the addition of GIS technology to a decision-making environment affect the performance of the individual decision-maker when the decision task involves spatially referenced information?

## 1.3. Importance of the topic

This study contributes to the body of IS research by assessing the contributions made by the addition of GIS technology to a decision-making environment which includes spatially referenced information. It may be important to organizations which are contemplating investments in GIS technology to help them assess the potential benefits of such investments.

## 1.3.1. Importance to IS research

A number of prior IS research efforts in computer graphics have reported mixed results, and many cite the need for related and supporting research [21]. Empirical research on the use of maps in general (that is, paper-based or computer-based) is minimal, but the little that is available is relevant to the study of visual aids, including graphics [21]. Some of these studies have dealt with communication effectiveness of map characteristics – such as symbology, colour, and display size – in map design [12,46]. However, none of these studies have dealt with business decision-making as it relates directly to maps.

Some studies have dealt implicitly with spatially referenced tasks without actually using maps. For example, [34] used laboratory experimentation to investigate the effect of task demands and graphical format on a spatially referenced task without using a graphical representation of the spatial nature of the problem. Specific attributes of various alternative store locations were presented to experiment participants in “business graphic” bar charts, and decisions were elicited. One significant outcome from this experiment was the suggestion that future graphics research should evaluate decision accuracy and decision time jointly. The present study incorporated this suggestion as a major premise.

One author stated the urgency of this general type of investigation regarding decision-making with computer graphics:

The most urgent area of research that must be addressed is the demonstration of decision-maker productivity improvements attributable to the use of computer graphics. Studies attempting to compare tabular and graphical presentations have frequently been poorly designed and produce equivocal findings. Additional studies must be conducted, preferably in both lab and field settings. These should be designed to compare differences among individual decision-makers, and more importantly, the characteristics of the tasks facing the decision-maker [32, p. 38].

This study provides some of the needed research in the manner so clearly called for by [32].

In a very interesting Harvard Business Review article heralding “The new promise of computer graphics,” the authors [51] recognized the great potential for managers and decision-makers which would be afforded by future computer graphics applications. However, rather than a discussion of the various types of charts and graphs which would soon be available to decision-makers, practically every example cited and illustrated in that article is related to spatial analysis, geography, location selection, and other types of location-based (i.e., spatial) tasks. This piece, while somewhat prophetic with regard to present day applications of GIS, for the most part has been ignored both in citation and in spirit as a springboard for new IS research.

A notable exception to the above assertion about the ignorance of (or perhaps simply neglect of) map-based tasks in the IS research community is found in [32]. In a comparison of the various forms of applications of computer graphics in business (even citing the Harvard Business Review paper), that author asserted:

The map, perhaps more than any other chart form, gains the most from the availability of computer graphics. The time to manually produce maps has restricted their use to a limited set of well-funded applications. Computer generated maps can be developed in a fraction of the time, and quickly updated to reflect changes in boundaries or represented data [32, p. 16].

One might also infer that the decision-maker utilizing the computer graphics map would also “benefit most from the availability of computer graphics.” However, even with the above assertion appearing years ago in a special edition of a major IS journal, research about GIS from within the traditional IS community has been practically nil. This study helps fill this apparent vacuum in the body of IS knowledge.

## 1.3.2. Importance to practitioners

It may be inferred from the preceding discussion that practitioners have had to make important economic decisions without the aid of needed basic research in the area of GIS-aided decision-making. Figures from Daratech of Cambridge, Massachusetts [23] estimated that total GIS-related software and hardware expenditures for 1989 totalled well over half a billion dollars. Daratech further estimated an annual growth rate of 25 percent through 1994. An article in Fortune declared GIS one of the fastest-growing branches of computing [10].

Consultants from Andersen Consulting [43] and International Business Machines [44] have both described how GIS will be significant change agents for many types of organizations in the coming decade. There are increasing indications that GIS will be integrated with existing IS and that it will become part of enterprise-wide IS and DSS [2]. But there has been little effort expended by IS researchers in the study and evaluation of this new technology and how it might impact existing and future IS and DSS.

This study makes a significant contribution to IS and GIS practitioners who may be evaluating potential benefits of GIS implementation, including how GIS can be applied as an SDSS to traditional DSS problems.

## 2. Literature review

## 2.1. GIS research

A considerable amount of GIS research, like early IS research, is found in various conference proceedings and special publications, and thus may not be commonly available to many IS researchers. No less than five international GIS professional organizations actively sponsor annual conferences and all five of these jointly sponsor another major annual conference.

A large part of the body of knowledge in GIS has been self-reported case studies by various practitioners and consultants. Much of it focuses on physical and operational concerns of implementation. However, there have been some research works reported which considered valuation of GIS usage.

For example, [22] proposed a general heuristic for calculating benefits of better decision-making due to contributions of a GIS. It included a two-step process: (1) estimation of the effect of better decision-making (i.e., how much value would be added to the result of the decision-making process from better decision-making), and (2) estimation of the contribution of the GIS to better decision-making. This study contributes to knowledge about the second step by providing a quantification of value added by better decision-making due to GIS usage. Results were obtained in this study which show time saved and error reduction (that is, risk reduction) realized through GIS utilization, both of which are quantifiable economic components of business decision-making.

As another example, [20] pointed out the possibility that better information from a GIS can reduce risk for an organization by applying GIS in decision-making for (1) solution-finding for well-structured problems, and (2) problem-finding for ill-structured problems. The present study focused on the first of these two classes of problems through presentation of a well-structured problem to experimental subjects engaged in solution-finding. (Note: Task structure is a probabilistic characteristic [24]. That is, the greater the probability that there exists one best solution to a task, then the more structured the task is said to be. Ill-structured problems have low probabilities, and well-structured problems have high probabilities of existence of a single best answer.)

Some GIS research and practitioner-oriented reports are beginning to appear in more mainstream IS literature. For example, $[38]$ discussed GeoRoute, an SDSS/GIS for transportation applications. Also, $[25]$ provided a useful overview and glossary of GIS to the IS community. Additionally, $[14]$ introduced the potential uses of GIS in general business problems to IS practitioners.

## 2.2. Graphics / human-computer interaction research

Modern research in graphics display and information extraction dates as far back as 1927, when [55] conducted a series of experiments with school children where he varied the type of information presentation – tabular versus graphic versus textual – and asked the subjects about the quantitative content of the information.

Many studies since then have focused on various aspects of how humans interact with graphical presentations of information. A significant number of these have had the objectives of contributing to the understanding of industrial controls design and of mechanical operator reactions to various types of information presentation. For example, [57] looked at how proximity of simultaneous displays of related information affected response times of an operator. This was similar to an earlier study [36] where colour and form of projected images were manipulated. The response time and response accuracy of experimental subjects were measured.

While useful as background for consideration of the various displays a GIS is capable of producing, these studies which focused on short-term physical response to graphical stimuli are not particularly helpful to the present study. This study was more concerned with how graphical representations of problem elements and spatial relationships of real objects and phenomena contribute to the understanding and solution of problems requiring more thought and reasoning.

Some studies have reported finding relationships of display format and task complexity. For example, [59] found evidence of an interaction between report format and task complexity. Results of the present study support this finding.

A conclusion of [54] was that the use of a visual problem structuring aid promotes desired outcomes at the individual and group levels. SDSS/GIS may provide such a visual problem structuring aid to the individual decision-maker in the present study.

An important area of graphics research which assists in grounding the current study in theory and prior research is Image Theory (IT), proposed by $[7,8]$ . IT has been used as the basis of a program of research at Indiana University, particularly in a series of dissertations $[1,16,18,30,35,39,58]$ . In addition, other recent research $[52]$ has used IT as a basis for studying data extraction tasks and graphical representations.

As an illustration of the many facets of representing tabular data graphically, [8] constructed one hundred graphical representations from the same set of tabular data. The various representations were then categorized and show as two major groups of representation types (see Fig. 1). The first group of representations is in the upper part of the figure, represented by various diagrams, scatter plots, etc. All of the related research effort identified thus far has been expended in this group.

However, an opportunity was identified for this study to explore part of the other half of representation types from IT. Note that the lower half of Figure 1 is concerned exclusively with maps and cartographic representations of the same set of data. This group of representations seemed to be untouched in the IS literature. The present study has built upon this map-based group of representations to more fully explore its implications for decision-making.

IT builds on efficiency as a basic premise, defined by [8] as follows:

Efficiency is defined by the following proposition: If, in order to obtain a correct and complete answer to a given question, all other things being equal, one construction requires a shorter observation time than another construction, we can say that it is more efficient for this question.

![](/api/attachments/VRND6X7F/fulltext/images/259b2653477670f16a971b7191af6efd306ddf4fa2f8056fa3948147c3e45c86.jpg)  
Fig. 1. Types of graphic constructions (after [8]).

Two additional facets of IT were presented by [8] that have not been explored in previous works; these are the concepts of images and figurations. An image is defined as a meaningful visual form, perceptible in the minimum instant of vision. Examples of images are single graphs and single maps, from which all the information necessary for a decision can be obtained from the one graphical display. Some concepts and multifaceted graphical illustrations, however, may be too complex to be represented by single images. Therefore, constructions of multiple images are required to fully represent them, and [8] termed these constructions of multiple images figurations. It is proposed in IT that such figurations are inherently less efficient than images for answering the majority of questions which can be asked about the data they represent.

The GIS practitioner literature is replete with references to the inherent inefficiencies of having a myriad of various paper maps and map-related tabular data which must be utilized to make decisions. The promise of GIS to reduce such inefficiencies is one of its major selling points. As one example, [56] described how the Kentucky Department of Revenue literally had so many paper maps that it was physically impossible to assess taxation of its state coal reserves. GIS was employed to process the information and simplify the decision-making.

This study has built upon the concepts of images and figurations in its construction of the experimental task to be employed, and has measured the relative degree of efficiency related to such graphical constructions. The findings should contribute to an expansion of IT knowledge regarding the contribution of technologies which include computer graphics, such as GIS.

## 2.3. Decision support systems research

One may ask the question whether GIS technology can be properly applied as a DSS. [49] defined DSS as a computer-delivered decision aid system that contains data bases, model (or decision aid) bases, and interfaces and software that allow decision-makers or their assistants to use and alter the data and model bases in real time. GIS includes all these attributes, and thus may be used as a DSS or SDSS in many applications of the technology.

Discussions of DSS generally are concerned with the nature of the task and decision-making environment. Two major categories of DSS applications are generally recognized $[53]$ ; one category (see $[28]$ ) includes systems which are used in problem finding. These may require an expert component to guide the user through the solution of relatively ill-structured problems $[47]$ . On the other hand, $[45]$ described systems which are used primarily in decision-making and generally address well-structured problems $[47]$ .

A laboratory experiment was reported by $[13]$ where decision-making was tested for an ill-structured problem. The independent variables which were manipulated were presence or absence of a decision-aiding heuristic, degree of interaction between the user and the delivery device, and whether the delivery device was a computer or pencil and paper. Dependent variables were quality of performance, productivity of ideas, user confidence in the quality of his/her performance, user satisfaction with the decision aid or support system, change in user attitude about the task, and change in user attitude about computers. This study used an experimental model roughly similar to $[13]$ , except that the problem was well-structured.

## 3. Hypotheses and methodology

Earlier studies in computer graphics research and image theory indicate that some information presentations are more efficient than others for use in decision-making. GIS technology goes a step further than this consideration, however. GIS does more than simply allow the colour, style, and form of displays to be manipulated for greater efficiency of information extraction and interpretation. As was pointed out by [32], being able to electronically manipulate maps also enables new kinds of information processing and display which previously were either not possible, or were uneconomic to pursue. Thus it is proposed that there is economic benefit in using GIS technology for certain types of problems. SDSS/GIS is an enabler of better decision-making.

One of the most straightforward tests of the efficiency of a decision support system is to consider the time and accuracy with which solutions to problems are obtained. This approach was adopted for this study.

An SDSS may be considered to make a positive contribution to the decision-maker's task if it enables him or her to reach: (a) a more accurate solution, (b) a faster solution to a given problem, or (c) both of these. This study postulated that an SDSS will present more efficient graphical displays (as defined in Image Theory) than conventional paper maps, and thus it may be hypothesized that a user of SDSS will benefit from the greater efficiencies predicted by Image Theory.

The first two hypotheses tested in this study were:

H1: Decision-makers using the SDSS will solve a problem in less time than those using only paper maps for the same problem.

H2: Decision-makers using the SDSS will solve a problem with fewer errors than those using only paper maps for the same problem.

There are also efficiency questions related to problem complexity that this study addressed in an exploratory manner. One would intuitively expect decision time to increase and accuracy to decrease when the problem complexity is increased. And indeed, this was shown to be generally true by $[1,18,30,35,39,58]$ . The present study was designed to test whether this relationship also holds true for a map-based decision task. Pursuant to this purpose, the following pair of hypotheses was posed:

H3: As the problem complexity is increased, decision-makers using the SDSS will exhibit less increase in solution time than those using only paper maps for the same type of problem.

H4: As the problem complexity is increased, decision-makers using the SDSS will exhibit less decline in solution accuracy than those using only paper maps for the same type of problem.

These hypotheses implied an expected interaction between problem complexity and SDSS usage.

## Independent variables

Two independent variables were used in the study:

(1) Problem complexity. The problem complexity variable was manipulated on two levels. The first level required subjects to rank order five facility sites using three spatial criteria. The second level required rank ordering of ten facility sites using seven spatial criteria.

(2) Presence / absence of SDSS. This variable was manipulated on two levels. On one level the subjects had only paper maps and tabular data to determine a solution to the experimental problem. On the second level, subjects were additionally provided with an SDSS which displayed graphical results of common data manipulations available in most GIS.

## Dependent variables

Two dependent variables were measured and analyzed in the study:

(1) Decision time. The overall time to process the problem statement, arrive at a solution, and record the solution was measured unobtrusively by the computer used by each subject. Subjects were given an unlimited amount of time for the problem, and the start time and end time at two distinct points in the experiment were captured automatically into a database.

(2) Accuracy. The solution determined by each subject was captured directly in a database. Because the problem is objective and has a predetermined correct solution, the computers automatically scored each subject's solution against the correct solution. The nature of the task required the subjects to rank order a series of alternative facility sites based on the various spatial criteria of the task. An error score was generated by summing over the total problem the absolute number of rank positions away from the correct position that each site was placed in a subject's ranking. Because two levels of problem complexity were being considered, the error score was converted to a percentage of total possible error for comparisons across cells of the research design matrix. Total possible error is the score obtained by using the above procedure on a list which is completely reversed from the correct solution.

## Controlled variables

Variables which could have an impact on the study and therefore were controlled were:

(1) Nature of task. Each subject solved the same stated problem. Only problem complexity (number of items to rank and number of criteria to consider) and the presence or absence of a decision aid (the SDSS) were manipulated.

(2) Training. All subjects received the same training by working the same short problem. The only difference was that subjects with the SDSS available received additional instructions on how to retrieve the necessary SDSS displays from the computer.

(3) Experimental setting. All subjects participated in the experiment in the same room, under the same physical conditions. Only subjects from a single experimental design cell were using the room at any given time. A computer-equipped classroom with 31 IBM PS/2 Model 50 computers was used during the entire study. All groups used the same software for answering questionnaires and recording solutions. The GIS software used for the study was Mapinfo from Mapinfo Corporation of Troy, NY. Custom menus and decision aids, which transformed the GIS into an SDSS for the study, were designed and developed using the development language MapCode, also from Mapinfo Corporation.

(4) Solution scoring rule. All subjects employed the same point-score solution rule to solve the problem. Each site was assigned specific point values based on each criterion. The total criteria points for each site were summed, and then sites were ranked based upon the point totals.

(5) Subject pool and assignment to design cells. All subjects were recruited from various sections of the same introductory computer course. Subjects received course credit for participation in the study. Each subject was randomly assigned to one and only one of the experimental design cells.

## 3.1. Research methodology

The study involved manipulation of the availability of SDSS and the problem complexity, measurement of individual field dependence by a standard timed test, and assessment of need for cognition by a pretask questionnaire. The two dependent variables, decision time and accuracy, were measured jointly in accordance with the suggestions of previous researchers $[31,33,34]$ .

A four-cell, $2 \times 2$ factorial design was employed. The unit of analysis was the individual decision-maker. The four experimental design cells for the treatments were:

No SDSS, less complex problem
No SDSS, more complex problem
SDSS, less complex problem
SDSS, more complex problem

## 3.2. Experimental procedure

A short practice task was then given to the subjects to familiarize them with the methodology to be used, the organization of the printed materials, the nature of the task, and how to manipulate the computer to record the solution to the problem. Subjects in the two design cells with the SDSS were additionally given instructions on how to retrieve and manipulate the displays required to solve the problem.

The subjects were then administered the main problem task. The task asked subjects to assume the role of an operations analyst in an electric power company. The company desired to replace some of its older coal-fired generating stations with a new fuel cell technology which is much cleaner and more efficient. The subjects prioritized several potential sites (five in the less complex problem, ten in the more complex problem) against several criteria (three in the less complex problem, seven in the more complex problem) which had spatial components. The criteria dealt with such factors as proximity of a natural gas pipeline, regions with endangered species, proximity to parks and recreational areas, and other such spatially referenced information. The priority ranking was based on a scoring rule which assigned points to sites based on each criterion. Fig. 2 shows one of the maps considered by the group which completed the more complex problem using the SDSS.

For each of the four experimental groups, the subjects were offered a cash performance prize of \$15 for first, \$10 for second, and \$5 for third place, based first on decision accuracy, then on elapsed time as a tie breaker. The cash prizes were paid immediately upon the completion of each group's experiment. Once the subject had indicated completion of entry of the final scores and rankings, the computer automatically recorded the ending time in the database file on the subject's floppy disk.

After each subject entered the final ranking of each site, he/she was automatically administered a post-task questionnaire. This questionnaire was one of two developed for this study. Subjects who did not use the SDSS answered 32 questions designed to evaluate the four constructs of user solution confidence, level of motivation, user process satisfaction, and subject attitude toward computers in general. Subjects who used the SDSS displays answered 46 questions, which included all of the 32 questions of the non-SDSS group, but added two additional constructs related to the computer graphics displays: ease of use and level of use relative to the paper maps.

![](/api/attachments/VRND6X7F/fulltext/images/2e146ebc73deb4792e96615d6d6cc9219097a3096a05bd01cb6890fb119c2162.jpg)  
Fig. 2. More complex problem population/major markets criterion SDSS screen.

Table 1  
Mean solution times in minutes

<table><tr><td>Solution times/ standard dev</td><td>Low complexity</td><td>High complexity</td><td>Row averages</td></tr><tr><td>No SDSS</td><td>14.6/3.08</td><td>35.6/10.00</td><td>25.1/6.54</td></tr><tr><td>SDSS</td><td>13.1/3.08</td><td>30.2/8.76</td><td>21.7/5.92</td></tr><tr><td>Column averages</td><td>13.6/3.08</td><td>32.9/9.38</td><td></td></tr></table>

## 4. Analysis

The research design follows Campbell and Stanley's Design 6 [11], the posttest-only control group design, with two dimensions of manipulated factors. An analysis of variance statistical model, as recommended by [11] for such designs, was employed as the primary model for comparing the means of the dependent variables. A total of 142 subjects completed the experiment, including 88 men and 54 women.

For the two performance measures of solution time and accuracy, the scores in the four experimental treatment groups are listed in Table 1 and Table 2, respectively. There were no significant correlations between any of the variables, so multicollinearity did not pose any problems for the analysis.

## 4.1. Analysis for SDSS usage and problem complexity

The first phase of analysis focused on determining the relationships of the treatment variables, SDSS usage and problem complexity, to the two dependent variables, solution time and accuracy. Analysis of variance was the primary investigative tool. Because cell sizes were not equal in the ANOVA, additional confirmatory analyses were done using an independent sample t-test comparison of means, which is not sensitive to differences in cell sizes.

Percent error was used for comparisons across different-complexity problems. Because there can be problems associated with using percentages or other ratios in ANOVA [48], a separate analysis was performed using an arcsine transform of the percent error. Aside from very slightly increasing the significance of the results, the analysis outcomes were identical. Therefore, the ANOVA results obtained from the percentage data are reliable.

## 4.1.1. Analysis of variance

For the research designed employed in this study, [11] recommended analysis of variance (ANOVA) as one of the most powerful analysis techniques. Therefore, hypotheses H1 and H2 were initially tested using ANOVA.

Table 3 shows the results of the ANOVA for solution time, while Table 4 shows the results of the ANOVA for percent error.

Because there were significant main effects in the ANOVA on both solution time and percent error for the availability (or not) of SDSS, Hypotheses H1 and H2 were supported. There was a significant interaction of SDSS availability and problem complexity for time (p < .10), so hypothesis H3 was supported. Hypothesis H4 was not supported. Assuming a large effect size for solution time (because of the small residual) and a medium effect for percent error, and using the tables from Cohen [15], the ANOVA tests have statistical power of approximately 0.99 and 0.70, respectively.

Table 2

<table><tr><td colspan="4">Mean percent error</td></tr><tr><td>Percent error/standard dev</td><td>Low complexity</td><td>High complexity</td><td>Row averages</td></tr><tr><td>No SDSS</td><td>8.1/18.26</td><td>8.2/7.55</td><td>8.2/12.91</td></tr><tr><td>SDSS</td><td>0.0/0.00</td><td>2.8/3.85</td><td>1.4/1.93</td></tr><tr><td>Column averages</td><td>4.1/9.13</td><td>5.5/5.7</td><td></td></tr></table>

Table 3  
Results of ANOVA for solution time (minutes)

<table><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>p</td></tr><tr><td>Problem complexity (A)</td><td>12828.1</td><td>1</td><td>12828.1</td><td>275.54</td><td>0.000</td></tr><tr><td>SDSS availability (B)</td><td>392.1</td><td>1</td><td>392.1</td><td>8.42</td><td>0.004</td></tr><tr><td>A X B</td><td>136.0</td><td>1</td><td>136.0</td><td>2.92</td><td>0.090</td></tr><tr><td>Residual</td><td>6424.7</td><td>138</td><td>46.6</td><td></td><td></td></tr><tr><td>Total</td><td>19780.9</td><td>141</td><td></td><td></td><td></td></tr></table>

Table 4  
Results of ANOVA for percent error

<table><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>p</td></tr><tr><td>Problem complexity (A)</td><td>79.0</td><td>1</td><td>79.0</td><td>0.76</td><td>0.384</td></tr><tr><td>SDSS availability (B)</td><td>1659.5</td><td>1</td><td>1659.5</td><td>16.00</td><td>0.000</td></tr><tr><td>A X B</td><td>63.8</td><td>1</td><td>63.8</td><td>0.62</td><td>0.434</td></tr><tr><td>Residual</td><td>14312.4</td><td>138</td><td>103.7</td><td></td><td></td></tr><tr><td>Total</td><td>16114.7</td><td>141</td><td></td><td></td><td></td></tr></table>

Table 5  
Independent samples T-test of solution time (minutes) for SDSS vs. no SDSS on low complexity problem

<table><tr><td rowspan="2">Group</td><td rowspan="2">N</td><td rowspan="2">Mean</td><td rowspan="2">Std dev</td><td colspan="5">Pooled variance estimate</td></tr><tr><td>F</td><td>p</td><td>t</td><td>df</td><td>1-tail p</td></tr><tr><td>SDSS</td><td>38</td><td>13.1</td><td>3.076</td><td>1.00</td><td>1.00</td><td>2.08</td><td>73</td><td>0.021</td></tr><tr><td>No SDSS</td><td>37</td><td>14.6</td><td>3.075</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 6  
Independent samples T-test of solution time (minutes) for SDSS vs. no SDSS on high complexity problem

<table><tr><td rowspan="2">Group</td><td rowspan="2">N</td><td rowspan="2">Mean</td><td rowspan="2">Std dev</td><td colspan="5">Pooled variance estimate</td></tr><tr><td>F</td><td>p</td><td>t</td><td>df</td><td>1-tail p</td></tr><tr><td>SDSS</td><td>34</td><td>30.2</td><td>8.76</td><td>1.31</td><td>0.450</td><td>2.35</td><td>65</td><td>0.011</td></tr><tr><td>No SDSS</td><td>33</td><td>35.6</td><td>10.00</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 7  
Independent samples T-test of percent error for SDSS vs. no SDSS on low complexity problem

<table><tr><td rowspan="2">Group</td><td rowspan="2">N</td><td rowspan="2">Mean</td><td rowspan="2">Std dev</td><td colspan="5">Pooled variance estimate</td></tr><tr><td>F</td><td>p</td><td>t</td><td>df</td><td>1-tail p</td></tr><tr><td rowspan="2">SDSS</td><td rowspan="2">38</td><td rowspan="2">0.0</td><td rowspan="2">0.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>*</td><td>*</td><td>2.70</td><td>36.0</td><td>0.005</td></tr><tr><td>No SDSS</td><td>37</td><td>8.1</td><td>18.26</td><td></td><td></td><td></td><td></td><td></td></tr></table>

\* F-value is undefined due to zero variance in the SDSS case

Table 8  
Independent samples T-test of percent error for SDSS vs. no SDSS on high complexity problem

<table><tr><td rowspan="2">Group</td><td rowspan="2">N</td><td rowspan="2">Mean</td><td rowspan="2">Std dev</td><td colspan="5">Pooled variance estimate</td></tr><tr><td>F</td><td>p</td><td>t</td><td>df</td><td>1-tail p</td></tr><tr><td>SDSS</td><td>34</td><td>2.8</td><td>3.85</td><td rowspan="2">3.84</td><td rowspan="2">0.000</td><td rowspan="2">3.69</td><td rowspan="2">47.3</td><td rowspan="2">0.001</td></tr><tr><td>no SDSS</td><td>33</td><td>8.2</td><td>7.55</td></tr></table>

## 4.1.2. Independent sample t-tests

The hypotheses were initially tested using univariate analysis of variance. As a confirmatory (albeit less powerful) test of hypotheses H1 and H2, simple one-tailed, independent sample t-test comparisons of mean solution times and percent error were examined for same-complexity problems. Tables 5 through 8 show the results of these analyses. The tables for solution time (5 and 6) show a pooled variance estimate because the significance of the F value is large (p > .05). The tables for percent error (7 and 8) show a separate variance estimate because the significance of the F value is small (p < .05). The approach follows standard practice [50].

All of the tests in Tables 5 through 8 are significant (p < .05). Therefore, the ANOVA results are confirmed and hypotheses H1 and H2 are supported.

## 4.1.3. Discussion

As stated in the introduction, GIS is a rapidly emerging technology which shows considerable promise as a decision support aid when the decisions to be made involve spatial information. Much of the information used in business has either explicit or implicit spatial components, such as addresses of customers, distribution of market segments, locations of mobile inventory and equipment, relevant political and regulatory zone boundaries, and distribution and transportation networks. Even though GIS has become readily available to both private and public organizations to manage and analyze such a myriad of spatial information, there has been a lack of basic research about the contributions of GIS to improved decision-making.

By examining how two major components of decision-making, decision time and accuracy, vary with the use of a GIS as an SDSS, this study contributes to knowledge about the value of such systems. This approach is congruent with that recommended by previous research in information systems $[31,33,34]$ . This study found that the addition of SDSS to the decision environment reduced decision time and increased accuracy for both of the problem complexity levels used in the study.

## 5. Conclusions

## SDSS use

The study found unequivocal evidence that addition of GIS technology to the decision environment for a spatially referenced decision task reduced the decision time and increased the accuracy of individual decision-makers. This evidence has both theoretical and practical significance.

Using an SDSS enabled decision-makers to complete the task in less time, possibly for three reasons. First, the SDSS provided interactive, colour graphical displays of the information rather than only the static, black-and-white information provided to subjects who had no SDSS. Other studies $[3,4,5,6,30,31]$ found that differences in performance related to type of display are to be expected. The present study is congruent with the prior research in this regard.

Second, and probably more importantly, the SDSS provided more efficient displays, in accordance with Image Theory (IT). A taxonomy was provided for IT by [8] for categorizing graphical displays as either images or figurations. An image is a minimum graphical form which is singly sufficient to answer a question posed about the information it contains. More complex data and concepts may require more complex graphical representations involving two or more images in order to answer a particular question. These collections of images to answer certain questions are called figurations in IT, and are inherently less efficient than images for answering such questions, according to IT. Subjects using only paper maps and tabular information had to solve parts of the task using figurations. Subjects using the SDSS, on the other hand, were able to use images for the same parts because the GIS technology essentially collapsed the figurations into images. The resulting images were simpler and more efficient than the figurations used by subjects who had no SDSS. The results obtained in the study bear this out.

Third, the more efficient (and perhaps more interesting) information presentation afforded by the SDSS enabled a better grasp of the task due to better visualization of the problem to be solved. This in turn contributed to greater performance efficiencies for subjects. The importance of problem visualization is discussed by $[54]$ .

These efficiencies predicted by IT also should increase the accuracy of subjects. This was shown to be true in this study. Although $[8]$ did not specifically address accuracy in his discussion of images and figurations in IT, other researchers $[31,33,34]$ pointed out the need and desirability of including both time and accuracy in any study related to the performance of decision-makers using graphical information. Therefore, the conclusions of these researchers may be combined with those of IT with regard to graphic display efficiency.

By taking an integrated approach and including both time and accuracy as components of graphical display efficiency, this study has shown that an SDSS makes positive contributions to decision-maker performance, as evidenced by lower solution times and greater accuracy.

## Interaction of SDSS with task complexity

The first author has considerable practitioner experience in the design and use of GIS technology for problem solving. An interesting observation during much of this experience was an apparent increase in human problem solving capacity associated with the use of a GIS. It appeared, from informal observation, that users of a GIS actually improved their problem solving capacity for the type of problem addressed by the GIS.

One outcome of this effect seemed to be that the GIS users experienced a lesser performance penalty (i.e., increase in time, decrease in accuracy) associated with more complex problems than nonusers of GIS. This in turn implied some interaction of GIS usage and task complexity.

This study provided some evidence for the hypothesized interaction of SDSS usage and task complexity. The interaction was significant for solution time (p < 0.10). It is possible that, while the two levels of task complexity employed in this study were sufficient to observe the main effects of SDSS usage and problem complexity, they may have encompassed too little difference in problem complexity to observe the hypothesized interaction with a higher level of significance. A later study will extend the present one by adding an additional level of complexity; this will permit a more complete investigation of the hypothesized interaction.

This interaction may hold considerable importance for practitioners, especially if it can be shown to be even more significant in the later study. Vendors of GIS technology are quick to point out the anticipated efficiency gains a purchaser may expect when implementing an SDSS/GIS. This study has shown that there are indeed performance gains associated with the use of SDSS. However, an interaction of SDSS usage and task complexity could indicate that SDSS usage enables decision-makers to extend the range of problem complexity which may be addressed. It may be that SDSS usage can facilitate solution of problems which were not solvable with previous manual methods. This was actually observed by the first author in previous practitioner experience. Further study is warranted to validate and quantify this observation.

## 5.1. Limitations

This study has at least two limitations. First, the task was specialized, and thus the results may not be generalizable to other less specialized tasks, although at least some generalizability to other spatial tasks is expected.

Second, the subjects were college sophomores. Generalizability of results obtained using such surrogate decision-makers has been questioned [27]. However, the validity of using sophomores as surrogates for more experienced decision-makers has been defended in the literature [26]. Additional work is required to confirm the validity of using sophomores as surrogate decision-makers for spatial tasks.

## 5.2. Future directions

This study points to additional research which should be undertaken. Of most interest at the present time is further exploration of the hypothesized interaction of SDSS usage with problem complexity. Because the present study did lend some support for the interaction, it is proposed to extend the study by testing another level of complexity in order to more fully test this interaction. It is anticipated that if enough complexity can be designed into the task, then a test for this interaction should show significant differences.

The study should be repeated or extended using more mature decision-makers. An extension to this study is planned utilizing graduate students or practitioners as subjects in order to test the effects of age and experience.

In the course of this study, additional data related to accuracy was collected from each subject for later analysis. That is, the point value assigned by each subject to each site based on each criterion was captured as part of the data collection. It now remains to analyze these data to see what types of displays showed the lowest accuracy across the subjects, and how the task and individual characteristics relate to differences in accuracy.

Additionally, a post-task questionnaire was administered in this study to each subject to assess such factors as decision-maker confidence, user process satisfaction, and individual level of motivation for the problem. Analysis of these data is needed to relate the factors to the task and individual characteristics.

Finally, this study has established a task environment and experimental methodology which can be applied to other similar tasks. Additional tasks should be developed and tested in order to test the generalizability of the results of the present study.

## Acknowledgement

An earlier version of this paper was presented at the second annual conference of the International Society for Decision Support Systems in Ulm, Germany, June 1992.

## References

[1] T.B.A. Addo, Development of a valid and robust metric for measuring question complexity in computer graphics experimentation, Unpublished doctoral dissertation (Indiana University, Bloomington, 1989).

[2] J.C. Antenucci, K. Brown, P.L. Croswell, and M.J. Kevany, Geographic Information Systems: A Guide to the Technology, (New York: Van Nostrand Reinhold, 1991).

[3] I. Benbasat and A.S. Dexter, An experimental evaluation of graphical and colour-enhanced information presentation, Management Science, 31(11), pp. 1348–1364 (1985).

[4] I. Benbasat and A.S. Dexter, An investigation of the effectiveness of colour and graphical information presentation under varying time constraints, MIS Quarterly, 9(1), pp. 59–83 (1986).

[5] I. Benbasat, A.S. Dexter, and P. Todd, The influence of colour and graphical information presentation in a managerial decision simulation, Human-Computer Interaction, 2, pp. 65–92 (1986).

[6] I. Benbasat, A.S. Dexter, and P. Todd, An experimental program investigating colour-enhanced and graphical information presentation: an integration of the findings, Communications of the ACM, 29(11), pp. 1094–1105 (1986).

[7] J. Bertin, Semiologie Graphique, (Paris: Mouton-Gautier, 1967).

[8] J. Bertin, Semiology of graphics: Diagrams, networks, maps. Trans. W.J. Berg, (Madison: University of Wisconsin Press, 1983).

[9] Business Week, pp. 69–78 (July 1, 1991).

[10] G. Bylinsky, Managing with electronic maps, Fortune, pp. 237–254. (April 24, 1989).

[11] D.T. Campbell and J.C. Stanley, Experimental and Quasi-Experimental Designs for Research. (Boston: Houghton Mifflin Company, 1963).

[12] H.W. Castner and A.H. Robinson, Dot area symbols in cartography: The influence of pattern on their perception, Technical Monograph No. CA-4, (Washington, DC: American Congress on Surveying and Mapping, Cartography Division, 1969).

[13] W.L. Cats-Baril and G.P. Huber, Decision Support Systems for ill-structured problems: an empirical study, Decision Sciences, 18, pp. 350–372 (1987).

[14] D. Churbuck, Geographics, Forbes, pp. 262–267 (January 6, 1992).

[15] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, (Hillsdale, NJ: Lawrence Erlbaum Associates, 1988).

[16] D.F. Cooke, Spatial Decision Support System: not just another GIS, Geo Info Systems, 2(5), pp. 46–49 (1992).

[17] M.D. Crossland, Individual decision-maker performance with and without a geographic information system: an empirical investigation, Unpublished doctoral dissertation (Indiana University, Bloomington, 1992).

[18] L.R. Davis, The effects of question complexity and form of presentation on the extraction of question-answers from an information presentation, Unpublished doctoral dissertation (Indiana University, Bloomington, 1986).

[19] L.R. Davis, Report format and the decision-maker's task: An experimental investigation, Accounting, Organizations, and Society, 14(5/6), pp. 495–508 (1989).

[20] W.H.E. De Man, Establishing a geographical information system in relation to its use: A process of strategic choices, International Journal of Geographical Information Systems, 2(3), pp. 245–261 (1988).

[21] G. DeSanctis, Computer graphics as decision aids: directions for research, Decision Sciences, 15, pp. 463–487 (1984).

[22] H.J. Dickinson and H.W. Calkins, The economic evaluation of implementing a GIS, International Journal of Geographical Information Systems, 2(4), pp. 307–327 (1988).

[23] S.M. Deyo, GIS maps new horizons, Microcad News, 6(9), pp. 27–31 (September, 1991).

[24] R.H. Doktor, On the commonality of creative products in the arts and sciences, Journal of Creative Behaviour, 3, pp. 90–94 (1969).

[25] C. Franklin, An introduction to geographic information systems: linking maps to databases, Database, pp. 12–21 (April, 1992).

[26] J. Greenberg, The college sophomore as guinea pig: setting the record straight, Academy of Management Review, 12 (1), pp. 157–159 (1987).

[27] M.E. Gordon, L.A. Slade, and N. Schmitt, The “science of the sophomore” revisited: from conjecture to empiricism, Academy of Management Review, 11 (1), pp. 191–207 (1986).

[28] M. Goul, B. Shane, and F. Tonge, Designing the expert component of a decision support system, Paper delivered at the ORSA/TIMS annual meeting, San Francisco (1984).

[29] F. Hanigan, GIS by any other name is still... The GIS Forum, 1, p. 6 (1988).

[30] E.D. Hoadley, The effects of colour and performance in an information extraction task using varying forms of information presentation, Unpublished doctoral dissertation (Indiana University, Bloomington, 1988).

[31] E.D. Hoadley, Investigating the effects of colour, Communications of the ACM, 33(2), pp. 120–139 (1990).

[32] B. Ives, Graphical user interfaces for business information systems, MIS Quarterly, Special Issue, pp. 15–42 (1982).

[33] S.L. Jarvenpaa and G.W. Dickson, Graphics and managerial decision-making: research based guidelines, Communications of the ACM, 31(6), pp. 764–774 (1988).

[34] S.L. Jarvenpaa, The effect of task demands and graphical format on information processing strategies, Management Science, 35(3), pp. 285–303 (1989).

[35] E.R. Joyner, The development of a metric for assessing the information complexity of time-series business graphs, Unpublished doctoral dissertation (Indiana University, Bloomington, 1989).

[36] S.W. Keele, Effects of input and output modes on decision time, Journal of Experimental Psychology, 85(2), pp. 157–164 (1970).

[37] W.R. King and J.I. Rodriguez, Evaluating Management Information Systems, MIS Quarterly, 2(3), pp. 43–51 (1978).

[38] G. Lapalme, J. Rousseau, S. Chapleau, M. Cormier, P. Cossette, S. Roy, GeoRoute: A geographic information system for transportation applications, Communications of the ACM, 35 (1), pp. 80–88 (1992).

[39] T.W. Lauer, The effects of variations in information complexity and form of presentation on performance for an information extraction task, Unpublished doctoral dissertation (Indiana University, Bloomington, 1986).

[40] M.J. Liberatore, G.J. Titus, and P.W. Dixon, The effects of display formats on information systems design, Journal of Management Information Systems, 5(3), pp. 85–99 (1988).

[41] H.C. Lucas, Jr., Performance and the use of an information system, Management Science, 21(8), pp. 908–919 (1975).

[42] A. Money, D. Tromp, and T. Wegner, The quantification of decision support within the context of value analysis, MIS Quarterly, 12(2), pp. 223–236 (1988).

[43] J.F. Nelson, GIS as change agent – friend or foe? GeoInfo Systems, 1(7), pp. 12–20 (July, 1991).

[44] S. Perkins, Down with deja vu: how to make change stick, GeoInfo Systems, 1(5), pp. 10-18 (May, 1991).

[45] W. Reitman, Applying artificial intelligence to decision support, In M.J. Ginzberg, W. Reitman, and E. Stohr (Eds.), Decision Support Systems (Amsterdam: North-Holland Publishing Company, 1982).

[46] W.D. Schontz, G.A. Trumm, and L.G. Williams, Colour coding for information location, Human Factors, 13(3), pp. 237–246 (1971).

[47] H. Simon, The new science of management decisions. (New York: Harper and Row 1960).

[48] R.R. Sokal and F.J. Rohlf, Biometry: The principles and practice of statistics in biological research. (San Francisco: W.H. Freeman and Company, 1969).

[49] R.H. Sprague, Framework for DSS, MIS Quarterly, 4(4), pp. 1–26 (1980).

[50] SPSS-X Advanced statistics guide (Chicago: SPSS, Inc., 1988).

[51] H. Takeuchi and A.H. Schmidt, The new promise of computer graphics, Harvard Business Review, pp. 122–131 (January/February, 1980).

[52] J.K.H. Tan and I. Benbasat, Processing of graphical information: A decomposition taxonomy to match data extraction tasks and graphical representations, Information Systems Research, 1(4), pp. 416–439 (1990).

[53] E. Turban and P.R. Watkins, Integrating expert systems and decision support systems, MIS Quarterly, 10(2), pp. 120–136 (1986).

[54] M. Venkatesh, and J.C. Verville, Problem formulation and representation in GDSS: a functional perspective. Working paper (Syracuse University, Centre for Science and Technology) submitted to IEEE Transactions on Systems, Man, and Cybernetics, 1992).

[55] J.N. Washburne, An experimental study of various graphic, tabular and textual methods of presenting quantitative material. The Journal of Educational Psychology, 18(6), pp. 361–376 (1927).

[56] S.A. Weber, A Geographic Information System approach to unmined mineral tax assessment, Proceedings of the 1990 Annual Conference of the Urban and Regional Information Systems Association, (1) pp. 25–28 (1990).

[57] C.D. Wickens and A.D. Andre, Proximity compatibility and information display: Effects of colour, space, and objectness on information integration, Human Factors, 32(1), pp. 61–77 (1990).

[58] K.H. Yoo, The effects of question difficulty and information complexity on the extraction of data from an information presentation. Unpublished doctoral dissertation (Indiana University, Bloomington, 1985).

[59] R.W. Zmud and R.P. Moffie, The impact of colour graphic report formats on decision performance and learning, Proceedings: International Conference on Information Systems, pp. 179–193 (1983).

![](/api/attachments/VRND6X7F/fulltext/images/ed210859ef8932167aacba5e4cdc1254795c31dd27113fd95585203d390b88f5.jpg)  
Martin D. (Marty) Crossland is Assistant Professor of Computer Information Systems in the College of Business Administration, Southwest Missouri State University. He holds the Ph.D. degree [MIS] from Indiana University. Dr. Crossland has published papers in Small Group Research, Technology Studies in the Proceedings of the Hawaii International Conference on Systems Sciences, and has presented papers at a number of  
national and international conferences.

![](/api/attachments/VRND6X7F/fulltext/images/4e97ea3129143b87edf1e76cb5bde97754386e5f1fb168d24db1a5c71d375ba2.jpg)  
Bayard E. (Bye) Wynne was Professor of Decision and Information Systems and former Director of the Institute for Research on the Management of Information Systems (IRMIS) in the School of Business, Indiana University – Bloomington. He held the Ph.D. degree [Management (Information Systems and Psychology)] from the University of Minnesota. Dr. Wynne published numerous articles and papers in MIS Quarterly, Small Group

Research, and other journals prior to his very untimely death in 1993. His co-authors in this paper very respectfully dedicate it to his memory. He is sadly missed by a legion of colleagues and former doctoral students.

![](/api/attachments/VRND6X7F/fulltext/images/5fc118a3bcc18a090b742558e6cfc1127b0b238cc3f85871a903efc8a345c508.jpg)

William C. (Bill) Perkins is Professor of Decision and Information Systems and present Director of the Institute for Research on the Management of Information Systems (IRMIS) in the School of Business, Indiana University - Bloomington. He holds the D.B.A. degree [Quantitative Analysis] from Indiana University, and has published papers in Decision Sciences, Applied Economics, Journal of Political Economy, Journal of Operations

Management, International Journal of Production Management, and other journals. Dr. Perkins is a Fellow of the Decision Sciences Institute and has received the Institute's Distinguished Service Award; he completed a term as President of the Institute after previously serving as Vice President.
