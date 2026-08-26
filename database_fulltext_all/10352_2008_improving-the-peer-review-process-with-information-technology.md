---
otero_id: 10352
otero_key: "S5HJKAQR"
title: "Improving the peer review process with information technology"
authors: "Munir Mandviwalla; Ravi Patnayakuni; David Schuff"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.04.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving the peer review process with information technology

Munir Mandviwalla <sup>a</sup>, Ravi Patnayakuni <sup>b</sup>, David Schuff <sup>a,</sup>⁎

<sup>a</sup> Temple University, United States

<sup>b</sup> University of Alabama, United States

## a r t i c l e i n f o

Article history: Received 5 June 2007 Received in revised form 20 April 2008 Accepted 27 April 2008 Available online 2 May 2008

Keywords: Peer review Scholarship Design science Process improvement Prototype

## a b s t r a c t

Peer review is the engine of scholarship where new knowledge is legitimized. Despite technological advances in publishing and communication, the process of review has not changed since it became prevalent over 100 years ago. This paper describes how information technology can be used to improve the peer review process. Taking a combined design science and natural science approach, we design and test a prototype system based on the principles of structured communication. Through an exploratory study, we <sup>fi</sup>nd that our proposed system is viewed more favorably by both authors and reviewers across several dimensions, including fairness, convenience, and value.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Information technology has fundamentally changed the production and dissemination of new knowledge. For example, in academia knowledge producers (authors) create manuscripts on sophisticated word processing software, share drafts and discuss ideas using a variety of communication tools, and produce print-ready journal copy using desktop publishing software. Teams of scientists can share and work on complex projects in ways that were simply not possible a few years ago, while authors of textbooks are now experimenting with electronic delivery mechanisms that will radically change the distribution model of the publishing industry.

Despite these technological advances, the process for evaluating the content of publications remains largely unchanged. The focus of this paper is peer review, the process by which new knowledge is legitimized by its acceptance and dissemination to the wider community. Peer review is often described as an instance of decision making (e.g., [33]), and as an example of knowledge production and dissemination. Peer review is also time consuming and expensive. Editors believe that the largest “cost” of producing a journal is reviewing and editing [22]. Weber [34] estimated a reviewing “opportunity cost” of \$24,500 for each published paper in Management Information Systems Quarterly.

IT has already impacted the peer review process, most notably in the use of web-based document management tools that can manage the process of submission, review, and arriving at an editorial decision. Yet the peer review process itself is essentially the same as it was since it became prevalent over 100 years ago [28]. Most information technologies simply automate the review process (e.g., [9]). The current peer review process of (often) slow back and forth deliberation among authors, reviewers, and editors continues the legacy of an earlier era de<sup>fi</sup>ned by infrequent, high-cost communication. Watson [32] argues that though the Internet has improved some aspects of publishing, most of the changes are simple and focus on the tasks of publication (“alpha level”), there has been little to no change to people's roles (“beta change”) or a restructuring of the underlying system (“gamma change”).

There is, however, a fundamental dilemma in researching how to use IT to improve the peer review process. There is no current literature that fully elaborates the potential problems. Further, there are no comprehensive behavioral models that can explain the impact of proposed IT enabled improvements. Therefore, we propose that both a design science and natural (behavioral) science research approach is necessary to build new utility into the peer review process and understand the impact of such proposed changes [15,20,31]. Cao et al. [5], who build on Hevner et al. [15], March and Smith [20], and Nunamaker et al.'s [24] design science approaches, suggest that a multi-methodological, cross-paradigm research approach that combines design and behavioral science will yield more powerful and insightful results. Research on the peer review process is at an early stage and very little aggregate knowledge has been accumulated, a combined approach will therefore improve the chances that important behaviors are identi<sup>fi</sup>ed early and only the most useful technical artifacts are built. As Hevner et al. [15] argue, truth and utility are inseparable and “an artifact may have utility because of some as yet undiscovered truth. A theory may yet to be developed to the point where its truth can be incorporated into design” (p. 80).

The remainder of this paper is structured using a combined design and natural science approach. First, we provide perspectives on peer review that illustrate the importance of the problem and our approach. Second, we apply the design science perspective to create a process based model to analyze the traditional peer review process and to serve as a baseline for changing the process. We propose a new process based on structured communication and implemented using a prototype system. Third, and in parallel, we apply the natural science perspective to develop a set of behavioral propositions to evaluate changes to the peer review process. The two perspectives of design and natural science come together in an exploratory study to evaluate the impact of the prototype system. In the <sup>fi</sup>nal sections, the results of the study are discussed.

## 2. The role and challenges of peer review

Improving the peer review process is particularly important for academic publishing. Worldwide growth in the number of higher education institutions has led to an increase in the number of faculty. There is increased pressure on journals because of the increased volume of material requiring review. Word processing has reduced the time cost of resubmitting manuscripts to different outlets. The result is that there is an increasing burden on the traditional volunteer model of peer review accompanied by increasing dissatisfaction with the process. Readers of peer-reviewed research often complain about lack of quality, sterility of material, and irrelevance [10], and observers believe that the traditional peer review process is currently too slow, and lacking in quality, impartiality, validity, and reliability [2,33]. According to Frost and Taylor [10], there are now questions about whether the centralized control structure of peer review and the publication process has led to a lack of innovation in the conventional outlets for academic scholarship. Journals often become equipped to handle the routine rather than recognize innovation and diversity [23]. More generally, at the policy level there have been questions about the application of peer review in science. For example, McCarty [21] outlines the experience of The American Psychologist in which a controversial article was accepted and then later rejected. The controversy was prominently played out on Internet newsgroups; the editor attributed some of the mistakes to the delays inherently built into a system based on postal mail.

As a reaction to these and other problems, some have questioned the very concept of peer review. Horrobin [16] suggests that the peer review concept is fatally <sup>fl</sup>awed because the people who serve as reviewers are never truly peers in terms of ability and that the process may inhibit truly innovative thinking. Bedeian [2] reports that Nobel laureate Rosalyn Yalow in her acceptance speech noted that “the truly imaginative are not being judged by their peers. They have none!” [35].

Others have suggested that although peer review is viable, various improvements to the process should be considered. For example, Apt [1] proposes a model in which computer science can start new, free, high quality journals that are universally accessible to all on the web and which serve to increase the number of outlets available. Others have suggested an entrepreneurial approach that advocates radical changes to knowledge production with ideas such as selfpublishing (“sky writing”) on the web and peer commentary, where comments are added to the published article after it has been peer reviewed [14]. Weblogs are the technical realization of this vision though they remain outside the realm of academic knowledge production. Bedeian [2] proposes a number of socially-motivated improvements to the peer review process including allowing authors to submit a note to reviewers with their submission, publishing referee comments, identifying the referees in the publication, rating review reports, and instituting an appeals process. Brown [4] proposes improvements to the process of peer review by advocating the double-blind evaluation process.

