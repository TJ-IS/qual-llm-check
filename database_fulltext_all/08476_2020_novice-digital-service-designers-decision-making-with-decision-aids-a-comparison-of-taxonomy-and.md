---
otero_id: 8476
otero_key: "PSFQ3V69"
title: "Novice digital service designers' decision-making with decision aids — A comparison of taxonomy and tags"
authors: "Xuanhui Liu; Karl Werder; Alexander Maedche"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113367"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Novice digital service designers' decision-making with decision aids — A comparison of taxonomy and tags

![](/api/attachments/PSFQ3V69/fulltext/images/e40e57f8014fc9f93d1344385cb0d9c55a1b6bfb9c9b9d1b13f11094d0203917.jpg)

Xuanhui Liu<sup>a,b,⁎</sup>, Karl Werder<sup>c</sup>, Alexander Maedche<sup>b</sup>

<sup>a</sup> Zhejiang Key Laboratory of Design and Intelligence and Digital Creativity, College of Computer Science and Technology, Zhejiang University, 866 Yuhangtang Rd, 310058 Hangzhou, China

<sup>b</sup> Institute of Information Systems and Marketing, Karlsruhe Institute of Technology, Kaiserstraße 89-93, 76133 Karlsruhe, Germany

<sup>c</sup> Cologne Institute for Information Systems, University of Cologne, Pohligstraße 1, 50969 Cologne, German

## A R T I C L E I N F O

Keywords: Cognitive effort Decision aid Decision style Tags Taxonomy

## A B S T R A C T

Digital services are a key driver of contemporary businesses. In order to scale the implementation of designcentric development processes, companies increasingly assign design work to design novices. As design novices have limited design knowledge and experience, they are challenged to select adequate design techniques throughout the entire lifecycle of digital services. Thus, providing decision aids to design novices is becoming increasingly important. In this research, we investigate taxonomy-based and tags-based decision aids. We draw on cognitive fit theory to construct a research model explaining the relationship between diferent decision aids and selection accuracy while considering the cognitive efort and the decision styles of novice designers. To test our hypotheses. we conducted a between-subiect laboratory experiment with 195 subiects. Our experimental results provide extensive support to our hypotheses. Taxonomy-based decision aids outperform tags-based decision aids concerning selection accuracy mediated by cognitive efort. Furthermore, the results suggest rational decision style as a moderator in the relationship between taxonomy-based decision aids and selection accuracy. Our results have practical implications: First, taxonomy-based decision aids should be primarily leveraged on decision support platforms supporting design processes. Second, design novices' decision style and cognitive efort are influential factors when developing decision aids to support digital service design processes.

## 1. Introduction

Design plays an essential role in all sectors. Design-oriented companies are characterized by higher revenue growth than their bench mark [1]. As we transition toward a digital society, face-to-face contacts are increasingly replaced by digital and human-free services [2]. Given the importance of design, digital service providers benefit from implementing design-centric processes within their organization. Specifi cally, selecting and applying adequate design techniques are influential tasks, as design techniques guide the design process by providing a set of necessary steps to accomplish a specific design goal [3]. However, hundreds of diferent design techniques are available [4]. Each design technique has specific design conditions that need to be met to take full advantage of it. Given the increasing amount of design techniques, particularly novice designers<sup>1</sup> are confronted with too much choice, which leads to higher complexity and making the selection of suitable design techniques increasingly dificult [5].

Much research has been done on the development and use of de cision aids to assist individuals in making choices [6]. An example is ecommerce [7] leveraging decision aids to support customers in the selection of products, whereby product attributes are classified into predefined categories to reduce the number of alternatives [8]. Scholars have investigated decision aids in manifold contexts, such as e-commerce [9], people-to-people loans [10], benchmarking tools [11], product recommendations [12]. and medical diagnoses [13]. Decision aids have various representation formats, such as decision trees [14], rules [8], tables [15], tags [16], and taxonomies [17]. In the context of loan application, the comprehensibility of decision trees, rules, and tables has been compared and evaluated based on their performance implications [18]. In the context of library collections, tags (i.e., a classification based on a flat hierarchy) have been investigated relative to their similarity and diference with expert-based classifications to evaluate the applicability of social tagging for library systems [19]. In the context of e-commerce, product taxonomy (i.e., a classification based on dimensions and characteristics) has been investigated to suggest customized categories [17]. However, there is a research gap concerning the question of how taxonomy-based or tags-based decision aids difer with regard to task performance when considering the in dividual characteristics, such as decision style, of the decision-maker.

![](/api/attachments/PSFQ3V69/fulltext/images/b5c526d5b7676625cf4765a2caa0d3a3464c24b81f76fe19bf3eb8d585cdbd32.jpg)  
Fig. 1. Diferences in the structure of taxonomy-based and tags-based decision aids

We drew on cognitive fit theory [20] as the theoretical foundation for our research on the efect of decision aids on task performance. Specifically, we investigated cognitive efort as a mediation variable, and we found that structural diferences between taxonomy-based and tags-based decision aids afects individual's cognitive eforts and task performance. In addition, we suggest that individuals with diverse de cision styles use the available information during the decision-making process in diferent ways when conducting a selection task [21]. Previous research has investigated the direct influence of intuitive and rational styles on choice quality [22] and task performance [23]. However, decision style is an aspect often overlooked by previous research on cognitive fit theory. Thus, we also investigated individuals' intuitive and rational decision style when using diferent decision aids, and we formulated the following research questions:

1) How do taxonomy-based and tags-based decision aids afect novice designers' cognitive efort and selection accuracy when selecting design techniques?

2) How do decision styles influence the relationship between decision aids and selection accuracy?

We conducted a laboratory experiment with 195 subjects to answer these questions. Our work provides several contributions. First, we advance research by constructing a nomological network around the use of decision aids, thus integrating research on information systems and human-computer interaction. Second, given the large number of design techniques and their importance for organizations, we advance the understanding of the use of decision aids and decision styles for selection tasks (e.g., [22]). Third, we extend previous research on cognitive fit theory by highlighting the importance of cognitive efort as well as rational and intuitive decision styles [24]. Finally, practitioners can benefit from our results on the efectiveness of decision aids for novice designers when considering their decision styles and cognitive efort. Beyond this specific context, we believe that our work can also inform the design of classification-based decision aids in general.

This paper is structured as follows: First, we introduce the conceptual foundations of decision aids, cognitive efort, and decision styles. Second, we suggest our research model and develop testable hypotheses. Third, we explain our research approach (i.e., the design of the laboratory experiment). Next, we present our data analysis and results. Finally, we discuss our results, contributions, and limitations.

## 2. Decision aids, cognitive efort and decision styles

Diferent decision aids — interventions that help people make decisions and improve decision quality [8,11] — to support design novices making decisions have been developed. We focus on taxonomy-based and tags-based decision aids because of the lack of research on comparing the performance between them. When referring to a taxonomybased decision aid, we suggest that the decision aid is based on a set of dimensions that includes a set of mutually exclusive and collectively exhaustive characteristics that are hierarchically structured. based on the definition of taxonomy provided by Nickerson et al. [25]. A taxonomy's categories are structured with parent-child relations, which are often based on experts' knowledge, such as plant taxonomy and animal taxonomy created by domain experts [25]. When referring to a tags-based decision aid, we suggest that the decision aid is based on flat categories that are neither hierarchically structured nor exclusive [26,27]. The categories of a set of tags have no parent-child relations and are often based on novices' understanding and preferences, such as tags created by users of websites [27]. Both decision aids support navigation as well as filtering and selecting information [27], and they are widely used on websites to support information access [28]. Fig. 1. shows the diferences between the two decision aids. Previous research has considered these two decision aids independently, either investigating the use of product taxonomy to extract customized categories [17] or the impact of data quality tags on the decision process [16].

Gathering and comparing various information involve cognitive ef forts [29]. Thus, some individuals require more cognitive efort than others — as it is the case of novices when compared to experts — to evaluate similarities and commonalities between alternatives when making decisions [30]. Cognitive efort refers to the mental efort and the cognitive resources spent on using a system that supports it [31]. Existing research investigates how cognitive efort is generated when using deci sion support systems for managerial decisions (e.g., marketing budgeting and resource allocation) [32] or how much cognitive efort is produced when using decision aids to choose products in the context of an e-com merce scenario [8]. Individuals tend to use a decision aid that requires less cognitive efort [33]. In our research, we focus on the cognitive efforts created when using either a taxonomy or tags for selection tasks.

Besides decision-makers' expertise and cognitive efort, decision styles can influence decision-making processes [34]. Intuitive decision style refers to decisions based on feelings and unstructured and randomized analysis processes [23]; rational decision style refers to gathering and comparing all the information before decision-making [23]. Both decision styles can impact an individual's information-processing ability. Previous research on decision styles has focused on developing and validating measurements on intuitive and rational decision styles [21], comparing diferent decision styles [35] and their efects [36]. The work on comparing diferent decision styles examines the preference for either intuitive or rational style for diferent kinds of decisions [35]. The research on influences of decision styles assesses the efects of intuitive and rational decision styles on individual financial behavior [36]. Although decision styles can influence decision-making processes, limited research has been conducted on decision styles' efect to when providing appropriate decision aids to decision-makers.

## 3. Hypotheses development

Cognitive fit theory explains the relationship between individual problem-solving skills, problem representation, and specific tasks. The theory has been applied to analyze individuals' problem-solving performance when using diferent information-presentation formats (graphs versus tables) [20,37]. An extension of cognitive fit theory suggests distinguishing between an internal and external problem representation, as both contribute to an individual's mental representation [38]. Internal problem representation refers to the abstract understanding of a domain's knowledge and previous experiences of using a tool or a system, whereas external problem representation refers to the abstraction implemented in a system or tool used when conducting a task [38,39]. A mismatch between internal and external problem representation can negatively influence the efectiveness and eficiency of task performance [38]. Extended cognitive fit theory has been applied to visual data analysis [40] and design patterns in software design [39].

We suggest design technique knowledge of design novices as the internal problem representation, whereas diferent decision aids are the external problem representations. Task performance is measured by selection accuracy, which indicates the number of correct selections that people make in a given experiment task. We present our research model in Fig. 2. In the following subsections, we develop each hypothesis.

## 3.1. The efect of decision aids on selection accuracy

