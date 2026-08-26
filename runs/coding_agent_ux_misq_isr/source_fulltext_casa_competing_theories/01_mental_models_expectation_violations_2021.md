# Mental models and expectation violations in conversational AI interactions

![](/api/attachments/QASZKBAW/fulltext/images/022961a89c45f5afab4f5973a480a9acd6fa6515b89600d33fa98aa84bbe1272.jpg)

G. Mark Grimes <sup>a,\*</sup>, Ryan M. Schuetzler <sup>b</sup>, Justin Scott Giboney

<sup>a</sup> University of Houston, CT Bauer College of Business, Houston, TX, United States of America

<sup>b</sup> Brigham Young University, Provo, UT, United States of America

## A R T I C L E I N F O

Keywords: Conversational AI Chatbots Conversational agents Engagement

## A B S T R A C T

Artificial Intelligence is increasingly becoming integrated in many aspects of human life. One particular AI comes in the form of conversational agents (CAs) such as Siri, Alexa, and chatbots used for customer service on websites and other information systems. It is widely accepted that humans treat systems as social actors. Leveraging this bias, companies sometimes attempt to masquerade a CA as a human customer service representative. In addition to the ethical and legal questions around this practice, the benefits and drawbacks of a CA pretending to be human are unclear due to a lack of study. While more human-like interactions can improve outcomes, when users find out that the CA is not human, they may have a negative reaction that may cause reputation harm in the company. In this research we use Expectation Violation Theory to explain what happens when users have high or low expectations of a conversation. We conducted an experiment with 175 participants where some participants were told they were interacting with a CA while others were told they were interacting with a human. We further divided the groups so that some participants interacted with a CA with low conversational capability while others interacted with a CA with high conversational capability. The results show that expectations formed by the user before the interaction change how the user evaluates the CA bevond the actual performance of the CA. These findings provide guidance to developers not just of conversational agents, but also for other technologies where users may be uncertain of a system’s capabilities.

## 1. Introduction

Artificial intelligence (AI) systems are increasingly being used in a wide range of industrial, business, and consumer-facing applications. When interacting with AI systems, users may have preconceived ex pectations of what will happen during and after the interaction. The expectations users have of the interaction are based on their mental model of how they believe the system works—the “frameworks that in dividuals construct in order to support their predictions of the world around them” [1]—and are a driving factor for satisfaction when using information systems [2]. The outcome users experience, however, may either conform to or violate their expectations. When users are familiar with a system, their mental models of system usage generally correspond to the capabilities of the system, even if not the actual process by which the system works [3]. However, the widely varying capabilities of AI systems makes it difficult for users to establish mental models of their interactions that accurately reflect the capabilities of the system [4]. For example, users may significantly underestimate the capabilities of an AI system because they are accustomed to the limitations of systems that do not use AI. Conversely, users may overestimate the capabilities of a system that is described as using “artificial intelligence” due to the wide range of capabilities that can be described as AI—some of which are considerably more capable and impressive<sup>1</sup> than others. When the capability of an AI system fails to meet users’ expectations, satisfaction with and use of the system drop [5].

One of the most common ways in which users currently interact with AI systems is through conversational agents (CAs) such as Alexa, Siri, and other online chatbots. Many users are not aware of the full range of capabilities of the conversational AI systems they interact with. Systems such as these have a wide range of conversational capabilities such as the ability to take directions, provide navigation, answer questions, execute actions, and engage in recreational activities such as telling jokes, trivia, and playing games [6,7]. CAs typically execute these ac tions in a human-like manner, and in some cases it is not clear if the system a user is interacting with is an AI-enabled system, a non-AI sys tem, a human, or some hybrid combination [8–10]. Furthe complicating this assessment, interactions may start as being conducted by a CA, but delegate to a human if the CA encounters problems [11]. This has given rise to a number of legal, ethical, and business questions about how and if conversational agents should disclose that they are a computer [12,13].

It is widely accepted that people form social expectations with computer systems they interact with [14]. Social expectations of infor mation systems are especially pronounced when interacting with CAs, since conversational AI systems use cues of humanness to create a sense of social presence that is not present in traditional information systems such as websites, applications, and databases. When a CA has better conversational skills, users’ experience heightened feelings of social connection and engagement [15]. As with other AI systems, the capa bilities of conversational AI systems are typically not clearly understood by users, thus expectations may not be accurate. Compounding social expectation issues, some companies attempt to pass off conversational AI systems as human by including cues such as names, avatars, and typing indicators [16,17]—although the use of such cues is controversial and the outcome of doing so is unclear [13,18].

When users feel engaged with a system it can lead to many desirable outcomes including satisfaction [2], increased success in implementa tion of new software products [19,20], higher perceived performance of information systems [21], future intention to use a system [22], trusting beliefs [23], repurchase intentions [24], and increased decision-making performance [25]. While more human-like interactions can improve outcomes, if users find out that the CA is not human, they may have a negative reaction that may negatively impact the interaction [12]. Additionally, recent research has suggested that while there are many positive outcomes of interactions that have better social connection, “better” conversational interactions do not always lead to better out comes. For example, in scenarios where disclosure of sensitive infor mation is the goal, CAs that are less engaging elicit more disclosure [26]. Similarly, in scenarios involving deception, deceivers are less guarded when the CA is less humanlike [27]. Based on our review of the current state of the art, there is still much to be learned about the best approach for creating a CA that is most effective for a given application.

Given the complex nature of conversational AI interactions, the rapid proliferation of conversational AI systems, the general lack of under standing of conversational AI, and the recent surge in interest for de velopers to continue building systems that are “better” at engaging in conversations, we seek to answer this research question:

RQ: What is the impact of expectations being violated on users’ evalua tions of conversational AI systems?

This research question is at the intersection of artificial intelligence and human communication theory at a time in history when humans are increasingly interacting with conversational systems in their day-to-day lives. To answer this question, we bring together research on conver sational agents, engagement, and Expectation Violation Theory [28,29] to understand how conversational AI is evaluated under different levels of expectation of the agent’s capability. In the following pages we pro vide the theoretical background on which this model is built, then quantitatively test the model and discuss the results and implications.

## 2. Literature review and model development

The goal of this research is to investigate the interaction of expec tations and realizations of conversational AI performance on users evaluation of the CA interaction. In this section we review relevant literature on conversational AI and expectations that inform the current work. We present a model that describes how the capabilities of conversational AI systems impact users’ evaluation of the system and how conversational AI performance either meeting or violating expectations—positively or negatively—impacts the relationship be tween system capabilities and evaluations of the system.

## 2.1. Conversational artificial intelligence

Conversational AI agents are computer systems that use natural language processing to carry out human-like conversations with users [30]. These systems are often implemented in conversational agents (CAs)—also known as “chatbots”—and integrated with a user interface to facilitate humanlike communication [31]. Similar to how people form social connections when they interact with one another, it is commonly accepted that users form social connections with computer system when interacting with them [32]. Chatbots often use cues of humanness dur ing interactions to improve perceptions of social presence, engagement, anthropomorphism, and humanness.

Chatbots are used in a wide range of applications including providing customer service [33], stress management [34], technical support [35], conducting medical interviews [36,37], providing student counseling services [38], and distributing emergency response information [39]. Their use continues to grow, and the chatbot market is expected to grow from \$2.6 billion in 2019 to \$9.4 billion in 2024 [40].

## 2.1.1. Conversational AI capabilities