In information systems there have been several efforts to improve peer review. Saunders [27] focuses on how reviewers and editors can practice “developmental reviewing” — the idea of providing the author with very detailed and constructive suggestions for revising the manuscript. Lee [19] outlines how information technology can be used to disseminate research and speed the review process. Weber [33] characterizes peer review as an instance of decision making and proposes improvements that include removing anonymity, and using the web to disseminate both papers under review and rejected papers along with their associated reviews. Watson [32] proposes certi<sup>fi</sup>cation and formal training for reviewers as well as restructuring the relationship between authors, reviewers, and editors into a “marketplace” where editors bid for articles based on reviews by accredited referees and authors evaluate review reports.

Peer review is also being increasingly applied outside academic publishing. Grant makers, accounting audits, policy review, software development, and standards review (e.g., IEEE) all apply peer review. Patton and Olin [25] provide a framework for applying peer review to improve regulatory decisions in response to recent controversies in the United States Congress about con<sup>fl</sup>icts of interest. Accounting <sup>fi</sup>rms use peer review to evaluate other <sup>fi</sup>rms and accountants and there is discussion of how to improve the peer review process to make the results more public (e.g., [29]). Increasingly on the web, user-submitted reviews are used to augment information provided by the manufacturer or retailer (e.g., reviews by customers on Amazon.com) and provide recommendations (e.g., TripAdvisor.com).

![](/api/attachments/S5HJKAQR/fulltext/images/e504de0f4c619912a902b013ed02548507ed41504431729b48c373f71a41f530.jpg)  
Fig. 1. The peer review process in context.

## 3. Part A — design science

## 3.1. Analysis of the peer review process

Peer review has been examined in almost every academic discipline. Yet, most articles are editorial-style thought pieces and there are few theoretical or empirical studies that consider the complete peer review process. Speci<sup>fi</sup>cally, the literature does not go far enough in elaborating, demonstrating, and evaluating how IT can fundamentally change the peer review process. Given that most scholars are not ready to abandon the basic precept of peer review, we assume that review by peers is a given. However, the process by which the process is conducted could be improved. In this section, we build a process-based model of peer review that can identify and explain the problems and suggest potential IT solutions.

Cummings and Frost [7] characterize academic publishing as a system of two related functions<sup>1</sup>. The communication process focuses on communicating high-quality manuscripts to readers, screening out lower quality articles, recognizing good scholarship, and communicating the accomplishments of a <sup>fi</sup>eld to insiders and outsiders. The control process represents managing scarce resources such as available journal pages, gate keeping in terms of paper selection, representation, and power differential among actors.

Cummings and Frost's [7] perspective is compatible with systems thinking. Academic publishing can be seen as a system in which ideas are communicated and controlled through processes to produce knowledge. The traditional peer review process is a type of communication and control process. The process itself has several components. Submitting includes the act of submitting (and resubmitting) the manuscript as well as associated activities such as interpreting submission guidelines, <sup>fi</sup>tting the publication to the guidelines, and logistical challenges in making sure the publication has a reviewable article (e.g., the <sup>fi</sup>le is corrupt, pages are missing, etc.). Reviewing includes the act of reviewing and associated activities such as interpreting the article, selecting reviewers, and dealing with late or inappropriate reviews. Finally, deciding includes making the <sup>fi</sup>nal editorial decision on the paper as well as associated document management activities such as keeping track of reviews.

Fig. 1 depicts peer review as a set of processes that convert ideas into knowledge (published articles), and which are embedded within the larger academic publishing processes of communication and control. Key stakeholders such as authors, reviewers, and editors in<sup>fl</sup>uence the process. Given our focus on peer review, we omit other important processes from Fig. 1 such as journal production (in which accepted papers are queued and prepared for publication). Submitting, reviewing, and deciding are presented sequentially only for illustrative purposes. For example, if an editor rejects a submission because it is in a foreign language, the reviewing process is never instantiated, and the decision is made immediately after submission.

Information technology can support and change the communication and control processes. For example, IT can change control procedures by making the process for submitting manuscripts more convenient. More formally, IT can have a transactional impact [8] by improving the basic control and communication operations involved in knowledge production such as the submission of a manuscript. By allowing submission at any time and from any place, IT can also have a geographical and temporal impact. The ability to make manuscripts available through the web gives IT the opportunity to perform a disintermediation role, and by recording revision marks in manuscripts IT can have a tracking role. IT can thus both improve and change the communication and control processes of academic publishing.

Using this model we can place the perceived problems of traditional peer review in context. For authors, the process of submitting is often confusing and slow. There is perceived lack of transparency and accountability regarding the reviewing process. When the reviews are returned they are often late, lacking in quality because they did not understand their main thesis, and may re<sup>fl</sup>ect particularistic biases. Authors may feel that the process does not add value and that there is pressure to conform to the reviewer's preferences, which may in turn lead to homogeneity of ideas and lack of innovation. Editors, on the other hand, are concerned about the lack of quali<sup>fi</sup>ed reviewers, their responsiveness, and of ensuring consistency among reviews to avoid problems of disagreement among referees. Editors are also concerned about their reputation and may prefer to err on the side of caution resulting in rejection of marginal but potentially innovative articles, indicating problems in the deciding process. Finally, reviewers are underappreciated, feel the pressure to provide extremely detailed “developmental” reviews in the context of submissions that come from increasingly diverse research traditions, methods, and cultures, and wonder about the value they get from the process.

It is interesting to note that most current attempts to apply IT to improve the peer review process have focused on improving the control aspects of the submitting process (e.g., web based upload of documents) and the deciding process (e.g., keeping track of documents and reviews). Few efforts have focused on changing and trying to improve the actual reviewing process (the middle box of Fig. 1). Our focus is to go beyond the traditional automational and control power of IT and consider ways to transform the entire peer review process. The model in Fig. 1 provides a baseline view of the traditional peer review process that can be used to consider transformational changes.

## 3.2. Proposed structured communication process and prototype

## 3.2.1. Structured communication process

Focusing on the communication aspects of the peer review process may lead to substantial improvements. Communication, including informal communication, is an important tool of the scienti<sup>fi</sup>c process [17,28]. We propose to link the key stakeholders (authors, referees, and editors) in the complete cycle of submission, refereeing, editing, presentation, and discussion using a structured communication process. Currently, these stakeholders are connected by mediating roles played by editors. Authors submit articles into a black box and sometime later an acceptance or rejection emerges. Reviewers read submissions divorced from context with no opportunity to engage the author in discussion. Yet, simply increasing communication without controls or structure is not a practical solution. Instead, we propose a structured communication process.

The goal of communication in peer review is to reach an editorial decision regarding an article. Goal-oriented communication has been extensively studied by philosophers, psychologists, sociologists, and others. One particularly relevant strand of work is research on mutual understanding [13,30] and common grounding [6]. According to Te'eni [30], goal-oriented communication consists of core content, context, and intention, and occurs within the context of the communicators' values, norms, and use of resources. The basic premise is that effective communication requires building mutual understanding as well as relationships among the communicators. Yet reaching mutual understanding is very dif<sup>fi</sup>cult because of differences in the values and norms of the communicator and in the availability of contextual information.