Decision aids can assist in the decision process by filtering the se lection possibilities based on specific decision conditions [12]. For example, The decision aid of products can be used to screen alternatives and make recommendations [12]. Having clear criteria to distinguish features can help an individual discriminate among diferent categories with higher accuracy. Overwhelming information and the negative implications of too much choice can be reduced by limiting the selection options through categorization [41]. For example, using a decision aid and selecting a specific category within it can restrict the design techniques to those that meet the category's criteria. Hence, decision aids can help design novices structure information in their decisionmaking process [42].

Previous research on classification-based decision aids suggests that a decision aid needs to be logical, clear, and well-structured to support decision-makers in comparing and evaluating alternatives [43]. While both taxonomy-based and tags-based decision aids can reduce selection complexity and positively influence the selection process by narrowing down the selection scope, there are diferences between them. While a taxonomy-based decision aid is well-defined, often requires expert involvement and has clear quality criteria [25], tags-based decision aids are clustered responses, often result from the involvement of novices and sufer from construct deficit and redundancy [44]. Given that the selection task itself needs a structured understanding of the content [30], we suggest that taxonomy-based decision aids help design novices to achieve higher selection accuracy than tags-based decision aids. Hence, we articulate the following hypothesis:

H1. : Using a taxonomy-based decision aid leads to higher selection accuracy than using a tags-based decision aid, whereas using a tagsbased decision aid leads to higher selection accuracy than using no decision aid at all

## 3.2. The efect of decision aids on cognitive efort

Using a system for a decision-making task requires individuals to understand the system when scanning information for alternatives and comparing them. Scanning information and comparing alternatives causes cognitive efort [45]. One way to reduce cognitive efort is to present less information to decision-makers [46]. Decision aids support the reduction of information through abstraction, and they narrow down the selection scope by focusing on key attributes among alternatives [47].

When there is no decision aid, individuals need to read and compare all the information provided in a system before making decisions, which increases the required cognitive efort. In contrast, a decision aid makes it possible to present less information that is better organized, thus reducing the cognitive efort spent on searching and comparing information. As both forms of decision aids reduce the number of alternatives [27], they both decrease cognitive efort. However, when comparing them, tags-based decision aids lack parent-child relations between categories, whereas the hierarchically structured categories in taxonomy-based decision aids reduce the complexity of the selection process, thus helping decision-makers understand the inner workings of decision aids through abstraction [48]. Understanding the inner workings of decision aids reduces the need for iterative interaction between decision-makers and decision aids. We suggest that the taxonomy-based decision aids provide a better fit with selection tasks than tags-based decision aids when design novices selecting design techniques [49,50]. Hence, we hypothesize:

H2. : Using a taxonomy-based decision aid leads to lower cognitive efort than using a tags-based decision aid, whereas using a tags-based decision aid leads to lower cognitive efort than using no decision aid at all.

## 3.3. The relation between cognitive efort and selection accuracy

The cognitive process of problem-solving includes identifying goals, searching solutions, and setting relations between alternative paths and goals [51]. The decision-making process of comparing solutions creates cognitive efort through the mental processing of information [52]. With increasing cognitive eforts, more time and resources are needed to process the information in the system, and less time and resources are available to consider contextual information, which reduces task performance [53]. Specifically, the cognitive efort required to understand a problem can distract a person's attention from the task of selecting accurate information needed to solve the problem [54]. This kind of distraction has been described as a noise [55]. As a result, we propose the following hypothesis:

H3a. : An increase in cognitive efort leads to lower selection accuracy.

![](/api/attachments/PSFQ3V69/fulltext/images/4cb3a0dfd8fcf4669d15a14384405a5fb916e2953e548f84cc348365b8c2f906.jpg)  
Fig. 2. Research model.

The mental cost of thinking, understanding, and figuring out how to find the correct information for a given problem distracts decisionmakers from their main tasks [54]. Hence, a decision aid can help them focus on essential information chunks $( \boldsymbol { \mathrm { e . g . } } ,$ , selection categories), thus reducing their individual's cognitive efort while performing their tasks. The reduced cognitive efort allows individuals to consider contextual information and focus on the decision at hand, leading to higher selection accuracy [56]. Thus, when novices select design techniques for a specific design task, using a decision aid reduces cognitive efort and leads to more attention for the selection of accurate design techniques. Hence, we formulate the following hypothesis:

H3b. : Cognitive efort mediates the efect of decision aids toward selection accuracy.

## 3.4. Moderating efect of decision styles

We distinguish between two decision styles — namely, “the typical manner by which individuals make decisions” [21] — rational and intuitive decision styles [57]. We suggest that the intuitive decision style matches well with tags-based decision aids. Intuitive decisionmakers are holistic and tend to follow their feelings, whereas structuring information is not a necessary step [21,58]. Indeed, tags-based decision aids are usually developed by novices, providing a lower level classification based on the surface information [27,59]. The fit between tags-based decision aids and intuitive decision style can enhance the positive efect of using tags-based decision aids on selection accuracy. Hence, we state the following hypothesis:

H4a. : The positive efect of using a tags-based decision aid on selection accuracy is moderated by an individual's intuitive decision style, whereby the efect is stronger for individuals with a high intuitive decision style.

We suggest that the rational decision style matches well with the taxonomy-based decision aids. Individuals with a rational decision style tend to structure information based on evidential factors [21,58]. Taxonomy-based decision aids provide a hierarchical structure that corresponds with rational decision-makers' habit of building a hierarchical structure of all the available information before decision making. For example, when using self-service technologies, rational decision-makers tend to search structured information [60]. The match between the structure of the taxonomy-based decision aid and the ra tional decision style can strengthen the positive efect between using taxonomy-based decision aids and selection accuracy [25]. Hence, we hypothesize:

H4b. : The positive efect of using a taxonomy-based decision aid on selection accuracy is moderated by an individual's rational decision style, whereby the efect is stronger for individuals with a high rational decision style.

## 4. Research method

In order to test the hypotheses, we conducted a controlled laboratory experiment to gather replicable data following the guidelines suggested by Marsden and Pingry [61]. In this section, we introduce time, location, and the process relative to data collection, the experi menters and subjects involved in $\mathbf { i t } ,$ as well as the treatments and tools used in the experiment.

## 4.1. Experiment design

We conducted 12 experiment sessions in three days (four sessions per day) in a well-facilitated economics laboratory with individual soundproofed computer cubicles. During the experiment, each participant received no interruptions from the experimenters or the other participants. Two authors of this paper supervised the 12 sessions throughout the whole experiment. We followed a between-subject design with two treatments and a control group. The first treatment group received the taxonomy of design techniques<sup>2</sup> as decision aid (Fig. 3). The second treatment group received the tags of design techniques<sup>3</sup> as decision aid (Fig. 4). The control group received a list of design techniques (Fig. 5). All participants could click on the corresponding technique to receive further information. The information provided for each design technique was the same across all groups. The experiment design with the treatment and control groups were embedded in Limesurvey [62].

## 4.2. Participants and incentives

We recruited $1 9 5 ^ { 4 }$ individuals for the experiment from the subject pool of a large German university. The subject pool consisted of 4000 individuals and was managed using ORSEE $[ 6 3 ] . ^ { 5 }$ Five data points were removed because of incomplete data $\left( N = 3 \right)$ or misunderstanding of the experimental tasks $\left( N = 2 \right)$ . Specifically, when asked whether they understood the definition of design techniques and description of the task scenarios and experiment tools with control questions, participants indicated that they did not understand them.

Thus, 190 participants provided valid data for the experiment analysis (64 for the taxonomy of design techniques, 62 for the tags of design techniques, 64 for the list of design techniques). The average age was 23 years $( S D ~ = ~ 4 . 2 )$ and 97% of them were students.<sup>6</sup>Table 1 summarizes the demographic profile. Students were suitable for our experiment with three reasons: students are appropriate proxies for (young) practitioners [64], they are considered as novices rather than experts (e.g., [65]), and have been frequently used in previous research on decision-making tasks [8,34]. The experiment took an average of 44.8 min $( S D = 9 . 8 )$ ). Each participant was randomly assigned to one of three groups and received a show-up fee of 5 euros and at least 8 euros for accomplishing the experiment. As there were correct answers in the experiment tasks, the participants were incentivized to achieve good performance by getting an additional 1 euro for each task based on their performance (up to 3 euros in total).

## 4.3. Experimental settings, procedures, and manipulations

Following the introduction and description of the data privacy

![](/api/attachments/PSFQ3V69/fulltext/images/ae0a03438ee68af6cabdc9139d5dd97a47fffa6110e4352c6fc4759f31b1dcf3.jpg)  
Fig. 3. The user interface of a taxonomy of design techniques.

![](/api/attachments/PSFQ3V69/fulltext/images/865206d21794834b5ce9c3503af58c28ba187ad92249fef3bc3c55ff3b675900.jpg)  
Fig. 4. The user interface of tags of design techniques.

![](/api/attachments/PSFQ3V69/fulltext/images/b737843fb5749298ad5190c32351a62609f4621ff3e0db2cb8ebe8cbb427b032.jpg)  
Fig. 5. The user interface of a list of design techniques (received by the control group).

Table 1  
Demographic profile (n = 190).

<table><tr><td>Demographic profile</td><td>Number</td><td>Percent</td></tr><tr><td>Gender</td><td></td><td></td></tr><tr><td>Female</td><td>56</td><td>29.4</td></tr><tr><td>Male</td><td>134</td><td>70.6</td></tr><tr><td>Age</td><td></td><td></td></tr><tr><td>Below 18</td><td>1</td><td>0.5</td></tr><tr><td>18–30</td><td>182</td><td>95.8</td></tr><tr><td>Above 30</td><td>7</td><td>3.7</td></tr><tr><td>Education</td><td></td><td></td></tr><tr><td>High School Graduation</td><td>115</td><td>60.5</td></tr><tr><td>Bachelor&#x27;s Degree</td><td>65</td><td>34.2</td></tr><tr><td>Master&#x27;s Degree</td><td>10</td><td>5.3</td></tr><tr><td>Job status</td><td></td><td></td></tr><tr><td>Student</td><td>184</td><td>96.8</td></tr><tr><td>Other (freelancer, employee, and unemployed)</td><td>6</td><td>3.2</td></tr></table>

statement, the experimental procedure was separated into three stages.

