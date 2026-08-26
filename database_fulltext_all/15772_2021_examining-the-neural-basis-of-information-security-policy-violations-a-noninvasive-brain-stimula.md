---
otero_id: 15772
otero_key: "XSEKKXTG"
title: "Examining the Neural Basis of Information Security Policy Violations: A Noninvasive Brain Stimulation Approach"
authors: "Ofir Turel; Qinghua He; Yatong Wen"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/15717"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# EXAMINING THE NEURAL BASIS OF INFORMATION SECURITY POLICY VIOLATIONS: A NONINVASIVE BRAIN STIMULATION APPROACH<sup>1</sup>

Ofir Turel

School of Computing and Information Systems, Faculty of Engineering and Information Technology, University of Melbourne, Parkville, VIC, Australia {oturel@unimelb.edu.au}

Qinghua He and Yatong Wen Faculty of Psychology, MOE Key Laboratory of Cognition and Personality, Southwest University, Chongqing, CHINA {heqinghua@swu.edu.cn} {wyt523@outlook.com}

Nonmalicious information security policy (ISP) violations can cause organizations significant harm. Here, we aim to extend the understanding of why employees engage in such acts. A large body of ISP violation research is based on the tenet that people violate ISPs to obtain personal benefits, as explained by rational choice and expectancy theories. But this assumption has only been weakly tested, using mostly correlational approaches. Our objective is to improve the causal basis for this argument by using a noninvasive brain stimulation (NIBS) technique, which actually modulates brain activity in regions of the brain that process value/gain assessments. Therefore, it can substantially increase the claim of causality—that expected rewards lead to ISP violations. To do so, we build on expectancy theory and neuroscience knowledge to theorize why reducing the excitability of neurons in the left dorsolateral prefrontal cortex (L DLPFC) can lower the endorsement of ISP violations. We test this idea in four experiments in which we use a NIBS technique called high-definition direct current stimulation (HD-tDCS). Our findings support the assertion that the L DLPFC is likely involved in the expectancy theory of ISP violations, and that endorsing such violations can be experimentally adjusted with NIBS techniques. These findings extend the understanding of cybersecurity behaviors, improve the causal support for the common assumption made by rational choice theory studies that ISP violations are motivated through perceived benefits, point to the need to consider the L DLPFC in research on positively valenced (or attractive) technology-mediated actions, and pave the way for future use of brain stimulation techniques for stronger causality claims in information systems research

Keywords: Information systems security, cybersecurity, transcranial direct current stimulation, neuroIS, decision-making, expectancy theory, IS policy violations, noninvasive brain stimulation

## Introduction

Cybersecurity is a high priority for practitioners and information systems (IS) researchers alike. The importance of this topic stems from the constantly evolving growing scale and set of threats to organizations, as well as the magnitude of problems that cybersecurity incidents cause (Cram et al. 2019; Cram et al. 2017). For example, the average cost per event for 1,579 reported cybersecurity incidents with damages of over \$100,000 was \$43.49M and the median loss was \$1.53M (Eling and Wirfs 2019).

While outside attackers or technical failures may account for some of these statistics, cybersecurity incidents often stem from—and are enabled at least in part by—insider or employee actions that bypass, neutralize, or disregard cybersecurity practices and policies (Barlow et al. 2018). Examples of these activities include information mishandling, and unauthorized downloads (Hu et al. 2015). Such behaviors are termed information security policy (ISP) violations and are defined as self-benefiting noncompliance with cybersecurity policies or standard practices (Willison and Warkentin 2013). Despite much research on this topic,

ISP violations remain an important problem (Barlow et al. 2018). They are typically (but not always) nonmalicious. Given their high prevalence and harm potential, we focus on volitional nonmalicious ISP violations (those not intended to cause harm) (Guo et al. 2011; Ormond et al. 2019); hereafter these are simply referred to as “ISP violations.”

Given the self-serving nature of ISP violations, and consistent with motivation theories (Steel and König 2006), ISP violations are likely motivated through the expected value, benefits, or gains they produce. For example, the motivation for not changing a password is a function of how much this inaction is expected to generate net positive gain to the user in terms of the user’s goals (e.g., making it easier to login, and consequently completing work tasks faster). Although the benefits of ISP violations are a part of a number of theories, they are most clearly stated in rational choice theory (Becker 1968) and expectancy theory (Vroom 1964). Previous studies on ISP violations have only tested rational choice theory and the motivational role of percived benefits using correlational techniques (Bulgurcu et al. 2010; Hu et al. 2011; Li et al. 2010; Vance and Siponen 2012). In other words, a large body of ISP violation research has been based on the tenet that people violate to obtain personal benefits, but this assumption has only been weakly tested. Our research objective is to improve the understanding of the persistence of ISP violations from the perspective of value/gain (benefit) assessment and its neural underpinnings using an approach that provides stronger support for causal inference. Our research question is: Do brain regions that process value/gains associated with actions mediate the endorsement of ISP violations?

Previous research has shown that the left dorsolateral prefrontal cortex (L DLPFC) mediates cognitive functionality (or processes thoughts), which relate to value judgment (He et al. 2016; Wen et al. 2019). Building on this, we first hypothesize that the L DLPFC mediates ISP violations. We next posit that if we could disturb the value/gain assessment function in the brain so that the outcomes of positively valenced target actions are perceived to be less attractive (Vroom 1964), we could reduce people’s endorsement of ISP violations, which would be reflected in lower attitudes and behavioral intentions. Thus, we propose that experimentally reducing the excitability of the L DLPFC with a noninvasive brain stimulation (NIBS) technique can impair the value/gain judgment function in the brain and consequently reduce the endorsement of ISP violations. We note that previous studies have lumped expected gains together with attitudes (see, Cram et al. 2019; Cram et al. 2017); however, attitudes are broader and can be based, in part, on gain assessments. By stimulating the L DLPFC, we can therefore more specifically examine the presumed effect of value/gain assessment on the endorsement of ISP violations. To establish causality through the experimental manipulation of the brain, we used NIBS techniques because they offer advantages over the commonly used NeuroIS techniques and surveys. NIBS, in contrast to correraltional surveys, actually modulate brain activity in regions of the brain that process (in our case, value/gain) assessments, thereby substantially increasing the claim of causality—that reward calculus leads to ISP violations.

Our hypotheses were tested in four experiments, all of which used a NIBS technique called high-definition transcranial direct current stimulation (HD-tDCS). In all experiments, the dependent variable was endorsements of (attitude and intentions toward) hypothetical scenarios rather than actual behavior, which is consistent with the majority of experimental research on ISP violations (Cram et al. 2019). Experiment 1 (n=56) asked participants to respond to counterbalanced control and ISP violation scenarios before and after reducing the excitability of their L DLPFC. Experiment 2 (n=66) added a randomly assigned sham condition (“pretend” stimulation) to the design of Experiment 1. Both studies were consistent in showing that the employed brain stimulation protocol can reduce the endorsement of ISP violations more than it reduces endorsement of less positively valenced control behaviors and more than it decreases endorsement of ISP violations in people receiving sham stimulation. Experiment 3 (n=48) indicated that the same procedure applied to a control (i.e., less functionally relevant) brain region (the visual cortex) does not produce the same results. Thus, the effects observed in Experiments 1 and 2 can be attributed to the L DLPFC. In Experiment 4 (n=18) we showed that the results in Studies 1 and 2 are polarity specific, that is, they do not inverse when switching from cathodal to anodal polarity.

From a theoretical standpoint, our findings support the idea that ISP violations are partly rational behaviors that likely involve value/gain assessment of expected outcomes as mediated by L DLPFC activity. This extends current views of the neural underpinnings of ISP violations that have focused on deficits in self-control brain centers and functions (Hu et al. 2015), and provides a more nuanced perspective compared to studies that focus on broader attitudes as drivers of ISP violations (Cram et al. 2019). By using NIBS, our findings also lend stronger support to causality than would be achievable with most other NeuroIS techniques and surveys (Dumont et al. 2018a). Lastly, the results pave the way for future NeuroIS research on processes that are mediated via the L DLPFC and for future use of noninvasive brain stimulation to study various IS user behaviors, including a broader range of technology-mediated dangerous behaviors (Turel, 2021).

From a practical standpoint, the findings can inform cybersecurity training practices. Specifically, they suggest that security education training and awareness (SETA) programs may need to be updated to focus on reducing users’ value/gain assessments that relate to ISP violations—and not just on the harm or broader attitude aspect of such acts.

## Theory and Hypothesis

## Motivation to Engage in ISP Violations

ISP violations seem to be at least partially rational behaviors motivated by attitudes toward such acts (Guo et al. 2011). Even though negative emotions (such as when employees feel unjustly treated) can also drive such events, the affective path is small, and significant only among frustrated employees (Ormond et al. 2019). Indeed, aside from attitudes, ISP violations are influenced by a range of rational reflections, such as response cost, detection certainty, and threat severity (Cram et al. 2019). As a result, we take a rational-motivational perspective in this study.

The motivation to engage in any behavior, presumably including ISP violations, can be explained by a judgmental value-assessment mechanism that calculates the expected gains from the action relative to some reference point (McClelland 1987). People are utility maximizers; they typically choose actions with positive value/gains and prefer higher value/gains over lower ones. This notion should apply to ISP violations, with people more likely to choose to violate ISPs if they see positive value/gains in the outcomes of this activity (e.g., it will result in increased job performance).

At the heart of this claim is the notion that ISP violations are instrumental for achieving user goals; they are conducted to serve the needs of users (Vance and Siponen 2012). For example, using unauthorized networks, downloading illegal software, or taking home classified data, can assist in finishing work on time. Attaining such goals can cater to selfactualization needs (Maslow 1943), the need for achievement (McClelland 1987), and the need for competence (Deci 1975), all of which motivate human actions (Bolles 1967). This is consistent with the functionalist view of attitude development (Katz 1960), in which attitudes are construed to assess whether actions cater to the functionalist needs of humans. When elements such as sanctions and neutralization processes stay constant, people who see high value/gain in the outcomes of ISP violations are more likely than others to endorse them.

Indeed, the role of value/gain assessment in motivating behaviors has been expressed, albeit mostly indirectly, in a range of motivation theories. These include expectancy theory (Vroom 1964), prospect theory (Kahneman and Tversky 1979), control theory (Carver and Scheier 1982), cybernetics theory (Wiener 1948), self-determination theory (Deci and Ryan 1985), and theories of reasoned action and planned behavior (Ajzen 1985). Collectively, these theories assume that people develop perceptions that relate to gains of actions (or inaction) as a basis for their behavioral choices. Such value/gain judgments have been incorporated directly or indirectly into various behavioral cybersecurity studies. For example, motivations to comply with ISPs have been explained by deterrence theory, neutralization theory, the theory of reasoned action, and protection motivation theory (Cram et al. 2017), among others.

Such studies imply that cybersecurity behavior is motivated by the ability of actions (or inactions) to provide gains that bridge the gap between the present and a desired end state (Liang and Xue 2009, 2010). It has been shown that the perceived utility of ISP violations (such as job performance gains) is a significant predictor of endorsing these violations (Guo et al. 2011). Although most studies in this area have either emphasized costs associated with ISP violations (e.g., detection certainty, punishment severity) or assumed that gains are reflected in attitudes (Cram et al. 2019), attitudes are summative reflections that account for a broad range of evaluations regarding the behavior, and not just expected gains. By focusing directly on processing the value/gains associated with violations (as mediated by the L DLPFC), and separating them from punishment avoidance and selfcontrol (as assumed to be mediated by the R DLPFC, see Hu et al. 2015), we present a unique perspective that can generate a more nuanced understanding of why people engage in ISP violations.

In formulating our hypotheses, we build on expectancy theory (Vroom 1964), which directly focuses on value/gain judgments, and many motivation theories expand on it. Specifically, expectancy theory suggests that motivation is a function of expectancy (perceptions that it is feasible to attain the goal with the chosen action), instrumentality (perceptions that the action increases progress toward the goal), and valence (the value/expected gain one places on the outcome of the action) (Vroom 1964). It posits that motivation to act is high when the outcome of the action is highly valued (positive valence), the action is perceived to help individuals achieve desired goals, and the link between the action and attaining the goal is clear. This theory can apply to many decision-making situations (Lawler and Suttle 1973).

When applied to ISP violations, the implication is that this course of action is more likely to be endorsed when people (1) believe that goals, such as completing a task on time, can be attained, for example, by using an unauthorized network (expectancy is high); (2) perceive that engaging in ISP violation (e.g., taking classified materials home) contributes to their ability to complete the work task (instrumentality is high); and (3) place high value on the outcome of ISP violations (e.g., work completion is seen as a large gain), and ISP violation is therefore highly positively valenced.

## DLPFC and Decision-Making

The DLPFC is a large region of the prefrontal cortex that is a center for decision-making (Turel and Bechara 2021). It has left and right hemisphere subregions. Our focus on the DLPFC in this study was guided by both theoretical and practical reasons. From a theoretical standpoint, the activation of the bilateral DLPFC has been shown to mediate goal formulation and gain expectancy development (Barraclough et al. 2004; Hare et al. 2009; Krain et al. 2006; McClure et al. 2007) and it is therefore expected to be associated with the decision-making processes prescribed by expectancy theory (Vroom 1964). This involvement is through the functional role of the DLPFC in higher-order cognitive processes that underlie decision-making (Chen et al. 2019b), including the weighing of potential gains of behaviors (Baumgartner et al. 2011; Hayashi et al. 2013; Heekeren et al. 2006; Wallis and Miller 2003). Appendix A provides a review of NeuroIS studies that have focused on the DLPFC. Visualization of the L DLPFC location (with the right being a mirror image) is shown in Figure 1 (Row A).

From a practical standpoint, NIBS techniques are better suited for the stimulation of cortical (outer brain) rather than subcortical (deeper) regions (Dumont et al. 2018a), as stimulating areas near the brain stem can cause health complications (Zhao et al. 2017). Targeting cortical brain regions that mediate decision-making may therefore be more useful and realistic. Indeed, many studies have demonstrated the potential of DLPFC stimulation to alter decision-making (Wen et al. 2019); we thus build on existing paradigms in neuroscience to advance knowledge in the IS discipline.

## Left DLPFC’s Role in ISP Violations

Without discounting the importance of the many other regions of the brain that can mediate decision-making, we focus specifically on the L DLPFC. This choice was guided by the presumed role of the L DLPFC in the expectancy theory account of positively valenced behaviors, of which ISP violation is an instance. Specifically, the left hemisphere of the prefrontal cortex tends to mediate the processing of positively framed expectancies (benefits, rewards, positive emotions) and approach motivation (Damasio 1994; Davidson 2004; Heller and Nitschke 1998; Joseph 1992). This region of the brain is also involved in the heuristic-based calculation (or mental shortcuts) and attribution of value/gains that assess the outcome of positively valenced behaviors (Ernst et al. 2004; Krawczyk 2002). As such, it can be relevant for the valence judgment of ISP violations.

Taking this view into account, it has been shown that the L DLPFC is engaged when assessing the value/gains of behaviors (Knoch et al. 2006), resultant approach behaviors (Huang et al. 2017), and the processing of reward contingencies (Sobotka et al. 1992). The mental calculus of value/gain judgments, mediated in part by the L DLPFC, has been included in various neuroscientific models of decisionmaking, as part of the “cold” (cognitive) executive function in the brain (Nejati et al. 2018). NeuroIS studies have focused on the DLPFC (see review in Appendix A), including for ISP violations (Hu et al. 2015), but limited attention has been paid to the role of the L DLPFC.

We note that ISP violations require the development of goals and an assessment of the benefits/valence of obtaining them. For example, when people decide to share their password, they expect gains from this action (e.g., accelerated teamwork, obtaining social acceptance). The assessment of these gains is presumed to be mediated via the L DLPFC (Ahn et al. 2013), which has been shown to be involved in approach assessments (Sutton and Davidson 1997). This has been demonstrated in functional MRI studies that found that the L DLPFC is activated in motivated behavior choices (Heekeren et al. 2006), and in brain stimulation studies that revealed how L DLPFC stimulation can influence motivated behaviors (Philiastides et al. 2011). This happens because the L DLPFC’s cognitive functionality is needed for making decisions. For example, a person must decide whether to download an illegal copy of software to achieve goals, and address immediate needs (e.g., complete a task). Attaching expected gains to this action requires the retrieval of past experiences from memory, recapturing or constructing goals, and ultimately developing gain heuristics, all of which are mediated by the L DLPFC (Sokol-Hessner et al. 2012; Steinbeis et al. 2012; Steinbeis et al. 2016). Thus:

