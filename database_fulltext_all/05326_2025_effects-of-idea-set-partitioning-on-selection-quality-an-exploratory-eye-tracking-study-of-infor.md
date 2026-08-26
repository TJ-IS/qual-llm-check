---
otero_id: 5326
otero_key: "TZDD3YHR"
title: "Effects of Idea Set Partitioning on Selection Quality: An Exploratory Eye-Tracking Study of Information Processing"
authors: "Frederik Wiedmann; Arnold Wibmer; Isabella Seeber; Ronald Maier"
year: "2025"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00958"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2025

# Effects of Idea Set Partitioning on Selection Quality: An Exploratory Eye-Tracking Study of Information Pr   ocessing

Frederik Wiedmann , frederik.wiedmann@t-online.de

Arnold Wibmer , arnold.wibmer@gmx.de

Isabella Seeber , isabella.seeber@grenoble-em.com

Ronald Maier , ronald.maier@uibk.ac.at

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Effects of Idea Set Partitioning on Selection Quality: An Exploratory Eye-Tracking Study of Information Processing

Frederik Wiedmann,<sup>1</sup> Arnold Wibmer,<sup>2</sup> Isabella Seeber,<sup>3</sup> Ronald Maier<sup>4</sup>

<sup>1</sup>University of Innsbruck, Austria, frederik.wiedmann@t-online.de <sup>2</sup>University of Innsbruck, Austria, arnold.wibmer@gmx.de <sup>3</sup>Grenoble Ecole de Management, France, isabella.seeber@grenoble-em.com <sup>4</sup>University of Innsbruck / University of Vienna, Austria, ronald.maier@uibk.ac.at

## Abstract

Organizers of innovation contests frequently rely on non-experts as raters to identify the most promising ideas. These raters often struggle with this cognitively demanding task, which limits their likelihood of selecting high-quality ideas. Building on (digital) nudging theory, this research suggests that partitioning a choice set of ideas into larger subsets (subsets of four vs. two ideas) influences raters’ information processing and cognitive effort, resulting in higher selection quality. We analyze data collected in an eye-tracking experiment involving 59 raters, finding that presenting larger idea subsets (i.e., less partitioning) fosters the selection of more novel ideas. This effect was mediated by raters’ degree of cue-wise information processing and by cognitive effort, which we theorize as the effortful comparative information processing mechanism. This mechanism is novel to nudging theory as it suggests that nudges not only improve results by facilitating heuristic, less effortful processing of information but also by triggering more effortful-comparative processing of information.

Keywords: Cognitive Effort, Eye-Tracking, Idea Selection, Information Processing, Nudging

Patrick Y. K. Chau was the accepting senior editor. This research article was submitted on July 6, 2022, and underwent three revisions.

## 1 Introduction

Driven by rapid digitalization, more and more organizations are relying on so-called open innovation contests, in which innovators from a crowd are invited to submit innovative solutions to a challenge (Armisen & Majchrzak, 2015). The scope of such efforts goes beyond generating ideas by including the phase of idea selection to identify the best submissions for later implementation. To identify or select ideas with the greatest potential, innovation contest organizers often rely on internal resources such as experts (Görzen & Kundisch, 2017; Mollick & Nanda, 2016). However, since internal experts have limited availability and are expensive (Galati, 2015), some innovation contest organizers instead use a crowd of end users or potential customers as non-expert raters (e.g., Chen et al., 2020; Klein & Garcia, 2015). Unfortunately, research indicates that non-expert raters are not as good as experts at judging the novelty and feasibility of ideas, two frequently used criteria of idea quality (e.g., Cui et al., 2019; Rietzschel et al., 2010), and the probability that a crowd of non-expert raters will select the highest quality ideas is often not better than chance (Rietzschel et al., 2010). The complexity of idea evaluation and selection contributes to this disparity (Mumford et al., 2002). Raters face significant cognitive demands as they strive to compare and contrast various available options (Jang & Yoon, 2016). As the number of options increases, the cognitive effort required to navigate this process also intensifies (Johnson & Payne, 1985).

Given these challenges, prior research has sought ways to support non-expert raters in selecting promising ideas (e.g., Cheng et al., 2020; de Buisonjé et al., 2017; Zhu et al., 2017). An approach to improving idea selection quality among non-expert raters includes changing user interface design elements to reduce task complexity (e.g., Banken et al., 2019; Blohm et al., 2016; Klein & Garcia, 2015) and to digitally nudge them towards better selection quality. The scant empirical evidence available on ITsupported idea selection suggests that non-expert raters make more accurate idea selection decisions when ideas are divided into multiple pairwise subsets (i.e., partitioned) rather than being presented all at once in a non-partitioned choice set (Santiago Walser et al., 2019). This suggests that high partitioning improves selection outcomes. Other research found that a non-partitioned choice set leads to better outcomes than a highly partitioned set of sequentially presented options (Basu & Savani, 2017). The findings contradict each other and depend most likely on the number of options presented to raters in the partitioned subsets. So far, partitioned sets have only been compared to non-partitioned sets, so that we do not yet understand whether presenting smaller or larger subsets nudges raters to better or worse idea selection, representing our first research gap.

Moreover, the existing literature fails to elucidate how partitioning affects final decisions. Specifically, we lack an understanding of how partitioning influences the selection of feasible and novel ideas, representing a crucial research gap that remains unaddressed. As each subset creates visual barriers to ideas from other subsets (Bruine de Bruin & Keren, 2003), they determine the scope of possible direct comparisons within the idea set. In particular, related literature suggests that non-expert raters can be constrained by a sequenced idea set because they lack juxtaposed options as reference points for comparisons (Basu & Savani, 2019). Indeed, nonexperts cannot leverage their knowledge networks as readily accessible templates, which would otherwise facilitate information processing, a capability often possessed by experts (Kim et al., 2011). Thus, comparing reference points, such as idea descriptions, idea titles, and ratings, enables non-expert raters to better evaluate the merit of ideas (Hsee & Zhang, 2010). As long as the amount of presented information does not overload non-expert raters, their evaluation of ideas should benefit from idea subsets that provide them with more reference points to directly compare ideas. With more ideas presented per subset, more reference points become available, which should improve information processing. Thus, changes in raters’ information processing behavior related to variations of idea subset sizes could explain how partitioning impacts the selection of feasible and novel ideas, representing our second research gap. It is important to understand the causal mechanism behind this digital nudge to inform the design of choice environments, which will lead to better choices (Johnson et al., 2012).

Consequently, we aim to fill both research gaps by answering the research question:

RQ: How does partitioning the choice set into subsets of various sizes affect information processing behavior and selection quality among non-expert raters in idea selection tasks?

We conducted an eye-tracking experiment with 59 nonexpert raters. The analysis of eye-tracking data enabled the deduction of individuals’ information processing strategies concerning the levels of cue-wise and optionwise processing, as well as the measurement of cognitive effort exerted during the process. Our findings showed that raters’ information processing strategy and cognitive effort mediated the effect of idea set partitioning on idea selection quality. Therefore, we contribute to the understanding of how and why a partitioning nudge triggers more effortful-comparative information processing—a form of deliberate processing—which increases the selection of novel ideas.

## 2 Theoretical Background

## 2.1 Idea Selection, Choice Architecture, and Digital Nudging

Idea selection tasks can be understood as multi-cue judgments and decision problems (Bröder et al., 2010; Juslin et al., 2003) that can identify ideas with certain desired qualities, such as highly creative ideas. In this context, an idea refers to an option, which includes a diverse set of multiple attributes or cues (e.g., idea description, ratings, tags) and thus also comprises feedback from other sources such as the crowd (Hoornaert et al., 2017; Santanen et al., 2004). Idea evaluation and selection is a complex activity (Mumford et al., 2002) in which raters form judgments on the potential of each option (Eling et al., 2015), resolve conflicts between options, consider trade-offs between multiple options (Einhorn & Hogarth, 1981; Rietzschel et al., 2019), and forecast the implications of developing or implementing certain options (Mumford et al., 2002) to ultimately select the best option(s). Raters are often given so-called evaluation criteria (e.g., novelty or feasibility) to focus their decision-making (e.g., Zhu et al., 2017) and to dissuade them from selecting ideas based on personal preferences. According to creativity literature, ideas are considered to be creative when they are highly novel (i.e., originality) and feasible (i.e., producible) (e.g., Cui et al., 2019; Rietzschel et al., 2010). Given that non-expert raters often misjudge such criteria (e.g., Blair & Mumford, 2007; Magnusson et al., 2016) and the probability that they will select a creative idea may not exceed a coin toss (Rietzschel et al., 2010), scholars are motivated to improve the design of (digital) choice environments to better facilitate raters in their selection task and improve their selection quality.

A major stream of research into idea selection has explored the role of different rating scales and raters’ response modes (e.g., Blohm et al., 2016; Klein & Garcia, 2015). Other streams of research have focused on the effects of (numeric) priming (de Buisonjé et al., 2017; Görzen & Kundisch, 2017) or task instructions on selection outcomes (Cheng et al., 2020). Only a limited amount of research has explored how partitioning ideas into pairs affects selection quality (Santiago Walser et al., 2019) or how partitioning ideas according to their similarity affects raters’ cognitive effort (Banken et al., 2019).

We argue that rating scales, priming, and idea partitioning can be understood as design elements. These adaptations to design elements aim to alter the choice environment, enabling individuals to perform the selection task better. In this research, we consider the design and effects of choice environment through the theoretical lenses of choice architecture (Congiu & Moscati, 2021; Thaler et al., 2012) and (digital) nudging (Weinmann et al., 2016). In general, nudges—enabled by a certain choice architecture—refer to “libertypreserving approaches that steer people in particular directions” (p. 583) to make their lives simpler, safer, or easier to navigate (Sunstein, 2014). Nudges are a form of indirect encouragement that can help individuals select certain options without limiting them to make different choices (Mele et al., 2021). Consequently, a choice environment can be altered to guide individuals toward better choices (Mele et al., 2021) or toward decisions that are more beneficial for them (Jesse & Jannach, 2021). Information systems researchers have transferred the principle of nudging to the digital context and introduced the term digital nudging (Mirsch et al., 2018; Weinmann et al., 2016), which refers to using user interface elements to influence users’ choice behavior (Weinmann et al., 2016). Particularly in the context of idea selection, we argue that nudging can prevent raters from engaging in unconscious behaviors known to bias decision-making. For example, when decision-making in online environments becomes complex, raters often switch to heuristics focusing on easy-to-interpret signals (e.g., likes or ratings) to make their decisions (Görzen & Kundisch, 2017). We suggest that partitioning a choice set into subsets can be considered a digital nudge that can simplify the decision environment to lower the risk of biased decision-making. Overall, digital nudging literature that focuses on presenting options in the idea selection context is scarce, and little is known about the effects of partitioning choice sets into multiple subsets of different sizes. Although initial studies have shown that partitioning an idea set into subsets is preferable to presenting the whole choice set at once (Santiago Walser et al., 2019), we still lack an understanding of how and why different subset sizes influence idea selection quality.

## 2.2 Idea Set Partitioning and Cue Evaluability

Implementing partitioning as a digital nudge in an online environment changes the presentation format of options (Johnson et al., 2012). Options can be organized into sets of varying sizes. In a non-partitioned set, all options are presented at once in a single set (Bruine de Bruin & Keren, 2003), referred to as simultaneous presentation. In contrast, partitioning divides the set of options into subsets, creating visual barriers between subsets. The lower end of partitioning organizes options into a minimum number of subsets (i.e., two). The upper end of partitioning organizes options into a maximum number of subsets, with each subset containing only one option. This is also referred to as sequential presentation. Within these lower and upper ends of partitioning, options can be partitioned into smaller or larger subsets.

For example, a set of 12 ideas can be presented simultaneously in a single non-partitioned set of all 12 ideas. Partitioning ranges from two subsets containing six ideas each, through intermediate configurations of three, four, and six subsets, up to twelve subsets containing one idea each.