In the first stage — the training part — we defined the term design technique and explained its use. Since we anticipated that participants had limited design technique knowledge, we used an example of a design technique instead of introducing a definition. We used the measurement from Flynn and Goldsmith [66] to measure participants prior knowledge of design techniques. The results indicated that the participants had a low average knowledge level with 2.87 (SD = 1.18). Before proceeding to the training section, participants were asked whether or not they understood the description of design techniques.

Two videos, using examples from zoology, were used to introduce the concept of decision aids. The first video<sup>7</sup> presented several animal pictures to the participants and showed the process of creating taxonomy or tags of the animals. The second video<sup>8</sup> illustrated how the created taxonomy or tags could be used as a decision aid to find animals. Following each video, participants were asked whether they un derstood how a taxonomy or tags work when selecting information based on a specific purpose. By using this generic, non-field specific example, the study avoided bias from preconceived information toward the tasks.

The second stage consisted of an experiment task in the context of a mobile app design project. Table 2 presents the detailed description of the task scenarios and the correct selections (i.e., design techniques). Three task scenarios that referred to each of three design stages (generating ideas, creating prototypes, and evaluating app) were provided to participants. We developed this experiment based on the review and synthesis of 31 scenarios in studies that describe the application of design techniques. An example is provided by concurrent think-aloud and A/B testing that can be applied for evaluating websites [79,82]. In the experiment, we used a mobile app development context, because, due to the ubiquitous use of mobile apps, participants could easily re late to their daily use of mobile apps. Furthermore, mobile app development is a rather smaller development and design project compared to, for instance, ERP systems. After each task scenario description, participants were asked whether they understood it. Each scenario was presented on a screen with the embedded experiment tool (a taxonomy of design techniques, tags of design techniques, or a list of design techniques), asking participants to select a maximum of five most ap propriate design techniques. Between two scenarios, there was a oneminute washout phase presenting a nature picture to allow participant to have a short break and make sure that the next task scenario would not be influenced by the previous one.

The third stage included the self-evaluating measurements related to the experiment task: perceived cognitive efort [50], decision styles [21], and demographics.

## 4.4. Measurements

The variable decision aids was operationalized through our experimental design. All other independent and control variables were measured using a 7-point Likert scale (1 = strongly disagree; 7 = strongly agree) [86]. Cognitive efort (Cronbach's Alpha = 0.89) was measured by adapting the questions from Pereira [52]. The items included in the measurement (Table 3) indicate the mental efort spent on using a system for decision-making tasks but not the mental resources needed for the tasks [8,50]. The measurement corresponds to the definition of cognitive efort suitable for testing our hypotheses. Intuitive decision style (Cronbach's Alpha = 0.88) and rational decision style (Cronbach's Alpha = 0.86) were adopted from Hamilton et al. [21] for their high internal consistency and distinction between two decision styles instead of generic cognitive styles [57], which has been used previously in decision-making research [22]. Based on our conceptual definition of decision styles, we use the decision-making process to assess an individual's decision style and present our final measurement items (Table 3). Thus, we considered the measurement introduced by Hamilton et al. [21] as appropriate.

Selection accuracy was measured by calculating the number of cor rected selections of design techniques for the three task scenarios (cf. [34]). For each task scenario, there were predefined seven correct selections (40 design techniques were included in the experiment tool). The predefined correct design techniques for each task scenario can be found in Table 2. As we gave predefined answers for each task scenario and incentivized participants to take the experiment seriously, we checked correct selections to measure selection accuracy. In the experiment, each participant was asked to select at most five techniques for each task scenario. As there was a total of three task scenarios, the number of correct selections ranged from 0 to 15. For example, if a participant provided three correct selections to the first scenario, four for the second one, and two for the third one, the resulting selection accuracy was 9.

The control variables included age, gender, education, and prior design technique knowledge. As the hypotheses focused on design novices, we used prior design technique knowledge (Cronbach's Alpha = 0.91) as a control variable based on the questions from Flynn and Goldsmith [66] that develops the measurement to measure subjective knowledge. The measurement includes items based on selfevaluation of prior knowledge. We adapted the measurement's items (Table 3) to evaluate the participants' design techniques knowledge level, which was suitable in the context of the experiment design.

## 4.5. Measurement validity

An exploratory factor analysis using principal component analysis and varimax rotation was performed on cognitive efort, rational de cision style, intuitive decision style, and prior design technique knowledge (cf. [87]). Results indicated that items loaded highly on their intended factor (with a maximum score of 0.89 and a minimum score of 0.65) and lowly on the other factors (with a maximum score of 0.16 and a minimum score of 0; Appendix A). Table 4 presents the median, mean, and standard deviation of each variable, as well as the correlations between the variables.

## 5. Data analysis and result

We used ordinary least square regression analysis to test our hypotheses (H1–H4b). Following our hierarchical regression analysis, we used Kruskal-Wallis test and Mann-Whitney U test for a detailed

Table 4  
Experiment task scenarios and correct selections.

<table><tr><td>Task scenario</td><td>Design technique</td><td>Reference</td></tr><tr><td colspan="3">Overall description:Please imagine you are working in a team on a project. Your project develops a mobile app enabling users to book cinema tickets. Please select suitable design techniques based on three design stages:</td></tr><tr><td rowspan="2">Stage 1: Generate ideas</td><td>3-12-3 Brainstorming</td><td>[67]</td></tr><tr><td>6-3-5 Brainwriting</td><td>[68]</td></tr><tr><td>You are at an early stage of your project.</td><td>Role-playing</td><td>[69]</td></tr><tr><td rowspan="2">You want to involve a group of people (more than two) to discuss the project and generate some ideas during the discussion.</td><td>Story sharing</td><td>[70]</td></tr><tr><td>Tomorrow headlines</td><td>[71]</td></tr><tr><td rowspan="2">You do not have access to real users.</td><td>Offering mapping</td><td>[72]</td></tr><tr><td>Storyboarding</td><td>[73]</td></tr><tr><td rowspan="2">Stage 2: Create prototypes</td><td>Bodystorming</td><td>[74]</td></tr><tr><td>Experience prototyping</td><td>[74]</td></tr><tr><td>You now want to create some initial prototypes based on the ideas created in stage 1.</td><td>Heuristic evaluation</td><td>[75]</td></tr><tr><td rowspan="2">After creating several prototypes, you want to compare them and decide on one or two prototypes for further refinement.</td><td>Collaborative sketching</td><td>[76]</td></tr><tr><td>Cognitive walkthrough</td><td>[77]</td></tr><tr><td rowspan="2">You again do not have access to real users when creating and evaluating prototypes.</td><td>Wireframing</td><td>[78]</td></tr><tr><td>Mood board</td><td>[74]</td></tr><tr><td rowspan="2">Stage 3: Evaluate App</td><td>Concurrent think-aloud</td><td>[79]</td></tr><tr><td>Retrospective think-aloud</td><td>[80]</td></tr><tr><td>You now have developed a first running version of the app.</td><td>Private camera conversation</td><td>[81]</td></tr><tr><td>You want to evaluate the app with real users before delivering it on a large scale to the market.</td><td>A/B testing</td><td>[82]</td></tr><tr><td rowspan="3">The evaluation seeks to collect real users&#x27; data and feedback within a couple of days.</td><td>Co-discovery</td><td>[83]</td></tr><tr><td>Product experience tracker</td><td>[84]</td></tr><tr><td>Experience clips</td><td>[85]</td></tr></table>

<table><tr><td>Measurement</td><td>Item</td></tr><tr><td>Rational decision styles [21]</td><td>I prefer to gather all the necessary information before committing to a decision.I thoroughly evaluate decision alternatives before making a final choice.In decision-making, I take time to contemplate the pros/cons or risks/benefits of a situation.Investigating the facts is an important part of my decision-making process.I weigh a number of different factors when making decisions.</td></tr><tr><td>Intuitive decision styles [21]</td><td>When making decisions, I rely mainly on my gut feelings.My initial hunch about decisions is generally what I follow.I make decisions based on intuition.I rely on my first impressions when making decisions.I weigh feelings more than analysis in making decisions.</td></tr><tr><td>Cognitive effort [52]</td><td>To complete the task, using [the taxonomy/tags/list] was very frustrating.To complete the task, using [the taxonomy/tags/list] took too much time.To complete the task, using [the taxonomy/tags/list] required too much effort.To complete the task, using [the taxonomy/tags/list] was too complex.To complete the task, using [the taxonomy/tags/list] was easy.</td></tr><tr><td>Prior design technique knowledge [66]</td><td>I know pretty much about design techniques.In a design group, I am one of the experts when using design techniques.Compare to most other members in a design team, I know less about these products.When using a design technique, I really do not know a lot.I do not feel very knowledgeable about design techniques.I have a lot of experiences with design techniques.I feel familiar with design techniques.</td></tr></table>

Descriptive statistic and correlations (n = 190).

<table><tr><td rowspan="2">Variables</td><td rowspan="2">Mdn</td><td rowspan="2">M</td><td rowspan="2">SD</td><td rowspan="2">α</td><td colspan="5">Correlations</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1. Selection accuracy</td><td>8</td><td>8.59</td><td>3.20</td><td>n/a</td><td>n/a</td><td></td><td></td><td></td><td></td></tr><tr><td>2. Cognitive effort</td><td>3</td><td>3.18</td><td>1.41</td><td>0.89</td><td>-0.47***</td><td>0.80</td><td></td><td></td><td></td></tr><tr><td>3. Rational decision style</td><td>5.7</td><td>5.47</td><td>0.91</td><td>0.86</td><td>-0.15*</td><td>0.16*</td><td>0.75</td><td></td><td></td></tr><tr><td>4. Intuitive decision style</td><td>3.2</td><td>3.35</td><td>1.08</td><td>0.88</td><td>0.14+</td><td>-0.01</td><td>-0.34***</td><td>0.78</td><td></td></tr><tr><td>5. Prior design technique knowledge</td><td>2.57</td><td>2.87</td><td>1.18</td><td>0.91</td><td>-0.04</td><td>0.03</td><td>0.06</td><td>0.15</td><td>0.78</td></tr></table>

Notes: 1) Mdn = median; M = mean; SD = standard deviation; α = Cronbach's Alpha; The diagonal shows the square roots of AVE; 2) $+ \ P \ < \ . 1 ; \ { ^ * P } \ < \ . O 5 ;$ $^ { * * } P \ < \ . O I ; ^ { * * * } P \ < \ . O O I .$

analysis of H1 and H2 by comparing the diferences of selection accu racy and cognitive efort across the three experimental groups (a taxonomy of design techniques, tags of design techniques, or a list of design techniques). For H4b, as the $R ^ { 2 }$ of the regression model with the moderating efect of rational decision style was higher than the regression model without the moderator, we used ANOVA test to compare whether the regression models (H4b) were significantly diferent from the models without the moderator. Table 5 presents a summary of the tests of the hypotheses and the relative results.

Table 5  
A summary of used tests and the results of $\mathrm { H } 1 - \mathrm { H } 4 \mathrm { b } .$

<table><tr><td>#</td><td>Hypothesis</td><td>Test</td><td>Result</td></tr><tr><td>H1:</td><td>Using a taxonomy-based decision aid leads to higher selection accuracy than using a tags-based decision aid, whereas using a tags-based decision aid leads to higher selection accuracy than using no decision aid at all.</td><td>Linear regression + Kruskal-Wallis test + Mann-Whitney U test</td><td>Supported</td></tr><tr><td>H2:</td><td>Using a taxonomy-based decision aid leads to lower cognitive effort than using a tags-based decision aid, whereas using a tags-based decision aid leads to lower cognitive effort than using no decision aid at all.</td><td>Linear regression + Kruskal-Wallis test + Mann-Whitney U test</td><td>Supported</td></tr><tr><td>H3a:</td><td>An increase in cognitive effort leads to lower selection accuracy.</td><td>Linear regression</td><td>Supported</td></tr><tr><td>H3b:</td><td>Cognitive effort mediates the effect of decision aids toward selection accuracy.</td><td>Linear regression</td><td>Supported</td></tr><tr><td>H4a:</td><td>The positive effect of using a tags-based decision aid on selection accuracy is moderated by an individual&#x27;s intuitive decision style, whereby the effect is stronger for individuals with a high intuitive decision style.</td><td>Linear regression</td><td>Not supported</td></tr><tr><td>H4b:</td><td>The positive effect of using a taxonomy-based decision aid on selection accuracy is moderated by an individual&#x27;s rational decision style, whereby the effect is stronger for individuals with a high rational decision style.</td><td>Linear regression + ANOVA</td><td>Not supported</td></tr></table>

## 5.1. The efect of decision aids on selection accuracy

We used the controls-only model and the direct-efect model (models 1 and 2 in Table 6) to test the efect of decision aid on selection accuracy (H1). None of the control variables was significantly regressed onto the dependent variable selection accuracy (model 1 in Table 6). When adding taxonomy-based and tags-based decision aids as in dependent variables (model 2 in Table 6), the coeficient of determination increased $( \Delta R ^ { 2 } = 0 . 4 9 7 )$ . The ANOVA test of these two models showed a significant diference [88] $( F ( 2 , 1 8 3 ) = 9 0 . 3 8 , p \ < \ . 0 0 1 ) .$

We tested the dependent variable selection accuracy for normality by using a Shapiro-Wilk test. The test indicated that data was not normally distributed $( W = 0 . 9 7 , p \ < \ . 0 5 )$ , suggesting the use of the Kruskal-Wallis test as an adequate test [89]. The test $( \mathrm { F i g . ~ } 6 ,$ left) that there is a significant efect of decision aids on selection accuracy across three conditions $( H \left( 2 \right) = 9 0 . 9 6 , p \ < \ . 0 0 1 )$ . We then used the Mann-Whitney U test for multiple comparisons, which showed that selection accuracy was significantly lower with no decision aid $( M d n = 6 . 5 )$ than taxonomy-based decision aid $( M d n = 1 2 . 0 , p ~ < ~ . 0 0 1 )$ . Selection accuracy was quasi-significantly lower without a decision aid than with tags-based decision aids $( M d n = 7 . 0 , p = . 0 7 9 )$ . Furthermore, selection accuracy was significantly lower with tags-based than with taxonomybased decision aids $( p ~ < ~ . 0 0 1 )$ . It is then possible to conclude that using taxonomy-based decision aids leads to higher accuracy than using either tags-based decision aids or no decision aid. Hence, H1 is sup ported.

Table 6  
Hierarchical linear regression for testing H1 $( n = 1 9 0 )$

<table><tr><td>Dependent variable</td><td colspan="2">Selection accuracy</td></tr><tr><td>Models</td><td>Model 1</td><td>Model 2</td></tr><tr><td colspan="3">Independent variables</td></tr><tr><td>Age</td><td>0.01 (0.07)</td><td>0.01 (0.05)</td></tr><tr><td>Gender</td><td>-0.33 (0.52)</td><td>-0.02 (0.37)</td></tr><tr><td>Edu</td><td>-0.10 (0.49)</td><td>-0.20 (0.35)</td></tr><tr><td>PDTK</td><td>0.07 (0.20)</td><td>-0.09 (0.15)</td></tr><tr><td>TAGS</td><td></td><td>0.75+ (0.41)</td></tr><tr><td>TAXO</td><td></td><td>5.11*** (0.41)</td></tr><tr><td>Constant</td><td>8.74*** (1.64)</td><td>6.94*** (1.19)</td></tr><tr><td> $R^2$ </td><td>0.003</td><td>0.50</td></tr><tr><td> $ΔR^2$ </td><td>-</td><td>0.497***</td></tr><tr><td>F Statistic</td><td>0.15 (df = 4; 185)</td><td>30.33*** (df = 6; 183)</td></tr></table>

Notes: 1) the table gives coefficients (standardized errors): $2 ) \ + \ p \ < \ . 1 ;$ $^ { * } p \ < \ . 0 5 ; ^ { * * } p \ < \ . 0 1 ; ^ { * * * } p \ < \ . 0 0 1 ; 3 ) \Delta \mathrm { R } ^ { 2 }$ scores compare the model against the controls-only model; 4) PDTK = prior design technique knowledge; TAGS = tags-based decision aid; TAXO = taxonomy-based decision aid.