In peer review, communication is typically anonymous, sporadic, and conducted over great distances, cultures, and even disciplines, and achieving mutual understanding can be seen as a key factor in reaching the best editorial decision. Therefore, the challenge (and potential bene<sup>fi</sup>t) of improving communication in the peer review process is signi<sup>fi</sup>cant. Te'eni [30] integrates the relevant research on improving communication using information technology and proposes a set of design guidelines focusing on improving mutual understanding. Discussion forums (or bulletin boards) are well known technological tools that are widely used in industry for many different tasks. The structure afforded by the discussion forum design artifact can improve communication and mutual understanding during the review process. We next describe the proposed structured communication review process using the model from Fig. 1. The proposal includes changes to the overall review process per the model in Fig. 1, and changes to the communication processes as afforded by the discussion forum. The key design attributes are summarized by applying Te'eni's guidelines for designing goal-oriented communication support systems in Table 1.

3.2.1.1. Submission. The traditional paper-based reviewing process typically only allows for a single opportunity to submit an article before it is passed through the reviewing cycle. While there are advantages to limiting authors to one complete submission/review/decision process, the use of IT can enhance communication between reviewers and authors so that authors can respond to questions from reviewers and editors between cycles of formal review. In the proposed structured communication process, all submissions are electronic and authors and reviewers interact with each other through an online discussion forum. Authors are allowed to submit additional material pertaining to the submission in response to the reviewers' questions (see below).

## 3.2.1.2. Reviewing

3.2.1.2.1. First stage. The reviewer is asked for a “preliminary decision” regarding the manuscript and is encouraged to ask speci<sup>fi</sup>c questions in the online forum. The review is then made available to other reviewers and authors for discussion and comment during a speci<sup>fi</sup>ed open window of time. During the open time window, authors and reviewers interact with each other and respond to questions and comments, clarify issues, provide additional information, and present arguments. The editors moderate the discussion.

3.2.1.2.2. Second stage. When the open time window is completed, the discussion forum is closed to authors. Reviewers are informed that the discussion is closing and are asked to provide their <sup>fi</sup>nal decision on the article after examining all interactions. All other aspects of the review process remain the same, including protecting the anonymity of the authors and reviewers.

3.2.1.3. Deciding. When the open time period is complete, the editor(s) make the <sup>fi</sup>nal decision using the original reviews and the subsequent interaction in the discussion forum. The major change is that editors now have the interaction on the forum, as well as the article and reviews per the traditional model, on which to base their decision. When a <sup>fi</sup>nal editorial decision has been made, the authors (and reviewers) are informed and are again allowed to view the discussion forum.

Table 1  
Key design attributes of proposed structured communication process

