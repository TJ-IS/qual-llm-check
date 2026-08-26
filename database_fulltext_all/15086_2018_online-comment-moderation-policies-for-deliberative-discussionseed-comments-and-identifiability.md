---
otero_id: 15086
otero_key: "Q2Y43PAF"
title: "Online Comment Moderation Policies for Deliberative Discussion–Seed Comments and Identifiability"
authors: "Kil-Soo Suh; Seongwon Lee; Eung-Kyo Suh; Hojin Lee; Jaehoon Lee"
year: "2018"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00489"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
ISSN 1536-9323

# Online Comment Moderation Policies for Deliberative Discussion–Seed Comments and Identifiability

Kil-Soo Suh<sup>1</sup>, Seongwon Lee<sup>2</sup>, Eung-Kyo Suh<sup>3</sup>, Hoseong Lee<sup>4</sup>, Jaehoon Lee<sup>5</sup>

<sup>1</sup>Yonsei University, Korea, kssuh@yonsei.ac.kr

<sup>2</sup>Dankook University, Korea, seongwon.lee.16@gmail.com <sup>3</sup>Dankook University, Korea, eungkyosuh@dankook.ac.kr <sup>4</sup>Korea Land & Housing Corporation , Korea, hs\_lee0306@naver.com.kr <sup>5</sup>University of New South Wales, Australia, jaehoon.lee@unsw.edu.au

## Abstract

Due to the development of media information technologies and the proliferation of mobile devices, the Internet has rapidly moved to the center of news readership. In contrast to traditional media, Internet news is often coupled with commenting platforms that can accommodate readers’ immediate feedback to news stories. However, a side-effect of this feature—malicious comments—is becoming an increasingly serious social problem. To alleviate this problem and increase the likelihood of comments functioning as deliberative discussion, we suggest two moderation policies—a policy of providing high-quality seed comments and a policy of increased identifiability through social networking service accounts—and examine their effects through a longitudinal online experiment. We designed experimental groups according to a 2 x 2 between-subjects factorial design. For our experiment, a total of 137 subjects read news stories and commented on them over 15 days by using a mobile Android application developed specifically for the experiment. We found the following relationships. First, both seed quality and identifiability improve the quality of user comments in terms of deliberative discussion. Second, these effects are comparable in magnitude. Third, there are no significant interaction effects between seeds and identifiability. Fourth, the effects of high-quality seeds disappear early with anonymous users but persist when users are identified by social media accounts. Fifth, the negative effects of low-quality seeds are present and persistent only when combined with anonymity. Otherwise, the negative effects of low-quality seed comments are canceled out by the positive effects of identifiability. Finally, anonymous males are easily provoked to respond to low-quality seed comments, but most females do not respond to such comments even in anonymous situations.

Keywords: Comment, Deliberative Discussion, Seed, Identifiability

## 1 Introduction

The Internet has rapidly moved to the center of news readership, due to the development of media information technologies and the proliferation of mobile devices. In addition, as news consumption via mobile devices surpasses the amount of news consumed on desktops (Pew Research Center, 2013; 2015), receiving and reading news in real time is becoming a prominent feature of news consumption.

Unlike with traditional media such as radio, print, and TV, Internet news sites often provide commenting platforms that readers can use to immediately respond to news stories. By offering the capacity for readers to immediately share their thoughts and feelings about a news story, Internet news providers are encouraging a type of interactive communication not possible in offline settings. Through the information communication technology (ICT) of the comment system, readers and journalists have the capacity to interact in ways that were previously impossible (Reader, 2012). And because such comments fulfill a function that helps people assess public opinion on a specific issue, researchers have been closely examining them in terms of content analysis and have been focusing on comments in a Big Data sense (Hsu et al., 2009; Li et al., 2014). Of the Internet news users surveyed, 37% responded that a news comment service may be an important function, and 25% of these respondents replied that they have written a comment, which shows that they recognize the role of news comment services (Purcell et al., 2010; Diakopoulos & Naaman, 2011).

But comment services have also engendered what is becoming a serious social problem—malicious comments. These kinds of comments constitute a form of undesirable conduct by disseminating falsehoods or attacking specific individuals with swear words, slander, and/or sexually degrading comments (Lee, 2005; Jeong, 2010) that can damage social bonds, contribute to social unrest and divisiveness, and cause targets severe displeasure. Abuse, hateful speech, and trolls are as old as the early days of the Internet. What has changed is their intensity and prevalence as a result of more interactivity on the web and the introduction of social media (WAN-IFRA, 2016). Research by the Korea Internet and Security Agency (2011) found that more than a half of all Internet users have been the target of malicious comments, which demonstrates the seriousness of this problem. And the presumption that an increasing number of people are getting and sharing news and comments online (Pew Research Center, 2015) from either news sites or social media sites is coupled with the accompanying presumption that the harmful consequences of malicious comments could become even more serious.

Comments on news sites have apparently not yet become the problem they are reported to be for social media, but news organizations are nevertheless encountering difficulties. Dozens of news sites have responded over the past three years by shutting down their comment systems. Aware of the magnitude of the problem, many online news startups do not even concern themselves with the comment function because of the difficulties of dealing with the abuse that comes with it (WAN-IFRA, 2016).

However, most news organization surveyed value comments and want a solution other than just closing themselves off from readers. For them, the value of comments lies in “adding to the debate” (53%), “providing ideas and input for future stories” (53%) and “encouraging diversity of opinions” (47%) (WAN-IFRA, 2016). To mitigate the problems of comment systems while encouraging the positive aspects, many Internet news sites have implemented a variety of policies designed to moderate or control the comments made on their sites. Some approaches to the problem include advance automatic filtering of comments (such as comment filtering algorithms), or posting comments only after review (e.g., huffingtonpost.com), or a comment notification policy that relies on the collective intelligence of commenters to report inappropriate comments so they can be removed (e.g., news.naver.com). Hron and Friedrich (2003) state that comment moderation policies are an important element in raising the quality and usefulness of online comments, and Coleman and Gotze (2001) also emphasize that comment moderation is an essential element contributing to asynchronous dialogue.

This study focuses on the possibility that comment capabilities could offer a kind of “Public Sphere” (Habermas, 1996) where the various thoughts and feelings of commenters would constitute a network. According to deliberative democratic theory, deliberative discussion among citizens holding a variety of perspectives and knowledge is an important element of democracy (Chambers, 2003; Gastile, 2008). Although one person might not be able to make pertinent decisions, a group discussion between a cyberspace assembly of various individuals could lead to logical and reasonable decisions (Dutwin, 2002). Strandberg and Berg (2013) identify four requirements for deliberative discussion: rationality, topical relevance, reciprocity, and polite and respectful expression. Strandberg and Berg (2013) studied the similarities of online comments from the viewpoint of deliberative discussions and determined that they have the characteristics of a democratic discussion.

In this study, we propose and empirically evaluate two moderation policies that could help improve the quality of comments by focusing on news comments as deliberative discussion. Departing from the previously mentioned policies that, in effect, censor and manage comments, we suggest active moderation policies that encourage people to write deliberative comments and examine whether these moderation policies led to deliberative discussions. We propose a policy to moderate news comments by using constructive seed comments based on social contagion theory. This is the first study that applies social contagion theory to online news comments. In addition, we suggest a login policy that uses social networking service (SNS) accounts for identification. Prior research on anonymity effects has demonstrated that SNS accounts are more identifiable than pseudonyms. Considering the current popularity of SNS, research involving identifiability through SNS accounts is appropriate and timely. Such proactive moderation policies would allow ICT comments to serve their intended role and make the exchange of viewpoints and opinions on a specific topic work effectively.

## 2 Literature Review

## 2.1 Internet News Comments

The Internet has changed many aspects of our lifestyles, including news readership. Compared with traditional media, the Internet has several benefits, one of which is that online readers can participate in a debate and discussion through commenting on the news. Such commentary has become the norm in Internet news participation and a common form of online citizenship expression (Weber, 2013). Communication researchers discuss the possibility of promoting public discussions among news readers through comments. Such discussions are viewed as rising to the level of debates, in which participants are willing to revise their own opinions in light of exposure to those of others who are equally wellinformed but have different viewpoints, perspectives, and information (Chambers, 2003). Dutwin (2002) found that even when individual online comments appeared unlikely to rise to the level of deliberation, in their totality, these comments contained deliberative elements that were usually a product of the group discussion.

However, in examining readers’ entries on a Finnish newspaper website, Strandberg and Berg (2013) found comments that both promoted and hindered democratic expression. Low-quality comments generate social problems such as comment trolling and malicious comments that may be serious enough to provoke selfinjury and deepen social divisions (WAN-IFRA, 2016). Readers’ comments are of concern for newspaper editors, who must develop policies aimed at moderating such comments. Most Internet news sites have adopted a moderation policy that censors comments as a way of picking out the “bad apples” (WAN-IFRA, 2016).

Moderation in online forums serves three major functions: progress control for starting and ending a discussion, debate activation and enhancing the quality of a discussion, and censorship used to filter and delete inappropriate comments (Wright, 2006). Research in this area has focused mostly on censorship like automatic filtering algorithms and policies to regulate malicious comments. The Tapestry system was one of the first efforts to rate online messages. Users were asked to rate content on an intranet site and, through collaborative filtering strategies, select news articles to recommend (Goldberg et al., 1992). Resnick (2001) discussed ways that online groups might regulate undesirable commentary. Crowdsourcing large groups to rate content could lead to better comments. Similarly, Lampe et al. (2014) explored how the tools currently in use to moderate and manage online comments might be applied to dealing with the large quantities of available information and to enhancing online discussion. This paper investigates commentmoderation policies and whether including discussion leads, such as seed comments, can foster better comments and more deliberative discussions.

## 2.2 Deliberative Discussion

For many years, political deliberation has been a favored theme of scholars who believe it can lead to an informed citizenry and, in turn, to a higher form of public opinion (Dutwin, 2003). Deliberation requires participants willing to address issues through arguments and counterarguments that are supported by evidence, data, and logic (Brookfield & Preskill, 2005). Its importance lies in the increased chance that the positions reached are the best possible positions given the situation (Jackman & Sniderman, 2006). Deliberative discussions are not like debates in which no one’s position changes. Rather, deliberation implicitly encourages listening to other viewpoints in an effort to understand alternatives and not simply to gather fodder for a rebuttal (Heanue et al., 2003). Many studies have suggested the characteristics that define deliberative discussion. Table 1 summarizes its five main characteristics: rationality, relevance, equality, reciprocity, and politeness.

Table 1. Characteristics of Deliberative Discussion

<table><tr><td>Author</td><td>Target Context</td><td>Rationality</td><td>Relevance</td><td>Equality</td><td>Reciprocity</td><td>Politeness</td><td>Other dimensions</td></tr><tr><td>Burkhalter, Gastil, and Kelshaw (2002)</td><td>Face-to-face</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Dahlberg (2001)</td><td>Online</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td>Autonomy from power</td></tr><tr><td>Dutwin (2003)</td><td>Face-to-face</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td>Process by public good</td></tr><tr><td>Fishkin and Luskin (2005)</td><td>Face-to-face</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>Comprehensive points of view</td></tr><tr><td>Gustmann and Thompson (2009)</td><td>Online</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td></tr></table>

Table 1. Characteristics of Deliberative Discussion