Extant research sheds little light on the implications of partitioning for decision quality. Basu and Savani (2017) compared sequential presentation to simultaneous presentation and found that decision makers presented with six options simultaneously make better decisions than if they are presented with the same number of options sequentially. Santiago Walser et al. (2019) compared the pairwise presentation of 30 options to the simultaneous presentation of the same 30 options in an idea selection task, finding that raters performed better in the idea selection when ideas were presented pairwise than when they were presented simultaneously. Whereas Basu and Savani (2017) found better selection quality with simultaneous presentation, Santiago Walser et al. found simultaneous presentation to be worse for selection quality. The inconsistency of these findings can perhaps be explained by the different information processing behaviors the presentation formats triggered. The simultaneous presentation of 30 options could have cognitively overloaded decision makers (Santiago Walser et al., 2019), while presenting six options was still manageable (Basu & Savani, 2017). Conversely, the sequential presentation of one idea at a time likely caused visual barriers (Bruine de Bruin & Keren, 2003), which hampered the comparison and evaluation between options (Basu & Savani, 2017). Thus, partitioning ideas into subsets could overcome such information processing challenges as long as the subset size does not cognitively overload decision makers and allows comparisons between options. However, we lack empirical evidence comparing varying subset sizes that arise from partitioning a choice set. Both studies identify information processing as a mechanism for the observed effects of partitioning on selection quality. However, it remains unclear how information cues of juxtaposed options feature in raters’ information processing and if smaller versus larger subsets change information processing behaviors.

Partitioning changes how cues are evaluated. The sequential presentation of subsets requires raters to store and retrieve cues from memory, which requires a significant memory load (Basu & Savani, 2017, 2019) because subsets create visual barriers to comparing options from one subset with options from other subsets (Bruine de Bruin & Keren, 2003). Therefore, decision makers frequently must rely solely on displayed information to make a choice and discount or ignore cues that must be retrieved from their memory (Payne et al., 1993). Indeed, studies have shown that comparisons across memory-based barriers are rare (Basu & Savani, 2017), and decision makers prefer direct comparisons among visually juxtaposed cues (Hsee & Leclerc, 1998; Simonson et al., 1993). Decision makers need reference points to infer the desirability of a cue in the context of an evaluation (Hsee & Zhang, 2010). If they lack reference points, their evaluations will not be responsive to the different values of a cue (Hsee & Zhang, 2010). For instance, raters can visually examine the number of likes (a crowd feedback cue) of an idea, but they cannot meaningfully evaluate whether the number is low, medium, or high without comparing it to the number of likes of another idea. Hence, raters can improve their judgments when presented with multiple ideas in a subset because comparisons between cues provide reference points for evaluation (Willemsen & Keren, 2004), and the ensuing cognitive load emerges from comparisons of cues rather than from retrieving information from memory. Larger idea subsets offer more juxtaposed options and thus more cues as reference points than smaller idea subsets.

## 2.3 Idea Subsets and Information Processing

The scarce findings of extant research on the effect of partitioning (Basu & Savani, 2017; Santiago Walser et al., 2019) on selection outcomes suggest that information processing strategies (Payne, 1982) play an explanatory role. Information processing strategies refer to a sequence of mental operations of a decision maker that are used to solve a decision problem (Payne et al., 1993). Researchers who trace decision processes have identified many information processing strategies, such as lexicographic rule, weighted additive (WADD) strategy, and others (Riedl et al., 2008). According to the WADD strategy, when decision makers face a set of options, they acquire all available cues from each option, weigh them according to their relative importance, combine them to pass judgment, and make a rational decision (Chu & Spires, 2003; Juslin et al., 2003). Although this strategy is the most accurate way of processing cues (Juslin et al., 2003), the level of cognitive effort it requires rises steeply as the number of options increases (Johnson & Payne, 1985). In response, decision makers adapt their information processing strategy to fit the complexity of the decision problem by relying on heuristics (e.g., Fishburn, 1974; Gigerenzer & Goldstein, 1996; Tversky, 1972). Heuristics can reduce cognitive effort because they include a stopping rule for information processing and choose the option that first meets or exceeds an aspiration level (Arazy et al., 2017; Brandstätter et al., 2006).

Strategies for processing (and comparing) available cues tend to follow either a more option- or more cuewise direction (Payne, 1976; Riedl et al., 2008). Adopting a so-called option-wise strategy, decision makers integrate information holistically, shifting from one cue to another within an option (Glaholt & Reingold, 2011). For instance, a rater can first process an idea’s description and then an idea’s feedback cues, such as the number of likes or tags, before moving to another idea. Adopting a so-called cue-wise strategy, decision makers process and integrate the information of the same dimension of a cue across multiple options (Glaholt & Reingold, 2011; Patalano et al., 2010). For example, a rater can compare crowd feedback cues for different ideas and then move on to compare idea descriptions between different ideas.

As the above shows, the link between information processing strategy and cognitive effort is complex. Option-wise strategies may involve both a more effortful integration of all cues and a less effortful heuristic processing (Riedl et al., 2008). Similarly, while cue-wise processing strategies are sometimes considered less effortful (Chu & Spires, 2003; Creyer et al., 1990; Juslin et al., 2003; Payne et al., 1988), applying comparative processing of all cues across different options can be a highly effortful information processing strategy (Mantel & Kardes, 1999; Riedl et al., 2008) when equally attractive options are compared (Jang & Yoon, 2016). Therefore, to understand these complex relationships, information processing strategies need to be considered together with the cognitive effort they require.

## 3 Hypotheses Development and Research Model

Our literature review reveals two gaps, which form the basis for our research model (see Figure 1). First, there is a lack of empirical evidence investigating the effects of partitioning on selection quality. We address this gap through the investigation of our first hypothesis. Second, the causal mechanism behind digital nudges is unclear. Since partitioning is likely to affect information processing strategies (Venema et al., 2020), we test whether information processing strategies (i.e., more option-wise or more cue-wise) and cognitive effort are causal mechanisms that can explain the relationship between partitioning and idea selection quality (H2- H5). Finally, we explore how a decision maker’s motivational orientation (i.e., regulatory focus) strengthens or weakens the relationship between partitioning and idea selection quality (H6). Given the ambiguous roles of cognitive effort and cognitive overload (Johnson & Payne, 1985) in prior research on partitioning (Basu & Savani, 2017; Santiago Walser et al., 2019), our research will focus on a setting in which raters do not experience cognitive overload. Therefore, we formulate our hypotheses assuming that raters have sufficient cognitive capacity to process the subsets.

Partitioning the ideas of an innovation contest creates subsets that contain a certain number of ideas. When the idea subset is larger (i.e., less partitioned), more ideas are juxtaposed, which offers raters more options and cues to visually compare, evaluate, and decide on. As topics for idea selection are typically innovative (Girotra et al., 2010), raters often lack expertise—which functions as a reference system to evaluate idea cues. When raters cannot rely on their expertise-based reference points, they have difficulty evaluating ideas due to the absence of cues that would otherwise serve as reference points, reducing the evaluability of ideas (Hsee & Zhang, 2010). However, raters presented with multiple ideas at once can compare them directly and process the available cues as reference points, which increases the evaluability of the cues (Willemsen & Keren, 2004). This, in turn, should improve judgments of idea quality. Such reference points are any cues that a choice architect deliberately includes to draw people’s attention. In other words, choice architects change the salience of cues (Thaler & Sunstein, 2009).

In innovation contests, several cues of an idea can signal quality. Feedback cues collected from an unknown crowd, such as likes or ratings, are interpreted as indicators of an idea’s popularity and quality (Beretta, 2019; Hoornaert et al., 2017). Such cues affect raters’ assessment of how promising an idea is. Likewise, feedback cues about the contributor, such as past ideas (Hoornaert et al., 2017), can signal whether the ideator had successfully generated ideas in the past. As past success is considered a strong predictor of high-quality ideas (Bayus, 2013), raters may be more confident that ideators with past success will generate novel and feasible ideas. Meanwhile, text-mining algorithms can automatically assess the novelty of idea descriptions (Toubia & Netzer, 2017) and thus influence the assessment of an idea’s potential and promise. In summary, each cue represents a reference point that can be used during the idea selection to draw raters’ attention. A larger number of reference points in a larger subset improves the evaluability of cues (Hsee & Zhang, 2010) and improves judgments of the idea quality. After all, subsets create visual barriers so that comparing options across subsets is unlikely (Bruine de Bruin & Keren, 2003). Hence, raters presented with larger idea subsets have more cues to compare, which, in turn, helps them to better evaluate an idea’s potential, compared to when they are presented with smaller idea subsets with fewer cues to compare. Therefore, we hypothesize:

H1: Raters presented with larger idea subsets (i.e., less partitioning) will select ideas with higher (a) novelty and (b) feasibility than raters presented with smaller idea subsets.

In an environment with cognitively manageable subsets, raters can exploit the juxtaposed options and engage in more in-depth information processing because they have more reference points to consider for evaluation (Basu & Savani, 2017). With more reference points available for direct comparisons, a user’s information processing strategy can be more analytical, leading to a more cue-wise processing of options (Jang & Yoon, 2016). For instance, raters using a more cue-wise strategy would focus more on comparing idea descriptions or idea feedback on the same dimension as they move their gaze from one feedback cue to the same feedback cue of another idea. In contrast, raters using a more option-wise strategy would focus on comparisons between the feedback cues of the same ideas, such as shifting the gaze from the idea descriptions to the feedback cues of the same idea and making comparisons among the variety of cues.

![](/api/attachments/TZDD3YHR/fulltext/images/10794bf9b0a506d7c0f779b015c2c4f5338606645f4a43a0a6907f418db3d193.jpg)  
Figure 1. Research Model

Due to the lack of research on information processing strategies within subsets, we drew on studies that manipulated the total number of options in a choice. Several related studies have indicated that presenting more options elicits more cue-wise processing (Ford et al., 1989; Lohse & Johnson, 1996; Russo & Dosher, 1983). Consequently, larger idea subsets should induce raters to process the available cues with a more cuewise strategy (i.e., less option-wise) compared to smaller idea subsets. Thus, we hypothesize:

H2: Raters presented with larger idea subsets (i.e., less partitioning) adopt a more cue-wise (i.e., less option-wise) processing strategy than raters presented with smaller idea subsets.

The cognitive effort exerted by raters is an indicator of deliberate information processing. Nevertheless, previous research has yielded inconclusive findings regarding the information processing strategy that leads to higher cognitive effort. Both option-wise processing and cue-wise processing have been associated with heightened and diminished cognitive effort (Bettman et al., 1990; Riedl et al., 2008). In the context of idea selection, we suggest that cognitive processing is more effortful with cue-wise compared to option-wise processing due to the following reasons: First, nonexpert raters are unlikely to adopt pure option-wise processing strategies and forego the benefits of juxtaposing options because they lack a mental reference system, which experts build through learning and experience. Thus, presenting multiple ideas at once invites comparative processing and thus more cue-wise processing (Basu & Savani, 2019). Second, information processing tends to be more deliberate when decision makers adopt more cue-wise processing (Horstmann et al., 2009). This is also supported by eyetracking studies where longer eye fixations on cues were found when decision makers adopted cue-wise processing (Russo & Dosher, 1983). Prolonged eye fixations indicate deeper processing (Just & Carpenter, 1976) and thus suggest that a decision maker applied more cognitive effort. Third, cue-wise processing occurs more often when information processing is logic- and reasoning-based, demanding more deliberation and cognitive effort, while option-wise processing is more common when imaginary information is processed (McGill & Anand, 1989).

In the context of idea selection, raters who adopt a more cue-wise processing strategy should experience higher cognitive effort because they will need to keep idea descriptions and feedback cues in mind to compare and evaluate the idea novelty and feasibility. Raters who adopt a more option-wise processing strategy can move from one option to the next without having to compare cues between options. This should lower the cognitive effort required because idea quality evaluations are accomplished per idea in this case, and there is no need to keep cue information in mind when moving to the next option. Moreover, raters adopting a more option-wise processing strategy will also need to expend less cognitive effort when judging an option since they lack the knowledge that could be retrieved from memory (lack of expertise), which keeps working memory low. Hence, we hypothesize:

H3: Raters adopting a more cue-wise (i.e., less optionwise) processing strategy expend higher levels of cognitive effort.

Prior research suggests that more cognitive effort is associated with more engagement (Westbrook & Braver, 2015) and more accurate decision-making (Johnson & Payne, 1985). Raters exert cognitive effort to recognize and distinguish different perspectives of shared ideas. This mindfulness allows them to compare, contrast, and make informed judgments (Javadi et al., 2013). Such a deliberate processing of content is effortful and slow (Thaler et al., 2012), but can lead to a better identification of top solutions (Meservy et al., 2014). In contrast, information cues such as likes can trigger heuristic processing during idea selection (Banken et al., 2019), reducing cognitive effort but potentially leading to systematic errors and lower-quality outcomes (Kahneman, 2011). Hence, raters who expend high levels of cognitive effort to evaluate ideas will process information deliberately, which should result in the selection of high-quality ideas. Thus, we hypothesize:

H4: Raters expending a high level of cognitive effort select ideas with higher (a) novelty and (b) feasibility.

Given the above, we argue for the following serial mediation hypothesis: Juxtaposing ideas can benefit selection quality as long as the cues among options can be processed in-depth (Basu & Savani, 2017) and do not cognitively overload raters. In this case, the hypothesized option-wise processing in smaller subsets implies comparing overall impressions of options (Jang & Yoon, 2016), which is less effortful because raters evaluate cues within an option but not across options. In contrast, the more cue-wise processing initiated by presenting ideas in larger subsets, which is linked to deliberate information processing (Horstmann et al., 2009), should be more effortful because cues are processed in-depth and compared across different options. Ultimately, the more effortful cue-wise processing should result in a higher selection quality due to the more deliberate information processing and the more evaluative comparison of cues facilitated by larger idea subsets. Consequently, we suggest the following serial mediation hypothesis:

H5: Raters’ information processing strategy and cognitive effort serially mediate the relationship between partitioning and selection quality, such that larger idea subsets lead to a more cue-wise information processing strategy, which in turn increases cognitive effort and subsequently results in the selection of ideas with higher (a) novelty and (b) feasibility.

It is likely that the ensuing information processing strategy is not only triggered by partitioning but is also affected by an individual’s dominant regulatory focus (Förster & Higgins, 2005; Mourali & Pons, 2009), which is a motivational orientation—a basic driver of attitudes and behaviors (Higgins, 1998). Regulatory focus theory distinguishes two distinct foci: promotion and prevention focus. Individuals with a promotion focus prefer speed over accuracy in task completion (Förster et al., 2003), favoring heuristic approaches (Pham & Avnet, 2004). Hence, promotion focus relates to the use of general attitudes, overall impressions, or intuitions (Mantel & Kardes, 1999), which can be related to more option-wise processing (Mourali & Pons, 2009). In contrast, individuals with a prevention focus prefer more vigilant strategies (Crowe & Higgins, 1997), processing substantive information (Pham & Avnet, 2004) on an item-specific level of independent aspects (Zhu & Meyers-Levy, 2007), which indicates more cue-wise processing.

When raters are presented with smaller idea subsets, raters with a promotion focus will adopt more optionwise information processing because their motivational state already has preferences for gaining overall impressions. In contrast, when raters are presented with larger idea subsets, raters with a prevention focus will adopt even stronger cue-wise information processing because their motivational preference is to process cues vigilantly to lower the risk for their decision. As argued above, a more cue-wise processing strategy should demand more cognitive effort, which will result in better selection quality. To test the moderating role and thus the conditional effect of regulatory focus on the proposed serial mediation in H5, we hypothesize:

H6: The mediating effects of information processing strategy and cognitive effort on the relationship between partitioning and the selection of ideas with higher (a) novelty and (b) feasibility are moderated by the regulatory focus of the rater, such that raters receiving larger subsets adopt an even more cuewise processing strategy when they have a prevention focus and raters receiving smaller subsets adopt an even more option-wise processing strategy when they have a promotion focus.

## 4 Method

We tested our hypotheses in a two-factorial betweensubject experimental design in a laboratory setting using eye-tracking. We manipulated the factors partitioning (idea subsets: four vs. two ideas) and the moderator regulatory focus (promotion vs. prevention focus). Participants were tasked to select the most promising ideas from the choice set of 32 ideas but were not restricted to how many ideas to select in each subset.

## 4.1 Idea Set, Treatments, and Eye-Tracking

To best mirror a real-world scenario, we selected 32 out of 347 ideas from a real online idea competition on the platform OpenIDEO, which focuses on gratitude at the workplace. We deemed the topic of the innovation contest to be appropriate because, compared to innovation contests that are more technical or specific to a domain, it was broad enough to allow participants to relate to it and engage with the ideas. Each idea contained a concise idea description and four idea feedback cues. Since the ideators’ original idea descriptions were long, we shortened them to a maximum of 130 words to fit the screen size for each condition. The new idea descriptions contained meaningful original sentences that best described the what, how, and why of each idea, with only minimally adapted wordings.

We also added three additional sources of information, namely crowd-based, content-based, and contributorbased information, because past research has shown that these sources of feedback cues are predictors of an idea’s future implementation (Hoornaert et al., 2017). We retained the original idea feedback cues on the OpenIDEO platform, i.e., the number of likes as crowd feedback, and the contributor’s historical idea score as contributor information. On the OpenIDEO platform, registered community members can “like” an idea by clicking on a heart-shaped “applause” button during the idea generation phase. The resulting number of likes ranged from 1 to 20. Historical idea scores representing the ideator’s past contributions on the platform varied from 11 to 101.

We added a creativity score and tags as additional feedback cues representing content information, as there was no information of this type available on the platform for this idea competition. The creativity score was computed via a web interface<sup>1</sup> provided by Toubia and Netzer (2017), which draws on a semantic network textmining algorithm. The score represented the creativity of the idea descriptions by balancing familiarity and novelty. It was interpreted between -1 (novel) and 1 (familiar), whereas 0 was the optimal balance for a creative idea. The creativity scores were between 0.13 and 0.36, indicating a tendency towards familiarity for all contest ideas. Tags were generated using IBM’s artificial intelligence service Natural Language Understanding (IBM, 2018). The service extracted the three best-ranked keywords (5-9 single words) from the idea description, representing the conceptual category that best aligned with the idea. We selected those keywords that had the highest relevance score, excluding the words “idea” and “gratitude”. Consequently, each idea consisted of an idea title, idea description, and idea feedback (likes, historical idea score, creativity score, and tags).

We manipulated the treatment partitioning by varying the number of ideas presented on one screen without changing the choice set. One group saw the 32 ideas of the choice set on 16 screens with two ideas each—thus, smaller subsets. The other group saw the same choice set of 32 ideas on 8 screens with four ideas each—thus, larger subsets. Participants could not switch between screens, as this would have blurred the barriers between subsets. A random number generator determined the sequence of idea presentation for each participant. For the regulatory focus treatment, we adapted the regulatory focus priming procedure from Chernev (2004). To prime a promotion focus, participants were tasked to write about their aspirations and hopes (Freitas & Higgins, 2002) and find a way to the cheese for a cartoon mouse placed in the middle of a paper-and-pencil maze (Friedman & Forster, 2001). To prime a prevention focus, participants were told to first write about duties and obligations (Freitas & Higgins, 2002) and prevent the cartoon mouse from getting caught by the cartoon eagle in the paper-andpencil maze by escaping to the mouse hole (Friedman & Forster, 2001). Both priming activities were described as warm-up activities before the idea selection task.

For eye-tracking, we defined non-overlapping areas of interest (AOIs) for idea description (including its title) and idea feedback cues (number of likes, historical idea score, creativity score, and tags) with a recommended error margin of 0.5 degrees (Figure 2). An automatic 5-point calibration procedure ensured reliable data collection. Figure 3 illustrates the partitioning in subsets of two and four ideas. To track participants’ gaze, we used a Tobii Pro X3-120 eyetracker with a sample rate of 120 Hz, which was directly mounted on a 24-inch Samsung SyncMaster B2440 screen with a resolution of 1920x1080. The participants entered their responses using a keyboard and mouse and were 60-65cm away from the screen that presented the stimuli. Light conditions in the lab were kept constant between 400 and 450 LUX.

![](/api/attachments/TZDD3YHR/fulltext/images/759397e002064d87e810f594111a784aaa6fa4211be793bce54379250a9d33c0.jpg)  
Figure 2. Example of Idea Description (Green-Shaded Boxes Indicate AOIs)

![](/api/attachments/TZDD3YHR/fulltext/images/2e895bedf15053a875e514800cd64a99ee86dcabbc9fc9b53ddcced2dc3858e9.jpg)  
Figure 3. Selection Task with Two (Left Panel) vs. Four Ideas (Right Panel) per Subset

## 4.2 Participants and Experiment Procedure

In total, 63 graduate students from a European university took part in the experiment from May to July 2018 (31 participants) and from March to April 2019 (32 participants). We invited students enrolled in the master’s degree program in information systems because their background allows them to perform the selection task from the perspective of decision makers with businessrelated thinking in the information systems field. We excluded three participants from the analysis due to problematic eye tracker calibrations and failed drift checks (Carter & Luke, 2020), which resulted in inaccurate gaze recordings. We also excluded one participant who spent insufficient time on the priming tasks (less than one minute, compared to the five minutes we requested). The resulting sample consisted of 59 participants <sup>2</sup> —19 women and 40 men. On average, participants were 25.17 years old (min 22; max 31). Most students (48) received class credits in a Research Methods course for their participation. The remaining 11 students participated without an extrinsic incentive. We randomly assigned participants to a treatment group. Before the eye-tracking-based idea selection task, participants had to perform the two warm-up activities described in the section above to prime them either to a promotion or prevention focus. Participants were informed about the task goal, introduced to the task environment, shown an exemplary idea, and informed that they could not go back to previous screens. After the 5-point calibration of the eye tracker, which took an average of 3.57 minutes (min = 1.4 minutes; max = 9.53 minutes), participants engaged in the idea selection task. There, participants selected the most promising ideas from a set of 32 ideas grouped in subsets of either two or four ideas, depending on their experimental group. On average, working on the idea selection task took 18.4 minutes (min 7.2 minutes; max 32.8 minutes). After completing the idea selection task, eye-tracking ended, and participants were asked to fill out an online questionnaire on the same monitor to collect control variables.

## 4.3 Measures

## 4.3.1 Eye-Tracking Based Measures

Information processing strategy: We measured the information processing strategy with the strategy index, which is used as an established process-tracing measure for multi-cue decision tasks (Jang & Yoon, 2016; Lohse & Johnson, 1996; Russo & Dosher, 1983). The strategy index shows whether a decision maker adopts a more option-wise information processing or a more cue-wise information processing. The index is calculated by subtracting the number of cue-wise transitions that a decision maker makes from the number of option-wise transitions and dividing the result by the sum of the option-wise and cue-wise transitions (Ball, 1997). The strategy index is fixed between -1 and +1, with -1 indicating complete cue-wise processing and +1 indicating complete option-wise processing. Hence, the information processing strategy is on the continuum from a negative index (more cue-wise processing) to a positive index (more option-wise processing), but always within the range of -1 to +1. First, we determined the strategy index per screen (i.e., per subset) using the sum of the eye-tracking-based cue- and option-wise gaze transitions. Then, we averaged the strategy indices across all subsets. Two participants skipped a screen, resulting in a lack of tracked gaze transition to determine the strategy index for this subset. We entered a 0 for these subsets, representing a neutral search strategy.