H1: The L DLPFC is involved in endorsing ISP violations.

## Left DLPFC Stimulation Effects on ISP Violations

NIBS includes techniques such as transcranial magnetic stimulation (TMS), transcranial alternating current stimulation (tACS), transcranial random noise stimulation (tRNS), transcranial pulsed current stimulation (tPCS), transcranial ultrasound stimulation (TUS), and tDCS (Dumont et al. 2018a; Zhao et al. 2017). In the NIBS family, tDCS is the most commonly used, safest, and easiest tool to deploy. It produces temporary neural modulation by running low amperage electrical current through the target brain region via electrodes that are placed on the scalp (Kuo et al. 2013). It is efficacious, and its only known side effects are light itching or tingling (Brunoni et al. 2011). Its benefits, underlying biophysiological mechanisms, configurations, limitations, and risks are explained elsewhere (see Dumont et al. 2018a; Zhao et al. 2017).

![](/api/attachments/XSEKKXTG/fulltext/images/7656f2dd710e5657cbc61785c0852037f62e1fa713bcaee4e320e062a125eb08.jpg)  
Maps generated with Soterix HD-Explore (Soterix Medical Inc., New York, NY, USA) for Experiments 1-2 when applying cathodal stimulation to the left DLPFC (A), Experiment 3 when applying cathodal stimulation to the left visual cortex (B), and Experiment 4 when applying anodal stimulation to the left DLPFC (C). The first column shows the center electrode positioning (in red). The second column shows the field intensity mapped on a standardized brain. It shows the flow of the current but not cellular effects. The last three columns show the coronal, sagittal, and axial slices of field intensity maps, respectively. Lines with arrow represent the current flow. Color bar indicates the field intensity (V/m). L: left; R: right; F: Frontal; B: Back.

Figure 1. Electrode Positioning of HD-tDCS and Expected Current Flow

Given such advantages, it has been widely used across neuroscience domains (Zhao et al. 2017). The technique’s main limitation is its ability to primarily reach cortical or outer regions of the brain. When trying to run current through subcortical or deeper structures, one must pass through cortical regions, which can confound the results. This may also result in running current through the brain stem, which can impair respiratory functions (Zhao et al. 2017). Thus, tDCS is mostly relevant in research settings when the theory dictates that the cortical surface is the target region.

An important feature of tDCS is that it can be set to increase or decrease the excitability of neurons in the brain areas being targeted and presumably upregulate or downregulate activity there. The direction of the effect is a function of how the current is directed, i.e., whether the polarity is positive or negative. Anodal (or positive) stimulation increases the excitability of target regions, while cathodal (negative) stimulation reduces it (Antal et al. 2003; Nitsche and Paulus 2000)<sup>2</sup>. These effects can last minutes to days (Zhao et al. 2017).

With its cortical location and involvement in many decision processes, the DLPFC has been a common stimulation target (Boggio et al. 2010; He et al. 2016). Nevertheless, the results of such studies have not been consistent (see Appendix A for a list of specific and review tDCS to DLPFC studies). This is most likely because of differences in stimulation polarity (anodal vs. cathodal), stimulation configuration (one hemisphere vs. both), the current used (0.5mA to 2mA), as well as the specific decision tasks involved. While previous studies mostly used tDCS, we use HD-tDCS because, by comparison, it increases stimulation focality (Villamar et al. 2013) and is a more precise and effective form of NIBS. Because of this difference, we have not relied on prior findings in our case. We therefore employed multiple studies with slightly different designs to increase confidence in the results.

The extant literature clearly reveals that cathodal stimulation to the L DLPFC (and a presumed reduction of excitability) has the potential to reduce the endorsement of positively valenced behaviors and shows that it does so by interrupting the value/gain assessment processes that make value/gains less salient in creating motivation. The L DLPFC is involved in weighing expected gains and promoting approach behaviors (Huang et al. 2017). When this area of the brain is upregulated with anodal stimulation, positively valenced (attractive) noninformation system actions are increased (He et al. 2016). It is possible then that temporarily suppressing activity in the L DLPFC may reduce a person’s ability to assign expected gains to a target ISP violation. According to motivation theories, reducing gain expectations should reduce behavior endorsement. From an expectancy theory perspective, the valence of the ISP violation outcome is expected to be reduced through such stimulation; consequently, the endorsement of these violations is expected to diminish. Overall, prior research points to the potential that the application of cathodal tDCS to the L DLPFC will reduce gain expectancies associated with positively valenced behaviors, which presumably include ISP violations. Hence, this neural stimulation can indirectly reduce the endorsement of such acts. We hypothesize:

H2: Cathodal stimulation of the L DLPFC will reduce (a) attitude toward, and (b) intentions to engage in ISP violations.

The L DLPFC does not exclusively process ISP violation gains (Nejati et al. 2018; Zhang et al. 2016). We therefore used control scenarios that were less positively valenced in comparison to ISP violations) as a way to increase confidence in the role of valence in the hypothesized changes (see scenario development description in Appendix B; pilot tests described in Appendix C show that the valence of ISP violations was significantly higher than that of control scenarios). We expected the interruption in value/gain assessment that we produced to generate stronger effects in the more positively valenced acts (ISP violations), compared to the control scenarios that were less positively valenced. The logic was that if positive valence were lower, value/gain information—interrupted or not— would be less relevant because people would be less motivated to integrate it into their decisions (Verplanken and Holland 2002). In contrast, if we interrupted value/gain processing in highly valenced behaviors, we would integrate lower or less clear values into the decision-making and produce outcomes less influenced by the value of the act (Valentin 2005). This is consistent with theories of motivation to process information, such as the elaboration likelihood model (Petty and Cacioppo 1986). We hence hypothesize that:

H3: The hypothesized reduction in attitudes and intentions (H2) will be stronger in ISP violations than in less positively valenced control scenarios.

## Method

The hypotheses were validated in four experiments (see Table 1). The objective of the multiple-study approach was to increase validity through replication with multiple designs (Studies 1 and 2), and to rule out alternative explanations (Studies 3 and 4).

All experiments employed HD-tDCS as the NIBS technique. While surveys and many common NeuroIS approaches (e.g., fMRI, fNIRS, and EEG) allow correlations between brain function and IS phenomena to be examined, NIBS techniques such as tDCS allow stronger causality inferences and are able to show that a brain region is necessary for an IS process. Conventional tDCS produces current flow through a relatively greater brain region between two large targeted surface electrodes, and this makes it difficult to maximize the utility of the current in focal points (Knotkova et al. 2019). HD-tDCS optimizes the stimulation focality by diminishing the electrode size. This is achieved because HD-tDCS uses a 4x1 ring-shaped electrode in which the center ring electrode is placed above the target cortical region and is surrounded by four return electrodes of opposite polarity. Compared to conventional electrode placement, this pattern results in higher focality and greater target intensity by restricting the flow of the current to outer cortical regions (Hogeveen et al. 2016). In addition, the aftereffects of HD-tDCS remain longer than those generated by conventional tDCS (Kuo et al. 2013). These advantages guided our decision to use HD-tDCS. Electrode positioning and simulated current flows for the four experiments are depicted in Figure 1. Figure 2 shows the HDtDCS device (left) in use with a participant (right).

<table><tr><td colspan="5">Table 1. Overall Experimental Plan</td></tr><tr><td></td><td>Experiment 1 (n=56)</td><td>Experiment 2 (n=66)</td><td>Experiment 3 (n=48)</td><td>Experiment 4 (n=18)</td></tr><tr><td>Objective</td><td>Test ability of cathodal tDCS over L DLPFC to change pre-stimulation endorsement of ISP violations</td><td>Test ability of cathodal tDCS over L DLPFC compared with sham stimulation to change pre-stimulation endorsement of ISP violations</td><td>Test that stimulation of a brain region that is less functionally relevant for ISP violations (L visual cortex) does not produce the L DLPFC effects.</td><td>Test that the observed effects are likely specific to the examined polarity (cathodal) and cannot be achieved or maybe even inversed with inversed polarity (anodal).</td></tr><tr><td>Design</td><td>Within-subjects; all subjects receive cathodal tDCS. A 2 (scenarios: test vs. control) x 2 (time: pre vs. post) repeated, within-factors design.</td><td>Between x two within mixed design; 33 subjects receive cathodal tDCS and 33 sham stimulation over L DLPFC. A 2 (stimulation: cathodal vs. sham, a between factor) x 2 (scenarios: test vs. control) x 2 (time: pre vs. post) repeated, between- within factors design.</td><td>Between x two within mixed design; 24 subjects receive cathodal tDCS and 24 sham stimulation over L visual cortex. A 2 (stimulation: cathodal vs. sham, a between factor) x 2 (scenarios: test vs. control) x 2 (time: pre vs. post) repeated, between- within factors design.</td><td>Within-subjects; all subjects receive anodal tDCS. A 2 (scenarios: test vs. control) x 2 (time: pre vs. post) repeated, within-factors design.</td></tr><tr><td>Required sample</td><td>17</td><td>18</td><td>18</td><td>17</td></tr><tr><td>Electrode positioning</td><td>Cathodal electrode over F3 and four anodal electrodes over F5, AF3, FC3, and F1</td><td>Cathodal electrode over F3 and four anodal electrodes over F5, AF3, FC3, and F1</td><td>Cathodal electrode over PO3 and four anodal electrodes over P1 P5 PO7 and O1</td><td>Anodal electrode over F3 and four cathodal electrodes over F5, AF3, FC3, and F1</td></tr><tr><td>Current</td><td>1.5mA (~20min)</td><td>1.5mA (~20min)</td><td>1.5mA (~20min)</td><td>1.5mA (~20min)</td></tr><tr><td>Statistical analysis</td><td>Repeated two-way ANCOVA</td><td>Repeated three-way ANCOVA</td><td>Repeated three-way ANCOVA</td><td>Repeated two-way ANCOVA</td></tr></table>

Note: L= Left, ANCOVA= analysis of covariance, tDCS= transcranial direct current stimulation, DLPFC=dorsolateral prefrontal cortex. Electrode positioning is based on the International 10-20 EEG System (Herwig et al. 2003); Required sample sizes were calculated a-priori with G\*Power 3.1 (Faul et al. 2009) for detecting a large effect (f = 0.3, equivalent to Cohen’s d = 0.6) with a probability of 0.80 (1-β).

![](/api/attachments/XSEKKXTG/fulltext/images/c5cd283d3bdc62e26692eb0eacb6daa5248ee1a48f376ee5db04252b50c8974e.jpg)

![](/api/attachments/XSEKKXTG/fulltext/images/4bcaacca389ad2cc4ba3cfb1e941240623d5d43ba1669ca51c1717fb886d5e1b.jpg)  
Figure 2. The HD-tDCS Device (left) and Being Used by a Participant (right)

## Experiment 1: tDCS Potential to Change Endorsement of ISP Violations

## Participants: Experiment 1

Fifty-six healthy college students (33 females, $\mathbf { M } _ { \mathrm { a g e } } = 2 0 . 4 1$ $\mathrm { S D } _ { \mathrm { A g e } } ~ = ~ 1 . 5 5$ years) volunteered to participate in this experiment. All were right-handed, had normal or correctedto-normal vision, and were free of psychotic, anxiety, depressive, bipolar, or substance abuse disorders, according to the Structured Clinical Interview for DSM-IV (First et al. 2001). None of them had traumatic brain injury or a history of neurological and psychiatric disorders (Kuo et al. 2014; Zhao et al. 2017). They were screened to make sure they were naive to tDCS research. All gave informed written consent before the experiment. Each participant was paid 80 RMB (about \$12) as a token of appreciation.

## Design and Procedure: Experiment 1

The experiment employed a single-blind within-subjects pre-post design (see Figure 3), in which each participant responded to counterbalanced control and case scenarios before and after stimulation (HD-tDCS to the L DLPFC). Each participant read and responded to four control and four ISP violation scenarios twice. These scenarios were randomly drawn without repetition from a pool of eight control and eight ISP violation scenarios. The four-plus-four scenarios before tDCS were different from those applied after tDCS. Following each scenario, the participants endorsement of ISP violations was captured with appropriate scales. One scenario at a time was randomly selected (without reuse) and displayed on the screen for at least 30 seconds before allowing an endorsement rating. This allowed participants to focus on the scenarios. To ensure they understood the procedure, they took part in two practice scenarios beforehand, which involved choice in unrelated domains: cafeterias and food.

After this pre-intervention, the volunteers had a two-minute break, during which their hair was separated to prepare the scalp at the stimulation site. Each participant then received cathodal HD-tDCS over the L DLPFC area at 1.5mA for 20 minutes. The current was delivered by ramping-up in the first 30 seconds and down in the last 30 seconds. A period of four minutes at the beginning of the stimulation allowed participants to adapt to it. They were asked to verbally report any discomfort. This was followed by the post-intervention phase, which employed the remaining four control scenarios and four ISP violation scenarios.

Because the effect of similar tDCS protocols can last at least 20 minutes after the intervention ends (Zhao et al. 2017), we terminated the current about nine minutes before the end of the post-test phase (or 12 minutes before the experiment was over) to ensure experimental effects, while at the same time minimizing participant discomfort. Even though, on the whole, no discomfort is typically reported (Dumont et al. 2018a; Zhao et al. 2017), at the end of the experiment the participants filled out a questionnaire about their tolerance of and feelings during the tDCS. They were also asked to guess if they were subjected to a “true” stimulation or were in a sham condition. This was done to ensure that the procedure felt natural to them and that they were blinded to the treatment.

## Materials: Experiment 1

Scenarios and Measures: The scenarios were carefully developed (see Appendix B) to ensure realism, and so that people could see more potential gains in ISP violation outcomes in the more positively valenced situations than in the control scenario behavior outcomes. This was validated (see Appendix C). In all the scenarios, participants were instructed to imagine they were a character with a common unisex Chinese name (Xiaoming) who is under academic and time pressure. We expected ISP violations that would help participants reach their educational goals (highly relevant in the study’s context) and anticipated highly positively valenced behavior to resolve the time pressure. The eight control scenarios focused on mundane student decisions, with positive but lower valence compared to the ISP violation scenarios.

After each scenario, participants were asked to complete attitude and intention scales regarding how they would have behaved, had they been in the same situation. Scales were adapted from Guo et al. (2011). The scales were pilot tested with 20 students (15 females, $M _ { \mathrm { a g e } } = 2 1 . 2 0 , S D _ { \mathrm { A g e } } = 1 . 3 2$ years); the responses established scale validity and reliability. (The materials used in the experiments are provided in English in Appendix B, and the pilot study results can be found in Appendix C.)

To rule out cases of tDCS discomfort (Villamar et al. 2013), we asked respondents at the end of the post-test session to report the extent to which they experienced any of the following issues: headache, neck pain, scalp pain, tingling, skin redness, sleepiness, trouble concentrating, acute mood change and other self-reported issues (1 = absent and 4 = severe). Participants also indicated the extent they thought these were related to HDtDCS and reported whether they received real or sham brain stimulation (1 = not at all; 5 = definitely).

![](/api/attachments/XSEKKXTG/fulltext/images/855c6e0e06fe1f58fc458c0e9529323c5d764b9722bd92beb321cc0495c1cb74.jpg)  
The procedure (pre-test, stimulation, and post-test) lasted about one hour. A two-minute break was given after the pre-test. HDtDCS started 4 minutes before the post-test and lasted 20 minutes. The last nine minutes relied on the lasting effect of tDCS, which was terminated at this point. Scenarios included a practice session and two experiment sessions. The pre-test study session included four randomly selected control, and four randomly selected ISP violation scenarios. The post-test scenarios included the remaining scenarios. After the instructions were given, one scenario at a time was displayed on the screen, and attitude and intention scales were administered after each trial. Tolerance assessment, including checking naivety to the test conditions, was performed at the end of the experiment.