<table><tr><td>Halpern and Gibbs (2013)</td><td>Online</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Jankowski and van Selm (2000)</td><td>Online</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td>Diversity of topics</td></tr><tr><td>Knight and Johnson (1994)</td><td>Face-to-face</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>Idealized process</td></tr><tr><td>Min (2007)</td><td>Face-to-face/ Online</td><td>√</td><td></td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Moy and Gastil (2006)</td><td>Face-to-face</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Strandberg and Berg (2013)</td><td>Online</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td></td></tr></table>

## 2.3 Social Contagion Theory

Rationality rests on making logical claims and arguments (Fishkin & Luskin, 2005; Min, 2007; Moy & Gastil, 2006; Halpern & Gibbs, 2013; Knight & Johnson, 1994; Dutwin, 2003; Strandberg & Berg, 2013) and contributes to the quality of public opinion (Min, 2007). Relevance insists that commenters stay on topic (Jankowski & van Selm, 2000). Since deliberative discussion is a political decision-making process (Gutmann & Thompson, 2009; Knight & Johnson, 1994), relevance to the topic at hand is an important factor. Equality is the basic element of public discussion. According to Burkhalter et al. (2002), deliberative discussion is a democratic process in which participants have an adequate opportunity to speak (Moy & Gastil, 2006) and also enjoy autonomy from political or economic influence (Dahlberg, 2001). Reciprocity is also an important characteristic because in deliberative discussion, participants gain awareness of others’ perspectives (Jankowski & van Selm, 2000), listen attentively, and converse in a way that bridges diverse types of speech and knowledge (Burkhalter et al., 2002; Moy & Gastil, 2006). The last characteristic is politeness (or civility), which is expressed through respect and polite behavior (Fishkin & Luskin, 2005; Burkhalter et al., 2002; Min, 2007; Halpern & Gibbs, 2013; Strandberg & Berg, 2013). Respect for others is a fundamental element of deliberative discussion.

Of these five characteristics, we selected three— rationality, relevance, and politeness—as criteria to use for our study. Since in an online context, people tend to be less aware and less concerned with social distinctions, the impact of social status and power is reduced, and an equalizing effect becomes more prominent (Dubrovsky et al., 1991); thus, we chose not to consider equality. Furthermore, since the primary function of comments on news sites is to express thoughts and opinions regarding the news, rather than responding directly to other people’s comments, we opted not to investigate reciprocity.

Researchers in various fields, such as sociology, social psychology, and psychoanalysis, have devoted much attention to the concept of “social contagion,” a term originally used by Gustave Le Bon (1895). Le Bon coined this term to describe the bad behavior people adopt when they are part of a crowd (Stephenson & Fielding, 1971). It describes how one person (an “initiator”) influences a behavioral aspect of another (the “recipient”) without this second person having any perception of an overt intention to influence. (Levy & Nail, 1993). Levy and Nail (1993) divided social contagion into three categories: disinhibitory, echo, and hysterical. Disinhibitory contagion occurs when a recipient loosens personal restraints in response to seeing an imitator perform an appealing act. In echo contagion, a recipient’s reaction to an initiator occurs spontaneously with little conscious thought. Hysterical contagion involves the spread of physical symptoms from initiator to recipient without the presence of any discernible mode of transmission. The majority of the prior research on social contagion has focused on negative behavior; however, positive behaviors can be also socially contagious. Tsvetkova and Macy (2014) found that generosity to others was contagious. They conducted an experiment in the context of donations and revealed that receiving help or just observing other persons helping others might increase the likelihood of generosity toward a stranger. Both positive and negative behaviors can be socially contagious.

A social contagion can be emotional as well as behavioral. A person or group can influence the emotions of another person or group through the conscious or unconscious induction of emotional states (Schoenewolf, 1990). Although emotional contagion is generally associated with face-to-face environments (Howard & Gendel, 2001; Neumann & Strack, 2000), some empirical studies have found that contagions can also be present in the electronic communication environment (Belkin, 2009). According to Coviello et al. (2014), both negative and positive emotions were transmitted in the Facebook context. They also showed that positive and negative emotional expressions have inhibitory effects on others and that highly similar feelings tend to be contagious.

Social contagions can appear as a cascade phenomenon (Nooy et al., 2011) featuring individual behavioral changes that flow through a group to shift patterns of behavior (Heal & Kunreuther, 2010). Bikhchandani et al. (1992) argue that such a phenomenon could spread through observation of others without conscious intention. Thus, the factor that instigates a social contagion is very important because it can determine whether the cascade that results is positive or negative. Although social contagions can be positive, previous works have focused on socially irresponsible behaviors like littering (Cialdini et al., 1990) and graffiti (Keizer et al., 2008). According to Tsvetkova and Macy (2015), one instance of undesirable conduct can set off other bad behavior with consequences that dwarf the original act.

Our paper uses social contagion theory to examine the influence of initial seed comments on those who write subsequent comments. We expect that the initial comments will affect the emotions and behavior of the next commentator, and that this will influence the next, and so on, eventually creating a cascade akin to that described by social contagion theory.

## 2.4 Indentifiability and Anonymity

The identifiability of a subject means that someone can be identified within a group of similar people who, in turn, represent all the people who could have potentially caused an action (Pfitzmann & Hansen, 2010). Anonymity is essentially the opposite condition (Pfitzmann & Köhntopp, 2001; Christopherson, 2007); identifiability is the opposite of anonymity, and the two are conceptually connected. Many researchers have studied the effects of anonymity on discussion, but the empirical evidence is inconclusive. Studies about the effects of anonymity on the satisfaction of participants in discussions have similarly found conflicting results (Jessup & Tansik, 1991; Connolly et al., 1990; Valacich et al., 1994).

On the positive side, people are less afraid of social evaluation and disapproval when they feel anonymous, and thus, they can be more honest and objective in their opinions (Pinsonneault & Heppel, 1997) and suggest more and diverse ideas (Shepherd et al., 1996; Pissarra & Jesuino, 2005). On the negative side, when people feel anonymous, they tend to be more aggressive and critical in evaluating others’ thoughts or opinions (Connolly et al., 1990; Jessup & Tansik, 1991; Jessup et al., 1990). Anonymity in terms of Le Bon’s (1895) elucidation of mob psychology plays an important role in turning rational individuals into primitive and emotional ones. Based on Le Bon’s study, Zimbardo (1969) argued that anonymity is the dominant variable in turning a crowd into a deindividuated state. When people cannot be identified, they cannot be assessed, criticized, or punished; consequently, they feel uninhibited and unrestrained, and, therefore, exhibit more disinhibition, for example, in the form of insulting or hostile behavior. When rational individuals feel anonymous, they sometimes begin to feel invincible and lose their sense of self-restraint. Under such conditions, they may yield to their instincts and submit to their racial unconscious (Suler, 2004).

In electronic communication environments, such as social network services and news comment systems, the impact of anonymity is often amplified because it uses computer-mediated text, and communication tends to seem more impersonal (Kiesler et al., 1984). Cyberbullying in the form of malicious comments occurs mostly under conditions of anonymity, and Lee (2015) has suggested that “abused anonymity” is an important research topic associated with the Bright ICT Initiative, which seeks to prevent undesirable activities on the Internet. Empirical research on the social-psychological aspects of anonymity in SNS is in its early stages (Byeon & Chung, 2012). The division between identifiability and anonymity in cyberspace can be vague, so this distinction may be different from how it is perceived in the physical world (Hwang, 2008). Using a real name does not preclude a sense of anonymity, because no face-to-face contact occurs in cyberspace; conversely, someone who uses an alias or pseudonym may still worry about the possibility of being identified on the basis of circumstantial details available, for example, on social networking sites. Normal SNS accounts generally include various personal details, such as birthdays, schools attended, or employment that can serve to identify users. Thus, in cyberspace, SNS accounts can sometimes be associated with higher degrees of identifiability than a real name.

## 3 Research Model and Hypotheses

This paper proposes two comment moderation policies. One is based on social contagion theory and the other on an online inhibition effect. We examine the effects of these policies on comment behavior, especially in terms of deliberative discussion. These two policies provide high-quality seed comments and increase identifiability through SNS accounts. Figure 1 presents the research model.

![](/api/attachments/Q2Y43PAF/fulltext/images/0bcd8189cd85accde67cbd12eb303ee539c65d81536a48476284dd25a33cda3a.jpg)  
Figure 1. Research Model

It is important that organizations or communities design environments that encourage their members to behave in accordance with their organization’s goals and beliefs. One way of doing this is to create an institutional climate, defined as a specific situation existing at a specific time, that gives context to what members of the institution think, feel, value, and define as behavioral norms (Bock et al., 2005; Delong & Fahey, 2000). According to social contagion theory, in such a situation, a person’s emotions, attitudes, and behaviors spread to others without anyone being aware of this (Levy & Nail, 1993).

Social contagion theory explains the phenomena of mimicking others’ behavior unconsciously or feeling the same emotions as others. If this phenomenon is continuously repeated to others and generates a social cascade, it would also lead to a phenomenon characterized by people’s attitudes and behaviors becoming similar to each other within a specific arena (Le Bon, 1895). In our paper, social contagion theory serves as the basis for the seed comment policy we propose. The characteristics and guidance of an initiator are critical in social contagion theory (Anderson & Thomson, 2004). If initiators have positive characteristics, then the effects of the contagion are also positive; if they have negative characteristics, the reverse is true. The position of a seed comment as the first response to a topic would serve to set an example for subsequent comments. If the seed comment establishes a tone of quality discourse, logic, and courtesy (Price & Cappella, 2002; Kim & Sun, 2006), the theory contends that the next comments would be likelier to reflect the same standards. Rational and considerate high-quality seed comments would influence subsequent comments in a positive direction, whereas low-quality comments would exert a negative effect. In other words, a seed comment policy would play the role of constructing an institutional climate (Delong & Fahey, 2000; Bock et al., 2005) of norms and value criteria for comment writing. Thus, we propose the following hypothesis.

H1: High-quality seed comments will have a positive impact on the degree of deliberative discussions in comments.

Pfitzmann and Köhntopp (2001) define the levels of anonymity as unlinkability and unobservability. High degrees of anonymity occur when individuals cannot be identified (unobservability) and their messages and behaviors cannot be linked to their identity (unlinkability). Anonymity helps people hide more easily within a crowd and triggers the online inhibition effect by making them feel disguised or masked (Suler, 2004). Thinking they are hidden, they may feel free to conduct themselves in undesirable ways. People who consider themselves unidentifiable may have less fear of punishment, may be more likely to act impulsively, and may behave in ways alien to how they conduct themselves offline (Siegel et al., 1986). Researchers have extensively studied the effects of anonymity on the quality of comments, including their degree of civility (Kilner & Hoadley, 2005; Omernick & Sood, 2013). According to Santana’s (2014) analysis of news comments, 53% of anonymous comments were uncivil, but only 28.7% of comments bearing real names were. Because people could be identified when they commented with their real name, they may have been concerned about others’ evaluations and criticisms of them and refrained from inappropriate behavior, such as writing malicious comments.

Although the relationship between anonymity and comments has been extensively researched, few studies have been conducted in the context of the currently pervasive SNS. Pfitzmann and Köhntopp (2001) compared the level of anonymity of various accounts and concluded that anonymous accounts were the most anonymous, followed by pseudonyms, with real names being least anonymous. Based on this, the degree of anonymity would likely rank even lower on an SNS account, where personal information, such as real name, age, and gender, personal photos, details of daily life etc., can be posted (Zhao et al., 2008). Hwang (2008) argued that a real name does not necessarily guarantee that a person can be identified on the Internet or an SNS account; the level of identifiability may actually be higher regardless of the name used in the context of various personal cues. Therefore, when people write comments using their SNS accounts, which ranks high in terms of the degree of identifiability, people may be more responsible in writing comments because they care about others’ opinions and attention. Thus, we propose the following hypothesis.