## 5.2. The efect of decision aids on cognitive efort

Two regression models were built to test H2 (models 1 and 2 in Table 7). The regression of all control variables on cognitive efort was not significant (model 1 in Table 7). When adding taxonomy-based and tags-based decision aids as independent variables (model 2 in Table $^ { 7 ) , }$ the $R ^ { 2 }$ of the regression model increased $( \Delta R ^ { 2 } = 0 . 2 7 )$ and there was a significant diference between the two models, as an ANOVA test suggested $( F \left( 2 , 1 8 3 \right) = 3 3 . 9 5 , p \ < \ . 0 0 1 )$

The Shapiro-Wilk test demonstrated that the dependent variable cognitive efort was non-normal $( W = 0 . 9 6 , p ~ < ~ . 0 0 1 )$ . We used the Kruskal-Wallis test (Fig. 6, right) to compare the three groups, which indicated that there was a significant efect of decision aids on cognitive efort for the three conditions (H $( 2 ) \ : = \ : 5 3 . 1 1 , p \ : < \ : . 0 0 1 )$ . The Mann: Whitney U test revealed that cognitive efort was significantly lower with tags-based decision aids $( M d n \ = \ 2 . 9 )$ than with no decision aid $( M d n \ = \ 4 . 2 , \ p \ < \ . 0 0 1 )$ . Furthermore, the cognitive efort was significantly lower with taxonomy-based decision aids $( M d n = 2 . 0 )$ than without decision aid $( p \ < \ . 0 0 1 )$ . The cognitive efort was significantly lower when using taxonomy-based decision aids than tags-based decision aids $( p \ < \ . 0 0 1 )$ . As a result, we suggest that using taxonomy-based decision aids leads to lower cognitive efort than either using tags-based decision aids or no decision aid. Hence, H2 is supported.

## 5.3. The mediating efect of cognitive efort

Following the guidelines by Zhao et al. [90], we tested the mediating efect of cognitive efort within the relationship between decision aids and selection accuracy. First, we modeled cognitive efort as an independent variable with a direct impact on selection accuracy (model 2 in Table 8). The regression model showed that cognitive efort had a negative efect on selection accuracy, and the $R ^ { 2 }$ increased to 0.217 compared to the controls-only model (model 1 in Table 8). Model 1 and model 2 (Table 8) showed a significant diference based on ANOVA test $( F \left( 1 , 1 8 4 \right) = 5 0 . 4 5 , p \ < \ . 0 0 1 )$ ). Hence, H3a is supported.

Second, a regression model with cognitive efort as mediator was built (model 3 in Table 8), which used both decision aids and cognitive efort as independent variables when predicting selection accuracy, $R ^ { 2 }$ increased to 0.52. We computed the average causal mediating efect (ACME), average direct efects (ADE), and p-values by using the mediation R package [90,91]. The results indicated a partial mediation with complementary efects of cognitive efort $( \mathrm { A C M E } ~ = ~ 0 . 6 6 , ~ p ~ = ~ . 0 1 )$ within the relationship of taxonomy-based decision aid and selection accuracy $( \mathrm { A D E } = 4 . 4 6 , p ~ < ~ . 0 0 1 )$ , whereas cognitive efort showed a full mediating efect $( \mathsf { A C M E } = 0 . 3 0 , p = . 0 3 )$ within the relationship between tags-based decision aids and selection accuracy $( \mathrm { A D E } = 0 . 4 5 ,$ $p \ = \ . 2 9 )$ . The result indicates that cognitive effort mediates the relationship between decision aids and selection accuracy. Hence, H3b is supported.

![](/api/attachments/PSFQ3V69/fulltext/images/2530e522dd531229467fc74e0c379e3ac0e619f33006c04610d0cd666d1ecf7e.jpg)

![](/api/attachments/PSFQ3V69/fulltext/images/e0f73feb660b3814458d86e420196276de177e399c99bbfb602f9fbdfd9c08e7.jpg)  
Fig. 6. The efect of decision aids on selection accuracy (left) and cognitive efort (right). The p value from Mann-Whitney U test shows between two groups also presented on both plots.

Hierarchical linear regression for testing H2 (n = 190).