## Figure 3. Experimental Procedure: Experiment 1

HD-tDCS: Applying tDCS over the left DLPFC has been shown to influence functions needed for decision-making (See Appendix A). Here we used HD-tDCS with a 4 x1 multichannel stimulation adapter, and a conventional tDCS device (Soterix Medical Inc.). Based on the International 10- 20 EEG System (Herwig et al. 2003), the cathodal electrode was placed over F3 and the four anodal electrodes placed over F5, AF3, FC3, and F1 . This configuration is in line with previous studies on the L DLPFC (He et al. 2016). Stimulation location determination followed procedures in Chen et al. (2019a). The HD-tDCS was delivered at 1.5mA for 20 minutes.

## Results: Experiment 1

None of the participants reported experiencing adverse effects during or after HD-tDCS. They were blinded to the stimulation and, after the experiment, 26/56 participants guessed that they were in a sham condition. Given that the attitude and intention scales were reliable (Cronbach’s alphas of 0.76 and 0.75, respectively), averages were calculated for each scenario. These were aggregated to pre-test and post-test attitude and intention scores, as well as separately for the control and ISP violation scenarios. Comparing these scores showed that endorsement was higher for control than for the ISP violation scenarios, consistent with the pilot study $( M _ { \mathrm { I S P \pm } }$

$S D _ { \mathrm { I S P } } = 3 . 5 0 \pm 0 . 8 9 \mathrm { v s . } M _ { \mathrm { c o n t r o l } } \pm S D _ { \mathrm { c o n t r o l } } = 5 . 7 3 \pm 0 . 7 2 , t ( 5 5 ) =$ $- 1 6 . 6 2 , p < 0 . 0 0 1$ , in attitude scale; and M<sub>ISP</sub> + SD<sub>ISP</sub> = 3.82 + 0.90 vs. $M _ { \mathrm { c o n t r o l } } \pm S D _ { \mathrm { c o n t r o l } } = 5 . 4 3 \pm 0 . 7 5 , t ( 5 5 ) = - 1 1 . 5 7 , p <$ 0.001, in intention scale).

HD-tDCS Effects: Attitude scores were analyzed with a 2 (time: pre- vs. post-stimulation score, a within-subjects factor) by 2 (scenarios: control vs. ISP violation scenarios, a withinsubjects factor) ANCOVA, controlling for sex (male vs. female, a between-subjects factor). We controlled for possible sex differences, given that men and women can differ in their responses to DLPFC stimulation (Ye et al. 2015). Results revealed a significant main effect of time [F(1,54) = 13.07, p = 0.001, η<sup>2</sup> = 0.20], suggesting that HD-tDCS significantly decreased participants’ attitude toward ISP violation (Figure 4a). There was also a significant main effect of scenarios [F(1,54) = 523.49, p < 0.001, η<sup>2</sup> = 0.91](Figure 4a), but no significant main effect of sex [F(1,54) = 3.53, p = 0.07, η<sup>2</sup> = 0.06]. Importantly, there was a significant time x scenarios interaction [F(1,54) = 18.69, p < 0.001, η<sup>2</sup> = 0.26], but no time x sex [F(1,54) = 0.61, p = 0.44, η<sup>2</sup> = 0.01], scenarios x sex [F(1,54) = 0.63, p = 0.43, η<sup>2</sup> = 0.01], or a three-way [F(1,54) = 2.22, p = 0.14, η<sup>2</sup> = 0.04] interaction. Simple effects (Figure 4a) revealed that HD-tDCS significantly decreased attitudes toward ISP violation [F(1,54) = 33.58, p < 0.001, η<sup>2</sup> = 0.38], but not toward control scenarios [F(1,54) = 0.09, p = 0.77, η<sup>2</sup> = 0.002].

a  
![](/api/attachments/XSEKKXTG/fulltext/images/095aee83221c886f83c48e641911977df3275a7e53a2cb40ccdcf98b76045065.jpg)

![](/api/attachments/XSEKKXTG/fulltext/images/0d80477b2862766abf12cc1016f11ecee3dc59299cacfc4def195fb535cf93c6.jpg)  
(a) Two-way ANCOVA model of pre- and post-tDCS attitude scores revealed significant main effects of tDCS and scenarios as well as significant interaction. A follow-up simple effects test demonstrated a significant impact of tDCS on reducing ISP violation attitudes but not attitudes related to the control scenarios, (b) the same tDCS effects were found in relation to intention scores.

Note: $^ { \star \star } p < 0 . 0 1 ; ^ { \star \star \star } p < 0 . 0 0 1 ;$ ns = nonsignificant. Error bars represent standard error (SE). The pre-test levels for the control and ISP scenarios were not equivalent in the pre-stimulation measurement. This is because ISP violations are qualitatively different than decisions to engage in control scenario behaviors. They likely involve social and moral norms, risk and punishment expectations that do not exist in the control scenarios

Figure 4. Experiment 1: tDCS Effects on (a) Attitudes and (b) Intentions Related to ISP Violation

Intention scores were analyzed with the same two-way ANCOVA model. Time did not produce significant main effect $[ F ( 1 , 5 4 ) = 3 . 0 3 , p = 0 . 0 9 , \eta ^ { 2 } = 0 . 0 5 ]$ , scenarios did [F(1,54) = 239.88, p < 0.001, $\eta ^ { 2 } = 0 . 8 2 ]$ , and time x scenarios was significant [F(1,54) = 4.41, p = 0.040, η<sup>2</sup> = 0.08] (Figure 4b). The main effect of sex was not significant $[ F ( 1 , 5 4 ) =$ $0 . 7 6 , p = 0 . 3 9 , \eta ^ { 2 } = 0 . 0 1 ]$ . Moreover, no significant time x sex [F(1,54) = 0.01, p = 0.906, $\eta ^ { 2 } < 0 . 0 0 1 ]$ , scenarios x sex [F(1,54) = 2.04, p = 0.159, η<sup>2</sup> = 0.04], or time x scenario x sex [F(1,54) = 0.21, p = 0.646, η<sup>2</sup> = 0.004] interactions were found. Simple effects (Figure 4b) suggested that tDCS significantly reduced ISP violation intentions $[ F ( 1 , 5 4 ) =$ 7.31, p = 0.009, $\eta ^ { 2 } ~ = ~ 0 . 1 2 ]$ , but not control scenario intentions $\left[ F ( 1 , 5 4 ) = 0 . 0 6 , p = 0 . 8 1 0 , \eta ^ { 2 } = 0 . 0 0 1 \right]$

## Discussion: Experiment 1

The results indicate that temporarily impairing the L DLPFC and its presumed value/gain function results in a significant reduction of the endorsement of ISP violations but not of mundane control scenario behaviors. This lends initial support to the idea that interruption of the L DLPFC more strongly affects highly positively valenced behaviors, including ISP violations, than mundane behaviors.

## Experiment 2: tDCS vs. Sham Potential to Change Endorsement of ISP Violations

## Participants: Experiment 2

Sixty-six healthy college students (36 females, $\mathrm { M _ { a g e } = 1 9 . 7 4 , S D _ { A g e } = }$ 1.62 years) were screened, as in Experiment 1, and randomly assigned to tDCS intervention (n=33, 18 females, $\mathbf { M } _ { \mathrm { a g e } } = 1 9 . 5 5 \pm$ 1.42) and sham groups (n=33, 18 females, $\mathbf { M } _ { \mathrm { a g e } } { = } 1 9 . 9 4 \pm 1 . 8 0 )$ ).

## Design and Procedures: Experiment 2

The experiment was like Experiment 1, but with several changed features. First, different control scenarios were used that were developed to be very mundane (low positive valence) (See Appendix B). Second, tDCS was not terminated before the end of the session, as in Experiment 1. Third, it employed a withinand between-subjects design that included a control (sham intervention) group. This group received 30 seconds of stimulation (15-second ramp-up and 15-second ramp-down) so that they could feel they were stimulated. This was done to account for possible placebo effects. We wanted to test whether the differences between the pre- and post-tDCS endorsements could be better attributed to the tDCS vs. to learning and/or placebo influences. Overall, these changes (see Figure 5) were implemented as a means to produce a more robust design and to increase confidence in the findings of Experiment 1.

![](/api/attachments/XSEKKXTG/fulltext/images/3a5bb37cfd1f1342d1bef2d8d2c447a61cf79ac8a2853b4f53520ce7a80b66e9.jpg)  
The procedure (pre-test, stimulation, and post-test) lasted about one hour. A two-minute break was given after the pre-test, HD: tDCS started four minutes before the post-test and lasted about 29 minutes in the case group and 30 seconds in the sham group. It was terminated in the case group when responses to post-test scenarios were completed. Scenarios included a practice session and two experiment sessions. The pre-test study session included four randomly selected control and four randomly selected ISP violation scenarios. The post-test scenarios included the remaining scenarios. After the presentation of instructions, one scenario at a time was displayed on the screen; attitude and intention scales were administered after each trial. Tolerance assessment was conducted at the end of the experiment. Participants were asked to guess which group (sham or stimulation) they believed they belonged to.

Figure 5. Experimental Procedure: Experiment 2

## Results: Experiment 2

None of the 66 participants reported experiencing adverse effects during or after HD-tDCS. They were naive to their stimulation assignment and, after the experiment, 14/33 and 15/33 in the sham and tDCS groups, respectively, guessed they had taken part in the sham scenario. Attitude (α = 0.74) and intention (α = 0.73) scales were reliable. We therefore used their averages. A three-way ANCOVA with two within-subjects factors (scenarios: control vs. ISP violation; and time: pre- vs. post-stimulation), one between-subjects factor (stimulation: tDCS vs. sham), and with sex as a covariate was employed for analyzing attitudes. Results revealed significant main effects of stimulation [F(1,63) = $1 2 . 1 4 , p = 0 . 0 0 1 , \eta ^ { 2 } = 0 . 1 6 ]$ , scenarios $[ F ( 1 , 6 3 ) = 8 4 . 7 6 , p <$ 0.001, $\eta ^ { 2 } = 0 . 5 7 ]$ and time $[ F ( 1 , 6 3 ) = 1 6 . 6 1 , p < 0 . 0 0 1 , \eta ^ { 2 } =$ 0.21]. Sex did not have main $[ F ( 1 , 6 3 ) = 2 . 0 9 , p = 0 . 1 5 3 , \eta ^ { 2 } =$ 0.03] or interaction effects. Significant two-way interactions were observed between scenarios and time [F(1,63) = 10.47, $p = 0 . 0 0 2 , \eta ^ { 2 } = 0 . 1 4 ]$ and stimulation and time [F(1,63) = $6 5 . 9 0 , p < 0 . 0 0 1 , \eta ^ { 2 } = 0 . 5 1 ]$ . There was a significant threeway interaction between time, scenarios and stimulation $\left[ F ( 1 , 6 3 ) = 5 . 9 5 , p = 0 . 0 1 8 , \eta ^ { 2 } = 0 . 0 9 \right]$

Simple effects tests (Figure 6a) revealed a significant decrease in attitudes toward ISP violation $[ F ( 1 , 6 3 ) = 6 0 . 8 4 , p < 0 . 0 0 1$ $\eta ^ { 2 } = 0 . 4 9 ]$ and control scenarios $[ F ( 1 , 6 3 ) = 1 6 . 0 6 , p < 0 . 0 0 1$ $\eta ^ { 2 } { = } 0 . 2 0 ]$ following tDCS. Pairwise comparisons indicate that the difference between scenarios (ISP violation vs. control) only occurred in subjects stimulated with tDCS [F(1,63) = 19.94, $p < 0 . 0 0 1 , \eta ^ { 2 } = 0 . 2 4$ in tDCS vs. F(1,63)= 1.03, p= 0.314, $\eta ^ { 2 } = ~ 0 . 0 2$ in sham group]. No similar significant decrease was observed in the sham group [F(1,63) = 1.20, p = 0.278, $\eta ^ { 2 } = 0 . 0 2 ]$ . We noted that the tDCS intervention produced a significant reduction in both attitudes toward ISP violation and control scenarios. This is reasonable, given that both types of scenarios are positively valenced (see Appendix C). Paired-sample t-tests indicated that the reduction after tDCS was significantly larger $( t ( 3 2 ) = 4 . 0 9 , \ p \ < \ 0 . 0 0 1$ Cohen’s d = 0.89) in ISP violation (M = 0.84 ± 0.71) compared to control $( M = 0 . 2 8 \pm 0 . 3 5 )$ scenarios.

![](/api/attachments/XSEKKXTG/fulltext/images/ab25099a5719d2f4e235ff0ce421336155d55886bbe801534324fda0ce7909b1.jpg)

![](/api/attachments/XSEKKXTG/fulltext/images/e2ffed827f0472b54ffc93bad9fea77f68d9161dd2831f51e7dba45cbf01fd14.jpg)  
(a) Three-way ANCOVA model of pre- and post-tDCS attitude scores revealed significant main effects and interactions. Simple effects and pairwise-comparison tests demonstrated the significant impact of tDCS on reducing attitudes toward ISP violation. This reduction was larger than reductions in attitudes toward control scenarios and compared to changes in the sham stimulation group in (b), the same tDCS effects were found in relation to intention scores.

Note: \*p <0.05; \*\*p < 0.01; \*\*\*p < 0.001; ns = non-significant. Error bars represent standard error (SE).

Figure 6. Experiment 2: tDCS Effects on (a) Attitudes and (b) Intentions Related to ISP Violations

The same three-way ANCOVA was employed for analyzing intentions. A similar pattern of significance emerged. Results reveal significant main effects of stimulation $[ F ( 1 , 6 3 ) = 1 3 . 4 3 , p = 0 . 0 0 1 , \eta ^ { 2 } = 0 . 1 8 ]$ , scenarios [F(1,63) = 20.94, p < 0.001, η<sup>2</sup>= 0.25] and time [F(1,63) = 4.14, p = 0.046, $\eta ^ { 2 } = 0 . 0 6 ]$ . Sex had a main effect on intentions [F(1,63) = 7.66, p = 0.007, η<sup>2</sup> = 0.11], but its interactions did not. A significant two-way stimulation x time interaction was observed [F(1,63) = 32.73, p < 0.001, η<sup>2</sup> = 0.34]. The three-way interaction (time x scenarios x stimulation) was not significant [F(1,63) = 1.48, p= 0.228, η<sup>2</sup> = 0.02].

Simple effects analysis (Figure 6b) showed that cathodal tDCS over the L DLPFC significantly reduced intentions toward ISP violations [F(1,63)=16.26, p < 0.001, η<sup>2</sup>= 0.21], as well as toward control behaviors [F(1,63)= 8.99, p= 0.004, $\eta ^ { 2 } = 0 . 1 3 ]$ . A pairwise comparison showed that the significant difference was only in the tDCS [F(1,63)= 4.14, p= 0.046, $\eta ^ { 2 } = 0 . 0 6 ]$ but not in the sham group $[ F ( 1 , 6 3 ) =$ 0.10, p= 0.756, η<sup>2</sup>= 0.002]. Importantly, the sham stimulation did not change intention toward ISP violation [F(1,63) = 1.96, p = 0.167, η<sup>2</sup> = 0.03]. In addition, while there was a significant reduction in both intentions toward ISP violation and control scenarios in the tDCS group, paired-sample t-tests indicated that the reduction was significantly larger (t(32) = 2.42, p = 0.022, Cohen’s d = 0.44) in ISP violation (M = 0.67, SD = 0.93) compared to control (M = 0.27, SD = 0.40) scenarios.

## Discussion: Experiment 2

The findings regarding attitudes and intentions were consistent with Experiment 1 results (Figures 4a and 4b), suggesting that reducing the excitability of neurons in the left DLPFC results in decreased endorsement of ISP violations, and relatively does not affect endorsement of behaviors with lower positive valence. The null effect of the sham stimulation demonstrated the efficacy of L DLPFC stimulation to reduce ISP violations beyond other (e.g., learning, placebo) effects. The findings therefore provide initial support for the causal involvement of the L DLPFC in ISP violations, because no reductions were observed in the sham group. The finding that the endorsement reduction after tDCS is larger in ISP violation than in control scenarios is consistent with the idea that L DLPFC stimulation affects gain assessments, and as ISP violations are more positively valenced compared to control scenarios, they are more strongly influenced by this stimulation.

