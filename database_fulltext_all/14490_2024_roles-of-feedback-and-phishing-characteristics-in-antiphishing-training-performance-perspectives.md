---
otero_id: 14490
otero_key: "FAU6CSDY"
title: "Roles of Feedback and Phishing Characteristics in Antiphishing Training Performance: Perspectives of Goal Setting and Skill Acquisition"
authors: "Shihe Pan; Dong-Heon Kwak; Jungwon Kuem; Sung S. Kim"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00854"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Roles of Feedback and Phishing Characteristics in Antiphishing Training P  erformance: P  erspectiv es of Goal Setting and Skill Acquisition

Shihe Pan , span@tju.edu.cn

Dong-Heon Kwak , dkwak@kent.edu

Jungwon Kuem , jkuem@albany.edu

Sung S. Kim , skim@bus.wisc.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Roles of Feedback and Phishing Characteristics in Antiphishing Training Performance: Perspectives of Goal Setting and Skill Acquisition

Shihe Pan,<sup>1</sup> Dong-Heon Kwak,<sup>2</sup> Jungwon Kuem,<sup>3</sup> Sung S. Kim<sup>4</sup>

<sup>1</sup>Tianjin University, China, span@tju.edu.cn <sup>2</sup>Kent State University, USA, dkwak@kent.edu <sup>3</sup>State University of New York at Albany, USA, jkuem@albany.edu <sup>4</sup>University of Wisconsin-Madison, USA, skim@bus.wisc.edu

## Abstract

Because phishing attacks often exploit individuals’ inexperience in detecting them, it is important for managers to provide workers with proper feedback on their reactions to phishing scams. However, little is known about what types of feedback are more effective in facilitating antiphishing training behavior and performance. The objectives of this study are to identify (1) the determinants of decision avoidance and detection accuracy, (2) the contextual effect of type of feedback in antiphishing training, (3) the impacts of perceived detection efficacy on training outcomes, and (4) the interaction effects between feedback characteristics and perceived detection efficacy/phishing characteristics on training outcomes. Drawing upon goal-setting theory, skill acquisition theory, and antiphishing training literature, our model provides a theoretical account of how feedback characteristics (e.g., type, quantity), phishing characteristics (e.g., phishing cue saliency), and perceived detection efficacy affect antiphishing training outcomes (e.g., decision avoidance and detection accuracy). To empirically test the model, we performed four experiments with 652 subjects in the United States from three different online panels via Amazon Mechanical Turk, Esearch.com, and Clickworker.com. Our results indicate that examplebased feedback is superior to abstract feedback in teaching how to correctly discern between phishing and legitimate emails in the context of link-embedded emails. We also show that perceived detection efficacy is essential for a better understanding of antiphishing training behavior and performance. Finally, we show an interaction effect between feedback quantity and phishing cue saliency on antiphishing training behavior and performance.

Keywords: Phishing, Antiphishing Training, Feedback, Phishing Cue Saliency, Perceived Detection Efficacy, Goal Setting, Skill Acquisition, Decision Avoidance, Detection Accuracy, Experiments, Hierarchical Linear Modeling

Paul Benjamin Lowry was the accepting senior editor. This research article was submitted on August 29, 2021 and underwent two revisions.

## 1 Introduction

Successful phishing attacks cause an enormous amount of financial and data losses in organizations. In fact, phishing is considered the number one cause of data breaches (Verizon, 2022). Recent studies show that in

2021, almost 80% of organizations were attacked, resulting in losses of more than \$2.4 billion (FBI, 2022; Proofpoint, 2022). Because phishing attacks often exploit individuals’ inexperience in detecting phishing scams, it is important for managers to train employees in awareness and detection (Nguyen et al.,

2021a; Silic & Lowry, 2020; Sumner, 2021). Organizations often offer phishing awareness programs that include security announcements, posters, newsletters, short videos, and feedback about previous phishing attacks (Educause, 2020; Sarno et al., 2022; Schuetz et al., 2020). These kinds of brief materials can be used to cover many employees and are easily embedded in individuals’ day-to-day workflow. However, such awareness programs may require information technology (IT) departments to devote considerable resources to their analysis, design, development, and administration (Osterman Research, 2019). Thus, to facilitate successful antiphishing behavior and performance in organizations, researchers and practitioners need to be able to systematically analyze the effectiveness of these educational programs under various conditions.

Several studies have examined how antiphishing training helps individuals differentiate between legitimate and phishing emails (Jampen et al., 2020; Jensen et al., 2017; Kumaraguru et al., 2007a; Nguyen et al., 2021a; Schuetz et al., 2020; Silic & Lowry, 2020; Wen et al., 2019). For example, Wang et al. (2016) showed that coping adaptiveness positively affects detection accuracy. Likewise, Sumner (2021) showed the effectiveness of the KnowBe4 training in enhancing individuals’ antiphishing performance. Also, Sarno et al. (2022) found that email classification aid and basic feedback improve people’s ability to discern between phishing and legitimate emails. Although prior research has revealed important aspects of antiphishing training, our knowledge of this research topic is lacking in several critical areas.

First, antiphishing training research has generally focused on detection accuracy as a major behavioral outcome (Jensen et al., 2017; Nguyen et al., 2021a; Silic & Lowry, 2020; Wang et al., 2017). However, little is known about common cases such as individuals deciding not to respond to an incoming email (Waterloo News, 2019). Decision avoidance, which inevitably entails a loss of potential benefits from interacting with others, is a universal phenomenon under uncertainty (Anderson, 2003). Therefore, to better understand the role of antiphishing training, it is important to examine not only detection accuracy but also decision avoidance.

Second, prior research on antiphishing training has attempted to identify the effectiveness of types of feedback in different contexts (Jensen et al., 2017; Nguyen et al., 2021a). For example, in the context of overlearning, Nguyen et al. (2021a) hypothesized that rule-based training is better than mindful training in discriminating against phishing emails and increasing phishing awareness. Identifying such contextual effects of feedback types is important because phishing emails have various formats, and organizations should try in their antiphishing training to inculcate awareness of the dangers of various formats.

Third, prior antiphishing research found that selfefficacy is an important predictor of antiphishing motivation and behavior (Sun et al., 2016; Verkijika, 2019; Wang et al., 2016, 2017). In the context of antiphishing training, perceived detection efficacy was found to influence overconfidence (Wang et al., 2016) and coping adaptiveness (Wang et al., 2017). Despite the findings of Wang et al. (2016, 2017), we are not certain that perceived detection efficacy can directly influence individuals’ decision avoidance and detection accuracy in antiphishing training.

Last, our understanding is limited regarding how feedback characteristics interact with phishing characteristics and individuals’ self-efficacy in regulating antiphishing behavior and performance. Because phishing attacks can take various formats, the effectiveness of feedback is unlikely to be identical across phishing scams and individuals’ detection efficacy. A systematic examination of the effect of feedback on antiphishing training behavior and performance cannot be complete without an additional analysis of phishing characteristics and individuals efficacy in detecting phishing emails.

The objectives of this research are to investigate (1) the determinants of decision avoidance and detection accuracy, (2) the contextual effect of type of feedback in antiphishing training, (3) the impacts of perceived detection efficacy on training outcomes, and (4) the interaction effects between feedback characteristics and perceived detection efficacy/phishing characteristics on training outcomes. Drawing upon goal-setting theory (Locke & Latham, 2002), we examined feedback characteristics (i.e., type, quantity), phishing characteristics (i.e., phishing cue saliency), and selfefficacy (i.e., perceived detection efficacy) as determinants of antiphishing training outcomes (i.e., decision avoidance and detection accuracy). Furthermore, based on skill acquisition theory (Anderson, 1982, 1987), we examined the contextual effects of feedback types (e.g., example-based feedback, mindful feedback) on antiphishing performance. Also, our model provides a theoretical account of the impacts of perceived detection efficacy on training outcomes and how feedback characteristics interact with perceived detection efficacy and phishing characteristics to influence antiphishing behavior.

To empirically test the proposed model, we performed four experiments with 652 subjects in the United States. Specifically, given the prevalence of phishing scams relying on false links in an email (PhishLabs, 2019; Proofpoint, 2022), we focused exclusively on those popular phishing techniques associated with false links. Our results indicate that example-based feedback is more effective than feedback with abstract information for correctly distinguishing between phishing and legitimate emails in the context of link-embedded emails. However, this effect is not sustainable when individuals encounter a new type of phishing email (i.e., phishing emails that do not include false links). In addition, we show that perceived detection efficacy is an important factor for better understanding antiphishing training behavior and performance. Finally, this study demonstrates that the impacts of phishing cue saliency on antiphishing outcomes vary significantly with the quantity of feedback.

Our study contributes to information systems (IS) and phishing research in several ways. First, we are among the few researchers who have examined both decision avoidance and detection accuracy within a goal-setting perspective to reveal the complex nature of antiphishing training behavior and performance. Second, we have theoretically proposed and empirically shown the contextual effect of feedback types. We show that example-based feedback can outperform mindful feedback in facilitating antiphishing training performance when emails involve links. Third, we offer a theoretical account of how the impact of perceived detection efficacy on detection accuracy changes with types of feedback. Fourth, drawing on skill acquisition theory, we have also shown an interaction effect between feedback quantity and phishing cue saliency in the context of antiphishing training. Overall, our study contributes significantly to IS research by providing a systemic, theory-driven model of how the offensive (phishing characteristics) and defensive (feedback characteristics) sides of phishing interact to regulate antiphishing behavior and performance.

## 2 Theoretical Background

## 2.1 Antiphishing Literature

Prior phishing research has examined individuals’ antiphishing performance from various perspectives (see Appendix A). One stream of research focused on the predictors of antiphishing performance, such as individual characteristics, phishing characteristics, and social and physical contexts, without explicitly considering external approaches to improve performance (Chen et al., 2020; Frank et al., 2022; Goel et al., 2017; Jaeger & Eckhardt, 2021; Vishwanath, 2017; Wang et al., 2016, 2017; Wright et al., 2014, 2023).

Another stream has examined the effectiveness of different external interventions for increasing individuals’ antiphishing performance. These diverse interventions included antiphishing warning systems (Abbasi et al., 2021; Nguyen et al., 2021b), fear appeals (Schuetz et al., 2020), phishing emails or website detection aids (Sarno et al., 2022; Zahedi et al., 2015), and incentives (Goel et al., 2021). In addition, several studies have examined the effectiveness of training programs for improving antiphishing performance (e.g., Dincelli & Smith, 2020; Jensen et al., 2017; Nguyen et al., 2021a; Silic & Lowry, 2020; Sumner et al., 2021). The current literature indicates the importance of the design features of training programs (e.g., the content, frequency, and delivery mode) in improving antiphishing performance. For example, Silic and Lowry (2020) showed the advantage of gamified antiphishing training over email warnings or announcements in improving antiphishing performance. Jensen and colleagues (Jensen et al., 2017; Nguyen et al., 2021a) compared two types of antiphishing training: mindfulness and rule-based. Mindfulness training asks trainees to allocate attention to their emails’ requests, consider carefully how the email contents are associated with their situations, and avoid rushed decisions. Rule-based training teaches individuals a list of cues that can help them discriminate between legitimate and phishing emails. Jensen et al. (2017) found that supplemental training based on the mindfulness technique was more effective than rule-based training after initial exposure to rulebased training. Nguyen et al. (2021a) found that mindfulness training was more effective than rulebased training for both short- and long-term memories. Nguyen et al. (2021a) also hypothesized that in the training context of overlearning, rule-based training is more effective than mindfulness training because overlearning during rule-based training can help individuals more quickly comprehend the rules and cues related to phishing emails. However, this hypothesis was not supported.

The rule-based training examined by Jensen et al. lists cues a person should look for when evaluating an email message. However, rule-based training is not confined to a specific format. As a result, there is a limited understanding of whether a certain type of rule-based training would be more effective than mindfulness training. In addition, the existing mindful and rulebased approaches have been incorporated into relatively long-lasting training programs that contain phishing introductions, webpage training materials, and practice sessions. Accordingly, it is unknown how mindfulness and rule-based training affect antiphishing performance in other training contexts, such as trial-and-error phishing detection or game-like antiphishing training.

Table 1. Descriptions of Feedback Types

<table><tr><td colspan="2">Feedback type</td><td>Descriptions</td><td>Study</td></tr><tr><td colspan="2">Mindful feedback</td><td>Encouraging trainees to allocate attention to process messages, relate the email contents to their situations, and avoid making hasty judgments</td><td>Jensen et al. (2017) Nguyen et al. (2021a)</td></tr><tr><td rowspan="2">Rule-based feedback</td><td>List-based</td><td>Stating a list of cues that people should pay attention to when evaluating email messages</td><td>Jensen et al. (2017) Nguyen et al. (2021a)</td></tr><tr><td>Example-based</td><td>Feedback that directly presents trainees with a prior phishing email and teaches them what the phishing cues look like in that specific email</td><td>Current study</td></tr></table>

In the current study, we examined the effectiveness of another rule-based training, namely example-based training. Example-based training refers to training materials that directly present trainees with what an actual phishing email looks like and how to recognize the phishing cues in a specific email. This examplebased training has been used in recent online phishing detection tests such as Google’s. Example-based training can be more concrete and better assist people’s understanding of what suspicious phishing cues look like compared to existing rule-based training, which typically conveys detection guidance via texts. This rationale aligns with findings from related studies on general security training and other antiphishing external interventions that suggest the advantage of concrete information (Reeves et al., 2023; Schuetz et al., 2020). However, recent studies imply that the design features of information-security-promoting materials and the characteristics of the corresponding protection task may interact to influence recipients’ protection behaviors (Schuetz et al., 2021; Vance et al., 2022). The relative effectiveness of different antiphishing training materials can be more complex, depending on the characteristics of the phishing messages at hand and individuals’ perceptions of those messages. Thus, this study investigates the relative effectiveness between example-based and mindfulness training across different phishing messages when used as feedback material in a trial-and-error phishing detection test. Table 1 further describes the three types of feedback in the context of antiphishing training.

## 2.2 Goal-Setting Theory

The notion of goals has been an important theoretical concept for describing how people achieve a desired end state (Gollwitzer, 1996; Kwak et al., 2022; Locke & Latham, 2002; Sheldon & Elliot, 1999). Locke and Latham (2002) noted that “a goal is the object or aim of an action, for example, to attain a specific standard of proficiency, usually within a specified time limit (p. 705). In the context of antiphishing training, the goals are to improve trainees’ knowledge of phishing and their antiphishing performance. Because goal-setting theory (Locke & Latham, 2002) helps identify various constructs that affect actual performance and their underlying mechanisms, the theory is suitable for examining determinants of decision avoidance and detection accuracy in antiphishing training. Based on goal-setting theory, we draw on feedback (i.e., feedback characteristics), task complexity (i.e., phishing characteristics), and self-efficacy (i.e., perceived detection efficacy), which represent, respectively, organizational intervention, task characteristics, and individual characteristics.

## 2.2.1 Feedback Characteristics

Feedback refers to information about a person’s performance of a task. Feedback can take various forms, such as progress bars, leaderboards, points, grades, and text (Kluger et al., 1994; Kwak et al., 2019; Werbach & Hunter, 2012). The use of feedback as a tool for informing individuals and members of an organization about their performance has been studied extensively (Kluger & DeNisi, 1996; Lam et al., 2011; Locke & Latham, 2002; Tseng et al., 2019). Prior researchers have considered it an important factor in increasing individuals’ engagement and performance (Bangert-Drowns et al., 1991; Kluger et al., 1994). Also, in several studies, feedback on antiphishing training has been used to improve antiphishing training performance (Jensen et al., 2017; Kumaraguru et al., 2007a; Sheng et al., 2007; Shepherd & Archibald, 2017; Silic & Lowry, 2020). Providing feedback is important because it can “serve as a motivational factor” and “correct illusory performance perceptions” (Jung et al., 2010, p. 728). People have an inherent desire to achieve tasks, and feedback can be used as a basis for facilitating antiphishing training behavior and performance.

Much research on phishing uses feedback to improve the learning outcomes of antiphishing training. For example, Kumaraguru et al. (2007a) found that trainees learn more effectively when they get immediate feedback through embedded training after they fail to detect a phishing attack than when the feedback is delivered later via email. Game-based training provides both evaluative (e.g., correct or incorrect answers) and informative (e.g., why it is phishing) feedback. Wen et al. (2019) examined a roleplay antiphishing game and stated the provision of feedback as one of their primary design principles. Silic and Lowry (2020) showed that a gamified security training program that continues to provide feedback was more effective than a simple emailcommunication security training program. Jampen et al. (2020) reviewed the effectiveness of different antiphishing training programs and confirmed the long-term effect of providing feedback.

However, the effect of feedback on task performance relies mainly on its characteristics (e.g., type of feedback, feedback quantity) as well as the task characteristics (e.g., task complexity) at hand (Hattie & Timperley, 2007; Kluger & DeNisi, 1996). Although much research exists on antiphishing feedback, no research has systematically investigated how antiphishing training behavior and performance vary with the characteristics of the feedback dispensed. Thus, it is important to examine the effects that feedback characteristics have on decision avoidance and detection accuracy. In particular, we examined two types of feedback: mindful and example-based (Canova et al., 2015b; Jensen et al., 2017; Stockhardt et al., 2016). Because mindful feedback is known to be effective in general antiphishing training, we attempted to identify the contexts in which examplebased feedback is more effective.

We further examined the role of feedback quantity in subsequent antiphishing training outcomes. Feedback quantity is defined as the details of information present in feedback as measured by the amount of text and graphics. Prior research has suggested that more feedback leads to more learning and better task performance (Newell, 1976; Salmoni et al., 1984). However, because individuals have limited cognitive resources, feedback quantity may not always lead to better performance (Kluger & DeNisi, 1996; Lam et al., 2011). Thus, it remains unclear how feedback quantity would influence decision avoidance and detection accuracy, especially in the context of antiphishing training.

## 2.2.2 Phishing Characteristics

Prior research has noted that task characteristics play an important role in predicting task performance (Devine & Kozlowski, 1995; Griffin et al., 1981; Locke & Latham, 2002; Mohammed & Harrison, 2013). For example, Oldham et al. (1976) found that job characteristics significantly influence work-related performance. Also, Devine and Kozlowski (1995) showed that task characteristics moderate the relationship between decision makers’ knowledge level and their decision accuracy. In particular, considerable research has emphasized that task complexity is among the most critical attributes of task characteristics in influencing individuals’ training behavior and performance (Liu & Li, 2012; Xu et al., 2014).

Task complexity is “the result of the attentional, memory, reasoning, and other information demands imposed by the structure of the task” (Robinson, 2001, p. 29). Thus, a higher level of task complexity requires more cognitive resources, adversely affecting decisionmaking and task performance (Braarud, 2001). In the context of decision-making, for example, Tversky and Kahneman (1981) claimed that the complexity of practical problems of decision tasks (e.g., portfolio selection) would prevent individuals from integrating existing options. Also, Steele-Johnson et al. (2011) found that both objective and subjective task complexity negatively influenced task performance.

In the context of antiphishing training, an antiphishing task involves the activity of differentiating between legitimate and phishing emails. Successful performance of such a task may depend on various factors, but as discussed previously, the complexity of the task is arguably among the most important factors affecting performance. For example, some phishing messages are easily detected by simple and apparent cues (e.g., incorrect names and suspicious sender addresses). In contrast, others are highly deceptive, with complex and concealed cues (e.g., a fake link buried in a lengthy message). Thus, as a factor reflecting the complexity of a task, the saliency of these cues is likely to play a critical role in antiphishing behavior and performance (Downs et al., 2006; Sheng et al., 2007). This study defines phishing cue saliency as the degree to which phishing cues are obvious in an email message. Despite the importance of phishing cue saliency in influencing antiphishing behavior and performance, little research has been conducted on this concept in the IS field.