Capabilities are tasks that an AI can perform. AI systems have a wide range of capabilities depending on the application, such as making recommendations or predictions [41], controlling industrial equipment [42], autonomous driving [43], playing music, giving directions, or controlling Internet-of-Things (IoT) devices [44]. Unsurprisingly, ca pabilities directly impact evaluation of the AI. For example, if an AI system that is intended to recommend movies, for example, does a poor job of recommending movies, evaluation of its movie recommendation capability will be low.

In the case of conversational AI systems, relevant capabilities include the system being able to follow conversational norms such as the maxims of relation and relevance [45], exhibit appropriate delays and variety in response speed [27], and give responses that are tailored to be relevant to the conversation at hand and that exhibit variety [46]. Re sponses that are tailored exhibit verbal cues that signal understanding of the message provided by the sender. This is related to Grice’s “maxim of relation” conversational norm, which states that conversation partners will respond to each other during the conversation by giving responses that are relevant to the message provided by their conversation partner.

A CA can exhibit tailored responses by giving follow-up questions or comments that are relevant to the message provided by the user. In addition to being relevant, this also signals that the chatbot has some memory of things that were previously said in the conversation. A partner that does not give tailored responses violates the maxim of relation by responding with generic questions or comments. Not giving tailored responses not only violates the maxim of relation, but also fails to demonstrate any memory of the conversation, signaling a lack of comprehension. In addition to relevance, CAs that have high conversa tional capability also exhibit variety in their responses. That is, the CA will exhibit linguistic diversity during the interaction, even if the intention is to express the same message. Saying exactly the same thing repeatedly in a conversation is typically considered to be a violation of conversational norms. Social connection is enhanced in a text medium by varying the natural language capability of the conversational AI during communication [26,47,48]. Social cues help CAs create a shared connection [49–52] with more skilled CAs creating more social connection than less skilled ones [53].

There are many potential outcomes of how an AI system is evaluated, such as system acceptance [19,20], perceived performance of informa tion systems [21] and future intention to use a system [22]. In the current work we focus on the user’s perception of the CA’s conversational engagement during the interaction. Conversational engagement is the perception that a CA can “communicate well by acting and responding to user input thoughtfully” [54]. CAs that show understanding of user input are evaluated as better communicators [55–57], results in increased satisfaction [6], and are viewed as more engaging than those that do not have a natural flow of conversation [58]. Thus we present Hypothesis 1:

H1. . Conversational AI systems with higher conversational capability lead to higher perceived conversational engagement compared to conversational AI systems with lower conversational capability.

## 2.1.2. Conversational AI expectations

When users interact with chatbot systems, there are many cues they may use to develop an expectation—the result or action that a person predicts will occur [5,59]—of how the interaction will move forward. Cues are implicit or explicit signals that are used to infer traits and generate expectations about the system. Users commonly use cues to assess information systems, and cues have been shown to shape users perceptions of systems [60,61]. Cues for conversational agents fall into three categories: identity cues, non-verbal cues, and verbal cues [46]. By using identity cues, such as giving the bot a human name or photo graphic avatar, chatbot designers can imply the bot is human without explicitly deceiving users [62]. Nonverbal cues like artificial reading and typing delays, typing indicators, and emoji can further imply hu manness. Finally, verbal cues, such as the previously described tailored responses and variety, mimic natural conversation [63]. If the goal is to create a humanlike conversation, a combination of all three types of cues is required. In addition to cues in the agent itself, cues can be found in the chat environment. For example, a company could explicitly describe an agent as a computer program, as a human, or they may leave the humanness of the agent ambiguous (i.e., a “support representative”) [16].

In many applications, such as with the Siri voice assistant, there is no expectation that the conversational AI is human. In other applications, such as a front-line customer service bot on a website, the conversational AI system may attempt to masquerade as human. Still in others, implementation, the humanness of a conversational AI may be ambig uous. Because people treat information systems as social actors and people generate expectations of humans they interact with, it is under standable that people have, or will generate, expectations regarding conversational ability about both CAs and humans. Since users will form expectations, bot developers may wish to attempt to set a certain expectation for users based on the capabilities of the bot or the desired outcomes of the interaction. While chatbot technology is rapidly advancing, it is not yet to the point of perfectly mimicking human conversation, and people have higher expectations of the conversational capability of humans than they do computers [64]. Thus, telling users they will interact with a human sets higher expectations for the inter action than does telling users they will be interacting with a computer chatbot.

## 2.2. Expectation violations

Once initial expectations are set, users’ experience with the system serves to either confirm (if the system works as expected) or violate (if the system does not work as expected) their expectations. As described by Expectation Violations Theory (EVT) [28,29], when an expectation is violated, attention toward the violation is increased and the receiver applies either a positive or negative valence to the violation [29,65,66]. The increased salience of violations results in more stringent evaluation of the violation and causes the effect—positive or negative—to be stronger than if the expectation was confirmed [28]. A positive violation is a violation that is seen favorably—e.g., when a conversational system performs better than expected, or delights the user with a previously unknown capability. A negative violation, on the other hand, is a violation that was undesirable—e.g., when the system does not meet expectations, or a feature the user expects to work fails to work [28]. The incongruity between expectations and capabilities leads to a sense of violation as outlined in Table 1.

By the very nature of expectations, if a person has low expectations it is more likely that their expectations will be exceeded (i.e., a positive violation) than it is that their expectation will not be met (i.e., a negative violation). Therefore, we propose a simple negative direct effect of expectation on expectation violations:

Table 1  
Expectation, capability, and violation valence matrix.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Capability</td></tr><tr><td>High</td><td>Low</td></tr><tr><td rowspan="2">Expectation</td><td>High</td><td>No Violation</td><td>Negative Violation (Displeasure)</td></tr><tr><td>Low</td><td>Positive Violation (Delight)</td><td>No Violation</td></tr></table>

H2. : When low expectations are set, the magnitude of positive expectation violation will, on average, be higher than when high ex pectations are set.

Similarly, when a conversational AI system has very high capabilities it is more likely that the capability will exceed expectations than it is for a system that has low capabilities. Therefore, we propose a positive direct effect of system capability on expectation violation:

H3. : When conversational AI capability is high, the magnitude of positive expectation violation will, on average, be higher than when conversational AI capability is low.

Of more interest than these direct effects, however, is the interaction of expectations and capabilities, which determines both the direction and magnitude of expectation violation. For example, a parent may be delighted to learn that a child who causes trouble at home (low expec tation) is extremely well behaved and helpful at school (a previously unknown high capability). On the other hand, the parent of a child who is well behaved at home (high expectation) would merely be content to learn their child is well behaved and helpful at school. Even a system with low capabilities can meet or exceed expectations, provided ex pectations are low to begin with. Similarly, a system with high capa bilities can fail to meet expectations if expectations are very high. When expectations are not aligned with what users experience, this results in a violation of expectations. This violation can be positive or negative, depending on whether the interaction exceeds or falls short of expec tations. When the performance of a system matches the user’s expec tations, there is no violation. Violations also have magnitude such that a system that is close to expectations, but not a perfect match, will result in a smaller violation than one where expectations are wildly misaligned. Thus we present Hypothesis four:

H4. : Users experience a) no expectation violation when conversa tional AI capability and expectations of the conversation are congruent, b) a positive expectation violation when conversational AI capability exceeds expectations of the conversation, and c) a negative expectation violation when expectations of the conversation exceed conversational AI capability.

As described by EVT, people pay more attention to interactions when they experience violations. This attention brings about a shift in the evaluation of the system [67,68]. Prior research has demonstrated that people who experience positive violations have a greater satisfaction than people who receive a confirmation of high expectations, people that experience negative violations have more unfavorable evaluations when compared to confirmation of low expectations, and when no violation occurs, the expectation is confirmed and does not impact the user’s evaluation of the system [64,67,68]. Therefore, we present hy pothesis five:

