---
otero_id: 5984
otero_key: "8WNMUGRZ"
title: "Can the outside‐view approach improve planning decisions in software development projects?"
authors: "Ofira Shmueli; Nava Pliskin; Lior Fink"
year: "2016"
journal: "Information Systems Journal"
doi: "10.1111/isj.12091"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Can the outside-view approach improve planning decisions in software development projects?

O<sup>fi</sup>ra Shmueli, Nava Pliskin & Lior Fink\*

Department of Industrial Engineering and Management, Ben-Gurion University of the Negev, Beer-Sheva 84105, Israel, email: <sup>fi</sup>nkl@bgu.ac.il

Abstract. This study empirically tackles the question of whether taking an outside-view approach, recommended for reducing the irrational behaviours associated with the planning fallacy, can also reduce the time underestimation, scope overload and over-requirement problems plaguing planning decisions in software development. Drawing on descriptive behavioural decision theory, this study examines whether the planning fallacy, a cognitive bias referring to the tendency of people to underestimate costs and overestimate bene<sup>fi</sup>ts in evaluating a task to be performed, can provide a theoretical platform for mitigating irrational behaviours in the planning of software development projects. In particular, we argue that taking an outside-view approach in planning decisions for software development may have the same mitigating effects on time underestimation, scope overload and over-requirement it has been shown to have on cost underestimation and bene<sup>fi</sup>t overestimation. In an experiment investigating this argument, participants were randomly assigned to four groups by manipulating two outside-view mechanisms: reference information about past completion times (present/absent) and role perspective (developerlconsultant). After being presented with a to-be-developed software project, they were requested to estimate development times of various software features and to recommend which features to include within project scope given a <sup>fi</sup>xed duration for the entire project. The results con<sup>fi</sup>rm that the three problems of time underestimation, scope overload and over-requirement are manifested in planning decisions for <sup>fi</sup>xed-schedule software development projects. Moreover, the results show that these problems are mitigated, yet not eliminated, by presenting reference information about past completion times and by having a consultant role.

Keywords: software development, planning decisions, time underestimation, scope overload, over-requirement, planning fallacy, outside view, inside view, reference information, role perspective, experiment

## INTRODUCTION

Planning decisions in software development projects suffer from the disturbing problems of time underestimation, scope overload and over-requirement that may lead to project failure and to signi<sup>fi</sup>cant economic and non-economic penalties. The phenomenon of time underestimation, which refers to the tendency of developers to underestimate the time needed for project com pletion and to produce overly optimistic development schedules, is one of the most common reasons for project failure (Charette, 2005; Nelson, 2007). The phenomenon of scope overload, which refers to the excessive inclusion of software features within the scope of a project while consuming more resources than those available (Buschmann, 2009; Bjarnason et al., 2010; Buschmann, 2010; Bjarnason et al., 2012), may lead to serious and expensive consequences such as quality issues, delays and failure to meet customer expectations (Elliott, 2007; Buschmann, 2010; Coman & Ronen, 2010; Bjarnason et al., 2012). The phenomenon of over-requirement, referring to the development of super<sup>fl</sup>uous software features beyond the actual needs of the customer or the market and also termed over-speci<sup>fi</sup>cation or gold-plating, is known to load projects with extra development efforts for no good reason and reduce the conceptual integrity of the product (Boehm & Papaccio, 1988; Ronen & Pass, 2008).

Both scope overload and over-requirement unavoidably lead to larger projects and to increased project risk (Zmud, 1980; McFarlan, 1981; Barki et al., 1993; Houston et al., 2001). In comparison to smaller projects, large-scale projects fail three to <sup>fi</sup>ve times more often (Charette, 2005), are much more prone to unexpected colossal events, including the demise of an entire organization (Flyvbjerg & Budzier, 2011) and have a 65% probability of being stopped and abandoned (Jones, 2007 cited by Coman & Ronen, 2009). The time underestimation, scope overload and over-requirement phenomena are hardly reversible. Underestimation of completion times early in the project tends to persist and leads to sustained false optimism later on in the project (Kutsch et al., 2011). Scope overload and over-requirement have as well a tendency to be sustained since, once introduced during the requirement engineering phase or later, extra features or even unneeded ones are very rarely cut off scope (Wetherbe, 1991; Dominus, 2006).

Despite evolutionary progress in software development methods and improvement in forecasting models, neither the accuracy of project completion times nor the quality of project scoping have been improved (Flyvbjerg, 2006; Jørgensen & Grimstad, 2008; Buschmann, 2009). A comprehensive review of the literature on judgment-based time prediction shows that underestimation has been reported more frequently than overestimation in software engineering and management research (Halkjelsvik & Jørgensen, 2012). Studies report that time underestimation and schedule overruns are more signi<sup>fi</sup>cant in larger software projects than in smaller ones (Heemstra & Kusters, 1991; Gray et al., 1999; Sauer et al., 2007). Therefore, decomposing large projects into smaller parts and using a bottom-up approach are recommended practices for time estimation (Hill et al., 2000; Bajaj et al., 2006; Halkjelsvik & Jørgensen, 2012), with empirical evidence con<sup>fi</sup>rming the improved accuracy of such procedures (Connolly & Dean, 1997; Hill et al., 2000; Jørgensen, 2004). Time estimation in software development projects is an elusive task, characterized by irrational and unexpected behaviour, such as the observation that project managers may be more biased towards underestimation than developers (Jørgensen & Moløkken-Østvold, 2004). The literature also addresses the biasing effect of irrelevant information (e.g. about systems that will not be integrated with the developed software) or misleading information (e.g. about unsubstantiated client expectations) on the time estimations of students and professionals, despite being instructed to ignore the irrelevant or misleading information (Jørgensen & Sjøberg, 2004; Jørgensen & Grimstad, 2008).

Thus, one is motivated to look for additional theoretical platforms based upon which time under estimation, scope overload and over-requirement could be explained and addressed. According to the literature about software development and project management, most roots of these three common, risky and costly planning <sup>fl</sup>aws can be traced to human nature and behaviour. Time underestimation is mainly attributed in this literature to the optimism bias, where future events are being judged in a more positive light than warranted by actual experience, or to strategic misrepresentation, where forecasters deliberately underestimate costs in order to gain approval and funding (Flyvbjerg, 2006). Scope overload and over-requirement are attributed in this literature to the professional interest and perfection aspiration of developers and to the inclination of users to ask for as much as possible (Ropponen & Lyytinen, 2000; Coman & Ronen, 2010). Soft ware developers often strive for the best possible solution (Westfall, 2005; Rust et al., 2006; Ronen & Pass, 2008), adding just-in-case functionality to ful<sup>fi</sup>l all potential future needs (Buschmann, 2010; Coman & Ronen, 2010), and users often exhibit an all-or-nothing attitude (Cule et al., 2000), adding costly bells and whistles to system requirements (Markus & Keil, 1994)

In line with the call by Goes (2013) for the consideration of behavioural economics in the context of information systems (IS), we propose and study in this work another possible reason for the persistence of time underestimation, scope overload and over-requirement. The behavioura bias targeted here, termed the planning fallacy, refers to people’s tendency to underestimate the time needed to complete a task (Kahneman & Tversky. 1979) and to overestimate its potential bene<sup>fi</sup>ts (Lovallo & Kahneman, 2003). The planning fallacy is manifested despite having experience or knowledge about previous projects, holds for novices as well as experts and has been demonstrated in a wide variety of tasks (Connolly & Dean, 1997; Pezzo et al., 2006b; Buehler et al., 2010a). Overly optimistic estimations, where development time is underestimated and potential bene<sup>fi</sup>ts are overestimated, are quite prevalent and hold for all project types: short (few days) to long (few years) in duration, inexpensive (few thousand dollars) to expensive (millions of dollars) and in the private or public sectors (Buehler et al., 2010a). Given the prevalence of the planning fallacy, we are motivated in this study to draw on this branch of descriptive behavioural decision theory (Slovic et al., 1977) for understanding how this fallacy is manifested in software development and how these manifestations can be alleviated.

With this motivation in mind, we argue that the phenomena of time underestimation, scope overload and over-requirement are the manifestations in the speci<sup>fi</sup>c context of software development of people’s general tendency to underestimate completion times and overestimate potential bene<sup>fi</sup>ts. Underestimation of completion times in software development projects may also lead to the illusion that an overloaded project scope is feasible. Overestimating the potential bene<sup>fi</sup>ts of software features may lead to scope overload and over-requirement because of a higher motivation to include in project scope, respectively, features that cannot be actually developed within schedule and features that are actually unnecessary.

We furthermore look for remedies of the planning fallacy as means to reduce these three phenomena. Two such remedies stem from Kahneman and Tversky’s (1979) fundamenta distinction between the inside-view and the outside-view approaches for estimating future tasks. They claim that the main cause of the planning fallacy is the intuitive inside-view approach to evaluating a project, by which people look inward and focus on project details and obstacles that can be envisioned while neglecting past experience and knowledge about previous prediction failures (Kahneman & Tversky, 1979; Buehler et al., 1994; Grif<sup>fi</sup>n & Buehler, 2005). Kahneman and Tversky (1979) and, later on, Lovallo and Kahneman (2003) thus proposed remedies by which the evaluator is guided to look outward rather than inward.