## 2.2.3 Self-Efficacy

Self-efficacy is an important concept in understanding task performance in achievement-based contexts such as learning and training (Locke & Latham, 2002). Prior research has concluded that self-efficacy is an important predictor of behavioral motivation and engagement (Bagozzi et al., 2003b; Bandura, 1997). In the context of antiphishing, Sun et al. (2016) found that antiphishing self-efficacy mediates the relationship between internet self-efficacy and antiphishing behavior. Likewise, Verkijika (2019) showed that antiphishing self-efficacy affects avoidance motivation and behavior. In antiphishing training, self-efficacy is likely to be a significant determinant of decisionmaking and performance. For example, Wang et al. (2017) showed that perceived detection efficacy significantly influences coping adaptiveness, thus affecting detection efforts and accuracy. Furthermore, Wang et al. (2016) found that perceived detection efficacy leads to overconfidence, which refers to “the extent to which confidence exceeds performance (or accuracy)” (p. 761). Despite the findings of Wang et al.

(2016, 2017), there is little understanding of the direct effect of perceived detection efficacy on decision avoidance and detection accuracy in the context of antiphishing training. Thus, it is still unknown whether perceived detection efficacy would be significant in determining antiphishing training outcomes even after controlling for already well-established factors such as coping responses.

## 2.3 Skill Acquisition Theory

Anderson (1982) proposed a framework for skill acquisition that includes three knowledge phases in the development of cognitive skills: (1) declarative knowledge, (2) knowledge compilation, and (3) procedural knowledge (Anderson, 1982, 2010). Declarative knowledge refers to knowledge about facts (Anderson, 2010). This phase of skill acquisition contains all the necessary memory and reasoning processes that allow an individual to obtain an understanding of task requirements (Anderson, 2010; Kanfer & Ackerman, 1989). The second phase, knowledge compilation, is “the process by which the skill transits from the declarative stage to the procedural stage” (Anderson, 1982, p. 369). In this phase, the best course of action sequences is chosen out of numerous alternatives that could be used to fulfill the same task requirements. As a result, knowledge composition integrates into a single procedure the procedural sequences required to perform a task. Finally, procedural knowledge is defined as “knowledge about how to perform the task” (Anderson, 2010, p. 205). This final phase of skill acquisition is reached when an individual fundamentally automatizes the skill, and the task can be performed accurately with little attention (Kanfer & Ackerman, 1989). Complete procedural knowledge is generally acquired after considerable consistent practice.

Prior research on skill acquisition has noted that declarative knowledge and procedural knowledge are on a continuum; that is, declarative knowledge can be developed into procedural knowledge via knowledge compilation (Anderson, 1982, 2010; Bialystok, 1979). Furthermore, obtaining declarative knowledge requires significant cognitive resources in skill acquisition (Phase 1), but after an individual learns skills through knowledge compilation (Phase 2) and procedural knowledge (Phase 3), the demands on cognitive resources lessen significantly. Accordingly, after knowledge proceduralization is complete, the task can be performed with few attentional resources (Kanfer & Ackerman, 1989; Taatgen et al., 2007).

When organizational interventions (e.g., feedback) and multiple tasks (e.g., phishing quizzes) are provided in training, organizations should consider how trainees can effectively acquire cognitive skills. This is because trainees have a limited cognitive capacity for acquiring new information (i.e., declarative knowledge), integrating the information and procedures (i.e., knowledge compilation), and applying the combination to different tasks (i.e., procedural knowledge) (Kanfer & Ackerman, 1989; Lam et al., 2011; Tseng et al., 2019). As a result, skill acquisition theory is expected to be useful in developing a better understanding of antiphishing behavior and performance by considering how individuals can effectively acquire and use cognitive skills in performing antiphishing tasks.

## 3 Research Model and Hypotheses

Figure 1 presents a conceptual model and the research hypotheses proposed in this study to examine the determinants of decision avoidance and detection accuracy in the context of antiphishing training. Drawing on goal-setting theory, we examine feedback characteristics (i.e., feedback type and quantity) at the individual level and phishing characteristics (i.e., phishing cue saliency) and self-efficacy (i.e., perceived detection efficacy) at the message level. Based on skill acquisition theory, we further propose the relative effectiveness of example-based feedback in the context of link-embedded emails. Hypothesis development is provided below.

## 3.1 Feedback Type and Perceived Detection Efficacy

From the skill acquisition perspective, feedback helps individuals obtain knowledge and correct existing knowledge (declarative knowledge), integrate various aspects of procedural knowledge into one simplified action sequence (knowledge compilation), and apply the obtained knowledge to task performance (knowledge proceduralization). Especially when feedback is provided with direct cues, such feedback is known to further reduce cognitive effort, improve cognitive attention, and eventually lead to higher performance (Kanfer & Ackerman, 1989). This happens because feedback with direct cues helps people expend their cognitive resources on the essential actions specified in such feedback only (Jung et al., 2010; Roch et al., 2000). Accordingly, examplebased feedback, which focuses on the attributes manipulated by attackers, is likely to facilitate antiphishing training behavior and performance. In particular, example-based feedback—which contains specific terms such as “HTTPs,” “website address,” and “email domain,” as well as specific guidelines such as “hover your mouse on the link”—makes it easier for people to apply specific antiphishing tips to the task of deciding whether the links within messages are genuine or fakes.

![](/api/attachments/FAU6CSDY/fulltext/images/ae82c0560fd87f6f81758cefcae43dace198dac0059cae77e2636185a34a25b6.jpg)  
Figure 1. Research Model

Unlike example-based feedback, mindful feedback encourages individuals to dynamically assign cognitive attention and improve awareness of context. In doing so, mindful feedback typically includes speculative suggestions such as “stop” and “don’t mindlessly act on an email” (Jensen et al., 2017). Mindful feedback can help make individuals more conscious when they check incoming emails. However, mindful feedback is unlikely to be the most effective form for directing an individual’s attention to specific cues present in phishing emails. Mindful feedback focuses on what to do rather than how to do; thus, individuals provided with mindful feedback may not have a clear idea of how mindful principles can be applied to the specific task of antiphishing.

In summary, individuals who are given example-based feedback can acquire procedural knowledge more easily than those instructed in mindful feedback in the context of link-embedded emails. Furthermore, when trainees successfully compile and proceduralize declarative knowledge, they can effectively perform a task with confidence and little cognitive burden (Kanfer & Ackerman, 1989). Accordingly, compared with mindful feedback, example-based feedback is more effective in helping individuals correctly recognize phishing messages with fake links. Mindful feedback, on the other hand, has the potential to make individuals more cautious in deciding whether an email is phishing or legitimate. Thus, we hypothesize this contextual effect of feedback type on antiphishing training outcomes as follows:

H1a: Example-based feedback leads to less decision avoidance than mindful feedback.

H1b: Example-based feedback leads to higher detection accuracy than mindful feedback.

In the context of antiphishing training, perceived detection efficacy is an individual’s confidence in whether they can detect a phishing email. Prior research (e.g., Bagozzi et al., 2003a; Fitzsimmons & Douglas, 2011) has noted that self-efficacy is aligned with expectancy, the belief that an individual’s effort will result in the accomplishment of the desired goal (Vroom, 1964). When their expectancy is high, individuals are motivated to expend their cognitive resources, leading to better task performance (Bagozzi et al., 2003a; Kanfer & Ackerman, 1989; Vroom, 1964). In the context of antiphishing training, when individuals believe they can detect a phishing email, they are unlikely to avoid making a decision on a phishing task. Moreover, people with high perceived detection efficacy will expend more cognitive effort to meet their expectations of identifying a phishing email (Sun et al., 2016; Verkijika, 2019; Wang et al., 2017). Therefore, all things being equal, increased effort toward an antiphishing task will increase detection accuracy. Based on the above reasoning, we hypothesize that:

H2a: Perceived detection efficacy negatively influences decision avoidance.

H2b: Perceived detection efficacy positively influences detection accuracy.

Self-efficacy reflects “the amount of time and effort one has to invest” and “how aspects of an action” to achieve a certain task (Liberman & Trope, 1998, p. 7). Thus, the effect of perceived detection efficacy on detection accuracy will be reinforced when trainees have sufficient cognitive resources and knowledge about how to perform antiphishing tasks. As previously noted, example-based feedback provides actual antiphishing tips and techniques, allowing individuals to easily understand and apply such feedback to the antiphishing task at hand. In skill acquisition, individuals given example-based feedback can easily compile and proceduralize their phishing knowledge and allocate their cognitive resources efficiently. Accordingly, example-based feedback facilitates procedural knowledge and is expected to enhance the successful realization of perceived efficacy. Thus, example-based feedback will strengthen the effect of perceived detection efficacy on detection accuracy.

In contrast, individuals receiving mindful feedback tend to face more difficulty in proceduralizing antiphishing knowledge because they do not receive detailed instructions about applying specific antiphishing tips to detect phishing messages with fake links. In addition, mindful feedback has less power to reinforce the successful realization of one’s feasible ideas. Thus, under mindful feedback, the effect of perceived detection efficacy on detection accuracy will be weaker. Overall, we hypothesize that the effect of perceived detection efficacy on detection accuracy will be stronger under the example-based feedback condition than under the mindful feedback condition in the context of link-embedded emails.<sup>1</sup>

H3b: There will be an interaction effect between feedback type and perceived detection efficacy on detection accuracy such that the positive effect of perceived detection efficacy will be stronger under the example-based feedback condition than under the mindful feedback condition.

## 3.2 Feedback Quantity and Phishing Cue Saliency

We hypothesized earlier about how example-based feedback and mindful feedback will have different effects on individuals’ decision avoidance and detection accuracy. We further proposed that decision avoidance and detection accuracy would vary with the amount of information provided in example-based feedback. The quantity of example-based feedback is defined as the amount of detailed information about phishing cues and antiphishing tips present in an educational message. Prior IS research has suggested that having enough information is an important attribute of information quality that leads to IS success (Kim et al., 2004; Kwak et al., 2019; Palmer, 2002). Likewise, feedback research has shown that more feedback enables individuals to make better use of feedback information to learn important task strategies and increase task performance (Bilodeau, 1966; Cook, 1968; Komaki et al., 1980). As discussed previously, individuals provided with educational information in a form conducive to procedural knowledge (e.g., example-based feedback) are expected to perform conventional antiphishing tasks more effectively than those provided with abstract, high-level information (e.g., mindful feedback) (Anderson, 1982, 2010). Furthermore, individuals given a high quantity of example-based feedback will be able to acquire more information about phishing emails and how to detect them. Subsequently, individuals provided with ample accessible procedural knowledge that can be readily applied to phishing tasks are likelier to be capable of differentiating between legitimate and phishing emails. Therefore, we hypothesize that the quantity of example-based feedback leads to reduced decision avoidance and increased detection accuracy in the context of link-embedded emails.

H4a: Quantity of example-based feedback negatively influences decision avoidance.

## H4b: Quantity of example-based feedback positively influences detection accuracy.

Complex tasks require more cognitive resources because they impose increased stress and cognitive loads on people (Lam et al., 2011; Norman & Bobrow, 1975; Robinson, 2001; Wickens, 1984). For example, at the initial stage of skill acquisition, Kanfer and Ackerman (1989) noted that complex tasks divert individuals’ cognitive resources toward self-regulatory processes and away from task-focused learning, leading to inefficiency in task performance. In the context of antiphishing training, a phishing email with high cue saliency, by definition, will involve numerous phishing cues. Such a phishing scam can be detected with minimal cognitive demand because its multiple cues are readily identifiable. In contrast, a phishing email with low cue saliency will have few cues and consequently be harder to recognize; identifying such phishing attempts requires more mental exertion, inevitably leading to inefficiency in antiphishing training performance (Jaeger & Eckhardt, 2021;

Kanfer & Ackerman, 1989). In general, the discussion mentioned previously leads us to expect that phishing cue saliency will be positively associated with detection accuracy.<sup>2</sup>

H5b: Phishing cue saliency positively influences detection accuracy.

We predicted earlier that phishing cue saliency would significantly impact detection accuracy. We further proposed that feedback quantity would moderate the effect of phishing cue saliency on antiphishing performance. If individuals are given little examplebased feedback (i.e., low-quantity feedback), the level of cue saliency in an email is not a major issue for antiphishing performance. The reason for this is that when individuals have limited knowledge of how to detect phishing cues, they are likely to focus only on the key signals they are trained to focus on and exclude other potentially important cues. Put differently, for those with a minimal set of antiphishing tips, it is cognitively demanding to identify peripheral phishing cues that lie outside the realm of procedural knowledge in their mental representation (Kanfer & Ackerman, 1989; Lam et al., 2011).

In contrast, when considerable example-based feedback is given (i.e., high-quantity feedback), this type of information is expected to facilitate the accumulation of antiphishing tips in the form of procedural knowledge. Such abundant tips are more likely to correspond to some of the phishing cues present in a phishing email. Accordingly, when individuals have plenty of knowledge on how to detect phishing cues, the level of cue saliency in an email will exert a larger impact on detection accuracy. In this condition of high-quantity feedback, even peripheral cues can be identified more easily with little cognitive overload (Lam et al., 2011; Tseng et al., 2019). As a result, the effects of phishing cue saliency on detection accuracy will be stronger with high-quantity information than with low-quantity information. 3 Thus, we hypothesize:

H6b: There will be an interaction effect between the quantity of example-based feedback and phishing cue saliency on detection accuracy such that in the context of link-embedded emails, the positive effect of phishing cue saliency will be stronger under the high feedback quantity condition than under the low feedback quantity condition.

## 4 Methods

Table 2 summarizes four experiments we conducted to test our research hypotheses. Experiment 1 examined the effects of feedback type (mindful vs. examplebased) on decision avoidance and detection accuracy (H1). Experiment 2 tested the effects of perceived detection efficacy (H2) and its interaction with feedback type (H3). Experiment 3 investigated the roles of feedback quantity (H4) and phishing cue saliency (H5) as well as their interaction effect (H6). These three experiments focused on link-embedded emails. In contrast, Experiment 4 was a supplementary study to further investigate the effects of feedback type for different email types (i.e., no-link-embedded emails vs. link-embedded emails).

To conduct the experiments, we created web-based surveys and phishing quizzes (Wang et al., 2016, 2017). For each experiment, we first introduced phishing emails as malicious emails trying to steal personal information and invited subjects to participate in phishing quizzes. Our four experiments followed similar procedures, as shown in Figure 2. All participants were required to complete a preliminary phishing test that included email quizzes. In the preliminary test, participants read two emails and indicated their judgments about each email (phishing; legitimate; skip the question/I do not know if it is a phishing message). Next, we presented different feedback materials to different groups of participants. After the preliminary test, participants were asked to complete the main phishing test, which now included a series of new email quizzes and message-level survey questions (e.g., perceived detection efficacy). Finally, participants completed a survey questionnaire to measure several control variables, such as coping responses.

We designed the emails in the phishing quizzes using Qualtric’s “text and graphic” type of question with HTML code modifications. Specifically, we modified the HTML code for the URL links to ensure the participants could hover their mouse over each link to see the underlying URL address but could not click on the link to be directed to the actual website page. This design allowed participants to read the texts and graphics in the emails and to interact with the links as they would in their mailboxes while keeping them within the survey during the experiment. We also presented the feedback material using the “text and graphic” type of question.

Table 2. Summary of Experiments

<table><tr><td colspan="2"></td><td>Experiment 1</td><td>Experiment 2</td><td>Experiment 3</td><td>Experiment 4</td></tr><tr><td colspan="2">Hypothesis</td><td>H1</td><td>H2, H3</td><td>H4, H5, H6</td><td>Post hoc</td></tr><tr><td colspan="2">Design</td><td>Single-factor between-subjects design</td><td>Single-factor repeated-measures design</td><td>2 × 2 mixed design</td><td>2 × 2 between-subjects design</td></tr><tr><td colspan="2">Subject</td><td>Amazon Mechanical Turk (n = 130)</td><td>Esearch.com (n = 110)</td><td>Amazon Mechanical Turk (n = 274)</td><td>Clickworker.com (n = 138)</td></tr><tr><td colspan="2">Dependent variable</td><td colspan="4">Decision avoidance (0: decision making, 1: decision avoidance)Detection accuracy (-1: incorrect, 0: skipping/I do not know if it is a phishing message, 1: correct)</td></tr><tr><td rowspan="2">Individual level IV</td><td>Manipulated</td><td>Feedback type (example-based vs. mindful)</td><td>Feedback type (example-based vs. mindful)</td><td>Feedback quantity (low vs. high)</td><td>Feedback type (example-based vs. mindful)Email type (link-embedded vs. no-link-embedded)</td></tr><tr><td>Measured</td><td colspan="4">Age, gender, prior phishing experience, average email load, preliminary training detection accuracy, task-focused coping, emotion-focused coping, avoidance coping</td></tr><tr><td rowspan="2">Message level IV</td><td>Manipulated</td><td>NA</td><td>NA</td><td>Phishing cue saliency (Low vs. high)</td><td>NA</td></tr><tr><td>Repeatedly measured</td><td>NA</td><td>Perceived detection efficacyResponse time</td><td>Perceived detection efficacyResponse time</td><td>NA</td></tr><tr><td colspan="2">Analytical methods</td><td>ANCOVA</td><td>Generalized estimating equation</td><td>Generalized estimating equation</td><td>ANCOVA</td></tr></table>

Figure 2. Experimental Procedure  
![](/api/attachments/FAU6CSDY/fulltext/images/6c8e801b7b99de57374b28dc1a7d0394d6856fd41713e5dfc19cc2d52b172616.jpg)

We targeted individuals older than 18 in the United States from three different online panels via Amazon Mechanical Turk, Esearch.com, and Clickworker.com. We conducted Experiments 1 and 3 using Amazon Mechanical Turk workers, Experiment 2 with Esearch.com participants, and Experiment 4 with Clickworker.com participants. Using different online panels allowed us to involve potential participants with diverse backgrounds.

We followed several procedures for ensuring data quality in online-panel studies (Dincelli & Smith, 2020; Lowry et al., 2016): (1) we implemented the “prevent ballot box stuffing” tool in Qualtrics and also removed responses with the same IP address, location, or the same birthdate with similar start times to ensure the participants took the survey only once and independently; (2) we checked the locations based on IP address and location longitude/latitude to exclude participants outside the United States; (3) we deleted participants who did not complete the entire experiment and those who did not provide valid answers to the survey questions (e.g., invalid birthdate); and (4) we informed participants, as a way to focus their attention on the test, that they would earn a base rate and then could earn extra incentives based on their performance on the main phishing test. In Experiment 4, in addition to prior procedures, we also implemented more rigorous procedures, including (1) enabling the Captcha question, bot detection tool, and RelevantID technology in Qualtrics to prevent bots and cheaters; (2) ensuring participants were relatively novel learners in this type of antiphishing training by screening out participants who reported that they had taken similar phishing quizzes before; and (3) screening out participants who did not pass the instructional manipulation check (Marett, 2015; Oppenheimer et al., 2009) to ensure the participants paid attention to the instructions and survey questions.

The details of the methods and results will be described for each experiment. Appendix B presents all the measurement items; Appendix C shows examples of feedback, phishing emails, and legitimate emails from the experiments.

## 4.1 Experiment 1

Experiment 1 tested the relative effectiveness between example-based feedback and mindful feedback (H1) in the context of link-embedded emails. This experiment used a single factor (feedback type: mindful vs. example-based) between-subjects design.