H5. : Expectation violation moderates the relationship between conversational AI capability and evaluation of conversational engagement.

Our full research model is presented in Fig. 1.

## 3. Method

One hundred eighty-nine participants from Amazon’s Mechanical Turk (mTurk) completed our human intelligence task (HIT) which was described as “Evaluate a movie recommender chat system”. Participants were paid \$2 to participate in the experiment which took about 15 min to complete (equivalent to approximately \$8/h). Workers on mTurk have been shown to accurately reflect characteristics of the general public [69]. Of the 189 participants who completed the study, 14 failed attention checks and were removed from the analysis. The average age of the 175 remaining participants was 36.2 years (SD = 11.3) and 72 participants were female (41%). The experiment was a 2 × 2 betweensubjects design in which participants were either told they would chat with a human (high expectation condition) or a chatbot (low expecta tion condition) and interacted with a conversational AI that exhibited either high or low conversational AI capability.

## 3.1. Research stimulus and task

After accepting the task, participants were randomly assigned and exposed to the expectation setting manipulation. where they were told: “In just a moment you will be placed in an online chat with [a computer chatbot | another person] to receive a movie recommendation,” where “computer chatbot” is intended to set a low expectation of conversa tional engagement and “another person” is intended to set a high expectation of conversational engagement. This manipulation is based on prior research which suggests people typically have higher expecta tions of conversational capability for humans than they do for computers [64]. There is discussion in online mTurk worker communities (for example, http://www.reddit.com/r/mturk) of HITs that do in fact pair mTurk workers with other humans for chat interactions, thus making this manipulation plausible for participants. Following the manipula tion, participants completed a short survey using a 7-point Likert scale anchored at “Strongly agree” and “Strongly disagree”. The survey con tained twelve items, eleven of which were masking items used to obscure the purpose of the survey and one key item (“I believe the conversation will be engaging.”), which was used as a manipulation check of the participant’s expectation of the interaction..

After completing the survey, participants were redirected to a chat interface where they were randomly assigned to interact with one of two custom CAs which were developed using the ChatScript language [70]. As described in the task, the CA conducted a short interview about their preferences, ostensibly to provide a movie recommendation based on the participants’ responses to a series of questions about their interests and preferences. One CA was designed to exhibit high conversational capability by providing responses that were tailored and exhibited va riety. The other CA was designed to exhibit low conversational skill by provided responses that were generic, repetitive, and non-relevant. As illustrated in Table 2, both CAs asked the same base questions (1a – 5a), but for the follow up questions (1b – 4b), the low conversational capa bility CA responded always responded with “Okay. Can you tell me more

## Table 2

Low and high skill conversation flows.

<table><tr><td>Low conversational capability CA</td><td>High conversational capability CA</td></tr><tr><td>1a. What genre or type of movie do you usually like?</td><td>1a. What genre or type of movie do you usually like?</td></tr><tr><td>1b. Okay. Can you tell me more about that?</td><td>1b. [Follow-up question based on response to 1a]</td></tr><tr><td>2a. Alright, what is your favorite outdoor activity?</td><td>2a. Alright, what is your favorite outdoor activity?</td></tr><tr><td>2b. Okay. Can you tell me more about that?</td><td>2b. [Follow-up question based on response to 2a]</td></tr><tr><td>3a. Okay, now what is your favorite type of food?</td><td>3a. Okay, now what is your favorite type of food?</td></tr><tr><td>4b. Okay. Can you tell me more about that?</td><td>3b. [Follow-up question based on response to 3a]</td></tr><tr><td>4a. In your opinion, what is the best way to start a day?</td><td>4a. In your opinion, what is the best way to start a day?</td></tr><tr><td>4b. Okay. Can you tell me more about that?</td><td>4b. [Follow-up question based on response to 4a]</td></tr><tr><td>5a. Last question-What is your favorite type of music to listen to?</td><td>5a. Last question-What is your favorite type of music to listen to?</td></tr><tr><td>5b. Cool. Based on everything you’ve said, I will now generate a recommendation. Please take this survey while I work on that.</td><td>5b. Cool. Based on everything you’ve said, I will now generate a recommendation. Please take this survey while I work on that.</td></tr></table>

about that?” while the high conversational capability CA used natural language processing to give a tailored follow up question.

In order to provide the tailored responses, a corpus of appropriate responses for anticipated answers to the base questions was developed by the research team (see Table 3 for examples). For each base question, the research team wrote relevant responses for 10–20 keywords we anticipated the participant might say in response to the base question. For many keywords, ChatScript has “topics” that group together similar words—for example, the “biking” response can be triggered by the participant saying any version of the word “bike” (e.g., “biking”, “bikes”, etc.) or any commonly related word $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . ,$ , “cycling”, “bicycle”, etc.). Similarly, the “comedy” response is triggered by a variety of related words such as “funny”, “humor”, “laugh”, etc. The bot was then pilot tested and responses were created for any unanticipated answers to the base questions. The CA did not attempt to give a tailored response to the last question, but instead replied with “Cool. Based on everything you’ve said, I will now generate a recommendation. Please take this survey while I work on that.” For all follow up responses it was important that the response be a question, so the participant had to give another response to keep the conversation going. If the high capability CA was not able to make a tailored response, it gave one of a few reasonable but generic responses such as “What is it about those movies you like?” or “What other things do you like to do outside?” Overall, the high conversational capability CA was able to respond with a tailored mes sage 92.7% of the time.

Table 3  
Example high conversational capability CA responses.

<table><tr><td>Topic/keywords</td><td>High conversational capability CA response</td></tr><tr><td colspan="2">Favorite movie genre</td></tr><tr><td>Horror</td><td>Do you like the blood and guts, or just like to be scared?</td></tr><tr><td>Drama</td><td>Do you feel like your life is lacking drama?</td></tr><tr><td>Comedy</td><td>Who do you think is funnier, Will Smith or Will Ferrell?</td></tr><tr><td colspan="2">Favorite outdoor activity</td></tr><tr><td>Biking</td><td>Nice. Do you usually bike by yourself or in a group?</td></tr><tr><td>Hiking</td><td>Hiking in the mountains, or in the woods?</td></tr><tr><td>Swimming</td><td>Do you like swimming in pools or open water?</td></tr><tr><td colspan="2">Favorite type of food</td></tr><tr><td>Pasta</td><td>Do you think you could ever give up eating pasta?</td></tr><tr><td>Steak</td><td>How do you like your steak prepared?</td></tr><tr><td>Pizza</td><td>I love Hawaiian pizza. How do you feel about pineapple on pizza?</td></tr><tr><td colspan="2">Best way to start a day</td></tr><tr><td>Coffee</td><td>Do you have coffee every morning?</td></tr><tr><td>Sleeping in</td><td>I love to sleep in. What time do you usually get up?</td></tr><tr><td>Exercise</td><td>You are more dedicated than I am. What are your health goals?</td></tr></table>

![](/api/attachments/QASZKBAW/fulltext/images/bec280626bbbb8f96f641d5acd5783f97e60a5256a3bcb15ca1c6058ef0a5a25.jpg)  
Fig. 1. Research model.

Upon completion of the interaction with the CA, participants were redirected to a survey containing validated items to measure engage ment. After the survey, all participants received the same movie recommendation regardless of their responses. Note that the recom mendation occurred after all other measures had been collected, thus it could not have impacted any other results. Participants were then asked if they had any comments for the research team and were presented with a debriefing statement that revealed their input had not been used to generate the recommendation, then given a validation code to verify their completion of the study for the mTurk HIT.

## 3.2. Measurement