Cognitive effort: The cognitive effort was measured with eye-tracking based on pupil dilations (sample rate: 40 Hz). Previous studies have shown that an increase in pupil size indicates higher cognitive effort (e.g., Fehrenbacher & Djamasbi, 2017; Payne et al., 1993). We used the CEP-Web tool (Zugal et al., 2017) to clean the raw pupillary data points (Carter & Luke, 2020). To account for individual differences in pupil size, pupillary data analysis requires a baseline that can be recorded just before the task begins, for example, during an introductory task (Kruger et al., 2013). The baseline is then subtracted from the actual pupil size to ensure a valid comparison. We used the average pupil dilation of the last introduction screen as a baseline and subtracted it from the average pupil dilation across the whole idea selection task. A positive value indicates a higher cognitive effort compared to the baseline screen, whereas a negative value suggests a lower cognitive effort compared to the baseline screen.

## 4.3.2 Performance-Based Measures

The quality of the selected ideas was operationalized with two measures: idea novelty and idea feasibility. Novelty refers to an idea that is original and that modifies a paradigm. Feasibility refers to ideas that can be easily implemented and are socially, legally, or politically acceptable (Dean et al., 2006). We measured idea quality in several steps:

Step 1—Expert assessment: Both criteria for each of the 32 ideas were assessed at least seven times by 10 HR experts on a scale from 1 to 5 (1 = low feasibility or novelty, 5 = high feasibility or novelty). Eight experts were HR managers in their respective organizations, had experience with gratitude initiatives, and were identified through snowball sampling. The other two experts had strong backgrounds in HR and were researchers at the university. The HR experts were invited based on the premise that the idea selection task concerned gratitude at the workplace. The assessment took place in an online survey tool, in which we presented ideas sequentially and in a randomized order. We displayed only the idea descriptions to prevent biases and excluded any additional idea feedback.

Step 2—Mean-centering and interrater reliability: For the analysis, the expert ratings were mean-centered to consider possible individual differences in the strictness of ratings. Based on the mean-centered ratings, we determined the interrater reliability by calculating the intraclass correlation coefficient (McGraw & Wong, 1996). Both idea novelty (ICC = 0.605, CI 95% = 0.349, 0.785) and idea feasibility (ICC = 0.631, CI 95% = 0.383, 0.804) achieved moderate interrater reliability (Koo & Li, 2016).

Step 3—Define unique quality value for each idea: To receive a single value of quality, we averaged the mean-centered expert ratings on idea novelty and feasibility for each idea. This resulted in a list of 32 ideas, which had associated feasibility and novelty ratings, and allowed us to deduce which ideas were higher (or lower) in feasibility (or novelty).

Step 4—Calculation of raters’ feasibility and novelty of selected ideas: For each participant, our idea selection platform tracked the ideas they selected. On average, raters selected 11 ideas out of 32. For each rater and each of their selected ideas, we assigned unique quality values, which were derived in Step 3. Then, we averaged the feasibility and novelty values within each participant’s set of selected ideas, which resulted in a list of participants and their average idea feasibility and novelty selection scores. A summary of the eye-tracking and performancebased measures is given in Appendix A.

## 4.3.3 Survey-Based Measures

To control for individual differences that could have affected participants’ cognitive effort and selection quality, we collected information on participants gender and English proficiency in a questionnaire. English proficiency was collected to control for different levels of language skills because participants were not native English speakers, and the entire experiment was conducted in English. Since all participants were students in a master’s degree program taught in English, the overall level of English proficiency was high. We assessed English proficiency using a self-reported single item on a 6-point Likert scale from 1 (beginner) to 6 (proficient). In addition, we collected participants’ gender to control for possible gender-related differences in information processing strategies (e.g., Meyers-Levy, 1989).

## 4.4 Correlation Between Expert Assessment and Idea Feedback

After collecting the expert assessment, we checked how they correlated with the feedback cues of the 32 ideas.<sup>3</sup> High correlations between idea feedback and expert assessment would indicate high predictability of idea quality based on the feedback cue.

The number of likes had a low correlation coefficient with the experts’ rating of novelty (r = 0.020) and a medium correlation coefficient with feasibility (r = 0.327) (see Table 1). The historical idea score had a low correlation coefficient with novelty (r = 0.210) and a medium correlation coefficient with feasibility (r = 0.313). The creativity score, which ranged from -1 to 1,

Note: \* significance level 0.05; \*\* significance level 0.01; <sup>a</sup>(0 = two ideas per subset; 1 = four ideas per subset); <sup>b</sup>(0 = promotion focus; 1 = prevention focus); <sup>c</sup>(1 = male; 0 = female)

was transformed to a positive scale to ease interpretation. The creativity score did not correlate with the expert’s assessment of novelty (r = -0.028) and had a low correlation coefficient with idea feasibility (r = 0.117). None of the correlations reached a significance level < 0.05. Only the number of likes and historical idea score had weak correlations $( p < 0 . 1 )$ with feasibility and/or novelty. Hence, these feedback cues were weak indicators of the expert-based assessments of idea novelty and feasibility.

## 5 Results

## 5.1 Sample and Assumption Tests

This section provides an overview of the sample and presents the descriptive statistics of the subset size and regulatory focus variables used in this study (see Table 2).

To test our proposed hypotheses, we performed several regression analyses, a serial mediation analysis, and a moderated serial mediation analysis using the PROCESS macro for SPSS (Hayes, 2018). Before undertaking the linear regression analysis, we performed statistical assumption tests for multivariate normality, multicollinearity, and homoscedasticity. For multivariate normality, we visually inspected Q-Q plots, which showed that observations are well distributed along the 45-degree line. Multicollinearity was tested with correlations (see Table 3) and variance inflation factors (VIFs). All VIFs were below the threshold of 4. Finally, we tested homoscedasticity using the Breusch-Pagan test, which revealed sufficient homoscedasticity $( p > 0 . 0 5 )$ ). Following the recommendation of Cohen et al. (2003), we used z-standardized SPSS factor scores of all continuous variables to gain standardized coefficients in the regressions for a more straightforward interpretation of effect sizes.

Table 1. Correlations Between Feedback Cues and Expert Ratings

<table><tr><td>Feedback cue</td><td>Expert assessment of idea novelty</td><td>Expert assessment of idea feasibility</td></tr><tr><td>Number of likes</td><td>.020</td><td>.327</td></tr><tr><td>Historical idea score</td><td>.210</td><td>.313</td></tr><tr><td>Creativity score</td><td>-.028</td><td>.117</td></tr></table>

Note: \* 0.05 significance level; \*\* significance level 0.01

Table 2. Sample Description

<table><tr><td rowspan="3" colspan="2">Variable</td><td colspan="4">Treatment</td></tr><tr><td colspan="2">Two ideas per subset</td><td colspan="2">Four ideas per subset</td></tr><tr><td>Promotion focus</td><td>Prevention focus</td><td>Promotion focus</td><td>Prevention focus</td></tr><tr><td rowspan="2">Gender</td><td>Male</td><td>10</td><td>9</td><td>9</td><td>12</td></tr><tr><td>Female</td><td>4</td><td>6</td><td>5</td><td>4</td></tr><tr><td colspan="2"></td><td>Mean (SD)</td><td>Mean (SD)</td><td>Mean (SD)</td><td>Mean (SD)</td></tr><tr><td colspan="2">English proficiency</td><td>4.43 (0.852)</td><td>4.80 (0.862)</td><td>4.86 (0.949)</td><td>4.94 (0.574)</td></tr><tr><td colspan="2">Information processing strategy</td><td>0.444 (0.287)</td><td>0.491 (0.234)</td><td>0.254 (0.248)</td><td>0.262 (0.211)</td></tr><tr><td colspan="2">Cognitive effort</td><td>-0.089 (0.081)</td><td>-0.064 (0.080)</td><td>-0.041 (0.083)</td><td>-0.067 (0.106)</td></tr><tr><td colspan="2">Selected ideas&#x27; novelty</td><td>0.018 (0.155)</td><td>0.022 (0.107)</td><td>0.056 (0.162)</td><td>0.013 (0.190)</td></tr><tr><td colspan="2">Selected ideas&#x27; feasibility</td><td>0.152 (0.218)</td><td>0.046 (0.096)</td><td>0.078 (0.184)</td><td>0.096 (0.165)</td></tr></table>

Table 3. Pearson Correlation

<table><tr><td></td><td>Correlations</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>1</td><td>Idea subseta</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Regulatory focusb</td><td>.016</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Genderc</td><td>.048</td><td>-.001</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>English proficiency</td><td>.172</td><td>.141</td><td>.112</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Information processing strategy</td><td>-.411**</td><td>0</td><td>.094</td><td>-.032</td><td>1</td><td></td><td></td><td></td></tr><tr><td>6</td><td>Cognitive effort</td><td>.131</td><td>0</td><td>-.039</td><td>-.16</td><td>-.341**</td><td>1</td><td></td><td></td></tr><tr><td>7</td><td>Selected idea&#x27;s novelty</td><td>.042</td><td>-.064</td><td>.043</td><td>-.193</td><td>-.009</td><td>.421**</td><td>1</td><td></td></tr><tr><td>8</td><td>Selected idea&#x27;s feasibility</td><td>-.03</td><td>-.127</td><td>-.239</td><td>-.045</td><td>-.066</td><td>-.226</td><td>-.336**</td><td>1</td></tr></table>

Table 4. Regressions Between Measures

<table><tr><td rowspan="2">Antecedent</td><td rowspan="2" colspan="2">Information processing strategya</td><td rowspan="2" colspan="2">Cognitive effort</td><td colspan="4">Idea quality</td></tr><tr><td colspan="2">Idea novelty</td><td colspan="2">Idea feasibility</td></tr><tr><td></td><td>Coeff.</td><td>SE</td><td>Coeff.</td><td>SE</td><td>Coeff.</td><td>SE</td><td>Coeff.</td><td>SE</td></tr><tr><td>Idea subset</td><td>-.823**</td><td>.248</td><td>.029</td><td>.280</td><td>.137</td><td>.271</td><td>-.070</td><td>.284</td></tr><tr><td>Information processing strategya</td><td></td><td></td><td>-.345*</td><td>.140</td><td>.154</td><td>.143</td><td>-.153</td><td>.150</td></tr><tr><td>Cognitive effort</td><td></td><td></td><td></td><td></td><td>.449**</td><td>.133</td><td>-.284*</td><td>.139</td></tr><tr><td>Regulatory focus</td><td>.098</td><td>.247</td><td>.074</td><td>.254</td><td>-.104</td><td>.246</td><td>-.226</td><td>.258</td></tr><tr><td>English proficiency</td><td>.023</td><td>.155</td><td>-.230</td><td>.160</td><td>-.154</td><td>.158</td><td>-.061</td><td>.170</td></tr><tr><td>Gender</td><td>.253</td><td>.263</td><td>.025</td><td>.273</td><td>.123</td><td>.264</td><td>-.486</td><td>.276</td></tr><tr><td>Constant</td><td>.088</td><td>.735</td><td>1.011</td><td>.757</td><td>.633</td><td>.744</td><td>.772</td><td>.779</td></tr><tr><td>Model summary</td><td colspan="2"> $R^2 = .182$ </td><td colspan="2"> $R^2 = .150$ </td><td colspan="2"> $R^2 = .220$ </td><td colspan="2"> $R^2 = .150$ </td></tr><tr><td></td><td colspan="2"> $F(4,54) = 3.000, P = .026*$ </td><td colspan="2"> $F(5,53) = 1.870, p = .116$ </td><td colspan="2"> $F(6,52) = 2.440, p = .037*$ </td><td colspan="2"> $F(6,52) = 1.467, p = .208$ </td></tr></table>

Note: \* significance level 0.05; \*\* significance level 0.01. <sup>a</sup>an information processing strategy represents either more option-wise (positive strategy index) or more cue-wise (negative strategy index) information processing

## 5.2 Effects of Partitioning