## 4.1.1 Treatment

Two survey websites were customized for our manipulation of the type of feedback (mindful vs. example-based), and the participants were randomly assigned to one of the two survey websites. Specifically, as mentioned before, participants were asked to complete a preliminary phishing test, including one legitimate email and one phishing email. Participants were required to indicate their decisions about each email (phishing; legitimate; skip the question). After the preliminary test, participants in each group were shown different feedback. For example-based feedback, we presented the prior phishing email with the fake URL address next to its fake link and explicitly taught participants how to detect the fake link within the email. For mindful feedback, we showed participants feedback adapted from the existing mindfulness training material (Jensen et al., 2017; Nguyen et al., 2021a). It reminded participants to be cautious with email links and to think more about the email’s requirements before acting on the email. Appendix C shows the feedback materials in the test.

## 4.1.2 Sample

We collected data on Amazon Mechanical Turk (MTurk), a crowdsourcing website where researchers can access many potential participants with diverse backgrounds. We recruited MTurk workers who were at least 18 years old and in the United States. To ensure data quality, we followed a rigorous data-cleaning procedure, as mentioned in the general description of the experiments. Sixteen participants did not complete the experiment. The final sample consisted of 130 participants. To examine nonresponse bias, we compared the age, gender, prior phishing experience, average email load, and preliminary training detection accuracy of the 16 excluded respondents (if they provided the data) with the responses of those who completed the experiment. The results show no significant differences between the two groups, suggesting that nonresponse bias is not an issue.

We also conducted a power analysis using G\*Power 3.1 (Faul et al., 2007). A sample size of 128 is sufficient to identify a medium effect size (Cohen’s f =

0.25) with a power of 0.80 at a significance level of 0.05 (Cohen, 1988, 1992). The average age of the participants was 35.63, and 47.69% of participants were female.<sup>4</sup>

## 4.1.3 Experimental Procedures

At the beginning of the experiment, we introduced phishing emails as malicious emails trying to steal personal information and invited participants to participate in phishing quizzes. After the introduction, participants were asked to complete a preliminary phishing test, including one legitimate email and one phishing email in random order. The participants were asked to indicate their decisions about each email (phishing; legitimate; skip the question). Then, they were provided with one of the two types of feedback (i.e., mindful or example-based).

After reading the feedback, all participants completed the main phishing test, including six new email quizzes. The participants were asked to report their decisions about each email’s legitimacy. To keep participants attention, we informed them that they would gain \$1 as a base rate, earn an extra \$0.05 for each correct answer, lose an extra \$0.05 for each wrong answer, and get no additional incentive for skipping the answer in the main test. Specifically, all participants were exposed to three legitimate emails and three phishing emails in random order. Finally, to measure our control variables, we asked participants about their coping responses (taskfocused, emotion-focused, and avoidance) and collected demographic information.

## 4.1.4 Measures

The dependent variables, decision avoidance, and detection accuracy, were measured based on participants’ objective performance on the phishing test. To measure decision avoidance, we coded participants’ answers on each email quiz as 1 if they chose “skip the question” and 0 if they made a decision. In addition, we coded wrong answers on each quiz as -1, correct answers as 1, and skipped answers as 0 to measure detection accuracy.

We included participants’ coping responses as control variables because Wang et al. (2017) showed that these responses had direct impacts on antiphishing performance in a similar phishing test. Based on Wang et al. (2017), we measured three types of coping responses—task-focused, emotion-focused, and avoidance. Finally, as controls, we also measured demographic information such as participants’ prior phishing experience, average email load, age, and gender.

## 4.1.5 Manipulation Check

We conducted a pilot study on Amazon Mechanical Turk to test whether individuals in the mindful feedback group perceived that the feedback required more thinking in terms of detecting phishing emails compared with those in the example-based group.<sup>5</sup> We implemented a mixed design with the presentation order of the type of feedback as the between-subjects factor and the type of feedback itself as the withinsubjects factor. After completing the same preliminary phishing test as in the main experiment, each participant was presented with mindful and examplebased feedback in random order. After they read each type of feedback, participants reported their degrees of agreement on a 7-point Likert scale to the items: “For detecting phishing emails, the previous education requires a lot of thinking/cognitive effort.” There were 133 valid responses, and we then conducted a mixed ANOVA. A significant difference existed in the ratings of the manipulation-check question after reading different feedback $( F _ { ( 1 , ~ 1 3 1 ) } = 1 6 . 8 3 , p < 0 . 0 0 1 )$ . The effect size $( f = 0 . 1 4 )$ fell between the conventional small to medium effect size. The presentation order did not significantly affect the ratings. The pairwise comparison shows that participants perceived that example-based feedback required less thinking than mindful feedback $( d i f = - 0 . 4 5 , t _ { ( 1 3 2 ) } = - 4 . 1 2 , p < 0 . 0 0 1 )$ .

## 4.1.6 Results and Discussion

We analyzed the impact of feedback type on decision avoidance and detection accuracy using an analysis of covariance (ANCOVA). For ANCOVA, we aggregated the scores of the six email quizzes in the main test for decision avoidance and detection accuracy, respectively. Thus, decision avoidance ranged from 0 to 6, and detection accuracy ranged from - 6 to + 6. Table 3 shows the results of the ANCOVA.

After controlling for other variables, the results showed a significant difference between the mean decision avoidance of the example-based feedback group and that of the mindful feedback group $( F _ { ( 1 , 1 2 0 ) } = 4 . 2 8 , p <$ 0.05). In comparing the estimated marginal means, we found that participants in the example-based feedback group showed less decision avoidance $( M = 0 . 1 5 )$ than those in the mindful feedback group $( M ~ = ~ 0 . 4 6 )$ suggesting support for H1a. The effect size (partial $\eta ^ { 2 } =$ 0.034 or $f = 0 . 1 9 )$ was between the small and medium effect sizes (0.10 and 0.25) suggested by Cohen (1988). It indicates that 3.4% of the total variance of the decision avoidance score was due to the membership of the feedback group after excluding the portion of the variance linearly associated with the covariates.

In addition, a significant difference was found between the mean detection accuracy of the mindful feedback group and that of the example-based feedback group $( F _ { ( 1 , 1 2 0 ) } = 3 6 . 3 4 , p < 0 . 0 0 1 )$ after controlling for control variables. In comparing the estimated marginal means, we found that the example-based feedback group had a higher detection accuracy (M = 4.10) than the mindful feedback group $( M = 1 . 2 8 )$ , suggesting support for H1b. The effect size (partial $\eta ^ { 2 } = 0 . 2 3 2 \ \mathrm { o r } f = 0 . 5 5 )$ surpassed a large effect size of $f = 0 . 4 0$ (Cohen, 1988). The variance caused by the membership of the feedback group accounted for 23.2% of the total variance of the detection accuracy score after excluding the portion of its variance linearly associated with the covariates.

Table 3. Experiment 1: ANCOVA Results for Decision Avoidance and Detection Accuracy

<table><tr><td rowspan="2"></td><td colspan="4">Decision avoidance</td><td colspan="4">Detection accuracy</td></tr><tr><td>Mean square</td><td>F</td><td>p-value</td><td>Effect size (partial η2)</td><td>Mean square</td><td>F</td><td>p-value</td><td>Effect size (partial η2)</td></tr><tr><td>Manipulation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FT (H1)</td><td>2.99</td><td>4.28</td><td>.041</td><td>.034</td><td>244.41</td><td>36.34</td><td>&lt; .001</td><td>.232</td></tr><tr><td>Control variables</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Age</td><td>.05</td><td>.07</td><td>.799</td><td>.001</td><td>1.77</td><td>.26</td><td>.609</td><td>.002</td></tr><tr><td>GEN</td><td>.12</td><td>.18</td><td>.674</td><td>.001</td><td>.14</td><td>.02</td><td>.885</td><td>.000</td></tr><tr><td>PPE</td><td>.26</td><td>.38</td><td>.541</td><td>.003</td><td>.20</td><td>.03</td><td>.862</td><td>.000</td></tr><tr><td>AEL</td><td>.29</td><td>.42</td><td>.518</td><td>.003</td><td>34.91</td><td>5.19</td><td>.024</td><td>.041</td></tr><tr><td>PTDA</td><td>.74</td><td>1.06</td><td>.306</td><td>.009</td><td>14.19</td><td>2.11</td><td>.149</td><td>.017</td></tr><tr><td>TC</td><td>1.14</td><td>1.63</td><td>.204</td><td>.013</td><td>21.59</td><td>3.21</td><td>.076</td><td>.026</td></tr><tr><td>EC</td><td>.36</td><td>.52</td><td>.472</td><td>.004</td><td>4.80</td><td>.71</td><td>.400</td><td>.006</td></tr><tr><td>AC</td><td>1.06</td><td>1.52</td><td>.220</td><td>.013</td><td>3.24</td><td>.48</td><td>.489</td><td>.004</td></tr><tr><td>Model fit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>R2</td><td colspan="4">.066</td><td colspan="4">.306</td></tr><tr><td>Adjusted R2</td><td colspan="4">-.004</td><td colspan="4">.254</td></tr></table>

Note: FT = feedback type (mindful = 0, example-based = 1); GEN = gender (male = 0, female = 1); PPE = prior phishing experience; AEL = average email load; PTDA = preliminary training detection accuracy; TC = task-focused coping; EC = emotion-focused coping; AC = avoidance coping

same design of feedback materials as those used in Experiment 1.

Finally, we performed the variance inflation factor (VIF) test to examine potential multicollinearity among the variables. The VIFs of all the variables ranged from 1.03 (prior phishing experience) to 1.69 (task-focused coping) and were well below 3.33. The result indicates that multicollinearity was not an issue.

## 4.2 Experiment 2

Experiment 2 examined the impacts of perceived detection efficacy on decision avoidance and detection accuracy (H2a and H2b), as well as the interaction effect between feedback type (mindful vs. examplebased) at the individual level and perceived detection efficacy at the message level on detection accuracy (H3b) in the context of link-embedded emails.

## 4.2.1 Treatment

The feedback materials in Experiment 2 were consistent with those in Experiment 1. We created two survey websites to manipulate feedback type (mindful vs. example-based) and randomly assigned the participants to one of the two survey websites. All participants were exposed to two phishing emails in random order in a preliminary test and were required to indicate their decisions about each email. After each quiz, we provided the answers (i.e., if their decisions about the emails were correct) to the participants, followed by the type of feedback they were assigned to. For the mindful feedback, we used the same feedback material as in Experiment 1. For the example-based feedback, we showed the image of each phishing email and how to detect the fake link within each phishing email. The feedback design was consistent with the one used in Experiment 1, except that we used different phishing emails.

## 4.2.2 Sample

We conducted Experiment 2 by inviting potential participants via email from a US-based online panel maintained by an online marketing research company (Esearch.com). We followed the data-cleaning procedure stated in the general description of the experiments. Thirty-seven participants did not finish the experiment. The final valid sample consisted of 110 participants. None of the participants who dropped out answered the demographic questions in the post survey. Thus, we compared their preliminary training detection accuracy with the complete sample to test nonresponse bias. There was no significant difference between the two groups, suggesting that nonresponse bias was not a problem. The sample size of the final sample was enough to achieve a medium effect size (Cohen’s $d = 0 . 5 0 )$ (Cohen, 1988, 1992; Faul et al., 2009). The average age was 46.44, and 47.27% of participants were female.

## 4.2.3 Experimental Procedures

We invited the participants to take part in phishing quizzes. The participants were then required to take a preliminary test, including two phishing emails, and indicate their decisions about each email. Afterward, they received the answers to each quiz and the feedback material they were assigned. After they read the feedback, all participants were asked to complete the main test, including four new email quizzes. To focus their attention, we also informed them that they would get a base rate (\$1.3). In addition, they would earn an extra \$0.05 for each correct answer, lose an extra \$0.05 for each wrong answer, and get no additional incentive for skipping the answer. The quizzes were chosen from those used in Experiment 1. Specifically, all participants were exposed to three legitimate emails and one phishing email in random order. Besides answering each quiz, they were also asked to report their perceived detection efficacy for each email quiz. Lastly, we asked participants about their coping responses and collected demographic information.

## 4.2.4 Measures

We measured decision avoidance, detection accuracy, coping responses, and other demographic variables using the same method as in Experiment 1. Additionally, we measured perceived detection efficacy for each email quiz in the main phishing test using four items such as “It is possible to determine whether the email is phishing” and “It is feasible to determine whether the email is phishing” (Bagozzi et al., 2003b; Dutton & Webster, 1988). We also recorded the time each participant spent on each quiz in the main test using the survey website as a message-level control variable.

## 4.2.5 Construct Validation

We performed a confirmatory factor analysis to examine the quality of our measurement items. Appendix D presents the descriptive statistics for all research variables and the results of construct validation. We examined composite reliability, and the scores for all measures exceeded the cutoff value of 0.70, indicating satisfactory reliability (Bagozzi & Yi, 1988). We tested convergent validity through item loadings and average variance extracted (AVE). All measurement items loaded significantly on the assigned construct (p < 0.001), and all scores of AVEs exceeded the cutoff value of 0.50 (Fornell & Larcker, 1981). All the measures showed satisfactory convergent validity. We also used chi-square tests to examine discriminant validity by comparing a series of model pairs (Segars & Grover, 1998). The chi-square difference tests were all significant, suggesting the satisfactory discriminant validity of our measures. We also compared the AVE for each construct to its correlations with other constructs (Gefen & Straub, 2000). For each construct, the AVE was greater than its correlations with other constructs, indicating discriminant validity.

Table 4. Experiment 2: GEE Results for Decision Avoidance and Detection Accuracy

<table><tr><td rowspan="2"></td><td colspan="5">Decision avoidance</td><td colspan="5">Detection accuracy</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td></tr><tr><td>Intercept</td><td>-4.33***</td><td>-4.55***</td><td>-6.86***</td><td>-8.90***</td><td>-9.27***</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Threshold</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-1.00|0.00</td><td></td><td></td><td></td><td></td><td></td><td>-.89***</td><td>-.91***</td><td>-.92***</td><td>-.94***</td><td>-.94***</td></tr><tr><td>0.00|1.00</td><td></td><td></td><td></td><td></td><td></td><td>-.80***</td><td>-.81***</td><td>-.82***</td><td>-.84***</td><td>-.84***</td></tr><tr><td>Level 2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Manipulation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FT</td><td>-2.11†</td><td>-1.74</td><td>-2.03†</td><td>-2.57*</td><td>-3.58*</td><td>-.71**</td><td>-.69**</td><td>-.65**</td><td>-.65**</td><td>-.71**</td></tr><tr><td>Individual factors</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Age</td><td></td><td></td><td></td><td>.76</td><td>.76</td><td></td><td></td><td></td><td>-.04</td><td>-.05</td></tr><tr><td>GEN</td><td></td><td></td><td></td><td>3.26</td><td>3.18</td><td></td><td></td><td></td><td>.24</td><td>.22</td></tr><tr><td>PPE</td><td></td><td></td><td></td><td>1.01</td><td>.94</td><td></td><td></td><td></td><td>.16</td><td>.14</td></tr><tr><td>AEL</td><td></td><td></td><td></td><td>-.37</td><td>-.35</td><td></td><td></td><td></td><td>.01</td><td>.01</td></tr><tr><td>PTDA</td><td></td><td></td><td></td><td>-.57</td><td>-.57</td><td></td><td></td><td></td><td>.02</td><td>.01</td></tr><tr><td>TC</td><td></td><td></td><td>.97</td><td>1.19</td><td>1.19</td><td></td><td></td><td>.12</td><td>.10</td><td>.10</td></tr><tr><td>EC</td><td></td><td></td><td>.56</td><td>.45</td><td>.44</td><td></td><td></td><td>.00</td><td>.01</td><td>-.02</td></tr><tr><td>AC</td><td></td><td></td><td>1.58***</td><td>2.11***</td><td>2.09***</td><td></td><td></td><td>.19†</td><td>.14</td><td>.13</td></tr><tr><td>Level 1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PDE (H2)</td><td></td><td>-.95*</td><td>-1.94***</td><td>-2.67***</td><td>-2.87***</td><td></td><td>-.23*</td><td>-.27*</td><td>-.28*</td><td>-.31*</td></tr><tr><td>RT</td><td></td><td></td><td></td><td>.14</td><td>.10</td><td></td><td></td><td></td><td>.03</td><td>.03</td></tr><tr><td>Interaction</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FT * PDE (H3b)</td><td></td><td></td><td></td><td></td><td>-.56</td><td></td><td></td><td></td><td></td><td>.41†</td></tr><tr><td>Model fit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>QIC</td><td>85.50</td><td>83.52</td><td>72.40</td><td>153.70</td><td>155.10</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>QICC</td><td>85.60</td><td>83.61</td><td>72.70</td><td>154.60</td><td>156.10</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Wald statistics</td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>3.92*</td><td>3.91</td><td>2.55</td><td>3.01†</td></tr><tr><td>df</td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>1</td><td>3</td><td>6</td><td>1</td></tr></table>

Note: Individual level: n = 110; message level: n = 440. \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, † p < 0.10 (two-tailed). For model fit, QIC and QICC were used for decision avoidance, and Wald statistics were used for detection accuracy. For GEE with ordinal outcomes, a negative (positive) sign indicates a positive (negative) effect on the outcome variable. FT = feedback type (mindful = 0, example-based = 1); GEN = gender (male = 0, female =1); PPE = prior phishing experience; AEL = average email load; PTDA = preliminary training detection accuracy; TC = task-focused coping; EC = emotion-focused coping AC = avoidance coping; PDE = perceived detection efficacy; RT = response time to each quiz

## 4.2.6 Generalized Estimating Equations

Our data contained repeated measures of dichotomous outcomes (decision avoidance) and ordinal outcomes (detection accuracy) nested within individuals, along with repeated measures of perceived detection efficacy, response time, and individual-level control variables. Generalized estimating equations (GEE) provided the means to analyze the repeated ordinal/dichotomous outcomes nested within individuals.

We analyzed the two dependent variables separately. Table 4 presents the results of the GEE for decision avoidance and detection accuracy, respectively. For each dependent variable, we built five alternative models. Model 1 includes only the individual-level treatment variable (i.e., feedback type). Model 2 includes the treatment variable and the message-level variable (i.e., perceived detection efficacy). Model 3 includes coping responses as control variables. Model 4 includes all other control variables. Finally, Model 5 includes the interaction term between feedback type and perceived detection efficacy.

For decision avoidance, we calculated model fit indices such as quasi-likelihood under the independence model criterion (QIC) and corrected quasi-likelihood under the independence model criterion (QICC) to compare the model fit. As shown in Models 1-3, the model fit better when we added perceived detection efficacy and coping responses. However, except for coping responses, other control variables did not significantly affect decision avoidance and did not increase the model fit. However, we kept all the control variables to explicitly partial out their effects. The results in Model 4 show that perceived detection efficacy was significantly and negatively associated with decision avoidance (-2.67, $p < 0 . 0 0 1 )$ ), supporting H2a. Holding other variables constant, when perceived detection efficacy increased by one standard deviation, the odds ratio of decision avoidance (i.e., skipping) was multiplied by 0.07 (e $^ { 2 . 6 7 } )$ , indicating a dramatic decrease in the probability of decision avoidance. The effect size of perceived detection efficacy corresponded to a Cohen’s d of 1.62 (Cox, 1970; Sánchez-Meca, 2003), which exceeded the conventional large effect size of $d = 0 . 8 0$ (Cohen, 1988). We did not hypothesize an interaction effect between feedback type and perceived detection efficacy, and Model 5 shows that the interaction effect between feedback type and perceived detection efficacy was not significant.