In the post-experiment survey we measured evaluations of conver sational engagement with a 7-point Likert scale anchored at “Strongly Agree” and “Strongly Disagree” using six measures about the partici pant’s chat partner: skill, politeness, engagement, responsiveness, thoughtfulness, and friendliness [71]. Expectation violation was oper ationalized in two ways. For H2–4, expectation violation was calculated using the technique described in [72] in which the expectation of engagement (measured just after the expectation setting manipulation, but before the interaction) was subtracted from the reported level of engagement (measured after the interaction. This resulted in a bipolar scale centered around zero with positive values if the final evaluation was higher than the initial expectation and negative values if it was lower than the initial expectation. However, since the evaluation of engagement itself is used in the testing of H5, in order to maintain orthogonality of the constructs we simply code expectation violation as − 1, 0, or 1 based on the combination of conditions such that participants where high expectations were set (told human), but they interacted with a low-capability CA were coded as − 1 (negative violation), participants where low expectations were set (told chatbot), but they interacted with a high-capability CA were coded as 1 (positive violation), and partici pants where the expectation and experience conditions were congruent (told human/high capability and told chatbot/low capability) were coded as 0 (no violation).

## 4. Analysis

## 4.1. Manipulation checks

Before investigating the impact of capability and expectation viola tion on engagement, we first check to ensure the manipulations had the intended effect. As previously described, we operationalized conversa tional capability with two factors suggested by previous research: 1) tailored responses and 2) variety in responses. With regarding to tailoring, the high-capability CA gave tailored responses 92.7% of the time, while the low-capability chatbot gave no tailored responses. Re view of the chat transcript showed that the responses given by the chatbot were appropriately tailored to the conversational at hand. To test for variety, lexical diversity was calculated using the type-token ratio (TTR) for the follow up responses each participant received $( \mathrm { i . e . , }$ responses 1b – 4b in Table 2). TTR is a ratio of how many unique words (types) are in a document divided by the total number of words (tokens) in the passage [73]. A higher TTR indicates more variety in the text. The average TTR for the low-capability chatbot (which gave the exact same response four times) was $\mathbf { M } = 0 . 2 5 , \mathbf { S } \mathbf { D } = 0 .$ . The average lexical diversity for the high-capability chatbot was $\mathrm { M } = 0 . 7 8 , \mathrm { S D } = 0 . 0 4$ . This difference is statistically significant, $\ t ( 1 7 3 ) = 1 2 . 8 7 , p < 0 . 0 0 1$ . Based on these two criteria, the conversational capability manipulation was successful.

To test the expectation setting manipulation, we observed the re sponses to the pre-interaction question, “I believe the conversation will be engaging.” We found that participants in the low expectation group responded on the seven-point scale with an average of 4.91 (SD = 1.47), while participants in the high expectation group responded with an average of 5.33 (SD = 1.13). This difference is statistically significant, t $( 1 5 9 . 3 4 ) = 2 . 1 1 , p = 0 . 0 2 , \mathrm { d } = 0 . 3 3 )$ , thus indicating the expectation setting manipulation was successful.

With regard to the reliability of the items used to measure engagement, we calculated Cronbach’s alpha which resulted in a value of 0.90, indicating high reliability.

## 4.2. Results

To show the main effect of conversational capability on evaluation of conversational engagement (H1), we conducted a between-subjects ttest. Participants evaluated conversational engagement more highly when interacting with the high capability CA $( \mathrm { M } = 5 . 6 0 , \mathrm { S D } = 1 . 0 4 )$ compared to the low capability $\mathbf { C A } \left( \mathbf { M } = 4 . 5 8 , \mathbf { S D } = 1 . 5 7 \right) , \mathbf { t } ( 1 3 2 . 8 6 ) =$ $4 . 9 5 , \mathrm { p } < 0 . 0 0 1 , \mathrm { d } = 0 . 8 6$ (Fig. 2). This provides support for hypothesis one.

Hypotheses two and three describe the main effects of expectations and capabilities, respectively, on expectation violations. As described in the measurement section, expectation violation was calculated by sub tracting the value of expectation of conversational engagement from the final rating of conversational engagement [72]. To test hypothesis two, a between-subjects t-test was conducted to test whether participants with low expectations had higher values of expectation violation than par ticipants with high expectations. The expectation violation for the low expectation group is 0.51 (SD = 1.51), compared to 0.02 (SD = 1.31) for the high expectation group. This difference is significant, t(163.95) = $2 . 2 0 , p = 0 . 0 3 , \mathrm { d } = 0 . 3 4 _ { \mathrm { \Omega } }$ , lending support to H2.

![](/api/attachments/QASZKBAW/fulltext/images/3d1afe6decdc0b2cb48253ba7b97298e53f31fa430efc7a5104b2c409e6937b4.jpg)  
Fig. 2. Main effect of conversational capability on engagement.

Hypothesis three posits that, controlling for expectations, when user interact with a CA that has high conversational capability, expectation violation will be more positive than when they interact with a CA has low conversational capability. The expectation violation for participant that interacted with the high capability CA was 0.73 (SD = 1.37), whereas the expectation violation for participants that interacted with the low capability CA $\mathsf { w a s } - 0 . 2 9 ( \mathrm { S D } = 1 . 4 3 )$ . A between-subjects t-test showed this difference to be statistically significant, t(165.59) = 4.49, p $< 0 . 0 0 1 , \mathrm { d } = 0 . 7 0$ , thus supporting H3.

While hypotheses 1–3 mirror many previous findings, hypotheses four and five represent the core contribution of this paper by illustrating how the incongruence of expectations and capabilities results in expectation violations (H4) that affect evaluation of conversational AI systems (H5) above and beyond the capabilities alone (as illustrated in H1). Hypothesis four suggests that users experience no violation when expectations and capabilities are congruent, a positive expectation violation when capability exceeds expectation, and a negative expec tation violation when expectation exceeds capability.

To test H4, we grouped participants based on whether the capabil ities of the CA they interacted with were congruent with the expecta tions that were set. Participants exposed to the low expectation manipulation that interacted with a high-capability chatbot were put into the “Capability above expectations” group. Participants exposed to the high expectation manipulation that interacted with a low-capability chatbot were put into the “Capability below expectations” group. Par ticipants exposed to the low expectation condition that interacted with a low-capability chatbot and those with exposed to the high expectation condition that interacted with a high-capability chatbot were put into the “Capability congruent with expectations” group. We ran a onesample t-test on the expectation violation for each group to determine if the group’s mean was significantly different than zero. A value of zero indicates that the pre-interaction expectation of the engagement was the same as their post-interaction assessment, a positive value means their evaluation was higher than their expectation, and a negative value means their evaluation was lower than their expectation.

For the “Capability congruent with expectations” group (H4a), the one sample t-test showed the value for expectation violation to not be significantly different than zero, $\mathbf { M } = 0 . 1 2 , \mathrm { t } ( 6 2 ) = 0 . 8 5 7 , p = 0 . 3 9 .$ For the “Capability above expectations” group (H4b), the one sample t-test showed a significant positive difference from zero, M = 2.16, t(31) = 12.178, p < 0.001. For the “Capability below expectations” group (H4c), the one sample t-test showed a significant negative difference from zero, $\mathbf { M } = - 1 . 0 0 , \mathrm { t } ( 3 4 ) = - 5 . 1 4 8 , \mathrm { p } < 0 . 0 0 1$ . Based on these results, H5 was supported. This difference is illustrated graphically in Fig. 3.