Lastly, it is interesting to observe a slight increase in endorsement for control scenarios in the sham condition. One potential explanation is that the participants may be reflecting the researchers’ expectations and providing socially desirable responses; this effect did not take place with regards to less socially approved behaviors (ISP violations) in the sham condition and was overtaken by changes in L DLPFC excitability in the active tDCS condition.

## Experiment 3: Effects of Stimulation of a Control Region

Experiment 3 aimed to examine whether the results obtained in Studies 1 and 2 were related to the L DLPFC, or could be replicated by the same stimulation protocol applied to a region not strongly theoretically related to value/gain assessment (a control region). For this, we specifically focused on the visual cortex. This was a reasonable choice, not only because the visual cortex is not directly involved in valence processing, but also because the stimulation of the L DLPFC may marginally interfere with vision, through pupil dilation (Allaert et al. 2019). The stimulations in Studies 1-3 may be similar in terms of less-relevant functional interferences, but the stimulation of the L DLPFC and not of the visual cortex is theoretically functionally relevant for valence processing. We expect that if the stimulation of the visual cortex does not impair people’s reading ability (which we checked, it did not), it should not produce changes in endorsement of ISP violations or control scenario behaviors.

## Participants: Experiment 3

Forty-eight healthy college students (24 females, $\mathbf { M } _ { \mathrm { a g e } } =$ 19.81, $\mathrm { S D } _ { \mathrm { A g e } } = 1 . 4 1$ years) were recruited following the same procedure and criteria as in in Studies 1 and 2 and were randomly assigned to cathodal (n=24, 12 females, $\mathbf { M } _ { \mathrm { a g e } } = 1 9 . 9 6 , \mathbf { S } \mathbf { D } _ { \mathrm { A g e } } = 1 . 4 6$ years) or sham HD-tDCS (n=24, 13 females, $\mathbf { M } _ { \mathrm { a g e } } = 1 9 . 6 7 , \mathbf { S } \mathbf { D } _ { \mathrm { A g e } } = 1 . 3 7$ years) over the L visual cortex.

## Design and Procedures: Experiment 3

The cathodal electrode was placed over PO3 based on the International 10-20 EEG System (Herwig et al. 2003) and the four anodal electrodes were placed over P1, P5, PO7, and O1. The HD-tDCS was delivered at 1.5mA for 20 minutes, as in the previous experiments.

## Results: Experiment 3

Participants in both groups (sham and cathodal HD-tDCS) were instructed to report blurry or any other vision difficulties at any point during the experiment or afterward. None reported such issues.

Attitudes: A three-way ANCOVA (Figure 7a) with two within-subjects factors (scenarios: control vs. ISP violation;

and time: pre- vs. post-stimulation) was applied to test the change in attitudes toward ISP violation, comparing cathodal vs. sham L visual cortex stimulation (stimulation: a betweensubjects factor). Sex was included as a covariate (male vs. female, a between-subjects factor); it had a significant main effect $[ \mathrm { F } ( 1 , 4 5 ) = 7 . 1 3 , \overset { \cdot } { p } = 0 . 0 1 1 , \eta ^ { 2 } = 0 . 1 4 ]$ , but no interaction effects. Results revealed significant main effects of stimulation $[ \mathrm { F } ( 1 , 4 5 ) = 4 . 5 2 , p = 0 . 0 3 9 , \eta ^ { 2 } = 0 . 0 9 ] ,$ , scenarios $[ \mathrm { F } ( 1 , 4 5 ) = 1 8 7 . 1 2 , p < 0 . 0 0 1 , \eta ^ { 2 } = 0 . 8 1 ]$ , but not time [F(1,45) = 0.54, p = 0.465, η<sup>2</sup> = 0.01]. There was neither a significant three-way interaction $[ \mathrm { F } ( 1 , 4 5 ) = 0 . 5 6 , p = 0 . 4 5 7 , \eta ^ { 2 } = 0 . 0 1 ] ,$ nor significant interactions between scenarios and stimulation $[ \mathrm { F } ( 1 , 4 5 ) = 2 . 3 9 , p = 0 . 1 2 9 , \eta ^ { 2 } = 0 . 0 5 ]$ , time and stimulation $[ \mathrm { F } ( 1 , 4 5 ) = 0 . 1 3 , p = 0 . 7 1 7 , \eta ^ { 2 } = 0 . 0 0 3 ]$ or time and scenarios $\left[ \mathrm { F } ( 1 , 4 5 ) = 0 . 0 5 , p = 0 . 8 2 1 , \eta ^ { 2 } = 0 . 0 0 1 \right]$

## Experiment 4: Polarity Effects

This experiment aimed to examine whether the results obtained in Experiments 1 and 2 can be explained by cathodal stimulation of the L DLPFC or can be reversed if we apply anodal stimulation to the same region. We expected that if the current-direction (polarity) effects were symmetrical and we reversed the direction of the current (i.e., used anodal stimulation), we should observe an increase in the endorsement of ISP violations (as opposed to the decrease we found in Experiments 1 and 2). We posed this expectation loosely and intended to explore rather than validate it because evidence regarding reversed polarity effects: (1) is mixed; (2) typically focuses on simple cognitive or biophysiological processes, as opposed to complex ones, such as ISP violations; and (3) is typically not specific to the L DLPFC.

To illustrate this, several studies showed polarity-dependent effects, such that only one polarity was effective. For example, cathodal stimulation—but not anodal—to the L DLPFC affected interference inhibition on a Stroop task (Soltaninejad et al. 2019). Similarly, anodal stimulation of the L DLPFC with cathodal stimulation of the R DLPFC affected working memory, but the inverse polarity did not (Keshvari et al. 2013). In contrast, other studies have demonstrated polarity-independent effects. For example, tDCS to motor regions produced the same results regardless of polarity (Faber et al. 2017). In further contrast, the polarity of tDCS to motor cortices was shown to influence interhemispheric inhibition in different directions (Tazoe et al. 2014). Thus, it is difficult to fully hypothesize on the effects of the reversed polarity of HD-tDCS to the L DLPFC on ISP violations.

![](/api/attachments/XSEKKXTG/fulltext/images/a8df7658052e1787ace32a8500cef7be17f40f063cab7e619300c9db8621e3fc.jpg)

![](/api/attachments/XSEKKXTG/fulltext/images/af494092ec5497adac6e801916a4e2f8f7467a1644aa37e13aab9fe139ba31d7.jpg)  
Note: \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001; ns = nonsignificant. Error bars represent standard error (SE).  
Figure 7. Experiment 3: L Visual Cortex (PO3) HD- tDCS Effects on (a) Attitudes and (b) Intentions toward ISP Violations, Comparing Cathodal vs. Sham Effects

## Participants: Experiment 4

Eighteen healthy college students (5 females, $\mathbf { M } _ { \mathrm { a g e } } = 1 9 . 8 3$ $\mathrm { S D } _ { \mathrm { A g e } } = 1 . 7 2$ years) were recruited and screened using the same procedures as in the previous experiments. All received anodal L DLPFC stimulation.

## Design and Procedures: Experiment 4

To test reverse polarity effects, the target anodal electrode was placed over F3, and the four cathodal electrodes were placed over F5, AF3, FC3, and F1. The HD-tDCS current strength and duration were identical to those used in prior experiments (1.5mA for 20 minutes).

## Results: Experiment 4

Attitudes: We employed a 2 (scenarios: control vs. ISP violation) by 2 (time: pre- vs. post-stimulation) ANCOVA, controlling for sex (it had no significant effects). Results (Figure 8a) revealed a significant main effect of scenarios [F(1,16) = $7 4 . 4 1 , \mathrm { p } < 0 . 0 0 1 , \mathrm { \eta } ^ { 2 } = 0 . 8 2 ]$ , but not time $\mathrm { \Delta } [ \mathrm { F } ( 1 , 1 6 ) = 3 . 7 4 , p =$ $0 . 0 7 1 , \ \eta ^ { 2 } = 0 . 1 9 ]$ , and no interaction of time by scenarios $[ \mathrm { F } ( 1 , 1 6 ) = 0 . 2 5 , p = 0 . 6 2 5 , \eta ^ { 2 } = 0 . 0 2 ]$ . People had higher attitudes toward control than ISP violation scenarios (Figure 8a).

Intentions: Intention scores were analyzed with the same two-way ANCOVA model. Similar results (Figure 8b) to attitudes were obtained. There was a significant main effect of scenarios $[ \mathrm { F } ( 1 , 1 6 ) = 3 4 . 8 9 , p < 0 . 0 0 1 , \eta ^ { 2 } = 0 . 6 9 ]$ , but not of time $[ \mathrm { F } ( 1 , 1 6 ) = 0 . 1 7 , p = 0 . 6 8 4 , \eta ^ { 2 } = 0 . 0 1 ]$ and their interaction $[ \mathrm { F } ( 1 , 1 6 ) = 1 . 2 2 , p = 0 . 2 8 5 , \eta ^ { 2 } = 0 . 0 7 ]$ . People had higher intentions to engage in control scenarios than in ISP violation scenarios (Figure 8b). There was a significant scenarios x sex interaction $[ \mathrm { F } ( 1 , 1 6 ) = 5 . 0 1 , p = 0 . { \bar { 0 } } 4 0 , \eta ^ { 2 } =$ 0.24], which alludes to potential sex-based differences in intentions to engage differentially in ISP violations and control behaviors, independent of the stimulation. There were no general sex-based differences in intentions.

## Discussion: Experiment 4

Results regarding attitudes and intentions pointed to the same conclusion, that there are polarity-dependent effects in our case. They specifically showed that only cathodal polarity was effective, and that anodal polarity to the L DLPFC was not. This is consistent with Soltaninejad et al. (2019) but extends their findings to a different montage (they ran current from one hemisphere to another) to a broader cognitive task (namely ISP violations) and a healthy population (they focused on people with ADHD). There can be several possible explanations in our case for the inability of anodal polarity to produce effects opposite in direction to those produced by cathodal polarity. One potential account is that because the DLPFC mediates a subset of processes needed for decision-making, it is possible that anodal stimulation does not produce large enough effects to override the normal-excitability functioning of other relevant brain regions (but cathodal stimulation does). Another potential explanation is that there are ceiling effects for the endorsement of ISP violations; that is, it is feasible and easier to reduce it but more difficult or less feasible to increase it. Such explanations merit further research.

a  
![](/api/attachments/XSEKKXTG/fulltext/images/871aad1c9127f3fe453f8920a29ab5b1fea65436557f9f4a9f2db6721f1835c4.jpg)

![](/api/attachments/XSEKKXTG/fulltext/images/2b1d0824b17d996290e721113485cfabc446c314bce8213a36fe69192c729a76.jpg)  
Note: \*p <0.05; \*\*p < 0.01; \*\*\*p < 0.001; ns= non-significant. Error bars represent standard error (SE).

Figure 8. Experiment 4: Anodal L DLPFC HD-tDCS Effects on (a) Attitudes and (b) Intentions toward ISP Violations

## General Discussion

This study contributes to IS research by (1) theorizing and examining the idea that value/gain assessments cause ISP violations through informing the development of attitudes and intentions toward such acts, (2) deepening knowledge of the neural underpinnings of ISP violations with a focus on the L DLPFC, (3) examining the possibility that experimental stimulation of this region reduces the endorsement of ISP violations, and (4) exemplifying the use of NIBS in information systems research.

To achieve these contributions, we built on motivation theories, in particular expectancy theory (Vroom 1964), and neuroscience insights about value/gain assessment to suggest that (H1) the endorsement of ISP violations is mediated through a brain region that presumably processes value/gain expectations regarding the outcomes of ISP violations (e.g., completing work tasks faster and hence increasing the attainment of personal goals). We further suggest that (H2), temporarily interrupting the value/gain function in the brain, can reduce the endorsement of ISP violations, (H3) more than it reduces endorsement of less positively valenced acts (Experiments 1 and 2). H1 and H2 also imply that interrupting regions that are less functionally relevant for value/gain assessment (Experiment 3) or increasing—as opposed to decreasing—excitability of the presumed value/gain function in the brain (Experiment 4) should not produce a reduction in the endorsement of ISP violations.

Findings from four experiments support our assertions. Results show that the L DLPFC mediates ISP violations, in part, because presumed downregulation of L DLPFC activity created a significant reduction in endorsing ISP violations, compared to control (lower positive valence) behaviors (Experiment 1) and compared to people who received sham stimulation (Experiment 2). Experiment 3 further showed that these effects are unlikely to be a product of any stimulation, and that stimulation of a target region that can be theoretically linked to value/gain assessment (the L DLPFC in our case) is likely needed to produce the results observed in Experiments 1 and 2. Hence H1 is supported.

Experiments 1 and 2 results further showed that it is feasible to noninvasively modulate L DLPFC activity via cathodal HD-tDCS, such that people’s endorsement of ISP violations significantly diminishes. The main effect sizes (partial eta squared) in Experiment 2 of stimulation on attitudes and intentions were 0.16 and 0.18 respectively, both of which are large effects. Experiment 4 supplements these findings and demonstrates polar asymmetry in the stimulation of the L DLPFC; anodal stimulation did not change ISP violation endorsements, while cathodal stimulation reduced them. Altogether, these findings lend support to H2 and H3, and these results have important implications.

## Theoretical Implications

First, the findings highlight the potential importance of gain/value assessments in driving cybersecurity behaviors, assuming that the L DLPFC mediates this function of decision-making. We say potential importance, because other cognitive functions associated with the L DLPFC may also explain changes in ISP violation endorsement. The findings further distinguish value/gain judgment, which relates to what is achieved by ISP violations, from attitudes toward ISP violations, which is a holistic assessment of the act. They show (in all the studies) that people have higher attitudes toward mundane actions compared to ISP violations, yet they see higher valence in ISP violations (Appendix C). They further show that presumed interruption of value/gain brain function in the L DLPFC serves as a partial basis for reduced endorsement of ISP violations. Previous studies have lumped gains together with attitudes, but attitudes are broader. We show here that the brain circuitry underlying value/gain assessment is just one mechanism that informs the development of attitudes and intentions toward ISP violations.

In addition, previous ISP research explained that perceived benefits drive ISP violations (e.g., as explained by rational choice theory). However, prior studies used correlational surveys to make the connection, and the evidence of a causal link between the two constructs was therefore weak. In contrast, this study uses tDCS to experimentally inhibit the L DLPFC, so that the endorsement of ISP violations is reduced but less positively valenced behaviors are not. This does not perfectly establish causality because the L DLPFC is involved in many other brain functions besides valence assessments, but the evidence of a causal link is much stronger than what is suggested in previous studies.

The findings also imply that ISP violations can be conceived of as at least partially rational behaviors that are consistent with motivation theories. The underlying logic is that users expect positive gains as a function of committing these acts and they are more positively valenced (compared to mundane daily behaviors). Based on our findings, presumed interruption of the value/gain assessment function in the brain is one way to reduce the endorsement of ISP violations.

Consequently, future behavioral cybersecurity research should place a stronger emphasis on the reduction of gain perceptions related to ISP violation outcomes, in addition to maintaining its current focus on education about harms and/or developing positive attitudes toward ISP compliance (Burns et al. 2015; Yoo et al. 2018). It would be interesting for future research to consider how sanctions or fear appeals modulate gain assessments from an expectancy theory perspective, and to evaluate whether other creative ways to reduce perceived gains of outcomes of ISP violations can be effective in achieving this goal.

Second, prior findings show that the value/gain assessment function in the brain is mediated via the L DLPFC. We show here that disrupting this region results in effects that are consistent with expectancy theory (Vroom 1964), namely reduced endorsement of ISP violations. This finding is in line with recent works that illuminate the role of the L DLPFC in decision-making (Huang et al. 2017) and extends knowledge regarding the neural basis of ISP violations, a necessary step to reduce such behaviors.

