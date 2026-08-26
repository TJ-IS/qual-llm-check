---
otero_id: 26054
otero_key: "D6HZ9TFN"
title: "A speech act lexicon: an alternative use of speech act theory in information systems"
authors: "Marius A. Janson; Carson C. Woo"
year: "1996"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1996.tb00020.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A speech act lexicon: an alternative use of speech act theory in information systems

Marius A. Janson & \*Carson C. Woo

School of Business Administration, University of Missouri–St Louis, 8001 Natural Bridge Road, St Louis, MO 63121, USA, email: mjanson@umslvma.umsl.edu, \*Faculty of Commerce and Business Administration, University of British Columbia, 2053 Main Mall, Vancouver, BC, Canada V6T 1Z2, email: Carson.Woo@ubc.ca

Abstract. Speech act theory focuses on pragmatic language qualities of making assertions, directions, promises, declarations and expressions. However, assigning speech acts to one of a few categories is not without controversy. The process is context dependent and, hence, individuals with divergent contextual views may categorize speech acts differently. Different categories, in turn, imply different speech act interpretations. The difficulty of disparate speech act interpretations can often be resolved by, for example, a process of negotiation. Nonetheless, it is easy to envisage situations in which agreement by negotiation is not possible. Such would be the case when a researcher studies transcribed speech act performances. We propose that Ballmer and Brennenstuhl's (1981) speech at classification method, which relies on an extensive speech act verb lexicon with sequencing and contextual information, can reduce disagreement among individuals who singly or together analyse and ascribe meaning to speech acts. We base this proposition on the results of exploratory research involving alternative knowledge acquisition methods. Our exploratory results suggest that Ballmer and Brennenstuhl's lexicon provides several promising future research directions of speech act use in information systems.

Keywords: Speech act, information systems, knowledge acquisition, cooperative group work, discourse analysis, text analysis

## INTRODUCTION

There is continuing interest in applying speech act theory to information systems research and practice (Bostrom, 1989; Dietz & Widdershoven, 1991; Dietz, 1992; Flores & Ludlow, 1980; Flores et al., 1988; Goldkulh & Lyytinen, 1984; Johannesson, 1995; Liebenau & Backhouse, 1990; Lyytinen, 1985; Maybury, 1992; Stamper, 1987; Van Reijswoud 1993; Winograd & Flores, 1986).

Auramäki et al. (1988), for example, used speech act theory to model communication and activities in the office. They decomposed complex office activities into interconnected speech acts, such as statements of fact, requests for action, commitment, declarations and disclosure of emotional states. Their approach aims to bring together and co-ordinate the speech acts of multiple individuals into coherent, action-focused discourses.

Despite this widespread interest, several research articles report problems associated with the application of speech act theory to information systems. Some of the more important problems are:

1 utterances may lack a one-to-one mapping to a single speech act category (Bowers & Churcher, 1988; De Michelis & Grasso, 1994);

2 speech act interpretations may conflict (Reiss, 1985; Auramäki et al., 1988);

3 speech acts are often part of a discourse and, hence, are related to previous and future utterances and cannot be studied in isolation (Bowers & Churcher, 1988; Habermas, 1981; Guinan, 1988);

4 some aspects of human discourse, such as common social experiences and contextual complexities, are not adequately addressed by speech act theory (Argyris et al., 1985; Barrett & Davis, 1986; Bogen, 1991; Suchman, 1994; Voss, 1992).

Several alternative approaches for overcoming some of these problems have been proposed (Winograd, 1994). For example, Habermas (1981) proposes to resolve ambiguities with respect to speech act interpretation by a process of negotiated sense-making. That is to say, the hearer responds to the ambiguity by requesting that the speaker provide additional explanation. Others, such as Argyris et al. (1985) and De Michelis and Grasso (1994), state that action is embedded in the ordinary language and social practices of the community in which that action occurs. Thus, interpreting action, assigning meaning and reducing ambiguities turn on contextual understanding.

However, one can easily envisage situations in which Habermas' agreement by negotiation is not feasible. For example, Auramäki et al. (1988) noted that multiple individuals analysing the same conversation graph came to conflicting interpretations. It is unreasonable to expect that the conversation graph designer will be present for sense-making every time someone else interprets it.

Although researchers such as Argyris et al. (1985) and Habermas (1981) suggested that context be incorporated in discourse analysis, they did not provide a mechanism for operationalizing their ideas in the information systems domain. De Michelis and Grasso (1994), on the other hand, did operationalize certain contextual aspects. They constructed a computer-based conversation system, which stores sequences of communicative events and links these to documents and commitment negotiations. Nevertheless, because the De Michelis and Grasso (1994) solution focuses on conversations among individuals, it does not address our problem, which is interpreting written documents.

In this paper, we propose Ballmer and Brennenstuhl's (1981) speech at lexicon as an alternative to the approaches discussed above. Our objective is to identify an approach for modelling speech acts contained in written documents whose authors are unavailable for further consultation on resolving potential ambiguities. Such an approach would be particularly suited to the use of speech act theory in the context of information systems analysis and design.

The assumption underlying our research is that the aforementioned speech act problems are caught up with the speech act classifactory model. Suchman (1994), for example, asserts that Searle's (1969, 1975, 1979) and Searle and Vanderveken's (1985) speech act model, which is often used in speech act theory-based information systems work, does not always do justice to the contextual subtleties and complexities.

The objective of our work is to show that Ballmer and Brennenstuhl's (1981) models have the potential to minimize the problems just discussed. The essential feature of Ballmer and Brennenstuhl's (1981) method is classifying speech acts by comparing and contrasting them with speech act clusters of similar semantic meaning. The practical realization of this concept is embodied in a speech act lexicon. Selecting a speech act class is rendered more objective, because the individual's subjective judgments are mediated by the speech act lexicon.

We support our proposition with the results of an exploratory empirical study of several alternative knowledge acquisition methods. We selected the topic because we found that it is easier to control the study and to show the validity of our results.

As already mentioned, the major objective of this article is to identify, apply and evaluate an alternative method of classifying speech acts. This article proceeds as follows: we shall first introduce, review and discuss the shortcomings of existing speech act methods. Next, we shall introduce Ballmer and Brennenstuhl's (1981) speech act modelling method. Following that, we shall use Ballmer and Brennenstuhl's model and its speech act verb lexicon to develop a four-step procedure for categorizing speech acts. We demonstrate this procedure by evaluating the multidimensional scaling knowledge acquisition method (Agarwal & Tanniru, 1990; Benbasat & Dhaliwal, 1989; Ngwenyama & Klein, 1994; Wilson, 1989). We then report on our exploratory study of the recall, repertory grid and coherence knowledge acquisition methods. Finally, we extend our exploratory study results to future research.

## SPEECH ACTS

## Speech act theory

Speech act theory maintains that speech, uttered in a particular way and under certain conditions, is an 'act'. As Austin (1962, p. 20) remarked: '... the more we consider a statement not as a sentence but as an act of speech the more we are studying the whole thing as an act'. In this sense, 'speech' is a process whereby a set of conditions is brought about (i.e. the 'act') by a performance (Lanigan, 1977, pp. 29–30).

Consider, for example, a store clerk's utterance, 'I need your credit card, please'. In effect, the clerk requests (politely orders) the store's customer to hand over his/her credit card so that the transaction can be completed. The communicative interaction between the clerk and customer can be analysed in terms of speech acts — factual statements, requests and commitments.

A speech act comprises three simultaneous subacts — the locutionary, illocutionary, and perlocutionary acts.

## Locutionary act

The locutionary act is the utterance of words. According to Lanigan (1977, p. 43) '... the speaker makes use of his/her vocabulary, hence, the speaker is doing something'.

## Illocutionary act

The illocutionary act is what the speaker does in saying something. Consider a store clerk's statement, 'Your account is overdrawn'. The clerk is informing the customer of a state of affairs and, hence, the illocutionary act is 'informing'.

Accordingly, Searle (1969) categorizes illocutionary acts into:

1 assertives — describe states of the world;

2 directives — induce the addressee to act in certain ways;

3 commissives — commit the speaker to act in certain ways;

4 declaratives — change a state of affairs; and

5 expressives — express the speaker's emotional state.

Searle and Vanderveken (1985, pp. 52–53) contend that this classification is exhaustive. Their claim is based on the direction of fit between words and world, which in turn is a component of the illocutionary force. That is to say, the speaker matches his words with the world (i.e. assertive), he motivates the addressee to match the world with his words (i.e. directive), he pledges to change the world to accord with his words (i.e. commissive), he changes the world by his words (i.e. declarative) or he matches words with his emotional state (i.e. expressive).

Illocutionary acts are further analysed in terms of illocutionary force. Searle (1969, pp. 64–71) defines ten rules and conditions for assessing illocutionary force. The most important of these are essential, preparatory and sincerity conditions (Levinson, 1988).

The essential condition or illocutionary point refers to the illocutionary act's purpose. In the earlier speech act example, 'I need your credit card, please', the store clerk requests the customer to hand over his credit card. Hence, the illocutionary point is 'requesting'. Several preparatory conditions are presumed. First, the customer has made a purchase and wishes to pay by credit card. Second, the clerk assumes that, unless specifically asked, the customer would not give his credit card when it is needed. Third, the sincerity conditions dictates that the speech act should not be frivolous. The clerk positively wants the customer to act in accord with the speech act's propositional content (i.e. hand over the credit card) because it is needed to complete the transaction.

## Perlocutionary act

Lastly, the perluctionary act is what the speaker does by saying something; it is the effect of the speech act performance on the addressee. The earlier statement, 'Your account is overdrawn' can cause the customer great anxiety. Thus, the perlocutionary act is 'alarming the customer'.