H1 proposes that raters presented with larger idea subsets will select ideas with higher novelty (H1a) and higher feasibility (H1b) than raters presented with smaller idea subsets. The regression showed no significant effect of partitioning on idea quality, suggesting that there was no direct effect of presenting larger subsets on the selected ideas’ novelty $( \beta = 0 . 1 3 7 , p > 0 . 0 5 )$ or feasibility $( \beta = -$ $0 . 0 7 0 , p > 0 . 0 5 )$ . Consequently, our results do not support H1a and H1b. H2 proposes that presenting raters with larger idea subsets will lead raters to adopt a more cuewise information strategy than presenting them with smaller idea subsets. Our results confirm that presenting larger subsets significantly affected the degree to which raters applied a more cue-wise information processing strategy, i.e., a less option-wise strategy $( \beta = - 0 . 8 2 8 , p <$ 0.05), supporting H2. H3 proposes that a more cue-wise information processing strategy is associated with higher cognitive effort. Conversely, it means that a more optionwise strategy would be associated with lower cognitive effort. We found a significant effect $( \beta = - 0 . 3 4 5 , p < 0 . 0 5 ) .$ supporting H3. H4 proposes a link between higher cognitive effort and better selection quality for ideas that are more novel and for ideas that are more feasible. The results of our data analysis confirm that higher cognitive effort led to the selection of ideas with higher novelty (β $= 0 . 4 4 9 , p < 0 . 0 5 )$ but also show that higher cognitive effort led to the selection of ideas with lower feasibility (β $= - 0 . 2 8 4 , p < 0 . 0 5 )$ . Hence, our results support H4a but not H4b, as the observed effect contradicts the proposed direction. Table 4 summarizes the results of the regression analyses.

## 5.3 Serial Mediation

The mediation tests were based on Model 6 (serial mediation) and Model 83 (moderated serial mediation) of the PROCESS macro for SPSS, both running with 5000 bootstraps. Bootstrapping-based mediation analyses are recommended by Zhao et al. (2010) to assess total, direct, and indirect effects (Hayes, 2018). Although there were no observable direct effects and total effects of the idea subset on idea novelty (H1a) and idea feasibility (H1b), their absence does not rule out the existence of indirect effects (Zhao et al., 2010). Therefore, we followed the suggestion of Zhao et al. (2010) and further explored information processing strategy and cognitive effort as potential underlying mechanisms. H5 proposes that raters’ information processing strategies and the applied cognitive effort serially mediate the relationship between partitioning and idea novelty (H5a) and idea feasibility (H5b). The serial mediation analysis revealed a significant positive indirect effect on the selected ideas’ novelty (indirect effect coefficient = 0.128, SE = 0.063, CI 95% = 0.021, 0.270). Hence, we conclude that presenting ideas in larger subsets leads to the selection of ideas with higher novelty through the adoption of a more cue-wise information processing strategy associated with higher cognitive effort. Since the direct effect of partitioning was not significant, this indicates an indirect-only mediation with a suppression effect (Zhao et al., 2010) and supports H5a. The total effect is not significant due to the presence of the suppression effect, which occurs when another indirect effect has an opposite sign to the total effect (Rucker et al., 2011). Specifically, in the serial mediation model, the indirect effect $\mathrm { X }  \mathrm { M } 1 $ Y<sup>a</sup> is negative $( \beta = - 0 . 1 2 7 , S E = 0 . 1 5 8 , C \mathrm { I } 9 5 \% = - 0 . 5 3 1$ 0.085), which opposes the total effect. Finally, the serial mediation analysis showed a significant negative indirect effect for the same mediators on the selected ideas’ feasibility (indirect effect coefficient = -0.081, SE $= 0 . 0 6 2 , \mathrm { C I } 9 5 \% = - 0 . 2 3 5 , - 0 . 0 0 2 )$ , which implies that larger idea subsets negatively affect raters’ selection of feasible ideas. Although we found a significant serial mediation for the selected ideas’ feasibility, the inverse direction of the indirect effect contradicts our hypothesis. Hence, H5b is not supported. Table 5 presents the mediation analysis results, and Figure 4 visualizes the serial mediation pathways.

Table 5. Mediating Effects of Information Processing Strategy and Cognitive Effort

<table><tr><td>Model</td><td>Parameters</td><td> $\beta$ </td><td>LLCI</td><td>ULCI</td></tr><tr><td rowspan="6">Serial mediation</td><td>Indirect effectX → M1 → M2 →  $Y^a$ </td><td>.128</td><td>.021</td><td>.270</td></tr><tr><td>Indirect effectX → M1 → M2 →  $Y^b$ </td><td>-.081</td><td>-.235</td><td>-.002</td></tr><tr><td>Direct effectX →  $Y^a$ </td><td>.137</td><td>-.407</td><td>.680</td></tr><tr><td>Direct effectX →  $Y^b$ </td><td>-.070</td><td>-.639</td><td>.499</td></tr><tr><td>Total effectX →  $Y^a$ </td><td>.151</td><td>-.386</td><td>.687</td></tr><tr><td>Total effectX →  $Y^b$ </td><td>.037</td><td>-.379</td><td>.343</td></tr><tr><td rowspan="2">Index of moderated serial mediation(regulatory focus as moderator)</td><td> $Y^a$  Idea novelty</td><td>.031</td><td>-.134</td><td>.182</td></tr><tr><td> $Y^b$  Idea feasibility</td><td>-.020</td><td>-.156</td><td>.104</td></tr><tr><td colspan="5">Note: aselected novelty of ideas; bselected feasibility of ideas</td></tr></table>

![](/api/attachments/TZDD3YHR/fulltext/images/d7846bbfc3cc625da4777167703709fc9c545f77ee66a7654c2e86df71a551ac.jpg)  
Figure 4. Underlying Mechanisms of Idea Set Partitioning with Larger (4 Ideas) and Smaller (2 Ideas) Subsets

## 5.4 Moderated Serial Mediation

Finally, H6 proposes that the indirect effect of partitioning differs systematically as a function of the regulatory focus, such that the mediating effects of information processing strategy and cognitive effort are moderated by the rater’s regulatory focus. Repeating the serial mediation analyses of H5 with regulatory focus as a moderator revealed no moderated serial mediation for either novelty (moderated mediation index = 0.031, SE = 0.078, CI 95% = -0.134, 0.182) or feasibility (moderated mediation index = -0.020, SE = 0.062, CI 95% = -0.156, 0.104) as presented in Table 5. Hence, H6 is not supported.

## 5.5 Summary of Results

Based on the results of the hypothesis testing, we conclude that a rater’s information processing strategy and cognitive effort mediate the relationship between partitioning and selection quality. In other words, presenting larger idea subsets leads raters to adopt a more cue-wise information processing strategy that is associated with higher cognitive effort. At a higher level of cognitive effort, we found inverse directions on the selection quality in terms of the novelty and feasibility of selected ideas. Whereas a higher cognitive effort led to the selection of more novel ideas, it simultaneously led to the selection of less feasible ideas. This contradictory effect on selection quality is illustrated in Figure 4.

![](/api/attachments/TZDD3YHR/fulltext/images/300ea0721688bf62e35831de3b5554b446d6b80d52ed9e6a24c638227837fbec.jpg)

![](/api/attachments/TZDD3YHR/fulltext/images/a46eebbf18f80541da459201f623d297550d7c6c70eada0a20111513a236616d.jpg)  
Figure 5. Scatterplots of Information Processing, Cognitive Effort, and Selection Quality

To better understand the effects, we visualized the findings in scatterplots (Figure 5) for idea novelty (left panel) and idea feasibility (right panel), and performed an in-depth analysis of the processing of information cues. Figure 5 shows the raters’ information processing strategies plotted on the x-axis and their cognitive effort plotted on the y-axis. Raters presented with four ideas per screen are represented by grey dots, and raters presented with two ideas per screen are represented by black dots. The larger the size of the dot, the more novel or feasible the selected ideas (see Figure 5). Since each plot has one extreme case (lower left corner), we repeated our analysis excluding these cases, finding that they did not affect the significance of our results or the direction of effects.

The scatterplots illustrate that the dominant pattern of information processing was option-wise for both subset sizes. Nonetheless, raters who were shown larger subsets adopted a more cue-wise processing strategy than raters who were shown smaller subsets. Applying a more cue-wise processing strategy was associated with higher cognitive effort, whereas applying a more option-wise processing strategy was associated with lower cognitive effort during the selection task. Thus, the graphs illustrate that more comparative information processing, i.e., comparing information cues between options, was associated with higher cognitive effort. At the same time, the graphs demonstrate duality in the relationship between cognitive effort and selection quality. Raters who were shown larger subsets and who therefore tended to adopt a more effortful-comparative processing strategy selected more novel ideas, whereas raters who were shown smaller subsets and who therefore tended to adopt a less effortful-comparative processing strategy selected more feasible ideas.

Along with the eye-tracking investigation, we asked participants if the selection task was too mentally taxing, leading to choice overload. The absence of information overload was a prerequisite for arguing the hypotheses (see Section 3). Related research has found that information overload fosters choice avoidance (Pilli & Mazzon, 2016) and that in idea selection settings, a presentation of 30 ideas results in a significantly lower number of selection choices than presenting 30 ideas in subsets of two (Santiago Walser et al., 2019).

To this end, we analyzed perceived choice overload (Heitmann et al., 2007), measured on a 7-point Likert scale collected during the post-survey, and the number of selected ideas. Descriptive statistics indicate that raters did not perceive an extreme level of choice overload and that choice overload was somewhat higher for raters selecting from subsets of four ideas (M = 4.493, SD = 1.122) versus subsets of two ideas (M = 4.250, SD = 1.1335). The number of selected ideas was also slightly lower for raters selecting from subsets of four ideas (M = 10.375, SD = 3.358) versus subsets of two ideas (M = 11.613, SD = 4.402). The ANOVA analysis showed that this difference was not significant for perceived choice overload (F(1,57) = 0.614, p > 0.05) and the number of selected ideas (F(1,57) = 1.581, p > 0.05). This indicates that choosing from a subset of two or four ideas did not result in a perceived depletion of raters’ cognitive resources and that the reported eyetracking findings are indicative of changes in cognitive effort but not cognitive overload. Table 6 summarizes the results of our hypothesis testing.

Table 6. Summary of Hypotheses Tests

<table><tr><td rowspan="2" colspan="2">Hypotheses</td><td colspan="2">Supported</td></tr><tr><td>Hx(a)</td><td>Hx(b)</td></tr><tr><td>H1</td><td>Raters presented with larger idea subsets (i.e., less partitioning) will select ideas with higher (a) novelty and (b) feasibility than raters presented with smaller idea subsets.</td><td>No</td><td>No</td></tr><tr><td>H2</td><td>Raters presented with larger idea subsets (i.e., less partitioning) adopt a more cue-wise (i.e., less option-wise) processing strategy than raters presented with smaller idea subsets.</td><td colspan="2">Yes</td></tr><tr><td>H3</td><td>Raters adopting a more cue-wise (i.e., less option-wise) processing strategy expend higher levels of cognitive effort.</td><td colspan="2">Yes</td></tr><tr><td>H4</td><td>Raters expending a high level of cognitive effort select ideas with higher (a) novelty and (b) feasibility.</td><td>Yes</td><td>No, inverse direction supported</td></tr><tr><td>H5</td><td>Raters&#x27; information processing strategy and cognitive effort serially mediate the relationship between partitioning and selection quality, such that larger idea subsets lead to a more cue-wise information processing strategy, which in turn increases cognitive effort and subsequently results in the selection of ideas with higher (a) novelty and (b) feasibility.</td><td>Yes</td><td>No, inverse direction supported</td></tr><tr><td>H6</td><td>The mediating effects of information processing strategy and cognitive effort on the relationship between partitioning and the selection of ideas with higher (a) novelty and (b) feasibility are moderated by the regulatory focus of the rater, such that raters receiving larger subsets adopt an even more cue-wise processing strategy when they have a prevention focus and raters receiving smaller subsets adopt an even more option-wise processing strategy when they have a promotion focus.</td><td>No</td><td>No</td></tr></table>