## H2: A level of high identifiability on a commentwriter’s account will positively affect the degree of deliberative discussion in comments.

The negative effect of a low-quality seed comment on the degree of deliberative discussion can be moderated by the level of identifiability. Negative emotions or unlawful behavior, such as swearing, attacking others, and graffiti, may be contagious through mimicking and social reciprocity (Kwon & Gruzd, 2017; Keizer et al., 2008). Keizer et al. (2008) validated that based on the broken window theory, a disorderly environment is an essential factor for catalyzing unlawful behaviors. Through six studies in anonymous settings, they found that one violation of a norm weakens people’s concern for appropriateness and fosters violations of other norms that spread disorder. Accordingly, anonymity is a catalyst for rapid contagion effects (Wilson & Kelling, 1982). In an anonymous setting, the desire to appear equally strong or even stronger gives rise to mimicry that can be communicated to others as aggression. (Kwon & Gruzd, 2017). Guadagno et al. (2010) investigated the psychological factors of Bronze Night in 2007 (the month-long online attacks on Estonia’s Internet infrastructure because of the relocation of The Bronze Soldier in Tallinn). They argued that the anonymity of online interaction explains why people are more likely to engage in contagious aggressive behavior. Participation in the attacks and the spread of messages were fueled by the relative anonymity of online communication, which made people behave with group norms and become aggressive (Guadagno et al., 2010).

In this study, we propose seed comments and commenter identifiability as active moderation policies to induce deliberative discussion. Prior studies discussed above have assessed the interaction effect of seed comments and commenter identifiability. Negative emotional and behavioral contagions can be provoked by low-quality seed comments, and can then reinforce a low level of identifiability. High levels of commenter identifiability can mitigate low-quality seed comments and prevent malicious commenting behavior from spreading. Even if seed comments are irrational, irrelevant, or impolite, highly identifiable people will nevertheless likely have reservations about mimicking their tone because such comments do not conform with general social norms. Conversely, anonymity unleashes unrestrained behavior (Dipboye, 1977), and people who are anonymous will feel less pressure and will act more freely on their own will because they are not easily identifiable. We believe that the contagion effect of low-quality seed comments will decrease with high identifiability. Thus, we propose the following hypothesis.

H3: The quality of seed comments and the level of identifiability will have an interaction effect on the degree of deliberative discussion—i.e., the negative impact of low-quality seed comments on the degree of deliberative discussion will be weaker with high levels of identifiability than with low levels of identifiability.

## 4 Research Method

## 4.1 Experimental Design

We used a longitudinal online experiment as the research method. Using this approach with a commercial survey company is superior in many ways to traditional laboratory experiments that use undergraduates. Three advantages include the diversity of possible participants, simpler recruitment, and speed of implementation (Mason & Suri, 2012). However, some of the disadvantages of the older approaches still exist: As with the more traditional techniques, panelists may lack motivation, be easily distracted, and may fail to heed instructions (Tsvetkova, 2015).

The experimental groups were designed as a 2 (seed comment: high quality vs. low quality) x 2 (login account: Facebook account vs. anonymity) betweensubjects factorial design. A commercial application software company developed the mobile application for this experiment. Experiment participants were recruited from ordinary people (not students) to enhance external validity. Subjects were drafted from people who met the following prerequisites: They should be interested in political news and should have experience writing occasional comments; they should be daily news readers who use an Android smartphone; and they should have active Facebook accounts. We randomly assigned participants to four groups (see Table 2), and analyzed the data of 137 subjects for this study.

Table 2. Experiment Group

<table><tr><td rowspan="2" colspan="2">Treatment</td><td colspan="2">Identifiability</td></tr><tr><td>Low: Anonymous</td><td>High: Facebook</td></tr><tr><td rowspan="2">Quality of seed comment</td><td>High</td><td>Group 1</td><td>Group 2</td></tr><tr><td>Low</td><td>Group 3</td><td>Group 4</td></tr></table>

## 4.2 Experiment System

Many people consume news on a daily basis. Political news, in particular, often stimulates active discussion among readers. Although the topics most likely to ignite inflammatory comments differ by region, politics sets off the most inflammatory comments in most continents, including Asia, the Middle East, Africa, and South America (WAN-IFRA, 2016). Therefore, we chose political news for this experiment. Participants in the experiment were assigned to read news stories and write comments for 15 days (3 weeks, excluding weekends) using a mobile Android application developed for the experiment. During the 15 days of the experiment, we provided five political news stories daily. We drew these stories from highly ranked news stories provided by Naver News (news.naver.com), Korea’s top news portal. A web crawler automatically gathered the 10 most viewed news stories each day before noon, and we selected the top five of these, discarding any duplicates. All participants read the same news, but the groups received different qualities of seed comments.

Many scholars assert that high-quality comments should reflect rationality and respect in terms of their content and linguistic style (Price & Cappella, 2002; Kim & Sun, 2006, Yang, 2008). According to Price and Cappella (2002), high-quality comments should develop a viewpoint anchored in argument and should also show “consideredness” of others’ opinions. Diakopoulos and Naaman (2011) also emphasize that “flaming” contributes to lower quality in the realm of online comments. It is also noteworthy that people read news comments not only to get new information or figure out others’ opinions or views, but also as a source of fun (Kim & Kim, 2008). News comments can be a source of entertainment and amusement, and online comments have hedonic functions as well as utilitarian functions.

Chen et al. (2011) divided the quality of comments into five levels— excellent, good, fair, bad, and abusive— based on how informative, useful, relevant, interesting, harassing, and violent the comments were. Thus, we define high-quality comments as helpful, credible, entertaining, and less irritating. Based on these characteristics, we created the seed comments by combining three actual comments from the Naver News site that demonstrated high or low quality, respectively— all of them were of similar length (see Appendix 1 for examples of the seed comments). A new comment always appeared above all other comments. The seed comment was on top of the feed at the beginning, but as comments were added, it moved to the bottom of all the comments without pagination, similarly to how most comment systems appear on real news sites.

The experiment application consisted of two layers. News headlines for each day were shown in the first layer. A click on a headline displayed the news content. The second layer displayed the news story and a window for commenting on the story. Participants could access past news by using the date menu at the bottom of the first layer. As a first step, participants in the experiment logged in using either a Facebook account or a pseudonym (see Figure 2), depending on their experimental group. Once logged in, we did not require them to log in again for the rest of the experiment. The Facebook groups could see the Facebook icon when writing comments or reading others’ comments; by clicking on a comment, they could move to the commenter’s Facebook timeline. In contrast, the groups using pseudonyms could see only the name “\*\*anonymous\*\*” while writing and reading comments, and could not further identify the comment writers (see Figure 3). Comments were shown in chronological order. Every participant’s activities in reading news and writing comments were saved as log data over the course of the experiment.

![](/api/attachments/Q2Y43PAF/fulltext/images/37d8252b875963c38e62bf1dcf93dd3f4b445ff427aad5b216cec18dfadb0fe2.jpg)  
Figure 2. Login Pages

![](/api/attachments/Q2Y43PAF/fulltext/images/02974f71373b436250de42f9cb0fe5d05b28cb3b2d414f1d5561afd1bc8f4759.jpg)  
Figure 3. News Comment Features

## 4.3 Experimental Procedure

Before the actual experiment phase started, participants answered a survey on their news-usage patterns, such as news reading time, preferred news categories, and their frequency of reading and writing comments. Around noon during each of the 15 days of the experiment, we posted the news and seed comments for that day on the application. We sent participants push messages to remind them of their assignment; however, to avoid interfering in their volition, we sent the message in the morning before updating the day’s news. We asked participants to read the day’s news and recommended that each of them write at least one comment every day. After completing the experiment, participants answered another survey about the task and manipulation checks. They received 20,000 Korean Won (approximately \$17) for their full participation in the experiment.

## 4.4 Dependent Variable

The participants were asked to do three tasks: complete a presurvey asking about their news usage habits, participate in the experiment, and complete a postsurvey that contained questions to check for manipulation. While 216 participants completed the presurvey, 175 of them completed the entire experiment. However, since 38 participants wrote very few comments during the experiment, we collected data from only the 137 participants who wrote comments for more than 5 days during the experiment. These 137 participants wrote 5,635 comments, averaging 41 comments for each participant. The dependent variable was the degree of deliberative discussion in the news comments, which we measured through content analysis. That degree was rated according to Strandberg and Berg’s (2013) characteristics for deliberative discussion. Strandberg and Berg (2013) suggest that rationality, relevance, reciprocity, and politeness comprise the four characteristics of deliberative discussion in a news comment context. However, as mentioned in the literature review section, we excluded reciprocity, deeming it not relevant for our context. We calculated the overall deliberative discussion scores as the sum of their normalized values.

We assigned 10 graduate students (five groups of two members each) to complete the content analysis on the comments. We derived the coding scheme from Strandberg and Berg (2013) and modified it by removing the reciprocity dimension. We designed our coding scheme according to the three dimensions of deliberative discussion: rationality, relevance, and politeness (see Appendix 2 for the full coding scheme). Before beginning content analysis, the coders were trained on the coding scheme and had time to implement a pilot analysis on some of the comments. The first round of the content analysis showed a Cohen’s Kappa intercoder reliability score of 0.83. This score means that the two coders substantially agreed with each other in the coding results (Landis & Koch, 1977). In cases of inconsistent coding, a coder from another team was reassigned to complete the final coding.

## 5 Results and Analysis

A total of 137 subjects participated; 31, 37, 37, and 32 subjects were allocated to Groups 1 through 4. The average age of participants was 37 years, and 67% were male (see Table 3 for the demographic information of participants). According to Naver (www.naver.com) and Daum (www.daum.net), which are two of Korea’s representative Internet news portals, the age distributions of Internet news readers, including mobile users, are similar across several different age groups (50+ age group is slight exception): 20-29 (23.8% for Naver and 21.4% for Daum), 30-39 (25.3% for Naver and 26.5% for Daum),

40-49 (21.9% for Naver and 23.8% for Daum), and 50 and over (11.59% for Naver and 14.31% for Daum). The median age bracket is 30-39 (Korea Press Foundation, 2011); thus, our sample has good fit with the actual population of Internet news readers.

Each group was treated the same statistically in terms of age (F=1.971, p=.121), gender ratio (Chisquare=3.238, p=.356), daily news reading time (F=1.887, p=.135), interest in political news (F =.619, p =.604), and the frequency of reading (F=.082, p=.970) and writing comments (F=.533, p=.660); thus, randomization seems to have been effective.

Table 3. Demographic Information

<table><tr><td>Variable</td><td>Scale</td><td>Group 1</td><td>Group 2</td><td>Group 3</td><td>Group 4</td><td>Total</td></tr><tr><td rowspan="2">Gender</td><td>Male</td><td>20</td><td>22</td><td>29</td><td>31</td><td>92 (67.2%)</td></tr><tr><td>Female</td><td>11</td><td>15</td><td>8</td><td>11</td><td>45 (32.8%)</td></tr><tr><td rowspan="4">Age</td><td>20-29</td><td>11</td><td>15</td><td>8</td><td>11</td><td>45 (32.8%)</td></tr><tr><td>30-30</td><td>3</td><td>10</td><td>9</td><td>8</td><td>30 (21.9%)</td></tr><tr><td>40-49</td><td>6</td><td>8</td><td>11</td><td>8</td><td>33 (24.1%)</td></tr><tr><td>50-59</td><td>11</td><td>4</td><td>9</td><td>5</td><td>29 (21.2%)</td></tr><tr><td colspan="2">Total</td><td>31</td><td>37</td><td>37</td><td>32</td><td>137 (100%)</td></tr></table>