Two mechanisms mentioned in the literature as having the potential to reduce the magnitude of the planning fallacy because of an outward look are the ‘reference class forecasting procedure’ and the ‘actor–observer perspective’. The <sup>fi</sup>rst mechanism guides the evaluator to sys tematically consider reference information regarding outcomes of similar tasks (e.g. completion times and costs) by identifying the reference class of similar cases and assessing their distribution (Kahneman & Tversky, 1979; Flyvbjerg, 2006). The second mechanism refers to the evaluator’s role perspective, arguing that observers estimating the expected performance of others are less prone to the planning fallacy than the actors who are going to perform the task themselves (Buehler et al., 1994, 1995, 2012). Because of the relevance of the planning fallacy to the software development context, we argue that both mechanisms might reduce the magnitude of time underestimation, scope overload and over-requirement. We further develop this argument and suggest that the <sup>fi</sup>rst mechanism refers to having or not having reference information about completion times of similar software development tasks, while the second mechanism refers to having a role perspective of a software consultant (observer) or a software developer (actor). Our research question is therefore: Can two mechanisms of the outside-view approach, suggested to mitigate the planning fallacy – having reference information about completion times and having a role perspective of a software consultant – reduce the magnitude of time underestimation, scope overload and over-requirement in software development planning decisions?

To empirically investigate this research question, we conducted an experiment in the context of software development in which the two outside-view mechanisms were manipulated. The experimental method is elaborated upon after the next section, which presents the theoretical background and hypotheses for this study. The results of this experiment, presented in the fourth section, contribute to research and practice in three ways. First. this is one of the first at tempts to apply both theory and methodology from behavioural economics to better understand the behavioural roots of what appears to be irrational decision making in software development. Second, this study explicates the relevance of the planning fallacy to software development by highlighting three major problems in software development projects, associating these problems with both time underestimation and bene<sup>fi</sup>t overestimation, thereby advancing the literature that focuses on time underestimation as the main implication of the planning fallacy. Third, we formally de<sup>fi</sup>ne two outside-view mechanisms that have the potential to mitigate the manifestations of the planning fallacy, and empirically confirm this potential in the planning of a <sup>fi</sup>xed-schedule software development project. This study thus contributes to both the IS literature and the general literature on the planning fallacy. The paper concludes not only with a discussion of the results and contributions of this work. but also with a review of its limitations and recommendations for future research.

## THEORETICAL BACKGROUND AND HYPOTHESES

## The planning fallacy

The planning fallacy was <sup>fi</sup>rst proposed by Kahneman and Tversky (1979), who explored the factors that limit the accuracy of intuitive judgments under uncertainty, referring initially to the tendency of people to underestimate the time needed to complete a task even in the presence of knowledge about past prediction failures and about overrun experience with similar tasks. Drawing on behavioural decision theory research, they emphasized the systematic and predictable nature of the planning fallacy and argued that it affects both experts and laypersons. The boundaries of the planning fallacy were expanded more recently, referring also to factors other than time, such as costs, risks and bene<sup>fi</sup>ts, and its de<sup>fi</sup>nition was broadened to encompass people’s tendency to underestimate time, costs and risks of future actions and, at the same time, to overestimate their bene<sup>fi</sup>ts (Lovallo & Kahneman, 2003; Kahneman, 2011).

Various psychological explanations were suggested for the planning fallacy. Kahneman and Tversky’s (1979) explanation, which refers to the inside-view evaluation approach, seems to be the most comprehensive and robust (Buehler et al., 2010a). People who evaluate a project using the inside-view approach look inward and focus on project details and obstacles that can be envisioned, neglecting past experience and knowledge about previous prediction failures. Additional psychological biases suggested to be related to the planning fallacy include: optimism bias – people’s tendency to judge future events in a more positive light than warranted; overcon<sup>fi</sup>dence effect – people’s tendency to be overcon<sup>fi</sup>dent in their own abilities and prediction accuracy and illusion of control – people’s tendency to overestimate the degree to which they have control over future events (Kahneman & Tversky, 1979; Lovallo & Kahneman, 2003). Another behavioural phenomenon possibly related to the planning fallacy is people’s desire to present themselves positively to others (Pezzo et al., 2006a).

The planning fallacy has been found to affect both individuals and groups (Sanna et al., 2005) and has been demonstrated for a wide variety of tasks (Buehler et al., 2010a), including origam folding (Pezzo et al., 2006b), school work, tax-form completion and computer programming (Connolly & Dean, 1997). Because of the tendency of organizations to suppress pessimistic opinions and to reward optimistic ones, employees’ optimistic biases are adopted and validated by the group, further reinforcing the planning fallacy (Lovallo & Kahneman, 2003). Holding a power position was found to increase bias in predictions of task completion time, suggesting that managers and others typically in charge of planning are more prone to time underestimation (Weick & Guinote, 2010). This <sup>fi</sup>nding is in line with another <sup>fi</sup>nding that managers and experienced entre preneurs are more prone to overcon<sup>fi</sup>dence than others (Shepherd et al., 2003; Nouri et al., 2012).

Overall, the planning fallacy has been reported to be associated with negative results. Time underestimation generally does not shorten the actual time a task takes. Although shorter time estimations may initiate action, their impact diminishes over the course of extensive multi-stage projects (Buehler et al., 2010b). Moreover, time underestimation early in a project tends to persist and leads to sustained false optimism in later project phases (Kutsch et al., 2011). Overestimation of bene<sup>fi</sup>ts in the planning or design phases presents the project as more attractive than it actually is or with exaggerated future throughput, possibly leading to poor investment decisions or to an overkill infrastructures design (Flyvbjerg, 2006).

As elaborated upon next, this work considers time underestimation, scope overload and over-requirement in software development planning as re<sup>fl</sup>ections of time underestimation and bene<sup>fi</sup>t overestimation associated with the planning fallacy.

## The planning fallacy and time underestimation

The planning fallacy is relevant to time underestimation in any context, including software development projects. In other words, because of the planning fallacy, software professionals are likely to underestimate the time needed to complete development tasks. The tendency to underestimate time and to produce overly optimistic development schedules was noted as one of the most common reasons for project failure in software development (Charette, 2005; Nelson, 2007). Unfortunately, as observed in studies of the planning fallacy, experience gained in software development does not improve time estimation, probably because of the perceived irrelevance of the past to the present considered-unique project (Buehler et al., 2010a). While the relevance of the planning fallacy to time underestimation in software development is clear, we argue in the next two sub-sections that the planning fallacy is of relevance to scope overload and over-requirement as well.

## The planning fallacy and scope overload

Software practitioners tend to include too many features within project scope, loading it with requirements that usually consume more resources than available (Buschmann, 2009; Bjarnason et al., 2010; Buschmann, 2010; Bjarnason et al., 2012). In software development projects, scope de<sup>fi</sup>nition is mainly undertaken early during the initiation phase of the project develop ment lifecycle, when features are being envisioned (Zwikael & Smyrk, 2011) and, in most cases, after a decision regarding project duration was already taken. The approach frequently practiced of setting the schedule as an independent variable (Boehm, 1999; Myers, 1999; Boehm, 2000; Yang et al., 2007; Boehm & Valerdi, 2008), enables meeting targets by <sup>fi</sup>rst identifying the customer’s longest acceptable schedule and then scoping the project according to developers’ estimations of feature development times and priorities. The planning fallacy may interfere with and reduce the effectiveness of scoping the project after duration has already been constrained. Because of the planning fallacy, by which people underestimate the time needed for development and, as a result, overestimate how much they can accomplish within a given period of time (Hayes-Roth & Hayes-Roth, 1979; Nouri et al., 2012), the software pro fessional overloads the project scope with more features than can be successfully completed on time. This phenomenon may also be the consequence of overestimating the potential ben e<sup>fi</sup>ts of features, which increases the motivation of the software professional to include addi tional features within project scope. Thus, the planning fallacy is of relevance to scope overload.

## The planning fallacy and over-requirement

Software practitioners tend to over-require and include super<sup>fl</sup>uous and unnecessary features within the project scope (Buschmann, 2009, 2010; Coman & Ronen, 2010). Over-requirement, which pertains currently to at least 30% of developed features in software projects (Coman & Ronen, 2009), was already included in the early 1990s by Boehm (1991) among the top 10 software development risks and has continued to be mentioned as a top risk ever since (Houston et al., 2001; Schmidt et al., 2001; Baccarini et al., 2004; Khanfar et al., 2008; Wheatcraft, 2011: Bernstein, 2012: Malhotra et al., 2012: Kaur et al., 2013: Pass & Ronen, 2014). Overrequirement may lead to delayed project launch and resource overruns, overall excessive complexity, increased probability of defects and reliability problems, systems larger than needed that are more dif<sup>fi</sup>cult to manage and more costly to maintain and even loss of an entire company (Battles et al., 1996; Westfall, 2005; Buschmann, 2009; Coman & Ronen, 2009; Buschmann, 2010; Coman & Ronen, 2010). Numerous examples of over-requirement can be found in the literature. Bank of America’s Master Net project is a good example, with about 3.5 million source lines of wish-list features, most of which without mission effectiveness rationale (Boehm et al., 2000; Boehm & Lane, 2010).