## 6 Discussion

Our research aimed to investigate how idea set partitioning affects idea selection quality and raters’ information processing behavior. We discovered a novel causal mechanism, which we term effortfulcomparative information processing and which explains how partitioning nudges influence decision outcomes. The mechanism indicates that as larger versus smaller subsets are presented, the frequency of comparisons between cues of different options also increases, resulting in greater cognitive effort. Conversely, when smaller versus larger subsets are presented, raters tend to focus more on comparing cues within each option, reducing cognitive effort. A more effortful-comparative approach resulted in the identification of more novel ideas with larger subsets, while a less effortfulcomparative approach led to the identification of more feasible ideas with smaller subsets.

By analyzing eye-tracking data, we observed significant differences in the information processing strategies and cognitive effort required when comparing smaller subsets with larger subsets. Related research on sequential and simultaneous presentation has suggested that more options allow for easier comparisons between ideas, resulting in more optimal choices (Basu & Savani, 2017, 2019). However, empirical evidence has so far been lacking. Our eye-tracking findings of changes in effortful-comparative information processing provide evidence that partitioning nudges impact decisions by promoting more or less deliberate thinking. A handful of other studies further support that nudging does not exclusively rely on System 1 processing. For instance, research by Van Gestel et al. (2020) demonstrated the effectiveness of default nudges even in situations with extensive deliberation. Moreover, investigations on recommender systems conducted by Kretzer and Maedche (2018) revealed that elaboration of recommendations can attenuate the impact of social influence nudges. Our findings contribute to the conceptualization that nudging encompasses a mechanism beyond System 1 processing, emphasizing the explanatory power that the effortful-comparative information processing mechanism can add to the nudging phenomenon.

We expected the regulatory focus of non-expert raters to moderate the effectiveness of the partitioning nudge. Specifically, we expected that a prevention focus would foster effortful-comparative information processing when idea subsets were larger. However, our findings did not reveal such a moderation, thereby indicating that the regulatory focus did not influence the effectiveness of the partitioning nudge. Thus, we could not confirm that regulatory focus influences information processing (Mantel & Kardes, 1999; Pham & Avnet, 2004; Zhu & Meyers-Levy, 2007) and did not detect an interaction with cue- and option-wise processing (Mourali & Pons, 2009) in idea selection tasks. It could be that the effect size of our regulatory focus priming was too weak to be detectable with our sample size.

Our results show that adaptations in information processing also occur when the total choice set is left unchanged but divided into smaller or larger subsets. This complements related decision-making research that has identified adaptations of the information processing strategy in response to manipulating the total choice set size (Lohse & Johnson, 1996; Russo & Dosher, 1983). We observed that raters applied different information processing strategies depending on the size of the subset, suggesting that they focused primarily on the information displayed within a single subset and thus discounted cues from prior subsets in their decision-making process. This observation supports the assertion that raters tend to decide among the options displayed currently to them (Payne et al., 1993). However, we are cautious in our prediction that our findings on partitioning effects can be generalized to much larger subsets. In the eye-tracking study, we manipulated only subsets of size two and four. Based on research on assortment sizes in consumer research (Scheibehenne et al., 2010), we expect that there is a tipping point where the subset would include too many ideas and cues, requiring too much cognitive effort to process the provided reference points, likely causing cognitive overload. Beyond such a tipping point, we anticipate that decision makers will switch from effortful-comparative information processing to more heuristic, less effortful information processing.

## 6.1 Theoretical Implications

Our findings have implications for nudging and choice architecture literature in that they challenge the notion that nudging primarily affects decision-making through heuristic processing and cognitive biases, as traditionally theorized (Kretzer & Maedche, 2018). Our findings instead suggest that partitioning fosters deliberate processing— effortful-comparative information processing— characterized by increased cue-wise comparisons and higher cognitive effort. Thus, our research provides a nuanced understanding of nudging and questions the prevailing notion that digital nudges rely solely on heuristic processing. Consequently, our research provides a novel mechanism that sheds light on the effects of nudging and suggests that partitioning subtly directs individuals toward a more deliberate information processing approach, as opposed to relying solely on heuristic processing. Individuals often turn to heuristics to save cognitive resources in overly complex decisions (Tversky & Kahneman, 1974) because there are limits to humans’ cognitive capacities and abilities to process information (Simon, 1955). For example, a heuristic process, such as the rule of thumb, will likely reduce the amount of information processed and thus lead to systematic errors or biased decisions that require more extensive deliberation (Evans, 2008; Mirsch et al., 2018). While the typical nudging approach builds theoretical bridges to heuristic processing, our approach demonstrates that (digital) nudging can also be utilized to guide individuals toward applying more cognitive effort to the task and comparing alternative solutions. By changing the choice environment, we reveal changes in the information processing behavior of raters, who are subtly guided toward more effortful, comparative information processing that leads to better choices while maintaining full freedom of choice.

Second, we complement research on information processing strategies (e.g., Chu & Spires, 2003; Johnson & Payne, 1985) by showing that raters who apply more cue-wise information processing also apply more cognitive effort during idea selection tasks. This observation helps clarify the mixed findings of prior studies about the relative effortfulness of information processing strategies. Related literature (Chu & Spires, 2003; Johnson & Payne, 1985; Payne et al., 1993) has associated cue-wise strategies with heuristic and effortless processing while linking strategies following pure option-wise processing with rational and effortful processing. Since our empirical evidence shows that cognitive effort increases when strategies are more cuewise, our findings support the stream of literature observing that more cue-wise strategies can also reflect deliberation (Horstmann et al., 2009) and improve selection quality (Magnusson et al., 2016). We explain the observed option-wise processing requiring lower cognitive effort with past research showing that optionwise processing fosters more holistic and imaginary information processing (McGill & Anand, 1989), which should be less effortful.

Third, our findings have implications for the literature on open innovation and crowdsourcing (e.g., Leimeister et al., 2009; Schlagwein & Bjorn-Andersen, 2014). Our research demonstrates that distinct levels of applied cognitive effort arising from different information processing strategies influence the quality of idea selection for non-expert raters. Based on the effortaccuracy framework in decision-making (Johnson & Payne, 1985; Payne et al., 1993), we expected that nonexpert raters who are nudged to apply an effortfulcomparative information processing approach would make more accurate decisions, selecting ideas with both high novelty and high feasibility. However, our empirical results suggest that more cognitive effort leads to selecting ideas with higher novelty but lower feasibility. The inverse relationship between criteria indicates that raters do not focus on both criteria simultaneously and equally (Zhu et al., 2017) when selecting the most promising ideas. Instead, raters prioritize novelty, which has been considered a hallmark of creativity in prior literature (Runco & Charles, 1993). Moreover, this prioritization comes at the cost of an idea’s feasibility, since novel ideas have typically not yet been implemented and are thus perceived to be less feasible (Rietzschel et al., 2010).

## 6.2 Practical Implications

Based on our findings, we offer some recommendations to innovation contest hosts who want to ensure that their non-expert raters are correctly selecting novel and feasible ideas from a large pool of generated ideas. To support non-experts in their evaluations, prior literature suggests that contest hosts should lower the level of complexity of the task and reduce the risk of overwhelming raters by partitioning a large number of ideas into more manageable subsets (Santiago Walser et al., 2019). However, our findings show that drastically reducing complexity by highly partitioning the idea set into small subsets may lead raters to prioritize feasibility over novelty. Contest hosts who want raters to identify novel ideas should provide non-expert raters with idea subsets that are large enough to offer multiple reference points for comparison.

## 6.3 Limitations

As with other research, this study has a few limitations that should be considered. First, our study focuses on idea novelty and feasibility as quality criteria. Although these criteria have been used widely (e.g., Blair & Mumford, 2007; Mumford, 2003; Rietzschel et al., 2010), other quality criteria like elaboration (Blohm et al., 2016) exist, to which our findings may not be generalized.

Second, we followed the call to understand human cognition in information systems contexts (Riedl et al., 2014) by utilizing methods of NeuroIS research (vom Brocke & Liang, 2014) to collect objective data about cognitive processing (Djamasbi et al., 2010). On the one hand, this allowed us to investigate raters’ information processing, as measured by the strategy index, and cognitive effort, without the need to rely on self-reported measures. On the other hand, the eye-tracking setting restricted our experimental design because it prevented us from exploring idea subsets that were larger than four ideas per screen. The reason for this limit was that we had to arrange the feedback cues with enough buffer between them to account for the accuracy of the eye-tracking device, which resulted in a maximum of four ideas per screen. Extending the size of subsets to eight or more ideas might have uncovered even more significant differences in the measured variables. Our experimental setting also diverges from potential selection practices where raters can view a more condensed presentation of ideas, use a scroll function, or use pop-up functionality to view more details on ideas.

Finally, we measured cue-wise information processing with transitions that occurred between options but not across subsets. The experimental setup did not allow raters to jump back and forth between screens to compare ideas. We made this design decision to reduce the variance of user behaviors, given the small N study. It is possible that information processing strategies and the ensuing cognitive effort might have shown different patterns if raters could have freely moved back and forth between screens. Hence, our findings should be interpreted in the context of comparisons across subsets not being possible.

## 6.4 Future Research and Conclusion

Our research points to several avenues of further research. Since raters are limited in their cognitive capacity (Simon, 1955), related research has found that presenting a non-partitioned idea set that visualizes all ideas simultaneously reduces selection quality (Santiago Walser et al., 2019). The positive effects of providing more reference points, and thus inviting more comparisons, are increasingly offset by the greater cognitive effort required to process the rising number of ideas per subset. Given that our experimental setup limited us to presenting no more than four ideas per subset, future research should explore subsets containing more than four ideas. It should also investigate the conditions in which tipping points occur—where increasing the number of ideas no longer enhances evaluability but instead overloads raters with information and diminishes selection quality. Future research should also examine the effects of the identified effortful-comparative processing mechanism on additional criteria such as elaborateness or relevance (Dean et al., 2006) when idea sets are partitioned into larger versus smaller subsets.

In conclusion, our research shows how the design of selection platforms can nudge information processing and selection quality. Specifically, our results show how contest hosts can alter the choice environment by partitioning the choice set into smaller or larger subsets to nudge non-expert raters to adopt more or less effortful-comparative information processing, which will influence selection quality.

## References

Arazy, O., Kopak, R., & Hadar, I. (2017). Heuristic Principles and Differential Judgments in the Assessment of Information Quality. Journal of the Association for Information Systems, 18(5), 403- 432.

Armisen, A., & Majchrzak, A. (2015). Tapping the innovative business potential of innovation contests. Business Horizons, 58(4), 389-399.

Ball, C. (1997). A comparison of single-step and multiple-step transition analyses of multiattribute decision strategies. Organizational Behavior and Human Decision Processes, 69(3), 195-204.

Banken, V., Ilmer, Q., Seeber, I., & Haeussler, S. (2019). A method for Smart Idea Allocation in crowdbased idea selection. Decision Support Systems, 124, Article 113072.

Basu, S., & Savani, K. (2017). Choosing one at a time? Presenting options simultaneously helps people make more optimal decisions than presenting options sequentially. Organizational Behavior and Human Decision Processes, 139, 76-91.

Basu, S., & Savani, K. (2019). Choosing Among Options Presented Sequentially or Simultaneously. Current Directions in Psychological Science, 28(1), 97-101.

Bayus, B. L. (2013). Crowdsourcing New Product Ideas over Time: An Analysis of the Dell IdeaStorm Community. Management Science, 59(1), 226- 244.

Beretta, M. (2019). Idea Selection in Web-Enabled Ideation Systems. Journal of Product Innovation Management, 36(1), 5-23.

Bettman, J. R., Johnson, E. J., & Payne, J. W. (1990). A Componential Analysis of Cognitive Effort in Choice. Organizational Behavior and Human Decision Processes, 45(1), 111-139.