The findings specifically show that ISP violations may not be just a function of self-control and harm assessments (Hu et al. 2015), but also possibly a function of value/gain assessments that are primarily mediated by the L DLPFC (He et al. 2016; Huang et al. 2017; Mengarelli et al. 2015). Future IS research should consider the role of the L DLPFC and its functionality in motivating cybersecurity (and other risky) behaviors. This focus on value/gain centers in the brain, beyond self-control centers, can help the discipline develop more comprehensive and nuanced theories of the neural underpinnings of cybersecurity behaviors; extant theories tend to focus on harm perceptions or attitudes but not on valence (Cram et al. 2019).

Third, the role of the L DLPFC in ISP violations we observed here behooves IS researchers to consider its possible value/gain assessment role in other positively valenced technology-mediated behaviors. Neuroscience studies (He et al. 2016; Steinbeis et al. 2012) and expectancy theory (Vroom 1964) imply that it is likely that the L DLPFC can mediate many IS-related behaviors and states, because they often involve value/gain assessments (Turel, 2021). Prior NeuroIS studies have typically implicated the bilateral or right DLPFC in several user cognitions and processes (see Appendix A). Without discounting the importance of the R DLPFC, the current findings suggest that the L DLPFC deserves a stronger emphasis in studies that focus on strongly positively valenced IS user behaviors (e.g., online dating, online piracy, videogaming, and online shopping) (Turel et al. 2011; Xu et al. 2012). They further suggest that such behaviors may be modulated through interventions that change their positive valence.

Finally, while the use of brain stimulation techniques has been mentioned in several NeuroIS studies (Dimoka et al. 2012; Dimoka et al. 2011; Riedl et al. 2014) and recent examples of NIBS applications in IS research have emerged (Dumont et al. 2018a; Dumont et al. 2018b), many IS phenomena, like ISP violations, could benefit from also using NIBS. Such approaches are advantageous over many NeuorIS techniques and survey studies, given their relative simplicity, safety, and ability to better support causal inferences. This study can therefore serve as a springboard for the use of such techniques in future NeuroIS research.

## Practical Implications

The detected relevance of the L DLPFC for ISP violations means that any of the cognitive functions to which this region of the brain significantly contributes could partly drive a person to breach ISP rules. Prior research has linked this region to value/gain assessment, among other important higher-order functions this region mediates; thus, it is reasonable to assume that ISP violations may be driven in part through value/gain assessments. It may therefore be possible to reduce the endorsement of such violations through behavioral interventions that target the reduction of value/gain assessments when considering ISP violations. Such interventions should be considered in future research. It is also worth considering extending and developing SETA programs that emphasize the low potential gains associated with the outcomes of ISP violations. The message could be delivered by cognitively shrinking the “carrot” associated with such actions, instead of (or in addition to) ensuring that the “stick” is clear. Another option for companies would be to take an employee-experience approach to find ways to address the needs behind these positively valanced behaviors.

Note that we advise against and refrain from prescribing NIBS for reducing endorsement of and/or actual ISP violations. Workplace brain stimulation is not yet feasible, and stimulation of the L DLPFC can affect many processes. It may also affect the value/gain assessment of anything and produce “bleed over” to other tasks that engage the L DLPFC.

## Limitations and Future Research

Several limitations of this work are noteworthy. First, tDCS effects may vary with the current amperage, electrode configuration, device used, and task employed (Huang et al. 2017). Even though our findings were established in multiple studies here, they should be strengthened with further replications before they can be generalized. Second, we focused on the L DLPFC, given its functional role in value/gain assessment. This does not discount the potential relevance of other areas of the brain for ISP violations, because many regions can mediate motivation and behavior. It is interesting to consider that the focus on reducing the expected gains of a behavior (as mediated via the L DLPFC) as opposed to increasing its perceived harms (presumably mediated via the R DLPFC) may be especially relevant in the case of ISP violations. This is assumed because people tend to mentally neutralize the potential harms of such behaviors (Siponen and Vance 2010). This may make the decision to engage in an ISP violation more dependent on the behavior’s anticipated gains, rather than on its potential harms. Future research should examine this assertion and evaluate how the interaction of the hemispheres affects decisions to violate ISPs.

Third, the DLPFC hemispheres are connected between themselves via the corpus callosum and with other regions via white matter tracts. Thus, modulating one region may trickle down to others. Future research should examine additional neural bases of cybersecurity behaviors; while we show that the L DLPFC is likely involved in such behaviors, we cannot conclude that it is the only or most important region.

Fourth, brain regions do not have one-to-one relationships with cognitive functionality. While we provide several layers of support for the idea that we likely interrupted the value/gain assessment process, this support is imperfect; it is possible that we interrupted additional functionalities, and/or that we interrupted only one of several regions that mediates value/gain assessments. Direct tests would be required in future research. We also assumed that we interrupted the valence component in the expectancy theory account of ISP violations but cannot rule out interruption of other expectancy theory components, or factors in other theoretical accounts of motivated ISP violations. This is a common limitation when studying complex processes because stimulated brain regions do not account for a single process. Hence, caution should be exercised when interpreting our results.

Fifth, our theoretical account explains all positively valenced behaviors, of which ISP violations are just one example. Testing the model in other IS contexts (e.g., online purchasing decisions) would be an important future extension of our work. In addition, there is an ongoing debate about whether ISP violations are at the other extreme of compliance or a standalone phenomenon. Recent evidence suggests that they can be distinct (See Cram et al. 2019). Since it is possible that compliance is also positively valenced, modulating the value/gain assessment can influence both and be counterproductive. ISP violations differ from compliance behaviors in that they are more “active, deliberate, and premeditated” (Cram et al. 2019, p.528) and should therefore be more affected by value/gain assessment disruption. We tested the valence of both and found that ISP violations are more positively valenced (See Appendix D). We nevertheless call for future research to examine the effect of tDCS on ISP compliance as another instance of positively valenced behavior.

Finally, an inherent limitation of tDCS techniques is their low spatial resolution (Dumont et al. 2018a). Even though we used HD-tDCS, we cannot rule out the possibility that our stimulation reached neighboring regions (orbifrontal/ ventromedial cortex). Future research that combines tDCS with neuroimaging techniques could shed light on this possibility.

## Conclusion

This study extends the understanding of the neural basis of cybersecurity behaviors from a motivation theory perspective. It further demonstrates the feasibility of noninvasive brain stimulation to change users’ endorsement of IS-related and technology-mediated behaviors. The findings show that ISP violations likely depend, in part, on motivational value/gain assessment processes that are mediated by the L DLPFC. We call for research to further examine the neural underpinnings of ISP violations, the role of the L DLPFC in a broader range of IS use behaviors, and the possibility of using noninvasive brain stimulation techniques for studying IS use behaviors.

## Acknowledgments and Grants

We would like to thank Ms. Youqing Peng and Ms. Chenyu Lv from Southwest University for their help in collecting the data. This work was supported by research grants from the National Natural Science Foundation of China (31972906), the Natural Science Foundation of Chongqing (cstc2020jcyj-msxmX0215) and the High-End Foreign Expert Introduction Program (G20190022029).

## References

Ahn, H. M., Kim, S. E., and Kim, S. H. 2013. “The Effects of High-Frequency Rtms over the Left Dorsolateral Prefrontal Cortex on Reward Responsiveness,” Brain Stimulation (6:3), pp. 310- 314.

Ajzen, I. 1985. “From Intentions to Actions: A Theory of Planned Behavior,” in Action Control, Springer, pp. 11-39.

Allaert, J., Sanchez-Lopez, A., De Raedt, R., Baeken, C., and Vanderhasselt, M.-A. 2019. “Inverse Effects of tDCS over the Left versus Right DLPC on Emotional Processing: A Pupillometry Study,” PLOS ONE (14:6), Article e0218327.

Antal, A., Kincses, T. Z., Nitsche, M. A., and Paulus, W. 2003. “Manipulation of Phosphene Thresholds by Transcranial Direct Current Stimulation in Man,” Experimental Brain Research (150:3), pp. 375-378.

Barlow, J. B., Warkentin, M., Ormond, D., and Dennis, A. 2018. “Don’t Even Think About It! The Effects of Antineutralization, Informational, and Normative Communication on Information Security Compliance,” Journal of the Association for Information Systems (19:8), pp. 689-715.

Barraclough, D. J., Conroy, M. L., and Lee, D. 2004. “Prefrontal Cortex and Decision Making in a Mixed-Strategy Game,” Nature Neuroscience (7:4), pp. 404-410.

Baumgartner, T., Knoch, D., Hotz, P., Eisenegger, C., and Fehr, E. 2011. “Dorsolateral and Ventromedial Prefrontal Cortex Orchestrate Normative Choice,” Nature Neuroscience (14:11), pp. 1468-U1149.

Becker, G. S. 1968. “Crime and Punishment: An Economic Approach,” in The Economic Dimensions of Crime, N. G. Fielding, A. Clarke, and R. Witt, Springer, pp. 13-68.

Boggio, P. S., Zaghi, S., Villani, A. B., Fecteau, S., Pascual-Leone, A., and Fregni, F. 2010. “Modulation of Risk-Taking in Marijuana Users by Transcranial Direct Current Stimulation (tDCS) of the Dorsolateral Prefrontal Cortex (Dlpfc),” Drug and Alcohol Dependence (112:3), pp. 220-225.

Bolles, R. C. 1967. Theory of Motivation, Harper & Row.

Brunoni, A. R., Amadera, J., Berbel, B., Volz, M.S., Rizzerio, B.G., and Fregni, F. 2011. “A Systematic Review on Reporting and Assessment of Adverse Effects Associated with Transcranial Direct Current Stimulation,” International Journal of Neuropsychopharmacology (14:8), pp. 1133-1145.

Bulgurcu, B., Cavusoglu, H., and Benbasat, I. 2010. “Information Security Policy Compliance: An Empirical Study on Rationality-Based Beliefs and Information Security Awareness,” MIS Quarterly (34:3), pp. 523-548.

Burns, A. J., Roberts, T. L., Posey, C., Bennett, R. J., and Courtney, J. F. 2015. “Assessing the Role of Security Education, Training, and Awareness on Insiders’ Security-Related Behavior: An Expectancy Theory Approach,” in Proceedings of the 48th Hawaii International Conference on System Sciences, pp. 3930-3940.

Carver, C. S., and Scheier, M. F. 1982. “Control Theory: A Useful Conceptual Framework for Personality-Social, Clinical, and Health Psychology,” Psychological Bulletin (92:1), p. 111-135.

Chen, W., Chen, R., and He, Q. 2019a. “Stimulation Location Determination Using a 3D Digitizer with High-Definition Transcranial Direct Current Stimulation,” JoVE (154), Article e60263.

Chen, W., Zhang, S., Turel, O., Peng, Y., Chen, H., and He, Q. 2019b. “Sex-Based Differences in Right Dorsolateral Prefrontal Cortex Roles in Fairness Norm Compliance,” Behavioural Brain Research (361), pp. 104-112.

Cram, A., D’Arcy, J., and Proudfoot, J. 2019. “Seeing the Forest and the Trees: A Meta-Analysis of the Antecedents of Information Security Policy Compliance,” MIS Quarterly (43:2), pp. 525-554.

Cram, W. A., Proudfoot, J.G., and D’Arcy, J. 2017. “Organizational Information Security Policies: A Review and Research Framework,” European Journal of Information Systems (26:6), pp. 605-641.

Damasio, A. R. 1994. Descartes’ Error: Emotion, Reason, and the Human Brain, Putnam Publishing.

Davidson, R. J. 2004. “What Does the Prefrontal Cortex ‘Do’ in Affect: Perspectives on Frontal Eeg Asymmetry Research,” Biological Psychology (67:1-2), pp. 219-233.

Deci, E. L. 1975. Intrinsic Motivation, Plenum.

Deci, E. L., and Ryan, R.M. 1985. Intrinsic Motivation and Self-Determination in Human Behavior, Springer.

Dimoka, A., Banker, R. D., Benbasat, I., Davis, F. D., Dennis, A. R., Gefen, D., Gupta, A., Lschebeck, A., Kenning, P. H., Pavlou, P. A., Mueller-Putz, G., Riedl, R., vom Brocke, J., and Weber, B. 2012. “On the Neurophysiological Tools in IS Rsearch: Developing a Research Agenda for NeuroIS,” MIS Quarterly (36:3), pp. 679-702.

Dimoka, A., Pavlou, P. A., and Davis, F. D. 2011. “NeuroIS: The Potential of Cognitive Neuroscience for Information Systems Research,” Information Systems Research (22:4), pp. 687-702.

Dumont, L., El Mouderrib, S., Théoret, H., Sénécal, S., and Léger, P.-M. 2018a. “Non-Invasive Brain Stimulation as a Set of Research Tools in NeuroIS: Opportunities and Methodological Considerations,” Communications of the Association for Information Systems (43), pp. 78-100.

Dumont, L., Larochelle-Brunet, F., Théoret, H., Riedl, R., Sénécal, S., and Léger, P.-M. 2018b. “Non-Invasive Brain Stimulation

in Information Systems Research: A Proof-of-Concept Study,” PLOS ONE (13:7), Article e0201128.

Eling, M., and Wirfs, J. 2019. “What Are the Actual Costs of Cyber Risk Events?,” European Journal of Operational Research (272:3), pp. 1109-1119.

Ernst, M., Nelson, E. E., McClure, E. B., Monk, C. S., Munson, S., Eshel, N., Zarahn, E., Leibenluft, E., Zametkin, A., and Towbin, K. 2004. “Choice Selection and Reward Anticipation: An fMRI Study,” Neuropsychologia (42:12), pp. 1585-1597.

Faber, H., Opitz, A., Müller-Dahlhaus, F., and Ziemann, U. 2017. “Polarity-Independent Effects of tDCS on Paired Associative Stimulation-Induced Plasticity,” Brain Stimulation (10:6), pp. 1061-1069.

Faul, F., Erdfelder, E., Buchner, A., and Lang, A.-G. 2009. “Statistical Power Analyses Using G\* Power 3.1: Tests for Correlation and Regression Analyses,” Behavior Research Methods (41:4), pp. 1149-1160.

First, M. B., Gibbon, M., Williams, J. B. W., and Spitzer, R. L. 2001. Structured Clinical Interview for DSM-IV: SCID Screen Patient Questionnaire (SSPQ) [Axis I] & SCID Screen Patient Questionnaire-Extended (SSPQ-X), Multi-Health Systems Inc.

Guo, K. H., Yuan, Y., Archer, N. P., and Connelly, C. E. 2011. “Understanding Nonmalicious Security Violations in the Workplace: A Composite Behavior Model,” Journal of Management Information Systems (28:2), pp. 203-236.

Hare, T. A., Camerer, C. F., and Rangel, A. 2009. “Self-Control in Decision-Making Involves Modulation of the VMPFC Valuation System,” Science (324:5927), pp. 646-648.

Hayashi, T., Ko, J. H., Strafella, A. P., and Dagher, A. 2013. “Dorsolateral Prefrontal and Orbitofrontal Cortex Interactions During Self-Control of Cigarette Craving,” in Proceedings of the National Academy of Sciences of the United States of America (110:11), pp. 4422-4427.

He, Q., Chen, M., Chen, C., Xue, G., Feng, T., and Bechara, A. 2016. “Anodal Stimulation of the Left DLPFC Increases IGT Scores and Decreases Delay Discounting Rate in Healthy Males,” Frontiers in Psychology (7), Article 1421.

Heekeren, H. R., Marrett, S., Ruff, D. A., Bandettini, P. A., and Ungerleider, L.G. 2006. “Involvement of Human Left Dorsolateral Prefrontal Cortex in Perceptual Decision Making Is Independent of Response Modality,” in Proceedings of the National Academy of Sciences of the United States of America (103:26), pp. 10023-10028.

Heller, W., and Nitschke, J. B. 1998. “The Puzzle of Regional Brain Activity in Depression and Anxiety: The Importance of Subtypes and Comorbidity,” Cognition & Emotion (12:3), pp. 421-447.