<table><tr><td>Dependent variable</td><td colspan="2">Cognitive effort</td></tr><tr><td>Models</td><td>Model 1</td><td>Model 2</td></tr><tr><td colspan="3">Independent variables</td></tr><tr><td>Age</td><td>-0.002 (0.03)</td><td>-0.004 (0.03)</td></tr><tr><td>Gender</td><td>0.25 (0.23)</td><td>0.16 (0.20)</td></tr><tr><td>Edu</td><td>0.12 (0.21)</td><td>0.16 (0.18)</td></tr><tr><td>PDTK</td><td>-0.04 (0.09)</td><td>0.02 (0.08)</td></tr><tr><td>TAGS</td><td></td><td>-0.81*** (0.22)</td></tr><tr><td>TAXO</td><td></td><td>-1.78*** (0.22)</td></tr><tr><td colspan="3">CE</td></tr><tr><td>Constant</td><td>2.84*** (0.72)</td><td>3.66*** (0.63)</td></tr><tr><td> $R^2$ </td><td>0.01</td><td>0.28</td></tr><tr><td> $ΔR^2$ </td><td>-</td><td>0.27***</td></tr><tr><td>F Statistic</td><td>0.52 (df = 4; 185)</td><td>11.79*** (df = 6; 183)</td></tr></table>

Notes: 1) the table gives coeficients (standardized errors); $2 ) \ + \ p \ < \ . 1 ;$ $^ { * } p \ < \ . 0 5 ; ^ { * * } p \ < \ . 0 1 ; ^ { * * * } p \ < \ . 0 0 1 ; 3 ) \Delta \mathrm { R } ^ { 2 }$ scores compare the model against the controls-only model; 4) PDTK = prior design technique knowledge; TAGS = tags-based decision aid; TAXO = taxonomy-based decision aid; CE = cognitive efort.

Hierarchical linear regression for testing H3a – H3b (n = 190).

<table><tr><td>Dependent variable</td><td colspan="3">Selection accuracy</td></tr><tr><td>Models</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td colspan="4">Independent variables</td></tr><tr><td>Age</td><td>0.01 (0.07)</td><td>0.01 (0.06)</td><td>0.01 (0.05)</td></tr><tr><td>Gender</td><td>-0.32 (0.52)</td><td>-0.06 (0.47)</td><td>0.04 (0.37)</td></tr><tr><td>Edu</td><td>-0.10 (0.49)</td><td>0.03 (0.44)</td><td>-0.14 (0.35)</td></tr><tr><td>PDTK</td><td>0.07 (0.20)</td><td>0.02 (0.18)</td><td>-0.09 (0.14)</td></tr><tr><td>TAGS</td><td></td><td></td><td>0.45 (0.42)</td></tr><tr><td>TAXO</td><td></td><td></td><td>4.46*** (0.47)</td></tr><tr><td>CE</td><td></td><td>-1.06*** (0.15)</td><td>-0.37** (0.14)</td></tr><tr><td>Constant</td><td>8.74*** (1.64)</td><td>11.76*** (1.51)</td><td>8.29*** (1.27)</td></tr><tr><td> $R^2$ </td><td>0.003</td><td>0.22</td><td>0.52</td></tr><tr><td> $\Delta R^2$ </td><td>-</td><td>0.217***</td><td>0.517***</td></tr><tr><td>F Statistic</td><td>0.15 (df = 4; 185)</td><td>10.24*** (df = 5; 184)</td><td>27.87*** (df = 7; 182)</td></tr></table>

Notes: 1) the table gives coeficients (standardized errors); $2 ) \ + \ p \ < \ . 1 ;$ $^ { * } p \ < \ . 0 5 ; ^ { * * } p \ < \ . 0 1 ; ^ { * * * } p \ < \ . 0 0 1 ; 3 ) \Delta \mathrm { R } ^ { 2 }$ scores compare the model against the controls-only model; 4) PDTK = prior design technique knowledge; TAGS = tags-based decision aid: TAXO = taxonomy-based decision aid: CE = cognitive efort.

## 5.4. The moderating efect of decision styles

Before analyzing the efect of rational and intuitive decision styles on the relationship between using decision aids and selection accuracy, the Kruskal-Wallis test was used to test the distribution of rational and intuitive decision styles across the three experimental groups. The result of our analysis for selection bias suggests that there was no difference in the distribution of rational and intuitive decision styles across the three experimental groups, with a p-value of 0.62 and 0.50, respectively.

We conducted a hierarchical regression analysis, starting with a controls-only model (model 1 in Table 9) that we extended to the direct efect of decision aids (model 2 in Table 9). Subsequently, we tested the moderation efect of both intuitive (model 3 in Table 9) and rational decision style (model 4 in Table 9). The results suggest neither a significant direct efect of intuitive decision style nor an interaction efect with either of decision aids on selection accuracy. Hence, H4a is not supported.

Adding rational decision style as an independent variable increased the coeficient of determination when comparing the model including the moderation of rational decision style (Model 4 in Table 9) to the direct-efect model (Model 2 in Table 9). The ANOVA test highlighted a trend of significant diference between the two models (models 2 and 4 in Table $9 ; F \left( 3 , 1 8 0 \right) = 2 . 3 8 ; p = . 0 7 ) .$ . The regression model with the rational decision style as a moderator (model 4 in Table 9) presented a significant direct efect of rational decision style and the interaction of rational decision style and taxonomy-based decision aids on selection accuracy. The moderating efect of rational decision style modestly improved the fit of the regression model. Hence. there was a moder ating efect of rational decision style in the relationship between taxonomy-based decision aids and selection accuracy. The negative coefficient of the interaction between rational decision style and taxonomybased decision aids indicates that individuals with an increasing rational decision style have a decreasing selection accuracy when using taxonomy-based decision aids. The result was the opposite of what hypothesized in H4b. Hence, H4b is not supported.

Since the negative regression lines of the interactive efect of rational decision style and taxonomy-based decision aids (Fig. 7 left) was not expected, we investigated this relationship further using a slope diference test [92].

The slopes for predicting selection accuracy were divided into three levels of rational decision styles (low = –1 SD, medium = variable's mean, high = +1 SD) [92] (Fig. 7 right). The standard deviation analysis of rational decision style reflected that when providing taxonomv-based decision aids. high rational decision-makers had a lower selection accuracy than low rational decision-makers. For low rational decision-makers, the efect of taxonomy-based decision aids (β = 1.23, $ { p } < \ . 0 0 1 )$ was positive, but the interaction efect of rational decision style and taxonomy-based decision aids was negative on selection accuracy $( \beta = \mathrm { ~ - } 0 . 5 4 , p = . 0 8 6 )$ . For high rational decision-makers, the efect on taxonomy-based decision aids $( \beta \ = \ 1 . 4 3 , \ p \ < \ . 0 0 1 )$ was positive, but the interaction efect of rational decision style and taxonomy-based decision aids was negative on selection accuracy $( \beta \ : = \ : \ : - 0 . 7 3 , p \ : = \ : . 0 8 6 )$ . When comparing the regression line of high and low rational decision-makers, the two standard coeficient values of the interaction efect of rational style and taxonomy-based decision aids showed that the higher the rational decision style, the lower the se lection accuracy.

Table 9  
Hierarchical linear regression for testing H4a and H4b (n = 190).

<table><tr><td>Dependent variable</td><td colspan="4">Selection accuracy</td></tr><tr><td>Model</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td colspan="5">Independent variable</td></tr><tr><td>Age</td><td>0.01 (0.07)</td><td>0.01 (0.05)</td><td>0.01 (0.05)</td><td>0.03 (0.05)</td></tr><tr><td>Gender</td><td>-0.32(0.52)</td><td>-0.02 (0.37)</td><td>0.06 (0.38)</td><td>-0.03 (0.37)</td></tr><tr><td>Edu</td><td>-0.09(0.49)</td><td>-0.20 (0.35)</td><td>-0.21 (0.35)</td><td>-0.30 (0.35)</td></tr><tr><td>PDTK</td><td>0.07 (0.20)</td><td>-0.09 (0.15)</td><td>-0.07 (0.15)</td><td>-0.09 (0.15)</td></tr><tr><td>TAGS</td><td></td><td>0.75+ (0.41)</td><td>0.91 (1.33)</td><td>1.42 (2.59)</td></tr><tr><td>TAXO</td><td></td><td>5.11***(0.41)</td><td>4.78***(1.33)</td><td>9.40*** (2.42)</td></tr><tr><td>IDS</td><td></td><td></td><td>-0.21 (0.26)</td><td></td></tr><tr><td>TAGS x IDS</td><td></td><td></td><td>-0.05 (0.38)</td><td></td></tr><tr><td>TAXO x IDS</td><td></td><td></td><td>0.10 (0.37)</td><td></td></tr><tr><td>RDS</td><td></td><td></td><td></td><td>0.62* (0.27)</td></tr><tr><td>TAGS x RDS</td><td></td><td></td><td></td><td>-0.13 (0.47)</td></tr><tr><td>TAXO x RDS</td><td></td><td></td><td></td><td>-0.79+(0.43)</td></tr><tr><td>Constant</td><td>8.74***(1.64)</td><td>6.94***(1.19)</td><td>7.49***(1.43)</td><td>3.40+ (1.93)</td></tr><tr><td> $R^2$ </td><td>0.003</td><td>0.50</td><td>0.50</td><td>0.52</td></tr><tr><td> $\Delta R^2$ </td><td>-</td><td>0.497***</td><td>0.497***</td><td>0.517***</td></tr><tr><td>F Statistic</td><td>0.15(df = 4; 185)</td><td>30.33***(df = 6; 183)</td><td>20.23***(df = 9; 180)</td><td>21.47***(df = 9; 180)</td></tr></table>

Notes: 1) the table gives coeficients (standardized errors); $2 ) \ + \ p \ < \ . 1 ;$ $^ { * } p \ < \ . 0 5 ; ^ { * * } p \ < \ . 0 1 ; ^ { * * * } p \ < \ . 0 0 1 ; 3 ) \Delta \mathrm { R } ^ { 2 }$ scores compare the model against the controls-only model; 4) PDTK = prior design technique knowledge; RDS = rational decision style; IDS = intuitive decision style; TAGS = tags based decision aid; TAXO = taxonomy-based decision aid

![](/api/attachments/PSFQ3V69/fulltext/images/4713e2b2605d93b007eb36d8414b3b9ffe566cf541bd3622321c674376c7185f.jpg)