<table><tr><td>Design guidelines (Te&#x27;eni [30])</td><td>Design attributes of proposed system</td><td>Role within the peer review process</td></tr><tr><td>Design must simultaneously consider enhancing mutual understanding and promoting relationships between communicators</td><td>Common space</td><td>The discussion forum provides a common space in which all authors and reviewers can see comments and responses. This common space can foster a sense of community and mutual trust since all content is available to all and all users can add to or start new conversations. Anonymity promotes interaction without fear of reprisal</td></tr><tr><td>Design should support adaptive behavior, including the contingent use of alternative communication strategies, alternative message forms, and alternative media</td><td>Interactive and parallel</td><td>Authors and reviewers can adjust the contextual information needed to understand reviews and articles by asking and responding to more (or less) questions, or by ignoring irrelevant questions and responses. The “preliminary decision” process encourages adaptive behavior by allowing reviewers to change their decision based on additional information. The forum also makes it easy to manage and sustain multiple parallel conversations</td></tr><tr><td>Design should monitor complexity and alert communicators to a high propensity of communication breakdowns</td><td>Editable structure</td><td>Discussion forums allow administrators (editors) to remove irrelevant posts and reorganize the posts so that they make more sense. Editors can easily see a communication breakdown by monitoring number of posts and responses and intervene if necessary. We added the artificial constraint of an “open time window for comments” to further limit complexity (see more below)</td></tr><tr><td>Design should support multiple levels of communication and easy travel between levels</td><td>Hierarchical</td><td>Topics (papers) and responses (reviews and questions) are organized around a hierarchical “threaded” structure that makes it easy to navigate between main content (the paper and reviews) and contextual information. A follow-up comment is automatically and visually tied to the original comment</td></tr><tr><td>Organizational memory should consist of speech act components, situations, norms, and values</td><td>Stored</td><td>All comments remain on the discussion forum so that authors and reviewers and editors can later refer to previous comments</td></tr><tr><td>Organizational memory should consist of associative information, accessible through multiple media, and represented in multiple forms, allowing for indeterminate and emergent views as well</td><td>Citation</td><td>The ability to cite conversations and postings from different threads can lead to new and emergent discussions (e.g., a reviewer may cross cite a posting by another reviewer)</td></tr></table>

## 3.2.2. Prototype implementation

To implement the structured communication process into a system, we created a secure web site following the discussion forum metaphor (see Fig. 2). The web site was created using Microsoft FrontPage and consisted of a series of Active Server Pages (ASP). The prototype went through several iterations to improve usability and performance for application in a live setting. One of the authors was the principal designer; while the editors involved in the exploratory study (see below) acted as testers.

The prototype implements the proposed structured communication process by (a) changes to the basic review process (e.g., the “open time window”) and (b) the discussion forum design artifact. The prototype provides a common space, supports interactive and parallel conversations, affords a hierarchical (and editable) visual structure, and allows cross referencing through citations and by storing all the conversations (see Table 1). We were unable to implement all the Te'eni (2006) guidelines. For example, the hierarchical structure of a discussion forum can also reduce adaptive behavior since there is only one way to see and use the forum, there are no automatic tools to provide communication breakdown alerts, and our implementation did not distinguish between different forms of communicative acts.

## 4. Part B — natural science

## 4.1. Evaluating the new peer review process

In this section, we propose a set of propositions to understand and evaluate the impact of the proposed peer review process improvements. Novel “system building” research projects often evaluate well-known concepts such as ease of use and satisfaction. These concepts, though important, do not fully explain the underlying reasons why a proposed system is used or not used. Understanding this is critical when the proposed system is exploratory, can be modi<sup>fi</sup>ed relatively easily, and the resulting usage patterns and behaviors are not fully understood. We developed the prototype in an iterative manner using real-world constraints while available theory and previous research provided guidance for the design choices. In other words, the “natural science” aspect reported in this section was developed in parallel with the “design science” aspect, and in an iterative manner. We found the following three perspectives to be useful in thinking about peer review.

## 4.1.1. The rational actor perspective

Frost and Taylor [10] provide an in-depth analysis of the peer review process from the editor's perspective. They suggest that the decision to accept or reject a manuscript may in the end be largely organizational and based on how well standard operating procedures, policies, and issues such as space, turnaround time, quality, number of submissions, and others are managed. Another aspect of the review process is the overall convenience of the process. These are largely independent concepts. For example, a process could honor deadlines and commitments but still seem inconvenient to authors and reviewers. Alternatively, the process could seem very convenient to authors and reviewers in terms of submission but suffer from poor management once the paper has been submitted. Any reasonably well-implemented IT based peer review process should improve management and convenience (e.g., it is easier to upload a <sup>fi</sup>le then to print out and mail it, and it is easier to collate reviews electronically than on disparate pieces of paper). This is a basic “automational” power of IT. This leads to our <sup>fi</sup>rst set of propositions:

![](/api/attachments/S5HJKAQR/fulltext/images/5f6509bbf01208e198b53cedc10d9b3ce026f39e33d646894a5758e51bf0f39e.jpg)  
Fig. 2. Prototype refereeing system

P1a: The structured communication process will improve the perception of how well the peer review process is managed as compared to the traditional reviewing process.

P1b: The structured communication process will improve perceptions about the convenience of the peer review process as compared to the traditional reviewing process.

In a study of how the Academy of Management Journal accepts and rejects articles, Beyer et al. [3] found that gate keeping – the use of normative rationalistic rules such as originality, clarity, sophisticated statistics and extensive documentation. In another study, Gilliland and Cortina [12] analyzed the underlying reasons for low inter-rater reliability of reviewers and found that reviewers agree on the basic criteria but apply them differently. The results of Beyer et al. [3] and Gilliland and Cortina [12] suggest that basic understandability (or lack) of a manuscript or of the review of the manuscript can also impact perceptions of the peer review process and the resulting decision.

In the proposed IT-enabled process, authors can easily obtain submission guidelines and other instructions. Reviewers can search and annotate articles. In addition, reviewers and authors can interact directly with each other. Other review reports are available to provide examples and provide insight for additional analysis and questioning. In summary, all of these opportunities to improve understanding suggest that:

P2: The structured communication process will improve perceptions about the understandability of articles, reviews, and reviewing process as compared to the traditional reviewing process.

## 4.1.2. Justice and fairness

Pfeffer et al. [26] analyzed the decision-making aspect of the peer review process and compared universalistic criteria – consistent, organizationally held norms (such as merit), with particularistic criteria – individually held criteria (such as race or social connections). Decisionmaking follows universalistic standards when the standards are established and well-understood. Less developed disciplines will face more uncertainty with regards to universally held criteria and may default to particularism, which can impact perceptions of fairness. They found that particularism was more evident in the social sciences than natural sciences. Beyer et al. [3] also argue that “low-level” paradigm <sup>fi</sup>elds such as management will lead to higher particularistic decisions because these <sup>fi</sup>elds have no universally held criteria.

Gilliland and Beckstein [11] apply “organizational justice theory” to peer review and distinguish between the perceived justice of decision outcomes – termed “distributive justice” – from the justice of the decision processes – termed “procedural justice.” They argue that the peer review process is similar to organizational decisions such as performance appraisal and personnel selection, and can be seen as an assessment of the author's research performance. Speci<sup>fi</sup>cally, the process of editorial decision making can be assessed in terms of perceptions of procedural justice, while perceptions about the fairness or justice of the actual outcome (acceptance or rejection) can be assessed in terms of distributive justice. In their study, they found that concepts of justice and fairness were important in predicting reactions and author intentions to submit further work to the journal. Procedural justice was operationalized as (a) external consistency (how authors are treated as compared with other authors) and internal consistency (how the different reviews impact the decision to accept or reject), (b) perceptions of whether reviewers avoid personal bias in their decisions, (c) the timeliness of the feedback, (d) the explanation or justi<sup>fi</sup>cation provided for the decisions, and (e) the sensitivity with which the decision is conveyed to the authors.

To evaluate the impact of our proposed improvements on the notion of “fairness” in the peer review process we must consider the perspectives of the authors, reviewers, and editors. For example, authors are likely to care about consistency (point (a) above) between a decision and the reviews, while reviewers are likely to be more concerned about being consistent with other reviewers regardless of the outcome. Therefore, we propose that the fairness of the review process is characterized by several factors, including impartiality (consistency and bias avoidance) and accountability (tone and conduct of the process). Authors, reviewers, and editors are typically all interested in the overall fairness of the peer review process regardless of the speci<sup>fi</sup>c reasons behind perceptions of fairness.

The structured IT-enabled peer review process is transparent — authors know that all reviews are “public” and that they can be seen by the other stakeholders. In addition, there is open interaction between reviewers and authors through the discussion forum. Authors (and reviewers) also know that they can question the initial reviews and provide additional information to support their position. Reviewers can also see the other reviews on the discussion forum. Therefore, we propose that:

## P3: The structured communication process will improve perceptions of fairness as compared to the traditional reviewing process.

Timeliness (point (c) above) encompasses a variety of process-related characteristics, including the speed of the submission process, the time a manuscript spends in review, responsiveness to questions about the process, and the timeliness of subsequent publication. We believe that these dimensions are implied by the more general concepts of management and convenience (as described in the previous section). Similarly, the concept of “explanation and justi<sup>fi</sup>cation” (point (d) above) was folded into the more general concept of understandability (also described in the previous section), which includes the explanation or understandability of the submission guidelines, the submitted manuscript, reviews, and publication guidelines.

## 4.1.3. Knowledge production

Laband [18] takes an economic perspective, characterizing scholarship and peer review as a knowledge production function with key inputs from authors, editors, and reviewers. He examined editorial correspondence and measured article and review quality by looking at items such as review length, citations, and time taken to revise. The basic thesis of the research was that reviewers and editors not only screen articles but also add value in the knowledge production process. Laband found that although editors' comments did not signi<sup>fi</sup>cantly increase manuscript quality, reviewer feedback does seem to add value by contributing to knowledge production (in addition to their role as screeners). Laband's work suggests that the concept of value may also impact perceptions about the peer review process. A process that provides detailed reviews that reveal new directions and insights may not only be perceived as fair and well-managed, but will also be perceived as adding value to the process overall. Conversely, it seems feasible that even if a process is perceived as being unfair and badly managed, authors could still see it as valuable if the reviews were useful and the process, however poor, resulted in new insights.

Laband's perspective also makes it clear that adding value (e.g., useful comments from the reviewers) has a cost in terms of effort. This is an important consideration given that most peer review processes are based on the volunteer model. Therefore, value is operationalized by both perceptions about the insights gained and also by the amount of effort required to provide and receive that insight. For authors, this would mean an assessment of the reviews and the effort required to understand and receive them. For reviewers, it is an assessment of the value the insight and knowledge gained by reading the manuscript, and of the value of being involved in the review process.

In the structured IT-enabled peer review process, authors have the opportunity to gain direct feedback and clari<sup>fi</sup>cations from reviewers through the discussion forum. Reviewers can see other reviews and also question authors about topics of interest or to clarify points through the discussion forum. These opportunities for interaction may yield more accurate and substantive reviews and reduce the effort required to produce quality reviews. This leads to the following proposition:

## P4: The structured communication process will improve perceptions about value as compared to the traditional reviewing process.

Laband's research and others (e.g., [6]) also focus on quality of the article as an important end function of the peer review process. There are several aspects of “quality” in this context – the submitted manuscript, the peer review process, and the <sup>fi</sup>nal manuscript. Direct perceptions about the quality of the peer review process itself are likely to be accounted for through other factors: fairness, understanding, value, and management. However, perceptions about whether changes to the peer review process improved the actual quality of an article are important in evaluating the proposed improvements. Finally, consistent with other IT enabled process improvement research, it would be important to understand the level of overall satisfaction with the process. Positive perceptions about fairness, understanding, value, and management should result in higher overall satisfaction. To summarize:

P5: The structured communication process will improve perceptions about the peer review process in terms of its impact on the quality of the article when compared to the traditional reviewing process.

P6: The structured communication process will improve perceptions about overall satisfaction as compared to the traditional reviewing process.

Together, our seven propositions represent a simplistic additive behavioral model of the peer review process. In reality, the relationships among the constructs may be more complex. Further, the outcome of the editorial decision may in<sup>fl</sup>uence the perceptions of the process itself (authors may be more likely to see a process as fair when the result is in their favor, regardless of the process details). Given the exploratory nature of this work, we decided to stay with a simple and parsimonious set of propositions. Empirical testing and application will hopefully, over time, build a more sophisticated behavioral picture of the peer review process.

## 4.2. Exploratory study

An exploratory study was conducted to evaluate the proposed structured communication process. Two mini-tracks at the Association of Information Systems (AIS) annual Americas conference participated in the study. There were a total of 28 submissions, 47 authors, 25 reviewers, and <sup>fi</sup>ve editors. One of the authors was co-cha for both tracks and acted as the “managing editor.” All submissions were sent by electronic mail to the managing editor. The authors and reviewers were then sent an explanation of the refereeing process. All reviews were posted to the prototype system to which each reviewer and author had secure but anonymous access (see Fig. 2). The peer review process was divided into two stages. Each reviewer was initially asked for a “preliminary decision” on the article and encouraged to ask speci<sup>fi</sup>c questions. The review site was then made available to reviewers and authors for discussion and comment during the one-week time window. All identi<sup>fi</sup>cation information was removed and the process was double-blind. After the open time period the site was restricted to reviewers, who were asked to look at all the comments and reviews and make a <sup>fi</sup>nal decision. The site was then restricted to the track chairs, who analyzed all the comments and made <sup>fi</sup>nal decisions for each article. A web-based questionnaire consistent with our propositions was administered to all participants. To gain comparative data, each participant was asked to rate their experience with the prototype system and with their most recent experience with the traditional refereeing process (excluding outlets that had a web-based reviewing system) on the dimensions of understandability, convenience, management, fairness, and value. Each dimension was comprised of two or three survey items accompanied by a brief, speci<sup>fi</sup>c description of what should be evaluated (for example, “Responsiveness,” an aspect of the Management dimension, was described as “kept informed of status, quick acknowledgement”). Respondents were asked to rate each item from 1 (“Excellent”) to 5 (“Very Poor”). We also asked participants several open-ended questions about the future impact of the structured communication process.

The study had a total of 36 sample points consisting of 22 authors and 19 reviewers (note: some authors were also reviewers). Participation levels among respondents varied. While one respondent frequented the review site once a day, 63% of the respondents visited the site once a week. On average, participants read four abstracts or papers (excluding their own) and eight additional reviews (excluding their own). Table 2 shows the descriptive statistics for authors and Table 3 for reviewers.

## 5. Discussion

The results of the exploratory study are encouraging with respect to our basic thesis that adding IT-enabled structured communication can provide bene<sup>fi</sup>ts. The prototype system was rated more positively by authors on at least one aspect of understandability, convenience, management, fairness, and value. For reviewers, the perceived improvements were not as strong – only one measure of management (responsiveness) and one measure of fairness (impartiality) was rated more highly for the prototype system. The remainder of this section discusses the results across the <sup>fi</sup>ve dimensions measured in this study in greater detail.

Table 2 Author ratings

<table><tr><td>Concept and Items</td><td>Mean (sd) traditional system</td><td>Mean (sd) structured communication system</td></tr><tr><td colspan="3">Understandability</td></tr><tr><td>Understandability of submission guidelines</td><td>1.83 (0.71)</td><td>1.77 (0.75)</td></tr><tr><td>Understandability of reviews</td><td>2.67 (0.84)</td><td>2.05 (0.80)</td></tr><tr><td>Understandability of the publication guidelines</td><td>2.06 (0.44)</td><td>2.00 (0.55)</td></tr><tr><td colspan="3">Convenience</td></tr><tr><td>Convenience of submission and review process</td><td>1.83 (0.71)</td><td>1.41 (0.59)</td></tr><tr><td>Convenience of the publication process</td><td>2.67 (0.84)</td><td>1.95 (0.97)</td></tr><tr><td colspan="3">Management</td></tr><tr><td>Timeliness of the submission and review process</td><td>2.61 (1.14)</td><td>1.36 (0.49)</td></tr><tr><td>Timeliness of the publication process</td><td>2.27 (1.03)</td><td>1.62 (0.74)</td></tr><tr><td>Responsiveness</td><td>2.67 (1.14)</td><td>1.50 (0.80)</td></tr><tr><td colspan="3">Fairness</td></tr><tr><td>Impartiality</td><td>2.18 (0.88)</td><td>1.91 (0.68)</td></tr><tr><td>Accountability</td><td>2.77 (1.01)</td><td>1.71 (0.78)</td></tr><tr><td colspan="3">Value</td></tr><tr><td>Feedback</td><td>2.81 (1.05)</td><td>2.09 (0.68)</td></tr><tr><td>Amount of effort required</td><td>2.14 (0.53)</td><td>2.35 (0.74)</td></tr></table>

Scale: 1 = “Excellent”, 5 = “Very Poor.

Table 3 Reviewer ratings

<table><tr><td>Concept and Items</td><td>Mean (sd) traditional system</td><td>Mean (sd) structured communication system</td></tr><tr><td colspan="3">Understandability</td></tr><tr><td>Understandability of submission guidelines</td><td>2.46 (0.97)</td><td>1.92 (0.64)</td></tr><tr><td>Understandability of the publication guidelines</td><td>2.00 (0.91)</td><td>2.23 (0.72)</td></tr><tr><td colspan="3">Convenience</td></tr><tr><td>Convenience of submission and review process</td><td>2.00 (0.95)</td><td>1.62 (0.77)</td></tr><tr><td colspan="3">Management</td></tr><tr><td>Timeliness of the submission and review process</td><td>1.92 (0.86)</td><td>1.54 (0.52)</td></tr><tr><td>Responsiveness</td><td>2.54 (1.39)</td><td>1.69 (0.63)</td></tr><tr><td colspan="3">Fairness</td></tr><tr><td>Impartiality</td><td>2.17 (0.83)</td><td>1.83 (0.72)</td></tr><tr><td>Accountability</td><td>2.17 (1.03)</td><td>1.92 (0.49)</td></tr><tr><td colspan="3">Value</td></tr><tr><td>Feedback</td><td>2.46 (0.97)</td><td>2.23 (0.60)</td></tr><tr><td>Amount of effort required</td><td>2.08 (0.69)</td><td>2.00 (0.82)</td></tr></table>

Scale: 1 = “Excellent”, 5 = “Very Poor.

## 5.1. Understandability

The prototype system does not appear to improve the understandability of the guidelines of the review process, but it does seem to improve the understandability of the reviews for authors. This is plausible given that while the process of understanding reviews leverages the interactive nature of the prototype system, communicating guidelines is essentially oneway communication from editor to author. In their open-ended comments regarding understandability, participants remarked:

• It may help clarify misunderstandings, give the author a chance to explain his side of the story, and get follow-up help from the reviewer (e.g., speci<sup>fi</sup>c references).

• It allows the quick resolution of misconceptions & misunderstandings

• Major points can be clarified.

• My concern is that people will get busy and not fulfill the goal of increasing interaction

The results above suggest that the structured communication process (supported by the common space, interactive, parallel, hierarchical, stored, and citation design attributes of the discussion forum) can increase interactivity, leading to increased understanding. Yet, this innovation will only work if the authors and reviewers cooperate. One reviewer remarked:

The lack of a response to my response made me decide not to give authors the bene<sup>fi</sup>t of the doubt. So instead of recommending accept with revision, I felt more con<sup>fi</sup>dent about recommending reject.

## 5.2. Convenience

The authors also rated the prototype system as more convenient than the traditional peer-review system, but reviewers did not. This may re<sup>fl</sup>ect the authors' greater investment in the process and their positive response to the availability of more information regarding their submission (and the relative ease of navigation afforded by the hierarchical design attribute of a discussion forum). For reviewers, they are required to provide a greater level of information than they would under the traditional model of peer review. This may mitigate their positive perceptions of the process. In fact, one may <sup>fi</sup>nd it surprising that reviewers did not rate the prototype system lower with regard to convenience given the “unpolished” interface of our prototype system (for example, the system lacked online help and error recovery). We believe the strength of the new review process resulted in the system being rated relatively highly.

It is reasonable to assume future peer review systems will be better-designed and include convenience features that users expect (e.g., automatic password reset and an improved user interface). These improved systems should result in even higher convenience ratings by authors and at least no less convenient by reviewers. However, it would be unwise to assume that better technology will necessarily lead to better results. One participant remarked:

Should also provide paper copies and a way to get feedback in other than web-based because it was inconvenient to have to be tied to my terminal while working on this….

## 5.3. Management

Authors also rated the prototype system higher than the traditional peer review model with regard to management. Speci<sup>fi</sup>cally, authors rated the timeliness of the submission, review, and publication process more highly. Again, this may re<sup>fl</sup>ect authors' higher level of investment in the process – the authors spend most of their time waiting during the peer review process, and therefore are more likely to notice improvement. Both authors and reviewers rated responsiveness (a measure of management) more highly for the prototype system.

## 5.4. Fairness

Impartiality (an aspect of fairness) was rated more highly by both authors and reviewers. Authors (but not reviewers) also rated the prototype system highly with regard to accountability. Perhaps this is the most valuable aspect of IT enablement – authors and reviewers believe the structured communication offered by the system helps arrive at a “fair” assessment of the submission (supported by the common space, stored, and citation design attributes of the discussion forum). However, accountability is already inherent in many review processes and is not aided as clearly by the technology.

We also asked participants an open-ended question about why they looked at reviews other than their own to gain further insight into the fairness concept. One participant commented that they looked at other reviews “To <sup>fi</sup>nd out about other possible papers …, and also to <sup>fi</sup>nd out more about the refereeing process as it applied to other papers.” Another participant more directly stated: “To compare assessments.” These comments do suggest that at least some participants will actively assess the fairness of the process if given the opportunity to do so.

## 5.5. Value

Authors also rated value more highly for the proposed peer review process, while reviewers did not. Speci<sup>fi</sup>cally, authors rated feedback highly, once again re<sup>fl</sup>ecting the greater investment authors have in receiving quality feedback regarding their work. There does not seem to be much difference with regard to effort for either authors or reviewers. This indicates a potential downside of structured communication – in order to provide a richer experience, more work is required on the part of the authors and reviewers. The open-ended question regarding why participants looked at other papers and reviews also provided additional interesting insights. Curiosity was a common reason, however, the respondents also remarked:

• Titles seemed interesting and related to my current research interests

• Skimmed through to find those of interest.

• get a sense of how to target the presentation

• Curious about seeing what other reviewers comments looked like.

• I was looking to see how others viewed papers which I had commented on. Mostly to see if I was off-base.

• I enjoyed being able to read other people's entries and the associated comments. I wanted to af<sup>fi</sup>liate with the other submissions.

• I read them to verify my perceptions. I can be in error. If I <sup>fi</sup>nd a mismatch between my perception and the comments of others I may go back and reread which may or may not cause a change in my position on the review.

These comments suggest that there are more dimensions of value and perceptions about increasing the overall quality of scholarship than we had originally conceptualized. Speci<sup>fi</sup>cally, the participants seem willing and interested in learning from the experience and adjusting their work accordingly. We suggest incorporating the concept of learning in the practice of reviewing and in future studies. Perhaps the greatest potential bene<sup>fi</sup>t of incorporating structured communication into the review process is that can become less of a control mechanism and more of a learning tool. Note that this particular insight follows directly from our combined design and natural science approach. The importance of learning would have been less obvious in the absence of a real design artifact to which users could react, and it might have become confounded with other issues if we had not delineated a baseline set of behavioral concepts.

In contrast with the above, when commenting on the impact of the new process in increasing the quality of scholarship, one respondent said that the changes were positive in terms of the “ability to react to comments (can lead to dialog about issues/questions). However, the effort is possibly increased?” One way to understand the lack of positive ratings for the reviewer group is that the bene<sup>fi</sup>t of increased learning and increased accuracy for reviewers may not be signi<sup>fi</sup>cant enough to offset the time cost.

## 5.6. Limitations

There are several limitations in our study. First, the objectives and motivations of the various stakeholders will likely vary with the type of outlet. The difference in ratings might have been greater if this system was used for a journal's review process rather than a conference. Second, the study is exploratory and should be followed up with a more rigorous experiment. The prototype also had several technical limitations; for example, the web-based user interface could be improved. However, as outlined below, the overall research did yield new and interesting insights.

## 6. Implications for future research and design

## 6.1. Improving the peer review process with IT

A discussion forum is an effective design artifact for promoting mutual understanding among authors and reviewers, resulting in a better evaluation of scholarly work. However, our results suggest that discussion forums cannot by themselves increase interaction and they do not support other process improvements that are likely needed to increase interaction such as reminders or ratings. Future design research should consider combining a discussion forum with a “document work<sup>fl</sup>ow” concept that visually depicts the <sup>fl</sup>ow of documents through the peer review process and provides embedded discussion forums as needed. The speci<sup>fi</sup>c attributes of this combined discussion forum and work<sup>fl</sup>ow design artifact could include.

• Automatic notification of new responses so the participants do not have to continually login and check for a response.

• Providing automatic updates to authors, reviewers, and editors when milestone events occur such as the assignment of an editor, assignment of reviewers, and the submission of a review.

• Setting expectations up front about the level of interactivity required from authors and reviewers.

• Educating the participants on the benefits of the structured communication approach. It is unclear if all the reviewers completely understood the potential bene<sup>fi</sup>ts of the approach.

• Allowing authors and editors to rate reviews and making the results public.

The Te'eni [30] design guidelines were very useful in thinking about improving goal oriented communication. However, the guidelines are dif<sup>fi</sup>cult to apply uniformly and consistently. Even though comprehensive application is not the authors stated intention, the lack of constraints can cause pitfalls. For example, one guideline recommends providing alternate communication strategies whereas another guideline advocates enhancing mutual understanding. Applied blindly, these two suggestions could lead to contradictory outcomes. Too many different communication strategies could end up inhibiting the achievement of mutual understanding! We found that the constraints and affordances of speci<sup>fi</sup>c design metaphors such as “discussion forum” or “document work<sup>fl</sup>ow” were helpful in thinking about how to apply IT to peer review. Future design science researchers may want to consider going beyond design propositions (or guidelines) and suggesting speci<sup>fi</sup>c design metaphors. These metaphors serve to bind the guidelines together and bring inherent constraints and affordances.

## 6.2. Increasing our understanding of peer review

The results indicate that the peer review process for authors can be improved comprehensively with IT. However, reviewers are skeptical of changes that will further increase their workload even though they tend to believe that the structured communication process can increase quality and perceptions of fairness. The concept of value holds the most promise for increasing our understanding of how reviewers approach peer review. Future studies need to measure value more precisely and include learning as a concept (as discussed previously). However, even with the limited understanding of value as provided by this study it is clear that approaches that increase the burden on reviewers, such as “developmental reviewing,” will only be embraced by the most diligent and are unlikely to succeed in the long run. We also suspect radical ideas are needed that go beyond traditional thinking. As Watson [32] suggested we need “gamma change” ideas such as his notion of formal certi<sup>fi</sup>cation for reviewers, a “scrip” system in which reviewers are obligated to review a certain number of articles in return for each submission, or even paying reviewers.

## 7. Conclusions

This paper analyzes the basic processes of peer review and proposed changes to the review process using an IT enabled structured communication approach. We investigated the problem from both a design science perspective through the development of a prototype system, and a natural science perspective by integrating previous literature into behavioral propositions that guided the evaluation of the prototype. An exploratory study provided further insights on the prototype system and on the underlying design and behaviors. This paper contributes to the literature at three different levels:

• From the design science perspective we prototype and demonstrate how structured communication can improve the peer review process by employing artifacts that increase mutual understanding. An evaluation of the prototype suggests that future design research should consider integrating the design concepts of “discussion forums” and “work<sup>fl</sup>ow” to peer review. Newer design concepts also need to consider reviewer motivation and look for new and easier ways to engage reviewers. We believe our work is one of the <sup>fi</sup>rst to consider and demonstrate how changing the process of review can lead to improvements.

• From the natural science perspective, we show how the theoretical perspectives of procedural justice, the rational actor, and economic value are important to understand peer review. These perspectives can also be applied to other forms of peer review such as product reviews on the web or audits of accounting practices. Procedural justice speaks to concerns of fairness that will likely always exist in any process that involves evaluation of one group by another. The rational actor perspective provides insights into the administrative aspects of any kind of review, and the economic perspective provides insights on why people choose certain behaviors. The combination of these perspectives into propositions is the <sup>fi</sup>rst step toward developing a comprehensive behavioral theory of peer review. The evaluation of the prototype provided additional insights including expanding the conception of value, adding learning as a concept, and suggesting re<sup>fi</sup>nements to the initial set of concepts.

• This paper also contributes to implementing and refining design science methodology. In line with suggestions from the literature [5,15,31] we extend the application of the design science perspective by combining it with the natural science perspective. Rather than settle for traditional benchmark style measures such as ease of use or performance, we developed behavioral theoretical propositions in conjunction with prototype development. The process of developing the prototype and in parallel, considering evaluation measures and theoretical approaches allowed us to converge on what we believe are key design artifacts (e.g., structured communication, work<sup>fl</sup>ow) and behaviors (e.g., fairness, value, learning) that might have been ignored by traditional approaches. The propositions provide a substantive basis for evaluating current and future systems, and a speci<sup>fi</sup>c direction for future research. To summarize, the combined approach is powerful because it generates new insights and lends more credibility to the results by anchoring design to behavioral issues of truth and relevance and anchoring behaviors to design issues of utility and feasibility.

The structured communication process proposed in this paper is relatively easy to implement, and we encourage editors of conferences and journals to continue the process of experimentation. Moreover, given that review is, at its core, a process, we believe that future IS research can continue to add signi<sup>fi</sup>cant value to this very important aspect of academic scholarship as it is increasingly applied to other domains.

## Acknowledgements

Thanks to Rick Watson, Simha Magal, and Blake Ives who were the co-mini track editors of the conference in which we tried out the peer review process. Thanks also to Lorne Olfman, Rick Watson, Blake Ives who reviewed previous drafts of this paper. Michael Carey, Zaheeruddin Asif, Cindy Marselis, Don Canuso, Laurel Miller, Deepika Gandhi, and Guoliang Hong also worked on the Temple Peer Review Manager system.

## References

[1] K.R. Apt, One more revolution to make: free scienti<sup>fi</sup>c publishing, Communications of the ACM 44 (5) (2001) 25–28.

[2] A.G. Bedeian, Peer Review and the Social Construction of Knowledge in the Management Discipline, Academy of Management Learning & Education 3(2) 198-216.

[3] J.M. Beyer, R.G. Chanove, W.B. Fox, The review process and the fates of manuscripts submitted to AMJ, Academy of Management Journal 38 (5) (1995)1219-1261

[4] R. Brown, The use of double anonymity in peer review: a decision whose time has come? Quality Assurance 11 (2-4) (2005) 103–109.

[5] J. Cao, J.M. Crews, M. Lin, A. Deokar, J.K. Burgoon, J.F. Nunamaker, Interactions between system evaluation and theory testing: a demonstration of the power of a multifaceted approach to information systems research, Journal of Management Information Systems 22 (4) (2006) 207-235.

[6] H.H. Clark, S.E. Brennan, Grounding in communication, in: L.B. Resnick, J. Levine, S.D. Teasley (Eds.), Perspectives on Socially Shared Cognition, American Psychological Association, Washington, DC, 1991, pp. 127–149

[7] L.L. Cummings, P.J. Frost (Eds.), Publishing in the Organizational Sciences, 2nd Edition, Sage Publications, Thousand Oaks, California, 1995.

[8] T.H. Davenport, J.E. Short, The new industrial engineering: Information technology and business process redesign, Sloan Management Review 31 (4) (1990) 11–27.

[9] P.V. Dressendorfer, Transition to Web-based peer review process for th transactions on nuclear science, IEEE Transactions on Nuclear Science 5 (1) (2004) 233.

[10] P.J. Frost, R.N. Taylor, Partisan Perspective: a multiple-level interpretation of the manuscript review process in social science journals, in: L.L. Cummings, P.J. Frost (Eds.), Publishing in the Organizational Sciences, 2nd Edition, Sage Publications, Thousand Oaks, California, 1995, pp. 13–43.

[11] S. Gilliland, B. Beckstein, Procedural and distributive justice in the editorial review process, Personnel Psychology 49 (3) (1996) 669–691.

[12] S. Gilliland, J. Cortina, Reviewer and editor decision making in the journal review process, Personnel Psychology 50 (1997) 427–452.

[13] J. Habermas, Moral Consciousness and Communicative Action (C. Lenhardt and S. W. Nicholsen, Trans.), MIT Press, Cambridge, Massachusetts, 1990.

[14] S. Harnad, M. Hemus, All-or-none: no stable hybrid or half-wa solutions for launching the learned periodical literature into the post Gutenberg galaxy, in: I. Butterworth (Ed.), The Impact of Electronic Publishing on the Academic Community, Portland Press, London, 1997, pp. 18–27.

[15] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004) 77–105.