Scope overload, which involves the overload of both needed and unneeded software features (Bjarnason et al., 2010, 2012), is obviously related to over-requirement. However, it is important to emphasize that over-requirement does not necessarily involve exceeding project resources and might be manifested within the boundaries of project resources. The planning fallacy is relevant to over-requirement because it involves the overestimation of bene<sup>fi</sup>ts. Because scoping decisions are about which features to include within a project and about which features to exclude, perceiving features as more bene<sup>fi</sup>cial than they actually are and evaluating them beyond their actual value, might bias planning decisions by the inclusion of super<sup>fl</sup>uous features.

Over-requirement is discussed here in more detail because of being more economically absurd and irrational than time underestimation and scope overload. Under the practice of over-requirement, the project would devote scarce resources to develop extra functionality or throughput of no real value (Westfall, 2005). With the project defocused and distracted from requirements of real value (Elliott, 2007), core features might have to be cut off if and when pressing project time constraints emerge (Coman & Ronen, 2009, 2010). Next, the outside-view approach is elaborated upon as a possible planning fallacy remedy for all the three phenomena involving time underestimation and bene<sup>fi</sup>t overestimation.

## The outside-view approach

Attempts to eliminate the planning fallacy by, for example, asking participants to predict a worst case scenario or to recall memories regarding past projects have failed (Pezzo et al., 2006a). Kahneman and Tversky (1979) provided an account of psychological processes that could explain such failures. They distinguished between two types of information available to a forecaster: (1) singular case information, which consists of evidence about a particular case under consideration, and (2) distributional statistical information, which consists of evidence about outcomes in similar situations. In their research, they found that people tend to focus on the information associated with the speci<sup>fi</sup>c problem at hand, termed the inside-view approach, rather than on the information about the outcomes of similar cases, termed the outside-view approach (Kahneman & Lovallo, 1993; Lovallo & Kahneman, 2003; Kahneman, 2011). Evaluations done in accordance with the inside-view approach, they argued, are likely to result in unrealistic predictions. This argument is consistent both with the observation that the planning fallacy occurs even in the presence of knowledge about past inaccurate predictions and past overruns (Kahneman & Tversky, 1979) and with the planning fallacy’s paradoxical nature of optimism about the future alongside realism about the past (Buehler et al., 2010a). Thus, they suggested harnessing the outside-view approach as a means to reduce inaccurate evaluations because of the planning fallacy.

The inside-view and outside-view approaches for assessing future costs and outcomes are quite different. While the former draws on knowledge about the speci<sup>fi</sup>c case at hand, focusing on its uniqueness and on future scenarios for its accomplishment, the latter draws on statistica knowledge about similar case outcomes, treating the current case as one of many (Kahneman & Tversky, 1979; Kahneman & Lovallo, 1993; Lovallo & Kahneman, 2003). When both are applied with equal skill, the outside-view approach is more likely than the inside-view approach to produce realistic estimations (Kahneman & Lovallo, 1993), as has been demonstrated in real-world examples and in laboratory experiments (Kahneman & Lovallo, 1993; Buehler et al., 1994; Flyvbjerg, 2013). Although the outside-view approach does not guarantee complete accuracy, forcing the estimator to face reality helps overcome the cognitive bias and provides some protection against unrealistic forecasts (Kahneman & Tversky, 1979; Kahneman & Lovallo, 1993; Flyvbjerg, 2013).

Unfortunately, in planning new projects, most individuals and organizations are inclined to adopt the inside-view approach (Flyvbjerg, 2006; Kahneman, 2011; Flyvbjerg, 2013), which is not only the traditional approach but also the intuitive one (Lovallo & Kahneman, 2003). It is an intuitive approach because the natural way to think about a project is to focus on the project itself, bring to bear knowledge about it, pay special attention to its unique or unusual features and try to predict the events that will in<sup>fl</sup>uence its future. Unless instructed to gather simple statistics about related projects, going outside the speci<sup>fi</sup>c project seldom enters the planner’s mind.

Based on the literature, we propose two speci<sup>fi</sup>c mechanisms that are likely to elicit an outside-view approach and, consequently, reduce irrationality problems associated with the planning fallacy. The <sup>fi</sup>rst mechanism is based on the ‘reference class forecasting procedure (Kahneman & Tversky, 1979) and the second mechanism is based on the ‘actor–observer perspective’ (Buehler et al., 1995, 2012). In the next section, the research model is formulated to describe the hypothesized bias-reducing effects of employing these two mechanisms in the speci<sup>fi</sup>c context of <sup>fi</sup>xed-schedule software development projects.

## Research mode

Drawing on the planning fallacy and on the tendency of people to underestimate costs and over estimate bene<sup>fi</sup>ts in planning decisions, we develop a research model that examines the biasreducing effects of two outside-view mechanisms on time underestimation, scope overload and over-requirement in planning for software development. In other words, we rely on the planning fallacy to argue that software engineers (a generic term used hereinafter in reference to both developers and consultants in software development projects) underestimate development times, as well as overestimate the number of features and over-required features that can be developed within a pre-determined project duration. We then hypothesize that two outside-view mechanisms reduce the magnitude of these three manifestations of the planning fallacy. The <sup>fi</sup>rst mechanism relates to whether or not the software engineer considers reference information about past similar cases – i.e. completion times of similar software development tasks in the past. The second mechanism relates to whether the software engineer has the role perspective of an actor or an observer – i.e. a role of software developer or software consultant. Thus, the hypotheses presented in Figure 1 describe the in<sup>fl</sup>uence of two independent variables on three dependent variables. The two independent variables are reference information (present or absent) and role perspective (developer or consultant). The three dependent variables, which respectively re<sup>fl</sup>ect the time underestimation, scope overload and over-requirement problems encountered in planning software development projects, are total time estimation, number of features included within scope, and number of over-required features included within scope.

## Reference information

Kahneman and Tversky (1979) suggested the reference class forecasting procedure according to which the evaluator systematically uses outside-view information. They recommended that the evaluator identify similar cases to which the case at hand can be referenced to, assess the distribution of outcomes for that reference class, compare characteristics of the case at hand to those in the reference class, and elicit a corresponding prediction (Kahneman & Tversky, 1979). The resulting predictions are more realistic than when using inside-view information (Kahneman & Tversky, 1979; Kahneman & Lovallo, 1993; Lovallo & Kahneman, 2003; Flyvbjerg, 2006, 2013).

Prediction improvement because of the exposure to outside-view information was demonstrated, for example, when students were asked to rate their future academic performance. Those who were not led to consider outside-view information expected, on average, to perform better than about 80% of their peers. Those who were required to answer a precedent question regarding the entrance scores of themselves and their peers, expected, on average, to perform better than about 60% of their peers. Although participants in both groups of subjects were aware of the entrance scores, ‘the simple detour into pertinent outside-view information’ resulted in a more realistic forecast, though still overcon<sup>fi</sup>dent (Lovallo & Kahneman, 2003, p. 61).

![](/api/attachments/8WNMUGRZ/fulltext/images/dbe64deb5b52db09d08deebfa8a02b2c6deb5aff1bbfce646b68037f0ca66d6b.jpg)  
Figure 1. Research model.  
© 2015 Wiley Publishing Ltd, Information Systems Journal 26, 395–418

This study and others (Buehler et al., 1995; Flyvbjerg, 2006) demonstrate that people intui tively tend to ignore relevant knowledge or experience gained in the past. Moreover, they tend to interpret their own past prediction failures in a manner that diminishes their relevance to the present prediction (Buehler et al., 1994, 1995), actually treating the current problem as unique (Kahneman & Tversky, 1979; Kahneman & Lovallo, 1993). This human tendency to ignore the past and to perceive the current project as unique has been demonstrated in the context of soft ware development as well (Buehler et al., 2010a).

Although experience and knowledge about the past are intuitively neglected in the face of a new situation, the presence of reference information has been observed to mitigate the problem of overly optimistic predictions. Whether the reference information is about similar cases expe rienced by others or about one’s own experience, its presence seems to shift the evaluator’s thoughts towards outside-view thinking, producing better estimations. Such mitigation is likely to hold for all aspects of the planning fallacy, including estimations of time, capacity and bene-<sup>fi</sup>ts. Lovallo and Kahneman (2003) therefore recommended using the outside-view approach, explicitly harnessing past knowledge when estimating future costs and while deciding about investment in competing initiatives (Lovallo & Kahneman, 2003; Kahneman, 2011).

On the basis of the reasoning presented above, in the speci<sup>fi</sup>c context of software develop ment projects, the presence of reference information about completion times in similar past projects is expected to mitigate the three problems plaguing planning decisions and reduce time underestimation, scope overload and over-requirement. Thus, we hypothesize that providing software engineers with reference information about past completion times shifts their thoughts towards outside-view thinking and improves the quality of their time estimations and project scoping decisions.