We provided participants with different qualities of seed comments and different levels of identifiability according to their experimental group (see Table 2). To verify that treatments were properly applied, we asked the participants the following two questions to assess quality and identifiability, respectively: “Did the first comment you read contain profanity or a rude tone?” and “Was your name displayed when you wrote your comment?” The Chi-square result showed that all treatments were clearly manipulated (p-value for both treatments<.001).

Additionally, we investigated the participants’ perception of the seed comments with a multidimensional concept for comment quality that was composed of dimensions of helpfulness (Yin et al., 2014), credibility, entertainment and irritation (Kim & Han, 2014) (see Appendix 3 for the questionnaire items). The ANOVA results showed that there were significant differences in the perception of seed comments on each of these dimensions between the high-quality, “good seed” comment groups and the low-quality “bad seed” comment groups. The participants in Groups 1 and 2 (high-quality seed comment groups) thought the seed comments more helpful, credible, entertaining, and less irritating. We also measured the level of perceived anonymity to check that the manipulation of identifiability was done properly. Groups 2 and 4 (Facebook groups) showed a significantly lower level of perceived anonymity than Groups 1 and 3 (anonymous groups). The ANOVA results are shown in Appendix 4. Thus, we believe all the manipulations were done properly.

The average number of comments per news story per group was 18.78.

ANOVA and Scheffe’s post hoc test resulted in no significant difference in the number of comments among Groups 1, 2, and 4 (mean of Group 1=18.29, mean of Group 2=17.09, and mean of Group 4=16.87). However, Group 3 (low-quality seed comment and anonymous) wrote significantly more comments than the other groups (mean=22.88, p-value < .01) (see Table 4).

Table 4. Number of Comments per News Item

<table><tr><td>Number of comments</td><td>Group 1</td><td>Group 2</td><td>Group 3</td><td>Group 4</td><td>Total</td></tr><tr><td>Minimum</td><td>10</td><td>9</td><td>15</td><td>9</td><td>9</td></tr><tr><td>Maximum</td><td>30</td><td>30</td><td>32</td><td>32</td><td>32</td></tr><tr><td>Average</td><td>18.29</td><td>17.09</td><td>22.88</td><td>16.87</td><td>18.78</td></tr></table>

## 5.1 Hypothesis Test

Seed quality and identifiability were our treatment variables, which we expected would influence comments by subsequent users. We gave each group of participants a different combination of treatments. To test the differences between groups in terms of the degree of deliberative discussion of user comments, we regressed the user-response variables—rationality, relevance, politeness, and the sum of their normalized values—on the treatments and their interaction:

$$
\begin{array}{l} \mathrm{Resp} _ {i, g, n} = \beta_ {0} + \beta_ {1} \mathrm{DIdentifiability} _ {g} + \\ \beta_ {2} \mathrm{DSeed} _ {g} + \beta_ {3} \mathrm{DIdentifiability} _ {g} \times \\ \mathrm{DSeed} _ {g} + \mathrm{NewsFE} _ {n} + \epsilon_ {i, g, n} \end{array}\tag{1}
$$

Where ${ \mathrm { R e s p } } _ { i , g , n }$ denotes the response by individual i of group g for news article n. DIdentifiability<sub>g</sub> is a dummy variable, which equals 1 if a participant logged in using a Facebook account. DSeed<sub>g</sub> is another dummy, which equals 1 if a user is given a seed comment of high quality. Their interaction was also controlled to test whether they had any synergy. News $\mathrm { { \dot { E } } _ { n } }$ is a dummy variable equal to 1 for a corresponding news article and zero otherwise to control for fixed effects of news articles. We report the results of this regression in Table 5. Each column corresponds to the degree of deliberative discussion in four aspects: rationality, relevance, politeness, and the sum of their normalized values.

Table 5. Treatment Effects on the Degree of Deliberative Discussion<sup>1</sup>

<table><tr><td>IV\DV</td><td>(1) Rationality</td><td>(2) Relevance</td><td>(3) Politeness</td><td>(4) Overall</td></tr><tr><td>DIdentifiability</td><td>0.163***(4.703)</td><td>0.100***(3.170)</td><td>0.121***(3.404)</td><td>0.206***(6.059)</td></tr><tr><td>DSeed</td><td>0.105***(3.110)</td><td>0.138***(4.461)</td><td>0.237**(6.814)</td><td>0.257***(7.744)</td></tr><tr><td>DSeed X DIdentifiability</td><td>0.061(1.215)</td><td>0.097**(2.114)</td><td>-0.104***(-2.012)</td><td>0.029(0.592)</td></tr><tr><td>News fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>5,635</td><td>5,635</td><td>5,635</td><td>5,635</td></tr><tr><td>R-squared</td><td>0.141</td><td>0.283</td><td>0.097</td><td>0.174</td></tr><tr><td colspan="5">The dependent variable is the degree of deliberative discussion in four aspects: rationality, relevance, politeness, and the sum of their normalized values. DIdentifiability is a dummy variable that equals 1 for those who post comments with their Facebook accounts and zero if posted anonymously. DSeed is a dummy variable that equals 1 for those who received a high-quality seed and zero otherwise. The third variable denotes the interaction between these two treatment variables. Fixed effects were controlled for each news story. Numbers in parentheses are OLS t statistics. ***, **, and * denote significance at the 1%, 5%, and 10% levels, respectively.</td></tr></table>

As expected, high-quality seed comments had a positive impact on the degree of deliberative discussions, thus Hypothesis 1 was supported. High identifiability also positively affected the degree of deliberative discussion in the comments, thus Hypothesis 2 was supported as well. Table 5 shows that both high identifiability and high-quality seed comments significantly improved user comments across all criteria. Moreover, politeness<sup>2</sup> was the only significant difference between the coefficients, confirming that they had almost equal influence. In the exception, seeds had stronger effects on politeness than on identifiability.

Furthermore, the two treatments had a positive synergy for relevance but a negative one for politeness. The two effects cancelled each other out, and overall, contrary to our expectation, there are no interaction effects between seed quality and identifiability on the sum of their normalized values. Thus, Hypothesis 3 is not supported.

## 5.2 Sequence Effects on the Treatments

Given that seed quality and identifiability had significant effects on user comments, one may wonder how persistent these effects are. Seeds may affect early comments more than later ones because latecomers may pay less attention to the seeds. Moreover, identifiability may possibly improve not only the quality of comments but also the persistence of the

treatment effects. To test this hypothesis, we drew Figure 4 to show the time trends of the user-response variables for each group. The response variables are demeaned for each news article to control for news fixed effects. The horizontal axis denotes sequence— i.e, the order in which each comment was posted. To make the graph smoother, we show the moving average of the last three comments of each group. The quality of comments is demeaned to control for news fixed effects.

![](/api/attachments/Q2Y43PAF/fulltext/images/5703fee776c5d51c431510d43a8277e526581e0844af094c19d7d846780480c2.jpg)  
(a) Rationality

![](/api/attachments/Q2Y43PAF/fulltext/images/2f8a54e1f6e230ee316dee7e3af26a65fa5de9c2ff982a8169d77ac50d791a03.jpg)  
(b) Relevance

(2)  
![](/api/attachments/Q2Y43PAF/fulltext/images/0a99fbff783fbe4826b5ab55821dfa3b13a8326d956f834ea43cd0020d4d38cc.jpg)

(c) Politeness  
![](/api/attachments/Q2Y43PAF/fulltext/images/adb8ce84a1bf50281073687ab05601834aa0766b3b7fa610be9c491d04eb7747.jpg)  
(d) Overall  
Figure 4. Sequence Effects of the Treatment

According to Figure 4, the responses of Group 1 (highquality seeds/anonymous) responses start at significantly positive levels but decline rapidly over time in rationality, relevance, and overall. In comparison, the responses of Group 2 (high-quality seeds/Facebook account) start at even higher values than Group 1 and then persist until the end in all but rationality. Therefore, these results show that the positive effects of high-quality seeds persist only when they are combined with identifiability. Otherwise, they soon vanish.

As for low-quality seed comments, in contrast, Group 3’s (low-quality seeds/anonymous) comments start as significantly negative and remain so in all but politeness.

However, the responses of Group 4 (low-quality seeds/Facebook account) move around zero without any specific patterns. Interestingly, these results suggest that low-quality seeds may demonstrate negative and persistent influences only when combined with anonymity.

These results are again confirmed by the following regression.

$$
\boxed { \begin{array}{c} \operatorname{Resp} _ {i, g, n} = \beta_ {0} + \\ \sum_ {g = 2} ^ {4} \beta_ {g} \text {DGroup} _ {g} + \sum_ {g = 1} ^ {4} \gamma_ {g} \text {DGroup} _ {g} \times \\ \text {Sequence} _ {i, g, n} + \text {NewsFE} _ {n} + \epsilon_ {i, g, n} \end{array} } ^ {\mathrm{g=2}}
$$

In this specification, DGroup<sub>g</sub> captures the y-intercept of dependent variables at Sequence = 0, and the interaction term, DGroup<sub>g</sub> x Sequence<sub>i,g,n,</sub> denotes the slopes of their time trends. The results, which are consistent with the figure 4, are shown in Table 6.

Table 6. Sequence Effects of the Treatments

<table><tr><td>D.V.I.V.</td><td>(1)Rationality</td><td>(2)Relevance</td><td>(3)Politeness</td><td>(4)Overall</td></tr><tr><td>DGroup2</td><td>0.171***(2.466)</td><td>0.069(1.089)</td><td>-0.070(-0.987)</td><td>0.091(1.336)</td></tr><tr><td>DGroup3</td><td>-0.230***(-3.460)</td><td>-0.279***(-4.587)</td><td>-0.342***(-5.004)</td><td>-0.456***(-6.983)</td></tr><tr><td>DGroup4</td><td>-0.075(-1.067)</td><td>-0.206***(-3.203)</td><td>-0.232***(-3.212)</td><td>-0.275***(-3.982)</td></tr><tr><td>Sequence X DGroup1</td><td>-0.020***(-4.688)</td><td>-0.014***(-3.537)</td><td>0.001(0.136)</td><td>-0.018***(-4.248)</td></tr><tr><td>Sequence X DGroup2</td><td>-0.015***(-3.621)</td><td>-0.001(-0.304)</td><td>0.010**(2.228)</td><td>-0.004(-0.878)</td></tr><tr><td>Sequence X DGroup3</td><td>-0.006**(-1.981)</td><td>0.000(0.056)</td><td>0.009***(2.793)</td><td>0.002(0.512)</td></tr><tr><td>Sequence X DGroup4</td><td>-0.007(-1.632)</td><td>0.003(0.732)</td><td>0.013***(2.784)</td><td>0.005(1.036)</td></tr><tr><td>News fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>ObservationsR-squared</td><td>5,6350.147</td><td>5,6350.284</td><td>5,6350.100</td><td>5,6350.177</td></tr><tr><td colspan="5">The dependent variable is the quality of comments in four aspects: rationality, relevance, politeness, and the sum of their normalized values. DGroup2-4 are dummy variables for each group. Group 1 and Group 3 are anonymous and Group 2 and Group 4 post comments with their Facebook accounts. Group 1 and Group 2 are given high-quality seeds in the beginning, but Group 3 and Group 4 receive low-quality ones. Fixed effects were controlled for each news story. Sequence denotes the order in which each comment was posted. Sequence is 1 for the first comment, 2 for the second, etc. Sequence interacts with each group dummy variable. Numbers in parentheses are OLS t statistics. ***, **, and * denote significance at the 1%, 5%, and 10% levels, respectively.</td></tr></table>