[16] E.T. Horrobin, Peer review: a philosophically faulty concept which is proving disastrous for science, in: S. Harnad (Ed.), Peer commentary on peer review: A case study in scienti<sup>fi</sup>c control, Cambridge Universit Press, Cambridge, United Kingdom, 1982, pp. 33–34.

[17] R. Kraut, J. Galegher, C. Egido, Relationships and tasks in scienti<sup>fi</sup>c research collaborations, in: I. Greif (Ed.), Computer Supported Cooperative Work: A Book of Readings, Morgan Kauffman, California, 1988, pp. 741–769.

[18] D.N. Laband, Is there value-added from the review in economics? Preliminary evidence from authors, The Quarterly Journal of Economics 105 (2) (1990) 341–352.

[19] A. Lee, Editor's comments, Management Information Systems Quarterl 23 (4) (1999) lv–lx.

[20] S.T. March, G. Smith, Design and natural science research on information technology, Decision Support Systems 15 (4) (1995) 251–266.

[21] R. McCarty, Science, politics, and peer review, American Psychologist 57 (3) (2002) 198.

[22] S. Minton, M.P. Wellman, JAIR at <sup>fi</sup>ve, AI Magazine 20 (2) (1999) 83–91.

[23] W.R. Nord, Looking at ourselves as we look at others: an exploration of the publication system for organizational research, in: L.L. Cummings, P.J. Frost (Eds.), Publishing in the Organizational Sciences, 2nd Edition, Sage Publications, Thousand Oaks, California, 1995, pp. 64–78.