## 6. Discussion

We constructed and tested a research model describing the impact of two important decision aids on selection accuracy while accounting for cognitive efort and diferent decision styles. Our work thus provides several contributions to the literature. First, it contributes to the nomological net of decision aids within the specific context of designing digital services [93]. While previous research investigated taxonomybased [17] and tags-based decision aids [16] independently from each other, this study extends these results by comparing the performance implications of them. The results suggest that both taxonomy-based and tags-based decision aids can help with the selection of design techniques. However, the use of taxonomy-based decision aids leads to higher selection accuracy.

Second, this research considered the role of decision styles as moderators when using decision aids to select design techniques. Thus, we integrated previously disjoint research focusing either on the influence of decision styles (e.g., [22]) or decision aids (e.g., [42]) on the task performance. We added decision styles as influential variables when investigating performance implications of decision aids.

Third, this research extended cognitive fit theory [20,37] by emphasizing the importance of cognitive efort and decision styles when using decision aids. Task performance (i.e., selection accuracy) improves when using a decision aid, as the decision aid reduces cognitive efort. These findings complement previous research that identified a mediating efect of cognitive efort in the relationship between transparency and trust [48]. In addition, this study extends previous research investigating the direct efect of decision styles on task performance [23] by investigating the moderating efects of rational and intuitive decision style on the relationship between decision aids and task performance.

## 6.1. Theoretical implications

Important theoretical implications emerge from our experimental results, which suggest a fully mediating efect of cognitive efort on the relationship between tags-based decision aids and selection accuracy. The negative efect of tags-based decision aids on cognitive efort suggests that categories without parent-child relations also reduce the cognitive efort when selecting design techniques. In contrast to tagsbased decision aids, the results suggest a partial mediation with complementary efects on the relationship between taxonomy-based decision aid and selection accuracy. Taxonomy-based decision aids could not only improve selection accuracy directly but also indirectly by reducing the cognitive efort. These results complement previous research on the transparency of recommendation agents [48], suggesting that also latent information structures influence individuals' cognitive eforts and task accuracy. Thus, this study sheds light on the causes of selection accuracy during decision-making tasks and advances theory on decision aids.

![](/api/attachments/PSFQ3V69/fulltext/images/044290a05bd56de1fb5c8ad306c64da199f2810aca0340720c7411c5cfe8d99d.jpg)  
Fig. 7. Linear regression analysis for testing the moderating effect of rational decision style (left) and the standard deviation analysis for testing the moderating effect of rational decision style (right).

Furthermore, we present important findings on the interaction of decision aids with decision styles. Our results suggest no moderating efect of intuitive decision style on the relationship between tags-based decision aid and selection accuracy. Although intuitive decision style tends toward the creation of flat categories [27,59], the corresponding decision style for tags-based decision aids did not positively influence selection accuracy in our experiment. We explain this finding with the various feelings and hunches that vary from person to person [21,58].

Our results about rational decision style suggest contradicting outcomes for the investigated decision aids. The interaction efect with the taxonomy-based decision aids is negative. When using taxonomy-based decision aids, selection accuracy slightly declined with the increase of rational decision style. This result is not in agreement with research that adheres to the promotion of rational decision-making processes in management [43]. This can be explained by the fact that rational de cision-makers need to familiarize with all relevant knowledge and structure the information in their mind prior to decision-making [21]. However, because of the lack of design technique knowledge [30], the structure of participants' mental models could not match the structure of the taxonomy-based decision aids created by experts. Thus, with a high rational decision style but limited knowledge, taxonomy-based decision aids negatively influence the decision-making processes.

## 6.2. Practical implications

The findings suggest higher task performance when using taxonomy-based decision aids when compared to using tags-based decision aids. Although our tags-based decision aid was built by novices, it did not support novices in the selection of design techniques as well as a taxonomy-based decision aid. Thus, practitioners benefit more from taxonomy-based decision aids when selecting design techniques. Tagsbased decision aids can be rather used as a supplement, for instance, to support navigation or provide a tag cloud [28]. Moreover, previous research supports the supplemental use of tags in library cataloguing systems [19].

Furthermore, we suggest that decision aid developers should design their systems in such a way that novices do not need a lot of mental eforts when using the system. This means, the provided decision aid needs to be understandable by novices. A well-structured decision aid helps to achieve this purpose. Our expert-based decision aid had an additional level of abstraction, increasing its structure and allowing novices to narrow down the search problem more easily. This characteristic helps novices to better understand the decision aid, as the task is divided into sub-problems that are easily understood by novices. As a result, novices find better support through expert-based decision aids in solving selection tasks, which is consistent in the context of applying decision aids for consumers, suggesting the reduction of mental efort to improve intention to use [8]. The positive efects of taxonomy-based decision aids outweigh the negative efect observed for users having already established their own mental structure of the problem domain.

## 6.3. Limitations and future research

This research also has its limitations. First, in the experiment, we measured task performance by the selection accuracy of design techniques for each task scenario. Although we predefined the correct selections of design techniques and grounded our decision in the literature, the measure was specifically developed for this study. Further research may investigate alternative context and performance measures, such as using the data from a real design project or evaluating decision aids in the context of website design.

Second, our evaluation is limited to the taxonomy and tags of design techniques. This matches the purpose of comparing the diferences between the efect of taxonomy-based and tags-based decision aids on design novices' selection of design techniques. However, there are design options for these decision aids. Hence, future research may investigate more design alternatives for decisions aids in order to better understand their efects on task performance.

Third, in the experiment settings, most of the participants were students. Therefore, we suggest including early-career employees and design experts in future research to investigate the influence of decision aids on individuals with diferent knowledge levels of design techniques.

## 7. Conclusion

Decision aids can shape and influence the accuracy of decisionmaking in selection tasks. However, the relationship between decision aids and the accuracy of decision making is complex. In this study, we compared two design choices of decision aids in the context of novices' selection of design techniques. We developed hypotheses based on the cognitive fit theory. A between-subject laboratory experiment was designed and conducted. The use of a taxonomy-based decision aid demonstrated a positive efect on selection accuracy, partially mediated by cognitive efort and modestly moderated by rational decision style. While the use of a tags-based decision aid proved to have a modest positive efect on selection accuracy and to be fully mediated by cognitive efort, a moderating efect of intuitive decision style on the relationship between tags-based decision aids and selection accuracy could not be substantiated.

The study not only contributes to the research on decision aids of design techniques by evaluating taxonomy-based and tags-based decision aids in a selection task, but also emphasizes the importance of considering cognitive efort and decision styles when novices use decision aids to select design techniques. With the right design of decision aids, novices can select the most adequate design technique for their project situation and, on this basis, design better digital services.

## Acknowledgements

We would like to thank the anonymous reviewers for their insightful and detailed comments in the reviewing process. We also thank the participants of the Cologne Institute for Information Systems research seminar participants for their feedback on an earlier versions of the manuscript. Thanks also to Prof. Shirley Gregor for her feedback on hypotheses and experiment plan. Xuanhui Liu also thanks the China Scholarship Council (CSC) for providing her scholarship (ID: 201508210181) for doing research in Germany.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.dss.2020.113367.

## References

[1] B. Sheppard, H. Sarrazin, G. Kouyoumjian, F. Dore, The Business Value of Design, https://www.mckinsey.com/business-functions/mckinsey-design/our-insights/thebusiness-value-of-design. (2018)

[2] K. Williams, S. Chatterjee, M. Rossi, Design of emerging digital services: A tax onomy, Eur, J. Inf, Syst. 17 (2008) 505–517. https://doi,org/10.1057/ejis,2008.38

[3] S. Brinkkemper, Method engineering: engineering of information systems devel opment methods and tools, Inf. Softw. Technol. 38 (1996) 275–280, https://doi. org/10.1016/0950-5849(95)01059-9.

[4] R. Curedale, Service Design: 250 Essential Methods, Design Community College Inc, Topanga CA. 2013.

[5] J.R. Pierce, H. Aguinis, The too-much-of-a-good-thing efect in management, J. Manage. 39 (2013) 313–338, https://doi.org/10.1177/0149206311410060.

[6] G. Elwyn, D. Frosch, A.E. Volandes, A. Edwards, V.M. Montori, Investing in delib. eration: A definition and classification of decision support interventions for people facing dificult health decisions, Med. Decis. Mak. 30 (2010) 701–711, https://doi. org/10.1177/0272989X10386231.

[7] B. Xiao, I. Benbasat, E-commerce product recommendation agents: use, characteristics, and impact, MIS Q. 31 (2007) 137–209, https://doi.org/10.2307/25148784.

[8] W. Wang, I. Benbasat, Interactive decision aids for consumer decision making in Ecommerce: The influence of perceived strategy restrictiveness, MIS Q. 33 (2009) 293–320, https://doi.org/10.2307/20650293.

[9] H. Xia, X. Pan, Y. Zhou, Z. (Justin) Zhang, Creating the best first impression: Designing online product photos to increase sales, Decis. Support. Syst. 131 (2020) 113235. https://doi.org/10.1016/j.dss.2019.113235.

[10] L. Puro, J.E. Teich, H. Wallenius, J. Wallenius, Borrower decision aid for people-topeople lending, Decis. Support. Syst. 49 (2010) 52–60, https://doi.org/10.1016/j dss.2009.12.009.

[11] M. Petrović, N. Bojković, I. Anić, M. Stamenković, S.P. Tarle, An ELECTRE-based decision aid tool for stepwise benchmarking: An application over EU digital agenda targets, Decis. Support. Syst. 59 (2014) 230–241, https://doi.org/10.1016/j.dss. 2013.12.002.

[12] W.-K. Tan, C.-H. Tan, H.-H. Teo, Consumer-based decision aid that explains which to buy: Decision confirmation or overconfidence bias? Decis. Support. Syst. 53 (2012) 127–141, https://doi.org/10.1016/j.dss.2011.12.010.

[13] M. Holmes-Rovner, J.S. Montgomery, D.R. Rovner, L.D. Scherer, J. Whitfield, V.C. Kahn. E.C. Merkle. P.A. Ubel. A. Fagerlin. Informed decision making. Med Decis, Mak, 35 (2015) 999–1009, https://doi,org/10.1177/0272989X15597226