For detection accuracy, Wald tests were performed to compare the nested models consecutively. As presented in Table 4, adding the control variables did not improve the model fit, but we kept the control variables for the same reason as mentioned before. We chose Model 5 as the final model for hypothesis testing. As shown in Model 5, perceived detection efficacy was significantly and positively associated with detection accuracy $( \ - 0 . 3 1 , p < 0 . 0 5 )$ , supporting H2b. The result indicates that holding other variables constant, when perceived detection efficacy increased by one standard deviation, the odds ratio of being less accurate (being incorrect vs. skipping or being correct/being incorrect or skipping vs. being correct) was multiplied by $0 . 7 3 ( \mathrm { e } ^ { - 0 . 3 1 } )$ , averaged across feedback type. The average effect size of perceived detection efficacy corresponded to a Cohen’s d of 0.19, which approached the conventional small effect size of $d = 0 . 2 0$ . The interaction effect between feedback type and perceived detection efficacy was marginally significant (-0.41, $p \ = \ 0 . 0 8 )$ , and thus H3b was marginally supported. The effect of perceived detection efficacy was stronger for individuals receiving example-based feedback than for those receiving mindful feedback. In the example-based feedback group, when perceived detection efficacy increased by one standard deviation, the odds ratio of being less accurate was multiplied by $0 . 6 0 \ ( \mathrm { e } ^ { - 0 . 5 1 5 } )$ corresponding to a Cohen’s d of 0.31 (i.e., between the conventional small and medium effect sizes); in the mindful group, the odds ratio of being less accurate was multiplied by $0 . 9 0 \quad ( \mathrm { e } ^ { - 0 . 1 0 5 } ) .$ which only corresponded to a Cohen’s d of 0.06.

![](/api/attachments/FAU6CSDY/fulltext/images/b621bbea693dfa48ac3f814e2663075a6eb20f5f7add58fd430888882f840e75.jpg)

Lastly, we also performed a VIF test to assess multicollinearity among all the variables in our proposed models. The VIFs of all the variables ranged from 1.06 (feedback type) to 1.44 (task-focused coping) and were below 3.33. The result indicates that multicollinearity was not a concern.

Figure 3 depicts the interaction plots for decision avoidance and detection accuracy. For decision avoidance, the change in the probability of skipping a quiz from low to high perceived detection efficacy does not differ between the example-based feedback group and the mindful feedback group. For detection accuracy, as perceived detection efficacy increases, the probability of correctly answering a quiz becomes much higher in the example-based feedback group than in the mindful feedback group. In summary, we conclude that perceived detection efficacy reduces decision avoidance and increases detection accuracy.

## 4.3 Experiment 3

We conducted Experiment 3 to test H4, H5b, and H6b. We used a 2×2 mixed design with feedback quantity (low vs. high) as the between-subjects factor and phishing cue saliency (low vs. high) as the withinsubjects factor to study how people’s decision avoidance and detection accuracy for various emails would differ when receiving different levels of feedback quantity.

![](/api/attachments/FAU6CSDY/fulltext/images/66b687503a63f1ee7bbe65fd57cd410a88a7c93cbd4665d4e1c918a375f5f28a.jpg)  
Note: Perceived detection efficacy is categorized as high (low) when the value is above (below) the mean. The probability of skipping and the probability of being correct were estimated based on the results of GEE  
Figure 3. Experiment 2: Interaction between Feedback Type and Perceived Detection Efficacy

## 4.3.1 Treatment

For feedback quantity, as in the prior experiments, participants had to complete a preliminary phishing test that included two email quizzes in random order. After the preliminary test, participants were randomly assigned to the two levels of feedback quantity. In both the low and high feedback quantity groups, we used a real phishing email different from any previous test to inform participants of some phishing cues and antiphishing techniques. Specifically, for low feedback quantity, we presented the phishing email and showed only how to detect the fake link within this email. We used the same phishing email for high feedback quantity, but this time we informed the participants of several phishing cues, such as fake links, fake email domains, and general greetings, and also explained other phishing techniques, such as using an urgent tone. Appendix C shows the details of the feedback design.

For phishing cue saliency, in the main test, three emails were in the low phishing cue saliency group. The other three were in the high phishing cue saliency group (two phishing emails and one legitimate email in each group). All participants had to complete the six quizzes. We manipulated phishing cue saliency for phishing emails by varying the number of phishing cues. For a phishing email with low phishing cue saliency, the email was modeled on the alleged sender’s genuine email. The only phishing cue was the fake link. For an email with high phishing cue saliency, in addition to the fake link, the email contained a suspicious email domain as well as one of the following cues: an urgent tone, minor grammatical errors, or a general greeting. The underlying assumption of the latter email was that the more phishing cues it contained, the likelier people would be to notice at least some of the cues and recognize the phishing email.

## 4.3.2 Sample

We conducted Experiment 3 by inviting participants from MTurk. The participants had to be at least 18 years old and be in the United States. We followed the same data-cleaning procedure as in Experiments 1 and 2. Seventy-one participants did not complete the experiment. The final sample consisted of 295 participants. To test nonresponse bias, we compared the dropouts’ preliminary training detection accuracy, age, gender, prior phishing experience, and average email load (if they provided the data) with the complete sample. No significant differences existed, suggesting that nonresponse bias was not a problem. Following the same procedures of power analysis as in Experiment 2, we also ran a power analysis for Experiment 3. This sample size is sufficient to achieve a medium effect size (Cohen’s d = 0.50) (Cohen, 1988, 1992; Faul et al., 2009). The average age was 38.17, and 50.51% of participants were female.

## 4.3.3 Experimental Procedures

As in the prior experiments, we invited participants to take phishing quizzes. Participants were asked to complete a preliminary phishing test that included two email quizzes in random order. We also provided them with the answers to each email quiz. Afterward, participants received their assigned feedback. We then conducted a manipulation check.

After the manipulation check, all participants were asked to complete the main phishing test of six email quizzes in random order. As mentioned earlier, three emails were in the low phishing cue saliency group, and the others were in the high phishing cue saliency group. Like previous experiments, they were told that they would get a base rate (\$1.50) and would gain or lose extra money based on their performance (i.e., earn an extra \$0.01 for a correct answer, lose \$0.01 for a wrong answer and get no additional incentive for a skipped answer). After each quiz, we also asked participants for their perceived detection efficacy. We also recorded the time they spent on each email. Lastly, we asked participants the same questions to measure the individual-level control variables as in the prior experiments.

## 4.3.4 Measures

We measured decision avoidance, detection accuracy, perceived detection efficacy, coping responses, response time, and other demographic variables using the same approach as in Experiment 2.

## 4.3.5 Manipulation Check

We asked participants about the number of tips (one tip or many tips) in their assigned feedback to check if a difference existed in the perceptions of feedback quantity between the low and high feedback quantity groups. Results of a chi-square test indicated a significant difference in the proportional distribution of choice of tip numbers between the high-quantity group and the low-quantity group $( \chi ^ { 2 } _ { ( 1 , ~ 2 9 5 ) } = 2 1 5 . 0 3 , p <$ 0.001). The effect size $( w ~ = ~ 0 . 8 5 )$ exceeded the conventional large effect size of $w = 0 . 5 0 $ , suggesting a strong association between the choice of tip numbers and the feedback group membership. The proportion of participants for the low-quantity group—many tips, the high-quantity group—many tips, the low-quantity group—one tip, and the high-quantity group—one tip were 0.06, 0.52, 0.41, and 0.01, respectively. The results suggest our manipulation of feedback quantity was successful. Twenty-one participants failed the manipulation check. We excluded them from the subsequent analysis. We did not ask questions about phishing cue saliency for each email message for these reasons: (1) The questions might have drawn participants’ attention to phishing cues, thus distorting their perceptions and decisions about the emails (Hauser et al., 2018; Kühnen, 2010); (2) phishing cue saliency represents one of the objective phishing characteristics or the intrinsic nature of email messages, and the significant influence of phishing cue saliency on detection accuracy provided evidence of successful manipulation (Gruijters, 2022; O’Keefe, 2003; Sigall & Mills, 1998). As a result, the final data set consisted of 274 participants. The average age was 38.36, and 51.09% of participants were female.

## 4.3.6 Construct Validation

As in Experiment 2, we performed a confirmatory factor analysis, including all the 14 research variables in our model, to examine the quality of our measurement items. Appendix D shows the descriptive statistics for all research variables and the results of construct validation. All the constructs showed satisfactory reliability, convergent validity, and discriminant validity.

## 4.3.7 Generalized Estimating Equations

We tested H4, H5b, and H6b using generalized estimating equations to accommodate the hierarchical nature of our data. We analyzed the two dependent variables separately. Table 5 shows the results of GEE for decision avoidance and detection accuracy, respectively. We built four alternative models for each dependent variable. Model 1 included the individualand message-level treatment variables (i.e., feedback quantity and phishing cue saliency). Model 2 included the treatment variables and all control variables. Model 3 included perceived detection efficacy and all the prior variables. Model 4 further included the interaction term between feedback quantity and phishing cue saliency.

We calculated QIC and QICC for decision avoidance. In Table 5, Model 3 showed the best model fit. The control variables did not significantly affect decision avoidance, but we kept them in our model to explicitly partial out their effects. The results of Model 3 show that feedback quantity did not have a significant main impact on decision avoidance $( 0 . 0 1 , p = \mathrm { n s } )$ , and thus H4a was not supported. The results of Model 3 also indicate that phishing cue saliency did not affect decision avoidance. However, perceived detection efficacy was significantly associated with decision avoidance $( - 1 . 8 4 , p < 0 . 0 0 1 )$ Holding other variables constant, when there was a onestandard-deviation increase in perceived detection efficacy, the odds ratio of decision avoidance was multiplied by $0 . 1 6 ( \mathrm { e } ^ { - 1 . 8 4 } )$ . The effect corresponded to a Cohen’s d of 1.12, which exceeds the conventional large effect size. This was consistent with our expectation that decision avoidance is influenced by an individual’s subjective evaluation of the task at hand. We did not hypothesize that there would be an interaction effect between feedback quantity and phishing cue saliency on decision avoidance. Model 4 also shows that the interaction effect was not significant.

For detection accuracy, as Table 5 shows, we used Wald tests to compare model fit. The model fit continued to improve as we added more research variables. In Model 3, the effect of feedback quantity barely reached a significance level of 0.05 (0.33, $p = 0 . 0 4 8 )$ . However, as shown in Model 4, this effect was replaced by a significant interaction effect between feedback quantity and phishing cue saliency $( - 0 . 5 9 , p = 0 . 0 1 )$ . Thus, while H4b was not supported, H6b was supported. The results of Model 4 also indicate a significant positive impact of phishing cue saliency on detection accuracy $( \ - 0 . 8 4 , p <$ 0.001), suggesting support for H5b.

As noted before, feedback quantity did not have a main impact on detection accuracy but moderated the effect of phishing cue saliency. This suggests the impact of phishing cue saliency was stronger under the high feedback quantity condition than under the low-quantity condition. Holding all other variables constant, the odds ratio of being less accurate for the messages with high phishing cue saliency was $0 . 4 3 ( \mathrm { e } ^ { - 0 . 8 4 } )$ times the odds ratio of being less accurate for the email messages with low phishing cue saliency, averaged across feedback quantity levels. The average effect size of phishing cue saliency equals a Cohen’s d of 0.51, approximately the conventional medium effect size. For individuals receiving low feedback quantity, the odds ratio of being less accurate for the messages with high phishing cue saliency was 0.58 $( \mathrm { e } ^ { - 0 . 5 4 5 } )$ times the odds ratio for the messages with low cue saliency, which equals a Cohen’s d of 0.33 (i.e., between the small and medium effect size). For those receiving high feedback quantity, the odds ratio of being less accurate for the messages with high phishing cue saliency was only $0 . 3 2 ( \mathrm { e } ^ { - 1 . 1 3 5 } )$ times the odds ratio for the messages with low cue saliency, which equals a Cohen’s d of 0.69 (i.e., surpassing the medium effect size). We calculated the values of the VIF for all the variables. The VIF values were below 3.33 and ranged from 1.01 (phishing cue saliency) to 1.42 (avoidance coping), suggesting multicollinearity was not a problem.

Figure 4 also presents the interaction plots for decision avoidance and detection accuracy. For decision avoidance, the probability of skipping a quiz is around 2%, regardless of the level of feedback quantity or phishing cue saliency. The plot for detection accuracy indicates that as phishing cue saliency changes from low to high, the probability of providing a correct answer increases much more in the high-quantity feedback group than in the low-quantity feedback group. In addition, for low phishing cue saliency, the probability of giving a correct answer is much higher in the low feedback quantity group; however, for high cue saliency, this probability is a bit higher in the high feedback quantity group. Overall, feedback quantity does not have a main impact on decision avoidance or detection accuracy. Phishing cue saliency has a positive impact on detection accuracy. There is an interaction effect between feedback quantity and phishing cue saliency on detection accuracy.

Table 5. Experiment 3. GEE Results for Decision Avoidance and Detection Accuracy

<table><tr><td rowspan="2"></td><td colspan="4">Decision avoidance</td><td colspan="4">Detection accuracy</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td>Intercept</td><td>-3.89***</td><td>-3.94***</td><td>-5.61***</td><td>-5.66***</td><td></td><td></td><td></td><td></td></tr><tr><td>Threshold</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-1.00|0.00</td><td></td><td></td><td></td><td></td><td>-1.46***</td><td>-1.51***</td><td>-1.62***</td><td>-1.62***</td></tr><tr><td>0.00|1.00</td><td></td><td></td><td></td><td></td><td>-1.34***</td><td>-1.38***</td><td>-1.48***</td><td>-1.49***</td></tr><tr><td>Level 2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Manipulation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FQ (H4)</td><td>.06</td><td>.09</td><td>.01</td><td>.00</td><td>.36*</td><td>.37*</td><td>.33*</td><td>.23</td></tr><tr><td>Individual factors</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Age</td><td></td><td>-.03</td><td>-.08</td><td>-.08</td><td></td><td>-.18*</td><td>-.19*</td><td>-.19*</td></tr><tr><td>GEN</td><td></td><td>-.29</td><td>-.66</td><td>-.69</td><td></td><td>.12</td><td>.09</td><td>.08</td></tr><tr><td>PPE</td><td></td><td>.08</td><td>.09</td><td>.10</td><td></td><td>.09</td><td>.08</td><td>.08</td></tr><tr><td>AEL</td><td></td><td>-.19</td><td>-.27</td><td>-.25</td><td></td><td>-.05</td><td>-.04</td><td>-.04</td></tr><tr><td>PTDA</td><td></td><td>-.18</td><td>.02</td><td>.05</td><td></td><td>.01</td><td>.08</td><td>.08</td></tr><tr><td>TC</td><td></td><td>-.19</td><td>.04</td><td>.05</td><td></td><td>.05</td><td>.11</td><td>.11</td></tr><tr><td>EC</td><td></td><td>.05</td><td>-.41</td><td>-.40</td><td></td><td>.33***</td><td>.27**</td><td>.28**</td></tr><tr><td>AC</td><td></td><td>-.08</td><td>.04</td><td>.04</td><td></td><td>.11</td><td>.11</td><td>.11</td></tr><tr><td>Level 1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Manipulation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PCS (H5b)</td><td>-.06</td><td>-.06</td><td>.09</td><td>.10</td><td>-.82***</td><td>-.84***</td><td>-.85***</td><td>-.84***</td></tr><tr><td>Message-level factors</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PDE</td><td></td><td></td><td>-1.84***</td><td>-1.85***</td><td></td><td></td><td>-.42***</td><td>-.43***</td></tr><tr><td>RT</td><td></td><td>.03</td><td>-.75†</td><td>-.76†</td><td></td><td>.06</td><td>.01</td><td>.01</td></tr><tr><td>Interaction</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FQ × PCS (H6b)</td><td></td><td></td><td></td><td>-.86</td><td></td><td></td><td></td><td>-.59*</td></tr><tr><td>Model fit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>QIC</td><td>329.79</td><td>343.10</td><td>259.30</td><td>263.70</td><td></td><td></td><td></td><td></td></tr><tr><td>QICC</td><td>329.81</td><td>343.40</td><td>259.60</td><td>264.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Wald statistics</td><td></td><td></td><td></td><td></td><td>-</td><td>29.16***</td><td>34.74***</td><td>5.99*</td></tr><tr><td>DF</td><td></td><td></td><td></td><td></td><td>-</td><td>9</td><td>1</td><td>1</td></tr></table>

Note: Individual level: $n = 2 7 4 ;$ message level: $n = 1 6 4 4 . { \begin{array} { l } { * * * * } \\ { p < 0 . 0 0 1 , * * p < 0 . 0 1 , * p < 0 . 0 5 , \dagger p < 0 . 0 5 , } \end{array} }$ 0.10 (two-tailed). For model fit, QIC and QICC were used for decision avoidance, and Wald statistics were used for detection accuracy. For GEE with ordinal outcomes, a negative (positive) sign indicates a positive (negative) effect on the outcome variable. FQ = feedback quantity (low = 0, high = 1); GEN = gender (male = 0, female = 1); PPE = prior phishing experience; AEL = average email load; PTDA = preliminary training detection accuracy; TC = task-focused coping; EC = emotion-focused coping; AC = avoidance coping; PCS = phishing cue saliency (low = 0, high = 1); PDE = perceived detection efficacy; RT = response time to each quiz

![](/api/attachments/FAU6CSDY/fulltext/images/8e18d4a27dd639fe69bcdd18adadafe98f93f5cf6cd0513a8cf28da980d1e5cd.jpg)

![](/api/attachments/FAU6CSDY/fulltext/images/114b6b8056d4766d050d0ed92616f2d5a3c146a093aaa81b6a06f04c83e0660d.jpg)  
Note: The probability of skipping and the probability of being correct were estimated based on the results of GEE  
Figure 4. Experiment 3: Interaction between Feedback Quantity and Phishing Cue Saliency

## 4.4 Experiment 4

In Experiment 1, we tested the relative effectiveness of example-based feedback and mindful feedback in the context of link-embedded emails, which is a common email type in daily life. However, it remains to be seen how the two types of feedback differ for an email type that differs from link-embedded emails. For example, some phishing emails only contain plain text and ask recipients to reply or call a phone number. Individuals also receive legitimate emails with plain text from time to time. Therefore, the effect of feedback type is unlikely to be identical across various email types. Experiment 4 was a supplementary study specifically designed to investigate the interaction effect between feedback type and email type. This experiment used a 2 (feedback type: mindful vs. example-based) × 2 (email type: link-embedded vs. nolink-embedded) between-subjects design.

## 4.4.1 Treatment

Participants were randomly assigned to one of the four experimental groups. For feedback type, the design of the example-based and mindful feedback was consistent with what we used in Experiments 1 and 2. We adjusted the content of the mindful feedback to make it more consistent with the existing mindfulness training material (Jensen et al., 2017; Nguyen et al., 2021a). For email type, all participants had to take six email quizzes (three legitimate emails and three phishing emails) in the main test. The embedded-link email group received emails with links consistent with the emails we used in previous phishing quizzes. The participants in the no-link-embedded email group received six emails without any links. Those phishing emails spoofed the email addresses to pretend to be from popular companies such as Microsoft and Facebook. The content of those phishing emails tried to convince people they were important notices, such as a reminder of Facebook copyright violations and security warnings. The phishing emails also asked for a reply or a phone call. The legitimate emails were real emails collected from colleagues of the authors. They were receipts or real notices from companies such as Chase. They typically did not ask for a direct reply. Appendix C shows the feedback materials in the test.