## Speech act applications in information systems

Speech act theory has been used to analyse information systems and to build computer-based communication systems (De Cindio et al., 1986; Flores & Ludlow, 1980; Flores et al., 1988; Goldkuhl & Lyytinen, 1984; Johannesson, 1995; Kaplan et al., 1992; Malone & Crowston, 1990). We provide two real-world examples below to illustrate the issues involved.

## Speech act-based modelling of information systems

Auramäki et al. (1988) define office activities as ‘dealing with symbols that describe and prescribe transactions’ for diverse purposes including ‘bargaining, and defining and enforcing contractual conditions’.

Dealing with symbols underlies SAMPO (speech act-based office modelling approach), which is based on Searle's speech act theory. Auramäki et al. (1988) contend that individuals apply the norms and rules governing office communication subconsciously. Hence, the purpose of SAMPO is: to discover and reconstruct the normative rules and to express them as 'conversation graphs'. This rule reconstruction process is accomplished by engaging the systems analyst in a discourse about the form and purpose of information passing among individuals or among processes.

The process just described is essentially one of categorization, and as such, open to ambiguities and misclassifications. In fact, based on first-hand experience, Auramäki et al. (1988) did observe some problems associated with the conversation graphs. The authors reported that multiple individuals interpreted conversation graphs differently. In this article, we suggest a method of reducing this ambiguity.

## Speech act-based modelling of communication

Dietz and Widdershoven (1991), Dietz (1992), Flores et al. (1988) and Habermas (1981) have all independently used speech act theory to model discourses. In fact, Flores et al. (1988) developed the Co-ordinator, which is a speech act-based tool for computer-mediated interpersonal communication. The system was conceptualized around language as social action with the purpose of ‘... facilitating a shared clarity of communication’. The Co-ordinator's messages are labelled requests or not-requests for action. The system's goal is to structure a conversation explicitly.

Carasik and Grantham (1988) applied the Co-ordinator under real-world conditions to facilitate computer-supported co-operative work. They reported that users felt constrained by the structure embodied in the system's conversational templates. Furthermore, several users linked message ambiguity with the underlying speech act theory embodied by the Co-ordinator.

De Cindio et al. (1986), De Michelis and Grasso (1994), Kaplan et al. (1992) and Malone and Crowston (1990) concur that speech act ambiguity is problematic. However, De Michelis and Grasso (1994) also suggest a way of reducing the ambiguity by interpreting speech act meaning in context. This procedure is the basis for their computer-based 'Milan Conversation Model'.

Nevertheless, because the 'Milan Conversation Model' assumes communication between two or more individuals, it does not address our objective, which is to interpret written text.

## Other aspects of speech act theory

This section links the speech act concept with other developments in action theory (Argyris et al., 1985), communicative action theory (Habermas, 1981) and issues related to speech at validity (Suchman, 1994).

Because speech acts are performed to bring about change in an existing state of affairs, they can be viewed in terms of Argyris et al.'s (1985) 'philosophy of action'. These authors focus on the beliefs and intentions of the actors and their intersubjective meanings and shared practices. As explained by Argyris et al. (1985), '... the knowledge required to understand action is embedded in the ordinary language and social practices of the community in which action occurs'.

Speech act theory is also a core concept of Habermas' (1981) theory of communicative action. This theory can, perhaps, best be illustrated in a decision-making context involving two individuals. Rational action by the actors requires agreement at three distinctly different reality or world perspectives: objective, social and subjective. First, the participants must agree on essential facts, conditions and causal relations that exist in the objective world. Second, they must agree on the relations and conditions prevailing in the social world. Third, rational decision-making involves the partners honestly disclosing the motivations and intentions underlying their actions. Thus, in communicative action, we again see that action is meaningful only in context.

Suchman (1994) convincingly demonstrated the dangers of using language as a system to get things done. These dangers include increased levels of control over individuals, automated surveillance and forcing individuals to respond with instrumental rationality in a world, which is overly complex and at times non-rational.

However, as pointed out by Orlikowski (1995), the restrictions just mentioned are but one side of the same coin: category systems are simultaneously enabling and constraining. Given this fact, it would not seem unreasonable to expect that category systems with many categories are less constraining than those with few categories.

In summary, the work done by others suggests that we need more flexible categorization systems and more contextual information. We argue that this can be achieved by implementing Ballmer and Brennenstuhl's (1981) speech act lexicon.

## An alternative speech act classificatory model

A top-down approach for categorizing speech acts is central to most, if not all, speech act models (Searle, 1969, 1975; Habermas, 1981; Flores & Ludlow, 1980). In Searle's work, the assertive, directive, commissive, declarative and expressive categories are derived from speech act theory. In practice, a speech act is compared against the essential, the preparatory and the sincerity conditions and then classified into one of five categories. In contrast to such top-down speech act models, we introduce Ballmer and Brennenstuhl's (1981) categorization, which is essentially bottom up.

Ballmer and Brennenstuhl (1981) set out to classify all existing speech act verbs using Searle's five speech act categories. They found, however, that adding a new speech act verb would frequently require extensive revisions of the collection of previously classified verbs. In fact, all indications were that revisions would continue until the last speech act was classified (Ballmer & Brennenstuhl, 1981). Therefore, the authors abandoned the top-down method, which classified speech act verbs by imposing a theoretically derived set of categories on the data.

Instead, Ballmer and Brennenstuhl (1981) first collected the set of all speech act verbs. This set was then used to form speech act verb clusters of similar semantic fields (Weisberger, 1962). These clusters were further divided into subclusters of increased, semantic specificity. The process resulted in an organized hierarchy comprising speech act models, speech act categories and speech act subcategories. Because the aforementioned hierarchy starts with data, the classificatory approach is essentially bottom up.

The prominent feature of Ballmer and Brennenstuhl's (1981) method is its speech act lexicon. To interpret the meaning of a speech act, one looks it up in the lexicon, which in turn points towards speech act subcategories or categories. Then, by comparing and contrasting the speech act with the semantic meanings associated with the aforementioned speech act clusters, one determines its meaning. We propose that Ballmer and Brennenstuhl's speech act lexicon helps minimize some of the difficulties with speech act analysis mentioned in this article's introduction and further described below.

## A SPEECH ACT LEXICON

## Overview of linguistic function's use

Ballmer and Brennenstuhl's (1981) method for classifying speech acts comprises subcategories, categories, models and model groups. The relationships among these entities is expressed by:

$$
\text { verbs } \varepsilon \text { subcategory } \subseteq \text { category } \subseteq \text { model } \subseteq \text { model   group } \subseteq \text { linguistic   function }
$$

At the lowest level, subcategories and categories comprise speech acts grouped according to semantic similarity. The meaning of a particular speech act is in part determined by neighbouring speech acts of the same subcategory or category. Models comprise speech act categories that are clustered around one of the four linguistic functions: expression, appeal, interaction and discourse (Table 1). Progressing from subcategory to category, to model, to model group, and to linguistic function reflects increasing degrees of structure.

Table 1 shows a one-to-one relationship between the linguistic functions, expression and appeal, and the emotion and enaction models respectively. In contrast, the linguistic functions, interaction and discourse, comprise multiple models. Progressing from expression, through appeal and interaction, to discourse implies increasing degrees of complexity.

Consider, for example, the customer who purchases a clothes dryer. After being installed in the customer's basement, the dryer fails on the first trial. The customer then contacts the store's manager. At this point, the customer is so irate that instead of negotiating a repair visit, he simply vents his anger. That is to say, he uses speech act verbs belonging to the linguistic function, expression.

Table 1. Ballmer and Brennenstuhl's (1988) system of models

<table><tr><td>Linguistic function</td><td>Model group</td><td>Description</td></tr><tr><td>Expression</td><td>1. Emotion model</td><td>Speaker expresses his personal feelings</td></tr><tr><td>Appeal</td><td>2. Enaction model</td><td>Speaker affects the hearer&#x27;s course of action</td></tr><tr><td rowspan="3">Interaction</td><td>3. Struggle model</td><td>Speaker and hearer negotiate co-operatively or competitively</td></tr><tr><td>4. Institutional model</td><td>A special case of the struggle model because the speaker achieves his goal by adhering to institutional norms</td></tr><tr><td>5. Valuation model</td><td>Special cases of the struggle model, the speaker makes evaluative statements about persons or things</td></tr><tr><td rowspan="3">Discourse</td><td>6. Discourse models</td><td>Speaker and hearer engage in rational discourse</td></tr><tr><td>7. Text models</td><td>Govern the information collecting and processing functions of the discourse models</td></tr><tr><td>8. Theme models</td><td>Special cases of the discourse models, speaker and hearer discuss ideas, thoughts, etc</td></tr></table>

The customer eventually realizes that a confrontational attitude is counterproductive. He then switches strategies and appeals for help by requesting a visit by a repair man. The customer has then progressed from the linguistic function, expression, to using speech act verbs belonging to the linguistic function, appeal.

Incompatibilities between the schedules of the repair shop and the customer cause further frustrations. The customer does not want to take a day off from work and seeks to negotiate a repair visit to his house on a Saturday. The repair shop manager is quite agreeable to this request. However, the next available Saturday is six weeks away, which is unsatisfactory to the customer.

Both participants eventually realize that only understanding each other's circumstances can resolve their mutual problem. After some discussion, the customer agrees to rearrange his work schedule and to be at home during a normal weekday without losing vacation days. The repair shop manager agrees to adjust the store's repair schedule and to send a repair man the next day. The manager and the customer have negotiated; thus, the exchange typifies the linguistic function, interaction.