[24] J. Nunamaker, M. Chen, T.D.M. Purdin, Systems Development in information systems research, Journal of Management Information Systems 7 (3) (1991) 89–106.

[25] D. Patton, S. Olin, Scienti<sup>fi</sup>c peer review to inform regulatory decision making: leadership responsibilities and cautions, Risk Analysis 26 (1) (2006) 5–16.

[26] J. Pfeffer, A. Leong, K. Strehl, Paradigm development and particularism: journal publication in three scienti<sup>fi</sup>c disciplines, Social Forces 55 (4) (1977) 938–951.

[27] C. Saunders, From the trenches: thoughts on developmental reviewing, MIS Quarterly 29 (2) (2005) iii–xii.

[28] A. Schaffner, The future of scienti<sup>fi</sup>c journals: lessons from the past, Information Technology and Libraries 13 (4) (1994) 239–248

[29] A. Snyder, Increasing transparency in peer review: members speak out, Journal of Accountancy 198 (6) (2004) 22–23.

[30] D. Te'eni, The language-action perspective as a basis for communication support systems, Communications of the ACM 49(5) 65-70.

[31] J. Walls, G. Widmeyer, O. El Sawy, Building an information system design theory for vigilant EIS, Information Systems Research 3 (1) (1992) 36–59.