## 4.4.2 Sample

We collected data on a crowdsourcing survey platform (Clickworker.com) different from the ones used in previous experiments. Participants had to be at least 18 years old and be in the United States. We followed the same data-cleaning procedure as in previous experiments. In addition, as mentioned before, we also screened out participants who reported that they had taken similar phishing quizzes before and implemented the available fraud detection tool in Qualtrics and an instructional manipulation-check question (Marett, 2015; Oppenheimer et al., 2009) to screen out fraudulent and inattentive participants. The final valid sample consisted of 138 participants. Twenty-one participants did not complete the experiment, and only two of them answered the post-survey questions. Thus, to examine nonresponse bias, we compared their preliminary training detection accuracy with that of the final sample. There was no significant difference, suggesting that nonresponse bias was not an issue. This sample size is sufficient to identify a medium effect size (Cohen’s f = 0.25) with a power of 0.80. The average age of the participants was 37.58, and 72.46% of participants were female.

## 4.4.3 Experimental Procedures

The experimental procedure followed those of the previous experiments. We invited the participants to take part in phishing quizzes. The participants took a preliminary test including two emails (one phishing and one legitimate email) and indicated their judgments (phishing; legitimate; I do not know if it is a phishing message) about each email. Unlike in the previous experiments, to further clarify the meaning of our answer options, we used “I do not know if it is a phishing message” instead of “Skip” to capture a situation in which a participant could not reach a decision. Afterward, they received the answers to each quiz and the feedback material they were assigned.

Afterward, all participants were required to complete the main test, including six new email quizzes. Consistent with other experiments, we also told them that they would gain a base rate while earning or losing a small amount of money based on their performance. Specifically, all participants were randomly exposed to three legitimate and three phishing emails. In the link-embedded email group, the participants were asked to judge six new emails with fake or genuine links. In the no-link-embedded group, the participants were required to evaluate six emails without any links. This email type was not present in the preliminary test and contained different action requirements (e.g., reply directly) beyond clicking on links. Except for answering each quiz, participants also reported their perceived detection efficacy toward each email quiz. Finally, we asked participants about their coping responses and collected demographic information.

## 4.4.4 Measures

To measure decision avoidance, we coded a participant’s answer to each email quiz as 1 if the person chose “I do not know if it is a phishing message” and 0 if the person made a decision. In addition, we coded wrong answers in each quiz as -1, correct answers as 1, and the “I don’t know” answer as 0 to measure detection accuracy. We then aggregated the scores for the six email quizzes in the main test. We measured perceived detection efficacy, coping responses, response time, and other demographic variables using the same approach as in the prior experiments. We then averaged perceived detection efficacy across the six emails in the main test for each participant to simplify the later data analysis because it was not at the core of Experiment 4.

## 4.4.5 Manipulation Check

After reading the assigned feedback, participants were presented with a manipulation check question that was consistent with that used in the pilot study—“For detecting phishing emails, this feedback requires a lot of thinking/cognitive effort.” They rated their agreement with the two statements using a 7-point Likert scale. We aggregated the scores for the two statements. The result of the analysis of variance shows that in the mindful feedback group, participants perceptions $( M = 5 . 7 3 )$ that the feedback required more thinking were higher than the perceptions of those in the example-based feedback group $( M = 4 . 8 8 , F _ { ( 1 , 1 3 6 ) } = 1 2 . 2 0 , p < 0 . 0 0 1 )$ , indicating that our manipulation of feedback type was successful. The effect size $( f = 0 . 3 0 )$ fell between the conventional medium to large effect size. We did not ask participants questions about the email type for the email messages for the same reasons as in Experiment 3.

## 4.4.6 Construct Validation

As in the prior experiments, we performed a confirmatory factor analysis, including all the research variables in our model, to examine the quality of our measurement items. Appendix D shows the descriptive statistics for all variables and the results of construct validation. All the constructs showed satisfactory reliability, convergent validity, and discriminant validity.

## 4.4.7 Analysis of Covariance

We performed a two-way analysis of covariance to test the effects of feedback type and email type. Table 6 shows the results of ANCOVA. For decision avoidance, there was a significant main effect of feedback type $( F _ { ( 1 , ~ 1 2 4 ) } ~ = ~ 6 . 1 9 , ~ p ~ < ~ 0 . 0 5 )$ and a significant interaction between feedback type and email type $( F _ { ( 1 , 1 2 4 ) } = 6 . 2 9 , p < 0 . 0 5 )$ . The magnitudes of the effect sizes (partial $\eta ^ { 2 } = 0 . 0 4 8 \ \mathrm { o r } \ f = 0 . 2 2 )$ both approached the conventional medium effect size. After removing the variance caused by all other factors, the interaction and the covariates, the variance caused by the membership of the feedback type group accounted for 4.8% of the remaining variance. Similarly, after excluding the variance due purely to feedback type or email type as well as the covariates, the variance caused by the membership of the feedback and email type combination accounted for 4.8% of the remaining variance. Pairwise comparisons with a Bonferroni adjustment show that for no-link-embedded emails, the adjusted mean of the example-based feedback group $( M = 0 . 3 0 )$ was significantly $( p < 0 . 0 5 )$ higher than that of the mindful group $( M = 0 . 0 4 )$ . For link-embedded emails, the feedback groups did not significantly differ $( p = 0 . 3 0 )$ . However, the adjusted mean score of the example-based feedback group $( M = 0 . 0 8 )$ was less than that of the mindful group $( M = 0 . 1 8 )$ . Moreover, perceived detection efficacy had a significant impact on decision avoidance $( F _ { ( 1 , 1 2 4 ) } = 1 1 . 4 8 , p < 0 . 0 0 1 )$ .

For detection accuracy, the main effects of feedback type and email type were not statistically significant. There was a significant interaction effect between feedback type and email type $( F _ { ( 1 , 1 2 4 ) } = 1 0 . 6 9 , p < 0 . 0 1 )$ after controlling for other control variables and perceived detection efficacy. The effect size (partial $\eta ^ { 2 }$ $= 0 . 0 7 9 \ \mathrm { o r } \ f = 0 . 2 9 )$ slightly exceeded the conventional medium effect size. After excluding the variance due purely to feedback type or email type and the covariates, the variance caused by the membership of the feedback and email type group combination accounted for 7.9% of the remaining variance. Pairwise comparisons with a Bonferroni adjustment show that for link-embedded emails, the adjusted mean score of the example-based feedback group $( M = 4 . 3 7 )$ was significantly $( p < 0 . 0 0 1 )$ higher than that of the mindful feedback group $( M =$ 2.36). For no-link-embedded emails, the difference between feedback groups was not significant $( p = 0 . 2 5 )$ 2 although the adjusted mean of the mindful group $( M =$ 2.57) was higher than that of the example-based feedback group (M = 1.87).

We calculated the values of the VIF for all the variables. All VIF values were below 3.33 and ranged from 1.06 (feedback type) to 1.28 (avoidance coping), implying that multicollinearity was not an issue.

Figure 5 also presents the interaction effect between feedback type and email type on decision avoidance and detection accuracy, respectively. For no-linkembedded emails, the adjusted mean score of decision avoidance was much higher in the example-based feedback group than in the mindful feedback group. For link-embedded emails, the adjusted mean score of decision avoidance in the mindful group was higher than that in the example-based feedback group, but the magnitude of the difference was much smaller. Meanwhile, for no-link-embedded emails, the adjusted mean score of detection accuracy in the mindful feedback group was only slightly higher than that in the example-based feedback group. For link-embedded emails, the score of detection accuracy was much higher in the example-based feedback group than in the mindful feedback group.

The purpose of Experiment 4 was to further investigate the effects of feedback type (mindful vs. examplebased) in different contexts (e.g., when encountering various email types). The results of Experiment 4 show the contextual effect of example-based feedback. For link-embedded emails, example-based feedback led to better detection accuracy than mindful feedback. However, for a new email type (i.e., no-link-embedded emails), the detection accuracy in the two feedback groups did not differ significantly. Example-based feedback led to more decision avoidance than mindful feedback in the context of no-link-embedded emails. The results indicate that the relative effectiveness of example-based feedback compared with mindful feedback depends on the email type.

Table 6. Experiment 4: ANCOVA Results for Decision Avoidance and Detection Accuracy

<table><tr><td rowspan="2"></td><td colspan="4">Decision avoidance</td><td colspan="4">Detection accuracy</td></tr><tr><td>Mean square</td><td>F</td><td>p-value</td><td>Effect size (partial η2)</td><td>Mean square</td><td>F</td><td>p-value</td><td>Effect size (partial η2)</td></tr><tr><td>Manipulation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FT</td><td>1.02</td><td>6.19</td><td>.014</td><td>.048</td><td>7.08</td><td>1.32</td><td>.252</td><td>.011</td></tr><tr><td>ET</td><td>.32</td><td>1.92</td><td>.168</td><td>.015</td><td>.67</td><td>.12</td><td>.725</td><td>.001</td></tr><tr><td>Control variables</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Age</td><td>.18</td><td>1.11</td><td>.295</td><td>.009</td><td>.02</td><td>.00</td><td>.958</td><td>.000</td></tr><tr><td>GEN</td><td>.01</td><td>.03</td><td>.856</td><td>.000</td><td>8.84</td><td>1.65</td><td>.201</td><td>.013</td></tr><tr><td>PPE</td><td>.00</td><td>.01</td><td>.921</td><td>.000</td><td>1.22</td><td>.23</td><td>.633</td><td>.002</td></tr><tr><td>AEL</td><td>.05</td><td>.31</td><td>.582</td><td>.002</td><td>3.09</td><td>.58</td><td>.449</td><td>.005</td></tr><tr><td>PTDA</td><td>.05</td><td>.33</td><td>.568</td><td>.003</td><td>4.25</td><td>.79</td><td>.375</td><td>.006</td></tr><tr><td>TC</td><td>.02</td><td>.11</td><td>.742</td><td>.001</td><td>8.30</td><td>1.55</td><td>.215</td><td>.012</td></tr><tr><td>EC</td><td>.07</td><td>.41</td><td>.523</td><td>.003</td><td>.10</td><td>.02</td><td>.891</td><td>.000</td></tr><tr><td>AC</td><td>.13</td><td>.79</td><td>.375</td><td>.006</td><td>.12</td><td>.02</td><td>.883</td><td>.000</td></tr><tr><td>PDE</td><td>1.89</td><td>11.48</td><td>.001</td><td>.085</td><td>1.27</td><td>.24</td><td>.628</td><td>.002</td></tr><tr><td>RT</td><td>.21</td><td>1.26</td><td>.264</td><td>.01</td><td>2.38</td><td>.45</td><td>.506</td><td>.004</td></tr><tr><td>Interaction</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FT × ET</td><td>1.04</td><td>6.29</td><td>.013</td><td>.048</td><td>57.22</td><td>10.69</td><td>.001</td><td>.079</td></tr><tr><td>Model fit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>R2</td><td colspan="4">.187</td><td colspan="4">.187</td></tr><tr><td>Adjusted R2</td><td colspan="4">.102</td><td colspan="4">.102</td></tr></table>

Note: FT = feedback type (mindful = 0, example-based = 1); ET = email type (no-link-embedded = 0, link-embedded = 1); GEN = gender (male = 0, female = 1); PPE = prior phishing experience; AEL = average email load; PTDA = preliminary training detection accuracy; TC = task-focused coping; EC = emotion-focused coping; AC = avoidance coping; PDE = perceived detection efficacy; RT = response time

![](/api/attachments/FAU6CSDY/fulltext/images/83d5a55027b6f9f4e2b5c3bdd48aa1ab05c70bbb785de0fe28f1ec3798d5304c.jpg)

![](/api/attachments/FAU6CSDY/fulltext/images/4cb89676897948313149283cfb9f9adfe91f5bcc974f62c9b2ee827c421d7434.jpg)  
Figure 5. Experiment 4: Interaction between Feedback Type and Email Type

## 5 Discussion and Conclusion

## 5.1 Summary of Findings

The objectives of this study were to identify: (1) the determinants of decision avoidance and detection accuracy, (2) the contextual effect of the type of feedback in antiphishing training, (3) the impacts of perceived detection efficacy on training outcomes, and (4) the interaction effects between feedback characteristics and perceived detection efficacy/phishing characteristics on training outcomes. Drawing upon goal-setting theory, skill acquisition theory, and the antiphishing training literature, our model provides a theoretical account of how feedback characteristics (e.g., type, quantity), phishing characteristics (e.g., phishing cue saliency), and perceived detection efficacy affect antiphishing training outcomes (e.g., decision avoidance and detection accuracy). We conducted four experiments to evaluate our proposed model and corresponding research hypotheses. Table 7 shows a summary of research findings from the four experiments.

Table 7. Summary of Research Findings

<table><tr><td>EXP</td><td>Hypothesis</td><td>Findings</td></tr><tr><td>1</td><td>H1ab</td><td>• Example-based feedback leads to less decision avoidance and higher detection accuracy than mindful feedback in the context of link-embedded emails (H1a and H1b supported).</td></tr><tr><td>2</td><td>H2ab, H3b</td><td>• Perceived detection efficacy decreases decision avoidance and increases detection accuracy (H2a and H2b supported).• There is a marginally significant interaction effect between perceived detection efficacy and feedback type on detection accuracy; as expected, however, the interaction is not significant on decision avoidance (H3b marginally supported).</td></tr><tr><td>3</td><td>H4ab, H5b, H6b</td><td>• Quantity of example-based feedback does not have a significant impact on decision avoidance and detection accuracy (H4a and H4b not supported).• Phishing cue saliency positively influences detection accuracy (H5b supported).• The effect of phishing cue saliency is stronger under the high feedback quantity condition than under the low feedback quantity condition (H6b supported).</td></tr><tr><td>4</td><td>Post hoc study</td><td>• For link-embedded emails, example-based feedback leads to better detection accuracy than mindful feedback; for a new email type (i.e., no-link-embedded emails), the scores of detection accuracy in the two feedback groups do not differ significantly.• Example-based feedback leads to more decision avoidance than mindful feedback in the context of no-link-embedded emails.</td></tr></table>

Using a single-factor design, Experiment 1 investigated the effects of feedback type on decision avoidance and detection accuracy. Based on the data from 130 MTurk participants, our findings support the hypothesis that example-based feedback is more helpful than mindful feedback in increasing detection accuracy (H1b) in the context of link-embedded emails. On the other hand, mindful feedback leads to more decision avoidance than example-based feedback (H1a). In addition, using a single-factor repeated measures design, Experiment 2 was intended to examine the effects of feedback type and perceived detection efficacy on outcomes. Based on the data collected from 110 members of a nationwide online panel, we found a significant effect of perceived detection efficacy on decision avoidance and detection accuracy (H2a and H2b).

Furthermore, this study suggests that the positive effect of perceived detection efficacy on detection accuracy is stronger for people who receive example-based feedback than for people who receive mindful feedback. However, this effect was only marginally significant (H3b). Furthermore, as expected, the type of feedback did not moderate the relationship between perceived detection efficacy and decision avoidance.

Experiment 3 used a 2×2 mixed design with 274 MTurk participants. It examined the effects of feedback quantity and phishing cue saliency on outcomes. In contrast to our prediction, the quantity of example-based feedback appears to have no significant impact on decision avoidance or detection accuracy (H4a and H4b). A plausible explanation is that the impact of feedback quantity on outcomes varies with other factors, such as types of phishing messages. Meanwhile, we found that phishing cue saliency positively influences detection accuracy (H5b). Finally, the effect of phishing cue saliency on detection accuracy is stronger when people receive high feedback quantity than when they receive low feedback quantity (H6b).

Experiment 4 used a 2×2 between-subjects design with 138 participants. The results show that the relative effectiveness of example-based feedback compared with mindful feedback depends on the email type. For link-embedded emails, example-based feedback leads to higher detection accuracy. However, for a new email type (in our study, the no-link-embedded emails), the difference in detection accuracy between examplebased feedback and mindful feedback is not significant, but example-based feedback leads to more decision avoidance in the context of no-link-embedded emails.

## 5.2 Theoretical Contributions

This study makes several theoretical contributions. First, based on goal-setting theory (Locke & Latham, 2002), this study identifies important predictors of antiphishing training outcomes: feedback characteristics, task characteristics, and self-efficacy. Although prior antiphishing training literature has examined these factors separately (e.g., Jensen et al., 2017; Wang et al., 2016), little research has examined these factors coherently within a goal-setting perspective. We believe that goal setting is an ideal theoretical perspective to identify the key factors that explain individuals antiphishing training outcomes because organizations and employees have a clear goal of increasing antiphishing training performance. This study contributes to IS research by presenting new insights into how factors of goal-setting theory can influence antiphishing training outcomes.

Second, whereas prior research on phishing has focused on detection accuracy, decision avoidance has received little attention. Our study is among the first to suggest differences in the mechanisms underlying decision avoidance and detection accuracy. In particular, we found that whereas detection accuracy is based on an objective criterion, subjective perceptions largely determine decision avoidance. Furthermore, we found that they have low correlations (-0.23 in Experiment 1, -0.05 in Experiment 2, -0.10 in Experiment 3, and -0.17 in Experiment 4). For these reasons, phishing cue saliency influences detection accuracy, but such a relationship could not be found for decision avoidance. Similarly, the impact of perceived detection efficacy on detection accuracy varies with feedback types, but no such interaction effect was found for decision avoidance. Thus, it is important that future researchers examine both decision avoidance and detection accuracy in the context of skill acquisition. Overall, this study contributes to IS research by providing an integrated theoretical framework for the different mechanisms regulating detection accuracy and decision avoidance.

Third, drawing on skill acquisition theory (Anderson, 1982), we argue that example-based feedback is more effective than mindful feedback in transforming declarative knowledge into procedural knowledge, which eventually leads to better detection accuracy. Our findings provide strong support for our major claim about the relative efficacy of feedback with concrete tips over feedback with abstract guidelines— at least in typical cases in which phishing cues are associated with low-level, specific technical attributes (e.g., fake links). However, mindful feedback makes individuals more conservative in deciding on an email’s legitimacy (Jensen et al., 2017; Nguyen et al., 2021a) in this context. One of the significant contributions of this study to IS research is its highlighting of the importance of assimilating declarative forms of organizational guidelines into actionable forms of procedural sequences in the context of antiphishing training. We expect that our theoretical framework will offer valuable insights into an in-depth analysis of novel antiphishing programs.

Fourth, self-efficacy is an important concept for understanding how people accomplish a given task (Bagozzi et al., 2003a, 2003b; Locke & Latham, 2002). In the context of antiphishing training, prior research has found that perceived detection efficacy increases overconfidence (Wang et al., 2016) and coping adaptiveness (Wang et al., 2017). However, we are uncertain of its direct effect on antiphishing training behavior and performance. Drawing on goal-setting theory, this study is among the first to highlight the important role of perceived detection efficacy in antiphishing training behavior and performance. Our findings indicate that perceived detection efficacy remains significant in determining decision avoidance and detection accuracy even after controlling for coping adaptiveness (i.e., task-focused, emotionfocused, and avoidance coping) and other well-known factors. These results suggest that perceived detection efficacy is an essential factor for a better understanding of antiphishing training outcomes.

Fifth, this paper provides a theoretical account of how feedback moderates the effect of perceived detection efficacy on antiphishing performance. We argue that because perceived detection efficacy is only a subjective behavioral possibility, proper antiphishing training could reinforce how such a possibility would successfully translate into antiphishing performance. More specifically, compared with mindful feedback, example-based feedback helps turn antiphishing tips into procedural knowledge, allowing users to successfully complete antiphishing tasks. As theorized in our model, we found that the impact of perceived detection efficacy on detection accuracy is stronger after showing example-based feedback than after showing mindful feedback. This study is meaningful because it theoretically and empirically reveals the important connection between the perspectives of selfefficacy and skill acquisition in the context of antiphishing training.