H1a: Software engineers without reference information about completion times in similar past projects will provide lower total time estimations for softwaredevelopment tasks than those with reference information

H1b: Software engineers without reference information about completion times in similar past projects will plan more features to be included within project scope than those with reference information

H1c: Software engineers without reference information about completion times in similar past projects will plan more over-required features to be included within project scope than those with reference information

## Role perspective

The perspective of the person making the prediction is also important for its accuracy. In soft ware development projects, planning decisions are generally ascribed to managers or project leaders. In practice, however, software developers and skilled consultants are often asked fo their assessments during the planning process and these estimations are either adjusted by the planner or accepted. According to Lovallo and Kahneman (2003), managers typically get, at least as a starting point, a preliminary plan drawn up by the person or team proposing the initiative. They further argue that because this proposed preliminary plan is most likely biased, because of the planning fallacy, the <sup>fi</sup>nal forecasts tend towards over-optimism either because of insuf<sup>fi</sup>cient adjustments or because of the planning fallacy bias by the managers themselves.

An important distinction in this context is between actors and observers. The classic notion of actor–observer asymmetry refers to the differences between the tendency of actors to attribute their actions to the speci<sup>fi</sup>c situation and the tendency of observers to attribute the same actions to the overall dispositions of the actors (Jones & Nisbett, 1971). For example, a student who studies hard for an exam is likely to explain her own behaviour by referring to the speci<sup>fi</sup>c situation of an upcoming dif<sup>fi</sup>cult exam, whereas other people are likely to attribute it to her dispositions, such as being hardworking or ambitious.

Buehler et al. (1994) demonstrated the differences between actors and observers in making time estimations. They and others (Buehler et al., 1995, 2010a, 2012) found that observers are less prone than the actors themselves to produce time underestimations for tasks performed by the actors. Buehler et al. (1994, 2010a) attribute these differences to different motivations, with observers generally less attentive than actors to the plans of the actors and more attentive to potential obstacles and to the actors’ past experiences and previous performance. In terms of the distinction between the inside view and the outside view, the actor is more inclined to focus on the speci<sup>fi</sup>c situation (inside view) while the observer is more inclined to take into account past performance in similar situations (outside view). Actually, simply imagining an upcoming task from the perspective of another person was found to reduce time underestimation and generate more realistic predictions by reducing cognitive and motivational processes that typically contribute to bias (Buehler et al., 2012).

Consistent with the above reasoning and <sup>fi</sup>ndings, we hypothesize that observers (i.e. consul tants who will not engage in actual software development) are likely to produce less biased predictions than actors (i.e. developers who will actually develop the software). Speci<sup>fi</sup>cally, the role perspective of a software consultant is expected to mitigate the three problems plaguing planning decisions in software development and reduce time underestimation, scope overload and over-requirement. Thus, having a role perspective of a software consultant is hypothesized to lead to less biased time estimations and project scoping decisions than having a role perspective of a software developer.

H2a: Software developers will provide lower total time estimations for their software-development tasks than software consultants

H2b: Software developers will plan to include more features within the scope of their software-development projects than software consultants

H2c: Software developers will plan to include more over-required features within the scope of their software-development projects than software consultants

## METHOD

Consistent with the dominant methodology in behavioural economics research, we conducted a controlled experiment to empirically test the research hypotheses. Overall, 100 advanced engi neering undergraduates, majoring in IS at a leading Israeli university, participated in the expe riment which took place as part of the mandatory junior-year course ‘Automation and Computer-integrated Manufacturing’. For the most part, because cognitive biases are brie<sup>fl</sup>y covered in a mandatory senior-year course, participants were not yet exposed to problems in decision making because of behavioural effects, including the planning fallacy.

It is worth noting that undergraduate engineering students in Israel are older on average than their typical counterparts elsewhere in the world (about two-thirds of the participants in our experiment were 26 years old or older). Most of them, especially IS majors in the junior and senior years, work part time in industry while in school and thus gain practical experience in software development. Because it is dif<sup>fi</sup>cult to collect data from employees in industry when a controlled environment is required, relying on students as participants is acceptable in experiments exploring decision making by employees in the software development industry (Keil et al., 2000; Williams et al., 2000; Andres, 2001; Khatri et al., 2006; Keil et al., 2007; Umapathy et al., 2008) or exploring behavioural biases by IS investment experts (Legoux et al., 2014). Moreover, in the current study, recruiting students as participants while manipulating the role perspective (developers or consultants) helped control alternative explanations related to moral hazard and opportunistic behaviour because real consultants might bene<sup>fi</sup>t <sup>fi</sup>nancially from enlarging a project (Gary, 2009; Kautz, 2009). With experienced developers and consultants as participants, it would have been impossible to experimentally manipulate the independent variable of role perspective (because of the self-selection of participants into roles), thus undermining the internal validity of our causal conclusions.

Following a pilot study aimed to test the experimental design and the manipulations, with a sample of 15 students from the same population as in the experiment, some minor modi<sup>fi</sup>cations of the experimental design were made according to feedback received from participants. The main experiment, as the pilot study, was based on a factorial design of ${ } _ { 2 \times 2 }$ with two dichotomous independent variables: reference information (with or without information regarding de velopment times of similar features in the past) and role perspective (developer or consultant). Prior to randomly grouping the target sample according to the factorial design, 10 participants were randomly excluded and assigned to a group that performed in a parallel session a sepa rate baseline experiment for further con<sup>fi</sup>rmations.

The remaining 75 participants were randomly assigned to one of four groups: (1) developers with reference information, (2) developers without reference information, (3) consultants with reference information and (4) consultants without reference information. In the three-step main experiment, manipulation of role perspective took place during the <sup>fi</sup>rst step whereas manipula tion of reference information took place in the second step. By the beginning of the experiment, assignments participants delivered in the course ‘Automation and Computer-integrated Manufacturing’ provided them with experience in development tasks similar to those referred to in the experiment. Students were not informed during the experiment that actual development would not be required, either as part of the experiment or as part of the course.

In the <sup>fi</sup>rst step of the experiment, participants in all four groups were told that they were employees of a big software company (The Company, hereinafter). Then, for manipulating role perspective, half of the participants were randomly assigned to a developer role, by being told that they were members of the development team in a development project, and half were assigned to a consultant role, by being told that they were members of the consulting team in the same project. Then, they were presented with a <sup>fi</sup>ctitious case about a software development project that The Company is planning for a speci<sup>fi</sup>c customer. According to the presented script, the project aims to operate a robot that would use blocks of different sizes, which arrive on a conveyor, to build three towers. Additional details about the sizes and locations of the towers were also provided, as was a list of 16 features (see Appendix) of the planned software that, according to the <sup>fi</sup>ctitious story, the customer had mentioned in early meetings with representatives of The Company.

The feature list presented to participants deliberately included features of different importance. Prior to the experiment, two course instructors were asked independently to express their opinion about feature importance to the project goal by differentiating between essential and unnecessary features. Five features on the list that both instructors considered unnecessary were then categorized as over-required. Obviously, all participants in the experiment were not informed about this categorization.

In parallel to the <sup>fi</sup>rst step of the experiment, participants in the separate baseline group were presented with the same fictitious case and list of 16 features. They were then asked to fill a questionnaire to express their opinion about feature importance, identifying features they found essential and features they found unnecessary. Of the <sup>fi</sup>ve features determined unnecessary by the course instructors. two were categorized as such by the entire baseline group and one was correctly identi<sup>fi</sup>ed by 80% of the baseline group. Of the remaining two unnecessary features, 50% of the baseline group identi<sup>fi</sup>ed one as unnecessary and 20% identi<sup>fi</sup>ed the other as unnecessary. Six of the remaining 11 features were correctly identi<sup>fi</sup>ed as necessary by the entire baseline group, and all except one were correctly identi<sup>fi</sup>ed as necessary by at least 70% of the baseline group. Although these feature valuations showed that the baseline group inaccurately assessed the importance of about one feature in each of the unnecessary and essential cate gories, they nevertheless con<sup>fi</sup>rmed that participants in the four main experimental groups had the fundamental ability to identify over-required features by themselves.

In the second step of the experiment, for manipulating reference information, half of the par ticipants assigned earlier to each of the two role perspectives were further randomly assigned to two groups. Half of the participants were provided with reference information by being informed, for each feature, about the average time it took to develop a similar feature in the past, while no such reference information was provided for the other half. Then, participants assigned to a developer role were informed that their assignment was to develop the project and they were asked to <sup>fi</sup>rst estimate how long it would take them to develop each feature. In contrast, participants assigned to a consultant role were informed that their assignment was to advise the project managers and they were asked to <sup>fi</sup>rst estimate how long it would take developers from the development team, who joined The Company together with them, to develop each feature. The instructions made it explicit to those assigned to a consultant role that they were estimating the completion times of others.

© 2015 Wiley Publishing Ltd, Information Systems Journal 26, 395–418