When the repair man arrives at the customer's residence, the discussion again moves to a different level. The interaction between repair man and customer is co-operative; both strive towards getting the appliance in working order. In accomplishing this goal, the repair man relies on the customer for information about the symptoms of the malfunctioning appliance. The customer in turn relies on the repair man's expertise to get his defective dryer working again. Both individuals engage in a rational discourse for information collection and processing. Hence, the speech act verbs used belong to the linguistic function, discourse.

The example shows a progression from the least complex to the most complex use of linguistic functions. However, it is also possible that a more complex linguistic function subsumes individual parts of less complex linguistic functions. To illustrate, during his discourse with the appliance store manager, the customer may at times resort to expressive and appeal speech act types to gain sympathy for the difficulties he is experiencing.

The example illustrates that linguistic functions are temporally related. Ballmer and Brennenstuhl (1981) contend that speech act categories can relate on several dimensions, including time and effectiveness. During negotiation, for example, speech acts signifying demands may be more effective than speech acts signifying expression of emotion. However, making demands frequently damages interpersonal relations and, for that reason, may ultimately become ineffective. Thus, sequencing speech act categories involves judgement and, at times, trial and error.

As we argued earlier, an important component of Ballmer and Brennenstuhl's (1981) speech act classification is the lexicon. The lexicon's first section is an alphabetical listing of speech act verbs. The lexicon's second section is a listing of models, categories and subcategories. Classifying speech act verbs is a two-step process. First, the speech act verb in question is located in the alphabetical list of the lexicon's first section, which then provides codes that link the speech act with subcategories or categories from the lexicon's second section.

## The thinking speech act model

The three knowledge acquisition methods used in this study are best expressed as thinking, information and theme models (Table 2). The thinking (DE) model is discussed in this section, while the information and theme models are presented in the Appendix.

A category code comprises two upper case letters followed by one numerical and one or two alphabetic subscripts. The upper case letters identify the model, the numerical subscript indicates the category's location within the speech act model and the alphabetic subscripts refer to the subcategory. Thus, the thinking model's category, $DE_{2}$ , precedes category $DE_{3}$ , and subcategory $DE_{6a}$ precedes subcategory $DE_{6b}$ .

The thinking (DE) model is a member of the 'text models' group. Its code is derived from the German word 'denken', which translates into the English word 'to think'. Thinking operations form the following sequence:

1 Get an idea (DE $_{1}$ ): this can occur by noticing something or by grasping a concept.

2 Consider the idea $(DE_{2})$ : paying close attention to the idea.

3 Wonder about the idea ( $DE_{3}$ ): being surprised at and hesitating about the idea.

4 Think over $(DE_{4})$ : re-entering an earlier thinking mode.

5 Make assumptions (DE $_{5}$ ): setting up beliefs.

6 Think over carefully (DE\$\_{6}\$): the detailed thinking process, which consists of (Table 2):

a collecting knowledge or a set of objects (DE $_{6a}$ );

b arranging the knowledge to facilitate analysis (DE $_{6b}$ ): (i) select; (ii) separate; (iii) compare; and (iv) identify;

Table 2. Examples of speech act verbs in selected categories

<table><tr><td>Model</td><td>Category</td><td>Speech act verbs</td></tr><tr><td rowspan="5">Thinking</td><td> $DE_{6a}$ </td><td>Amass, collect, gather</td></tr><tr><td> $DE_{6bi}$ </td><td>Select, single out, sort out</td></tr><tr><td> $DE_{6bii}$ </td><td>Separate, set aside, lay aside</td></tr><tr><td> $DE_{6c}$ </td><td>Analyse, classify, segment, fit in</td></tr><tr><td> $DE_{6d}$ </td><td>Infer, conclude, deduce, induce, derive</td></tr><tr><td rowspan="6">Information</td><td> $IN_{1aa}$ </td><td>Ascertain, determine, look up, search</td></tr><tr><td> $IN_{3ba}$ </td><td>Compare, choose, select, separate, set aside</td></tr><tr><td> $IN_{3bb}$ </td><td>Appraise, assess, evaluate</td></tr><tr><td> $IN_{5ac}$ </td><td>Extract, pick out, pull out, pluck out</td></tr><tr><td> $IN_{5b}$ </td><td>Recall, remember, recollect, call to mind</td></tr><tr><td> $IN_{6aa}$ </td><td>Inform, publish, report, display, describe</td></tr><tr><td rowspan="6">Theme</td><td> $TO_{3a}$ </td><td>Arrange, order, structure</td></tr><tr><td> $TO_{3b}$ </td><td>Rearrange, reorder, restructure</td></tr><tr><td> $TO_{4}$ </td><td>Connect, combine, join, unite, tie together</td></tr><tr><td> $TO_{5a}$ </td><td>Put first, bring to relief, put into foreground</td></tr><tr><td> $TO_{5ab}$ </td><td>Accentuate, emphasize, lay stress on</td></tr><tr><td> $TO_{5ac}$ </td><td>Attract attention to call attention to</td></tr></table>

c analysing the knowledge (DE $_{6c}$ );  
d inferring new objects or knowledge ( $DE_{6d}$ );  
e differentiating objects or knowledge ( $DE_{6e}$ ); and  
f putting together something useful ( $DE_{6f}$ ).  
7 Have doubt about the idea (DE\$\_{7}\$): becoming suspicious of the idea's validity.  
8 Plan/decide (DE $_{8}$ ): if all is well, planning and decision-making occurs to implement the idea.

## A four-stage procedure

To learn more about the speech act lexicon and to explore its potential for reducing message ambiguity, we developed a four-stage procedure to analyse knowledge acquisition methods (Figure 1). First, based on a careful study of the knowledge acquisition method's essence and manner of application, the knowledge engineer partitions the method into small steps (Figure 1, stage 1). Then, in the procedure's second stage, the engineer uses the lexicon's alphabetically listed speech acts to identify speech act categories or subcategories that best describe each step of the knowledge acquisition method (Figure 1, stage 2). Next, starting with the previously identified categories, the knowledge engineer selects one or more speech act models that express the essence of the knowledge acquisition method under investigation (Figure 1, stage 3). The second and third stages exemplify the use of Ballmer and Brennenstuhl's (1981) lexicon.

Then, from among the aforementioned potential speech act models, the knowledge engineer selects one model whose categories most completely describe the knowledge acquisition method's steps. Selecting this speech act model is guided by three concepts: (1) each speech act category is a 'linguistic field'; (2) speech acts are sequenced on a dimension of time, effectiveness, efficiency, etc.; and (3) Ockam's razor, which is to say, representing a knowledge acquisition method as one speech act model is preferable over expressing it as a mixture of two or more speech act models (Angeles, 1981). The knowledge engineer then re-expresses all the knowledge acquisition method's steps using only speech act categories in the selected speech act model (Figure 1, stage 4).

![](/api/attachments/D6HZ9TFN/fulltext/images/2ff93025f347768e5e9c5615965bdb41c47e417c584b3b0c94ae4258891838f0.jpg)  
Figure 1. The speech act lexicon-based procedure.

The remainder of this section shows how our Ballmer and Brennenstuhl (1981) lexicon-based four-stage procedure helps overcome some of the speech act drawbacks that were described in this article's introduction.

\- Mapping utterances into speech act categories. This mapping proceeds in two distinct steps: from utterance to speech act verb, and from speech act verb to speech act category. Ballmer and Brennenstuhl's lexicon supports the second step by assuming that the speech act verbs used are correct in describing the utterance. The last stage of our procedure (Figure 1, stage 4) challenges this assumption by retracing the entire four-step procedure using the contextual information in the potential speech act models. This is an application of double-loop learning, whereby the governing variables (i.e. the speech act categories) are manipulated (Argyris et al., 1985; Argyris, 1990).

\- Avoiding overinterpretation. At issue here is the interpretation of the speech act model by someone other than its originator. The lexicon four-stage procedure helps reduce the likelihood of multiple interpretations thanks to three types of contextual information: (1) each speech act category belongs to a single speech act model; (2) each category is a linguistic field consisting of speech acts with similar meanings; and (3) categories are sequenced on time, effectiveness, efficiency or on some other dimension.

\- Anterior and posterior speech acts. As mentioned earlier, some speech act categories of Ballmer and Brennenstuhl's speech act models are related on the time dimension. This time-relatedness underlies the mechanism for evaluating speech acts in context.

\- Further considerations. Some of the speech act categories in Ballmer and Brennenstuhl's speech act models are sequenced on dimensions other than time, e.g. on effectiveness, efficiency or some other dimension. Such sequencing provides additional contextual information, which other speech act theories lack. Thus, the last stage of the four-stage speech act classification procedure forces the consideration of this contextual information. It is, perhaps, important to state that Ballmer and Brennenstuhl's speech act models do not consider all forms of human discourse. Thus, even though body language is an important aspect of oral discourse (Barrett & Davis, 1986), it plays no part in Ballmer and Brennenstuhl's model. However, Ballmer and Brennenstuhl's model is not unique in this respect, because other speech act models have similar limitations and, furthermore, our project focuses solely on written material.

We will return again to the above topics later, where we demonstrate how our four-stage procedure (Figure 1) reduces ambiguities in our empirical study.

## An application of the lexicon

Table 3 shows the results of using the four-stage procedure on the multidimensional scaling knowledge acquisition method (Olson & Rueter, 1987). A knowledge engineer starts the multidimensional scaling method by first identifying objects in the expert's domain of interest. The expert is then asked to rate each object pair on similarity. These ratings are input to a computer-based analysis program that produces the best placement of the objects in n-dimensional space. Next, several two-dimensional projections of the n-dimensional space are constructed and displayed in graphical form. The two-dimensional graphs are then augmented with plausible labels. If, for example, objects on the y-axis are shown in increasing order of their size, then a plausible labelling for that dimension (i.e. y-axis) is 'size'.