Blair, C. S., & Mumford, M. D. (2007). Errors in idea evaluation: preference for the unoriginal? The Journal of Creative Behavior, 41(3), 197-222.

Blohm, I., Riedl, C., Füller, J., & Leimeister, J. M. (2016). Rate or trade? Identifying winning ideas in open idea sourcing. Information Systems Research, 27(1), 27-48.

Brandstätter, E., Gigerenzer, G., & Hertwig, R. (2006). The priority heuristic: Making choices without trade-offs. Psychological Review, 113(2), 409- 432.

Bröder, A., Newell, B. R., & Platzer, C. (2010). Cue integration vs. exemplar-based reasoning in multiattribute decisions from memory: A matter of cue

representation. Judgment and Decision Making, 5(5), 326-338.

Bruine de Bruin, W., & Keren, G. (2003). Order effects in sequentially judged options due to the direction of comparison. Organizational Behavior and Human Decision Processes, 92(1-2), 91-101.

Carter, B. T., & Luke, S. G. (2020). Best practices in eye tracking research. International Journal of Psychophysiology, 155, 49-62.

Chen, L., Xu, P., & Liu, D. (2020). Effect of Crowd Voting on Participation in Crowdsourcing Contests. Journal of Management Information Systems, 37(2), 510-535.

Cheng, X., Fu, S., de Vreede, T., de Vreede, G. J., Seeber, I., Maier, R., & Weber, B. (2020). Idea convergence quality in open innovation crowdsourcing: A cognitive load perspective. Journal of Management Information Systems, 37(2), 349-376.

Chernev, A. (2004). Goal-attribute compatibility in consumer choice. Journal of Consumer Psychology, 14(1-2), 141-150.

Chu, P. C., & Spires, E. E. (2003). Perceptions of accuracy and effort of decision strategies. Organizational Behavior and Human Decision Processes, 91(2), 203-214.

Cohen, P., West, S. G., & Aiken, L. S. (2003). Applied multiple regression/correlation analysis for the behavioral sciences. In Lawrence Erlbaum Associates Publishers (3rd ed.).

Congiu, L., & Moscati, I. (2021). A review of nudges definitions, justifications, effectiveness. Journal of Economic Surveys, 36(1), 1-26.

Creyer, E. H., Bettman, J. R., & Payne, J. W. (1990). The Impact of accuracy and effort feedback and goals on adaptive decision behavior. Journal of Behavioral Decision Making, 3(1), 1-16.

Crowe, E., & Higgins, E. T. (1997). Regulatory focus and strategic inclinations: Promotion and prevention in decision-making. Organizational Behavior and Human Decision Processes, 69(2), 117-132.

Cui, Z., Kumar PM, S., & Gonçalves, D. (2019). Scoring vs. ranking: An experimental study of idea evaluation processes. Production and Operations Management, 28(1), 176-188.

de Buisonjé, D. R., Ritter, S. M., de Bruin, S., ter Horst, J. M. L., & Meeldijk, A. (2017). Facilitating creative idea selection: The combined effects of selfaffirmation, promotion focus and positive affect. Creativity Research Journal, 29(2), 174-181.

Dean, D. L., Hender, J. M., Rodgers, T. L., & Santanen, E. L. (2006). Identifying quality, novel, and

creative ideas: Constructs and scales for idea evaluation. Journal of the Association for Information Systems, 7(10), 646-698.

Djamasbi, S., Siegel, M., & Tullis, T. (2010). Generation Y, web design, and eye tracking. International Journal of Human Computer Studies, 68(5), 307- 323.

Einhorn, H. J., & Hogarth, R. M. (1981). Behavioral decision theory: Processes of judgment and choice. Annual Review of Psychology, 32(1), 53- 88.

Eling, K., Langerak, F., & Griffin, A. (2015). The performance effects of combining rationality and intuition in making early new product idea evaluation decisions. Creativity and Innovation Management, 24(3), 464-477.

Evans, J. S. B. T. (2008). Dual-processing accounts of reasoning, judgment, and social cognition. Annual Review of Psychology, 59, 255-278.

Fehrenbacher, D. D., & Djamasbi, S. (2017). Information systems and task demand: An exploratory pupillometry study of computerized decision making. Decision Support Systems, 97, 1-11.

Fishburn, P. C. (1974). Lexicographic Orders, utilities and decision rules: A survey. Management Science, 20(11), 1442-1471.

Ford, J. K., Schmitt, N., Schechtman, S. L., Hults, B. M., & Doherty, M. L. (1989). Process tracing methods: Contributions, problems, and neglected research questions. Organizational Behavior and Human Decision Processes, 43(1), 75-117.

Förster, J., & Higgins, E. T. (2005). How global versus local perception fits regulatory focus. Psychological Science, 16(8), 631-636.

Förster, J., Higgins, E. T., & Taylor, A. (2003). Speed/accuracy decisions in task performance: Built-in trade-off or separate strategic concerns? Organizational Behavior and Human Decision Process, 90, 148-164.

Freitas, A. L., & Higgins, E. T. (2002). Enjoying goaldirected action: The role of regulatory fit. Psychological Science, 13(1), 1-6.

Friedman, R. S., & Forster, J. (2001). The effects of promotion and prevention cues on creativity. Journal of Personality and Social Psychology, 81(6), 1001-1013.

Galati, F. (2015). Complexity of judgment: Ahat makes possible the convergence of expert and nonexpert ratings in assessing creativity. Creativity Research Journal, 27(1), 24-30.

Gigerenzer, G., & Goldstein, D. G. (1996). Reasoning the fast and frugal way: Models of bounded

rationality. Psychological Review, 103(4), 650- 669.

Girotra, K., Terwiesch, C., & Ulrich, K. T. (2010). Idea generation and the quality of the best idea. Management Science, 56(4), 591-605.

Glaholt, M. G., & Reingold, E. M. (2011). Eye movement monitoring as a process tracing methodology in decision making research. Journal of Neuroscience, Psychology, and Economics, 4(2), 125-146.

Görzen, T., & Kundisch, D. (2017). When in doubt follow the crowd: How idea quality moderates the effect of an anchor on idea evaluation. International Conference on Information Systems (ICIS), 1-20.

Hayes, A. F. (2018). Introduction to mediation, moderation, and conditional process analysis: A regression-based approach. In Guilford Press (2nd ed.).

Heitmann, M., Lehmann, D. R., & Herrmann, A. (2007). Choice goal attainment and decision and consumption satisfaction. Journal of Marketing Research, 44(2), 234-250.

Higgins, E. T. (1998). Promotion and prevention: Regulatory focus as a motivational principle. Advances in Experimental Social Psychology, 30(C), 1-46.

Hoornaert, S., Ballings, M., Malthouse, E. C., & Van den Poel, D. (2017). Identifying new product ideas: Waiting for the wisdom of the crowd or screening ideas in real time. Journal of Product Innovation Management, 34(5), 580-597.

Horstmann, N., Ahlgrimm, A., & Glöckner, A. (2009). How distinct are intuition and deliberation? An eye-tracking analysis of instruction-induced decision modes. Judgment and Decision Making, 4(5), 335-354.

Hsee, C. K., & Leclerc, F. (1998). Will products look more attractive when presented separately or together? Journal of Consumer Research, 25(2), 175-186.

Hsee, C. K., & Zhang, J. (2010). General evaluability theory. Perspectives on Psychological Science, 5(4), 343-355.

IBM. (2018). Watson natural language understanding. https://www.ibm.com/cloud/watson-naturallanguage-understanding

Jang, J. M., & Yoon, S. O. (2016). The effect of attributebased and alternative-based processing on consumer choice in context. Marketing Letters, 27(3), 511-524.

Javadi, E., Gebauer, J., & Mahoney, J. (2013). The impact

of user interface design on idea integration in electronic brainstorming: An attention-based view. Journal of the Association for Information Systems, 14(1), 1-21.

Jesse, M., & Jannach, D. (2021). Digital nudging with recommender systems: Survey and future directions. Computers in Human Behavior Reports, 3(December 2020), Article 100052.

Johnson, E. J., & Payne, J. W. (1985). Effort and Accuracy in Choice. Management Science, 31(4), 395-414.

Johnson, E. J., Shu, S. B., Dellaert, B. G. C., Fox, C., Goldstein, D. G., Häubl, G., Larrick, R. P., Payne, J. W., Peters, E., Schkade, D., Wansink, B., & Weber, E. U. (2012). Beyond nudges: Tools of a choice architecture. Marketing Letters, 23(2), 487-504.

Juslin, P., Jones, S., Olsson, H., & Winman, A. (2003). Cue abstraction and exemplar memory in categorization. Journal of Experimental Psychology: Learning Memory and Cognition, 29(5), 924-941.

Just, M. A., & Carpenter, P. A. (1976). Eye fixations and cognitive processes. Cognitive Psychology, 8(4), 441-480.

Kahneman, D. (2011). Thinking, fast and slow. Farrar, Straus, Giroux.

Kim, K., Bae, J., Nho, M. W., & Lee, C. H. (2011). How do experts and novices differ? Relation versus attribute and thinking versus feeling in language use. Psychology of Aesthetics, Creativity, and the Arts, 5(4), 379-388.

Klein, M., & Garcia, A. C. B. (2015). High-speed idea filtering with the bag of lemons. Decision Support Systems, 78, 39-50.

Koo, T. K., & Li, M. Y. (2016). A guideline of selecting and reporting intraclass correlation coefficients for reliability research. Journal of Chiropractic Medicine, 15(2), 155-163.

Kretzer, M., & Maedche, A. (2018). Designing social nudges for enterprise recommendation agents: An investigation in the business intelligence systems context. Journal of the Association for Information Systems, 19(12), 1145-1186.

Kruger, J. L., Hefer, E., & Matthew, G. (2013). Measuring the impact of subtitles on cognitive load: Eye tracking and dynamic audiovisual texts. Proceedings of the 2013 Conference on Eye Tracking South Africa (pp. 62-66).

Leimeister, J., Huber, M., Bretschneider, U., & Krcmar, H. (2009). Leveraging crowdsourcing: Activation-supporting components for IT-based

ideas competition. Journal of Management Information Systems, 26(1), 197-224.

Lohse, G. L., & Johnson, E. J. (1996). A comparison of two process tracing methods for choice tasks. Organizational Behavior and Human Decision Processes, 68(1), 28-43.

Magnusson, P. R., Wästlund, E., & Netz, J. (2016). Exploring users’ appropriateness as a proxy for experts when screening new product/service ideas. Journal of Product Innovation Management, 33(1), 4-18.

Mantel, S. P., & Kardes, F. R. (1999). The role of direction of comparison, attribute-based processing, and attitude-based processing in consumer preference. Journal of Consumer Research, 25(4), 335-352.

McGill, A. L., & Anand, P. (1989). The effect of imagery on information processing strategy in a multiattribute choice task. Marketing Letters, 1(1), 7-16.

McGraw, K. O., & Wong, S. P. (1996). Forming inferences about some intraclass correlation coefficients. Psychological Methods, 1(1), 30-46.

Mele, C., Russo Spena, T., Kaartemo, V., & Marzullo, M. L. (2021). Smart nudging: How cognitive technologies enable choice architectures for value co-creation. Journal of Business Research, 129(August 2020), 949-960.

Meservy, T. O., Jensen, M. L., & Fadel, K. J. (2014). Evaluation of competing candidate solutions in electronic networks of practice. Information Systems Research, 25(1), 15-34.

Meyers-Levy, J. (1989). Gender differences in information processing: A selectivity interpretation. In P. Cafferata & A. Tybout (Eds.), Cognitive and affective responses to advertising (pp. 219-260). Lexington Books.

Mirsch, T., Lehrer, C., & Jung, R. (2018). Making digital nudging applicable: The digital nudge design method. International Conference on Information Systems (ICIS).