In the third step of the experiment, participants were informed that the project duration cannot exceed 18 h and were asked to choose features to be included within project scope. Finally, participants answered demographic and background questions.

For testing the different hypotheses, three dependent variables were calculated based on the answers of each participant: (a) Total Time Estimation, (b) Number of Features Included and (c) Number of Over-Required Features Included. The Total Time Estimation summed the time estimations provided by the participant for the development of the 16 features on the list. The Number of Features Included counted the number of features that the participant included within project scope out of the full list of 16 features. The Number of Over-Required Features Included counted the number of features that the participant included within project scope out of the list of <sup>fi</sup>ve features determined as unnecessary by both course instructors.

## RESULTS

Data analysis was based on time estimations and project scoping decisions by 75 gender balanced participants in the four experimental groups. The four groups were relatively balanced in terms of their size, with 18 participants in the group of developers without reference informa tion and 19 participants in each of the other three groups. Data analysis was pursued via anal ysis of variance (ANOVA) and multivariate analysis of variance (MANOVA) in SPSS (univariate and multivariate general linear models).

The <sup>fi</sup>ndings indicate that the experiment was able to capture the three investigated prob lems in the planning of software development proiects: time underestimation. scope overload and over-requirement. First, the mean of Total Time Estimation provided by participants was 23.03 h, almost half of the total time it takes to develop similar features, as presented to participants by reference information (43.50 h). The mean of Total Time Estimation was 28.18h and 17.73 h, respectively for those with and without reference information of previous completion times, implying time underestimation in both the presence and absence of reference information. Because our experimental procedure used homogenous groups with randomly assigned participants, the consistent differences across all 16 features provided evidence for treatment effectiveness. Second, the mean of Number of Features Included was 10.89. This <sup>fi</sup>nding implies scope overload, because taking into consideration the time it takes to develop similar features (as being expressed by the provided reference information), the development of the features included by participants within scope would have taken on average 27.92 h, much beyond the maximum of 18 h allotted for the project. Third, the mean of Number of Over-Required Features Included for all participants was 2.13, implying overrequirement because of the inclusion within scope, on average, of almost half of the <sup>fi</sup>ve unnecessary features.

Table 1 presents the Pearson correlations among the three dependent variables, showing that the variables of Number of Features Included and Number of Over-Required Features Included were positively correlated, and that both were negatively correlated with Total Time Estimation. These highly-signi<sup>fi</sup>cant correlations provided evidence that the three dependent variables were re<sup>fl</sup>ective of a single phenomenon, which we identi<sup>fi</sup>ed as the planning fallacy.

Table 1. Correlation matrix

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Total time estimation</td><td>1</td><td></td><td></td></tr><tr><td>Number of features included</td><td>-0.526***</td><td>1</td><td></td></tr><tr><td>Number of over-required features included</td><td>-0.398***</td><td>0.841***</td><td>1</td></tr></table>

(r values are shown; $^ { \star \star \star } p < 0 . 0 0 1 )$

Tables 2 through 4 show the means (and standard deviations) of the three dependent variables in the four experimental groups. As can be seen in these tables, the group with a role perspective of consultants and with reference information about completion times (both outsideview mechanisms) provided the highest mean of Total Time Estimation (30.95 h), the lowest mean of Number of Features Included (8.42) and the lowest mean of Number of Over-Required Features Included (1.11). In contrast, the group of developers without reference information (no outside-view mechanisms) provided the lowest mean of Total Time Estimation (17.66 h), the highest mean of Number of Features Included (13.28) and the highest mean of Number of

Table 2. Means (standard deviations) for total time estimation in hours

<table><tr><td rowspan="2">Role</td><td colspan="2">Reference information</td><td rowspan="2">Total</td></tr><tr><td>With</td><td>Without</td></tr><tr><td>Developer</td><td>25.41 (10.34)</td><td>17.66 (14.18)</td><td>21.64 (12.80)</td></tr><tr><td>Consultant</td><td>30.95 (19.75)</td><td>17.80 (7.17)</td><td>24.37 (16.10)</td></tr><tr><td>Total</td><td>28.18 (15.80)</td><td>17.73 (10.98)</td><td>23.03 (14.53)</td></tr></table>

Table 3. Means (standard deviations) for number of features included

<table><tr><td rowspan="2">Role</td><td colspan="2">Reference information</td><td rowspan="2">Total</td></tr><tr><td>With</td><td>Without</td></tr><tr><td>Developer</td><td>11.21 (3.17)</td><td>13.28 (2.97)</td><td>12.22 (3.21)</td></tr><tr><td>Consultant</td><td>8.42 (2.82)</td><td>10.79 (2.74)</td><td>9.61 (2.99)</td></tr><tr><td>Total</td><td>9.82 (3.28)</td><td>12.00 (3.08)</td><td>10.89 (3.35)</td></tr></table>

Table 4. Means (standard deviations) for number of over-required features included

<table><tr><td rowspan="2">Role</td><td colspan="2">Reference information</td><td rowspan="2">Total</td></tr><tr><td>With</td><td>Without</td></tr><tr><td>Developer</td><td>2.37 (1.74)</td><td>3.61 (1.69)</td><td>2.97 (1.80)</td></tr><tr><td>Consultant</td><td>1.11 (1.33)</td><td>1.53 (1.68)</td><td>1.32 (1.51)</td></tr><tr><td>Total</td><td>1.74 (1.66)</td><td>2.54 (1.97)</td><td>2.13 (1.85)</td></tr></table>

© 2015 Wiley Publishing Ltd, Information Systems Journal 26, 395–418

Over-Required Features Included (3.61). The differences between the two conditions of reference information (with or without) and the two conditions of role perspective (developer or consultant) were in the hypothesized directions for all three dependent variables. Speci<sup>fi</sup>cally, on average, while participants without reference information estimated it would take 17.73 h to develop all features and included 12.00 features within scope, of which 2.54 were over-required, participants with reference information estimated it would take 28.18 h to develop all features and included 9.82 features within scope, of which 1.74 were over-required. Similarly, on average, while developers provided estimations of 21.64 h, 12.22 features within scope and 2.97 over-required features, consultants provided estimations of 24.37 h, 9.61 features within scope and 1.32 over-required features. We subsequently used the ANOVA procedure to test whether these differences were signi<sup>fi</sup>cant enough to provide support for the research hypotheses.

To ensure the statistical validity of our results, we con<sup>fi</sup>rmed that the ANOVA assumptions of normal distribution of errors (differences between values and group means) and homogeneity of variances (homoscedasticity) were not violated. The Shapiro–Wilk test of normality and the Levene test of equality of error variances showed that these assumptions were violated only for Total Time Estimation but not for Number of Features Included and Number of Over-Required Features Included. Because time estimations were skewed to the right, we transformed time estimations to log values and con<sup>fi</sup>rmed that the demands for near-normality $_ { ( p = 0 . 0 2 8 }$ in the Shapiro–Wilk test) and homoscedasticity $\scriptstyle ( p = 0 . 1 3 4$ in the Levene test) were satis<sup>fi</sup>ed. Because using the log transformation had no impact on our <sup>fi</sup>ndings, and given that our <sup>fi</sup>ndings are more interpretable with the original time estimations, we used those in further data analyses.

Table 5 presents the ANOVA results for the full factorial models for the three dependent variables. Given the signi<sup>fi</sup>cant correlations among the three dependent variables, we also present the respective MANOVA results in Table 5. As can be seen in the table, the ANOVA results supported H1a-c, showing that reference information had statistically signi<sup>fi</sup>cant effects on Total Time Estimation $( F = 1 0 . 9 3 3 , p < 0 . 0 1 )$ , the Number of Features Included $( F = 1 0 . 7 5 4 , p < 0 . 0 1 )$ and the Number of Over-Required Features Included $( F = 4 . 9 7 1 , p < 0 . 0 5 )$ . The ANOVA results provided no support for H2a, with a non-signi<sup>fi</sup>cant effect of role perspective on Total Time Estimation $( F = 0 . 8 0 5 , ~ p = 0 . 3 7 3 )$ . The ANOVA results did, however, provide support for H2b and H2c, with statistically signi<sup>fi</sup>cant effects of role perspective on the Number of Features

Table 5. ANOVA and MANOVA results

<table><tr><td rowspan="2">Effect</td><td colspan="3">ANOVA</td><td rowspan="2">MANOVA</td></tr><tr><td>Total time estimation</td><td>Number of features included</td><td>Number of over-required features included</td></tr><tr><td>Reference information</td><td>10.933**</td><td>10.754**</td><td>4.971*</td><td>4.941**</td></tr><tr><td>Role perspective</td><td>0.805</td><td>15.225***</td><td>20.129***</td><td>6.897***</td></tr><tr><td>Reference information × role perspective</td><td>0.728</td><td>0.050</td><td>1.212</td><td>1.738</td></tr><tr><td> $R^2$ </td><td>0.150</td><td>0.266</td><td>0.267</td><td></td></tr><tr><td>Adjusted  $R^2$ </td><td>0.114</td><td>0.235</td><td>0.236</td><td></td></tr></table>

(F values are shown; \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001.)