Table 3. Speech at category codes for the multidimensional scaling method, stages one to two

<table><tr><td>Step</td><td>Description</td><td>Speech act verb</td><td>Speech act verb category</td></tr><tr><td>1</td><td>Gather objects of interest</td><td>Gather Identify</td><td> $DE_{6a}$   $TE_{-1cb}$   $DE_{6b}$   $IN3_{ba}$   $VV_a$ </td></tr><tr><td>2</td><td>Select object pair</td><td>Select Choose</td><td> $DE_{6bi}$   $IN_{3ba}$   $TO_{3a}$   $VV_g$ </td></tr><tr><td>3</td><td>Compare object pair</td><td>Evaluate Compare</td><td> $WT_o$   $VV_g$   $DE_{6bii}$   $DE_{6f}$   $DE_{6biii}$   $DE_{6g}$   $IN_{3ba}$   $TO_{5e}$ </td></tr><tr><td>4</td><td>Analyse similarity data</td><td>Analyse</td><td> $DE_{6c}$ </td></tr><tr><td>5</td><td>Infer labels for each axis of the two-dimensional space</td><td>Infer</td><td> $DE_{6d}$   $IN_{2a}$   $TE_{-1cb}$ </td></tr></table>

Table 3 shows the outcome of the procedure's (Figure 1) first two steps. The knowledge acquisition method's steps shown in Table 3 link up with speech act categories belonging to speech act models DE, IN, TO and VV. These four models arise because several speech acts occur in alternative speech act subcategories. Thus, to identify the speech act model that best fits the knowledge acquisition method in hand, the knowledge engineer re-expresses all the steps in Table 3 as a DE, an IN, a TO and a VV speech act model. Sequencing and contiguity criteria are then used to select, from the four alternatives, the speech act model that best captures the knowledge acquisition method's essence. The outcome of fitting the thinking model, DE, to the multidimensional scaling method is shown in Table 4. Because all the steps in the method are expressible by the DE identifier, the multidimensional scaling knowledge acquisition method corresponds best with Ballmer and Brennenstuhl's (1981) thinking model (DE).

## AN EXPLORATORY STUDY

## Purpose

Our study's purpose was to explore the lexicon-based four-stage procedure's usefulness for overcoming some of the speech act drawbacks mentioned in the article's introduction. To this end, the study focused on two issues:

1 What are the difficulties others might have with the lexicon-based procedure and what are their suggestions for overcoming them?

2 Do individuals who, independent of one another, use the procedure to analyse knowledge acquisition methods reach similar conclusions?

## Subjects

Three PhD and two MSc students participated in the exploratory study, forming a convenience sample. These students were selected because they had completed an advanced course which, among other topics, concentrated specifically on knowledge acquisition.

Table 4. Fit thinking model (DE) to multidimensional scaling method, stage four

<table><tr><td>Category</td><td>Description</td><td>Speech act verb</td><td>Step</td></tr><tr><td> $DE_{6a}$ </td><td>Gather the important objects</td><td>Gather</td><td>1</td></tr><tr><td> $DE_{6bi}$ </td><td>Select, choose or pick out two objects</td><td>Select Choose</td><td>2</td></tr><tr><td> $DE_{6biii}$ </td><td>Compare objects for similarity</td><td>Compare</td><td>3</td></tr><tr><td> $DE_{6c}$ </td><td>Analyse or arrange similarity data in terms of space of lowest possible dimensionality</td><td>Analyse</td><td>4</td></tr><tr><td> $DE_{6d}$ </td><td>Infer or deduce meaningful labels for each axis</td><td>Infer Deduce</td><td>5</td></tr></table>

## Research plan

## First meeting

Because the study was exploratory, it used a straightforward project plan. During a preliminary meeting, each subject received a project plan, two articles on knowledge acquisition and Ballmer and Brennenstuhl's (1981) speech act lexicon. The project plan detailed the study's objectives, subjects' obligations, a time schedule for completing project assignments and the remuneration the subjects would receive for project participation.

The first article (Olson & Rueter, 1987) explained five knowledge acquisition methods in depth, including two knowledge acquisition methods used in this study (multidimensional scaling and recall methods). The second article (Janson & Woo, 1992, abbreviated) discussed Ballmer and Brennenstuhl's (1981) speech act lexicon and demonstrated the five-stage procedure by analysing the multidimensional scaling method. At the meeting's conclusion, the subjects were instructed to study the aforementioned materials in preparation for a second meeting with the project's investigators.

## Second meeting

The two-hour meeting opened with a question and answer session to ensure that the subjects understood the knowledge acquisition process (Olson & Rueter, 1987) and the lexicon-based procedure for anlaysing methods (Janson & Woo, 1992). This session, one hour in length, was devoted to discussing, explaining and demonstrating the lexicon.

During the remaining hour, the subjects applied the lexicon-based procedure to analyse the recall method. All five subjects completed the assignment within the allotted time of one hour. Subsequent to the meeting, we compared subjects' analyses with our own analysis of the recall method. The subjects concluded unanimously that the recall method was best described by Ballmer and Brennenstuhl's (1981) information model. These results were in agreement with our earlier independent analysis of the recall method. This outcome motivated us to complete the remainder of the project.

At the meeting's conclusion, the subjects were given several documents:

1 An unabbreviated version of the earlier article on the speech act lexicon, which also included a lexicon-based analysis of the recall method (Janson & Woo, 1992).

2 An explanation of the underlying theory and application of the repertory grid method (Hart, 1989).

3 An explanation of the theory and practical application of the coherence method (Abdul-Gader & Kozar, 1990).

With these materials in hand, the subjects were instructed to carry out, individually and separately, a lexicon-based analysis of the repertory grid and the coherence methods.

## Analytical procedures

All five subjects analysed the repertory grid and coherence methods for knowledge acquisition in their own time and at a location of their choice. The written response of each subject was evaluated separately on completeness, consistency and correctness. The investigators then compared and contrasted the results obtained by each subject against those of the other four subjects.

## RESULTS OF THE EXPLORATORY STUDY

We shall discuss in turn the subjects' classifications of the recall method (Olson & Rueter 1987), the repertory grid method (Boose, 1985; Hart, 1989) and the coherence method for knowledge acquisition methods (Abdul-Gader & Kozar, 1990). A brief description of these methods is given in the Appendix. First, for each knowledge acquisition method, we shall discuss in detail the classificatory process used by one of the five subjects. Second, for each of the three knowledge acquisition methods, we shall discuss all five subjects' final classification.

## Recall method

Table 5 shows the results of subject E's application of the first two stages of our four-stage procedure (Figure 1, stages 1 and 2): the recall method's procedural steps (column 1), the corresponding speech act verbs (column 2) and the speech act categories (column 3). Table 6 shows the potential speech act models, which subject E targeted for a closer analysis of the previous table (Figure 1, stage 3). Subject E provisionally identified the information (IN) and thinking (DE) models as candidates for describing the recall knowledge acquisition method. Next, for each of these two models, subject E re-expressed the knowledge acquisition steps using only speech acts of the corresponding speech act model (Table 7). Of the two speech act models, subject E selected the information model as best representing the recall knowledge acquisition method. As a special cautionary remark, subject E noted that category IN $_{-1}$ (Table 7, step 2) is out of sequence in relation to other categories and, thus, does not fit perfectly. He further suggested that a reversal of category sequencing be considered to resolve the problem.

Table 5. Speech act category codes for the recall method, stages one to two, subject E

<table><tr><td>Step</td><td>Speech act verb</td><td>Speech act categories</td></tr><tr><td>1. Recall object name</td><td>Recall</td><td> $IN_{5aa}$ ,  $IN_{5b}$ ,  $TV_{7j}$ </td></tr><tr><td>2. Record object order</td><td>Record</td><td> $DE_1$ ,  $ET/TE_{ab}$ ,  $VV_a$ </td></tr><tr><td>3. Examine for regularity</td><td>Examine</td><td> $EN_{5cc}$ ,  $EN_{5cd}$ ,  $IN_{1aa}$ ,  $NO_{6c}$ ,  $TE_{-1b}$ ,  $VV_c$ </td></tr><tr><td>4. Classify into chunks</td><td>Classify</td><td> $DE_{6c}$ ,  $IN_{3aa}$ ,  $IN_{3ac}$ ,  $TO_{3a}$ ,  $VE_{-1}$ ,  $VV_a$   $WT_o$ </td></tr><tr><td>5. Draw into ordered tree</td><td>Draw</td><td> $DE_{6b}$ ,  $DT_2$ ,  $ET/TE_{aa}$ ,  $ET/TE_{ab}$ ,  $ET/TE_{ac}$ ,  $TO_{5c}$ ,  $TV_5$ </td></tr><tr><td>6. Conclude relationships</td><td>Conclude</td><td> $DE_{6d}$ ,  $DI_{10}$ ,  $DI/TU$   $TE_{-1cb}$ ,  $TU_{aa}$ </td></tr></table>

Table 6. Potential speech act models for the recall method, stage three, subject E

<table><tr><td colspan="6">Step</td></tr><tr><td>1. Recall</td><td>2. Record</td><td>3. Examine</td><td>4. Classify</td><td>5. Draw</td><td>6. Conclude</td></tr><tr><td> $IN_{5aa}$ </td><td></td><td> $IN_{1aa}$ </td><td> $IN_{3aa}$ </td><td></td><td></td></tr><tr><td> $IN_{5b}$ </td><td></td><td></td><td> $IN_{3ac}$ </td><td></td><td></td></tr><tr><td></td><td> $DE_1$ </td><td> $DE_{6c}$ </td><td> $DE_{6c}$ </td><td> $DE_{6b}$ </td><td> $DE_{6d}$ </td></tr></table>