Hypothesis 5 describes the interaction of conversational capability and expectation violation, which is illustrated graphically in Fig. 4. The panel on the left represents the low expectation condition where par ticipants were told they would be chatting with a chatbot, while the panel on the right represents the high expectation condition where participants were told they would be chatting with a human. The left most point in each panel represents the pre-interaction reported expectation of engagement.

We found participants evaluated the conversational engagement of the low-capability chatbot (left panel of Fig. 4) more favorably when they had low expectations (M = 4.82, SD = 1.55) than they did when they had high expectations (M = 4.33, SD = 1.58)—that is, participants rated the same chatbot differently depending on the expectations that were set. Further, not only is the absolute difference in evaluation substantial (a change of 0.5), but the relative difference between expectation and final evaluation is much lower in the low-expectation condition—a non-significant drop of 0.1 $( \mathrm { t } ( 7 5 . 1 1 ) = - 0 . 3 1 , p = 0 . 7 6 ,$ d = 0.07—indicating there was no expectation violation, while the relative difference in expectations and evaluations is substantially greater in the high-expectation condition—a drop of 1.0 (t(55.65) = − 3.57, p < 0.001, d = 0.96—suggesting there was a negative expecta tion violation.

![](/api/attachments/QASZKBAW/fulltext/images/bb650e9c835c1b90be2bb289696f67a9156153e710ffa662614870d9b68cacd1.jpg)  
Fig. 3. Expectation violation valence.

Similarly, when interacting with the high-capability chatbot (right panel of Fig. 4), we see a larger increase between expectation and evaluation (an increase from 4.9 to 5.5) when low expectations were set, than when high expectations where set (an increase from 5.3 to 5.7). Both of the differences from expectations are significant, t(115.67) = $2 . 4 5 , p = 0 . 0 2 , \mathrm { d } = 0 . 4 6$ for the low capability CA and $\operatorname { t } ( 1 1 0 . 9 9 ) = 2 . 1 4 ,$ p = 0.03, d = 0.40, for the high capability CA. These results suggest that users will more heavily penalize a CA that fails to meet expectations than be delighted by a CA that exceeds their expectations.

Ultimately this shows that incongruence of expectations and per formance will lead to more extreme positive or negative expectation violations, which will serve to influence evaluation of the conversational AI agent above and beyond the capability of the agent itself. The results of the hypothesis testing are summarized in Table 4, and the practical importance of this finding is described in the discussion section.

## 5. Discussion

The capabilities of AI systems, and conversational AI systems in particular, vary widely and their functionality is not always apparent to users. This leads to situations where users may come in to an interaction with expectations that are far above or far below the actual capabilities of the system. To ensure users have a good experience, companies may wish to make efforts to set expectations. However, it is currently unclear how companies should approach this—should the company try to impress users with high expectations, or should companies set modest expectations and allow their users to be delighted when expectations are exceeded?

This study demonstrated that when users are told they will interact with a human rather than a bot, their expectations for the interaction are elevated. Prior research has shown that expectations influence evalua tions of systems such that people are delighted when expectations are exceeded and disappointed when expectations are not met. This is operationalized in a chatbot when the bot responds well, gives relevant information quickly, and does not experience the technical glitches that are common with conversational agent technology. However, meeting these goals is difficult as this technology is changing rapidly, so technical issues are common [74]. The same rudimentary chatbot is rated better when viewed by someone who expects a bot compared to someone who expects a human. Thus, as our study shows, it is best for companies to set modest expectations of their chatbot and let users be pleasantly sur prised when their expectations are exceeded.

Table 4  
![](/api/attachments/QASZKBAW/fulltext/images/fce52770c0bf5acac91d95da36290ac75ac96d56962f2089f94b2982ec0b9029.jpg)

![](/api/attachments/QASZKBAW/fulltext/images/ac6485c822b0f134ae648928118afa2a1212fcbddc939c83f7c7f944903ca51d.jpg)  
Fig. 4. Interaction of conversational capability and expectation on rating of engagement.

<table><tr><td>Hypothesis</td><td>Support</td></tr><tr><td>H1. Conversational AI systems with higher conversational capability lead to higher evaluation of conversational engagement compared to conversational AI systems with lower conversational capability.</td><td>Yes</td></tr><tr><td>H2. When low expectations are set, the magnitude of positive expectation violation will, on average, be higher than when high expectations are set.</td><td>Yes</td></tr><tr><td>H3. When conversational AI capability is high, the magnitude of positive expectation violation will, on average, be higher than when conversational AI capability is low.</td><td>Yes</td></tr><tr><td>H4: Users experience a) no expectation violation when conversational AI capability and expectations of the conversation are congruent, b) a positive expectation violation when conversational AI capability exceeds expectations of the conversation, and c) a negative expectation violation when expectations of the conversation exceed conversational AI capability.</td><td>Yes</td></tr><tr><td>H5: Expectation violation moderates the relationship between conversational AI capability and evaluation of conversational engagement.</td><td>Yes</td></tr></table>

Our findings also show that with a sufficiently good bot, you can set high expectations and still exceed them. Similarly, a bad bot can fail to meet even the lowest of expectations. Our CA with high conversational capability received higher scores for engagement than users expected. While our good bot was far from perfect, using short, tailored follow up questions, it was able to connect with users to create a significantly better feeling of engagement. This serves to illustrate that even if bots are not perfect, by putting some effort into ensuring users do not get exceptionally bad responses, they can still be “good enough" as long as expectations are set appropriately. However, it is very important that companies using chatbots need to clearly understand what their bots capabilities are before deciding how to set expectations.

These implications are especially important for companies consid ering deceiving users by saying (or implying) they are interacting with a human when in fact they are interacting with a bot. As more companies use conversational technology as the first line of customer service, this type of deception will lead to greater anger and frustration when the technology fails. Beyond the ethical and legal considerations of misleading customers, these results suggestion that from a business perspective companies that use customer service chatbots should clearly indicate to customers that they are talking to AI. This will help cus tomers by anchoring their expectations. It will help the company by reducing the number of negative expectation violations that lead to dissatisfied customers.

Finally, our study contributes to the understanding of expectations and expectation violations by extending it to the context of conversa tional technology. Prior research has extensively investigated this in human-human communication [28], and prior work has suggested human treat computers as social actors [14,75], however as computers become more humanlike, researchers must consider whether traditional human communication theories should be used to explain humancomputer interactions, or whether distinct theories are needed. In this work we have shown that one theory typically used to describe human communication—expectation violation theory—maintains its efficacy in this setting. Without explaining to users how the bot will work, or how the conversation will flow, the simple prompt of conversation with a human or a bot was sufficient to create an expectation for users what will happen.

## 6. Limitations and future research

While this work provides a good foundation for understanding ex pectations and evaluations of conversational AI systems, this is certainly not an exhaustive exploration of conversational agents and expectations. We anticipate many avenues for future research into the combination of these topics. For example, the boundary conditions of this paper are limited to text-based conversational AI systems. While we believe the idea of expectation violation and evaluation will apply to many infor mation systems scenarios, we are not able to generalize beyond conversational AI. This will be a great opportunity for future research into other AI systems such as recommendation agents, self-driving ve hicles, and other cyber-physical systems.

Second, this research explicitly told users they would be interacting with a chatbot or a human as a conversation partner. We did not study what happens when users are not told what they will be interacting with. Some early pilot studies we conducted suggested that users have pre conceived ideas as to what they will be interacting with. It is possible that despite what we told participants they assumed their chat partner was a computer, simply because of the context of the online interaction. We considered alternative approaches to capture this information early in the experiment, however we concluded that asking participants in the beginning if they assumed they would interact with a human or a computer would likely have as strong of an anchoring effect as simply telling them what they will be interacting with. Therefore, we did not include that in this study. However, addressing this issue of precon ceived notions of the interaction is an open research opportunity.