Herwig, U., Satrapi, P., and Schönfeldt-Lecuona, C. 2003. “Using the International 10-20 Eeg System for Positioning of Transcranial Magnetic Stimulation,” Brain Topography (16:2), pp. 95-99.

Hogeveen, J., Grafman, J., Aboseria, M., David, A., Bikson, M., and Hauner, K. 2016. “Effects of High-Definition and Conventional tDCS on Response Inhibition,” Brain Stimulation (9:5), pp. 720-729.

Hu, Q., West, R., and Smarandescu, L. 2015. “The Role of Self-Control in Information Security Violations: Insights from a Cognitive Neuroscience Perspective,” Journal of Management Information Systems (31:4), pp. 6-48.

Hu, Q., Xu, Z., Dinev, T., and Ling, H. 2011. “Does Deterrence Work in Reducing Information Security Policy Abuse by Employees?,” Communications of the ACM (54:6), pp. 54-60.

Huang, D. Q., Chen, S., Wang, S. Q., Shi, J. C., Ye, H., Luo, J., and Zheng, H. L. 2017. “Activation of the DLPFC Reveals an Asymmetric Effect in Risky Decision Making: Evidence from a tDCS Study,” Frontiers in Psychology (8), Article 38.

Joseph, R. 1992. The Right Brain and the Unconscious: Discovering the Stranger Within, Plenum.

Kahneman, D., and Tversky, A. 1979. “Prospect Theory: An Analysis of Decision under Risk,” Econometrica (47:2), pp. 263-291.

Katz, D. 1960. “The Functional Approach to the Study of Attitudes,” Public Opinion Quarterly (24:1), pp. 163-204.

Keshvari, F., Pouretemad, H.R., and Ekhtiari, H. 2013. “The Polarity-Dependent Effects of the Bilateral Brain Stimulation on Working Memory,” Basic Clinical Neuroscience (4:3), pp. 224-231.

Knoch, D., Gianotti, L. R. R., Pascual-Leone, A., Treyer, V., Regard, M., Hohmann, M., and Brugger, P. 2006. “Disruption of Right Prefrontal Cortex by Low-Frequency Repetitive Transcranial Magnetic Stimulation Induces Risk-Taking Behavior,” Journal of Neuroscience (26:24), pp. 6469-6472.

Knotkova, H., Nitsche, M. A., Bikson, M., and Woods, A. J. 2019. Practical Guide to Transcranial Direct Current Stimulation: Principles, Procedures and Applications, Springer.

Krain, A. L., Wilson, A. M., Arbuckle, R., Castellanos, F. X., and Milham, M. P. 2006. “Distinct Neural Mechanisms of Risk and Ambiguity: A Meta-Analysis of Decision-Making,” Neuroimage (32:1), pp. 477-484.

Krawczyk, D. C. 2002. “Contributions of the Prefrontal Cortex to the Neural Basis of Human Decision Making,” Neuroscience & Biobehavioral Reviews (26:6), pp. 631-664.

Kuo, H.-I., Bikson, M., Datta, A., Minhas, P., Paulus, W., Kuo, M.- F., and Nitsche, M. A. 2013. “Comparing Cortical Plasticity Induced by Conventional and High-Definition 4× 1 Ring tDCS: A Neurophysiological Study,” Brain Stimulation (6:4), pp. 644-648.

Kuo, M.-F., Paulus, W., and Nitsche, M. A. 2014. “Therapeutic Effects of Non-Invasive Brain Stimulation with Direct Currents (tDCS) in Neuropsychiatric Diseases,” NeuroImage (85), pp. 948-960.

Lawler, E. E., and Suttle, J. L. 1973. “Expectancy Theory and Job Behavior,” Organizational Behavior and Human Performance (9:3), pp. 482-503.

Li, H., Zhang, J., and Sarathy, R. 2010. “Understanding Compliance with Internet Use Policy from the Perspective of Rational Choice Theory,” Decision Support Systems (48:4), pp. 635-645.

Liang, H., and Xue, Y. 2009. “Avoidance of Information Technology Threats: A Theoretical Perspective,” MIS Quarterly), pp. 71-90.

Liang, H., and Xue, Y. 2010. “Understanding Security Behaviors in Personal Computer Usage: A Threat Avoidance Perspective,” Journal of the Association for Information Systems (11:7), pp. 394-413.

Maslow, A. H. 1943. “A Theory of Human Motivation,” Psychological Review (50:4), pp. 370-396.

McClelland, D. C. 1987. Human Motivation, CUP Archive.

McClure, S.M., Ericson, K.M., Laibson, D.I., Loewenstein, G., and Cohen, J.D. 2007. “Time Discounting for Primary Rewards,” Journal of Neuroscience (27:21), pp. 5796-5804.

Mengarelli, F., Spoglianti, S., Avenanti, A., and di Pellegrino, G. 2015. “Cathodal tDCS over the Left Prefrontal Cortex Diminishes Choice-Induced Preference Change,” Cerebral Cortex (25:5), pp. 1219-1227.

Nejati, V., Salehinejad, M. A., and Nitsche, M. A. 2018. “Interaction of the Left Dorsolateral Prefrontal Cortex (L-DLPFC) and Right Orbitofrontal Cortex (OFC) in Hot and Cold Executive Functions: Evidence from Transcranial Direct Current Stimulation (tDCS),” Neuroscience (369), pp. 109- 123.

Nitsche, M., and Paulus, W. 2000. “Excitability Changes Induced in the Human Motor Cortex by Weak Transcranial Direct Current Stimulation,” The Journal of Physiology (527:3), pp. 633-639.

Ormond, D., Warkentin, M., and Crossler, R. E. 2019. “Integrating Cognition with an Affective Lens to Better Understand Information Security Policy Compliance,” Journal of the Association for Information Systems (20:12), pp. 1794-1843.

Petty, R. E., and Cacioppo, J. T. 1986. “The Elaboration Likelihood Model of Persuasion,” in Communication and Persuasion, Springer, pp. 1-24.

Philiastides, M. G., Auksztulewicz, R., Heekeren, H. R., and Blankenburg, F. 2011. “Causal Role of Dorsolateral Prefrontal Cortex in Human Perceptual Decision Making,” Current Biology (21:11), pp. 980-983.

Rahman, A., Reato, D., Arlotti, M., Gasca, F., Datta, A., Parra, L. C., and Bikson, M. 2013. “Cellular Effects of Acute Direct Current Stimulation: Somatic and Synaptic Terminal Effects,” The Journal of Physiology (591:10), pp. 2563-2578.

Riedl, R., Davis, F. D., and Hevner, A. R. 2014. “Towards a NeuroIS Research Methodology: Intensifying the Discussion on Methods, Tools, and Measurement,” Journal of the Association for Information Systems (15:10), pp. i-xxxv.

Siponen, M., and Vance, A. 2010. “Neutralization: New Insights into the Problem of Employee Information Systems Security Policy Violations,” MIS Quarterly (34:3), pp. 487-502.

Sobotka, S. S., Davidson, R. J., and Senulis, J. A. 1992. “Anterior Brain Electrical Asymmetries in Response to Reward and Punishment,” Electroencephalography and Clinical Neurophysiology (83:4), pp. 236-247.

Sokol-Hessner, P., Hutcherson, C., Hare, T., and Rangel, A. 2012. “Decision Value Computation in DLPFC and VMPFC Adjusts to the Available Decision Time,” European Journal of Neuroscience (35:7), pp. 1065-1074.

Soltaninejad, Z., Nejati, V., and Ekhtiari, H. 2019. “Effect of Anodal and Cathodal Transcranial Direct Current Stimulation on DLPFC on Modulation of Inhibitory Control in ADHD,” Journal of Attention Disorders (23:4), pp. 325-332.

Steel, P., and König, C. J. 2006. “Integrating Theories of Motivation,” Academy of Management Review (31:4), pp. 889- 913.

Steinbeis, N., Bernhardt, B. C., and Singer, T. 2012. “Impulse Control and Underlying Functions of the Left DLPFC Mediate Age-Related and Age-Independent Individual Differences in Strategic Social Behavior,” Neuron (73:5), pp. 1040-1051.

Steinbeis, N., Haushofer, J., Fehr, E., and Singer, T. 2016. “Development of Behavioral Control and Associated VMPFC–

DLPFC Connectivity Explains Children’s Increased Resistance to Temptation in Intertemporal Choice,” Cerebral Cortex (26:1), pp. 32-42.

Sutton, S. K., and Davidson, R. J. 1997. “Prefrontal Brain Asymmetry: A Biological Substrate of the Behavioral Approach and Inhibition Systems,” Psychological Science (8:3), pp. 204-210.

Tazoe, T., Endoh, T., Kitamura, T., and Ogata, T. 2014. “Polarity Specific Effects of Transcranial Direct Current Stimulation on Interhemispheric Inhibition,” PLOS ONE (9:12), Article e114244.

Turel, O., Serenko, A., and Giles, P. 2011. “Integrating Technology Addiction and Use: An Empirical Investigation of Online Auction Users, ” MIS Quarterly (35:4), pp. 1043-1062.

Turel, O. 2021. “Technology-Mediated Dangerous Behaviors as Foraging for Social-Hedonic Rewards: The Role of Implied Inequality,” MIS Quarterly (45:3), pp. 1249-1286.

Turel, O., and Bechara, A. 2021. “A Triple-System Neural Model of Maladaptive Consumption,” Journal of the Association for Consumer Research (6:3), pp. 324-333.

Valentin, V. V. 2005. Foundations for a Neurobiologically Plausible Model of Decision Making, University of California Press.

Vance, A., and Siponen, M. 2012. “Is Security Policy Violations: A Rational Choice Perspective,” Journal of Organizational and End User Computing (24:1), pp. 21-41.

Verplanken, B., and Holland, R.W. 2002. “Motivated Decision Making: Effects of Activation and Self-Centrality of Values on Choices and Behavior,” Journal of Personality and Social Psychology (82:3), p. 434-447.

Villamar, M. F., Volz, M. S., Bikson, M., Datta, A., DaSilva, A. F., and Fregni, F. 2013. “Technique and Considerations in the Use of 4x1 Ring High-Definition Transcranial Direct Current Stimulation (HD- tDCS),” Journal of Visualized Experiments (77), Article e50309).

Vroom, V. H. 1964. Work and Motivation, Wiley.

Wallis, J. D., and Miller, E.K. 2003. “Neuronal Activity in Primate Dorsolateral and Orbital Prefrontal Cortex During Performance of a Reward Preference Task,” European Journal of Neuroscience (18:7), pp. 2069-2081.

Wen, Y. T., Turel, O., Peng, Y. Q., Lv, C. Y., and He, Q. H. 2019. “Cathodal Stimulating the Left DLPFC Changes Risk Disposition toward Common Risky Behaviors in Daily-Life,” Neuroscience Letters (709), Article 134400.

Wiener, N. 1948. Cybernetics or Control and Communication in the Animal and the Machine, Technology Press.

Willison, R., and Warkentin, M. 2013. “Beyond Deterrence: An Expanded View of Employee Computer Abuse,” MIS Quarterly (37:1), pp. 1-20

Xu, Z., Turel, O., and Yuan, Y. 2012. “Online Game Addiction among Adolescents: Motivation and Prevention Factors,” European Journal of Information Systems (21:3), pp. 321-340.

Ye, H., Chen, S., Huang, D. Q., Wang, S. Q., Jia, Y. M., and Luo, J. 2015. “Transcranial Direct Current Stimulation over Prefrontal Cortex Diminishes Degree of Risk Aversion,” Neuroscience Letters (598), pp. 18-22.

Yoo, C. W., Sanders, G. L., and Cerveny, R. P. 2018. “Exploring the Influence of Flow and Psychological Ownership on Security Education, Training and Awareness Effectiveness and

Security Compliance,” Decision Support Systems (108), pp. 107-118.

Zhang, Y.-Y., Xu, L., Rao, L.-L., Zhou, L., Zhou, Y., Jiang, T., Li, S., and Liang, Z.-Y. 2016. “Gain-Loss Asymmetry in Neural Correlates of Temporal Discounting: An Approach-Avoidance Motivation Perspective,” Scientific Reports (6:1), pp. 1-10.

Zhao, H. C., Qiao, L., Fan, D.Q., Zhang, S. Y., Turel, O., Li, Y. H., Li, J., Xue, G., Chen, A. T., and He, Q. H. 2017. “Modulation of Brain Activity with Noninvasive Transcranial Direct Current Stimulation (tDCS): Clinical Applications and Safety Concerns,” Frontiers in Psychology (8), Article 685.

## About the Authors

Ofir Turel (corresponding author) a professor of information systems management within the School of Computing and Information Systems at The University of Melbourne. and a scholar in residence in the Decision Neuroscience Program, Department of Psychology, University of Southern California. His research interests include a broad range of behavioral, biophysiological, and managerial issues related to information systems and technologies. He has published over 160 journal papers in information systems, business, psychology, and psychiatry journals. His research has been featured in numerous media outlets, including TV, radio, podcasts. and newspapers. Examples include the Wall Street Journal, Washington Post, CBC, C|net Times Higher Education, The Rolling Stone, and PBS.

Qinghua He (corresponding author) is a professor of psychology at the Faculty of Psychology, Southwest University, China. He is also a member of the Chongqing Collaborative Innovation Center for Brain Science, member of the Southwest University Branch, Collaborative Innovation Center of Assessment toward Basic Education Quality at Beijing Normal University, Chongqing, China, and a member of the Institute of Psychology, Key Laboratory of Mental Health, Chinese Academy of Sciences, Beijing, China. His main research interests include the neural basis of decision-making and its application to addiction prevention. He has published over 80 journal papers in neuroscience, psychology, and psychiatry journals. He was designated as a Chongqing Talent in 2019.

Yatong Wen is a Ph.D. candidate at the Institute of Psychology, Chinese Academy of Sciences. She is also affiliated with the Faculty of Psychology, MOE Key Laboratory of Cognition and Personality, Southwest University, Chongqing, China. Her main research interests are the neural basis of risky decisions and addiction.

## Appendix A

## Key Studies

## NeuroIS studies on Dorsolateral Prefrontal Cortex (DLPFC)

The importance of the DLPFC as a target region has been demonstrated in NeuroIS research. For example, Dimoka et al. (2011) suggested that perceived ease of use is mapped onto the DLPFC, given that activation of DLPFC is associated with working memory, cognitive effort, and problem solving. DLPFC activation has also been linked to both trust and distrust assessments (Riedl et al. 2010) and to the cognitive information processing of online seller profiles (Dimoka 2010). It has also been suggested that DLPFC activation is a marker for cognitive overload in system use (Dimoka et al. 2012). Moreover, videogame engagement has been linked to the density of theta oscillations in the L DLPFC, given its role in information encoding and declarative and episodic memory processes (Li et al. 2014). Similarly, cognitive performance and supporting information processing were associated with L DLPFC activation in virtual teams (Minas et al. 2014).

Note that many NeuroIS studies have focused on the bilateral DLPFC as a unit, which prevents a more nuanced understanding of the possible role of each hemisphere in ISP violation. Exceptions that took a more unilateral view of the DLPFC include Minas et al. (2014) that showed differential roles of left and right hemisphere activity based on the nature of the information processed (obvious/ supportive vs. new/challenging); and Hu et al. (2015) that focused on the right hemisphere as a brain center that mediates self-control. Hu et al. (2015) showed that activity in both prefrontal cortex hemispheres (including the DLPFC), but especially in the right hemisphere, was associated with self-control abilities and endorsement of ISP violations. Thus, focusing on the left DLPFC is not only aligned with the expectancy theory account of ISP violations according to which ISP violations are partly expected-gain driven, but also allows for the advancement of the IS field through the investigation of the role of a relatively unexplored brain region in user behaviors.

## Key Studies of tDCS of DLPFC