The similarities among the five subjects who, independent of one another, applied our four-stage procedure, are shown in Table 11. The similarities between subjects on speech act category selection, in general, can be illustrated using the agreement between subjects D and E (Table 8). Notice both the differences and similarities between the speech acts used by subjects D and E. We attributed these differences to the slightly different procedural steps used to re-express the recall knowledge acquisition method. Subject E had two more steps than subject D. Subject D's third and fourth steps correspond to subject E's fourth step. Thus, in this particular instance, subject D provided a more detailed description or greater degree of granularity than subject E. For the steps with the same granularity, both subjects selected identical speech act categories. This between-subject agreement suggests that Ballmer and Brennenstuhl's (1981) lexicon reduces ambiguity of speech act interpretation.

## Repertory grid method

The repertory grid knowledge acquisition method is considerably more complex than the recall method and, hence, matching speech act models with the repertory grid method is more complex as well. We shall discuss in detail the results of subject D, while summarizing the results of subjects A, B, C and E (Table 11).

The results of the first two stages of the lexicon-based classifactory procedure (Figure 1) are shown in Table 9. Using this table, subject D identified the thinking (DE), the information (IN) and the thematic phase (TV) models as potentially good fits for the repertory grid knowledge acquisition method. A thorough analysis led subject D to select the thinking model (DE) as best reflecting the repertory grid method (Table 10). Step six in Table 10 was left unexplained by the thinking model. This step can be accounted for by the category, $TV_{7d}$ (Table 9) of the thematic phases (TV) model. In this case, using the sequencing and contiguity criteria, the lone thematic phases model is subsumed by the thinking model (DE).

Table 7. Fit information model (IN) to recall method, stage four, subject E

<table><tr><td>Speech act category</td><td>Speech act verb</td><td>Description</td><td>Step</td></tr><tr><td> $IN_{1aa}$ </td><td>Trace</td><td>Trace object names</td><td>1</td></tr><tr><td> $IN_{-1}$ </td><td>Set up a list</td><td>Set up an object list</td><td>2</td></tr><tr><td> $IN_{1aa}$ </td><td>Examine</td><td>Examine for regularities</td><td>3</td></tr><tr><td> $IN_{3aa}$ </td><td>Classify</td><td>Classify chunks</td><td>4</td></tr><tr><td> $IN_{3aa}$ </td><td>Sort</td><td>Sort into ordered trees</td><td>5</td></tr><tr><td> $IN_{8a}$ </td><td>Acknowledge</td><td>Acknowledge relationships</td><td>6</td></tr></table>

Table 8. Recall method, stage four, subjects D and E

<table><tr><td colspan="4">Subject D</td><td colspan="4">Subject E</td></tr><tr><td>Category</td><td>Speech act verb</td><td>Description</td><td>Step</td><td>Category</td><td>Speech act verb</td><td>Description</td><td>Step</td></tr><tr><td rowspan="2"> $IN_{1aa}$ </td><td rowspan="2">Search out</td><td rowspan="2">Search objects in memory</td><td rowspan="2">1</td><td> $IN_{1aa}$ </td><td>Trace</td><td>Trace object names</td><td>1</td></tr><tr><td> $IN_{-1}$ </td><td>Set up a list</td><td>Set up an object list</td><td>2</td></tr><tr><td> $IN_{1aa}$ </td><td>Examine</td><td>Examine objects for regularity</td><td>2</td><td> $IN_{1aa}$ </td><td>Examine</td><td>Examine for regularities</td><td>3</td></tr><tr><td> $IN_{2a}$ </td><td>Detect</td><td>Detect objects chunks</td><td>3</td><td> $IN_{3aa}$ </td><td>Classify</td><td>Classify chunks</td><td>4</td></tr><tr><td> $IN_{2a}$ </td><td>Put information into</td><td>Put chunks into a lattice</td><td>4</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"> $IN_{3aa}$ </td><td rowspan="2">Arrange</td><td rowspan="2">Arrange chunks into an ordered structure</td><td rowspan="2">5</td><td> $IN_{3aa}$ </td><td>Sort</td><td>Sort into ordered trees</td><td>5</td></tr><tr><td> $IN_{8a}$ </td><td>Acknowledge</td><td>Acknowledge relationships</td><td>6</td></tr></table>

Table 11 shows that four of the five subjects classified the repertory grid knowledge acquisition method as best expressed by the thinking model. One of the five subjects (subject A), however, selected the theme organization (TO) speech act model. It is interesting to note that the first speech act category of the TO model is the thinking model itself. Hence, the theme organization model is essentially an extension of the thinking model (DE). This, in turn, implies that subject A is not that much at odds with the majority's speech act model selection. A further analysis of the data indicates that subject A described the repertory grid method using only seven steps, while the other subjects' descriptions range from nine to twelve steps. Furthermore, some subjects did also consider the TO speech act model, but rejected it after some thought, because the model fails to describe all the nine to twelve steps. This suggests that the selection of a different speech act model by subject A is due to the granularity or the level of detail of expressing the knowledge acquisition's procedural steps.

Please also notice that steps one to five and seven to eleven of Table 10 equate with speech act categories $DE_{6b}$ and $DE_{6c}$ respectively. This suggests two distinct activity clusters in the repertory grid method. Although subjects B, C and E (who also selected the DE model) show additional speech act categories, the majority of them are subcategories of $DE_{6}$ , which contains speech act categories for describing the various thinking procedures. Thus, these subjects agree that the repertory grid method is a thinking procedure, and the different speech act subcategories within $DE_{6}$ are attributed to the granularity or the level of detail of expressing the knowledge acquisition's procedural steps.

Table 9. Speech act category codes for the repertory grid method, stages one to two, subject D