Third, the scenario of a movie recommendation was somewhat contrived. The chatbot asked the questions and followed up exactly once to each of the user responses. We asked people to evaluate the system prior to getting a movie recommendation. However, we were asking for their evaluation of the interaction, not the movie recommendation itself. There may be a connection between the chatbot and the evaluation of the system as a whole that should be investigated in future research.

Finally, there appeared to be a substantial skew toward higher levels of reported expectation. While the difference in expectations was sig nificant, we believe it is likely that many participants in the low ex pectations condition over reported their true expectations due to response biases such as social desirability or extreme responding. Also, at the time they reported their expectation they had very limited in formation about the interaction from which to form an expectation. Expectations are known to change over time, so future research should consider more accurate ways to measure expectations, and measure changes in expectations throughout the course of the experiment, rather than only at the onset and conclusion of the study.

Relatedly, another avenue for additional research would be to investigate preconceived notions of AI capabilities. In the analysis of reported expectations, we noticed that while people generally expected high performance out of human partners, there was a great deal more variability in expectations for computer partners. Consider that, as described in the manipulation check for expectation setting, participants that were told they would be interacting with a human rated their expectation with a mean of 5.33 (SD = 1.13) on the seven-point scale while participants that were told they would be interacting with a computer rated their expectation with a mean of 4.91 (SD = 1.47). While this difference is significant, it appears likely that expectations were influenced by a response bias in which participants rated their expec tation of the interaction fairly high regardless of their actual expecta tion. Additionally, as illustrated in Fig. 5, there is far more variance in the condition where participants were told they would be interacting with a computer compared to the condition where participants were told they would be interacting with a human. It is possible that this is due to the fact that while most people would agree that humans can typically engage in a chat conversation, people’s experience with and expectation of computers is much more widely varied. This is a potential area for future research to investigate.

## 7. Conclusion

The purpose of this study was to answer the question: What is the impact of expectations being violated on users’ evaluation of conversational AI systems? To this end we performed an experiment that showed that 1) expectations can be set by telling a user they are interacting with a bot or a human, 2) incongruence of expectations and capabilities will lead to expectation violations, 3) expectation violations evaluations of the CA above and beyond the actual performance of the agent. Of great interest, we found that the same low-quality CA was rated much more favorably when low expectations were set than when high expectations were set, and that evaluation of a high-quality CA was only marginally impacted by expectations. Ultimately, we have learned that setting expectations through cues of AI capability congruent to or less than the actual AI capability can increase engagement of conversational AI systems, thereby enabling developers of conversational AI systems to create conversational agents that engage with users more effectively.

![](/api/attachments/QASZKBAW/fulltext/images/b9206dcb860d0b28015361afdc5791fa8da450793e29ace7b6d6f3b9eb6e632d.jpg)  
Fig. 5. Expectation of engagement by expectation set.

## References

[1] E. Phillips, S. Ososky, J. Grove, F. Jentsch, From tools to teammates: toward th development of appropriate mental models for intelligent robots, Proc. Hum. Factors Ergon. Soc. (2011) 1491–1495, https://doi.org/10.1177 1071181311551310.

[2] R. Vaezi, A. Mills, W. Chin, H. Zafar, User satisfaction research in information systems: Historical roots and approaches, Commun. Assoc. Inf. Syst. 38 (2016) 501–532, https://doi.org/10.17705/1CAIS.03827

[3] H.A. Simon, J.R. Hayes, The understanding process: problem isomorphs, Cogn Psychol. 8 (1976) 165–190.

[4] R. Budiu. Mental Models for Intelligent Assistants. http://www.nngroup.com/artic les/how-to-rate-the-severity-of-usability-problems/, 2019.

[5] S. Brown, V. Venkatesh, S. Goyal, Expectation confirmation in information systems research: a test of six competing models, MIS Q. 38 (2014) 729–756. http://aisel. aisnet.org/cgi/viewcontent.cgi?article=3190&context=misq.

[6] A. Purington, J.G. Taft, S. Sannon, N.N. Bazarova, S.H. Taylor, “Alexa is my new BFF”: Social roles, user satisfaction, and personification of the Amazon Echo, Conf. Hum. Factors Comput. Syst. Proc. (2017), https://doi.org/10.1145 3027063.3053246. Part F1276.

[7] T. Strohmann, D. Siemon, S. Robra-Bissantz, Designing virtual in-vehicle assistants: design guidelines for creating a convincing user experience. AIS Trans, Human: Comput. Interact 11 (2019) 54–78. https://doi,org/10.17705/1thci,00113.

[8]. Jeremy Hsu, Out of the way, human! Delivery robots want a share of vour sidewalk - scientific American. Sci. Am. (2019). https://www.scientificamerican.com/artic e/out-of-the-wav-human-delivery-robots-want-a-share-of-vour-sidewalk (accessed February 25, 2020)

[9] L. Wise, New media doesn't mean new rules: the challenges of chatbots, Soc, Media Week. (2018). https://socialmediaweek.org/blog/2018/06/new-media-doesntmean-new-rules-the-challenges-of-chatbots/ (accessed January 27, 2021)

[10] Y. Leviathan, Y. Matias, Google AI blog: Google duplex: an AI system for accomplishing real-world tasks over the phone. Google Blog, (2018) 1–4. https://a i.googleblog.com/2018/05/duplex-ai-system-for-natural-conversation.html (accessed January 27, 2021).

[11] Devashish Mamgain, Chatbot Human Handoff: Seamless Human Takeover in a Hybrid Solution - Kommunicate Blog. https://www.kommunicate.io/blog/cha tbot-human-handoff/. 2020

[12] X. Luo, S. Tong, Z. Fang, Z. Qu, Frontiers: machines vs. humans: the impact of artificial intelligence chatbot disclosure on customer purchases, Mark. Sci. 38 (2019) 937–947, https://doi.org/10.1287/mksc.2019.1192.

[13] R. Diresta, A New Law Makes Bots Identify Themselves—That’s the Problem WIRED, Wired. https://www.wired.com/story/law-makes-bots-identify-th emselves/, 2019.

[14] C. Nass, J. Steuer, E.R. Tauber, Computers are social actors, Conf. Compan. Hum. Fact. Comput. Syst. CHI 94 (1994) 204, https://doi.org/10.1145/259963.260288.

[15] R.M. Schuetzler, G.M. Grimes, J.S. Giboney, The impact of chatbot conversational skill on engagement and perceived humanness, J. Manag. Inf. Syst. 37 (3) (2020) 875–900. Forthcoming.

[16] D. Gershgorn, A California law now means chatbots have to disclose they’re not human, Quartz. https://qz.com/1409350/a-new-law-means-californias-bots-have to-disclose-theyre-not-human, 2018 (Accessed January 26, 2021).

[17] U. Gnewuch, S. Morana, M.T.P. Adam, A. Maedche, Faster is not always better: understanding the effect of dynamic response delays in human-chatbot interaction, 26th Eur, Conf. Inf. Syst. Beyond Digit. - Facet. Socio-Technical Chang. ECIS 2018 (2018).

[18] J. Grudin, R. Jacques, Chatbots, humbots, and the quest for artificial general intelligence, Conf. Hum. Factors Comput. Syst. Proc. (2019) 1–11, https://doi,org 10.1145/3290605.3300439.

[19] D. Howcroft, B. Light, The social shaping of packaged software selection, J. Assoc. Inf. Syst. 11 (2010) 122–148, https://doi.org/10.17705/1jais.00224.