Finally, although much research exists concerning feedback characteristics in phishing research, little was known about whether feedback quantity makes a difference in antiphishing behavior and performance. Drawing on skill acquisition theory, this study is the first to shed light on the moderating effect of feedback quantity on the relationship between phishing cue saliency and its behavioral outcomes. Specifically, we theorize that for those with minimal example-based information (i.e., low-quantity feedback), phishing cue saliency is relatively less important as a determinant of detection accuracy. In contrast, for those with ample example-based information (i.e., high-quantity feedback), phishing cue saliency is more important as a factor regulating detection accuracy. Our findings clearly provide empirical support for the proposed model. In sum, this study is meaningful because it theoretically and empirically shows that the impacts of phishing characteristics on antiphishing outcomes vary considerably with how antiphishing feedback is provided.

## 5.3 Practical Contributions

Our study provides significant practical implications for information security practitioners who want to use feedback in their antiphishing training programs. First, our results emphasize the importance of examplebased feedback in improving detection accuracy. Specifically, example-based feedback is shown to be crucial for helping people better identify the legitimacy of fake-link-embedded phishing emails because it facilitates the formation of procedural knowledge related to phishing cues and antiphishing techniques. Thus, we encourage information security managers to consider incorporating example-based feedback into their antiphishing training programs for fake-linkembedded phishing emails.

Second, as Figure 4 shows, more feedback is not always better in antiphishing training. Specifically, low-quantity feedback is better for sophisticated phishing (low cue saliency). These findings suggest the importance of ensuring that trainees thoroughly digest basic antiphishing tips before being exposed to other more sophisticated antiphishing techniques. In this manner, basic tips can be more efficiently translated into procedural knowledge in one’s mental representation, a mental step that can free up cognitive resources for assimilating new antiphishing techniques. Taken together, this study highlights the risk of offering employees too much information; thus, practitioners are encouraged to start with a basic training program while cautiously implementing a complex and expensive training program.

## 5.4 Limitations and Future Research Directions

Several limitations in our study should be noted. First, all our experiments were based on web-based survey quizzes. Previous phishing studies have used similar online experiments to measure phishing detection accuracy (Sheng et al., 2010; Wang et al., 2016, 2017). This method has been recognized as an efficient approach to collecting data because it addresses ethical dilemmas that could result from field experiments (Wang et al., $2 0 1 6 ) . ^ { 6 }$ Nevertheless, it would be helpful to reexamine the effects found in the present study in nonexperimental settings. Second, our experiments were conducted using participants who live in the United States because the content of the phishing and legitimate emails was based on English and US companies (e.g., Chase, Amazon, FedEx, etc.). Nevertheless, using US samples may limit generalizability because phishing emails from different countries may have different characteristics. Therefore, future research could examine our model using samples from other countries. Third, we only tested the effects of feedback in the short term. The long-term effects of the feedback in the study remain to be tested. Fourth, the current study was focused only on phishing emails with deceitful links. However, other types of phishing attempts go far beyond such fraudulent links and are difficult to detect. For example, some phishing emails contain attachments and ask the receivers to download the files. Thus, our findings may not be applicable to other types of phishing. Fifth, our feedback materials and training were relatively short. Thus, our findings regarding the role of feedback cannot be generalized to other longer forms of feedback or training.

In addition, although we controlled for several factors when testing our hypotheses, we may still have failed to control for some potentially important variables. Thus, our results should be interpreted carefully until more control variables are added to the model. Lastly, we asked participants to categorize each email as either legitimate or phishing and to report “Skip” or “I do not know if it is a phishing message” if they could not decide. Several phishing studies have used similar methods to record participants’ decisions about email legitimacy in web-based phishing experiments (Nguyen et al., 2021a; Wang et al., 2017). However, individuals may not categorize an email as absolutely phishing or absolutely legitimate in practice before taking action. Our study may have been more informative and better reflected reality if we had assessed individuals’ perceptions about each email’s legitimacy or their degree of certainty in each decision—for example, by using a Likert scale.

This study yields insights into several additional avenues for future research. First, it provides either example-based or mindful feedback, not both, to each experimental group. Future research could test if providing both example-based and mindful feedback would be more effective than providing them separately. Second, although this study focused on phishing cue saliency as a phishing characteristic, future research should examine other phishing characteristics to better understand the actual ramifications that feedback has on antiphishing behavior and performance. For example, Goel et al. (2017) showed that phishing attempts can be categorized by various factors such as the gain-loss frame, the extrinsic-intrinsic taxonomy, and personalization. We cannot expect that the effectiveness of a certain type of feedback will be identical across these different types of phishing. Thus, we encourage researchers to investigate the correspondence between feedback and phishing characteristics for more efficient and effective antiphishing training.

Another avenue for further research is related to the paradoxical finding that less feedback may be better for sophisticated phishing. In particular, it would be interesting to examine if these results would hold in a repeated, long-term educational context because the benefit of extra information could be more apparent after continued learning. Future research could also examine the impacts of feedback characteristics across diverse social, task, and physical contexts because antiphishing behavior is sensitive to such contextual factors. We appeal to others to examine how the characteristics of feedback and other antiphishing interventions interact with message-, individual-, physical context-, task context- or even social contextrelated factors to influence antiphishing performance.

Lastly, as stated previously, we asked each participant to make a ternary decision on each email’s legitimacy. Future studies could elicit participants’ perceptions of each email’s genuineness or the certainty of their decisions using a Likert scale. This alternative design may better reflect the continuum perceived by the email receivers when checking emails in practice and provide more informative results. Future studies could also measure participants’ perceptions about other email properties, such as source credibility, to provide more information on individuals’ perceptions of emails.

## 5.5 Concluding Remarks

Despite the importance of offering proper feedback on individuals’ reactions to phishing scams, our understanding is severely limited concerning the efficacy of such educational information under various types of phishing attacks. We developed and tested a theoretical, conceptual framework that describes how feedback and phishing characteristics interact to influence decision avoidance and detection accuracy. More research is needed to untangle the complex interactions between feedback and phishing characteristics on antiphishing behavior and performance. We hope that the proposed model will be helpful for such endeavors in this important line of research.

## Acknowledgments

We would like to thank the senior editor, Paul Benjamin Lowry, and three anonymous reviewers for their insightful comments and suggestions on the paper.

## References

Abbasi, A., Dobolyi, D., Vance, A., & Zahedi, F. M. (2021). The phishing funnel model: A design artifact to predict user susceptibility to phishing websites. Information Systems Research, 32(2), 410-436.

Al-Daeef, M. M., Basir, N., & Saudi, M. M. (2017). Security awareness training: A review. Proceedings of the World Congress on Engineering. Available at https://www.iaeng. org/publication/WCE2017/WCE2017\_pp446- 451.pdf

Anderson, C. J. (2003). The psychology of doing nothing: Forms of decision avoidance result from reason and emotion. Psychological Bulletin, 129(1), 139- 167.

Anderson, J. R. (1976). Language, memory, and thought. Laurence Erlbaum Associates.

Anderson, J. R. (1982). Acquisition of cognitive skill. Psychological Review, 89(4), 369-406.

Anderson, J. R. (1987). Skill acquisition: Compilation of weak-method problem situations. Psychological Review, 94(2), 192-210.

Anderson, J. R. (2010). Cognitive psychology and its implications. Macmillan.

Arachchilage, N. A. G., Love, S., & Beznosov, K. (2016). Phishing threat avoidance behaviour: An empirical investigation. Computers in Human Behavior, 60, 185-197.

Bagozzi, R. P., & Yi, Y. (1988). On the evaluation of structural equation models. Journal of the Academy of Marketing Science, 16(1), 74-94.

Bagozzi, R. P., Bergami, M., & Leone, L. (2003a). Hierarchical representation of motives in goal setting. Journal of Applied Psychology, 88(5), 915-943.

Bagozzi, R. P., Dholakia, U. M., & Basuroy, S. (2003b). How effortful decisions get enacted: The motivating role of decision processes, desires, and anticipated emotions. Journal of Behavioral Decision Making, 16(4), 273-295.

Bandura, A. (1997). Self-efficacy: The exercise of control. WH Freeman.

Bangert-Drowns, R. L., Kulik, C. L. C., Kulik, J. A., & Morgan, M. (1991). The instructional effect of feedback in test-like events. Review of Educational Research, 61(2), 213-238.

Bialystok, E. (1979). Explicit and implicit judgements of L2 grammaticality. Language Learning, 29(1), 81-103.

Bilodeau, I. M. (1966). Information feedback. In E. A. Bilodeau (Eds.), Acquisition of skill (pp. 255-296). Academic Press.

Braarud, P. Ø. (2001). Subjective task complexity and subjective workload: Criterion validity for complex team tasks. International Journal of Cognitive Ergonomics, 5(3), 261-273.

Brookes, S. T., Whitely, E., Egger, M., Smith, G. D., Mulheran, P. A., & Peters, T. J. (2004). Subgroup analyses in randomized trials: Risks of subgroupspecific analyses; power and sample size for the interaction test. Journal of Clinical Epidemiology, 57(3), 229-236.

Butler, R. (1987). Task-involving and ego-involving properties of evaluation: Effects of different feedback conditions on motivational perceptions, interest, and performance. Journal of Educational Psychology, 79(4), 474-482.

Butler, R., & Nisan, M. (1986). Effects of no feedback, task-related comments, and grades on intrinsic motivation and performance. Journal of Educational Psychology, 78(3), 210-216.

Canova, G., Volkamer, M., Bergmann, C., Borza, R., Reinheimer, B., Stockhardt, S., & Tenberg, R. (2015b). Learn to spot phishing URLs with the Android NoPhish app. Proceedings of the IFIP World Conference on Information Security Education.

Carver, C. S., & Scheier, M. F. (1982). Control theory: A useful conceptual framework for personality— social, clinical, and health psychology. Psychological Bulletin, 92(1), 111-135.

Chen, R., Gaia, J., & Rao, H. R. (2020). An examination of the effect of recent phishing encounters on phishing susceptibility. Decision Support Systems, 133, Article 113287.

Cohen, J. (1988). Statistical power analysis for the behavioral sciences. Lawrence Erlbaum Associates.

Cohen, J. (1992). A power primer. Psychological Bulletin, 112(1), 155-159.

Cook, D. M. (1968). The impact on managers of frequency of feedback. Academy of Management Journal, 11(3), 263-277.

Cox, D. R. (1970). Analysis of binary data. New York: Chapman & Hall/CRC.

Devine, D. J., & Kozlowski, S. W. (1995). Domainspecific knowledge and task characteristics in decision making. Organizational Behavior and Human Decision Processes, 64(3), 294-306.

Dincelli, E., & Chengalur-Smith, I. (2020). Choose your own training adventure: Designing a gamified

SETA artefact for improving information security and privacy through interactive storytelling. European Journal of Information Systems, 29(6), 669-687

Downs, J. S., Holbrook, M. B., & Cranor, L. F. (2006). Decision strategies and susceptibility to phishing. Proceedings of the 2nd Symposium on Usable Privacy and Security.

Dutton, J. E. (1988). Patterns of interest around issues: The role of uncertainty and feasibility. Academy of Management Journal, 31(3), 663-675.

Earley, P. C., Northcraft, G. B., Lee, C., & Lituchy, T. R. (1990). Impact of process and outcome feedback on the relation of goal setting to task performance. Academy of Management Journal, 33(1), 87-105.

Educause (2020). Cybersecurity awareness resource library. https://www.educause.edu/focus-areasand-initiatives/policy-and-security/cybersecurityprogram/resources/information-securityguide/toolkits/cybersecurity-awareness-resourcelibrary

Faul, F., Erdfelder, E., Buchner, A., & Lang, A. G. (2009). Statistical power analyses using G\* Power 3.1: Tests for correlation and regression analyses. Behavior Research Methods, 41(4), 1149-1160.

Faul, F., Erdfelder, E., Lang, A. G., & Buchner, A. (2007). G\* Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. Behavior Research Methods, 39(2), 175-191.

Federal Bureau of Investigation. (2022). Internet crime report. Internet Crime Complaint Center, Federal Bureau of Investigation. https://www. ic3.gov/Media/PDF/AnnualReport/2022\_IC3Re port.pdf

Fitzsimmons, J. R., & Douglas, E. J. (2011). Interaction between feasibility and desirability in the formation of entrepreneurial intentions. Journal of Business Venturing, 26(4), 431-440.

Fornell, C., & Larcker, D. F. (1981). Evaluating structural equation models with unobservable variables and measurement error. Journal of Marketing Research, 18(1), 39-50.

Frank, M., Jaeger, L., & Ranft, L. M. (2022). Contextual drivers of employees' phishing susceptibility: Insights from a field study. Decision Support Systems, 160, Article 113818.

Gefen, D., & Straub, D. W. (2000). The relative importance of perceived ease of use in IS adoption: A study of e-commerce adoption. Journal of the Association for Information Systems, 1(1), 1-25.

Goel, S., Williams, K. J., Huang, J., & Warkentin, M. (2021). Can financial incentives help with the struggle for security policy compliance? Information & Management, 58(4), Article 103447.

Goel, S., Williams, K., & Dincelli, E. (2017). Got phished? Internet security and human vulnerability. Journal of the Association for Information Systems, 18(1), 22-44.

Gollwitzer, P. M. (1996). The volitional benefits of planning. In P. M. Gollwitzer & J. Bargh (Eds.), The psychology of action: Linking cognition and motivation to behavior (pp. 287-312). Guilford Press.

Griffin, R. W., Welsh, A., & Moorhead, G. (1981). Perceived task characteristics and employee performance: A literature review. Academy of Management Review, 6(4), 655-664.

Gruijters, S. L. (2022). Making inferential leaps: Manipulation checks and the road towards strong inference. Journal of Experimental Social Psychology, 98, Article 104251.

Haddock, C. K., Rindskopf, D., & Shadish, W. R. (1998). Using odds ratios as effect sizes for meta-analysis of dichotomous data: A primer on methods and issues. Psychological Methods, 3(3), 339-353.

Harks, B., Rakoczy, K., Hattie, J., Besser, M., & Klieme, E. (2014). The effects of feedback on achievement, interest and self-evaluation: The role of feedback’s perceived usefulness. Educational Psychology, 34(3), 269-290.

Hattie, J., & Timperley, H. (2007). The power of feedback. Review of Educational Research, 77(1), 81-112.

Hauser, D. J., Ellsworth, P. C., & Gonzalez, R. (2018). Are manipulation checks necessary? Frontiers in Psychology, 9, Article 998.

Heckhausen, H. (2013). The anatomy of achievement motivation. Academic Press.

Hulland, J., Baumgartner, H., & Smith, K. M. (2018). Marketing survey research best practices: Evidence and recommendations from a review of JAMS articles. Journal of the Academy of Marketing Science, 46, 92-108.

Jaeger, L., & Eckhardt, A. (2021). Eyes wide open: The role of situational information security awareness for security‐related behaviour. Information Systems Journal, 31(3), 429-472.

Jampen, D., Gür, G., Sutter, T., & Tellenbach, B. (2020). Don’t click: Towards an effective anti-phishing training. A comparative literature review. Human-

centric Computing and Information Sciences, 10(1), 1-41.

Jensen, M. L., Dinger, M., Wright, R. T., & Thatcher, J. B. (2017). Training to mitigate phishing attacks using mindfulness techniques. Journal of Management Information Systems, 34(2), 597- 626.

Jung, J. H., Schneider, C., & Valacich, J. (2010). Enhancing the motivational affordance of information systems: The effects of real-time performance feedback and goal setting in group collaboration environments. Management Science, 56(4), 724-742.

Kahneman, D. (1973). Attention and effort. Prentice-Hall.

Kanfer, R., & Ackerman, P. L. (1989). Motivation and cognitive abilities: An integrative/aptitudetreatment interaction approach to skill acquisition. Journal of Applied Psychology, 74(4), 657-690.

Kim, S., & Stoel, L. (2004). Apparel retailers: Website quality dimensions and satisfaction. Journal of Retailing and Consumer Services, 11(2), 109-117.

Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. Psychological Bulletin, 119(2), 254-284.

Kluger, A. N., Lewinsohn, S., & Aiello, J. R. (1994). The influence of feedback on mood: Linear effects on pleasantness and curvilinear effects on arousal. Organizational Behavior and Human Decision Processes, 60(2), 276-299.

Komaki, J., Heinzmann, A. T., & Lawson, L. (1980). Effect of training and feedback: Component analysis of a behavioral safety program. Journal of Applied Psychology, 65(3), 261-270.

Kühnen, U. (2010). Manipulation checks as manipulation: Another look at the ease-of-retrieval heuristic. Personality and Social Psychology Bulletin, 36(1), 47-58.

Kumaraguru, P., Rhee, Y., Acquisti, A., Cranor, L. F., Hong, J., & Nunge, E. (2007). Protecting people from phishing: The design and evaluation of an embedded training email system. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems.

Kwak, D.-H., Deng, S., Kuem, J., and Kim, S. S. (2022). How to achieve goals in digital games? An empirical test of a goal-oriented model in Pokemon GO. Journal of the Association for Information Systems, 23(2), 553-588.

Kwak, D. H., Ma, X., Polites, G., Srite, M., Hightower, R., & Haseman, W. (2019). Cross-level

moderation of team cohesion in individuals utilitarian and hedonic information processing: Evidence in the context of team-based gamified training. Journal of the Association for Information Systems, 20(2), 161-185.

Lam, C. F., DeRue, D. S., Karam, E. P., & Hollenbeck, J. R. (2011). The impact of feedback frequency on learning and task performance: Challenging the “more is better” assumption. Organizational Behavior and Human Decision Processes, 116(2), 217-228.

Liberman, N., & Trope, Y. (1998). The role of feasibility and desirability considerations in near and distant future decisions: A test of temporal construal theory. Journal of Personality and Social Psychology, 75(1), 5-18.

Liu, P., & Li, Z. (2012). Task complexity: A review and conceptualization framework. International Journal of Industrial Ergonomics, 42(6), 553-568.

Locke, E. A., & Latham, G. P. (2002). Building a practically useful theory of goal setting and task motivation: A 35-year odyssey. American Psychologist, 57(9), 705-717.

Lowry, P. B., D’Arcy, J., Hammer, B., & Moody, G. D. (2016). “Cargo Cult” science in traditional organization and information systems survey research: A case for using nontraditional methods of data collection, including Mechanical Turk and online panels. The Journal of Strategic Information Systems, 25(3), 232-240.

Marett, K. (2015). Checking the manipulation checks in information security research. Information & Computer Security, 23(1), 20-30.

Mohammed, S., & Harrison, D. A. (2013). The clocks that time us are not the same: A theory of temporal diversity, task characteristics, and performance in teams. Organizational Behavior and Human Decision Processes, 122(2), 244-256.

Newell, K. M. (1976). Knowledge of results and motor learning. Exercise Sport Sciences Reviews, 4(1), 195-228.

Nguyen, C., Jensen, M., & Day, E. (2021a). Learning not to take the bait: A longitudinal examination of digital training methods and overlearning on phishing susceptibility. European Journal of Information Systems, 32(2), 238-262.

Nguyen, C., Jensen, M. L., Durcikova, A., & Wright, R. T. (2021b). A comparison of features in a crowdsourced phishing warning system. Information Systems Journal, 31(3), 473-513.