A comparison of the results in Table 5, Table 6, and Figure 4 provides an interesting implication for the interaction of seed quality and anonymity. Considered alone, as in Table 5, the interaction term is not significant. However, conditional on the sequence of comments, Figure 4 and Table 6 show that the interaction term affects the persistence of subsequent comments. The impact on persistence is most visible between Group 1 and Group 2, both of which were treated with high-quality seeds. The effect of the treatment persists when combined with Facebook identity (Group 2), but the effect is positive only at the outset and gradually vanishes when respondents are anonymous (Group 1). Therefore, we conclude that although the interaction term does not affect the quality of comments, identifiability makes the effects of highquality seeds more persistent.

## 5.3 Further Analysis

In addition to hypotheses testing, we analyzed the data to determine if there was a gender effect. Figure 5 displays our results in terms of the degree of deliberative discussion. Females generally scored higher than males $( \mathrm { t } ~ = ~ 8 . 7 8 , ~ \mathrm { p } ~ < ~ . 0 1 )$ . Moreover, we found gender differences in all groups except Group 1. Most of the participants susceptible to low-quality seed comments were males; most females did not respond to low-quality seed comments. Responses in Group 3 (low-quality seeds/anonymous) were especially interesting. As expected, overall responses in this group showed the lowest levels of deliberative discussion; but surprisingly, responses from females in Group 3 showed even higher levels of deliberative discussion than Group 1 (high-quality seeds/anonymous). To understand this unexpected result, we checked the perceived anonymity of each subject. Females in Group 3 had the lowest perceived anonymity, even lower than females in the Facebook groups. It is unclear why this was the case: perhaps low-quality comments made females feel uneasy and induced fear that they might be identified if they followed the pattern set by the low-quality seed comments. In contrast, males in Group 3 showed the highest degree of perceived anonymity of males in any group, and were highly susceptible to low-quality seed comments, resulting in this group scoring the lowest level of deliberative discussion of any of our groups.

![](/api/attachments/Q2Y43PAF/fulltext/images/e12fbe2d4815c588cdf6a6121865a80ad1f47f811d37221ef69862e80327b45a.jpg)  
Figure 5. Gender Differences

We were also curious about whether the participants exhibited any behavioral time trends. For example, would repeated exposure to treatments (seed quality and identifiability) induce any cumulative effects on the participants’ behavior? Or, would comment quality deteriorate over time as participants became bored with the experiment? Berlyne (1970) came up with a two-factor theory to explain the effects of prolonged stimuli. According to this theory, familiarity with stimuli may play out in the interaction between two antagonistic processes. In one, the stimuli become more appealing with familiarity. In the other, the stimuli become less appealing with familiarity. The loss of appeal may reflect a “tedium” factor, and increased appeal may reflect a “positive-habituation” factor. Which of these prevails in specific cases is unpredictable. In our case, it is possible that the effects of seeds and identifiability could be enhanced over time. Just as continuous exposure to advertisements or media shapes people’s perspectives and behavior (Stice et al., 1994), repetitive exposure to high-quality or low-quality seed comments could influence people to internalize a pattern of writing comments that reflects the tone and standards of the seed comments.

To test this trend, we took the average of the overall qualities of comments by an individual (i) per date (t), $\overline { { \mathrm { R e s p } } } _ { i , t }$ ,and then regressed this variable on dates (t),

$$
\overline {{\mathrm{Resp}}} _ {i, t} = \beta_ {0} + \beta_ {1} t + \epsilon_ {i, t}\tag{3}
$$

Table 7 shows the results of this regression. The first four columns show the regression results for each group, and the last column provides results for the full sample.

As shown in the table, the overall qualities of comments deteriorated over time in all groups. Moreover, Group 2’s comments tended to decline in quality twice as fast as Group 3’s (-0.022 vs. -0.011), but this difference in rate of decline was not statistically significant. Although not reported in this paper, we also checked the interaction terms of the dates with group dummies, $t \mathrm { ~ x ~ } \mathrm { D G r o u p } _ { g } ,$ and these interaction terms appeared insignificant for all groups. Therefore, we can conclude that the qualities of comments deteriorated at almost equal rates. This similarity in rates of decline also implies that deterioration is not attributable to exposure to specific treatments because we did not find any significant differences between groups. Thus, as a stimulus is repeated, participants may gradually succumb to a “tedium” factor. However, this phenomenon in our study may have been a function of the experimental situation and would benefit from further study.

Table 7. Time Trends of Comments

<table><tr><td>Group</td><td>1</td><td>2</td><td>3</td><td>4</td><td>all</td></tr><tr><td>Date</td><td>-0.018***(-2.782)</td><td>-0.022***(-3.546)</td><td>-0.011**(-2.007)</td><td>-0.019***(-3.319)</td><td>-0.018***(-5.648)</td></tr><tr><td>Observations</td><td>366</td><td>465</td><td>440</td><td>414</td><td>1,685</td></tr><tr><td>R-squared</td><td>0.021</td><td>0.026</td><td>0.009</td><td>0.026</td><td>0.019</td></tr></table>

The dependent variable is the average of overall qualities of comments by an individual per date, and the explanatory variable is dates. This test is to show the changes in the quality of comments over time. Numbers in parentheses are OLS t statistics. \*\*\*, \*\*, and \* denote significance at the 1%, 5%, and 10% levels, respectively.

## 6 Discussion and Conclusions

Although a news comment service encourages interaction among readers and gives journalists useful feedback, it has also a dark side—malicious comments. To alleviate the problem and increase the positive function of deliberative discussion, we suggested two moderation policies—providing highquality seed comments and increasing identifiability through SNS accounts—and examined their effects by conducting an online experiment. We found the following relationships throughout the analysis of the experimental data. First, both high seed quality and identifiability improved the quality of user comments in terms of deliberative discussion. Second, their effects were comparable in magnitude. Third, there were no significant interaction effects between seeds and identifiability. Fourth, the effects of high-quality seeds disappeared early with anonymous users but persisted when users’ identities were revealed. Fifth, the effects of low-quality seeds were present and persistent only when combined with anonymity. Otherwise, the negative effects of the low-quality seeds were canceled out by the positive effects of identifiability. Finally, anonymous males were easily provoked to respond to low-quality seed comments, but most females did not respond to low-quality seed comments even in an anonymous situation.

Several limitations should be considered when interpreting the results of the present study. First, we could not control participants’ behavior as we could have in a laboratory because this experiment was conducted in an online setting. For example, we recommended that each participant write at least a comment a day, but compliance varied from participant to participant, and Group 3 (low-quality seed/anonymous) differed significantly in the number of comments written. However, we do not think there is any systematic bias in the results. Next, we created seed comments by assembling three news comments of high and low quality, respectively. But if this policy were to be implemented on a real news site, great care should be taken in handling seed comments because their use could easily be misinterpreted as an attempt to manipulate public opinion. Third, a relatively large number of subjects dropped out without completing the tasks, which is not unusual in online experiments.

Even with these limitations, however, this study has both theoretical and practical implications. First of all, from an academic viewpoint, we extend the scope of comment research by expanding the management objectives from censorship of malicious comments to the initiation of deliberative discussion. We proposed a policy for moderating news comments by using constructive seed comments, and tested its effect. Second, this is the first study that applies social contagion theory to online news comments. To date, social contagion theory has been mostly examined offline, but this study verified that online news comments can also be contagious. Third, we proposed a login policy using SNS accounts and validated its effect empirically. Considering the current popularity of SNS, research involving identifiability through SNS accounts is appropriate and timely. Fourth, unlike preceding studies that relied on secondary data, we conducted an experiment to use as a research method so that we could analyze the direct effects of the proposed moderation policies. Also, the through controlling internal factors, we were able to increase internal validity. Finally, we conducted a longitudinal experiment so that sequential changes in the degree of deliberative discussion of news comments over time could be observed and discussed.

From a practical viewpoint, the results of this study have interesting implications. According to our results, the quality of the first comment (i.e., seed comment) impacts the degree of deliberative discussion in the comments that follow. This result implies that Internet news sites could enhance the degree of deliberative discussion among commenters by placing comments of high quality at the top of the comment feed. However, to mitigate the criticism of manipulation of public opinion, rather than constructing an artificial seed comment, it would be preferable to develop an evaluation system that measures the quality of comments and automatically places the highest-quality comments at the top of the list.

Another implication of the current study is that a newspaper could enhance the degree of deliberative discussion present in comment systems by requiring a login using SNS accounts for identification. In our study, this was especially true for male participants. The effect of eliminating anonymity for this group was as effective as providing high-quality seed comments. Thus, this would likely be the simplest way to enhance the degree of the deliberative discussion. However, this intervention would come at a price. If people feel nervous about social evaluation, they may write fewer comments (Pissarra & Jesuino, 2005), and the feeling of online surveillance may threaten the flow of free speech and public interaction online (Dahlberg, 2001).

These implications suggest promising avenues for future research. First, it would be useful to develop an evaluation mechanism to measure the quality of comments. One way of assessing comments is to use social buttons. Although such buttons—like, recommend, and share buttons—have been used to rate comments on new sites and social media, they may be of little use in their current form. For our purposes, they are not suitable because they offer too little choice to indicate reactions to comments. There are at least two perspectives concerning the value of the information in comments—one utilitarian and the other hedonic (Suh, et al. 2016). As it stands now, a reader who thinks a comment is important and another reader of the same comment who is amused by it have only the like button as a choice. If buttons are to be used to measure both the informational and hedonic qualities of a comment, social buttons should be improved to permit proper assessment (Suh, et al. 2016).

Furthermore, researchers might consider the detailed investigation of gender differences concerning contagion effects under conditions of anonymity. The current study found significant gender effects, but it is not clear why females and males behave differently when they are exposed to low-quality comments under anonymous conditions. This phenomenon could definitely use a more theoretical examination.

## Acknowledgements

The authors would like to thank the anonymous reviewers for their helpful comments and suggestions for improving the quality of this paper. We also acknowledge the valuable help of Garam Hong for carrying out our experiment. This work was supported by the National Research Foundation of Korea Grant funded by the Korean Government (NRF-2013S1A5A2A03044892).

## References

Anderson, C. & Thompson, L. L. (2004). Affect from top down: How powerful individuals’ positive affect shapes negotiators. Organization Behavior and Human Decision Processes, 95(2), 125-139.

Belkin, L. Y. (2009). Social contagion in the electronic communication context: Conceptualizing dynamics and implications of electronic emotional encounters in organizations. Journal of Organizational Culture, Communications and Conflict, 13(2), 105-122.

Berlyne, D. E. (1970). Novelty, complexity, and hedonic value. Perception & Psychophysics, 8(5a), 279-286.

Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A theory of fads, fashion, custom and cultural change as information cascades. Journal of Political Economy, 100(5), 992–1026.

Bock, G., Zmud, R. W., Kim, Y., & Lee, J. (2005). Behavioral intention formation in knowledge sharing: Examining the roles of extrinsic motivators, social-psychological forces, and organizational climate. MIS Quarterly, 29(1), 87-111.

Brookfield, S. D. & Preskill, S. (2005). Discussion as a way of teaching: Tools and techniques for democratic classrooms (2nd ed.). San Francisco, CA: Jossey-Bass.