<table><tr><td colspan="5">Table A1. Specific Studies</td></tr><tr><td>Study</td><td>Sample</td><td>Task/outcome</td><td>tDCS stimulation</td><td>Results</td></tr><tr><td>(Fregni et al. 2005)</td><td>15 healthy subjects (4 men)</td><td>Sequential-letter working memory task</td><td>1. Anodal left2. Cathodal left3. Sham</td><td>Only anodal stimulation of the left increased working memory task performance. Left DLPFC is involved in working memory.</td></tr><tr><td>(Fecteau et al. 2007a)</td><td>36 healthy college students (11 men)</td><td>Gambling task</td><td>1. Concurrent anodal tDCS of right and cathodal of left2. Concurrent anodal of left and cathodal of right3. Sham</td><td>Right anodal/left cathodal stimulation increased safe choices and earned points compared to other groups; they also chose faster.Right anodal/left cathodal were insensitive to reward magnitude. They were highly risk-averse and likely did not seriously consider risky prospects.</td></tr><tr><td>(Fecteau et al. 2007b)</td><td>35 healthy college students (9 men)</td><td>Balloon Analog Risk Task</td><td>1. Concurrent anodal tDCS of right and cathodal of left2. Concurrent anodal of left and cathodal of right3. Sham4. Anodal to left or right; separately for each hemisphere</td><td>Both types of bilateral tDCS strategies led to more risk-averse responses compared to sham.Stimulations of the separate hemispheres did not produce significant behavior changes.</td></tr><tr><td>(Boggio et al. 2008)</td><td>13 healthy subjects (11 men)</td><td>Alcohol craving</td><td>1. Concurrent anodal tDCS of right and cathodal of left2. Concurrent anodal of left and cathodal of right3. Sham</td><td>Both types of bilateral tDCS strategies led to decreased cravings</td></tr><tr><td>(Wolkenstein et al. 2014)</td><td>28 healthy subjects</td><td>delayed response working memory (DWM) task and an arithmetic inhibition task (AIT)</td><td>1. Cathodal left2. Sham</td><td>Cathodal tDCS induced cognitive control deficits in the form of negativity bias (reduced response accuracy and increased response latency) when facing negative cues. Down-sensitizing the left DLPFC causes cognitive control issues only when faced with negative materials.</td></tr><tr><td>(Pripfl and Lamm 2015)</td><td>20 smokers</td><td>Affective and nicotine-cue picture appraisals</td><td>3. Anodal left4. Anodal right5. Sham</td><td>Anodal right tDCS reduced negative emotions but did not change positive emotions or nicotine craving cure appraisals. Anodal left tDCS did not produce positive effects.</td></tr><tr><td>(Heeren et al. 2015)</td><td>56 highly trait-anxious women</td><td>Attentional bias for threat (measured by reaction times and eye-movements)</td><td>1. Attention Bias Modification (ABM) procedures +anodal tDCS to left2. ABM+ Cathodal tDCS to left3. ABM+ Sham</td><td>ABM+ anodal tDCS to left reduces gaze time on the threat, but did not change response time. Left DLPFC is involved in threat assessment and maintenance through gaze.</td></tr><tr><td>(Ye et al. 2015a)</td><td>60 healthy college students (24 men)</td><td>Gambling (pairs of lottery choices)</td><td>1. Anodal left/ cathodal right2. Cathodal left/ anodal right3. Sham</td><td>Sham produced risk reduction (“wealth effect”). No effect of stimulations, which is indicative that both promote risk reduction that counterbalances the “wealth effect.”</td></tr><tr><td>(Ye et al. 2015b)</td><td>60 healthy college students (25 men)</td><td>Gambling (risk matrix)</td><td>1. Anodal left2. Anodal right3. Sham</td><td>Right anodal/left cathodal tDCS decreased risk aversion in the gain frame and increased risk aversion in the loss frame.</td></tr><tr><td>(Mengarelli et al. 2015)</td><td>48 healthy subjects (20 men)</td><td>Free-choice paradigm</td><td>1. Cathodal left2. Cathodal right3. Sham</td><td>Cathodal tDCS over the left, but not over the right, DLPFC caused a reduction of the typical behavior-induced preference change relative to sham stimulation. Left DLPFC is involved in dissonance reduction through rationalization.</td></tr><tr><td>(Luft et al. 2017)</td><td>60 healthy subjects (13 men)</td><td>Matchstick arithmetic problems</td><td>1. Anodal left2. Cathodal left3. Sham</td><td>Cathodal tDCS to the left significantly increased the likelihood of solving problems that require relaxation of previously learned constraints.</td></tr><tr><td>(Huang et al. 2017)</td><td>150 healthy college students (68 men)</td><td>Gambling (risk matrix)</td><td>1. Anodal left2. Anodal right3. Sham</td><td>Left anodal tDCS led to risk aversion in the gain frame.Right cathodal tDCS led to risk seeking in the loss frame.Point to differential roles of left (gain assessment) and right (punishment/self-control) hemispheres in risky decisions.</td></tr></table>

Note: rTMS = repeated transcranial magnetic stimulation; tDCS = transcranial direct current stimulation; HD-tDCS = high definition transcranial direct current stimulation; DLPFC = dorsolateral prefrontal cortex

## List of Review Studies on tDCS Effects

Berryhill, M. E., Peterson, D. J., Jones, K. T., and Stephens, J. A. 2014. “Hits and Misses: Leveraging tDCS to Advance Cognitive Research,” Frontiers in Psychology (5), Article 800.

Brunoni, A. R., and Vanderhasselt, M.-A. 2014. “Working Memory Improvement with Non-Invasive Brain Stimulation of the Dorsolateral Pre-Frontal Cortex: A Systematic Review and Meta-Analysis,” Brain Cognition, (86), pp. 1-9.

Dedoncker, J., Brunoni, A.R., Baeken, C., and Vanderhasselt, M.-A. 2016. “A Systematic Review and Meta-Analysis of the Effects of Transcranial Direct Current Stimulation (tDCS) over the Dorsolateral Prefrontal Cortex in Healthy and Neuropsychiatric Samples: Influence of Stimulation Parameters,” Brain Stimulation (9:4), pp. 501-517.

Hill, A. T., Fitzgerald, P. B., and Hoy, K. E. 2016. “Effects of Anodal Transcranial Direct Current Stimulation on Working Memory: A Systematic Review and Meta-Analysis of Findings from Healthy and Neuropsychiatric Populations,” Brain Stimulation, 9(2), 197-208.

Horvath, J. C., Forte, J. D., and Carter, O. 2015. “Evidence that Transcranial Direct Current Stimulation (tDCS) Generates Little-to-no Reliable Neurophysiologic Effect beyond MEP Amplitude Modulation in Healthy Human Subjects: A Systematic Review,” Neuropsychologia (66), 213-236.

Horvath, J. C., Forte, J. D., and Carter, O. 2015. Quantitative Review Finds no Evidence of Cognitive Effects in Healthy Populations from Single-Session Transcranial Direct Current Stimulation (tDCS). Brain Stimulation, 8(3), 535-550.

Imburgio, M. J., and Orr, J. M. (2018). “Effects of Prefrontal tDCS on Executive Function: Methodological Considerations Revealed by Meta-Analysis,” Neuropsychologia (117), 156-166.

Jacobson, L., Koslowsky, M., and Lavidor, M. 2012. “TDCS Polarity Effects in Motor and Cognitive Domains: A Meta-Analytical Review,” Experimental Brain Research (216:1), 1-10.

Mancuso, L. E., Ilieva, I. P., Hamilton, R. H., and Farah, M. J. 2016. “Does Transcranial Direct Current Stimulation Improve Healthy Working Memory? A Meta-Analytic Review,” Journal of Cognitive Neuroscience, 28(8), 1063-1089.

Medina, J., and Cason, S. 2017. “No Evidential Value in Samples of Transcranial Direct Current Stimulation (tDCS) Studies of Cognition and Working Memory in Healthy Populations,” Cortex (94), pp. 131-141.

Mervis, J. E., Capizzi, R. J., Boroda, E., and MacDonald, A. W. 2017, “Transcranial Direct Current Stimulation over the Dorsolateral Prefrontal Cortex in Schizophrenia: A Quantitative Review of Cognitive Outcomes,” Frontiers in Human Neuroscience (11:4), Article 44.

Nilsson, J., Lebedev, A. V, Rydström, A., and Lövdén, M. 2017. “Direct-Current Stimulation Does Little to Improve the Outcome of Working Memory Training in Older Adults,” Psychological Science (28:7), pp. 907-920.

Price, A. R., and Hamilton, R. H. 2015. “A Re-Evaluation of the Cognitive Effects from Single-Session Transcranial Direct Current Stimulation,” Brain Stimulation (8:3), Article 663665.

Summers, J. J., Kang, N., and Cauraugh, J. H. 2016. “Does Transcranial Direct Current Stimulation Enhance Cognitive and Motor Functions in the Ageing Brain? A Systematic Review and Meta-Analysis,” Ageing Research Reviews (25), pp. 42–54.

Tremblay, S., Lepage, J. F., Latulipe-Loiselle, A., Fregni, F., Pascual-Leone, A., and Théoret, H. 2014, “The Uncertain Outcome of Prefrontal tDCS,” Brain Stimulation (7:6), pp. 773-783.

## Appendix B

## tDCS Experiment Scenarios

## Scenario Development

Experiment 1’s control scenarios were based on interviews with five students (three females). Experiment 2’s scenarios were based on interviews with 10 students (five females). They helped to identify decisions that produce outcomes with positive but low immediate gains (i.e., have relatively low positive valence) and that are common in students’ lives. The same panel that assisted with control scenarios for Experiment 1 helped to select the most realistic ISP violation scenarios from Guo et al. (2011) and Hu et al. (2015) and contextualize them to the university in which this study was conducted. Hence, the selected ISP violation scenarios reflected reasonably realistic ISP violations in the examined university settings. The resultant 16 scenarios for Experiment 1 and the additional eight for Experiment 2 were translated into Chinese using a forward-backward translation process. The resultant pool of scenarios for Experiment 1 was evaluated via interviews with another panel of 10 students (5 females). Additional interviews with ten different students (four females) were employed for assessing Experiment 2 scenarios. Their feedback indicated that the scenarios’ realism and understandability were high and that the expected low and high positive valence of the outcomes of control and ISP violation scenarios was realistic.

## Study Materials

## Instructions

Xiaoming is an undergraduate student at this university. The university has explicit and strict data management and access policies. These policies forbid any unauthorized access, copy, transfer, or use of its confidential or nonconfidential data, password sharing, and other unsafe IS security behaviors. Xiaoming has been taking 20 courses this semester, and each course has many requirements and projects to complete, with strict deadlines. Therefore, Xiaoming is under tremendous time pressure; Xiaoming’s academic performance is at risk. Xiaoming may not graduate on time if not doing well in all of the courses. In the following scenarios, imagine that you are Xiaoming

## Control Scenarios: Study 1

1. Xiaoming receives an email from the university that the ministry of education is holding a meeting next weekend seeking inputs from students regarding their program of education at the university. Xiaoming’s parents always taught him that it is good to express opinions and help improve the future of others. Wanting to express an opinion and listen to others’ opinions, Xiaoming decided to attend.

2. Xiaoming receives an email from a friend that there is a big one-day sale of computers at JD.com, with major discounts. Xiaoming’s friends believe that s/he needs a new computer since the current computer is slow. Finding it to be a good deal, Xiaoming decided to check the computers on sale on JD.com during this sale.

3. Xiaoming receives a Wechat message from a friend that there is a big birthday dinner gathering for a mutual friend. Attending this birthday party will allow Xiaoming to have a good time and catch up with several friends not seen for a while. Finding it potentially useful, Xiaomin decided to attend.

4. Xiaoming’s best friend Xiaohong, who studies at another university, called to ask if Xiaoming is interested in going to a soccer game next weekend. Xiaoming's parents always discouraged watching soccer and encouraged studying instead. Since Xiaoming enjoys soccer, Xiaoming decided to join Xiaohong.

5. Xiaoming does not remember classmates’ names since s/he attends many classes and interacts with many students. To avoid awkward situations, Xiaoming decided to write down the names of the classmates in a notebook.

6. Xiaoming received permission from his professor to copy lab data to a personal disk in order to work on it from home. These data are needed for a homework assignment due next week. Therefore, Xiaoming copied the data to a personal USB drive.

7. Xiaoming’s dad owns a business that uses secured wireless networks. Xiaoming needs to work on school projects in this office. The school permits working on homework assignments from anywhere, assuming reasonable security assurances. Hence, Xiaoming decided to use the secured network for accessing school email.

8. Xiaoming needs Microsoft Visio to create charts for one of the school projects. The school provides this software and allows downloading it from the school servers because this software is needed for many homework projects. It even provides training showing students how to download and use this software. Hence, Xiaoming decided to download the software to Xiaoming’s personal computer.

## Control Scenarios: Study 2

1. Xiaoming receives an email from the university that the ministry of education is holding a meeting next weekend seeking inputs from students regarding their program of education. Xiaoming decided to attend.

2. Xiaoming receives a QQ group chat message from the dormitory saying that the old maintenance person (with whom Xiaoming was not familiar) is going to be replaced with a new one. Xiaoming decided to read the provided information on the new maintenance person.

3. Xiaoming reads a flyer on the cafeteria’s bulletin board, saying that the cafeteria manager (with whom Xiaoming was not familiar) is replaced by a new one. Xiaoming decided to read the provided bio of the new manager.

4. Xiaoming receives a text message from the university that there is a new website that outlines travel policies for department managers. Xiaoming decided to visit the website.

5. Xiaoming receives a Wechat message from the university that there is a dinner for the retiring manager of a lab (with whom Xiaoming was not familiar). Xiaoming decided to attend.

6. Xiaoming reads on the front page of the university website that the university hosts a badminton match between two universities from another province. Xiaoming decided to forward this information.

7. Xiaoming is a vegetarian. Today, the cafeteria is serving two main courses that Xiaoming does not like equally—fried Tofu or fried eggplants. Xiaoming decided to pick the fried tofu.

8. Xiaoming participates in a lab he does not like. Xiaoming needs to continue to work on lab data after class. Xiaoming copied the data to a personal USB drive.

## Case/target (ISP Violation) Scenarios

1. Writing Down the Password (Guo et al. 2011). For security and privacy reasons, the university issued difficult to remember user names and passwords; and implemented a policy stating that students are required to keep their passwords to themselves. Finding it difficult to remember the password, Xiaoming wrote down the user name and password on a sticker and attached it to the laptop computer s/he usually uses.

2. Unauthorized Portable Devices for Storing and Carrying Project Data (Guo et al. 2011). For the coursework, Xiaoming often prepares reports and presentations from home. As a result, Xiaoming often uses personal USB drives to copy data back and forth from the university computers. In a specific lab where confidential information is used, however, the university policy prohibits students from attaching unauthorized devices to the computers. The IT department argues that the use of unauthorized devices can cause security problems, such a loss and disclosure of confidential lab data and the spreading of computer viruses. Finding it difficult to work on the data during lab time, Xiaoming copied the data to a personal USB drive and to it home to work on it.

3. Installation and Use of Unauthorized Software (Guo et al. 2011). Xiaoming needs the AutoPro123 software (free) package for completing a project due in a week. The university does not provide this software package. While this package is too large to be installed on personal laptops, it can be installed on the lab computers at your university. The university, however, prohibits the installation of unauthorized software. The IT department insists that unapproved open source software may damage security and expose the network to external attacks. Finding it difficult to work on the project without this software, Xiaoming installed the AutoPro123 software on a lab computer.

4. Using Open Public Wireless Network for Accessing Confidential Lab Information (Guo et al. 2011). For the coursework, Xiaoming often works from different places with unsecured public wireless internet access. In a specific lab where confidential information is used, however, the university policy prohibits students from using unsecured public wireless networks. The IT department argues that such networks lack the needed encryption for securing the data. Finding it difficult to work on a lab project only when at the university, Xiaoming uses free public wireless access when working on this lab data.

5. Sharing Confidential IT security Information (Hu et al. 2015). Xiaoming received an email from a Southwest university professor who asked Xiaoming to talk about the details of IT security management at his dad’s firm, which is considered confidential, in a class seminar. Xiaoming thought it is an opportunity to impress the professor and agreed to do so.