[32] R. Watson, The academic publication systems: A time for redesign, University of Georgia, Working Paper, 2006

[33] R. Weber, The journal review process: a manifesto for change, Communications of the Association for Information Systems 2(12)2-22.

[34] R. Weber, Retrospection: the MIS quarterly's review processes: 1995– 2001, MIS Quarterly 26 (2) (2002) v–xi

[35] R. Yalow, Competency testing for reviewers and editors, in: S. Harnad (Ed.), Peer commentary on peer review: A case study in scienti<sup>fi</sup>c control, Cambridge University Press, Cambridge, United Kingdom, 1982 pp. 60–61.

Munir Mandviwalla, Associate Professor, founding chair of the Management Information Systems department, and Executive Director, Irwin L. Gross Institute for Business and Information Technology, Fox School of Business Temple University holds a BSc in Systems Engineering from Boston University, an MBA from the Peter F. Drucker School of Management at Claremont Graduate University, and a Ph.D. in Management Information Systems from the Programs in Information Science at Claremont Graduate University. His current research interests include communication technologies, globalization, and the use of prototyping for theory development. His publications have appeared in Management Information Systems Quarterly, ACM Transactions on Computer Human Interaction, Journal of Organizational Computing and Electronic Commerce, Decision Support Systems, Small Group Research, Communications of the Association for Information Systems, and Information Systems Journal.

Ravi Patnayakuni is an Associate Professor of information systems in the Department of Economics and Management Information Systems at the University of Alabama in Huntsville. His research focuses on, digital supply chains, IT business value, IT implementation, systems development and knowledge management. Ravi received his D.B.A from Southern Illinois University at Carbondale and has held positions at Temple University and The University of Melbourne, Australia prior to his current appointment. His research has been published in Journal of Management Information Systems, MIS Quarterly, Communications of the ACM, Omega, Communications of th AIS, and Information Systems Journal.

David Schuff is Assistant Professor of Management Information Systems in the Fox School of Business and Management at Temple University. He holds a BA in Economics from the University of Pittsburgh, an MBA from Villanova University, an MS in Information Management from Arizona State University, and a Ph.D. in Business Administration from Arizona State University. His research interests include the strategic use of information systems, the assessment of total cost of ownership in large networked organizations, and data warehousing. His work has been published in journals such as Decision Support Systems, Information & Management, Communications of the ACM, and Information Systems Journal.