Burkhalter, S., Gastil, J., & Kelshaw, T. (2002). A conceptual definition and theoretical model of public deliberation in small face-to-face groups. Communication Theory, 12(4), 398-422.

Byeon, S., & Chung, S. (2012). The chilling effect of anonymity and organizational membership in social network service. Korean Journal of Journalism & Communication Studies, 56(4), 105-132.

Chambers, S. (2003). Deliberative democratic theory. Annual Review of Political Science, 6(1), 307- 326.

Chen, B. C., Guo, J., Tseung, B., & Yang J. (2011). User reputation in a comment rating environment. In Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 159-167). New York, NY: ACM.

Christopherson, K. M. (2007). The positive and negative implications of anonymity in Internet social interactions: “On the Internet, nobody knows you’re a dog.” Computers in Human Behavior, 23(6), 3038-3056.

Cialdini, R. B., Reno, R. R., & Kallgren, C. A. (1990). A focus theory of normative conduct: Recycling the concept of norms to reduce littering in public places. Journal of Personality and Social Psychology, 58(6), 1015-1026.

Coleman, S. & Gotze, J. (2001). Bowling together: Online public engagement in policy deliberation. London: Hansard Society.

Connolly, T., Jessup, L. M., & Valacich, J. S. (1990). Effects of anonymity and evaluative tone on idea generation in computer-mediated groups. Management Science, 36(6), 689-703.

Coviello, L., Sohn, Y., Kramer, A. D. I., Marlow, C., Franceschetti, M., Christakis, N. A., & Fowler, J. H. (2014). Detecting Emotional Contagion in Massive Social Networks. Plos One, 9(3), 1-6.

Dahlberg, L. (2001). Computer-mediated communication and the public sphere: A critical analysis. Journal of Computer-Mediated Communication, 7(1).

DeLong, D. W., & Fahey, L. (2000). Diagnosing cultural barriers to knowledge management. Academy of Management Executive, 14(4), 118-127.

Diakopoulos, N., & Naaman, M. (2011). Towards quality discourse in online news comments. In Proceedings of the ACM 2011 Conference on Computer Supported Cooperative Work (pp. 133-142). New York, NY: ACM.

Dipboye, R. L. (1977). Alternative approaches to deindividuation. Psychological Bulletin, 84(6), 1057-1075.

Dubrovsky, V. J., Kiesler, S., & Sethna, B. N. (1991). The equalization phenomenon: Status effects in computer-mediated and face-to-face decisionmaking groups. Human-Computer Interaction, 6(2), 119-146.

Dutwin, D. (2002). Can people talk politics? A study of deliberative democracy (Doctoral dissertation). University of Pennsylvania, Philadelphia, PA.

Fishkin, J. S., & Luskin, R. C. (2005). Experimenting with a democratic ideal: Deliberative polling and public opinion. Acta Politica, 40(3), 284- 298.

Gastil, J. (2008). Political communication and deliberation. Thousand Oaks, CA: Sage.

Goldberg, D., Nichols, D., Oki, B. M., & Terry, D. (1992). Using collaborative filtering to weave an information tapestry. Communications of the ACM, 35(12), 61-70.

Guadagno, R. E., Cialdini, R. B., & Evron, G. (2010). Storming the servers: A social psychological analysis of the first Internet war. Cyberpsychology, Behavior, and Social Networking, 13(4), 447-453.

Gutmann, A., & Thompson, D. (2009). Why deliberative democracy? Princeton, NJ: Princeton University Press.

Habermas, J. (1996). Between facts and norms: Contributions to a discourse theory of law and democracy. Cambridge, MA: The Massachusetts Institute of Technology Press.

Halpern, D., & Gibbs, J. (2013). Social media as a catalyst for online deliberation? Exploring the affordances of Facebook and YouTube for political expression. Computers in Human Behavior, 29(3), 1159-1168.

Heal, G., & Kunreuther, H. (2010). Social reinforcement: Cascades, entrapment, and tipping. American Economic Journal: Microeconomics, American Economic Association, 2(1), 86-99.

Heanue, A., Kranich, N., & Willingham, T. (2003). Public forums for today’s critical issues. American Libraries, 43(1), 68-89.

Hite, D. M., Voelker, T., & Robertson, A. (2014). Measuring perceived anonymity: The development of a context independent instrument. Journal of Methods and Measurement in the Social Sciences, 5(1), 22- 39.

Howard, D. J., & Gendel, C. (2001). Emotional contagion effects on product attitudes.

Journal of Consumer Research, 28, 189-201.

Hron, A., & Friedrich, H. F. (2003). A review of webbased collaborative learning: Factors beyond technology. Journal of Computer Assisted Learning, 19(1), 70– 79.

Hsu, C., Khabiri, E., & Caverlee, J. (2009). Ranking comments on the social web. In Proceedings 2009 International Conference on Computational Science and Engineering, 4, 90–97.

Hwang, S. G. (2008). A constitutional study on the mandatory personal identification on the Internet. Chonnam Law Review, 25(1), 7-37.

Jackman, S., & Sniderman, P. M. (2006). The limits of deliberative discussion: A model of everyday political arguments. The Journal of Politics, 68(2), 272-283.

Jankowski, N., & van Selm, M. (2000). The promise and practice of public debate in cyberspace. In

K.L. Hacker, and J. van Dijk (Eds.), Digital democracy: Issues of theory and practice (pp. 149-165). Thousand Oaks, CA: Sage.

Jeong, B. (2010). A analysis over user’s perception and intension of Internet malicious message uploading. Journal of Political Communication, 16, 345-381.

Jessup, L. M., Connolly, T., & Galegher, J. (1990). The effects of anonymity on GDSS group process with an idea-generating task. MIS Quarterly, 14(3), 313-321.

Jessup, L. M., & Tansik, D. A. (1991). Decision making in an automated environment: The effects of anonymity and proximity with a group decision support systems. Decision Science, 22(2), 266-279.

Keizer, K., Lindberg, S., & Steg, L. (2008).The spreading of disorder. Science, 322(5908), 1681-85.

Kiesler, S., Siegel, J., & McGuire T. W. (1984). Social psychological aspects of computer-mediated communication. American Psychologist, 39(10), 1123-1134.

Kilner, P. G., & Hoadley, C. M. (2005). Anonymity options and professional participation in an online community of practice. Proceeding CSCL ‘05 Proceedings of the 2005 Conference on Computer Support for Collaborative Learning (pp. 272-280). Taipei, Taiwan: International Society for the Learning Sciences.

Kim, Y. J., & Han, J. (2014). Why smartphone advertising attracts customers: A model of web advertising, flow, and personalization. Computers in Human Behavior, 33, 256-269.

Kim, J. K., & Kim, D. H. (2008). Motivation of reading and writing Internet reply and satisfaction of college Internet reply users. Cybercommunication Academic Society, 25(4), 5-47.

Kim, E., & Sun, Y. (2006). The effect of replies in Internet news on the audience. Korean Journal of Journalism & Communication Studies, 50(4), 33-64.

Knight, J., & Johnson, J. (1994). Aggregation and deliberation: On the possibility of democratic legitimacy. Political Theory, 22(2), 277-296.

Korea Internet and Security Agency. (2011). Survey on the Internet ethical culture. Retrieved from . http://download.kpf.or.kr/MediaPds/GJYA NUGBJOBEHTT.pdf

Kwon, K. H., & Gruzd, A. (2017). Is aggression contagious online? A case of swearing on

Donald Trump’s campaign videos on YouTube. Proceedings of the 50th Hawaii International Conference on System Sciences. Retrieved from https://aisel.aisnet.org/cgi/viewcontent.cgi?arti cle=1264&context=hicss-50 268, 2165-2174.,\

C., Zube, P., Lee, J., Park, C. H., & Johnston, E. (2014). Crowdsourcing civility: A natural experiment examining the effects of distributed moderation in online forums. Government Information Quality, 31(2), 317-326.

Landis, J. K., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. Biometrics, 33(1), 159-174.

Le Bon, G. (1895). The crowd: A study of the popular mind. Paris, France: Psychologie des Foules.

Lee, H. (2005). Behavioral strategies for dealing with flaming in an online forum. The Sociological Quarterly, 46(2), 385-403.

Lee, J. K. (2015). Research framework for AIS Grand vision of the Bright ICT initiative. MIS Quarterly, 39(2), iii-xii.

Levy, D., & Nail, P. (1993). Contagion: A theoretical and empirical review and reconceptualization. Genetic, Social, and General Psychology Monographs, 119(2), 233-284.

Li, D., Niu, J., Qiu, M., & Liu, M. (2014). Sentiment analysis on Weibo data. In Proceedings of Computing, Communications and IT Applications Conference (ComComAp), 2014 (pp. 249-254). IEEE.

Mason, W., & Suri, S. (2012). Conducting behavioral research on Amazon’s mechanical turk. Behavior Research Methods, 44(1), 1-23.

Min, S. J. (2007). Online vs. face-to-face deliberation: Effects on civic engagement. Journal of Computer-Mediated Communication, 12(4), 1369-1387.

Moy, P., & Gastil, J. (2006). Predicting deliberative conversation: The impact of discussion networks, media use, and political cognitions. Political Communication, 23(4), 443-460.

Neumann, R., & Strack, F. (2000). Mood contagion: Automatic transfer of mood between persons. Journal of Personality and Social Psychology, 79(2), 211-223.

Nooy, W. D., Mrvar, A., & Batagelj, V. (2011). Exploratory social network analysis with Pajek Cambridge, UK: Cambridge University Press.

Omernick, E., & Sood, S. O. (2013). The impact of anonymity in online communities. Social Computing (SocialCom), 2013 International Conference on IEEE, (pp. 526– 535). IEEE.

Pew Research Center. (2013). 12 trends shaping digital news. Retreived from http://www.pewresearch.org/facttank/2013/10/16/12-trends-shaping-digitalnews/

Pew Research Center. (2015). State of the news media 2015. Retrieved from http://www.pewresearch.org/topics/state-ofthe-news-media

Pfitzmann, A., & Hansen, M. (2010). A terminology for talking about privacy by data minimization: Anonymity, unlinkability, undetectability, unobservability, pseudonymity, and identity management. Retreived from http://dud.inf.tudresden.de/Anon\_Terminology.shtml

Pfitzmann, A., & Köhntopp, M. (2001). Anonymity, unobservability, and pseudonymity: A proposal for terminology. In H. Federrath (Ed.), Proceedings Workshop on Design Issues in Anonymity and Unobservability, vol. 2009 of Lecture Notes in Computer Science, Springer-Verlag.

Pinsonneault, A., & Heppel, N. (1997). Anonymity in group support systems research: A new conceptualization, measure, and contingency framework. Journal of Management Information Systems, 14(3), 89-108.

Pissarra, J., & Jesuino, J. C. (2005). Idea generation through computer-mediated communication: The effects of anonymity. Journal of Managerial Psychology, 20(3), 275-291.

Price, V., & Cappella, J. N. (2002). Online deliberation and its influence: The electronic dialogue project in campaign 2000. IT & Society, 1(1), 303-329.

Purcell, K., Mitchell, A., Rosenstiel, T., & Olmstead, K. (2010). Understanding the participatory news consumer. Pew Internet & American Life Project, 1(1), (19-21).

Reader, B. (2012). Free press vs. free speech? The rhetoric of “civility” in regard to anonymous online comments. Journalism & Mass Communication Quarterly, 89(3), 493-513.