6. Sharing Password (Hu et al. 2015). Xiaoming’s best friend, Xiaohong, who studies at another university, needed to run analysis on software that exists on Southwest university computers. She called to ask if Xiaoming can help her by sharing the university user and password just for this task. Xiaoming wanted to help his/her friend and agreed to share the user name and password.

7. Intentional-Unauthorized Download (Hu et al. 2015). Xiaoming has been upset about the university that cuts water and/or power too often. Xiaoming, therefore, decided to vent his/her anger by ignoring significant IT security policies and downloading and playing unsecured videogames on university computers.

8. Ignoring Password Change Recommendations (came up in pilot study). Xiaoming receives an email from the university that asks him/her to change the university password that has not been changed for over a year. This is the third request the university had sent. The email explains why changing the password is important for avoiding security breaches. Xiaoming is too busy. He/she deleted the email and decided not to change his/her password.

## General Measures (sliding scales after each scenario)

## Attitude (1-7 scale)

Performing this behavior is

• a (bad . . . good) idea.

• (harmful . . . beneficial).

• (wrongful . . . rightful).

• (unreasonable . . . reasonable).

• Should Xiaoming do [the behavior]? (No . . . Yes).

## Behavioral Intention (1-7 scale)

• I would do [the behavior] if I were Xiaoming.

• It is likely I would do [the behavior] if I were in a similar situation.

• I would perform the exact same thing if I were Xiaoming.

• I predict I would perform the same actions as Xiaoming.

## Appendix C

## Pilot Studies

## Pilot Test: Experiment 1

To test Experiment 1 scenarios, participants (20 in total) received both types of scenarios (eight control scenarios and eight ISP violation scenarios) in random order. The attitude and intention scales were reliable, with Cronbach alphas of 0.78 and 0.75, respectively, in control scenarios, and 0.82 and 0.75, respectively, in ISP violation scenarios. Mean scores of control scenarios were compared to these of ISP violation scenarios. Differences in attitude $[ M _ { \mathrm { \ c o n t r o l - I S P } } \pm S D _ { \mathrm { \ c o n t r o l - I S P } } = 2 . 3 8 \pm 1 . 1 2 , t ( 1 9 ) = 9 . 6 1 , p < 0 . 0 0 1 ]$ and intention $[ M _ { \mathrm { \ c o n t r o l - I S P } } \pm S D _ { \mathrm { \ c o n t r o l - I S P } } = 2 . 4 2 \pm$ $0 . 9 6 , t ( 1 9 ) = 1 1 . 2 7 , p < 0 . 0 0 1 ]$ were statistically significant. This indicated that both attitudes, and intentions toward the control scenarios were significantly higher than those toward the ISP violation scenarios. This is reasonable and is indicative of healthy decision-making; people had a lower attraction to what they perceived to be rewarding yet problematic behaviors (ISP violations in our case), even though such behaviors are more positively valenced<sup>3</sup>. This increases confidence in the validity of the scenarios. It highlights differences between valence and attitudes; attitudes are broader and are built, in part, on value assessment.

We also assessed the valence of the gains expected from completing the tasks described in the scenarios by asking respondents to report on a 1 (not at all)—5 (highly welcome/appreciated) scale the extent to which they welcome and appreciate the outcome of behaving this way. Mean valence of the ISP violation scenarios (M $^ { \prime } \mathrm { _ { I S P } } \pm S D \mathrm { _ { I S P } } { = } 4 . 0 8 \pm 1 . 1 1 ) $ was significantly higher $( t ( 1 9 ) = 2 . 4 3 , p = 0 . 0 2 5 )$ than that of the control scenarios (M <sub>Control</sub> $\pm S D _ { \mathrm { c o n t r o l } } { = } 3 . 4 6 \pm 0 . 2 3 )$ . This indicated that people see more potential value/gains in completing the ISP violation than control behaviors. Moreover, both control and ISP violations scenarios had mean valence scores significantly (both $p { < } 0 . 0 0 1 )$ ) above the middle point (3). This means that both the control and ISP violation behaviors were positively valenced; the perceived gains associated with these behaviors were beyond indifference.

Note that while the ISP violation scenarios were significantly more positively valenced compared to control scenarios, the attitudes and intentions toward engaging in ISP violations were lower. This is still consistent with expectancy theory (Vroom 1964), according to which the motivation to engage in a behavior is a function of expectancy, instrumentality, and valence. Thus, even though valence is higher in ISP violation scenarios, it is possible that expectancy and instrumentality are lower, compared to the control scenarios. For example, people may see the risk in ISP violations and believe that they do not have full control over the outcomes; they may consequently infer that their effort will not necessarily produce the expected performance gains (e.g., illegally downloaded software may slow down a person if it propagates viruses), even when such gains are highly desirable.

## Pilot Test: Experiment 2

A similar procedure was employed to pilot test Experiment 2’s scenarios. Eighteen participants received both types of scenarios in random order. The attitude and intention scales were reliable, with Cronbach alphas of 0.77 and 0.76, respectively in control scenarios, and 0.78 and 0.79, respectively, in ISP violation scenarios. Mean scores of control scenarios were compared to these of ISP violation scenarios. Like in the pilot test for Study 1, differences in attitude $[ M _ { \mathrm { \ c o n t r o l - I S P } } \pm S D _ { \mathrm { \ c o n t r o l - I S P } } = 2 . 3 2 \pm 1 . 0 1 , t ( 1 7 ) = 9 . 7 4 , p < 0 . 0 0 1 ]$ and intention $[ M _ { \mathrm { \ c o n t r o l - I S P } } \pm S D _ { \mathrm { \ c o n t r o l - I S P } } = 1 . 9 2$ $\pm 0 . 7 5 , t ( 1 7 ) = 1 0 . 8 6 , p < 0 . 0 0 1 ]$ were statistically significant. Similar to the pilot test for Experiment 1, mean valence of the ISP violation scenarios $( M _ { \mathrm { { \scriptsize ~ I S P \pm } } } \large { S D _ { \mathrm { { \scriptsize ~ I S P } } } } = 3 . 9 7 \pm 0 . 8 8 )$ was significantly higher $( t ( 1 7 ) = 2 . 6 4 , p = 0 . 0 1 2 )$ than that of the control scenarios $( M \mathrm { c o n t r o l } \pm S D \mathrm { c o n t r o l } { = }$ $3 . 4 0 \pm 0 . 2 5 )$ . In addition, both control and ISP violations scenarios had mean valence scores significantly (both $p { < } 0 . 0 0 1 )$ above the middle point (3). Lastly, the DLPFC mediates many cognitive functions; it is broadly involved in the executive function of decision-making (Fassbender et al. 2004). We, therefore, wanted to mitigate the possibility that ISP violations require higher cognitive effort compared to control scenarios. To this end, we asked pilot study participants to rate how much thinking/reflection they would engage in before deciding if they want to perform the described behaviors (1=” very little: $5 \mathrm { = } \mathrm { \Omega } ^ { 6 4 } \mathrm { a } \mathrm { l o t \Omega } ^ { 9 } )$ . ISP violation scenarios $( M _ { \mathrm { { \scriptsize ~ I S P \pm } } } \mathrm { { \scriptsize { S D _ { \mathrm { { I S P } } } = 1 . 8 9 \pm 0 . 9 0 ) } } }$ did not significantly differ $( t ( 1 7 ) = 0 . 1 6 4 , p$ = 0.872) in expected cognitive effort from control scenarios $( M _ { \mathrm { { \scriptsize ~ C o n t r o l } } \pm } S D _ { \mathrm { { \scriptsize ~ C o n t r o l } } } = 1 . 9 4 \pm 0 . 8 0 )$ . We hence concluded that the scenarios are valid and reliable, that they do not differ in the required cognitive effort, and that they produce different gain/valence beliefs in the expected direction. The consistency between pilot studies 1 and 2 provided confidence in the employed design and scenarios.

## Appendix D

## Valence of ISP Violation Vs. Compliance

This study aimed to examine if ISP violations are more positively valenced than ISP compliance. This assumption underlies the idea that tDCS can reduce endorsement of ISP violations, because it can also potentially reduce endorsement of compliance. We therefore recruited 28 students $( M _ { \mathrm { A g e } } \pm S D _ { \mathrm { A g e } } { = 2 0 . 5 \pm 1 . 2 1 } )$ and assessed the valence of the gains expected from (1) completing the tasks described in the eight ISP violation scenarios, and (2) complying with school policy and expectations, and not committing the presented acts. We did so by presenting the scenarios, once with compliance and another time with violation gain framing, in random order. For each scenario we asked respondents to report on a 1 (not at all) – 5 (highly welcome/appreciated) scale the extent to which they welcome and appreciate the outcome of (a) behaving this way, and in another question (b) complying with policies and expectations, and not enacting the behavior. Mean valence of the ISP violation $( M _ { \mathrm { { \scriptsize ~ I S P \pm } } } \mathrel { + } S D _ { \mathrm { { \scriptsize ~ I S P } } } = 3 . 9 7 \pm 0 . 6 8 )$ was significantly higher $( t ( 2 7 ) = 1 7 . 9 9 , p < 0 . 0 0 1 )$ than that of compliance (M <sub>Compliance</sub> + $S D _ { \mathrm { C o m p l i a n c e } } = 1 . 6 3 \pm 0 . 3 5 )$ . This indicated that people see more potential value/gains in ISP violation than in compliance, at least with regards to our ISP violation scenarios. Moreover, the correlation between the two was not significant (r=0.22, p=0.257). In addition, while ISP violation scenarios had mean valence scores significantly (p <0.001) above the middle point (3) of the scale; ISP compliance had a score significantly $( p < 0 . 0 0 1 )$ below this midpoint. Together, these findings indicated, in line with Cram et al. (2019), that at least in our context, compliance and violation are distinct phenomena, and that ISP violation is much more positively valenced than ISP compliance.

## Appendix References

Boggio, P.S., Sultani, N., Fecteau, S., Merabet, L., Mecca, T., Pascual-Leone, A., Basaglia, A., and Fregni, F. 2008. “Prefrontal Cortex Modulation Using Transcranial Dc Stimulation Reduces Alcohol Craving: A Double-Blind, Sham-Controlled Study,” Drug and Alcohol Dependence (92:1), pp. 55-60.

Cram, A., D’Arcy, J., and Proudfoot, J. 2019. "Seeing the Forest and the Trees: A Meta-Analysis of the Antecedents of Information Security Policy Compliance," MIS Quarterly (43:2), pp. 525-554.

Dimoka, A. 2010. “What Does the Brain Tell Us About Trust and Distrust? Evidence from a Functional Neuroimaging Study,” MIS Quarterl (34:2), pp. 373-396.

Dimoka, A., Banker, R.D., Benbasat, I., Davis, F.D., Dennis, A.R., Gefen, D., Gupta, A., Lschebeck, A., Kenning, P.H., Pavlou, P.A., Mueller-Putz, G., Riedl, R., vom Brocke, J., and Weber, B. 2012. “On the Neurophysiological Tools in IS Rsearch: Developing a Research Agenda for NeuroIS,” MIS Quarterly (36:3), pp. 679-702.

Dimoka, A., Pavlou, P.A., and Davis, F.D. 2011. “NeuroIS: The Potential of Cognitive Neuroscience for Information Systems Research,” Information Systems Research (22:4), pp. 687-702.

Fassbender, C., Murphy, K., Foxe, J.J., Wylie, G.R., Javitt, D.C., Robertson, I.H., and Garavan, H. 2004. “A Topography of Executive Functions and Their Interactions Revealed by Functional Magnetic Resonance Imaging,” Cognitive Brain Research (20:2), pp. 132-143.

Fecteau, S., Knoch, D., Fregni, F., Sultani, N., Boggio, P., and Pascual-Leone, A. 2007a. “Diminishing Risk-Taking Behavior by Modulating Activity in the Prefrontal Cortex: A Direct Current Stimulation Study,” Journal of Neuroscience (27:46), pp. 12500-12505.

Fecteau, S., Pascual-Leone, A., Zald, D.H., Liguori, P., Theoret, H., Boggio, P.S., and Fregni, F. 2007b. “Activation of Prefrontal Cortex by Transcranial Direct Current Stimulation Reduces Appetite for Risk During Ambiguous Decision Making,” Journal of Neuroscience (27:23), pp. 6212-6218.

Fregni, F., Boggio, P.S., Nitsche, M., Bermpohl, F., Antal, A., Feredoes, E., Marcolin, M.A., Rigonatti, S.P., Silva, M.T.A., Paulus, W., and Pascual-Leone, A. 2005. “Anodal Transcranial Direct Current Stimulation of Prefrontal Cortex Enhances Working Memory,” Experimental Brain Research (166:1), pp. 23-30.

Guo, K.H., Yuan, Y., Archer, N.P., and Connelly, C.E. 2011. “Understanding Nonmalicious Security Violations in the Workplace: A Composite Behavior Model,” Journal of Management Information Systems (28:2), pp. 203-236.

Heeren, A., Baeken, C., Vanderhasselt, M.A., Philippot, P., and de Raedt, R. 2015. “Impact of Anodal and Cathodal Transcranial Direct Current Stimulation over the Left Dorsolateral Prefrontal Cortex During Attention Bias Modification: An Eye-Tracking Study,” PLOS ONE (10:4), Article e0124182.

Hu, Q., West, R., and Smarandescu, L. 2015. “The Role of Self-Control in Information Security Violations: Insights from a Cognitive Neuroscience Perspective,” Journal of Management Information Systems (31:4), pp. 6-48.

Huang, D.Q., Chen, S., Wang, S.Q., Shi, J.C., Ye, H., Luo, J., and Zheng, H.L. 2017. “Activation of the DLPFC Reveals an Asymmetric Effect in Risky Decision Making: Evidence from a tDCS Study,” Frontiers in Psychology (8), Article 38.

Li, M., Jiang, Q., Tan, C.-H., and Wei, K.-K. 2014. “Enhancing User-Game Engagement through Software Gaming Elements,” Journal of Management Information Systems (30:4), pp. 115-150.

Luft, C.D., Zioga, I., Banissy, M.J., and Bhattacharya, J. 2017. “Relaxing Learned Constraints through Cathodal tDCS on the Left Dorsolateral Prefrontal Cortex,” Scientific Reports (7), Article 2916.

Mengarelli, F., Spoglianti, S., Avenanti, A., and di Pellegrino, G. 2015. “Cathodal tDCS over the Left Prefrontal Cortex Diminishes Choice-Induced Preference Change,” Cerebral Cortex (25:5), pp. 1219-1227.

Minas, R.K., Potter, R.F., Dennis, A.R., Bartelt, V., and Bae, S. 2014. “Putting on the Thinking Cap: Using NeuroIS to Understand Information Processing Biases in Virtual Teams,” Journal of Management Information Systems (30:4), pp. 49-82.

Pripfl, J., and Lamm, C. 2015. “Focused Transcranial Direct Current Stimulation (tDCS) over the Dorsolateral Prefrontal Cortex Modulates Specific Domains of Self-Regulation,” Neuroscience Research (91), pp. 41-47.

Riedl, R., Hubert, M., and Kenning, P. 2010. “Are There Neural Gender Differences in Online Trust? An fMRI Study on the Perceived Trustworthiness of Ebay Offers,” MIS Quarterly (34:2), pp. 397-428.

Vroom, V.H. 1964. Work and Motivation, John Wiley.

Wolkenstein, L., Zeiller, M., Kanske, P., and Plewnia, C. 2014. “Induction of a Depression-Like Negativity Bias by Cathodal Transcranial Direct Current Stimulation,” Cortex (59), pp. 103-112.

Ye, H., Chen, S., Huang, D.Q., Wang, S.Q., Jia, Y.M., and Luo, J. 2015a. “Transcranial Direct Current Stimulation over Prefrontal Cortex Diminishes Degree of Risk Aversion,” Neuroscience Letters (598), pp. 18-22.

Ye, H., Chen, S., Huang, D.Q., Wang, S.Q., and Luo, J. 2015b. “Modulating Activity in the Prefrontal Cortex Changes Decision-Making for Risky Gains and Losses: A Transcranial Direct Current Stimulation Study,” Behavioural Brain Research (286), pp. 17-21.