Mollick, E., & Nanda, R. (2016). Wisdom or madness? Comparing crowds with expert evaluation in funding the arts. Management Science, 62(6), 1533-1553.

Mourali, M., & Pons, F. (2009). Regulatory fit from attribute-based versus alternative-based processing in decision making. Journal of Consumer Psychology, 19(4), 643-651.

Mumford, M. D. (2003). Where have we been, where are we going? Taking stock in creativity research. Creativity Research Journal, 15(2-3), 107-120.

Mumford, M. D., Lonergan, D. C., & Scott, G. (2002). Evaluating creative ideas. Inquiry: Critical Thinking Across the Disciplines, 22(1), 21-30.

Patalano, A. L., Juhasz, B. J., & Dicke, J. (2010). The relationship between indecisiveness and eye movement patterns in a decision making informational search task. Journal of Behavioral Decision Making, 23(4), 353-368.

Payne, J. W. (1976). Task complexity and contingent processing in decision making : An information search and protocol analysis. Organizational Behavior and Human Performance, 16(2), 366- 387.

Payne, J. W. (1982). Contingent decision behavior. Psychological Bulletin, 92(2), 382-402.

Payne, J. W., Bettman, J. R., & Johnson, E. J. (1988). Adaptive strategy selection in decision making. Journal of experimental psychology: Learning, memory, and cognition, 14(3), 534-552.

Payne, J. W., Bettman, J. R., & Johnson, E. J. (1993). The adaptive decision maker. Cambridge University Press.

Pham, M. T., & Avnet, T. (2004). Ideals and oughts and the reliance on affect versus substance in persuasion. Journal of Consumer Research, 30(4), 503-518.

Pilli, L. E., & Mazzon, J. A. (2016). Information overload, choice deferral, and moderating role of need for cognition: Empirical evidence. Revista de Administração, 51(1), 36-55.

Riedl, R., Brandstätter, E., & Roithmayr, F. (2008). Identifying decision strategies: A process-and outcome-based classification method. Behavior Research Methods, 40(3), 795-807.

Riedl, R., Davis, F., & Hevner, A. (2014). Towards a NeuroIS research methodology: Intensifying the discussion on methods, tools, and measurement. Journal of the Association for Information Systems, 15(10), i-xxxv.

Rietzschel, E. F., Nijstad, B. A., & Stroebe, W. (2010). The selection of creative ideas after individual idea generation: Choosing between creativity and impact. British Journal of Psychology, 101(1), 47- 68.

Rietzschel, E. F., Nijstad, B. A., & Stroebe, W. (2019). Why great ideas are often overlooked. In P. B. Paulus & B. A. Nijstad (Eds.), The Oxford handbook of group creativity and innovation (pp. 178-197). Oxford University Press.

Rucker, D. D., Preacher, K. J., Tormala, Z. L., & Petty, R. E. (2011). Mediation analysis in social psychology: Current practices and new

recommendations. Social and Personality Psychology Compass, 5(6), 359-371.

Runco, M. A., & Charles, R. E. (1993). Judgments of originality and appropriateness as predictors of creativity. Personality and Individual Differences, 15(5), 537-546.

Russo, J. E., & Dosher, B. A. (1983). Strategies for multiattribute binary choice. Journal of Experimental Psychology: Learning, Memory, and Cognition, 9(4), 676-696.

Santanen, E. L., Briggs, R. O., & de Vreede, G.-J. (2004). Causal relationships in creative problem solving: Comparing facilitation interventions for ideation. Journal of Management Information Systems, 20(4), 167-198.

Santiago Walser, R., Seeber, I., & Maier, R. (2019). Designing idea convergence platforms: The role of decomposition of information load to nudge raters towards accurate choices. AIS Transactions on Human-Computer Interaction, 11(3), 179-207.

Scheibehenne, B., Greifeneder, R., & Todd, P. M. (2010). Can there ever be too many options? A metaanalytic review of choice overload. Journal of Consumer Research, 37(3), 409-425.

Schlagwein, D., & Bjorn-Andersen, N. (2014). Organizational learning with crowdsourcing: the revelatory case of LEGO. Journal of the Association for Information Systems, 15(11), 754-778.

Simon, H. A. (1955). A behavioral model of rational choice. The Quarterly Journal of Economics, 69(1), 99.

Simonson, I., Nowlis, S., & Lemon, K. (1993). The effect of local consideration sets on global choice between lower price and higher quality. Marketing Science, 12(4), 357-377.

Sunstein, C. R. (2014). Nudging: A very short guide. Journal of Consumer Policy, 37(4), 583-588.

Thaler, R. H., & Sunstein, C. R. (2009). Nudge: Improving decisions about health, wealth, and happiness. Penguin Books.

Thaler, R. H., Sunstein, C. R., & Balz, J. P. (2012). Choice architecture. SSRN. https://doi.org/ 10.2139/ssrn.1583509

Toubia, O., & Netzer, O. (2017). Idea Generation, Creativity, and Prototypicality. Marketing Science, 36(1), 1-20.

Tversky, A. (1972). Elimination by aspects: A theory of choice. Psychological Review, 79(4), 281-299.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124-1131.

Van Gestel, L. C., Adriaanse, M. A., & De Ridder, D. T. D. (2020). Do nudges make use of automatic processing? Unraveling the effects of a default nudge under type 1 and type 2 processing. Comprehensive Results in Social Psychology, 5(1–3), 4-24.

Venema, T. A. G., Kroese, F. M., Benjamins, J. S., & de Ridder, D. T. D. (2020). When in doubt, follow the crowd? Responsiveness to social proof nudges in the absence of clear preferences. Frontiers in Psychology, 11. https://doi.org/10.3389/fpsyg. 2020.01385

vom Brocke, J., & Liang, T. P. (2014). Guidelines for neuroscience studies in information systems research. Journal of Management Information Systems, 30(4), 211-234.

Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital Nudging. Business & Information Systems Engineering, 58(6), 433-436.

Westbrook, A., & Braver, T. S. (2015). Cognitive effort: A neuroeconomic approach. Cognitive, Affective and Behavioral Neuroscience, 15(2), 395-415.

Willemsen, M. C., & Keren, G. (2004). The role of negative features in joint and separate evaluation. Journal of Behavioral Decision Making, 17(4), 313-329.

Zhao, X., Lynch, J. G., & Chen, Q. (2010). Reconsidering Baron and Kenny: Myths and truths about mediation analysis. Journal of Consumer Research, 37(2), 197-206.

Zhu, R., & Meyers-Levy, J. (2007). Exploring the cognitive mechanism that underlies regulatory focus effects. Journal of Consumer Research, 34(1), 89-96.

Zhu, Y., Ritter, S. M., Müller, B. C. N., & Dijksterhuis, A. (2017). Creativity: Intuitive processing outperforms deliberative processing in creative idea selection. Journal of Experimental Social Psychology, 73, 180-188.

Zugal, S., Pinggera, J., Neurauter, M., Maran, T., & Weber, B. (2017). Cheetah Experimental Platform Web 1.0: Cleaning pupillary data. arXiv. https://doi.org/10.48550/arXiv.1703.09468

Appendix A: Operationalization of Measures

<table><tr><td>Construct</td><td>Measure</td><td>Formula</td><td>Description</td><td>Scale</td></tr><tr><td>Information processing strategy</td><td>Strategy index (SI)</td><td>For each screen s: $SI_s = \frac{tro_s - trc_s}{tro_s + trc_s}$ Aggregated: $SI = \frac{\sum_{s=0}^{n} \frac{tro_s - trc_s}{tro_s + tro_s}}{n}$ </td><td> $tro_s$ refers to the number of option-wise transitions on a screen s.trcsrefers to the number of cue-wise transitions on a screen snrefers to the total number of idea subsets, which is either 8 or 16.</td><td>Interval scale between -1 (purely cue-wise) +1 (purely option-wise)</td></tr><tr><td>Cognitive effort</td><td>Pupil dilation (PD)</td><td>For each time stamp t: $PD_t = \frac{(LPD_t + RPD_t)}{2} - BPD$ Aggregated: $PD = \frac{\sum_{t=0}^{n} \frac{(LPD_t + RPD_t)}{2} - BPD}{n}$ </td><td> $LPD_t$ refers to the pupil dilation of the left eye at time stamp t $RPD_t$ refers to the pupil dilation of the right eye at time stamp tBPDrefers to the average pupil dilation (both eyes) during the last introduction screen.nrefers to the total number of time stamps of the eye-tracking recording during the idea selection task.</td><td>Interval scale</td></tr><tr><td>Idea novelty</td><td>Novelty of selected ideas</td><td>For each idea i: $Nov_i = s_i * rn_i$ Aggregated: $Nov = \frac{\sum_{i=0}^{n} s_i * rn_i}{\sum_{i=0}^{n} s_i}$ </td><td> $s_i$ shows whether the idea iwas selected by the participant, being 1 if it was selected and 0 if it was not selected. $rn_i$ refers to the mean novelty rating of the idea iacross experts.nrefers to the total number of ideas in the idea set, which is 32.</td><td>Interval scale</td></tr><tr><td>Idea feasibility</td><td>Feasibility of selected ideas</td><td>For each idea i: $Feas_i = s_i * rf_i$ Aggregated: $Feas = \frac{\sum_{i=0}^{n} s_i * rf_i}{\sum_{i=0}^{n} s_i}$ </td><td> $s_i$ shows whether the idea iwas selected by the participant, being 1 if it was selected and 0 if it was not selected. $rf_i$ refers to the mean feasibility rating of the idea iacross experts.nrefers to the total number of ideas in the idea set, which is 32.</td><td>Interval scale</td></tr></table>

Appendix B: Correlation Between Feedback Cues and Selections by Non-Expert Raters

<table><tr><td>Feedback cue</td><td>Number of times the idea was selected by non-experts</td></tr><tr><td>Number of likes</td><td>0.678***</td></tr><tr><td>Historical idea score</td><td>0.532**</td></tr><tr><td>Creativity score</td><td>- 0.134</td></tr><tr><td colspan="2">Note: * significance level 0.05; ** significance level 0.01, *** significance level 0.001</td></tr></table>

## About the Authors

Frederik Wiedmann holds a doctorate in management from the University of Innsbruck, Austria. His research interests include digital nudging in the contexts of crowd-based innovation and crowdwork. His research has appeared in the proceedings of the European Conference on Information Systems, the Hawaii International Conference on System Sciences, and Information Systems and Neuroscience. https://orcid.org/0000-0001-9311-3810

Arnold Wibmer holds a doctorate in management from the University of Innsbruck, Austria. His research interests include eye-tracking, crowd-based innovation, and digital nudging. His research has appeared in proceedings of the European Conference on Information Systems, the Hawaii International Conference on System Sciences, and Information Systems and Neuroscience. https://orcid.org/0000-0002-7665-9990

Isabella Seeber is an associate professor of information systems in the Department of Management, Technology, and Strategy at Grenoble Ecole de Management, France. She holds a doctorate in business administration from the University of Innsbruck, Austria, where she also obtained her habilitation degree. Her research interests include conversational AI in team collaboration, team and crowd-based innovation, digital nudging, and digitalization in knowledge management. Her research has appeared in journals such as Journal of the Association for Information Systems, Journal of Management Information Systems, Decision Support Systems, Internet Research, and Information & Management. https://orcid.org/0000-0001-8246-8974

Ronald Maier is a professor of information systems at the University of Innsbruck, Austria, and also serves as vice rector for Digitalisation and Knowledge Transfer at the University of Vienna, Austria. He received his PhD in management information systems from WHU Otto Beisheim School of Management in Koblenz, Germany, and a habilitation degree from the University of Regensburg, Germany. His research interests include collaboration engineering, connectivity, crowdsourcing, and knowledge management. His research has appeared in journals such as Journal of Management Information Systems, Journal of Strategic Information Systems, and Business & Information Systems Engineering. https://orcid.org/0000-0001-9764-7289