Resnick, P. (2001). Beyond bowling together: Sociotechnical capital. in J. Carroll (Ed.), HCI in the New Millennium. Boston, MA: Addison-Wesley.

Santana, A. D. (2014). Virtuous or vitriolic: The effect of anonymity on civility in online newspaper reader comment boards. Journalism Practice, 8(1), 18-33.

Schoenewolf, G. (1990). Emotional contagion: Behavioral induction in individuals and groups. Modern Psychoanalysis, 15, 49-61

Shepherd, M. M., Brigges, R. O., Reining, B. A., Yen, J., & Nunamaker, J. F. (1996). Invoking social comparison to improve electronic brainstorming: Beyond anonymity. Journal of Management Information Systems, 12(3), 155- 170.

Siegel, J., Dubrovsky, V., Kiesler, S., & McGuire, T. W. (1986). Group processes in computermediated communication. Organizational Behavior and Human Decision Processes, 37(2), 157-187.

Stephenson, G. M., & Fielding, G. T. (1971). An experimental study of the contagion of leaving behavior in small gatherings. Journal of Social Psychology, 84(1), 81- 91.

Stice, E., Schupak-Neuberg, E., Shaw, H. E., & Stein, R. I. (1994). Relation of media exposure to eating disorder symptomatology: An examination of mediating mechanisms. Journal of Abnormal Psychology, 103(4), 836-840.

Strandberg, K., & Berg, J. (2013). Online readers’ comments Democratic conversation platforms or virtual soapboxes?. Comunicao e Sociedade - Communication & Society, 23, 132–152.

Suh, K.-S., Suh, E.-K., Lee, S., Lee, H., Hong, G., & Yoo, S. M. (2016). Design and evaluation of social buttons for news comments. The Pacific-Asia Conference on Information Systems 2016.

Suler, J. (2004). The online disinhibition effect. CyberPsychology & Behavior, 7(3), 321-326.

Tsvetkova, M., & Macy, M. W. (2014). The Social Contagion of Generosity. Plos One, 9(2), 1-9.

Tsvetkova, M., & Macy, M. W. (2015). The social contagion of antisocial behavior.

Sociological Science, 2(Feb), 36-49.

Tsvetkova, M. (2015). The contagion of social behavior (Doctoral dissertation). Cornell University, Ithaca, NY.

Valacich, J. S., Dennis, A. R., & Connolly, T. (1994). Idea generation in computer- based groups: A new ending to an old story. Organization Behavior and Human Decision Processes, i(3), 448-467.

WAN-IFRA. (2016). The 2016 global report on online commenting: Chapter 1: The problem with comments. Retrieved from http://blog.wanifra.org/print/2016/10/17/the-2016

Weber, P. (2013). Discussions in the comments section: Factors influencing participation and interactivity in online newspapers’ reader comments. New Media & Society, 16(6), 941- 957.

Wilson, J. Q., & Kelling, G. L. (1982). Broken windows. In R. G. Roger & G. P. Alpert (Eds.), Critical issues in policing: Contemporary readings (7th ed.). Long Grove: IL: Waveland.

Wright, S. (2006). Government-run online discussion fora: Moderation, censorship and the shadow of control. Political Studies Association, 8(4), 550-568.

Yang, H. S. (2008). The effects of the opinion and quality of user posting on Internet news readers attitude toward the news issue. Korean Journal of Journalism & Communication Studies, 52(2), 254-281.

Yin, D., Bond, S., & Zhang, H. (2014). Effect of discrete emotions on perceived helpfulness of online reviews. MIS Quarterly, 38(2), 539-560.

Zhao, S., Grasmuck, S., & Martin, J. (2008). Identity construction on Facebook: Digital empowerment in anchored relationships. Computers in Human Behavior, 24, 1816-1836.

Zimbardo, P. G. (1969). The human choice: Individuation, reason and other versus deindividuation, impulse, and chaos. In W. T. Arnold and D. Levin (Eds.), Nebreska symposium on motivation 17 (pp. 237-307), Lincoln: NE: University of Nebraska Press.

## Appendix

Table A1. Examples of Seed Comments and the Corresponding News

<table><tr><td>News</td><td>High-quality seed comment</td><td>Low-quality seed comment</td></tr><tr><td>News 1</td><td>A thriving economy consists of thriving companies and people, not just thriving chaebols, The government can control companies to a certain extent, but people&#x27;s hearts are impossible to control, especially when they turn away from you. Ms. President, please adhere to principles and values.</td><td>Fuck. I was so ready to start the day happily after eating a delicious breakfast, but as soon as I saw her fucking face, my day got ruined forever, goddammit. Please put a warning sign in front of this article. I really want to throw an egg in her face.</td></tr><tr><td>News 2</td><td>There is a need for a practical diplomatic policy with both the U.S. and China. We need to use China as a lever to pressure both North Korea and Japan. We should be friendly to China without forsaking the U.S. Because the U.S. is the only country that can keep everyone in check.</td><td>I bet your ass feels restless, you bitch. Soon the day will come when you will get shot. Bang! Bang! I&#x27;ve never seen such a China-friendly government like this fucking one. Does anyone have a brain? Fuckers.</td></tr><tr><td>News 3</td><td>I don&#x27;t think we need to treat a country that violated the Armistice Agreement with respect. Our government should also strike for real this time. Also, this shouldn&#x27;t be public knowledge.</td><td>Fucking kill those sons of bitches! Let&#x27;s kill everything that&#x27;s alive above the  $38^{th}$  parallel. Put fucking photos of Kim right next to the loudspeakers. I bet North Korean bastards will stop shooting out of fear that they might shoot their dear leader&#x27;s piggy face.</td></tr></table>

## News Item 1: President Park Decides upon Special Pardons through Temporary Cabinet Council

On the 13th, President Park will hold a temporary cabinet council in the Blue House to complete a special pardons list to celebrate the 70th anniversary of Korea’s independence. The list of special pardons for businessmen seems shorter than expected. The only head of a conglomerate on the list is SK Group Chairman Chey Tae-won. The rest of the list includes 2 million people who are traffic law violators and convicts who committed crimes of desperation to stay alive. This excludes corrupt politicians. This is the second time Park has granted pardons during her time in office. In her opening statement, Park will explain the meaning of special pardons as a gesture of the development of state and national unification. She will also finalize the list. The Blue House said the Minister of Justice, Kim Hyun-woong, will announce the list at the Seoul Government Complex after the cabinet council. The discussion of special pardons started at last month’s chief secretary’s meeting, where Park said, “there is a need for special pardons for the development of state and national unification.” She ordered a review of potential subjects. After that, the Ministry of Justice, the National Police Agency, the Ministry of Strategy and Finance, the Ministry of Government Administration, and the Ministry of Home Affairs started the list. Last month they chose a selection committee and began evaluating the proposed list and later reported it to Park. Because Park has a strict standard for pardoning conglomerate heads, the list of businessmen to receive special pardons is a short one. In her last presidential election pledge, she promised to strengthen punishment for embezzlement and limit the special pardons for serious crimes of CEOs and major shareholders. Also, Lotte Group’s recent family management dispute worsened public opinion toward conglomerates, and that probably will lead to a shorter special pardons list for businessmen. SK Group Chairman Chey Tae-won has served 2 years and 7 months of a 4-year sentence, which is the longest sentence served by the head of a conglomerate. Because he has already served more than a third of his sentence, he was included in the special pardons list. Even if he is pardoned, he is unlikely to be reinstated. Chey is serving time because of embezzlement. If he is not reinstated, he will not be able to recover his position as the director of the board. Hanwha Group’s Chairman Kim Seung-yon, who was sentenced to 3 years in prison and 5 years of probation, was excluded from the list because he already been pardoned twice. Gu Bon-sang, the former LIG Nex1 vice chairman, and Gu Bon-yeop, the former LIG Construction vice president, are brothers who are serving time for issuing fraudulent commercial paper valued at 180 billion won. They are unlikely to be pardoned because of public opinion. However, because special pardons are a part of the president’s exclusive power, there is a chance that when the list is announced it could have some unexpected names. Park’s first special pardons were granted at the beginning of last year. At the time, 2,896,499 traffic law violators and 5,925 convicts who committed crimes of desperation were pardoned.

## News Item 2: President Park to Visit China Next Month for the 70th Commemoration of the End of WWII

President Park will visit Beijing on September 3rd to attend the 70th commemoration of the defeat of the Japanese and Fascism. However, according to the Blue House, it’s uncertain if Park will attend the military parade that shows off Chinese military power. On the 20th, Senior Presidential Secretary for Foreign Affairs Ju Chul-ki announced to the media that Park will attend China’s commemoration. Ju said Park was invited by Chinese President Xi Jinping to visit China from September 2nd through September 4 to attend the commemoration of the end of World War II. The ceremony will take place on Thursday, September 3rd, in Beijing.

## News Item 3: Military Moves Direct Fire Weapon to Defend Against Possible Attack of the Enemy

The South Korean military has gone on its highest level of security alert and increased the fire power in the area of the latest loudspeaker broadcasting campaign. The tension between the North and the South is heightening near the border as the possibility of a North Korean attack grows. The military said on the 11th, “Yesterday at 5 p.m., we started an intermittent broadcasting campaign and raised the security alert along the western and central front. We’ve increased the number of troops on the front line and reduced the break time. We also moved the division’s direct fire weapons in case the enemy attacks the loudspeakers.” After the sinking of the ROK’s Cheonanham in 2010, South Korea announced on May 24th its resumption of the loudspeaker broadcasting campaign. North Korea threatened to attack the broadcasting site as a response. The South Korean military said, “Since we have methods to guard against any provocations of North Korea and to fight back, if North Korea attacks the site, we will counterattack under our righ of self-defense.” The military stepped up its surveillance in the area where the broadcasting campaign is taking place by using video surveillance and unmanned reconnaissance drones equipped with forward-looking infrared cameras. The military also moved up TOW anti-tank missiles and anti-aircraft weapons in case there is an attack from the North Korean guard posts. Also in case of North Korean attack by multiple rocket launchers, AN/TPQ36, a weapon-locating radar, and K9 self-propelled artillery have been placed in the area. K4 grenade launchers, K3 heavy machine guns, and 90mm recoilless rifles have been placed even in the areas where the broadcasting campaign hasn’t started but loudspeakers are in place.

Table A2. Coding Scheme

<table><tr><td>Dimension</td><td>Sub-division</td><td>Scheme</td><td>Scoring</td></tr><tr><td rowspan="6">Rationality</td><td>Justification</td><td>The comment includes at least one piece of evidence for the commenter&#x27;s argument</td><td>Included: 1, Not included: 0</td></tr><tr><td rowspan="5">Level of evidence</td><td>The comment includes accurate facts or external sources as evidence of the argument</td><td rowspan="5">At least one evidence included: 1, Not included: 0</td></tr><tr><td>The comment includes general facts or common sense as evidence for the argument.</td></tr><tr><td>The comment includes parallels or comparisons as evidence for the argument.</td></tr><tr><td>The comment includes anecdotes (reality-based, hypothetical) as evidence for the argument.</td></tr><tr><td>The comment includes personal experience as evidence for the argument.</td></tr><tr><td rowspan="3">Relevance</td><td rowspan="3">Level of relevance</td><td>The comment is directly relevant to the news topic.</td><td rowspan="3">Directly: 2, Indirectly: 1, Not Relevant: 0</td></tr><tr><td>The comment is indirectly relevant to the news topic.</td></tr><tr><td>The comment is not relevant to the news topic.</td></tr><tr><td rowspan="4">Politeness</td><td rowspan="4">Incivility and impoliteness</td><td>The comment includes at least one instance of a threat to democracy.</td><td rowspan="3">At least one instance included: 0, Not included: 1 (reversed)</td></tr><tr><td>The comment includes at least one instance of a stereotype.</td></tr><tr><td>The comment includes at least one instance of a threat to other individuals&#x27; rights</td></tr><tr><td>The comment includes at least one instance of rudeness or incivility.</td><td>Included: 0, Not included: 1 (reversed)</td></tr></table>