[20] G. Liu, E. Wang, C. Eng Huang, Chua, leveraging social capital to obtain top management support in complex, cross-functional IT projects, J. Assoc. Inf. Syst. 16 (2015) 707–737.

[21] B. Szajna, R.W. Scamell, The effects of information system user expectations on their performance and perceptions, Manag. Inf. Syst. Q. Q. 17 (1993) 493–514, https://doi.org/10.2307/249589.

[22] A.K.M. Najmul Islam, M. Mantym¨ aki, ¨ A. Bhattacherjee, Towards a decomposed expectation confirmation model of it continuance: The role of usability, Commun. Assoc. Inf. Syst. 40 (2017) 502–523, https://doi.org/10.17705/1cais.04023.

[23] C. Avgerou, Explaining trust in IT-mediated elections: A case study of e-voting in Brazil, J. Assoc, Inf, Syst. 14 (2013) 420–451, https://doi,org/10.17705 1jais.00340.

[24] S. Goode, H. Hoehle, V. Venkatesh, S.A. Brown, User compensation as a data breach recovery action: An investigation of the sony playstation network breach, Manag. Inf. Syst. Q. 41 (2017) 703–727, https://doi.org/10.25300/MISQ/2017/ 41.3.03.

[25] S. Morana, S. Schacht, A. Scherp, A. Maedche, A review of the nature and effects of guidance design features, Decis. Support. Syst. 97 (2017) 31–42, https://doi.org/ 10.1016/j.dss.2017.03.003.

[26] R.M. Schuetzler, J.S. Giboney, G.M. Grimes, J.F. Nunamaker, The influence of conversational agent embodiment and conversational relevance on socially desirable responding, Decis. Support. Syst. 114 (2018) 94–102, https://doi.org/ 10.1016/i.dss.2018.08.011.

[27] R.M. Schuetzler, G.M. Grimes, J.S. Giboney, The effect of conversational agent skill on user behavior during deception, Comput. Hum, Behay, 97 (2019) 250–259 https://doi.org/10.1016/i.chb.2019.03.033.

[28] J.K. Burgoon, D.A. Newton, J.B. Walther, E.J. Baesler, Nonverbal expectancy violations and conversational involvement. J. Nonverbal Behay. 13 (1989) 97–119.

[29] J.K. Burgoon, J.L. Hale, Nonverbal expectancy violations: model elaboration and application to immediacy behaviors, Commun. Monogr. 55 (1988) 58–79, https:// doi.org/10.1080/03637758809376158.

[30] A. Ram, R. Prasad, C. Khatri, A. Venkatesh, R. Gabriel, Q. Liu, J. Nunn, B. Hedayatnia, M. Cheng, A. Nagar, E. King, K. Bland, A. Wartick, Y. Pan, H. Song, S. Javadevan, G. Hwang, A. Pettigrue. Conversational AI: The Science Behind the Alexa Prize, 2018.

[31] C. Rzepka, B. Berger, User interaction with AI-enabled systems: A systematic review of IS research, in: Proc. 39th Int. Conf. Inf. Syst, 2018.

[32] C. Nass, Y.M. Moon, P. Carney, Are people polite to computers? Responses to computer-based interviewing systems, J. Appl. Soc. Psychol. 29 (1999) 1093–1110, https://doi.org/10.1111/j.1559-1816.1999.tb00142.x.

[33] A. Xu, Z. Liu, Y. Guo, V. Sinha, R. Akkiraju, A new chatbot for customer service on social media, in: Proc. 2017 CHI Conf. Hum. Factors Comput. Syst., ACM, New York, NY, USA, 2017, pp. 3506–3510, https://doi.org/10.1145/ 3025453.3025496.

[34] S. Park, J. Choi, S. Lee, C. Oh, C. Kim, S. La, J. Lee, B. Suh, Designing a Chatbot for a brief motivational interview on stress management: qualitative case study, J. Med. Internet Res. 21 (2019), e12231, https://doi.org/10.2196/12231.

[35] S. Subramaniam, P. Aggarwal, G.B. Dasgupta, A. Paradkar, COBOTS - A cognitive Auton. Agents MultiAgent Syst., International Foundation for Autonomous Agents and Multiagent Systems. Richland. SC. 2018, pp. 597–604.

[36] Y. Kobori, A. Osaka, S. Soh, H. Okada, Novel application for sexual transmitted infection screening with an AI Chatbot, J. Urol. 199 (2018) e189–e190, https:// doi.org/10.1016/j.juro.2018.02.516.

[37] K. Bottles, Will Patients Trust Sociable Humanoid Robots, 2011.

[38] T. Lee, K. Jagannath, N. Aggarwal, R. Sridar, S. Wilde, T. Hill, Y. Chen, Intelligent career advisers in your pocket? A need assessment study of Chatbots for student career advising, in: Proc. 25th am. Conf. Inf. Syst, 2019.

[39] R.P. Schumaker, H. Chen, Leveraging question answer technology to address terrorism inquiry, Decis, Support, Syst, 43 (2007) 1419–1430, https://doi,org 10.1016/j.dss.2006.04.007.

[40] M.-H. Nguven, The latest market research, trends, and landscape in the growing Al chatbot industry, Business Insider. https://www.businessinsider.com/chatbot-ma rket-stats-trends. 2020 (Accessed January 26. 2021).

[41] J.S. Giboney, S.A. Brown, P.B. Lowry, J.F. Nunamaker, User acceptance of knowledge-based system recommendations: Explanations, arguments, and fit, Decis. Support. Syst. 72 (2015), https://doi.org/10.1016/j.dss.2015.02.005.

[42] M.Q. Raza, A. Khosravi, A review on artificial intelligence based load demand forecasting techniques for smart grid and buildings, Renew. Sust. Energ. Rev. 50 (2015) 1352–1372, https://doi.org/10.1016/j.rser.2015.04.065.

[43] L.N. Long, S.D. Hanford, O. Janrathitikarn, G.L. Sinsley, J.A. Miller, A review of intelligent systems software for autonomous vehicles, in: Proc. 2007 IEEE Symp. Comput. Intell. Secur. Def. Appl. CISDA 2007, 2007, pp. 69–76, https://doi.org/ 10.1109/CISDA.200Z.368137.

[44] I. Lopatovska, H. Oropeza, User interactions with “Alexa” in public academic space, Proc. Assoc. Inf. Sci. Technol. 55 (2018) 309–318, https://doi.org/10.1002 pra2.2018.14505501034.

[45] H.P. Grice, Logic and conversation, in: P. Cole, J.L. Morgan (Eds.), Syntax Semant. 3 Speech Arts, 1975. pp. 41–58

[46] A.M. Seeger, J. Pfeiffer, A. Heinzl, Designing anthropomorphic conversational agents: Development and empirical evaluation of a design framework, in: Int. Conf. Inf, Syst. 2018, ICIS 2018, 2018, pp. 1–17.

[47] K.L. Nowak, F. Biocca, The effect of the agency and anthropomorphism on Users sense of Telepresence, Copresence, and social presence in virtual environments, Presence Teleoperat. Virtual Environ. 12 (2003) 481–494, https://doi.org/ 10.1162/105474603322761289.

[48] C. Tu, M. Mcisaac, The relationship of social presence and interaction in online classes, Am. J. Dist. Educ. 16 (2002) 131–150, https://doi.org/10.1207/ S15389286AJDE1603\_2.

[49] F. Biocca, C. Harms, J.K. Burgoon, Toward a more robust theory and measure of social presence: review and suggested criteria, Presence Teleoperat. Virtual Environ. 12 (2003) 456–480, https://doi.org/10.1162/105474603322761270.