[14] P. Karhade, M.J. Shaw, R. Subramanyam, Patterns in information systems portfolio prioritization: Evidence from decision tree induction, MIS Q. 39 (2015) 413–433, https://doi.org/10.25300/MISQ/2015/39.2.07.

[15] F. Witlox, M. Antrop, P. Bogaert, P. De Maever, B. Derudder, T. Neutens, V. Van Acker, N. Van de Weghe, Introducing functional classification theory to land use planning by means of decision tables, Decis. Support. Syst. 46 (2009) 875–881, https://doi.org/10.1016/i.dss.2008.12.001

[16] R. Price, G. Shanks, The impact of data quality tags on decision-making outcomes and process, J. Assoc. Inf. Syst. 12 (2011) 323–346, https://doi.org/10.17705/ 1jais.00264.

[17] A. Griva, C. Bardaki, K. Pramatari, D. Papakiriakopoulos, Retail business analytics: Customer visit segmentation using market basket data, Expert Syst. Appl. 100 (2018) 1–16, https://doi.org/10.1016/j.eswa.2018.01.029.

[18] J. Huysmans, K. Dejaeger, C. Mues, J. Vanthienen, B. Baesens, An empirical evaluation of the comprehensibility of decision table, tree and rule based predictive models, Decis. Support. Syst. 51 (2011) 141–154, https://doi.org/10.1016/j.dss 2010.12.003.

[19] C. Lu, J. Park, X. Hu, User tags versus expert-assigned subject terms: A comparison of LibraryThing tags and Library of Congress subiect headings, J. Inf, Sci, 36 (2010) 763–779, https://doi.org/10.1177/0165551510386173.

[20] I. Vessey, D. Galletta, Cognitive fit: An empirical study of information acquisition, Inf. Syst. Res. 2 (1991) 63–84, https://doi.org/10.1287/isre.2.1.63.

[21] K. Hamilton, S.-I. Shih, S. Mohammed, The development and validation of the rational and intuitive decision styles scale, J. Pers. Assess. 98 (2016) 523–535 https://doi.org/10.1080/00223891.2015.1132426.

[22] T. Pajala, Explaining choice quality with decision style, cognitive reflection and decision environment, J. Oper. Res. Soc. 70 (2019) 1410–1424, https://doi.org/10. 1080/01605682.2018.1495994

[23] C.-C. Lee, H.K. Cheng, H.-H. Cheng, An empirical study of mobile commerce in insurance industry: Task-technology fit and individual differences, Decis, Support Syst. 43 (2007) 95–110. https://doi,org/10.1016/i.dss,2005.05.008.

[24] I. Benbasat, A.S. Dexter, Individual diferences in the use of decision support aids, J. Account. Res. 20 (1982) 1–11. https://doi,org/10.2307/2490759.

[25] R.C. Nickerson, U. Varshney, J. Muntermann, A method for taxonomy development and its application in information systems, Eur. J. Inf. Syst. 22 (2013) 336–359, https://doi.org/10.1057/ejis.2012.26.

[26] L.F. Spiteri, The structure and form of folksonomy tags: The road to the public library catalog, Inf. Technol. Libr. 26 (2007) 13–25. https://doi,org/10.6017/ital v26i3.3272.

[27] S.A. Golder, B.A. Huberman, Usage patterns of collaborative tagging systems, J. Inf Sci, 32 (2006)198–208, https://doi,org/10.1177/0165551506062337

[28] J. Sinclair, M. Cardew-Hall, The folksonomy tag cloud: When is it useful? J. Inf, Sci 34 (2008).15–29 https://doi org/10.1177/0165551506078083

[29] E.J. Johnson, J.W. Payne, Efort and accuracy in choice, Manag. Sci. 31 (1985) 395–414. https://doi.org/10.1287/mnsc.31.4.395

[30] N. Bonnardel, L. Lanzone, T. Sumner, Designing web sites: Opportunistic actions and cognitive efort of lay-designers, Cogn. Sci. Q. 3 (2003) 25–56.

[31] A. Westbrook, T.S. Braver, Cognitive efort: A neuroeconomic approach, Cogn. Afect. Behav. Neurosci. 15 (2015) 395–415, https://doi.org/10.3758/s13415-015- 0334-y.

[32] G.L. Lilien, A. Rangaswamy, G.H. Van Bruggen, K. Starke, DSS efectiveness in marketing resource allocation decisions: reality vs. perception, Inf. Syst. Res. 15 (2004) 216–235, https://doi.org/10.1287/isre.1040.0026.

[33] P. Todd, I. Benbasat, The influence of decision aids on choice strategies: An ex perimental analysis of the role of cognitive effort. Organ. Behav. Hum. Decis Process, 60 (1994) 36–74. https://doi.org/10.1006/obhd.1994.1074.

[34] K. Hamilton, S.-I. Shih, S. Mohammed, The predictive validity of the decision styles scale: An evaluation across task types, Pers. Individ. Dif. 119 (2017) 333–340, https://doi.org/10.1016/j.paid.2017.08.009.

[35] L. Sjöberg, Intuitive vs. analytical decision making: Which is preferred? Scand. J. Manag. 19 (2003) 17–29, https://doi.org/10.1016/S0956-5221(01)00041-0.

[36] E. Gambetti, F. Giusberti, Personality, decision-making styles and investments, J. Behav. Exp. Econ. 80 (2019) 14–24, https://doi.org/10.1016/j.socec.2019.03.002

[37] I. Vessey, Cognitive fit: A theory-based analysis of the graphs versus tables literature, Decis. Sci. 22 (1991) 219–240, https://doi.org/10.1111/j.1540-5915.1991.

tb00344.x.

[38] T.M. Shaft, I. Vessey, The role of cognitive fit in the relationship between software comprehension and modification, MIS Q. 30 (2006) 29–55, https://doi.org/10. 2307/25148716

[39] G. Mangalaraj, S. Nerur, R. Mahapatra, K.H. Price, Distributed cognition in software design: An experimental investigation of the role of design patterns and collaboration, MIS Q. 38 (2014) 249–274, https://doi.org/10.25300/MISQ/2014/38. 1.12.

[40] J. Baker, D. Jones, J. Burkman, Using visual representations of data to enhance sensemaking in data exploration tasks, J. Assoc. Inf. Syst. 10 (2009) 533–559, https://doi.org/10.17705/1jais.00204.

[41] R. Greifeneder, B. Scheibehenne, N. Kleber, Less may be more when choosing is dificult: Choice complexity and too much choice, Acta Psychol. 133 (2010) 45–50, https://doi.org/10.1016/j.actpsy.2009.08.005.

[42] J.M. Mackay, J.J. Elam, A comparative study of how experts and novices use a decision aid to solve problems in complex knowledge domains, Inf. Syst. Res. 3 (1992) 150–172, https://doi.org/10.1287/isre.3.2.150.

[43] N. Thawesaengskulthai, J.D.T. Tannock, A decision aid for selecting improvement methodologies, Int. J. Prod. Res. 46 (2008) 6721–6737, https://doi.org/10.1080/ 00207540802230553

[44] A. Burton-Jones, J. Recker, M. Indulska, P. Green, R. Weber, Assessing representation theory with a framework for pursuing success and failure, MIS Q. 41 (2017) 1307–1333, https://doi.org/10.25300/MISQ/2017/41.4.13.

[45] J.R. Bettman, E.J. Johnson, J.W. Payne, A componential analysis of cognitive efort in choice, Organ. Behav. Hum. Decis. Process. 45 (1990) 111–139, https://doi.org/ 10.1016/0749-5978(90)90007-V

[46] S.S. Iyengar, M.R. Lepper, When choice is demotivating: Can one desire too much of a good thing? J. Pers. Soc. Psychol. 79 (2000) 995–1006, https://doi.org/10.1037 0022-3514.79.6.995.

[47] M.C. Tremblay, A.R. Hevner, D.J. Berndt, The use of focus groups in design science research, Commun. Assoc. Inf. Syst. 26 (2010) 121–143, https://doi,org/10.1007 978-1-4419-5653-8 10.

[48] W. Wang, I. Benbasat, Empirical assessment of alternative designs for enhancing diferent types of trusting beliefs in online recommendation agents, J. Manag. Inf. Syst. 33 (2016) 744–775, https://doi.org/10.1080/07421222.2016.1243949.

[49] A. Engin, R. Vetschera, Information representation in decision making: The impact of cognitive style and depletion efects, Decis. Support. Syst. 103 (2017) 94–103, https://doi.org/10.1016/j.dss.2017.09.007.

[50] W. Hong, J.Y.L. Thong, K.Y. Tam, The efects of information format and shopping task on consumers’ online shopping behavior: A cognitive fit perspective, J. Manag. Inf. Syst. 21 (2004) 149–184, https://doi.org/10.1080/07421222.2004.11045812.

[51] Y. Wang, V. Chiew, On the cognitive process of human problem solving, Cogn. Syst. Res. 11 (2010) 81–92, https://doi.org/10.1016/j.cogsys.2008.08.003.

[52] R.E. Pereira, Optimizing human-computer interaction for the electronic commerce environment, J. Electron. Commer. Res. 1 (2000) 23–44.

[53] E.C. Garbarino, J.A. Edell, Cognitive efort, afect, and choice, J. Consum. Res. 24 (1997) 147–158, https://doi.org/10.1086/209500.

[54] J. Johnson, Designing with the Mind in Mind: Simple Guide to Understanding User Interface Design Rules, Morgan Kaufmann, Burlington, 2010.

[55] M.D. Robinson, J.T. Johnson, F. Herndon, Reaction time and assessments of cog nitive effort as predictors of evewitness memory accuracy and confidence, J. Appl Psychol. 82 (1997) 416–425. https://doi,org/10.1037/0021-9010.82.3.416.

[56] P. Todd, I. Benbasat, Evaluating the impact of DSS, cognitive efort, and incentives on strategy selection. Inf, Syst. Res. 10 (1999) 356–374. https://doi,org/10.1287 isre.10.4.356.

[57] C.W. Allinson, J. Hayes, The cognitive style index: A measure of intuition-analysis for organizational research, J. Manag. Stud. 33 (1996) 119–135, https://doi.org 10.1111/i,1467-6486.1996.tb00801.x.

[58] S. Epstein, R. Pacini, V. Denes-Raj, H. Heier, Individual diferences in intuitive-experiential and analytical-rational thinking styles, J. Pers. Soc. Psychol. 71 (1996) 390–405, https://doi.org/10.1037/0022-3514.71.2.390