Table A3. Questionnaire Items for the Quality of Seed Comment

<table><tr><td>Variable</td><td>Dimensions</td><td>Items</td><td>Source</td></tr><tr><td rowspan="13">Quality of seed comment</td><td rowspan="4">Helpfulness</td><td>Is the first comment...</td><td rowspan="4">Yin et al., 2014</td></tr><tr><td>Useful?</td></tr><tr><td>Informative?</td></tr><tr><td>Helpful?</td></tr><tr><td rowspan="3">Credibility</td><td>Believable?</td><td rowspan="9">Kim and Han, 2014</td></tr><tr><td>Convincing?</td></tr><tr><td>Credible?</td></tr><tr><td rowspan="3">Entertainment</td><td>Interesting?</td></tr><tr><td>Enjoyable?</td></tr><tr><td>Pleasant?</td></tr><tr><td rowspan="3">Irritation</td><td>Annoying? (reversed)</td></tr><tr><td>Irritating? (reversed)</td></tr><tr><td>Intrusive? (reversed)</td></tr><tr><td rowspan="5">Perceived anonymity</td><td colspan="2">I am confident that others do not know who I am when I write a comment.</td><td rowspan="5">Hite et al., 2014</td></tr><tr><td colspan="2">I believe that my personal identity remains unknown to others.</td></tr><tr><td colspan="2">My comments I wrote cannot be tracked back to my personal identity.</td></tr><tr><td colspan="2">I am easily identified as an individual by others (reversed).</td></tr><tr><td colspan="2">Others are likely to know who I am (reversed).</td></tr></table>

Table A4. ANOVA Results for Manipulation Measurements

<table><tr><td>Dependent Variables</td><td>Source</td><td>Sum of Squares</td><td>df</td><td>Mean Square</td><td>F- Value</td><td>P-Value</td></tr><tr><td rowspan="7">Helpfulness</td><td>Constants</td><td>2110.824</td><td>1</td><td>2110.824</td><td>852.913</td><td>.000</td></tr><tr><td>Seed</td><td>28.700</td><td>1</td><td>2.700</td><td>11.597</td><td>.001</td></tr><tr><td>Identifiability</td><td>1.201</td><td>1</td><td>1.201</td><td>.485</td><td>.487</td></tr><tr><td>Seed X identifiability</td><td>7.855</td><td>1</td><td>7.855</td><td>3.174</td><td>.077</td></tr><tr><td>Error</td><td>329.154</td><td>133</td><td>2.475</td><td></td><td></td></tr><tr><td> $R^2$ </td><td>.100</td><td></td><td></td><td></td><td></td></tr><tr><td>Adjusted  $R^2$ </td><td>.080</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="7">Credibility</td><td>Constants</td><td>1619.700</td><td>1</td><td>1619.700</td><td>800.013</td><td>.000</td></tr><tr><td>Seed</td><td>31.267</td><td>1</td><td>31.267</td><td>15.443</td><td>.000</td></tr><tr><td>Identifiability</td><td>.659</td><td>1</td><td>.659</td><td>.325</td><td>.569</td></tr><tr><td>Seed X identifiability</td><td>2.302</td><td>1</td><td>2.302</td><td>1.137</td><td>.288</td></tr><tr><td>Error</td><td>269.271</td><td>133</td><td>2.025</td><td></td><td></td></tr><tr><td> $R^2$ </td><td>.111</td><td></td><td></td><td></td><td></td></tr><tr><td>Adjusted  $R^2$ </td><td>.091</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="6">Entertainment</td><td>Constants</td><td>1812.912</td><td>1</td><td>1812.912</td><td>1000.607</td><td>.000</td></tr><tr><td>Seed</td><td>16.692</td><td>1</td><td>16.692</td><td>9.213</td><td>.003</td></tr><tr><td>Identifiability</td><td>1.081</td><td>1</td><td>1.081</td><td>.597</td><td>.441</td></tr><tr><td>Seed X identifiability</td><td>.112</td><td>1</td><td>.112</td><td>.062</td><td>.804</td></tr><tr><td>Error</td><td>240.971</td><td>133</td><td>1.812</td><td></td><td></td></tr><tr><td> $R^2$ </td><td>.067</td><td></td><td></td><td></td><td></td></tr></table>

Table A4. ANOVA Results for Manipulation Measurements

<table><tr><td></td><td>Adjusted R2</td><td>.046</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="7">Irritation</td><td>Constants</td><td>2668.501</td><td>1</td><td>2668.501</td><td>1258.705</td><td>.000</td></tr><tr><td>Seed</td><td>69.910</td><td>1</td><td>69.910</td><td>32.976</td><td>.000</td></tr><tr><td>Identifiability</td><td>2.052</td><td>1</td><td>2.052</td><td>.968</td><td>.327</td></tr><tr><td>Seed X identifiability</td><td>2.320</td><td>1</td><td>2.320</td><td>1.094</td><td>.297</td></tr><tr><td>Error</td><td>281.965</td><td>133</td><td>2.120</td><td></td><td></td></tr><tr><td>R2</td><td>.205</td><td></td><td></td><td></td><td></td></tr><tr><td>Adjusted R2</td><td>.187</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="7">Perceived anonymity</td><td>Constants</td><td>2891.530</td><td>1</td><td>2891.530</td><td>1818.271</td><td>.000</td></tr><tr><td>Seed</td><td>.088</td><td>1</td><td>.088</td><td>.055</td><td>.814</td></tr><tr><td>Identifiability</td><td>21.605</td><td>1</td><td>21.605</td><td>13.586</td><td>.000</td></tr><tr><td>Seed X identifiability</td><td>1.249</td><td>1</td><td>1.249</td><td>.786</td><td>.377</td></tr><tr><td>Error</td><td>211.505</td><td>133</td><td>1.590</td><td></td><td></td></tr><tr><td>R2</td><td>.097</td><td></td><td></td><td></td><td></td></tr><tr><td>Adjusted R2</td><td>.077</td><td></td><td></td><td></td><td></td></tr></table>

Table A5. Regression Results with Control Variables

<table><tr><td>D.V.I.V.</td><td>(1)Rationality</td><td>(2)Relevance</td><td>(3)Politeness</td><td>(4)Overall</td></tr><tr><td>DIdentifiability</td><td>0.184***(5.105)</td><td>0.124***(3.759)</td><td>0.121***(3.255)</td><td>0.230***(6.493)</td></tr><tr><td>DSeed</td><td>0.121***(3.290)</td><td>0.138***(4.094)</td><td>0.236***(6.219)</td><td>0.266***(7.335)</td></tr><tr><td>DSeed X DIdentifiability</td><td>0.033(0.600)</td><td>0.066(1.334)</td><td>-0.101*(-1.813)</td><td>-0.001(-0.024)</td></tr><tr><td>Privacy concern</td><td>0.034***(2.938)</td><td>-0.001(-0.082)</td><td>-0.019(-1.576)</td><td>0.008(0.678)</td></tr><tr><td>Social comparison</td><td>-0.041***(-2.695)</td><td>-0.057***(-4.096)</td><td>-0.000(-0.010)</td><td>-0.053***(-3.524)</td></tr><tr><td>Curiosity aboutothers&#x27; thought</td><td>0.029**(2.110)</td><td>0.054***(4.231)</td><td>0.010(0.697)</td><td>0.050***(3.658)</td></tr><tr><td>Political propensity</td><td>0.045***(2.708)</td><td>0.047***(3.151)</td><td>0.042**(2.465)</td><td>0.072***(4.438)</td></tr><tr><td>News reading time</td><td>0.001**(2.456)</td><td>0.000(0.068)</td><td>-0.001**(-2.166)</td><td>0.000(0.157)</td></tr><tr><td>Ratio of reading political news</td><td>0.002**(2.384)</td><td>-0.000(-0.440)</td><td>-0.002***(-2.967)</td><td>-0.000(-0.586)</td></tr><tr><td>Number of comments read per 10news item</td><td>-0.011**(-2.551)</td><td>-0.002(-0.432)</td><td>-0.005(-1.151)</td><td>-0.009**(-2.254)</td></tr><tr><td>Number of comments written per 10news item</td><td>-0.019***(-2.975)</td><td>0.007(1.124)</td><td>-0.001(-0.137)</td><td>-0.007(-1.138)</td></tr><tr><td>News fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>5,611</td><td>5,611</td><td>5,611</td><td>5,611</td></tr><tr><td>R-squared</td><td>0.149</td><td>0.286</td><td>0.103</td><td>0.181</td></tr></table>

Table A5. Regression Results with Control Variables

The dependent variable is the degree of deliberative discussion in four aspects: rationality, relevance, politeness, and the sum of their normalized values. DIdentifiability is a dummy variable that equals 1 for those who post comments with their Facebook accounts and zero if posted anonymously. DSeed is a dummy variable that equals 1 for those who received a high-quality seed and zero otherwise. The third variable denotes the interaction between these two treatment variables. Others are control variables. Fixed effects were controlled for each news story. Numbers in parentheses are OLS t statistics. \*\*\*, \*\*, and \* denote significance at the 1%, 5%, and 10% levels, respectively.

## About the Authors

Kil-Soo Suh is a professor of Information Systems at Yonsei University in Seoul, Korea. He holds a BA in business administration from Yonsei University, an MBA from the Kelley School of Business at Indiana University, and a PhD in management information systems from the Kelley School of Business at Indiana University. His research interests are in the areas of interface design for electronic commerce, communication media, virtual reality, and implementation of information. His work has been published in various journals including Behaviour and IT, Decision Support Systems, Information and Management, Information Systems Research, International Journal of Electronic Commerce, and MIS Quarterly.

Seongwon Lee is a research professor at Dankook University. She holds her PhD in management information systems from the School of Business at Yonsei University in Seoul, Korea. She has 10 years of experience as an IT systems and database engineer. Her research interests focus on SNS strategy, Big Data analysis, and machine learning. Her work has been published in the Asia Pacific Journal of Information Systems and Information Systems Review. Seongwon Lee is the corresponding author of this research.

Eung-Kyo Suh is an assistant professor at the Graduate School of Business at Dankook University. He received his PhD in management information systems from the School of Business at Yonsei University in Seoul, Korea. He has 10 years of IT strategy field experience in multiple industries. His current research interests are in the areas of the social and organizational aspects of decision support technologies, electronic commerce, and human-computer interaction in information systems. His work has been published in various journals including MIS Quarterly and Information and Management.

Hoseong Lee is an assistant manager of the Army Facilities Management Department at the Korea Land & Housing Corporation. He received his master’s degree in management information systems and his bachelor’s degree in library & information science from Yonsei University in Seoul, Korea. His current interests are digital marketing strategy in E-commerce, and the classification and public utilization of real estate information.

Jaehoon Lee is a senior lecturer at the School of Banking and Finance at the University of New South Wales, Australia. He earned his PhD in finance from the University of Illinois at Urbana-Champaign. His research focuses on asset pricing and risk premiums, and his research has appeared in the Journal of Financial Economics and the Journal of Financial and Quantitative Analysis.