Norman, D. A., & Bobrow, D. G. (1975). On data-limited and resource-limited processes. Cognitive Psychology, 7(1), 44-64.

O'Keefe, D. J. (2003). Message properties, mediating states, and manipulation checks: Claims, evidence, and data analysis in experimental persuasive message effects research. Communication Theory, 13(3), 251-274.

Oldham, G. R., Hackman, J. R., & Pearce, J. L. (1976). Conditions under which employees respond positively to enriched work. Journal of Applied Psychology, 61(4), 395-403.

Oppenheimer, D. M., Meyvis, T., & Davidenko, N. (2009). Instructional manipulation checks: Detecting satisficing to increase statistical power. Journal of Experimental Social Psychology, 45(4), 867-872.

Osterman Research. (2019). The ROI of security awareness training. https://ostermanresearch. com/2019/08/19/orwp\_0313/

Palmer, J. W. (2002). Web site usability, design, and performance metrics. Information Systems Research, 13(2), 151-167.

PhishLabs. (2019). Phishing trends and intelligence report. https://info.phishlabs.com/hubfs/2019 %20PTI%20Report/2019%20Phishing%20Tren ds%20and%20Intelligence%20Report.pdf?ref=h ackernoon.com

Proofpoint. (2022). State of the phish report. https://go.proofpoint.com/en-2022-state-of-thephish.html

Rakoczy, K., Klieme, E., Bürgermeister, A., & Harks, B. (2008). The interplay between student evaluation and instruction: Grading and feedback in mathematics classrooms. Journal of Psychology, 216(2), 111-124.

Reeves, A., Calic, D., & Delfabbro, P. (2023). “Generic and unusable”: Understanding employee perceptions of cybersecurity training and measuring advice fatigue. Computers & Security, 128, 103137.

Robinson, P. (2001). Task complexity, task difficulty, and task production: Exploring interactions in a componential framework. Applied Linguistics, 22(1), 27-57.

Roch, S. G., Lane, J. A., Samuelson, C. D., Allison, S. T., & Dent, J. L. (2000). Cognitive load and the equality heuristic: A two-stage model of resource overconsumption in small groups. Organizational Behavior and Human Decision Processes, 83(2), 185-212.

Salmoni, A. W., Schmidt, R. A., & Walter, C. B. (1984). Knowledge of results and motor learning: A review and critical reappraisal. Psychological Bulletin, 95(3), 355-386.

Sánchez-Meca, J., Marín-Martínez, F., & Chacón-Moscoso, S. (2003). Effect-size indices for dichotomized outcomes in meta-analysis. Psychological Methods, 8(4), 448-467.

Sarno, D. M., McPherson, R., & Neider, M. B. (2022). Is the key to phishing training persistence? Developing a novel persistent intervention. Journal of Experimental Psychology: Applied, 28(1): 85-99.

Schuetz, S. W., Benjamin Lowry, P., Pienta, D. A., & Bennett Thatcher, J. (2020). The effectiveness of abstract versus concrete fear appeals in information security. Journal of Management Information Systems, 37(3), 723-757.

Schuetz, S., Lowry, P. B., Pienta, D., & Thatcher, J. (2021). Improving the design of information security messages by leveraging the effects of temporal distance and argument nature. Journal of the Association for Information Systems, 22(5), 1376-1428.

Segars, A. H., & Grover, V. (1998). Strategic information systems planning success: An investigation of the construct and its measurement. MIS Quarterly, 22(2), 139-163.

Sheldon, K. M., & Elliot, A. J. (1999). Goal striving, need satisfaction, and longitudinal well-being: The selfconcordance model. Journal of Personality and Social Psychology, 76(3), 482-497.

Sheng, S., Holbrook, M., Kumaraguru, P., Cranor, L. F., & Downs, J. (2010). Who falls for phish? A demographic analysis of phishing susceptibility and effectiveness of interventions. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems.

Sheng, S., Magnien, B., Kumaraguru, P., Acquisti, A., Cranor, L. F., Hong, J., & Nunge, E. (2007). Antiphishing phil: The design and evaluation of a game that teaches people not to fall for phish. Proceedings of the 3rd Symposium on Usable Privacy and Security.

Shepherd, L. A., & Archibald, J. (2017). Security awareness and affective feedback: Categorical behaviour vs. reported behaviour. Proceedings of the International Conference on Cyber Situational Awareness, Data Analytics and Assessment.

Sigall, H., & Mills, J. (1998). Measures of independent variables and mediators are useful in social psychology experiments: But are they necessary? Personality and Social Psychology Review, 2(3), 218-226.

Silic, M., & Lowry, P. B. (2020). Using design-science based gamification to improve organizational

security training and compliance. Journal of Management Information Systems, 37(1), 129- 161.

Steele-Johnson, D., Steinke, J., & Kalinoski, Z. (2011). Cognitive ability and objective and subjective task complexity: Unique and differential effects on performance, self-efficacy, and cognitive appraisals. Journal of Organizational Psychology, 11(1), 73-86.

Stockhardt, S., Reinheimer, B., Volkamer, M., Mayer, P., Kunz, A., Rack, P., & Lehmann, D. (2016). Teaching phishing-security: Which way is best? IFIP International Conference on ICT Systems Security and Privacy Protection.

Sumner, A., Yuan, X., Anwar, M., & McBride, M. (2022). Examining factors impacting the effectiveness of anti-phishing trainings. Journal of Computer Information Systems, 62(5), 975-997.

Sun, J. C. Y., Yu, S. J., Lin, S. S., & Tseng, S. S. (2016). The mediating effect of anti-phishing self-efficacy between college students’ internet self-efficacy and anti-phishing behavior and gender difference. Computers in Human Behavior, 59, 249-257.

Taatgen, N. A., Van Rijn, H., & Anderson, J. (2007). An integrated theory of prospective time interval estimation: The role of cognition, attention, and learning. Psychological Review, 114(3), 577-598.

Tseng, S. T., Levy, P. E., Aw Young, S. H., Thibodeau, R. K., & Zhang, X. (2019). Frequent feedback in modern organizations: Panacea or fad? In L. A. Steelman & J. R. Williams (Eds.), Feedback at work (pp. 53-73). Springer.

Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. Science, 211(4481), 453-458.

Vance, A., Eargle, D., Eggett, D., Straub, D., & Ouimet, K. (2022). Do security fear appeals work when they interrupt tasks? A multi-method examination of password strength. MIS Quarterly, 46(3), 1721- 1738.

Verizon. (2022). 2022 Data breach investigations report. Verizon. https://www.verizon.com/ business/resources/reports/dbir/2022/masterguide/

Verkijika, S. F. (2019). “If you know what to do, will you take action to avoid mobile phishing attacks”: Self-efficacy, anticipated regret, and gender. Computers in Human Behavior, 101, 286-296.

Vishwanath, A. (2017). Getting phished on social media. Decision Support Systems, 103, 70-81.

Vroom, V. H. (1964). Work and Motivation. Wiley.

Wang, D. D., Durcikova, A., & Dennis, A. R. (2023). Security is local: The influence of the immediate workgroup on information security. Journal of the Association for Information Systems, 24(4), 1052- 1101.

Wang, J., Li, Y., & Rao, H. R. (2016). Overconfidence in phishing email detection. Journal of the Association for Information Systems, 17(11), 759- 783.

Wang, J., Li, Y., & Rao, H. R. (2017). Coping responses in phishing detection: An investigation of antecedents and consequences. Information Systems Research, 28(2), 378-396.

Waterloo News. (2019). Why people don't reply to your emails? https://uwaterloo.ca/news/news/whypeople-dont-reply-your-emails

Wen, Z. A., Lin, Z., Chen, R., & Andersen, E. (2019). What. hack: Engaging anti-phishing training through a role-playing phishing simulation game. Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems.

Werbach, K., & Hunter, D. (2012). For the win: How game thinking can revolutionize your business. Wharton Digital Press.

Wickens, C. D. (1984). Processing resources in attention. In R. Parasuraman & D. R. Davies (Eds), Varieties of attention (pp. 63-102). Academic Press.

Wright, R. T., Jensen, M. L., Thatcher, J. B., Dinger, M., & Marett, K. (2014). Research note—Influence techniques in phishing attacks: An examination of vulnerability and resistance. Information Systems Research, 25(2), 385-400.

Wright, R., Johnson, S. L., & Kitchens, B. (2023). Phishing Susceptibility in Context: A Multi-level Information Processing Perspective on Deception Detection. MIS Quarterly, 47(2), 803-832.

Xu, J., Benbasat, I., & Cenfetelli, R. T. (2014). Research note—The influences of online service technologies and task complexity on efficiency and personalization. Information Systems Research, 25(2), 420-436.

Zahedi, F. M., Abbasi, A., & Chen, Y. (2015). Fakewebsite detection tools: Identifying elements that promote individuals’ use and enhance their performance. Journal of the Association for Information Systems, 16(6), 448-484.

## Appendix A: Literature Review on Phishing

Table A1. Literature Review

<table><tr><td>Source</td><td>Journal</td><td>Phishing type</td><td>Focus</td><td>Theoretical backgrounds</td><td>Methods</td><td>Main findings</td></tr><tr><td>Arachchilage &amp; Love (2013)</td><td>CHB</td><td>Not specified</td><td>Factors of phishing avoidance motivation</td><td>· Technology threat avoidance theory</td><td>Survey</td><td>· Perceived threat, safeguard effectiveness, safeguard cost, and self-efficacy affect phishing avoidance motivation.</td></tr><tr><td>Arachchilage &amp; Love (2014)</td><td>CHB</td><td>Email</td><td>Factors of phishing avoidance motivation</td><td>· Technology threat avoidance theory</td><td>Survey</td><td>· Procedural knowledge and conceptual knowledge positively influence self-efficacy.· Self-efficacy influences avoidance motivation, which in turn affects avoidance behavior.</td></tr><tr><td>Herath et al. (2014)</td><td>ISJ</td><td>Email</td><td>Factors of intention to adopt an email authentication service</td><td>· Technology acceptance model· Technology threat avoidance theory</td><td>Survey</td><td>· Users' risk perceptions and evaluations of internal and external coping strategies affect their intention to adopt email authentication services.</td></tr><tr><td>Wright et al. (2014)</td><td>ISR</td><td>Email</td><td>Relative efficacy of phishers' influence techniques</td><td>· Persuasion and motivation theory</td><td>Field experiment</td><td>· Users are more vulnerable to phishing influence techniques offering a high degree of self-determination.</td></tr><tr><td>Zahedi et al. (2015)</td><td>JAIS</td><td>Website</td><td>Determinants of use and performance of fake-website detection tools</td><td>· Protection motivation theory</td><td>Controlled lab experiment</td><td>· Detector accuracy, detector speed influence coping appraisal (e.g., coping self-efficacy) while cost of error influences threat appraisal (e.g., threat severity).</td></tr><tr><td>Wang et al. (2016)</td><td>JAIS</td><td>Email</td><td>Determinants of overconfidence in phishing email detection</td><td>· Social cognitive theory</td><td>Survey experiment</td><td>· Cognitive effort reduces overconfidence.· Variability in attention allocation, dispositional optimism, and familiarity with the business entities in the emails increase overconfidence.</td></tr><tr><td>Algarni et al. (2017)</td><td>EJIS</td><td>Social network sites</td><td>Role of source characteristics in susceptibility to social engineering victimization</td><td>· Susceptibility to social engineering· Source credibility theory</td><td>Scenario-based experiment</td><td>· Source characteristics influence perceived sincerity, competence, attraction, and worthiness, which in turn affect susceptibility to social engineering victimization.</td></tr><tr><td>Goel et al. (2017)</td><td>JAIS</td><td>Email</td><td>Effect of phishing messages on phishing susceptibility</td><td>·Dual-processing model</td><td>Experiment</td><td>·Users' phishing susceptibility is significantly influenced by contextualized messages that appeal to their specific concerns.</td></tr><tr><td>Jensen et al. (2017)</td><td>JMIS</td><td>Email</td><td>Effectiveness of mindful training</td><td>·Mindful theory</td><td>Field experiment</td><td>·People who received mindfulness training are better able to avoid phishing attacks than people who received rule-based training.</td></tr><tr><td>Moody et al. (2017)</td><td>EJIS</td><td>Email</td><td>Role of situational and personality factors in phishing susceptibility</td><td>·Protection motivation theory·Social credibility theory</td><td>Experiment</td><td>·User's phishing susceptibility is significantly influenced by emails sent from a known source, curiosity, risk propensity, general internet usage, and internet anxiety.</td></tr><tr><td>Wang et al. (2017)</td><td>ISR</td><td>Email</td><td>Determinants and effects of coping adaptiveness in antiphishing training</td><td>·Extended parallel process model·Coping theory</td><td>Survey experiment</td><td>·Perceived phishing threat, phishing detection efficacy, and phishing anxiety influence coping adaptiveness.·Coping adaptiveness positively affects detection effort and detection accuracy.</td></tr><tr><td>Verkijika (2019)</td><td>CHB</td><td>Mobile</td><td>Determinants of mobile phishing avoidance behavior</td><td>·Technology threat avoidance·Regret theory</td><td>Survey</td><td>·Anticipated regret increases mobile phishing avoidance motivation and behavior.</td></tr><tr><td>Chen et al. (2020)</td><td>DSS</td><td>Email</td><td>Antecedents of phishing susceptibility</td><td>·Deception theory·Expectation confirmation theory</td><td>Survey</td><td>·Phishing susceptibility is influenced by detection process difficulty and detection outcome failure.</td></tr><tr><td>Frauenstein &amp; Flowerday (2020)</td><td>C&amp;S</td><td>Social network sites</td><td>The mediating role of information processing</td><td>·Personality traits·Heuristic-systematic model</td><td>Survey</td><td>·Agreeableness, conscientiousness, neuroticism, and openness significantly influence heuristic processing that in turn affects phishing susceptibility.</td></tr><tr><td>Jensen et al. (2020)</td><td>SSRN</td><td>Email</td><td>Role of gamification elements</td><td>·Gamification·Cognitive evaluation theory</td><td>Field experiment</td><td>·Gamification elements (e.g., leaderboard, rewards, punishment) are significantly related to an individual's phishing reporting.</td></tr><tr><td>Schuetz et al. (2020)</td><td>JMIS</td><td>Email</td><td>Factors of fear appeal outcomes</td><td>·Fear appeal model·Protection-motivation model·Construal level theory</td><td>Field experiment</td><td>·Concrete fear appeals are more effective than abstract fear appeals in affecting threat severity and response efficacy.</td></tr><tr><td>Silic &amp; Lowry (2020)</td><td>JMIS</td><td>Email</td><td>Organizational security training systems using gamification</td><td>• Gamification• Hedonic-motivation system adoption model</td><td>Design science using a field experiment</td><td>• Users' motivations and coping needs via gamified security training significantly increase their positive behavioral changes.</td></tr><tr><td>Abbasi et al. (2021)</td><td>ISR</td><td>Website</td><td>Proposing a phishing funnel model (PFM) that predicts user susceptibility to phishing websites</td><td>• Technology acceptance model• Protection motivation theory</td><td>Design science using a field experiment</td><td>• PFM outperforms competing models in predicting individuals' susceptibility to phishing websites.</td></tr><tr><td>Chen et al. (2021)</td><td>I&amp;M</td><td>Website</td><td>Factors and impacts of calibrated trust</td><td>• Automation trust and reliance</td><td>Controlled lab experiment</td><td>• Trust calibrator calibrates people's trust in detection tools against phishing websites.• People's calibrated trust is associated with their tool reliance, use, and performance against phishing websites.</td></tr><tr><td>Goel et al. (2021)</td><td>I&amp;M</td><td>Email</td><td>Role of financial incentives in security policy compliance</td><td>• Prospect theory</td><td>Controlled lab experiment</td><td>• Effect of financial incentives on compliance with information security policies on phishing is higher in the negative frame incentive condition than in the positive frame incentive condition.</td></tr><tr><td>Jaeger &amp; Eckhardt</td><td>ISJ</td><td>Email</td><td>Factors and impacts of situational information security awareness</td><td>• Situation awareness• Protection motivation theory</td><td>Eye tracking, Survey</td><td>• Individual-level (innate traits, experience) and system-level (design variations, warning signal) factors influence situational information security awareness.• Situational information security awareness increases perceived threat and perceived coping efficacy.</td></tr><tr><td>Jensen et al. (2021)</td><td>EJIS</td><td>Email</td><td>Role of susceptibility claims in IT security behavior</td><td>• Social judgment theory</td><td>Longitudinal field experiment</td><td>• Susceptibility claims influence precaution-taking behavior against phishing (i.e., overt attacks), but not against password cracking (i.e., furtive attacks).</td></tr><tr><td>Nguyen et al. (2021)</td><td>EJIS</td><td>Email</td><td>Role of overlearning in antiphishing training</td><td>• Overlearning• Signal detection theory</td><td>Longitudinal field experiment</td><td>• Overlearning leads to less phishing susceptibility and better email discrimination.• Mindfulness training is more effective than rule-based training and no training.</td></tr><tr><td>Sumner (2021)</td><td>JCIS</td><td>URL</td><td>Factors of effectiveness of antiphishing training</td><td>·Personality traits ·Technology threat avoidance theory</td><td>Pre- and post-training survey</td><td>·Training improves participants' average accuracy in detecting phishing URLs.</td></tr><tr><td>Sarno et al. (2022)</td><td>JEPA</td><td>Email</td><td>Developing and testing a phishing classification aid for antiphishing training</td><td>·Signal detection theory</td><td>Controlled lab experiments</td><td>·Phishing classification aid and basic feedback increase subjects' ability to discriminate phishing emails from legitimate ones</td></tr><tr><td>Frank et al. (2022)</td><td>DSS</td><td>Email</td><td>Putting forth a categorical model of multidimensional context that can be used to explain phishing susceptibility</td><td>·Contextualization</td><td>Field experiment in an international company</td><td>·Phishing susceptibility is sensitive to contextual factors</td></tr><tr><td>Wright et al. (2023)</td><td>MISQ</td><td>Email</td><td>Exploring contextual factors that may influence phishing susceptibility</td><td>·Contextual theory</td><td>Field experiment</td><td>·Individual's position in the knowledge flows of the organization and the impact of workgroup responsibilities on their cognitive processing influence phishing susceptibility</td></tr></table>

## Appendix B: Measurement Items

Unless specified, all items were measured with a 7-point Likert scale (1 = Strongly Disagree, 7 = Strongly Agree)

Manipulation Checks Example-Based vs. Mindful Feedback For detecting phishing emails, this feedback requires MIN1. A lot of thinking. MIN2. Cognitive effort.

Feedback Quantity How many tips for detecting phishing emails have you seen in the previous education? (One tip/Many tips) One tip = 0, Many tips = 1

Research Variables Age: Age in years

Gender (GEN) Male = 0, Female = 1

Prior Phishing Experience (PPE) How many times have you been phished in the past? (5-point scales anchored with “None at all” and “A great deal”)

Average Email Load (AEL): Number of emails received per day on average

Preliminary Training Detection Accuracy (PTDA) Is this a Phishing email? (Yes/No/Skip) Detection Accuracy: Incorrect = -1, Skip = 0, Correct = 1

Task-Focused Coping (TC) TC1. I made every effort to perform my goals. TC2. I concentrated hard on doing well.

Emotion-Focused Coping (EC) EC1. I worried about my inadequacies. EC2. I blamed myself for not doing better. EC2. I blamed myself for not knowing what to do.

Avoidance Coping (AC) AC1. I acted as though the task wasn’t important. AC2. I didn’t take the task too seriously. AC2. I decided there was no point in trying to do well.