Included $( F = 1 5 . 2 2 5 , p < 0 . 0 0 1 )$ and the Number of Over-Required Features Included $( F = 2 0 . 1 2 9 , p < 0 . 0 0 1 )$ . As shown in Table 5, the MANOVA results con<sup>fi</sup>rmed the overall effects of reference information $( F = 4 . 9 4 1 , p < 0 . 0 1 )$ ) and role perspective $( F = 6 . 8 9 7 , p < 0 . 0 0 1 )$ on the combination of all three dependent variables. In all the estimated models, the interaction terms between reference information and role perspective were non-signi<sup>fi</sup>cant.

## DISCUSSION AND CONCLUSION

The <sup>fi</sup>ndings of this study lend support to our view that the three problems of time underestimation, scope overload and over-requirement in software development planning are different manifestations of a single decision-making bias, i.e. the planning fallacy. It is possible, nevertheless, that the relatively high correlations among the three variables representing these three prob lems in our experiment may be indicative of cause-and-effect relationships among them. Speci<sup>fi</sup>cally, it is conceivable that more features, in general and over-required features, in particular, are included within the scope of a project because time estimations for feature devel opment are overly optimistic. Put differently, if software engineers perceive each feature as less demanding in terms of the time needed for its development, they may have the impression that more features could be developed within a given project duration. As a consequence of this unrealistic perception of time slack, they may include within project scope more super<sup>fl</sup>uous features together with necessary ones. Importantly, this cause-and-effect explanation extends our reasoning in hypothesis development, which suggests that time underestimation, scope overload and over-requirement in software development planning are analogous to cost underestimation and bene<sup>fi</sup>t overestimation associated with the planning fallacy. Instead of arguing that the planning fallacy underlies all three problems in software development planning, we could argue that the planning fallacy manifests itself through time underestimation, which, in turn, is responsible for scope overload and over-requirement. However, given that time estimations were not manipulated in our experimental design, it is impossible to draw from our empirical results such causal conclusions about the relationships among the dependent variables. This causal explanation remains a challenge to be addressed by future research.

Our empirical <sup>fi</sup>ndings do suggest, however, that the planning fallacy is a plausible descriptive explanation for time underestimation, scope overload and over-requirement because these problems are mitigated by the same mechanisms shown to reduce the planning fallacy. An important contribution of this study to the general literature on the planning fallacy is the conceptual identification and empirical testing of reference information and role perspective as two comparable mechanisms that can potentially shift decision makers from the more biased inside-view approach to the more realistic outside-view approach. Our results con<sup>fi</sup>rm this potential for both mechanisms. However, while the introduction of reference information was found to in<sup>fl</sup>uence all three problems we investigated, taking the role of a consultant was found to in<sup>fl</sup>uence scope overload and over-requirement but not time underestimation.

A plausible explanation for this mixed <sup>fi</sup>nding about role perspective is that the experimenta manipulations may have failed to create a sense of detachment for consultants, who were asked to assess the development time needed for their ‘friends in the development team who joined The Company together with them’. Lovallo and Kahneman (2003) emphasized that when independent consultants are brought in to assist in forecasting, they often remain stuck in the inside view by concentrating on the project itself and produce estimations that tend also to be distorted by cognitive biases. Another possible explanation is that informing consultants that they were assigned to advise the project managers, before asking them to provide time estimations for developers, somewhat empowered them. It is possible that this empowerment led them to provide more optimistic time estimations (Weick & Guinote, 2010), thus offsetting the biasreducing effect of having a consultant role. On the other hand, the experimental manipulations were strong enough to elicit highly signi<sup>fi</sup>cant differences (at the 0.001 level) between consultants and developers for the total number of features and the number of over-required features included within scope, suggesting that the consultant perspective mitigates bene<sup>fi</sup>t overestimation but not time underestimation. The observation about the difference between reference information and role perspective in mitigating the problems plaguing software development planning is, again, proposed as an interesting avenue for future research about the different implications of different outside-view mechanisms.

Importantly, however, the <sup>fi</sup>ndings show that both reference information and role perspective mitigate the biases in planning decisions but fail to eliminate them. Even participants in the experimental group in which both outside-view mechanisms were at play (i.e. consultants with reference information) still exhibited time underestimation, scope overload and overrequirement, although these problems were least severe for this group. In contrast, these prob lems were most severe for the experimental group in which no outside-view mechanisms were at play (i.e. developers without reference information). Our <sup>fi</sup>ndings of non-signi<sup>fi</sup>cant interaction effects suggest that the main effects of reference information and role perspective are additive. In terms of bias mitigation, two outside-view mechanisms are thus superior to one, and one outside-view mechanism is superior to none. This <sup>fi</sup>nding about different mechanisms having additive rather than overlapping effects is another noteworthy contribution of this work. An interesting question for future research that naturally follows is whether it is possible to further mitigate the negative implications of the planning fallacy by introducing additional outside-view mechanisms in the speci<sup>fi</sup>c situation examined here as well as in more general situations.

The <sup>fi</sup>ndings of this study can help both practitioners and researchers. The results extend the line of practical research on techniques for improving time estimation in software development projects, such as decomposing the project into smaller parts and using a bottom-up approach to estimation (Jørgensen, 2004; Bajaj et al., 2006) or avoiding exposure to irrelevant and mis leading information (Jørgensen & Grimstad, 2008). The current study suggests that, to the extent possible, developers and consultants in software development projects should strive to base their estimations on the outcomes of past projects of their own and of others. They should resist the inclination to consider each software development project as a unique endeavour and, instead, seek to <sup>fi</sup>nd relevance in previous projects as a baseline for estimations. In addition, managers of software development projects should be aware that developers are more inclined than consultants towards scope overload and over-requirement and that the underestimation of development time is possibly at the root of both planning problems. Setting a schedule constraint before project scoping, as implemented in the current study, is known to be one of the practices used in software development projects, either because of customer and market needs or in order to control the project scope and focus (Yang et al., 2007; Boehm & Valerdi, 2008). Thus, the current study offers advice to practitioners about biases that might still exist, despite such efforts to better control schedule and scope in software developmen projects, and about potential mechanisms for their mitigation.

As noted above, this study also contributes to the general literature on the planning fallacy beyond the speci<sup>fi</sup>c contribution to IS research. This contribution emerges from the attention to and the investigation of two outside-view mechanisms in concert. Whereas previous research into the planning fallacy focused on a single mechanism at a time (e.g. Buehler et al., 1994; Flyvbjerg, 2006; Buehler et al., 2012), employing a multi-mechanism approach enabled showing that different outside-view mechanisms have bias-mitigating effects that accumulate one on top of the other, with little overlap. This <sup>fi</sup>nding suggests that the identi<sup>fi</sup>cation of additional mechanisms that facilitate an outside view is likely to further improve decision making in planning for software development. Another contribution to the planning fallacy literature lies in considering in a single empirical study both biases attributed to the planning fallacy, time underestimation and bene<sup>fi</sup>t overestimation. Whereas previous research into the planning fallacy generally addressed only the former bias, the current study addresses both biases as explaining different problems in software development projects.

Although it is practically impossible in an experiment to mimic all the complexities of real-world projects, another contribution of this study is the use of experimental methods to explore causeand-effect relationships between situational variables and planning decisions in software devel opment projects. The current experiment tried to emulate reality concerning time estimation and project scoping, sacri<sup>fi</sup>cing external validity (the ability to generalize the <sup>fi</sup>ndings) for internal validity (the ability to infer causal relationships). To address this limitation, further research can target software developers or software consultants in the <sup>fi</sup>eld at the phase of planning a real project and ask them relevant questions about feature development times and features to be included within project scope. Given issues of moral hazard and opportunistic behaviour that this study avoided by targeting students, the role perspective should be either manipulated differently in similar real-world research or special care should be exercised to control the different economic incentives of developers and consultants. Furthermore, the external validity of our <sup>fi</sup>ndings is limited to situations in which the schedule is <sup>fi</sup>xed prior to the determination of project scope by the developers. Thus, for example, our <sup>fi</sup>ndings cannot be generalized to projects where agile methodologies are used or the customer is driving requirement speci<sup>fi</sup>cation. Nevertheless, the generality of the planning fallacy suggests that our <sup>fi</sup>ndings may be applicable to projects in which the scope is not determined by the developers or project duration is not constrained in advance.

Notwithstanding these limitations, this study demonstrates the relevance of the planning fallacy to the time underestimation, scope overload and over-requirement problems that for many years have plagued planning decisions in software development projects. The results con<sup>fi</sup>rm the impact of two outside-view mechanisms, reference information and role perspec tive, on reducing the three problems. The results suggest that having reference information about previous development times reduces but does not eliminate time underestimation, scope overload and over-requirement. The results furthermore suggest that although role perspective does not in<sup>fl</sup>uence time underestimation, it does reduce but does not eliminate scope overload and over-requirement in the sense that software developers tend to be more biased in scoping decisions than software consultants. Finally, our <sup>fi</sup>ndings con<sup>fi</sup>rm that the lens of behavioural economics has the potential to advance understanding of the anomalies associated with poor planning in software development projects.