[59] D. Hoe-Lian Goh, A. Chua, C. Sian Lee, K. Razikin, Resource discovery throug social tagging: A classification and content analytic approach. Online Inf. Rey, 33 (2009) 568–583. https://doi.org/10.1108/14684520910969961

[60] F. Simon, J.-C. Usunier, Cognitive, demographic, and situational determinants of service customer preference for personnel-in-contact over self-service technology, Int. J. Res. Mark. 24 (2007) 163–173, https://doi.org/10.1016/j.ijresmar.2006.11. 004.

[61] J.R. Marsden, D.E. Pingry, Numerical data quality in IS research and the implications for replication, Decis. Support. Syst. 115 (2018) A1–A7, https://doi.org/10. 1016/i dss 2018.10.007

[62] Limesurvey LimeSurvey - The No.1 of open source survey tools, (n.d.). https:/ www.limesurvey.org/.

[63] B. Greiner, An online recruitment system for economic experiments, in: K. Kremer, V. Macho (Eds.), Forschung Und Wissenschaftliches Rechnen [Research and Scientific Computing], Gesellschaft für wissenschaftliche Datenverarbeitung, Göttingen. 2004, pp. 79–93

[64] JN. Druckman. C.D. Kam. Students as experimental participants: A defense of the “narrow data base", in: JN. Druckman, D.P. Green, JH. Kuklinski, A. Lupia (Eds.) Cambridge Handbook of Experimental Political Science, Cambridge Universit Press, Cambridge, 2011, pp. 41–57, , https://doi.org/10.1017/ CBQ9780511921452.004.

[65] S.-N. Yao, C.-T. Lin, J.-T. King, Y.-C. Liu, C. Liang, Learning in the visual association of novice and expert designers, Cogn. Syst. Res. 43 (2017) 76–88, https://doi.org/ 10.1016/j.cogsys.2017.01.005

[66] L.R. Flynn, R.E. Goldsmith, A short, reliable measure of subjective knowledge, J.

Bus. Res. 46 (1999) 57–66, https://doi.org/10.1016/S0148-2963(98)00057-5.

[67] D. Gray, S. Brown, J. Macanufo, Games for Opening, in: C. Wheeler (Ed.), Gamestorming: A Playbook for Innovators, Rulebreakers, and Changemakers, O’Reilly Media, Inc, Sebastopol, CA, 2010, pp. 78–79.

[68] A. Wodehouse, W. Ion, Augmenting the 6-3-5 method with design information, Res. Eng. Des. 23 (2012) 5–15, https://doi.org/10.1007/s00163-011-0110-0.

[69] B. Martin, B. Hanington, Universal Methods of Design, Rockport Publisher, Beverly, 2012.

[70] IDEO, Human Centered Design Toolkit, 2nd ed., (2011) http://www.designkit.org resources/1.

[71] S. Moritz, Service Design: Practical Access to an Evolving Field, Köln International School of Design, 2005. http://www.liebertonline.com/doi/abs/10.1089/tmj. 2010.0201.

[72] J. Pan, Z. Yin, A practice on wayfinding system design with service design thinking, in: A. Marcus (Ed.), Design, User Experience, and Usability: Interactive Experience Design. DUXU 2015., Springer, Cham, 2015: pp. 400–411. https://doi.org/10. 1007/978-3-319-20889-3\_38.

[73] G. Curtis, L. Vertelney, Storyboards and Sketch Prototypes for Rapid Interface Visualization, in: CHI’90 Tutorial, ACM Press, 1990.

[74] M. Buchenau, J.F. Suri, Experience prototyping, Proceedings of the Conference on Designing Interactive Systems Processes, Practices, Methods, and Techniques - DIS ‘00, ACM Press, Brooklyn, New York, 2000, pp. 424–433, , https://doi.org/10. 1145/347642.347802

[75] R. Agarwal, V. Venkatesh, Assessing a firm’s web presence: A heuristic evaluation procedure for the measurement of usability, Inf. Syst. Res. 13 (2002) 168–186. https://doi.org/10.1287/isre.13.2.168.84.

[76] U.B. Sangiorgi, F. Beuvens, J. Vanderdonckt, User interface design by collaborative sketching, Proceedings of the Designing Interactive Systems Conference on - DIS′12, ACM Press, Newcastle, 2012, pp. 378–387, , https://doi.org/10.1145/2317956. 2318013.

[77] J. Rieman, M. Franzke, D. Redmiles, Usability evaluation with the cognitive walkthrough, Conference Companion on Human Factors in Computing Systems - CHI ‘95, ACM Press, New York, New York, USA, 1995, pp. 387–388, , https://doi. org/10.1145/223355.223735.

[78] N.A. Curtis, Modular Web Design - Creating Reusable Components for User Experience Design and Documentation, New Riders, Berkeley, CA, 2010.

[79] H. Petrie, J. Precious, Measuring user experience of websites, Proceedings of the 28th of the International Conference Extended Abstracts on Human Factors in Computing Systems - CHI EA '10. ACM Press. Atlanta, GA. 2010, pp. 3673–3678., https://doi.org/10.1145/1753846.1754037

[80] A. Hyrskykari, S. Ovaska, P. Majaranta, K.-J. Räihä, M. Lehtinen, Gaze path sti mulation in retrospective think-aloud, J. Eye Mov. Res. 2 (2008) 1–18.

[81] G. de Vries, M. Hartevelt, R. Oosterholt, Private camera conversation: A new method for eliciting user responses? Behav. Inf. Technol. 14 (1995) 358–360, https://doi.org/10.1080/01449299508914654.

[82] J. Nielsen, Putting A/B Testing in its Place, (2005), pp. 1–5 https://www.nngroup. com/articles/putting-ab-testing-in-its-place/ (accessed June 12, 2020).

[83] P. Koutsabasis, T. Spyrou, J.S. Darzentas, J. Darzentas, On the performance of no vice evaluators in usability evaluations, Proceedings of the 11th Panhellenic Conference on Informatics, 2007, pp. 1–10.

[84] E.K. Macdonald. H.N. Wilson, U. Konus, Better customer insights - in real time Harvard Business Review. (2012) https://hbr,org/2012/09/better-customer insight-in-real-time . Accessed date: 14 June 2020.

[85] M. Isomursu. K. Kuutti, S. Väinämö. Experience clip: Method for user participatior and evaluation of mobile concepts, Proceedings of the Eighth Conference on Participatory Design Artful Integration: Interweaving Media. Materials and Practices - PDC 04, ACM Press, Toronto, Canada, 2004, pp. 83–92, , https://doi. org/10.1145/1011870.1011881

[86] A. Burton-Jones, D.W. Straub, Reconceptualizing system usage: An approach and empirical test, Inf. Syst. Res. 17 (2006) 228–246, https://doi.org/10.1287/isre. 1060.0096.

[87] C. Yi, Z. (Jack) Jiang, I. Benbasat, Enticing and engaging consumers via online product presentations: The efects of restricted interaction design, J. Manag. Inf. Syst. 31 (2015) 213–242, https://doi.org/10.1080/07421222.2014.1001270.

[88] R.M. Baron, D.A. Kenny, The moderator–mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations, J. Pers. Soc. Psychol. 51 (1986) 1173–1182, https://doi.org/10.1037/0022-3514.51.6. 1173.

[89] S. Siegel, N.J. Castellan, Nonparametric Statistics for the Behavioral Sciences, 2nd ed, McGraw-Hill, New York, 1988.

[90] X. Zhao, J.G. Lynch, Q. Chen, Reconsidering Baron and Kenny: Myths and truths about mediation analysis, J. Consum. Res. 37 (2010) 197–206, https://doi.org/10. 1086/651257

[91] D. Tingley, T. Yamamoto, K. Hirose, L. Keele, K. Imai, Mediation: R package for causal mediation analysis, J. Stat. Softw. 59 (2014) 1–38, https://doi.org/10. 18637/jss.v059.i05.

[92] H. Aguinis, R.K. Gottfredson, Best-practice recommendations for estimating interaction efects using moderated multiple regression, J. Organ. Behav. 31 (2010) 776–786, https://doi.org/10.1002/job.686.

[93] K.D. Bailey, Typologies and Taxonomies: An Introduction to Classification Techniques, Sage, Thousand Oaks, CA, 1994.

[94] A. Bruun, J. Stage, Barefoot usability evaluations, Behav. Inf. Technol. 33 (2014) 1148–1167, https://doi.org/10.1080/0144929X.2014.883552

[95] F. Faul, E. Erdfelder, A.-G. Lang, A. Buchner, G\*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences, Behav. Res. Methods 39 (2007) 175–191, https://doi.org/10.3758/BF03193146.

[96] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, 2nd ed, Lawrence Erlbaum Associates, Hillsdale, NJ, 1988.

Xuanhui Liu (liuxuanhui@zju.edu.cn) is a post doc at the Zhejiang University. Xuanhui received her doctorate degree in information systems at the Karlsruhe Institute of Technology, Institute of Information Systems and Marketing. Her research interests in clude digital service design and used-centered systems. Her research has been published in International Conference on Information Systems, European Conference on Information Systems, etc.

Karl Werder (werder@wiso.uni-koeln.de) is a research fellow in the research group Information Systems and Systems Development at the University of Cologne. Prior, he worked as a senior researcher at paluno, the Ruhr Institute for Software Technology (University of Duisburg-Essen) and as a research assistant at the Institute for Enterprise Systems (University of Mannheim). Karl received his doctorate degree in Informatior Systems from the Karlsruhe Institute of Technology. His research interests include software development, systems design, game research, and data analytics. His work has been published in leading Journals (e.g., IEEE Transactions on Software Engineering, California Management Review. Information Technology & People, Information & Software Technology) and international conferences.

Alexander Maedche (alexander.maedche@kit.edu) is full professor of Information Systems at the Karlsruhe Institute of Technology. Previously he was full professor of Information Systems and managing director of the Institute of Enterprise Systems at the University of Mannheim. His research focuses on designing user-centered and intelligent digital service systems. He has published more than 100 papers in journals and conferences, such as the Decision Support Systems, Computers in Human Behavior, International Journal of Human-Computer Studies, Journal of the Association for Information Systems, and Information and Software Technology.