Perceived Detection Efficacy (PDE) PDF1. It is possible to determine whether the email is phishing. PDF2. It is feasible to determine whether the email is phishing. PDF3. I am certain about my judgement of this email. PDF4. I am sure of my judgement of this email.

Antiphishing Outcomes (DAV and DAC) Is this a Phishing email? (Yes/No/Skip) Decision Avoidance: Decision Making = 0, Skip/I don’t know if it is a phishing message = 1 Detection Accuracy: Incorrect = -1, Skip/I don’t know if it is a phishing message = 0, Correct = 1

![](/api/attachments/FAU6CSDY/fulltext/images/4efd2836dd02c6693e244f7b9798d22261847a2f83d2703a292e195e383cb4a9.jpg)

![](/api/attachments/FAU6CSDY/fulltext/images/6e3adb482982a27fd71a6ef6ac9edfcac3983be2ae544303596d30abccad1c2b.jpg)

## Appendix C: Email Samples and Manipulations

![](/api/attachments/FAU6CSDY/fulltext/images/e7f0613e0273a627cd05a7121eac0ef196edf94435b6e11029c02c59be8bf0ab.jpg)

Security alert

![](/api/attachments/FAU6CSDY/fulltext/images/28deab38c49e6221a3110b46bda594204e5cb7213facb837e8148d876ff4308e.jpg)

New sign-in to your linked account Taryn231@gmail.com

Your Google Account was just signed into from a new Windows device You're getting this email to make sure it was you. Check activity

You received this email to let you know about important changes to your Google Account and services. © 2019 Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA

Your September 2019 Transaction History

Your transaction history for September 2019 is now available.

![](/api/attachments/FAU6CSDY/fulltext/images/a69c3089279818715c5316f4cce4d4aff160337c2de8dc636c773076c34b7142.jpg)

## Legitimate Email

Figure C1. Experiments 1 and 2: Email Samples in the Preliminary Test

![](/api/attachments/FAU6CSDY/fulltext/images/e5d550cf9d4f76c37eb0c098e3da36bb28620f8ac15b7d3c0d4054d76ac4d0c8.jpg)

New sign-in to your linked account

This is a phishing email! Hover your mouse on the link to see the website address at the bottom of your screen, it is not google.com!

Your Google Account was just signed into from a new Windows device. You're getting this email to make sure it was you.

http://accounts.go.com/AccountChooser?continue=http: /myaccount.my.com/nt/1sdjkhjhdkjhdcsjdhgcslkjhgl-is

You received this email to let you know about important changes to your Google Account and services © 2019 Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA

whenever you see an email that reguests you to click on a link or open an attachment, or provide information: STOp!Think... Check.

• Do not mindlessly act on an email by downloading a file, clicking a link, or replying.

Click here: http://www.2csv.ora Download attachment: attachment

• Does the request ask for private or proprietary information?

• Is the request unexpected or rushed?

• Does the request make sense?

• Why would the sender want me to do this?

• Consider for a moment what the email is asking you to do.

If you are not sure about the email, check with the sender using other methods such as phone calls.

## Example-Based Feedback Mindful Feedback Figure C2. Experiments 1 and 2: Feedback Materials

![](/api/attachments/FAU6CSDY/fulltext/images/012456b97257761d17bd93e6abbeb010de8a055f3055dc2d9cb9d9a9ab402463.jpg)

Customer Support Team <customersupport@netflix.com> Netflix-Restart Membershin

![](/api/attachments/FAU6CSDY/fulltext/images/6df09041021b483836c608352298e08d37c7cb84b6c6eb5a3fe8e005e74cc1fd.jpg)

![](/api/attachments/FAU6CSDY/fulltext/images/3d64b8aef74ea357e0c8319bcba1c995503e7a1e28eb87fd05f688c032414937.jpg)

We've cancelled your membership Friday, Oct 11

Access vour files on vour mobile device!

Obviously we'd love to have you back. If you change your mind, simply restart your membership to enjoy all the best TV shows and movies without interruption

We're here to help, if you need it. Visit the Help center for more info or contact us.

\- Your friends at Netflix

![](/api/attachments/FAU6CSDY/fulltext/images/239ff3da725a2895dc3e6b4621c40534f09f3e4ff1daaf67eb060ec01cb93f44.jpg)

The Dropbox mobile app lets you view and share your files from any mobile device, no matter where you are. You can even mark your most important docs for offline viewing.

With apps for Android, iPhone, iPad, and Windows phones and tablets, Dropbox has you covered no matter where you are!

Looking for a central place to create and share ideas? Try Dropbox Paper.

## Phishing Email

## Legitimate Emai

Figure C3. Experiments 1 and 2: Email Samples in the Main Test

![](/api/attachments/FAU6CSDY/fulltext/images/5d1121ca248cf047064058721f6cf63375691ea50f85cc436a76e1402af1abcd.jpg)

![](/api/attachments/FAU6CSDY/fulltext/images/42ce113133ffba1c66ce75f25f03f2d70fc9e945f53c999d4eb28cbff0b86d67.jpg)  
<sup>7</sup> For legitimate emails, we could not manipulate the appearance of the email. Thus, we chose legitimate emails with very short URLs such as “https://venmo.com” in the high phishing cue saliency group and chose legitimate emails with relatively long URLs such as “https://buy.itunes.apple.com” in the low phishing cue saliency group.

Example-based Feedback Mindful Feedback Figure C8. Experiment 4: Feedback Materials  
![](/api/attachments/FAU6CSDY/fulltext/images/16bd9d5a9051dcc86e467850758fb60d321de5ea61908cb699f1a70a7445f946.jpg)  
Figure C7. Experiment 4: Email Samples in the Preliminary Test

![](/api/attachments/FAU6CSDY/fulltext/images/d87d805b9216a2609c1b037ca64565c914b219f67212d6e8b1caa1c992268790.jpg)

![](/api/attachments/FAU6CSDY/fulltext/images/d6288819b50560d0cd3dc20faab5060d3b9c80fb471692a9f835e66f0fed79ef.jpg)

![](/api/attachments/FAU6CSDY/fulltext/images/ab977864d6dd1df3c481fa75aebcba778964b41062e9fb5081e69a618acc2b98.jpg)

Customer Support Team <customersupport@netflex.com> Netflix-Restart Membership

## NETFLIX

We're sorry to say goodbye!

We've cancelled your membership Monday, Sep 19

Obviously, we'd love to have you back. If you change your mind. simply restart your membership to enjoy all the best TV shows and movies without interruption.

We're here to help, if you need it. Visit the Help center for more info or contact us.

\- Your friends at Netflix

![](/api/attachments/FAU6CSDY/fulltext/images/df20862f1509c73d03c2b65af77d8948eee0270eb0e15df197f1f1155542bbba.jpg)

ReplyReply AllForward

Mon 9/19/2022 11:20 AM Facebook <facebookaccount@facebookmail.com> [CASE 9078596746] Important Message from Facebook

![](/api/attachments/FAU6CSDY/fulltext/images/2df474c66d6b9ee05ca8e37816fc53867c317fc1ce9fda4fe7af2c6da2d6cf84.jpg)

## Link-Embedded Phishing Email No-link-embedded Phishing Email Figure C9. Experiment 4: Phishing Emails in the Main Test

![](/api/attachments/FAU6CSDY/fulltext/images/3b02e5ceb480007bada4f171dc53c6e489911055af282b26601e9ef113794403.jpg)

Your August 2022 Transaction History

Your transaction history for August 2022

## View History on Venmo.com

please visit our Help Center at help.venmo.com

Mon 9/19/2022 10:47 AM

Dear MATT SMITH,

Please do not respond to this confirmation e-mail

## Link-Embedded Legitimate Email No-Link-Embedded Legitimate Email Figure C10. Experiment 4: Legitimate Emails in the Main Test

Appendix D: Results of Confirmatory Factor Analysis  
Table D1. Experiment 2

<table><tr><td rowspan="2"></td><td rowspan="2">Mean</td><td rowspan="2">SD</td><td rowspan="2">CR</td><td rowspan="2">AVE</td><td colspan="13">Correlation matrix</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td>Individual level</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1 FT</td><td>.50</td><td>.50</td><td>-</td><td>-</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2 Age</td><td>46.99</td><td>13.93</td><td>-</td><td>-</td><td>.06</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3 GEN</td><td>.48</td><td>.50</td><td>-</td><td>-</td><td>.02</td><td>-.26</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4 PPE</td><td>2.62</td><td>1.22</td><td>-</td><td>-</td><td>-.01</td><td>.14</td><td>-.07</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5 AEL</td><td>48.02</td><td>46.04</td><td>-</td><td>-</td><td>-.01</td><td>.26</td><td>.12</td><td>.03</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6 PTDA</td><td>-.05</td><td>.74</td><td>-</td><td>-</td><td>-.09</td><td>.27</td><td>-.08</td><td>.23</td><td>.14</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7 TC</td><td>6.43</td><td>.83</td><td>.88</td><td>.78</td><td>.06</td><td>-.14</td><td>.09</td><td>-.06</td><td>.02</td><td>.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8 EC</td><td>3.91</td><td>1.74</td><td>.89</td><td>.72</td><td>-.13</td><td>-.32</td><td>-.05</td><td>-.07</td><td>-.03</td><td>-.40</td><td>.08</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9 AC</td><td>1.96</td><td>1.33</td><td>.93</td><td>.82</td><td>-.06</td><td>-.03</td><td>-.01</td><td>.23</td><td>-.06</td><td>.06</td><td>-.45</td><td>.19</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Message level</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10 PDE</td><td>5.34</td><td>1.28</td><td>.95</td><td>.81</td><td>.06</td><td>.01</td><td>-.10</td><td>.15</td><td>.14</td><td>.24</td><td>.28</td><td>-.12</td><td>.02</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>11 RT</td><td>28.37</td><td>27.25</td><td>-</td><td>-</td><td>-.07</td><td>.09</td><td>-.08</td><td>.02</td><td>-.09</td><td>.16</td><td>.13</td><td>-.14</td><td>-.21</td><td>-.05</td><td>1.00</td><td></td><td></td></tr><tr><td>12 DAV</td><td>.03</td><td>.17</td><td>-</td><td>-</td><td>-.08</td><td>-.00</td><td>-.00</td><td>-.01</td><td>.14</td><td>-.03</td><td>-.11</td><td>.13</td><td>.23</td><td>-.20</td><td>-.08</td><td>1.00</td><td></td></tr><tr><td>13 DAC</td><td>.30</td><td>.94</td><td>-</td><td>-</td><td>.17</td><td>-.05</td><td>-.06</td><td>-.05</td><td>-.03</td><td>-.03</td><td>.08</td><td>-.03</td><td>-.08</td><td>.14</td><td>.02</td><td>-.06</td><td>1.00</td></tr><tr><td colspan="18">Note: SD = standard deviation; CR = composite reliability; AVE = average variance extracted. FT = feedback type (mindful = 0, example-based = 1); GEN = gender (male = 0, female = 1); PPE = prior phishing experience; AEL = average email load; PTDA = preliminary training detection accuracy; TC = task-focused coping; EC = emotion-focused coping; AC = avoidance coping; PDE = perceived detection efficacy; RT = response time to each quiz; DAV = decision avoidance; DAC = detection accuracy</td></tr></table>

Table D2. Experiment 3

<table><tr><td rowspan="2"></td><td rowspan="2">Mean</td><td rowspan="2">SD</td><td rowspan="2">CR</td><td rowspan="2">AVE</td><td colspan="14">Correlation matrix</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>Individual level</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1 FQ</td><td>.50</td><td>.50</td><td>-</td><td>-</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2 Age</td><td>38.13</td><td>9.51</td><td>-</td><td>-</td><td>.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3 GEN</td><td>.44</td><td>.50</td><td>-</td><td>-</td><td>.03</td><td>.13</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4 PPE</td><td>2.28</td><td>1.04</td><td>-</td><td>-</td><td>.03</td><td>.05</td><td>.15</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5 AEL</td><td>35.67</td><td>57.39</td><td>-</td><td>-</td><td>.10</td><td>.10</td><td>.11</td><td>.09</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6 PTDA</td><td>.16</td><td>.73</td><td>-</td><td>-</td><td>.06</td><td>.09</td><td>-.01</td><td>-.01</td><td>.05</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7 TC</td><td>6.63</td><td>.66</td><td>.82</td><td>.70</td><td>-.02</td><td>.16</td><td>.16</td><td>-.12</td><td>.05</td><td>.15</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8 EC</td><td>3.11</td><td>1.80</td><td>.90</td><td>.76</td><td>.01</td><td>-.03</td><td>.14</td><td>.13</td><td>-.03</td><td>-.22</td><td>-.16</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9 AC</td><td>1.49</td><td>1.12</td><td>.97</td><td>.92</td><td>.02</td><td>-.14</td><td>-.19</td><td>.16</td><td>-.04</td><td>-.10</td><td>-.58</td><td>.33</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Message level</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10 PCS</td><td>.50</td><td>.50</td><td>-</td><td>-</td><td>-.00</td><td>-.00</td><td>-.00</td><td>-.00</td><td>-.00</td><td>-.00</td><td>.00</td><td>-.00</td><td>-.00</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>11 PDE</td><td>5.49</td><td>1.37</td><td>.94</td><td>.79</td><td>-.01</td><td>-.01</td><td>-.07</td><td>-.05</td><td>.03</td><td>.15</td><td>.25</td><td>-.22</td><td>-.10</td><td>.10</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>12 RT</td><td>22.02</td><td>18.70</td><td>-</td><td>-</td><td>.06</td><td>.08</td><td>.03</td><td>.06</td><td>.01</td><td>.02</td><td>.06</td><td>.00</td><td>-.01</td><td>-.07</td><td>-.12</td><td>1.00</td><td></td><td></td></tr><tr><td>13 DAV</td><td>.02</td><td>.15</td><td>-</td><td>-</td><td>.00</td><td>.01</td><td>-.01</td><td>.01</td><td>-.03</td><td>-.00</td><td>-.03</td><td>.01</td><td>.02</td><td>-.04</td><td>-.27</td><td>.02</td><td>1.00</td><td></td></tr><tr><td>14 DAC</td><td>.53</td><td>.84</td><td>-</td><td>-</td><td>.00</td><td>.05</td><td>-.02</td><td>-.06</td><td>.02</td><td>.02</td><td>.11</td><td>-.12</td><td>-.12</td><td>.19</td><td>.22</td><td>-.03</td><td>-.10</td><td>1.00</td></tr></table>

Note: SD = standard deviation; CR = composite reliability; AVE = average variance extracted. FQ = feedback quantity (low = 0, high = 1); GEN = gender (male = 0, female = 1); PPE = prior phishing experience; AEL = average email load; PTDA = preliminary training detection accuracy; TC = task-focused coping; EC = emotion-focused coping; AC = avoidance coping; PCS = phishing cue saliency (low = 0, high = 1); PDE = perceived detection efficacy; RT = response time to each quiz; DAV = decision avoidance; DAC = detection accuracy

Table D3. Experiment 4

<table><tr><td rowspan="2"></td><td rowspan="2">Mean</td><td rowspan="2">SD</td><td rowspan="2">CR</td><td rowspan="2">AVE</td><td colspan="14">Correlation Matrix</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>1 FT</td><td>.49</td><td>.50</td><td>-</td><td>-</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2 ET</td><td>.53</td><td>.50</td><td>-</td><td>-</td><td>.09</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3 Age</td><td>37.58</td><td>10.16</td><td>-</td><td>-</td><td>.00</td><td>-.03</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4 GEN</td><td>.72</td><td>.45</td><td>-</td><td>-</td><td>-.01</td><td>-.09</td><td>.15</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5 PPE</td><td>2.67</td><td>1.15</td><td>-</td><td>-</td><td>.00</td><td>-.05</td><td>.16</td><td>.11</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6 AEL</td><td>45.27</td><td>89.55</td><td>-</td><td>-</td><td>-.06</td><td>-.12</td><td>-.04</td><td>.12</td><td>.19</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7 PTDA</td><td>-.09</td><td>.57</td><td>-</td><td>-</td><td>.07</td><td>.04</td><td>.07</td><td>.04</td><td>-.04</td><td>.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8 TC</td><td>6.46</td><td>.94</td><td>.93</td><td>.88</td><td>.00</td><td>-.12</td><td>.08</td><td>.03</td><td>.03</td><td>.03</td><td>-.06</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9 EC</td><td>3.93</td><td>1.80</td><td>.89</td><td>.73</td><td>.04</td><td>-.07</td><td>-.04</td><td>-.21</td><td>.08</td><td>-.05</td><td>-.19</td><td>-.06</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10 AC</td><td>1.29</td><td>.56</td><td>.89</td><td>.74</td><td>.05</td><td>.07</td><td>-.07</td><td>-.25</td><td>-.05</td><td>-.04</td><td>.12</td><td>-.36</td><td>.06</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>11 PDE</td><td>5.44</td><td>1.01</td><td>.95</td><td>.90</td><td>.04</td><td>.05</td><td>.10</td><td>-.07</td><td>.19</td><td>-.03</td><td>.00</td><td>.25</td><td>-.12</td><td>-.18</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>12 RT</td><td>34.21</td><td>23.60</td><td>-</td><td>-</td><td>.16</td><td>-.18</td><td>.24</td><td>.11</td><td>.10</td><td>-.05</td><td>.13</td><td>-.02</td><td>-.07</td><td>-.03</td><td>.00</td><td>1.00</td><td></td><td></td></tr><tr><td>13 DAV</td><td>.14</td><td>.43</td><td>-</td><td>-</td><td>.07</td><td>-.09</td><td>-.12</td><td>.02</td><td>-.08</td><td>.04</td><td>-.08</td><td>-.01</td><td>.11</td><td>-.05</td><td>-.30</td><td>.09</td><td>1.00</td><td></td></tr><tr><td>14 DAC</td><td>2.74</td><td>2.44</td><td>-</td><td>-</td><td>.19</td><td>.24</td><td>.03</td><td>-.09</td><td>-.03</td><td>-.09</td><td>.12</td><td>.06</td><td>-.05</td><td>.02</td><td>.02</td><td>.04</td><td>-.17</td><td>1.00</td></tr><tr><td colspan="19">Note: SD = standard deviation; CR = composite reliability; AVE = average variance extracted. FT = feedback type (mindful = 0, example-based = 1); ET = email type (no-link-embedded email = 0, link-embedded email = 1); GEN = gender (male = 0, female = 1); PPE = prior phishing experience; AEL = average email load; PTDA = preliminary training detection accuracy; TC = task-focused coping; EC = emotion-focused coping; AC = avoidance coping; PDE = perceived detection efficacy; RT = response time to each quiz; DAV = decision avoidance; DAC = detection accuracy</td></tr></table>

## About the Authors

Shihe Pan is an assistant professor at Tianjin University. She received her PhD from the University of Wisconsin-Madison. Her research interests include online user behaviors such as privacy and security-related behaviors, human machine collaboration, and problematic IT use.

Dong-Heon Kwak is an associate professor at Kent State University. He received his PhD from the University of Wisconsin-Milwaukee. His research interests include online helping behaviors, IT training, enterprise systems, and gamification.

Jungwon Kuem is an associate professor at the University of Albany. She received her PhD from the University of Wisconsin-Madison. Her research covers broad issues related to online user behavior in social networking services and online communities, IT addiction, phishing, and cyberloafing.

Sung S. Kim is the Peter T. Allen Professor at Wisconsin School of Business. His research covers broad issues related to online user behavior including habit, addiction, loyalty, switching costs, information privacy and security, gaming, and social networking.

Copyright © 2024 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