## REFERENCES

Andres, H.P. (2001) A contingency approach to software project coordination. Journal of Management Information Systems, 18, 41–70.

Baccarini, D., Salm, G. & Love, P. (2004) Management o risks in information technology projects. Industrial Man agement and Data Systems, 104, 286–295.

Bajaj, N., Tyagi, A. & Agarwal, R. (2006) Software estimation: a fuzzy approach. ACM SIGSOFT Software Engineering Notes, 31, 1–5.

Barki, H., Rivard, S. & Talbot, J. (1993) Toward an assess ment of software development risk. Journal of Manage ment Information Systems, 10, 203–225.

Battles, B.E., Mark, D. & Ryan, C. (1996) An open letter to CEOs: how otherwise good managers spend too much on information technology. The McKinsey Quarterly, 1996.116-127.

Bernstein, L. (2012) Things I learned from taming software development. ACM SIGSOFT Software Engineering Notes, 37, 5–6.

Bjarnason, E., Wnuk, K. & Regnell, B. (2010) Overscoping: reasons and consequences—a case study on decision making in software product management.4th International Workshop on Software Product Management (IWSPM), Sydney, NSW, Australia, September 27.

Bjarnason, E., Wnuk, K. & Regnell, B. (2012) Are you biting of more than you can chew? A case study on causes and effects of overscoping in large-scale software engineering Information and Software Technology, 54, 1107–1124.

Boehm, B. & Papaccio, P. (1988) Understanding and controlling software costs. IEEE Transactions on Software Engineering, 14, 1462–1477.

Boehm, B. (1991) Software risk management: principles and practices. IEEE Software, 8, 32–41.

Boehm, B. (1999) Making RAD work for your project. Computer, 32, 113–117.

Boehm, B. (2000) The art of expectations management. Computer, 33, 122–124.

Boehm, B., Port, D. & Al-Said, M. (2000) Avoiding the soft ware model-clash spiderweb. Computer, 33, 120–122.

Boehm, B. & Valerdi, R. (2008) Achievements and challenges in COCOMO-based software resource esti mation. IEEE Software, 25, 74–83.

Boehm, B. & Lane, J.A. (2010) Evidence-based software processes. International Conference on Software Pro cess (ICSP), Paderborn, Germany, July 8–9.

Buehler, R., Grif<sup>fi</sup>n, D. & Ross, M. (1994) Exploring the “Planning Fallacy”: why people underestimate their task completion times. J. Pers. Soc. Psychol., 67, 366–381.

Buehler, R., Grif<sup>fi</sup>n, D. & Ross, M. (1995) It’s about time: optimistic predictions in work and love. European Review of Social Psychology, 6, 1–32.

Buehler, R., Grif<sup>fi</sup>n, D. & Peetz, J. (2010a) The Plannin Fallacy: cognitive, motivational, and social origins. Ad vances in Experimental Social Psychology, 43, 1–62.

Buehler, R., Peetz, J. & Grif<sup>fi</sup>n, D. (2010b) Finishing on time: when do predictions in<sup>fl</sup>uence completion times? Organ. Behav. Hum. Decis. Process., 111, 23–32.

Buehler. R., Griffin, D.. Lam. K. & Deslauriers, J. (2012) Perspectives on prediction: does third-person imagery improve task completion estimates? Organ. Behav. Hum. Decis. Process., 117, 138–149

Buschmann, F. (2009) Learning from failure, part 1: sco ping and requirements woes. IEEE Software, 26, 68–69.

Buschmann, F. (2010) Learning from failure, part 2: featuritis, performitis, and other diseases. IEEE Soft ware, 27, 10–11.

Charette, R.N. (2005) Why software fails. IEEE Spectrum, 42, 42–49.

Coman, A. & Ronen, B. (2009) Overdosed management how excess of excellence begets failure. Human Sys tems Management, 28, 93–99.

Coman, A. & Ronen, B. (2010) Icarus’ predicament: manag ing the pathologies of overspeci<sup>fi</sup>cation and overdesign. In ternational Journal of Project Management, 28, 237–244.

Connolly, T. & Dean, D. (1997) Decomposed versus holistic estimates of effort required for software writing tasks. Management Science, 43, 1029–1045.

Cule, P., Schmidt, R., Lyytinen, K. & Keil, M. (2000) Strate gies for heading off IS project failure. Information Sys tems Management, 17, 65–73.