[50] L. Qiu, I. Benbasat, Evaluating anthropomorphic product recommendation agents: a social relationship perspective to designing information systems, J. Manag. Inf. Syst. 25 (2009) 145–182.

[51] J. Appel, A. Von Der Pütten, N.C. Kr¨amer, J. Gratch, Does humanity matter? Analyzing the importance of social cues and perceived agency of a computer system for the emergence of social reactions during human-computer interaction, Adv. Human-Comput. Interact. 2012 (2012), https://doi.org/10.1155/2012 324694.

[52] M. Heerink, B. Krose, ¨ V. Evers, B. Wielinga, Relating conversational expressiveness to social presence and acceptance of an assistive social robot, Virtual Reality 14 (2010) 77–84, https://doi.org/10.1007/s10055-009-0142-1.

[53] R.E. Guadagno, J. Blascovich, J.N. Bailenson, C. Mccall, Virtual humans and persuasion: the effects of agency and behavioral realism, Media Psychol. 10 (2007) 1–22,doi:10.108/15213260701300865.

[54] T.M. Holtgraves, S.J. Ross, C.R. Weywadt, T.L. Han, Perceiving artificial social agents, Comput. Hum. Behav. 23 (2007) 2163–2174, https://doi.org/10.1016/j chb.2006.02.017.

[55] J. Kirakowski, P. O’Donnell, A. Yiu, The perception of artificial intelligence as “Human” by computer users, in: Human-Computer Interact. HCI Intell. Multimodal Interact. Environ., Springer, 2007, pp. 376–384.

[56] S.S. Sundar, S. Bellur, J. Oh, H. Jia, H.-S. Kim, Theoretical importance of contingency in human-computer interaction: effects of message interactivity on user engagement, Commun. Res. 43 (2016) 595–625, https://doi.org/10.1177/ 0093650214534962

[57] M.L. Jensen, P.B. Lowry, J.L. Jenkins, Effects of automated and participative decision support in computer-aided credibility assessment. J. Manag, Inf. Syst. 28 (2011) 201–234.

[58] M. Koufaris, Applying the technology acceptance model and flow theory to online consumer behavior, Inf. Syst. Res. 13 (2002) 205–223, https://doi.org/10.1287/ isre 13.2.205.83

[59] S.H. Wang, R. Baillargeon, L. Brueckner, Young infants’ reasoning about hidden objects: evidence from violation-of-expectation tasks with test trials only, Cognition. 93 (2004) 167–198, https://doi.org/10.1016/j.cognition.2003.09.012. Cognition. 93 (2004) 167–198, https://doi.org/10.1016/j.cognition.2003.09.012

[60] V. Venkatesh, F.D. Davis, A theoretical extension of the technology acceptance model: four longitudinal field studies, Manag. Sci. 46 (2000) 186–204.

[61] M. Grimes, J. Marquardson, Quality matters: evoking subjective norms and coping appraisals by system design to increase security intentions, Decis. Support. Syst. 119 (2019) 23–34, https://doi.org/10.1016/j.dss.2019.02.010.

[62] J.F. Nunamaker, D.C. Derrick, A.C. Elkins, J.K. Burgoon, M.W. Patton, Embodied conversational agent-based kiosk for automated interviewing, J. Manag, Inf, Syst 28 (2011).17–48, https://doi.org/10.2753/MIS0742-1222280102.

[63] J. Feine, U. Gnewuch, S. Morana, A. Maedche, A taxonomy of social cues for conversational agents, Int. J. Hum. Comput. Stud. (2019), https://doi.org/ 10.1016/i,jihcs.2019.07.009.

[64] J.K. Burgoon, J.A. Bonito, P.B. Lowry, S.L. Humpherys, G.D. Moody, J.E. Gaskin, J. S. Giboney, Application of expectancy violations theory to communication with and judgments about embodied agents during a decision-making task, Int. J. Hum Comput, Stud, 91 (2016) 24–36, https://doi,org/10.1016/i,jihcs.2016.02.002

[65] J.K. Burgoon, Interpersonal expectations, expectancy violations, and emotional

[66] K. Floyd, J.K. Burgoon, Expectancy violations theory, in: LA. Guerrero, M. Hecht J. DeVito (Eds.). Nonverbal Commun. Read. 3rd ed., Waveland Press, Prospect Heights, IL, 2007.

[67] S.A. Brown, V. Venkatesh, J. Kuruzovich, A.P. Massey, Expectation confirmation; an examination of three competing models, Organ. Behav. Hum. Decis. Process 105 (2008). 52–66 https://doi 0rg/10.1016/i obhdp.2006.09.008

[68] J.K. Burgoon, A.S.E. Hubbard, Cross-cultural and intercultural applications of expectancy violations theory and interaction adaptation theory, in: W. Gudykunst

(Ed.), Theor. About Intercult. Commun, Sage Publications, Thousand Oaks, California, 2005, pp. 149–171.

[69] Z.R. Steelman, B.I. Hammer, M. Limayem, Data collection in the digital age: innovative alternatives to student samples, Manag. Inf. Syst. Q. 38 (2014) 355–378.

[70] B. Wilcox, ChatScript, 2017.

[71] T.M. Holtgraves, S.J. Ross, C.R. Weywadt, T.L. Han, Perceiving artificial social agents, Comput. Hum. Behav. 23 (2007) 2163–2174, https://doi.org/10.1016/j. chb.2006.02.017.

[72] D.L. KELLEY, J.K. BURGOON, Understanding marital satisfaction and couple type as functions of relational expectations, Hum. Commun. Res. 18 (1991) 40–69. https://doi.org/10.1111/i.1468-2958.1991.tb00528.x.

[73] G.D. Biber, S. Conrad, Leech, The Longman Student Grammar of Spoken and Written English. Pearson Education India. 2002

[74] A. Abdellatif, D. Costa, K. Badran, R. Abdalkareem, E. Shihab, Challenges in Chatbot Development : A Study of Stack Overflow Posts, 2020, https://doi.org 10.1145/3379597.3387472

[75] C. Nass, Y. Moon, Machines and mindlessness: social responses to computers, J. Soc. Issues 56 (2000) 81–103, https://doi.org/10.1111/0022-4537.00153.

G. Mark Grimes is an Assistant Professor of Decision and Information Sciences at th University of Houston. His research focuses on conversational agents, information system security, and analysis of human-computer interaction behaviors to detect changes in emotional and cognitive states. Mark’s research has been published in Journal of the As sociation for Information Systems, Journal of Management Information Systems, Decision Support Systems, Computers in Human Behavior, numerous other journals and conferences, and has been presented to various industry and government organizations. Mark received his Ph.D. in Management Information Systems from the University of Arizona.

Ryan M. Schuetzler is an Assistant Professor of Information Systems at Brigham Young University. His research focuses on conversational agents, collaboration, and how users behave when interacting with artificial intelligence. Ryan’s research has been published in Decision Support Systems, the Journal of Management Information Systems, The Accounting Review, Computers in Human Behavior, and numerous other journals and conferences. He serves as president of the Midwest USA chapter of the Association for Information Systems. He received his Ph.D. from the University of Arizona

Justin Scott Giboney is an Associate Professor of Information Technology & Cyberse curity at Brigham Young University. He received his Ph.D. in Management Information Systems from the University of Arizona. His research focuses on behavioral information security, deception detection, and knowledge-based systems. He has been an investigator on eight NSF-funded grants on information security, deception and forensics-related technologies. Dr. Giboney has published 37 papers related on information security, deception detection, and decision support in such journals as MIS Quarterly, Computers & Security, Decision Support Systems, and Computers in Human Behavior, and others.