<table><tr><td>Step</td><td>Description</td><td>Speech act verb</td><td>Speech act category</td></tr><tr><td>1</td><td>Select a problem</td><td>Select</td><td> $DE_{6b}$   $IN3_{ba}$   $TO_{3a}$   $VV_{g}$ </td></tr><tr><td>2</td><td>Select objects in domain of expertise</td><td>Select</td><td> $DE_{6b}$   $IN3_{ba}$   $TO_{3a}$   $VV_{g}$ </td></tr><tr><td>3</td><td>Pick out three objects</td><td>Pick out</td><td> $DE_{6b}$   $IN5_{ac}$   $IN3_{ba}$ </td></tr><tr><td>4</td><td>Define dimension for objects</td><td>Define</td><td> $TO_{2a}$ </td></tr><tr><td>5</td><td>Rate the objects on this dimension</td><td>Rate</td><td> $VV_{g}$   $WTO$ </td></tr><tr><td>6</td><td>Repeat steps three to five</td><td>Repeat</td><td> $TV_{7d}$ </td></tr><tr><td>7</td><td>Record the results</td><td>Record</td><td> $DE_{1}$   $ET/TE_{ab}$   $VV_{a}$ </td></tr><tr><td>8</td><td>Add missing values</td><td>Add in</td><td> $TO_{2d}$ </td></tr><tr><td>9</td><td>Group the objects</td><td>Group</td><td> $IN3_{ac}$ </td></tr><tr><td>10</td><td>Group the dimensions</td><td>Group</td><td> $IN3_{ac}$ </td></tr><tr><td>11</td><td>Work out a focused grid</td><td>Work out</td><td> $KA_{2b}$   $KA_{4cac}$   $KA_{4cbc}$   $KA_{1db}$   $TV_{6a}$ </td></tr><tr><td>12</td><td>Review and alter the grid</td><td>Review, alter</td><td> $ET/TE_{a}$   $KA_{-1d}$   $TE_{-1b}$   $TE_{0bb}$   $TO_{2e}$   $TV_{6'b}$   $TV_{7b}$ </td></tr></table>

## Coherence method

Abdul-Gader and Kozar (1990) recommend the coherence method as a technique for analysing, interpreting and comprehending data arising from verbal interactions between the knowledge engineer and the domain expert. In short, the coherence method is a supplement to commonly used knowledge acquisition techniques.

Table 10. Fit thinking model (DE) to repertory grid method, stage four, subject D

<table><tr><td>Category</td><td>Speech act verb</td><td>Description</td><td>Step</td></tr><tr><td> $DE_{6b}$ </td><td>Choose</td><td>Choose a problem or objective</td><td>1</td></tr><tr><td> $DE_{6b}$ </td><td>Select</td><td>Select objects</td><td>2</td></tr><tr><td> $DE_{6b}$ </td><td>Pick out</td><td>Pick out three objects</td><td>3</td></tr><tr><td> $DE_{6b}$ </td><td>Choose</td><td>Choose dimension</td><td>4</td></tr><tr><td> $DE_{6b}$ </td><td>Rank</td><td>Rank the objects</td><td>5</td></tr><tr><td></td><td>Repeat steps 3 to 5</td><td></td><td>6</td></tr><tr><td> $DE_{6c}$ </td><td>Arrange</td><td>Arrange the result into a grid</td><td>7</td></tr><tr><td> $DE_{6c}$ </td><td>Make out</td><td>Make out the missing values</td><td>8</td></tr><tr><td> $DE_{6c}$ </td><td>Classify</td><td>Classify the objects into clusters</td><td>9</td></tr><tr><td> $DE_{6c}$ </td><td>Classify</td><td>Classify the dimensions into clusters</td><td>10</td></tr><tr><td> $DE_{6c}$ </td><td>Arrange</td><td>Arrange clusters into a focused grid</td><td>11</td></tr><tr><td> $DE_{8c}$ </td><td>Judge</td><td>Judge the grid&#x27;s appropriateness</td><td>12</td></tr></table>

Table 11. Speech act models for selected knowledge acquisition methods

<table><tr><td>Subject code/name</td><td>DE</td><td>IN</td><td>ET</td><td>TO</td></tr><tr><td colspan="5">Recall method</td></tr><tr><td>A.</td><td></td><td>*</td><td></td><td></td></tr><tr><td>B.</td><td></td><td>*</td><td></td><td></td></tr><tr><td>C.</td><td></td><td>*</td><td></td><td></td></tr><tr><td>D.</td><td></td><td>*</td><td></td><td></td></tr><tr><td>E.</td><td></td><td>*</td><td></td><td></td></tr><tr><td colspan="5">Grid method</td></tr><tr><td>A.</td><td></td><td></td><td></td><td>*</td></tr><tr><td>B.</td><td>*</td><td></td><td></td><td></td></tr><tr><td>C.</td><td>*</td><td></td><td></td><td></td></tr><tr><td>D.</td><td>*</td><td></td><td></td><td></td></tr><tr><td>E.</td><td>*</td><td></td><td></td><td></td></tr><tr><td colspan="5">Coherence method</td></tr><tr><td>A.</td><td>*</td><td></td><td></td><td></td></tr><tr><td>B.</td><td></td><td>*</td><td></td><td></td></tr><tr><td>C.</td><td></td><td>*</td><td></td><td></td></tr><tr><td>D.</td><td></td><td>*</td><td>*</td><td></td></tr><tr><td>E.</td><td>*</td><td></td><td></td><td>*</td></tr></table>

DE, thinking model; IN, information model; ET, experience and text model; TO,  
theme organization model.

Abdul-Gader and Kozar (1990) further argue that the coherence method is particularly useful at the start of the expert system developmental process. The verbal data from initial and exploratory interviews with the expert are often ill-structured. The coherence method is helpful at this stage, because it analyses the discourse at the level of the sentence, the relationship between contiguous sentences and collections of sentences. Analysis of collections of sentences provides insight into recurring themes, which guide the expert during his decision-making. The coherence method also brings into focus the areas of the knowledge domain that need additional exploration. This, in turn, helps the expert system developer to plan additional interviewing strategies.

As shown in Table 11, the choice between the thinking and information models is two to three. Two of the five subjects (D and E) conclude that the coherence method is best described by a mix of speech act models. Even though subjects A and E selected the thinking model, their choice leaves steps unaccounted for. Similarly, even though subjects B, C and D selected the information model, their choice too leaves steps unaccounted for. Hence, both the thinking and information models are questionable choices for describing the essential features of the coherence method.

## DISCUSSION

## Exploratory study results

Table 11 summarizes the overall results of the study. For the recall and the repertory grid methods, the independent analytical results of the five subjects were equal (recall method) to nearly equal (repertory method). In the case of the coherence method, however, the opinions among the five subjects were divided. Several reasons for the mixed results can be identified. First, it might be argued that the speech act-based procedure breaks down for more complex knowledge acquisition techniques. Second, it might be said that individual steps of complex knowledge acquisition techniques should be described by one to several speech act models. Third, the disparate results might reveal unnoticed or unsuspected problems with the coherence knowledge acquisition method. We shall consider these possibilities in turn.

Between the repertory grid and the recall knowledge acquisition techniques there is, in fact, a significant jump in complexity. The repertory grid technique itself is more complex, but also the type of knowledge being described is more intricate. Yet, in the case of the aforementioned models, agreement among the independent results of the participants remained almost perfect. Thus, the contention that the lexicon-based procedure is inappropriate when evaluating complex knowledge acquisition techniques is not supported by our exploratory results.

The suggestion that describing the more complex knowledge acquisition techniques accurately calls for two or more speech act models is more promising. In fact, two of the five subjects suggested the need for mixing speech act models to describe more complex knowledge acquisition methods. From the notes of one of the participants (E), we quote: ‘... rather than apply an either-or approach to identifying a speech act model, a combination of models should be encouraged . . .’. Subject E then continues by suggesting that this should be in the form of a single speech act model combined with different supplemental models. The possibility of multiple models, however, is somewhat undercut, because the five experimental subjects did not agree on which speech act model best describes the coherence method (Table 11).

We now consider the third possibility, that disagreement on speech act models might reveal unnoticed or unsuspected problems with the coherence knowledge acquisition technique. In their article, Abdul-Gader and Kozar (1990) described the essentials and complexities of knowledge acquisition, explained in detail the coherence method and discussed its application to knowledge acquisition for developing an expert system for oil exploration.

While investigating the mixed exploratory results, we reread closely Abdul-Gader and Kozar's (1990) coherence method article. This involved teasing out major themes, classifying relationships between themes and tracing out potential patterns of theme occurrences. Based on the evidence, we became convinced that the oil exploration case study did not report insights gained from actual experience with the coherence method but, instead, illustrated how it could be used. Further contacts with the coherence method's authors confirmed our findings (K. Kozar, personal communication, 1993).

Hence, we suggest that the disagreement among the five subjects can be traced back to the way Abdul-Gader and Kozar (1990) describe the theory and application of the coherence method. After proposing the coherence method as a valuable technique, the article then theorizes about application issues. Recommendations concerning the application of the coherence method were not tested and subsequently not refined by first-hand practical experience.

Thus, we propose that the inconsistent explanatory results reflect the provisional status of the aforementioned recommendations and are not caused by inherent weaknesses of the lexicon-based speech act classificatory procedure. In fact, had we not attempted to find a speech act model, we would not have discovered the difficulties with Abdul-Gader and Kozar's recommendations.

## Implications of the exploratory study

As noted by Ballmer and Brennenstuhl (1981, pp. 56–57), speech act taxonomies based on speech act theory alone are neither exhaustive nor exclusive. As a result, some speech acts are not accounted for by such taxonomies, whereas others can belong to more than one category. This suggests speech acts that are unclassifiable, or speech acts that can be classified into multiple categories. These ambiguities cause individuals who independently analyse identical speech acts to arrive at conflicting speech act classifications. When agreement between evaluators cannot be reached through negotiation, the usefulness of speech act theory becomes suspect.

Ballmer and Brennenstuhl's lexicon-based speech act classification procedure does not suffer the flaws mentioned above. This fact is corroborated by the nearly unanimous agreement among the five subjects who independently investigated the recall and repertory grid knowledge acquisition methods. The only exception to their consistency is in the use of the coherence method, in which intersubject disagreement arose from the characteristics of the knowledge acquisition method. Discussions with the coherence method originators (K. Kozar, personal communication, 1993) confirmed our initial impression.

Finally, the exploratory results are not limited to knowledge acquisition but, instead, are applicable to additional instances of speech act theory use. For example, Auramäki et al. (1988) noted difficulties with interpreting the results of analysing an office information system. Based on our experience with the lexicon-based procedure, we propose that a corrective method similar to the fourth stage of Figure 1 would reduce the problem noted by Auramäki et al. (1988). In other words, when ambiguity occurs, one should consider speech acts that are sequenced in time, effectiveness, efficiency or some other dimension, and speech acts that are linked to the same speech act model (Ballmer and Brennenstuhl, 1981).

## Limitations

Our study has several limitations: it used a convenience sample, a small sample size and it investigated just three knowledge acquisition methods. In addition, the study's five subjects were graduate students who may or may not be representative of the population of practising knowledge engineers. Also, the application of Ballmer and Brennenstuhl's (1981) speech act lexicon focused on knowledge acquisition methods only. Hence, one should be careful when extending this study's findings to information systems in general. Finally, because the study is exploratory and limited to five subjects, any suggestion of statistical significance would be entirely inappropriate.

## DIRECTIONS FOR FURTHER RESEARCH

In this section, we set forth our ideas for future research directions. We hope that these ideas, together with the results reported in this paper, will motivate others in the information systems community to adopt the lexical approach for their own research.

## Replication of the study

We would like to replicate our study using larger sample sizes and a greater variety of knowledge acquisition methods. Unfortunately, it is difficult to find subjects who are familiar with knowledge acquisition systems and who can make the considerable time commitment needed for the study. Therefore, rather than aiming for statistical significance, it would be more effective to use the limited number of available subjects to gain additional insight into the extent to which a speech act lexicon can resolve message ambiguity. Given the high level of agreement among the subjects in our exploratory study on the nature of the knowledge acquisition methods, we expect that only a limited number of additional replications are needed to capture all the potential variation in the answers. Even if this were not the case (i.e. Ballmer & Brennenstuhl's lexicon does not help resolve message ambiguity), we would have learned something useful about the role of speech act theory in information systems.

## Classification of knowledge acquisition methods

We would like to derive a classification of knowledge acquisition methods using the four-step procedure (Figure 1) to analyse commonly used knowledge acquisition methods. In this paper, we have already identified the multidimensional and repertory grid knowledge acquisition methods as belonging to the same class, because they are best described by Ballmer and Brennenstuhl's (1981) thinking model. To follow up this research direction, we suggest performing qualitative case studies to identify any differences among the use of knowledge acquisition methods of the same class.

## Classification of systems analysis and design methods

While this exploratory study applied the four-step procedure (Figure 1) to knowledge acquisition methods, it can also be used to analyse and categorize alternative information systems analysis and design methods. There have already been many such comparative studies of information systems and analysis methods and, hence, we do not expect that further studies would provide additional significant insights. However, such comparative studies should be seen as a way of testing the lexicon-based four-step procedure. The results of studying system analysis methods using the four-step procedure can then be contrasted with the results from numerous other studies. Substantial correspondence between the findings of different studies would be a corroboration of our four-step procedure.

## Office activity modelling

We would like to augment the speech acts used in SAMPO (Auramäki et al., 1988) by using Ballmer and Brennenstuhl's (1981) lexicon-based speech act classification. The purpose of information passing would be specified by speech acts, which in turn are linked through Ballmer and Brennenstuhl's speech act lexicon. In other words, our four-step procedure (Figure 1) can help select speech acts and speech act models. We suggest that adding the linkage component (specified using speech act models) would reduce the number of alternative interpretations of a conversation graph when analysed by different individuals.

## Computer supported communication

We would like to alter the Co-ordinator (Flores et al., 1988), which is based on Searle's speech act theory, by a speech act lexicon-based communication protocol and then repeat the Carasik and Grantham (1988) study. The overall modified protocol would comprise several smaller protocols that each represent a speech act model of Ballmer and Brennenstuhl's (1981) speech act classification. The corrective step (Figure 1, step 4) could then be incorporated into the overall protocol as a way to incorporate 'context'.

A conversation might start using a protocol that is based on a certain speech act model. As it proceeds, the participants might come to realize that their communication is better described by a protocol based on an alternative speech act model. The communication system would then allow the communicators to switch to the new speech act model. It should be interesting to see which of the Co-ordinator's problems, reported by Carasik and Grantham (1988), would be resolved by the aforementioned protocol. An issue of equal importance is whether the new communication protocol gives rise to new communication problems.

## CONCLUSIONS

Earlier speech act applications, such as Co-ordinator and SAMPO, encountered some unexpected difficulties because individuals with divergent contextual views categorized and interpreted speech acts differently. The procedure that we constructed, discussed, demonstrated and empirically explored is based on Ballmer and Brennenstuhl's (1981) speech at lexicon and modelling system. The speech act lexicon directs the sender who generates the speech acts and the receiver who interprets them. Hence, in contrasts to other methods for categorizing speech acts, Ballmer and Brennenstuhl's system explicitly includes contextual information in the form of its speech act lexicon and system of models.

To demonstrate the potential contribution of our four-stage procedure to information systems, we conducted an exploratory empirical study involving five subjects who independently analysed three knowledge acquisition methods. There was good agreement among the subjects on the nature of two out of three knowledge acquisition methods. Even though some of the subjects did not always select exactly the same series of speech act categories, we discovered that the inconsistencies arose out of the level of detail or the degree of granularity to which individual subjects carried out their analysis.

In one instance, there was a high level of disagreement among the analytical results reported by the five subjects. An in-depth study led us to conclude that these conflicting results did not arise from our procedure but, rather, from previously unsuspected problems with the coherence knowledge acquisition method.

The contribution of our project is fourfold. First, we introduced an alternative speech act theory for use in information systems. We then demonstrated its application through a detailed analysis of the procedural steps of several knowledge acquisition methods using Ballmer and Brennenstuhl's speech act categories and models. Second, we introduced the idea that mapping an utterance to a speech act category requires two distinct stages and, therefore, using Ballmer and Brennenstuhl's lexicon by itself is insufficient for incorporating contextual information. We overcame this difficulty by introducing the fourth stage of our four-stage lexicon-based procedure. Third, we discovered a limitation of Ballmer and Brennenstuhl's speech act lexicon, which in effect says that in cases in which the level of detail or degree of granularity of the analysis is insufficient, multiple interpretations of speech acts can still occur. Fourth, we suggested other promising research avenues, whereby Ballmer and Brennenstuhl's speech act lexicon can make contributions to information systems.

## ACKNOWLEDGEMENTS

The authors gratefully acknowledge the support of the University of Missouri-St Louis, Office of the Vice Chancellor for Academic Affairs, and Center for International Studies; the University of British Columbia, Humanities and Social Sciences Small Grants Division.

## APPENDIX

## The recall knowledge acquisition method

The recall method comprises two parts (Olson & Rueter, 1987; Janson & Woo, 1992). First, the knowledge engineer selects an object used by the expert during a decision-making task. The expert is then asked to recall additional objects that are used in conjunction with the original object. This procedure is repeated many times with different randomly chosen objects. The outcome is a series of alternative object strings used during the expert's problem-solving activity. Second, object strings are examined for regularity. Of particular interest are objects recalled in chunks that appear in many alternative object strings. These chunks suggest that the expert views these objects as integral to problem-solving.

For example, computing averages, summing and counting observations feature prominently in statistical data base problem-solving. Thus, when requested to recall dBase commands, the expert may include {sum, count, average} in one sequence, and {average, sum, count} in a different sequence. The series {average, sum, count} is a chunk of objects recalled together. The knowledge engineer, after first documenting the aforementioned object chunk, continues the search for other object chunks.

## The repertory grid knowledge acquisition method

This method is based on Kelly's (1955) personal construct theory. A repertory grid is a two-dimensional matrix comprising (1) objects in the expert's problem domain; and (2) object characteristics (Olson & Rueter, 1987; Shaw & Woodward, 1990).

The knowledge engineer meets with the expert and elicits entities or objects, which the expert uses during problem-solving (LaFrance, 1988). The knowledge engineer then constructs object triads and asks the expert which characteristics set any two object pairs apart from the third object. This process terminates when the knowledge engineer decides that key object dimensions have been identified. Several techniques enable analysing the repertory grid (Boose, 1985). Two such techniques are hierarchical clustering and multidimensional scaling (Olson & Rueter, 1987).

## The coherence knowledge acquisition method

The coherence method comprises three steps: (1) developing a world plan; and (2) generating micro- and (3) macro-discourse structures (Abdul-Gader & Kozar, 1990).

The world plan defines the global context in which the expert performs his or her decision-making tasks. This plan focuses on two aspects of the expert's discourse: explaining how a task should be performed and describing how the task is performed.

Micro-structures originate from identifying relationships between clauses of individual sentences and from analysing relationships between two or more sentences. Examples of these clauses are explanation, parallelism, contrast and temporal sequencing. Macro-structures arise from investigating multiple sentences and paragraphs. These structures describe the goals and themes that hold the entire discourse together.

Abdul-Gader and Kozar (1990) state that the coherence method is a data-oriented bottom-up approach. The world plan, developed in the first stage, links the data arising from discourse analysis with the expert's overall goals and purposes.

## The theme organization speech act model

The theme organization (TO) model belongs to the 'theme models' group. Its categories comprise speech act verbs that specify thematic structures of discourses. The categories are:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1 Systematically searching data (IN$_{1a}$)
Describes how to find data:
a performing a general search (IN$_{1aa}$);
b raising questions (IN$_{1ab}$); and
c hypothesizing (IN$_{1ab}$).

2 Finding data (IN$_{2}$)
Describes how data were obtained:
a directly (IN$_{2a}$);
b implied (IN$_{2a*}$);
c by problem solving (IN$_{2a'}$); and
d received from someone (IN$_{2b}$).
(Note: the symbols * and ' augment the alphabetical subscript).

3 Organizing and evaluating data (IN$_{3}$)
Presents data in useable form:
a arranging data (IN$_{3aa}$);
b testing usefulness of data arrangement (IN$_{3ab}$);
c categorizing data (IN$_{3ac}$);
d comparing data (IN$_{3ba}$); and
e evaluating data (IN$_{3bb}$).

4 Recalling data (IN$_{5}$)
Searches previously known but subsequently lost data:
a thinking back (IN$_{5aa}$);
b searching without recall (IN$_{5ab}$);
</div>

1 Thinking ( $TO_{1}$ ): activities specified by the thinking model (DE) are organized into themes.

2 Thematizing (TO₂): describes how to organize and structure thematic data:

a clustering data round a broad theme (TO $_{2a}$ );

b clustering data around a narrow theme (TO $_{2b}$ ); and

$$
\left(\mathrm{TO} _ {2 \mathrm{c}}\right)
$$

3 Structuring (TO $_{3}$ ): structuring data (TO $_{3a}$ ) and restructuring data (TO $_{3b}$ ).

4 Connecting data and/or structures ( $TO_{4}$ ): grouping related data and/or structures.

5 Accentuating data differences (TO $_{5}$ ):

a focusing on data (TO $_{5a}$ );

b accentuating data features (TO $_{5b}$ );

c de-emphasizing data features (TO $_{5c}$ ); and

d comparing/contrasting data (TO $_{5e}$ ).

Table 2 shows typical speech act verbs for the categories of the theme organization model.

## The information speech act model

The information (IN) model belongs under the 'text models' group. Its categories include speech act verbs for searching, examining, questioning and hypothesizing about data.

c extracting data (IN $_{5ac}$ ); and

d moving data from long-term to short-term memory (IN $_{5b}$ ).

## 5 Distributing data (IN $_{6}$ )

Informs others of the data: circulating, diffusing, spreading, publishing, depicting, posting and reporting (IN $_{6aa}$ ).

Table 2 shows typical speech act verbs for the categories of the information model.

## REFERENCES

Abdul-Gader, A. & Kozar, K. (1990) Discourse analysis for knowledge acquisition: the coherence method. Journal of Management Information Systems, 6, 62–82.

Agarwal, R. & Tanniru, M.R. (1990) Knowledge acquisition using structured interviewing: an empirical investigation. Journal of Management Information Systems, 7, 123–140.

Angeles, P. (1981) Dictionary of Philosophy. Barnes and Noble, New York.

Argyris, C., Putnam, R. & McLain Smith, D. (1985) Action Science. Jossey-Bass, San Francisco.

Argyris, C. (1990) Overcoming Organizational Defences.
Allyn and Bacon, Boston.

Auramäki, E., Lehtinen, E. Lyytinen, K. (1988) A speech-act-based office modeling approach. ACM Transactions on Office Information Systems, 6, 126–152.

Austin, J.L. (1962) How to do Things with Words, 2nd edn, Urmson, J.O. & Sbisa, M. (eds), Harvard University Press, Cambridge, MA.

Ballmer, Th. & Brennenstuhl, W. (1981) Speech Act Classification. Springer-Verlag, New York.

Barrett, R.A. & Davis, B.C. (1986) 'Successful systems analysts analysts hone their communication skills.' Data Management, 24(4), 18–21.

Benbasat, I. & Dhaliwal, J. (1989) A framework for the validation of knowledge acquisition. Knowledge Acquisition, 1, 215–233.

Bogen, D. (1991) The doctrine of literal expression in Searle. Journal of Theory and Social Behavior, 20, 31–63.

Boose, J.H. (1985) A knowledge acquisition program for expert systems based on personal construct psychology. International Journal of Man–Machine Studies, 23, 495–525.

Bostrom, R.P. (1989) Successful application of communication techniques to improve the systems development process. Information and Management, 16, 279–295.

Bowers, J. & Churcher, J. (1988) Local and global structuring of computer mediated communication: developing linguistic perspectives on computer-supported cooperative work in COSMOS. In: Proceedings of the Conference on Computer-Supported Cooperative Work, Suchman, L. (ed.), Portland, OR, 26–28 September, 1988. Association for Computing Machinery, New York, 125–139.

Carasik, R.P. & Grantham, C.E. (1988) A case study of computer-supported cooperative work. In: Proceedings of the Conference on Human Factors in Computing Systems, Washington, DC., 15–19 May, 1988. Association for Computing Machinery, New York, 61–66.

De Cindio, F., De Michelis, G., Simone, C., Vassalo, R. & Zanaboni, A. (1986) Chaos as a coordination technology. In: Proceedings of MCC Conference on Computer Support for Cooperative Work. Austin, TX, 3–5 December, 1986. Micro Computing Corporation, Austin, TX, 325–342.

De Michelis, G. & Grasso, M.A. (1994) Situating conversations within the language/action perspective: the Milan conversation model. In: Proceedings of the Conference on Computer Supported Cooperative Work, Furuta, R. & Neuwirth, C. (eds.), Chapel Hill, NC, 22–26 October, 1994. Association for Computing Machinery, New York, 89–100.

Dhaliwal, J.S. & Benbasat, I. (1990) A framework for the comparative evaluation of knowledge acquisition tools and techniques. Knowledge Acquisition, 2, 145–166.

Dietz, J.L.G. & Widdershoven, G.A.M. (1991) Speech acts or communicative action? In: Proceedings of the Second European Conference on Computer-Supported Cooperative Work (ECSCW), Bannon, L., Robinson, M., & Schmidt, K. (eds), Kluwer, Amsterdam, The Netherlands, 235–248.

Dietz, J.L.G. (1992) Modeling communication in organizations. In: Linguistic Instruments in Knowledge Engineer

ing, Riet, R.v.d. (ed.), North Holland, New York, 131–143.

Flores, F. & Ludlow, F. (1980) Doing and speaking in the office. In: Proceedings of an International Task Force Meeting, Goeran, F. & Sprague, R. (eds), Pergamon, New York, 95–118.

Flores, F., Graves, M., Hartfield, B. & Winograd, T. (1988) Computer systems and the design of organizational interaction. ACM Transactions on Office Information Systems, 6, 153–172.

Goldkuhl, G. & Lyytinen, K. (1984) Information system specification as rule reconstruction. In: Beyond Productivity: Information Systems Developments for Organizational Effectiveness, Bemelmans, Th.M.A. (ed.), North Holland, New York, 79–94.

Guinan, P.J. (1988) Patterns of Excellence for IS Professionals: An Analysis of Communication Behavior. ICIT Press, Washington, DC.

Habermas, J. (1981) The Theory of Communicative Action, Vol. 1. Beacon Press, Boston, MA.

Hart, A. (1989) Knowledge Acquisition for Expert Systems. Kogan Page, London.

Janson, M. & Woo, C. (1992) Investigating information and knowledge gathering methods: a speech act lexicon perspective. In: Information System Concepts: Improving the Understanding, Falkenberg, E.D., Rolland, C., & El-Sayed, E.N. (eds), North Holland, New York.

Johannesson, P. (1995) Representation and communication – a speech act based approach to information systems design. Information Systems, 20, 291–303.

Kaplan, S., Tolone, W., Bogia, D. & Bignoli, C. (1992) Flexible, active support for collaborative work with conversation builder. In: Proceedings of the Conference on Computer-Supported Cooperative Work, Toronto, Canada, 31 October–4 November, 1992. Association for Computing Machinery, New York, 378–385.

Kelly, G.A. (1955) The Psychology of Personal Constructs. Norton, New York.

Lanigan, R.L. (1977) Speech Act Phenomenology. Martinus Nijhoff, The Hague, The Netherlands.

LaFrance, M. (1988) The knowledge acquisition grid: a method for training knowledge engineers. In: Knowledge-Based Systems, Vol. 1, Gaines, B. & Boose, J. (eds), Academic Press, New York, 81–91.

Levinson, S.C. (1988) Pragmatics. Cambridge, New York.

Liebenau, J. & Backhouse, J. (1990) Understanding Information: An Introduction. Macmillan, London.

Lyytinen, K.J. (1985) Implications of theories of language

for information systems. Management Information Systems Quarterly, 9, 61–74.

Malone, T.W. & Crowston, K. (1990) What is coordination theory and how can it help design cooperative work systems? In: Proceedings of the Conference on Computer Supported Cooperative Work, Los Angeles, CA, 7–10 October, 1990. Association for Computing Machinery, New York, 357–370.

Maybury, M.T. (1992) Communicative acts for explanation generation. International Journal Man–Machine Studies, 37, 135–172.

Olson, J. & Rueter, H.H. (1987) Extracting expertise from experts: methods for knowledge acquisition. Expert Systems, 4, 152–168.

Orlikowski, W.J. (1995) Categories: concept, content, and context. Computer Supported Cooperative Work: An Internation Journal, 3, 73–78.

Ngwenyama, O.K. & Klein, H.K. (1994) An exploration of expertise of knowledge workers: towards a definition of the universe of discourse for knowledge acquisition. Information Systems Journal, 4, 141–166.

Reiss, N. (1985) Speech Act Taxonomy. Benjamins Publishing Company, Philadelphia, PA.

Searle, J.R. (1969) Speech Acts: An Essay in the Philosophy of Language. Cambridge University Press, Cambridge, UK.

Searle, J.R. (1975) Indirect speech acts. In: The Logic of Grammar, Davison, D. & Harman, G. (eds), Dickenson Publishing, Eucino, CA, 59–82.

Searle, J.R. (1979) A taxonomy of illocutionary acts. In: Expression and Meaning: Studies in the Theory of Speech Acts, Searle, J.R. (ed.), Cambridge University Press, Cambridge, UK. 1–29.

Searie, J.R. & Vanderveken, D. (1985) Illocutionary Logic. Cambridge University Press, New York.

Shaw, M.L.G. & Woodward, J.B. (1990) Modeling expert knowledge. Knowledge Acquisition, 2, 179–206.

Stamper, R. (1987) Semantics. In: Critical Issues in Information Systems Research, Boland, R.J. & Hirschheim, R.A. (eds), Wiley, New York, 43–48.

Suchman, L. (1994) Do categories have politics? Computer Supported Cooperative Work, 2, 177–190.

Van Reijswoud, V.E. (1993) A transaction analysis-based approach for requirement determination of computer mediated communication systems. Research Memorandum, No. RM 93–059, Limburg University, Maastricht, Netherlands.

Voss, K. (1992) Reflexions concerning the paper: investigating information and knowledge gathering methods: a

speech act lexicon perspective. Presented at International Federation for Information Processing Conference, WG 8.1 conference Information System Concepts: Improving the Understanding. Alexandria, Egypt.

Weisberger, L. (1962) Basics of a Content Derived Grammar. Schwann Press, Düsseldorf, Germany.

Wilson, M. (1989) Task models for knowledge elicitation. In: Knowledge Elicitation: Principles, Techniques, and Applications, Diaper, D (ed.), John Wiley, New York, 197–219.

Winograd, T. (1994) Categories disciplines, and social coordination. Computer Supported Cooperative Work, 2, 191–197.

Winograd, T. & Flores, F. (1986) Understanding Computers and Cognition: A New Foundation for Design. Addison Wesley, Addison.

## Biographies

Carson Woo is Associate Professor in the Management Information Systems Division at the Faculty of Commerce and Business Administration and associate member in the Department of Computer Science, the University of British Columbia, Vancouver, Canada. In the fall of 1992 he spent four months as Visiting Scientist at the Centre for Advanced Studies, IBM Canada Laboratory in Toronto. He received his BSC, MSc., and PhD degrees in Computer Science from the University of Toronto. Dr Woo served as Chair Person of the Special Interest Group on Office Information Systems (SIGOIS) of the Association for Computing Machinery from 1991 through 1995.

Marius Janson is Associate Professor of Management Science and Information Systems at the University of Missouri-St. Louis. He earned his PhD degree in management science and information systems at the University of Minnesota. His research interests centre on the application of speech act theory to information systems modelling, and social and international issues concerning information systems use. Dr Janson's articles have appeared in Decision Sciences, Information & Management, Journal of Economic and Business Statistics, Journal of Management Information Systems, Management Information Systems Quarterly, and Omega.