Dominus, M. (2006) Creeping featurism and the ratche effect. The Universe of Discourse, May 15 (available a http://blog.plover.com/prog/featurism.html; accessed December 15, 2014).

Elliott, B. (2007) Anything is possible: managing feature creep in an innovation rich environment. Proceedings of the IEEE International Engineering Management Conference, Piscataway, NJ, July 29–Aug 1.

Flyvbjerg, B. (2006) From Nobel prize to project management: getting risks right. Project Management Journal, 37, 5–15.

Flyvbjerg, B. & Budzier, A. (2011) Why your IT project may be riskier than you think. Harv. Bus. Rev., 89, 23–25

Flyvbjerg, B. (2013) Quality control and due diligence in project management: getting decisions right by taking the outside view. International Journal of Project Management, 31, 760–774.

Gary, M. (2009) Poor industry consultancy threatens data center constructions, December 16 (available at http:// www.businesscomputingworld.co.uk/poor-industry-consultancy-threatens-data-centre-constructions/; accessed December 8, 2014).

Goes, P.B. (2013) Editor’s comments: information systems research and behavioral economics. MIS Quarterly, 37, iii–viii.

Gray, A.R., MacDonell, S.G. & Shepperd, M.J. (1999) Factors systematically associated with errors in subiective estimates of software development effort: the stability of expert judament Proceedings of the Sixth International Software Metrics Symposium, Boca Raton, FL, November 4–6

Grif<sup>fi</sup>n, D. & Buehler, R. (2005) Biases and fallacies, memories and predictions: comment on Roy, Christenfeld, and McKenzie (2005). Psychol. Bull., 131, 757–760.

Halkjelsvik, T. & Jørgensen, M. (2012) From origami to software development: a review of studies on judgmentbased predictions of performance time. Psychol. Bull., 138, 238–271.

Hayes-Roth, B. & Hayes-Roth, F. (1979) A cognitive mode of planning. Cognit. Sci., 3, 275–310.

Heemstra, F.J. & Kusters, R.J. (1991) Function point analysis: evaluation of a software cost estimation model. European Journal of Information Systems, 1. 229–237.

Hill, J., Thomas, L.C. & Allen, D.E. (2000) Experts’ estimates of task durations in software development projects. International Journal of Project Management, 18, 13–21.

Houston, D.X., Mackulak, G.T. & Collofello, J.S. (2001) Stochastic simulation of risk factor potential effects for software development risk management. Journal of Systems & Software, 59, 247–257.

Jones, C. (2007) Estimating Software Costs: Bringing Realism to Estimating, 2nd edn. McGraw-Hill, NY.

Jones, E.E. & Nisbett, R.E. (1971) The Actor and the Observer: Divergent Perceptions of the Causes of Behavior. General Learning Press, Morristown, NJ.

Jørgensen, M. (2004) Top-down and bottom-up expert esti mation of software development effort. Information and Software Technology, 46, 3–16

Jørgensen, M. & Moløkken-Østvold, K. (2004) Reasons fo software effort estimation error: impact of respondent role, information collection approach, and data analysi method. IEEE Transactions on Software Engineering, 30, 993–1007.

Jørgensen, M. & Sjøberg, D.I.K. (2004) The impact of customer expectation on software development effort estimates. International Journal of Project Management 22, 317–325.

Jørgensen, M. & Grimstad, S. (2008) Avoiding irrelevant and misleading information when estimating develop ment effort. IEEE Software, 25, 78–83.

Kahneman, D. & Tversky, A. (1979) Intuitive prediction: biases and corrective procedures. TIMS Studies in Management Science, 12, 313–327.

Kahneman, D. & Lovallo, D. (1993) Timid choices and bold forecasts—a cognitive perspective on risk taking. Management science, 39, 17–31.

Kahneman, D. (2011) Thinking, Fast and Slow. Allen Lane London. UK.

Kaur, K., Jyoti, B. & Rani, R. (2013) Analysis of Gold Plating: a software development risk. International Journal of Computer Science and Communication Engineering, 2, 51–54.

Kautz, K. (2009) The impact of pricing and opportunistic behavior on information systems development. Journa of Information Technology Theory and Application, 10, 24–41.

Keil, M., Tan, B., Kwok-Kee, W. & Saarinen, T. (2000) A cross-cultural study on escalation of commitment behavior in software projects. MIS Quarterly, 24, 299–325

Keil, M., Im, G.P. & Mähring, M. (2007) Reporting bad new on software projects: the effects of culturally constituted views of face-saving. Information Systems Journal, 17, 59–87.

Khanfar, K., Elzamly, A., Al-Ahmad, W., El-Qawasmeh, E.. Alsamara, K. & Abuleil, S. (2008) Managing software project risks with the chi-square technique. Internationa Management Review, 4, 18–29.

Khatri, V., Vessey, I., Ramesh, V., Clay, P. & Park, S.J. (2006) Understanding conceptual schemas: exploring the role of application and IS domain knowledge. Information Systems Research, 17, 81–102.

Kutsch, E., Maylor, H., Weyer, B. & Lupson, J. (2011) Performers, trackers, lemmings and the lost: sustained false optimism in forecasting project outcomes—evidence from a quasi-experiment. International Journal of Project Management, 29, 1070–1081.

Legoux, R., Leger, P., Robert, J. & Boyer, M. (2014) Con<sup>fi</sup>r mation biases in the <sup>fi</sup>nancial analysis of IT investments. Journal of the Association for Information Systems, 15, 33–52.

Lovallo, D. & Kahneman, D. (2003) Delusions of success: how optimism undermines executives’ decisions. Harv. Bus Rev 8156-63

Malhotra, N., Bhardwaj, M. & Kaur, R. (2012) Estimating the effects of Gold Plating using fuzzy cognitive maps. International Journal of Computer Science and Informa tion Technologies, 3, 4806–4808.

Markus, M.L. & Keil, M. (1994) If we build it, they will come: designing information systems that people want to use. Sloan Manage. Rev., 35, 11–25.

McFarlan, F.W. (1981) Portfolio approach to information systems. Harv. Bus. Rev., 59, 142–150.

Myers, W. (1999) Early communication key to software project success. Computer, 32, 110-111.

Nelson, R. (2007) IT project management: infamous fail ures, classic mistakes, and best practices. MIS Quarterly Executive, 6, 67–78.

Nouri, P., Jamali, B. & Ghasemi, E. (2012) The role o experience on techno-entrepreneurs’ decision making biases. Management Science Letters, 2, 1957–1964.

Pass, S. & Ronen, B. (2014) Reducing the software value gap. Communications of the ACM, 57, 80–87.

Pezzo, S.P., Pezzo, M.V. & Stone, E.R. (2006a) The socia implications of planning: how public predictions bias future plans. Journal of Experimental Social Psychology, 42, 221–227.

Pezzo, M.V., Litman, J.A. & Pezzo, S.P. (2006b) On the distinction between yuppies and hippies: individua differences in prediction biases for planning future tasks. Personality and Individual Differences, 41, 1359–1371.

Ronen, B. & Pass, S. (2008) Focused Operations Manage ment: Achieving More with Existing Resources. John Wiley & Sons, Hoboken, NJ.

Ropponen, J. & Lyytinen, K. (2000) Components of soft ware development risk: how to address them? A project manager survey. IEEE Transactions on Software Engi neering, 26, 98–112.

Rust, R.T., Thompson, D.V. & Hamilton, R.W. (2006) Defeating feature fatigue. Harv. Bus. Rev., 84, 98–107.

Sanna, L.J., Parks, C.D., Chang, E.C. & Carter, S.E. (2005) The hourglass is half full or half empty: temporal framing and the group Planning Fallacy. Group Dynamics: The ory, Research and Practice, 9, 173–188.

Sauer, C., Gemino, A. & Reich, B.H. (2007) The impact of size and volatility on IT project performance. Communi cations of the ACM, 50, 79–84.

Schmidt, R., Lyytinen, K., Keil, M. & Cule, P. (2001) Identi fying software project risks: an international Delphi study Journal of Management Information Systems, 17, 5–36.

Shepherd, D.A., Zacharakis, A. & Baron, R.A. (2003) VCs decision processes: evidence suggesting more experi ence may not always be better. Journal of Business Ven turing, 18, 381–401.

Slovic, P., Fischhoff, B. & Lichtenstein, S. (1977) Behav ioral decision theory. Annu. Rev. Psychol., 28, 1–39.

Umapathy, K., Purao, S. & Barton, R.R. (2008) Designing enterprise integration solutions: effectively. European Journal of Information Systems, 17, 518–527.

Weick, M. & Guinote, A. (2010) How long will it take? Power biases time predictions. Journal of Experimenta Social Psychology, 46, 595–604.

Westfall, L. (2005) The what, why, who, when and how o software requirements.Proceedings of the ASQ World Conference on Quality and Improvement, Seattle, WA, May 16–18.

Wetherbe, J.C. (1991) Executive information requirements: getting it right. MIS Quarterly, 15, 51–65.

Wheatcraft, L.S. (2011) Triple your chances of projec success risk and requirements. INCOSE Internationa Symposium, Denver, CO, June 23.

Williams, L., Kessler, R.R., Cunningham, W. & Jeffries, R. (2000) Strengthening the case for pair programming. IEEE Software, 17, 19–25.

Yang, D., Boehm, B., Yang, Y., Wang, Q. & Li, M. (2007) Coping with the cone of uncertainty: an empirical study of the SAIV process model. In: Software Process Dynam ics and Agility, pp. 37–48, Springer, Berlin, Germany.

Zmud, R. (1980) Management of large software efforts MIS Quarterly, 4, 45–55.

Zwikael, O. & Smyrk, J. (2011) An engineering approach for project scoping.IEEE 18th International Conference on Industrial Engineering and Engineering Manage ment, Changchun, China, September 3–5

## Biographies

O<sup>fi</sup>ra Shmueli has recently completed her PhD studies in the Department of Industrial Engineering and Managemen at Ben-Gurion University of the Negev, Israel. She holds a BSc degree in mathematics and computer science from the Hebrew University and MSc degree in information systems from Tel Aviv University. Harnessing vast practica experience as a software developer, system analyst and project manager, her doctoral research has addressed the behavioural roots of over requirement, showing tha software systems contain functionality that is well beyond need because of behavioural biases.

Nava Pliskin acquired her PhD and MSc degrees from Harvard University and her BSc degree from Tel-Aviv University. She is a tenured full professor in the Department of Industrial Engineering and Management at Ben-Gurion University of the Negev, Israel, where she holds the Solomon and Abraham Krok Chair in Entrepreneurial Management. The Harvard Business School invited her during 1996–1997 to serve as a Visiting Associate Professor and hold the Thomas Henry Carroll Ford Foundation Chair. Professor Pliskin is conducting research on topics related to management and strategy of information systems at the organizational and individual level, with recent work devoted to big data and behavioural effects in software development. Her research papers have been published in such leading journals as Journal of the Association for Information Systems, ACM Transactions on Information Systems, Information Society, Communications of the ACM, IEEE

Transactions on Engineering Management, Information & Management, Database for Advances in Information Systems and Decision Support Systems.

Lior Fink is a senior lecturer in the Department of Industrial Engineering and Management at Ben-Gurion University of the Negev, Israel. He holds a bachelor’ degree in psychology and economics, a master’s degree in social-industrial psychology and a PhD degree in information systems from Tel Aviv University. His research interests focus on economic and strategic aspects of IT development, outsourcing and deployment. Lior's articles have been published in numerous information systems journals including MIS Quarterly Furopean Journal of Information Systems, Information Systems Journal, Journal of the Association for Information Systems, Journal of Information Technology and Journal of Strategic Information Systems. His work has also appeared in economics, project management and medical informatics journals.

## APPENDIX : EXPERIMENTAL TASK AND FEATURE LIST

## Project title

Software for constructing three block towers

## Project details

A block comes onto a conveyor. There are three block sizes – small, medium and large. The robot needs to collect the blocks, identify their sizes and build towers. The towers will be constructed from uniformly-sized cubes (one tower with small-sized cubes, one tower with medium-sized cubes. and one tower with large-sized cubes). The number of blocks in the towers and the distance between them are parameters that will be determined by the user. The towers will be placed on the same axis, with the distance determined by the user. The robot will throw unused blocks to a surplus box.

## Software Feature List (features categorized as unnecessary are marked with \*)

1 Sensing a block that arrives on a conveyor and holding it at a location designated for blocks collection.

2 Running a conveyor at a certain speed until tower construction is completed

3 Turning a block upside down – its top edge would now become its bottom edge

4 Returning a block to ready-products conveyor and running that conveyor \*

5 Placing a ready tower onto a ready-products conveyor and running it \*

6 Identifying the size of a block and deciding where to place the block according to its size (normal size – to a location remembered by the robot, abnormal size – to the surplus box)

7 Planning the location of the towers and allowing the robot to study the locations

8 Stopping the conveyor in case of emergency by pressing a button

9 Dismantling a tower of uniformly-sized blocks (a tower built of large/medium/small blocks)

10 Dismantling a tower of unequally-sized blocks (large block under medium block, medium block under small block) \*

11 Conveying a block to the point it should arrive and studying the next point

12 Constructing a tower of unequally-sized blocks (large block under medium block, medium block under small block) out of the blocks in the uniformly-sized towers \*

13 Printing blocks inventory by size (X large-sized, Y medium-sized, Z small-sized) by pressing a button

14 Producing a printout depicting the locations of blocks (showing towers of different types)

15 Relocation of a tower of uniformly-sized blocks from Location X to Location Y

16 Handling the arrival of a useless block (size that does not <sup>fi</sup>t or size that <sup>fi</sup>ts a ready tower)
