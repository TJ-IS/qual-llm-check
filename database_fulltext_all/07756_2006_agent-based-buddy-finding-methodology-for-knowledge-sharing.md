---
otero_id: 7756
otero_key: "BSQ5BJWZ"
title: "Agent-based buddy-finding methodology for knowledge sharing"
authors: "Xiaoqing Li; Ali R. Montazemi; Yufei Yuan"
year: "2006"
journal: "Information & Management"
doi: "10.1016/j.im.2005.07.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Agent-based buddy-finding methodology for knowledge sharing

Xiaoqing Li <sup>a,1</sup>, Ali R. Montazemi <sup>b,\*</sup>, Yufei Yuan

<sup>a</sup> Department of MIS, College of Business and Management, University of Illinois at Springfield, One University Plaza, MS-115 Springfield, IL 62703-5407, USA

<sup>b</sup> Michael G. DeGroote School of Business, McMaster University, Hamilton, Ont. L8S 4M4, Canada

Received 12 December 2003; received in revised form 26 October 2004; accepted 28 July 2005 Available online 4 October 2005

## Abstract

The Internet provides an opportunity for knowledge sharing among people with similar interests (i.e., buddies). Emails, mailing lists, chat rooms, electronic bulletin boards, newsgroups are ways for identifying buddies. However, manual ways of finding a buddy are time consuming and not generally effective. Collaborative filtering technologies can provide useful information to users based on others’ interests, and software agent technology is a promising tool for finding buddies. Software agents are autonomous and can represent users’ preferences and perform tasks with built-in learning and reasoning capabilities. They can also communicate with one another to exchange information. Here, we define an agent-based buddy-finding methodology. Agents are created to represent users and exchange sample information with possible buddies while assessing the information exchanged. Thus, we present a methodology for developing an agent that identifies a set of buddy-agents using a built-in fuzzy reasoning mechanism to assess the buddy membership of peer agents. Using this, the agents cultivate a dynamic acquaintance list of their peer agents. The methodology was empirically tested in a context involving sharing musical-knowledge. We show that the buddies found by agents are as good as those found manually. © 2005 Elsevier B V All rights reserved

Keywords: Knowledge management; Information sharing; Intelligent agent; P2P; Case-based reasoning; Fuzzy logic

## 1. Introduction

Knowledge is a major driving force for organizational change and wealth creation and ‘‘knowledge management is an increasingly important source of competitive advantage for organizations’’ [20]. However, people often need to exchange ideas and knowledge sharing may be obtained by using electronic messaging systems such as emails, mailing lists, chat rooms and message boards, allowing people to find their ‘‘buddies’’ on the Internet [8]. With the increasing number of users, however, conventional methods suffer from information overload [18,21,54]. Automatic methods could relieve this problem [25]. One automatic technology is collaborative filtering: it recommends useful information based on a buddy’ interests [36]. For example, Firefly (www.firefly.com) uses the opinion of buddies to share knowledge about products such as music, books, Web pages, and restaurants. But the collaborative filtering technology needs a centralized knowledge base to retain the knowledge of all its users. This poses the question of how to deal with a decentralized knowledge base where a large number of users are involved.

This paper discusses an agent-based buddy-finding methodology for a decentralized knowledge-sharing environment and describes the empirical test we performed to evaluate users’ satisfaction with agentfound buddies in sharing knowledge of music.

## 2. Knowledge management

Knowledge is now a major driving force for organizational change and wealth creation, and effec tive knowledge management is an increasingly important source of competitive advantage and a key to the success of modern organizations [29,35]. As a result, companies are now implementing knowledge manage ment processes and its supporting technologies. Knowledge management systems (KMS) are a class of IS developed to support and enhance the organizational processes of knowledge creation, storage/retrieval, transfer and application [2,10]. Recent progress has transformed the processes of management of organiza tional knowledge: various technologies, such as knowledge networks, communities of practice, and virtual communities, are applied to manage organizational resources better, especially that stored in human minds, so-called tacit knowledge [41,56]. The challenge is in sharing tacit knowledge. In the network model of knowledge-management, knowledge remains with the individual who develops and possesses it; it is transferred mainly through person-to-person contact. For example, Hoffman–LaRoche, a pharmaceutical company, developed a knowledge map of its drug approval process [34]. Rather than controlling and directing flows of knowledge, the task of managing knowledge networks is then one of creating accessibility [4]. Informal networks provide critical channels for collective sense-making and shared understandings [31]. Evidence of such efforts can be seen in Japan, where ‘‘talk rooms’’ are established to enable people to meet and converse when they wish [14]. Within organizations, informal networks of employees thus manage and transfer organizational knowledge. People share knowledge and work together to solve problems in ‘‘communities of practice.’’ In many organizations, people set these up to share knowledge and skills, the participants begin using and developing their skills by working together on issues of common interest [47]. The process thus becomes one of social participation [59]; it is a shift in how people find individuals in the organization with knowledge that can be used to solve difficult problems. This is a movement toward the idea that useful knowledge is to be found throughout the organization [13]. Then knowledge transfer goes on between like-minded people rather than flowing from the ‘‘best’’ to the ‘‘less able.’’

Communities of practice are formed over time by individuals with a need to associate themselves with others who are dealing with similar issues and facing similar challenges [33,63]; they have gone beyond faceto-face exchanges to online interactions, shared Web spaces, email lists, discussion forums, and synchronous chats [39]. One of the fast-growing trends today is the virtual team or virtual community: generally a virtual location in which people can meet to socialize, exchange experiences, and enjoy the possibility of establishing relationships without physical presence [27,32,57]. The team crosses time, space, and cultural boundaries and does so effectively [30]. Virtual communities encourage participants to share their knowledge and it is our contention that multi-agent systems can be used effectively in support of knowledge-sharing there.

Peer-to-peer (P2P) systems are becoming increasing popular, as the bandwidth, computational power, and large storage capacity became more readily available to the Internet users [62]. These systems, such as Gnutella (www.gnutella.com), allow users to share information, music, games and other files using decentralized database architecture. The challenge for these users is in finding peers that can best satisfy their needs. Present message routing systems are based on the flooding broadcasting methods with versions like Rumor mongering [44]; each time a user sends a message to the community, the routing method broadcasts the requests to all other users. Most who receive a message either cannot help the sender, because they do not have the information or have no desire to respond (i.e., they are free riders). Adar and Huberman [1] reported that 70% of Gnutella P2P participants are free riders, only consuming resources without contributing. In the Rumor mongering routing method, users broadcast their requests to some randomly selected users; this reduces the communication cost, but may miss relevant peers. The major structural problem with either of these two methods is lack of knowledge of who are best able to respond to a request. To ameliorate this problem, we developed a new methodology that helps the users of P2P systems identify peers (called buddies) likely to satisfy their needs.

## 3. Intelligent agent systems

The agent paradigm and multi-agent systems (MAS) are widely recognized as suitable abstractions for dealing with complex application environments, especially open environments with unpredictable dynamics that make traditional approaches less effective [49]. In these, the structure of the system is capable of dynamic change. In order to achieve the user’s goal, the agent executes autonomously, communicates with other agents or the user, while monitoring the state of its operational environment. Its components are not known before starting the process and they may change over time and be highly heterogeneous [48].

MAS are groups of agents that work as a single system to integrate their functions and to perform large, complex tasks [42]. Each agent needs to collaborate with others and a fundamental requirement of the agent is its ability to coordinate its actions with others [15] and manage dependencies between activities [52]. Many efforts are currently trying to solve this coordination problem for organizations [6,16,17].

One of the basic problems facing designers of open, multi-agent systems for the Internet is the connection issue; i.e., finding the other agents with specific preferences and capabilities [11]. Preference is (meta) knowledge about what types of information would be of use to a requester, both in form (e.g., John follows the price of IBM stock) and in other characteristics (e.g., John wants only free information or John wants stock quotes at least every 35 min). Capability refers to (meta) knowledge about what types of requests can be served by a provider (e.g., Mary can provide the current price of any NASDAQ stock, delayed 15 min, free, at a rate of 10 quotes per minute).

There are basically two kinds of control structures in MAS [38,53]: centralized and decentralized. In the former, all agents communicate their solutions to a central coordinator. The service provider agents advertise their capabilities to the middle agent, which, when it receives a service request, transmits the task to an appropriate agent. This control structure is based on the advertised agents’ capabilities. As in the MAS developed by Pouchard and Walker [45], different agents are distinguished according to their roles and responsibilities. When all the agents’ roles and capabilities are similar or difficult to differentiate, the central control structure will not work. For example, in music fan societies, all users have an interest in and knowledge of music, and their interests and knowledge are constantly changing, making it difficult for a middle agent to keep track of all possible music that would match the changing interests of each user.

MASs are best suited for use in open systems with a large and varying number of agents [58]. Pouchard and Walker contend that the central control agent (CA) may create a bottleneck, since it controls all information exchange for all other agents as the number of users increases. It is believed that the CA can scale up to 100 users and therefore assembly of the right team of agents and their control is of prime importance in the decentralized control structure [12]. There is no middle agent in a decentralized control structure and this means that agents use an acquaintance list to communicate only with a small subset of agents. In the acquaintance model, individual agents contain information on the current capabilities of their peers. For example, PoliTeam is a groupware support system that uses intelligent agent technology and case-based reasoning as a way of sharing information among team members [7]; feedback control relationships are captured in a multi-layered model of organizational memory and transferred to users by agent-facilitators. This approach is based on a system dynamic mode of organizational learning, where the group members constitute a small, finite set with similar needs.

The problem with the present decentralized structure of systems is their need to predetermine the acquaintance list in the large and dynamic network of P2P systems in which the users do not know one another. Our buddy-finding methodology ameliorates this problem by creating a dynamic list of buddies.

## 4. The objective of our investigation

Our basic assumption was that a message sent by agent A1 to find information about a specific stock could be best answered by the agents of investors whose portfolio (case-based) was similar to the portfolio of that agent’s owner. Thus, our objective was to identify agents (buddies) who could best respond to a request of another agent. We assumed that, an agent should first try using methods similar to those that provided answers for similar problems. This is reinforcement learning; it involves a method based on a set of specific processes in which some aspects of the behaviour is given more (or less) prominence in future operations: a reinforcement operator [55]. This specifies how the agent should change its assessment of its buddy-agents. Fig. 1 shows agent A1 sending messages to a number of other agents to help satisfy a request from decision maker D1. The responses from other agents are then presented to D1. Then the trainer D1 notifies agent A1 of the degree of satisfaction (positive or negative reinforcement) with each of the responses. Thus the agent (reinforcement operator) selects buddy-agents based on the decision maker’s preferences.

The idea of a buddy is somewhat vague. Someone can be between a perfect buddy (100% similar) and a completely different (0% similar), depending on the degree of congruence of interests. We used Zadeh’s fuzzy set theory to assess the membership: ‘‘a fuzzy set may be regarded as a class in which there is a gradual progression from membership to non-membership or, more precisely, in which an object may have a degree of membership lying somewhere between unity (full membership) and zero (non-membership)’’ [61]. The buddy membership could be calculated on the basis of a set of criteria when responding to a request. We assume that the two criteria related to knowledge request are:

![](/api/attachments/BSQ5BJWZ/fulltext/images/28c88ecfd6b3d3d5fe352fbdfe3a86ab3b10978cd36d975225ea01dfb7d6ca14.jpg)  
Fig. 1. Reinforcement learning model.

(1) Response time (T): the time for each agent to respond to a request: an agent tends to select buddies that respond quickly to its requests (i.e., minimize T).

(2) Response quality (Q): the quality of the response (recommendation) received; i.e., the match between requested information and recommendations of the agent. We used a range from 0 to 1, where 1 indicated a perfect match and 0 was no match. Thus, the objective was to maximize Q.

The goal attainment for T and Q were specified to be:

$$
\mu (T) = \frac {1}{1 + T ^ {2}}\tag{1}
$$

$$
\mu (Q) = \frac {1}{1 + (Q - 1) ^ {2}}\tag{2}
$$

The goal attainment t, q for all the agents $( x _ { 1 } , x _ { 2 } , x _ { 3 } , \dots )$ was computed as:

$$
(G _ {t} (x _ {i})) = \{(x _ {1}, \mu (t _ {1})), (x _ {2}, \mu (t _ {2})), (x _ {3}, \mu (t _ {3})) \}\tag{3}
$$

$$
\left(G _ {q} \left(x _ {i}\right)\right) = \left\{\left(x _ {1}, \mu \left(q _ {1}\right)\right), \left(x _ {2}, \mu \left(q _ {2}\right)\right), \left(x _ {3}, \mu \left(q _ {3}\right)\right) \right\}\tag{4}
$$

We used a variation of Yager’s fuzzy intersection [60] to assess the aggregate value of goal attainment by each agent. The final membership value (D) for each agent was computed by the fuzzy intersection of all the criteria that they should attain:

$$
\begin{array}{l} D = \{[ x _ {i}, \min _ {j} (G _ {j} (x _ {i}) ^ {w j}) ], \\ \text { where } i = 1, \ldots , n; j = t, q \} \end{array}\tag{5}
$$

Here wt and wq were the weights assigned by the decision maker to the significance of buddy-agents response time and quality of response: the greater the weight, the more important the attribute. For example, a decision maker could state the timeliness of response as wt of 2.3 and quality of response as less significant with a value of wq of 1.2. Then, for three responding agents $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$

$$
\begin{array}{c} (\tilde {G} _ {t} (x _ {i})) ^ {2. 3} = \{(x _ {1}, 0. 7 ^ {2. 3}), (x _ {2}, 0. 5 ^ {2. 3}), (x _ {3}, 0. 4 ^ {2. 3}) \} \\ = \{(x _ {1}, 0. 4 4), (x _ {2}, 0. 2), (x _ {3}, 0. 1 2) \} \end{array}\tag{6}
$$

$$
\begin{array}{c} (\tilde {G} _ {q} (x _ {i})) ^ {1. 2} = \{(x _ {1}, 0. 3 ^ {1. 2}), (x _ {2}, 0. 8 ^ {1. 2}), (x _ {3}, 0. 6 ^ {1. 2}) \} \\ = \{(x _ {1}, 0. 2 4), (x _ {2}, 0. 7 6), (x _ {3}, 0. 5 4) \} \end{array}\tag{7}
$$

Resulting in

$$
D = \{(x _ {1}, 0. 2 4), (x _ {2}, 0. 2), (x _ {3}, 0. 1 2) \}\tag{8}
$$

This means that the degree of buddy memberships for $x _ { 1 } , x _ { 2 } , x _ { 3 }$ were 0.24, 0.2, and 0.12, respectively. We then can select buddies with the highest membership value(s).

The central idea underlying software agents is that of delegation [28,43]. In our methodology, subjects delegate their buddy-finding task to agents, and the agents find buddies for the subjects. The major concern of the users is the quality of the results of the agent recommendation; users expect that agents can find buddies as good as those they themselves would.

Our research question is therefore:

Is the proposed agent-based buddy-finding methodology useful to humans?

We can use the subjects’ manually found buddies as a benchmark in evaluating the effectiveness of the agentbased methodology in testing the research conjecture:

There is no significant perceived difference between the buddies found through the agent methodology and buddies manually identified by the subjects.

## 5. Empirical evaluation in a music selection scenario

The decision environment used here was the selection of buddies who recommend music titles based on a person’s musical interest. We developed an MAS to help music fans find buddies. Our reason for using this decision environment was:

1. There are music fans everywhere and listening to and evaluating music does not require significant training. This made it easier to recruit subjects.

2. There are many well-grounded studies in the retrieval and classification of music (e.g., www.moodlogic.- com; www.musclefish.com [9]) to help support our investigation.

3. Listeners can react to music within seconds. Even untrained listeners can make rapid judgments from quite short elements, including determining the music’s style, performer, beat, complexity, and emotional impact [51]. Therefore, we expected reliable results from people quickly evaluating a song (e.g., MoodLogic users take 30 s to listen to and choose a piece of music). A short time limit was very important in assuring the reliability of the results of our experiments, since a prolonged experiment could tire subjects and make them impatient.

We used MoodLogic (http://www.moodlogic.com) as the provider of the music in our experiment. This is an Internet music application site that evaluates both quantitative and qualitative features of music. MoodLogic states that the most reliable way to know how consumers perceive each song in the music universe is to ask them systematically and repeatedly. Since March 2000, MoodLogic has attracted more than 40,000 music fans of all kinds to listen to songs and evaluate them from a public website called Jaboom (www.jaboom. com). To date, they have gathered metadata concerning consumer perceptions of over 500,000 song titles in the most popular genres, across all relevant decades since the 1950s. MoodLogic has used a set of key information describing each song:

 Song ID tag, song, album and artist names;

 genre, mood, decade, tempo, beat, popularity, vocal style, lead vocal style.

Here, music buddies is the term we have used to denote people with similar music interests and preferences for features such as tempo and beat, as well as qualitative features (such as mood and popularity). The music attribute data from MoodLogic were used in the agent-based buddy-finding methodology.

## 5.1. Music similarity measures

We used case-based reasoning (CBR) methodologies to represent music and to select similar music. SaxEx is a CBR system capable of generating expressive performances of melodies based on examples of human performances [3,37]. SaxEx is used to endow the automatically generated music with the impressiveness that characterizes human performance. The attributes for our musical CBR system are shown in Table 1.

Our CBR system could respond to a question such as, ‘‘What is the similarity between Here by The Beatles and The Story in Your Eyes by The Moody Blues?’’ We measure music similarity by calculating the difference between users’ preferences for different songs. The value of preference descriptors was measured by means of Likert-type scales with a range of 1–9.

## 5.2. Tools

We developed a web-based system which allowed users to perform four major tasks: (i) enter their music attribute preferences; (ii) select their favorite music at a music site and create a music collection; (iii) communicate with other subjects and manually find buddies; and (iv) evaluate the quality of subject- and agent-found buddies.

This test system consisted of three major components: (i) a music browser; (ii) a message board; and (iii) an agent-based buddy-finding system.

## 5.2.1. The music browser

We used a commercial music browser from MoodLogic (http://browser.moodlogic.com/B/So/667/) that enables subjects to search according to their tastes and preferences in music; browsing choices include the following attributes: (i) genre, (ii) decade, (iii) mood, (iv) tempo, (v) beat strength, (vi) vocal arrangement, (vii) vocal style and (viii) popularity. The system allowed subjects to select the attribute value from a dropdown list and to listen to different pieces of music in order to understand their attribute values. Subjects could then rate the importance of each attribute in selecting a piece of music.

Table 1  
Music features classification from MoodLogic

<table><tr><td>Genre</td><td>Mood</td><td>Decade</td><td>Tempo</td><td>Beat</td><td>Popularity</td><td>Vocal style</td><td>Lead style</td></tr><tr><td>Rock</td><td>Upbeat</td><td>1960s</td><td>Very slow</td><td>Light</td><td>Top picks</td><td>Smooth</td><td>Male</td></tr><tr><td>R&amp;B/soul</td><td>Happy</td><td>1970s</td><td>Slow</td><td>Medium</td><td>Popular</td><td>Neutral</td><td>Female</td></tr><tr><td>Country</td><td>Romantic</td><td>1980s</td><td>Medium</td><td>Heavy</td><td>Well known</td><td>Raspy</td><td>Mixed</td></tr><tr><td>Electronica</td><td>Mellow</td><td>1990s</td><td>Fast</td><td></td><td>Split decision</td><td></td><td>Instrumental</td></tr><tr><td>Rap/hip-hop</td><td>Sentimental</td><td>Current</td><td>Very fast</td><td></td><td>Niche</td><td></td><td></td></tr><tr><td>Jazz</td><td>Sad</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New age</td><td>Brooding</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Alternative</td><td>Aggressive</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Easy listening</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reggae</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Folk</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Blues</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gospel</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Latin</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>World</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 5.2.2. Message board

We used a message board provided by ezboard.com to allow subjects to communicate. This board has an important search function that enables a user to find one another.

## 5.2.3. Agent-based buddy-finding system

We developed an MAS using procedures adopted from previous research [22,23,40]. It performed the following functions: (i) selecting buddy-agents; (ii) broadcasting the requirements to other agents; (iii) facilitating local comparison of music by means of the distributed case-based reasoning systems (CBR); and (iv) ranking and presenting music information received from other agents. AGENTBUILDER software (see www.agentbuilder.com for its description) was used to provide a communication protocol among agents. An overview of the proposed system is given in Fig. 2.

To test the stated conjecture, the performance of agent-based buddy-finding methodology was compared with the subject’s manual buddy-finding method. There are many ways for users to communicate and find their buddies on the Internet, such as email, instant messaging, chat rooms, newsgroups, and message boards. With email, users can contact buddies for whom they already have addresses. However, the number of buddies is generally somewhat limited. With instant messaging and chat rooms, users can contact only those who log in at the same time. A very popular peer-to-peer means of sharing music is through a message board (e.g., www.mp3.com); this provides one-to-many asynchronous communication. Its advantages are obvious:

 users can post their requests on the message board and check them whenever they have time (asynchronous communication);

 requests can be seen by all who log in to this message after posting (one-to-many);

 users can search others’ postings and reply to theirs at a different time (asynchronous communication);

 users can search others’ replies.

Message boards such as http://www.mp3.com/ provide music fans with a place to exchange information. We developed our own message board for subjects to share music information. They were asked to choose their top five buddies, based on who offered the best recommendations.

There are many ways to create the profile of user preference in an agent-based system. One can simply ask users to manually enter their preferences for various music attributes. This is a very common and effective method [19].

## 5.3. Subjects

Volunteer subjects were recruited from two undergraduate classes and one graduate class at the University of Illinois. All subjects were MIS major or minor students. Each subject was given five extra bonus points to his or her final grade for completing the tests. Thirty-eight students participated in the experiment, but since four did not complete all the required steps, the total number of subjects in the final evaluation was 34. The subjects were asked to answer three questions about their music-related habits: (i) time spent listening; (ii) money spent on purchasing music CDs per year; and (iii) time spent downloading music from the Internet. The average time spent in listening to music was 2.6 h per day (S.D. = 1.88), average money spent on purchasing music CDs was \$ 4.79 per year (S.D. = 3.22) and the average number of times downloading music from the Internet was 2.2 times per year (S.D. = 2.86). This indicated that subjects had a varying degree of interest in music.

![](/api/attachments/BSQ5BJWZ/fulltext/images/1a410af635efaba5455d5dabb72cbab1768a63bf8cc8b1f5148af7f6082358cf.jpg)  
Fig. 2. An overview of the MAS system in support of music selection.

## 5.4. Data collection

We collected the following data electronically and stored them in a database:

 subjects’ music-related habits;

 subjects’ evaluation of subject-found buddies;

 subjects’ evaluation of mixed buddies from subjectfound buddies and agent-found buddies;

 subjects’ evaluation of songs in three groups: (i) subject-found buddies; (ii) agent- found buddies; and (iii) final selection of buddies;

 subjects’ comments on the evaluation process.

## 5.5. Experimental procedures

1. Subjects were asked to use a weighted-score method to assess the factors that determined their music preferences based on the music attributes presented on http://www.moodlogic.com, using a Likert-type scale of 1–9 (from 1: extremely unimportant to 9: extremely important) for each category (genre, mood, decade, tempo, beat, popularity, lead vocals, vocal style). The relative importance was calculated by dividing each category by the sum of the scores. Within each category, subjects gave preference scores of 1–9 (from 1: do not like at all, to 9: like very much) to each item (e.g., smooth, neutral, and raspy in the category of vocal style).

2. Subjects created their music collections by selecting their favorite music from the music site: subjects were asked to identify their 20 favorite music titles from Moodlogic (www.moodlogic.com).

3. Each subject was asked to announce the music titles from his or her collection of 20 music titles on the message board and to ask for music titles similar to them. Each subject had to provide a recommendation of at least 10 requests from other people on the message board. Recommendations should have been based on the subject’s list of 20 music titles selected in step 2.

4. Based on the recommendation, each subject-selected five subjects as his or her buddies with closest music interests. We call this manual process subject-found buddies. The subject could also add some comments to each selected buddy, indicating his or her perception of the value of the suggestions from that buddy.

5. We compared this ranking with that from the proposed agent-based methodology to see whether the two

rankings were correlated. Subjects assessed the quality of buddies selected by themselves and those selected by our buddy-finding agent methodology. In order to analyze the quality of the results of the agent recommendations, we computed whether there were significant differences between agent-found buddies and subject-found buddies. To this end, subjects were presented with the top five ‘‘subject-found buddies’’ (from step 4) and the top five agent-found buddies in random order. Next, the subjects were asked to assess the buddies using a Likert-type scale of 1–9. The top five buddies from this assessment were called the final subject-selected buddies.

6. We then presented three sets of buddies to the subjects:

 agent-found buddies,

 subject-found buddies,

 final subject-selected buddies.

7. Subjects evaluated the quality of the three possible groups of buddies and provided their degree of satisfaction with the music in each set. Since our major concern was the quality of agent recommendation, we needed to know to what extent we could trust the recommendation from the agent. We therefore compared the merits of agent-found buddies with those that subjects selected themselves (subject-found buddies).

Table 2  
Notation of abbreviations

<table><tr><td>Abbreviation</td><td>Definition</td><td>Explanation</td></tr><tr><td> $B_s$ </td><td>Subject-found buddies</td><td>Buddies that the subject got from the message board through the manual method (step 3 of experimental procedures), such as  $B_{s1}, B_{s2}, B_{s3}, B_{s4}, B_{s5}$ </td></tr><tr><td> $B_a$ </td><td>Agent-found buddies</td><td>Buddies that the subject got from our proposed agent-based buddy-finding methodology, such as  $B_{a1}, B_{a2}, B_{a3}, B_{a4}, B_{a5}$ </td></tr><tr><td> $B_{sf}$ </td><td>Final subject-selected buddies</td><td>Buddies that are the top five buddies selected from the mixed set of subject-found buddies and agent-found buddies (step 5 of experimental procedures)</td></tr><tr><td> $R_s$ </td><td>Rank order of subject-found buddies</td><td>Subjects&#x27; ranking of subject-found buddies (step 4 of experimental procedures). For example, the subject ranked five subject-found buddies ( $B_s$ ) based on their quality as  $B_{s3} > B_{s2} > B_{s4} > B_{s5} > B_{s1}$ . We call this rank  $R_s$ .</td></tr><tr><td> $R_a$ </td><td>Rank order of agent-found buddies</td><td>Agents&#x27; ranking of subject-found buddies ( $B_s$ ). For example, in step 4 of the experimental procedures, subjects ranked five subject-found buddies as  $B_{s3} > B_{s2} > B_{s4} > B_{s5} > B_{s1}$ . In our proposed agent methodology, the agent computed fuzzy membership values for these five buddies, so we got another rank order of them with agent methodology, such as  $B_{s5} > B_{s3} > B_{s4} > B_{s1} > B_{s2}$ . We call this rank  $R_a$ .</td></tr><tr><td> $E_{ia}$ </td><td>Evaluation of items (music) of agent-found buddies</td><td>From step 7 of the experimental procedures. The subject was presented the music collection from the group of agent-found buddies. The evaluation is the similarity of the music contained in this group of buddies to music contained in the music collection of this subject</td></tr><tr><td> $E_{is}$ </td><td>Evaluation of items (music) of subject-found buddies</td><td>From step 7 of the experimental procedures. The subject was presented the music collection from the group of subject-found buddies. The evaluation is the similarity of the music contained in this group of buddies to music contained in the music collection of this subject</td></tr><tr><td> $E_{isf}$ </td><td>Evaluation of items (music) of final subject-found buddies</td><td>From step 7 of the experimental procedures. The subject was presented with the music collection from the group of final subject-found buddies. The evaluation is the similarity of the music contained in this group of buddies to music contained in the music collection of this subject</td></tr></table>

The experiment was carried out in a computer lab. Since the experiment took from 3 to 6 h, it was divided into two parts: the first included steps 1 and 2 and the second consisted of steps 3–7.

## 5.6. Validity check of subject-found buddies

To check the validity of subject-found buddies, we determined whether or not they shared any preferences. Analysis showed that 90% of the subject-found buddies shared preferences with the subject regarding music genre, and the other 10% had common interests with the subject regarding other attributes, such as mood, tempo, beat, etc.

## 6. Results and analysis

We analyzed the test results from a variety of perspectives to assess the stated conjecture, using symbols shown in Table 2.

## 6.1. Buddy overlap analysis

Our first analysis was to assess whether there was a significant overlap between agent-found buddies $\left( B _ { \mathrm { a } } \right)$ and the subject-found buddies $( B _ { \mathrm { s } } )$ (see Fig. 3). The mean value of the buddy overlap between agent-found buddies $( B _ { \mathrm { a } } )$ and the subject-found buddies $( B _ { \mathrm { s } } )$ was 21% $( \mathrm { S . D . } = 0 . 1 5 )$ . This shows little buddy overlap. The reason apparently was that buddy-agents used the total set of music by all subjects (i.e., all case-bases) to assess the degree of buddy membership $( B _ { \mathrm { s } } )$ but subject assessed buddies $( B _ { \mathrm { a } } )$ were based on responses received from a subset of the total set of peers (not everyone responded to all requests). Therefore, it is likely that subjects missed selecting some of the buddies found by the agent $( \mathrm { i } . \mathrm { e } . , B _ { \mathrm { a } } )$ . To this end, a pair wise t-test was conducted to assess overlap between agent-found $\left( B _ { \mathrm { a } } \right)$ and final subject-found buddies $( B _ { \mathrm { s f } } )$ and overlaps between subject-found buddies $( B _ { \mathrm { s } } )$ and final subjectselected buddies $( B _ { \mathrm { s f } } )$ (i.e., to test $B _ { \mathrm { a } } \cap B _ { \mathrm { s f } }$ and $B _ { \mathrm { s } } \cap B _ { \mathrm { s f } } )$ (see Fig. 3). This could reveal whether there was a meaningful difference between the significance of agent-found buddies $\left( B _ { \mathrm { a } } \right)$ and subject-found buddies $( B _ { \mathrm { s } } )$ to the subject-selected buddies $( B _ { \mathrm { s f } } )$

The mean value of the overlap between agent-found buddies $\left( B _ { \mathrm { a } } \right)$ and final subject-found buddies $( B _ { \mathrm { s f } } )$ was 55% $( \mathrm { S . D . } = 1 8 \% )$ , and the mean value of the overlap between subject-found buddies $( B _ { \mathrm { s } } )$ and final subjectselected buddies $( B _ { \mathrm { s f } } )$ was $5 9 \% \mathrm { ( S . D . } = 1 9 \% )$ . To understand why buddy overlap is high between $B _ { \mathrm { a } }$ and $B _ { \mathrm { s f } }$ and between $B _ { \mathrm { s } }$ and $B _ { \mathrm { s f } } ,$ we noted that $B _ { \mathrm { s f } }$ represented the final subject-selected buddies selected from both sets $B _ { \mathrm { a } }$ and $B _ { \mathrm { s } }$ . This results show that, the subjects selected approximately half from $B _ { \mathrm { a } }$ and half from $B _ { \mathrm { s } }$ . This reinforced the fact that they are equally good from a subject’s perspective. The pair wise t-test for the evaluation of the overlap values between these two groups of buddies showed no significant difference $( t = - 0 . 7 3 , p = 0 . 4 7 )$ ). This result shows that we cannot reject the stated conjecture in terms of the buddy overlap.

There is no significant preference difference between the buddies found through the proposed agent methodology and those identified by the subjects.

## 6.2. Assessment of buddy preference

Subjects used a Likert-type scale of 1–9 to state their perception of the goodness of top-five ranked buddies for each of the two groups of buddies: $B _ { \mathrm { a } }$ and $B _ { \mathrm { s } }$ (see

![](/api/attachments/BSQ5BJWZ/fulltext/images/b308dc58d206f594e3cd965955b84506e4515d0d8828c33628e349902ff5243e.jpg)  
Final subject-selected buddies $\mathbf { ( B _ { s f } ) }$  
Fig. 3. Overlap among agent-found buddies $( B _ { \mathrm { a } } ) ,$ , subject-found buddies $( B _ { \mathrm { s } } ) _ { \mathrm { : } }$ , and final subject-found buddies $( B _ { \mathrm { s f } } )$

Table 3). A pair wise t-test was conducted to compare subjects’ perception of agent-found buddies $( B _ { \mathrm { a } } )$ , and subject-found buddies $( B _ { \mathrm { s } } )$ . This analysis would reveal whether there was significant difference between subjects’ preference of buddies found by agents $\left( B _ { \mathrm { a } } \right)$ and those found manually $( B _ { \mathrm { s } } )$

The mean evaluation score of the subject-found buddies $( B _ { \mathrm { s } } )$ was 6.27 (S.D. = 2.39), and the mean evaluation score of the agent-found buddies $\left( B _ { \mathrm { a } } \right)$ was $6 . 0 5 \ : \ : \ : \mathrm { ( S . D . } = 2 . 3 5 \ )$ . The pair wise t-test for the evaluation of these two groups of buddies showed no significant difference between them $( t = - 0 . 1 3 6 ,$ $p = 0 . 1 7 7 )$ . This result thus showed that the stated conjecture could not be rejected.

There is no significant perceived preference difference between buddies found through the proposed agent-found methodology and buddies identified by the subjects.

## 6.3. Evaluation of items of agent-found versus subject-found buddies

An overlap analysis was used to compare the commonality between the agent-found buddies $\left( B _ { \mathrm { a } } \right)$ and those of subject-found buddies $( B _ { \mathrm { s } } )$ . First, we analyzed the overlap rate between the musical preferences of agent-found buddies $( B _ { \mathrm { a } } )$ and those of the subject-found buddies $( B _ { \mathrm { s } } )$ based on the characteristics of music they had in common. This assessed whether there was any significant difference between the music preferences of agent-found $\left( B _ { \mathrm { a } } \right)$ and subjectfound buddies $( B _ { \mathrm { s } } )$ . See Table 4 for a calculation of overlap rate.

The statistical analysis for the music overlap of all subjects showed that the mean overlap was 99.69% $( \mathrm { S . D . } = 0 . 0 0 5 )$ This indicated that there was a significant similarity between the characteristics of music selected for each subject by the agent-found buddies $( B _ { \mathrm { a } } )$ and characteristics of those selected directly by the subject-found buddies $( B _ { \mathrm { s } } )$ . Thus we cannot reject the stated conjecture in terms of the characteristics of the music overlap.

There is no significant preference difference between the buddies found through the proposed agent-found methodology and buddies identified by subjects.

Although there was no significant difference between the characteristics of the music preference of the agent-found versus subject-found buddies, there is still a question whether the subjects were satisfied (measured by means of a Likert-type scale of 1–9) with the selected music in each of the three groups. A nonparametric Kruskal–Wallis test was used to assess the subjects’ degree of satisfaction with the items (music) of the three groups of buddies: (i) agent-found buddies $( B _ { \mathrm { a } } ) ;$ ; (ii) subject-found buddies $( B _ { \mathrm { s } } ) ;$ ; and (iii) final subject-selected buddies $( B _ { \mathrm { f s } } )$ . This result could reveal whether there was a significant difference among subjects’ evaluations of music of the three possible buddy groups.

Table 3  
Perception of subject 1 for the top-five ranked agent-found buddies and subject-found buddies

<table><tr><td>Subject</td><td>Agent-found buddies ( $B_a$ )</td><td>Perception of goodness (1–9)</td></tr><tr><td>S1</td><td>S3</td><td>8</td></tr><tr><td>S1</td><td>S10</td><td>7</td></tr><tr><td>S1</td><td>S11</td><td>6</td></tr><tr><td>S1</td><td>S7</td><td>5</td></tr><tr><td>S1</td><td>S9</td><td>4</td></tr></table>

Subject Subject-found buddies $( B _ { \mathrm { s } } )$ Perception of goodness (1–9)

<table><tr><td>S1</td><td>S7</td><td>9</td></tr><tr><td>S1</td><td>S26</td><td>6</td></tr><tr><td>S1</td><td>S8</td><td>5</td></tr><tr><td>S1</td><td>S9</td><td>4</td></tr><tr><td>S1</td><td>S15</td><td>3</td></tr></table>

The Kruskal–Wallis test for the evaluation of items (music) of three different buddy selections $( E _ { \mathrm { i a } } , E _ { \mathrm { i s } } , E _ { \mathrm { i s f } } )$ showed no significant difference among them $( \chi ^ { 2 } = 4 . 3 4 , p = 0 . 1 1 )$ . This indicated that the music of the agent-found buddies $( B _ { \mathrm { a } } )$ reached the same satisfaction level as the music of subject-found buddies (both $B _ { \mathrm { s } }$ and $B _ { \mathrm { s f } } )$ . This finding also indicated that we cannot reject the stated conjecture.

There is no significant perceived difference between the buddies found through the proposed agent-found methodology and buddies identified by the subjects.

Finally, to further prove the validity of our methodology, we assessed the written comments of the subjects. Their comments showed no difference in their preferences about different group of buddies.

Table 4  
Example of music type overlap of one subject

<table><tr><td>Genre</td><td>Musical preferences of agent-found buddies ( $B_a$ )</td><td>Musical preferences of subject-found buddies ( $B_s$ )</td><td>Overlap</td></tr><tr><td>Rock</td><td>50</td><td>53</td><td>50</td></tr><tr><td>Country</td><td>40</td><td>40</td><td>40</td></tr><tr><td>Jazz</td><td>10</td><td>7</td><td>7</td></tr><tr><td>Total</td><td>100</td><td>100</td><td>97</td></tr></table>

Subjects commented on the music contained in the agent-found buddies $( B _ { \mathrm { a } } ) \mathrm { : }$ : ‘‘this group is very similar to me,’’ ‘‘similar,’’ ‘‘Somebody has same experience in music,’’ etc. with the music in the collections of subjectfound buddies $( B _ { \mathrm { s } } )$ , subjects found the music contained in the agent-found buddies $( B _ { \mathrm { a } } )$ to be as good as the music in the collections of subject-found buddies. For example, one subject commented: ‘‘good one, I like your choices very much’’; and another subject remarked: ‘‘Although there were different songs in this list, I recognized many of them. So, I felt this list was about as good as the list for group 1 [the subject-found buddy group].’’ More directly, some subjects simply considered that the agent-found buddies $( B _ { \mathrm { a } } )$ had the same music tastes as they did. For example, one subject commented: ‘‘Somebody has same experience in music.’’ Subjects’ comments showed their acceptance of agent-found buddies $\left( B _ { \mathrm { a } } \right)$ through the recognition of the similarity between the music tastes of agent-found buddies $( B _ { \mathrm { a } } )$ and the music tastes of subject-found buddies $( B _ { \mathrm { s } } )$

In the final evaluation, subjects were not told the source of each group of buddies. Their comments indicated that many subjects could not identify the difference between the agents-found and subjects-found buddies. For example, one subject commented for the agent-found buddies that ‘‘This is the better group of music I like to listen $\mathrm { t o } , \vec { \mathbf { \Lambda } }$ and the same subject commented for the subject-found buddies that ‘‘These are close to what I like to hear.’’ Another subject commented about the agent-found buddies: ‘‘This group is getting better towards being similar;’’ and the same subject commented about the subject-found buddies that ‘‘This group is similar, but not as close as it should be.’

Thus, the analysis shows that there is no significant difference between agent-found $( B _ { \mathrm { a } } )$ and buddies identified by the subjects $( B _ { \mathrm { s } } )$

## 7. Conclusion

The purpose of our investigation was to determine whether our methodology could simulate human perception in assessing the quality of buddies. The first major finding of this investigation was that the agents can work as well as human subjects in finding music buddies. The second showed that there is no significant difference between subjects’ satisfaction with the items (music) contained in agent-found buddies and the items contained in subject-found buddies. These test results support our conjecture. The methodology is particularly useful in a large P2P environment with dynamic membership in which users can join/leave the network at will. Furthermore, the users’ information requirements (e.g., exchange of music) can change over time. In such an environment, current methodologies advocate sending a request to all the peers, which is inefficient, or creating predefined local list of buddies, which is impractical for a large and dynamic network of users. In contrast, our methodology accurately identified groups of users (buddies) who could best satisfy each other’s information needs. This method of message routing was limited to a small subset of the P2P network, making communication efficient, avoiding flooding the network to broadcast to redundant users. Furthermore, the buddy-agent methodology updated the list of buddies when information need between buddies changed, enabling users to find buddies for sharing information in the virtual world.

Our methodology could be used to facilitate buddyfinding among large numbers of users in a distributed environment. Companies in technologically intensive fields rely on collaborative relationships to access, survey, and exploit emerging technological opportunities [46]. It is commonly believed that learning is enhanced when knowledge workers are encouraged to collaborate with like-minded individuals [24]. Our methodology makes use of a combination of agent technology and distributed CBR systems in support of knowledge sharing among like-minded decision maker. The contribution of our buddy-finding methodology is a significant progress in this area. Our buddy-finding methodology is automatic, it can save users tremendous time without lowering quality of results.

Whilst the results of empirical tests of our proposed methodology are encouraging, there are some limitations:

 First, the tests of the buddy-finding methodology used a relatively small sample of users. The real advantage of MAS lies in the reduction of information overload for environments in which there is a very large number of users needing to share information with each other.

 Users in online communities build trust mainly by cooperative interactions through message boards [26,28,50]. When using our buddy-finding methodology, however, the users would receive the recommended buddies directly from agents. Consequently, lack of prior interactions between the users and the recommended buddies might influence the users’ trust about the usefulness of the recommended agent-found buddies. However findings indicate that it is indeed possible to create trust between users without prior interactions [5].

## Acknowledgments

The authors would like to thank the four anonymous reviewers and Dr. Sibley for their comments on earlier drafts of this manuscript. This research has been supported in part by a grant awarded to Dr. Montazemi from Natural Sciences and Engineering Research Council of Canada.

## References

[1] E. Adar, B. Huberman, Free riding on Gnutella, First Monday, 2000.

[2] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25(3), 2001, pp. 107–136.

[3] J.L. Arcos, T-air: a case-based reasoning system for designing chemical absorption plants, in: D.W. Aha, I. Watson (Eds.), Case-Based Reasoning Research and Development, LNAI 2080, Fourth International Conference on Case-Based Reasoning, ICCBR 2001, Vancouver, BC, Canada, July/August 2001, Springer-Verlag, Berlin, 2001, pp. 576–588.

[4] M. Augier, M.T. Vendelo, Networks, cognition, and management of tacit knowledge, Journal of Knowledge Management 3(4), 1999, pp. 252–261.

[5] S. Ba, P.A. Pavlov, Evidence of the effect of trust building technology in electronic markets: price premiums and buyer behavior, MIS Quarterly 26(3), 2002, pp. 243–268.

[6] P. Bernus, G. Uppington, Co-ordination of management activities-mapping organizational structure to the decision structure, in: W. Conen, G. Neumann (Eds.), Coordination Technology for Collaborative Application—Organizations, Processes and Agents, LNCS 1364, Springer-Verlag, Berlin, 1998, pp. 25–38.

[7] A. Bordetsky, G. Mark, Memory-based feedback controls to support groupware coordination, Information Systems Research 11(4), 2000, pp. 366–385.

[8] M. Catterall, P. Maclaran, Researching consumers in virtual worlds: a cyberspace odyssey, Journal of Consumer Behaviour 1(3), 2002, pp. 228–237.

[9] W. Chai, B. Vercoe, Using user models in music information retrieval systems, in: Proceedings of the International Symposium on Music Information Retrieval, Plymouth, Massachusetts, October, 2000.

[10] L.K. Chang, S. Lee, I.W. Kang, KMPI: measuring knowledge management performance, Information and Management 42(3), 2005, pp. 469–482.

[11] R. Davis, R.G. Smith, Negotiation as a metaphor for distributed problem solving, Artificial Intelligence 20(1), 1983, pp. 63–109.

[12] F. Dignum, B. Dunin-Keplicz, R. Verbrugge, Agent theory for team formation by dialogue, in: C. Castelfranchi, Y. Lespe´rance (Eds.), Intelligent Agents VII, Proceedings of the Seventh International Workshop on Agent Theories Architectures and Languages, ATAL 2000, Boston, MA, USA, July 2000, LNAI 1986, Springer-Verlag, Berlin, 2001, pp. 150–166.

[13] N.M. Dixon, The changing face of knowledge, The Learning Organization 6(5), 1999, pp. 212–216.

[14] V. Dougherty, Knowledge is about people, not databases, Indus trial and Commercial Training 31(7), 1999, pp. 262–266.

[15] E.H. Durfee, Distributed problem solving and planning, in: M. Luck, M. Marik, O. Stepankova, R. Trappl (Eds.), Multi-Agent

Systems and Applications, LNAI 2086, Springer-Verlag, Berlin, 2001, pp. 118–149.

[16] G. Fernandez, I. Wijegunaratne, A cooperation approach to distributed application engineering, in: W. Conen, G. Neuman, G. Goods, J. Hartmanis, J.V. Leeuwen (Eds.), Coordination Technology for Collaborative Applications—Organizations, Processes, and Agents, Lecture Notes in Computer Science 1364, Springer-Verlag, Berlin, 1998, pp. 39–48.

[17] R.A. Flores, R.C. Kremer, D.H. Norrie, An architecture for modeling Internet-based collaborative agent systems, in: T. Wagner, O. Rana (Eds.), Infrastructure for Agents, Multi-Agent Systems, and Scalable Multi-Agent Systems, LNAI 1887, International Workshop on Infrastructure for Scalable Multi-Agent Systems, Barcelona, Spain, June 2000, Revised Papers, Springer-Verlag, Berlin, 2001, pp. 56–63.

[18] F. Geyer, Virtual communities in cyberspace, Kybernetes 25(4), 1996, pp. 60–66.

[19] N. Good, J.B. Schafer, J.A. Konstan, A. Borchers, B. Sarwar, J. Herlocker, J. Riedl, Combining collaborative filtering with personal agents for better recommendations, in: Proceedings of the 16th National Conference on Artificial Intelligence and Eleventh Conference on Innovative Applications of Artificial Intelligence, Orlando, Florida, USA, July 18–22, AAAI Press/ MIT Press, 1999, pp. 439–446.

[20] P. Gottschalk, Knowledge management in the professions: the case of it support in law firms, in: Proceedings of the 33rd Hawaii International Conference on System Sciences, vol. 3, Maui, Hawaii, January 4–7, 2000.

[21] D. Gould, Virtual organization, in: Leading Virtual Teams (online) 2, September 1999, http://www.seanet/com/-daveg/ ltv.htm.

[22] K. Gupta, A framework for the design and development of diagnostic case-based reasoning systems, Ph.D. Thesis, School of Business, McMaster University, 1996.

[23] K.M. Gupta, A.R. Montazemi, Empirical evaluation of retrieval in case-based reasoning systems using modified cosine matching function, IEEE Transaction on Systems, Man, and Cybernetics 27(5), 1997, pp. 601–612.

[24] M.T. Hansen, N. Nohria, T. Tierney, what is your strategy for managing KM? Harward Business Review 1999, pp. 105–116.

[25] B. Hayes-Roth, An architecture for adaptive intelligent systems, Artificial Intelligence 72(12), 1995, pp. 329–365.

[26] D.L. Hoffman, T.P. Novak, M. Peralta, Building consumer trust online, Communications of the ACM 42(4), 1999, pp. 80– 85.

[27] H. Holmstro¨m, Virtual communities as platforms for product development: an interpretive case study of customer involvement in online game development, in: Proceedings of the 22nd Inter national Conference on Information Systems, New Orleans, LA, USA, December 16–19, 2001, pp. 299–306.

[28] Y. Hu, Some thoughts on agent trust and delegation, in: Proceedings of the Fifth International Conference on Autonomous Agents, AGENTS’01, Montreal, Que., Canada, May 28–June 1, 2001, pp. 489–496.

[29] B. Irma, S. Rajiv, Organizational knowledge management: A contingency perspective, Journal of Management Information Systems 18(1), 2001, pp. 23–55.

[30] P. Johnson, V. Heimann, K. O’Neill, The wonderland of virtual teams, Journal of Workplace Learning 13(1), 2001, pp. 24–29.

[31] J.C. Lang, Managing in knowledge-based competition, Journal of Organizational Change Management 14(6), 2001, pp. 539– 553.

[32] K.R.T. Larsen, C.R. McInerney, Preparing to work in the virtual organization, Information and Management 39(6), 2002, pp. 445–456.

[33] E. Lesser, L. Prusak, Communities of practice, social capital, and organizational knowledge, in: J.W. Cortada, J.A. Woods (Eds.), The Knowledge Management Yearbook 2000–2001, Butterworth Heinemann, 2000, pp. 251–259.

[34] M.M. Lynne, Toward a theory of knowledge reuse: types of knowledge reuse situations and factors in reuse success, Journal of Management Information Systems 18(1), 2001, pp. 57–93.

[35] Y. Malhotra, Enabling knowledge exchanges for e-business communities, Information Strategy 18(3), 2002, pp. 26–31.

[36] D. Maltz, K. Ehrlich, Pointing the way: active collaborative filtering, Conference Proceedings on Human Factors in Computing Systems, 1995, Denver, Colorado, ACM Press/Addison-Wesley Publishing Co., New York, NY, USA, 1995, pp. 202–209.

[37] R.L. Ma´ntaras, J.L. Arcos, The synthesis of expressive music: a challenging CBR application, in: D.W. Aha, I. Watson (Eds.), Case-Based Reasoning Research and Development, LNAI 2080, Fourth International Conference on Case-Based Reasoning, ICCBR 2001, Vancouver, BC, Canada, July/August 2001, Springer-Verlag, Berlin, 2001, pp. 16–26.

[38] V. Marˇ´ık, M. Peˇchoucˇek, J. Lazˇansky´, C. Roche, PVS’98 agents: structures, models and production planning application, Robotics and Autonomous Systems 27, 1999, pp. 29–43.

[39] D.R. Millen, M.A. Fontaine, M.J. Muller, Understanding the benefit and costs of communities of practice, Communications of the ACM 45(4), 2002, pp. 69–73.

[40] A.R. Montazemi, K.M. Gupta, An adaptive agent for case description in diagnostic CBR systems, Journal of Computers in Industry 29, 1996, pp. 209–224.

[41] A. Newell, Putting it all together, in: D. Klahr, K. Kotovsky (Eds.), Complex Information Processing: The Impact of Herbert Simon, Hillsdale, NJ, Lawrence Erlbaum, 1988.

[42] M. Nodine, D. Chandrasekara, A. Unruh, Task coordination paradigms for information agents, in: C. Castelfranchi, Y. Lespe´rance (Eds.), Intelligent Agents VII, Proceedings of the Seventh International Workshop on Agent Theories Architectures and Languages, ATAL 2000, Boston, MA, USA, July 2000, LNAI 1986, Springer-Verlag, Berlin, 2001, pp. 167– 181.

[43] T.J. Norman, C. Reed, Delegation and responsibility, in: C. Castelfranchi, Y. Lespe´rance (Eds.), Intelligent Agents VII, Proceedings of the Seventh International Workshop on Agent Theories Architectures and Languages, ATAL 2000, Boston, MA, USA, July 2000, LNAI 1986, Springer-Verlag, Berlin, 2001, pp. 136–149.

[44] M. Portmann, A. Seneviratne, Cost-effective broadcast for fully decentralized peer-to-peer networks, Computer Communications 26, 2003, pp. 1159–1167.

[45] L. Pouchard, D.W. Walker, A Community of Agents for User Support in a Problem-Solving Environment, in: T. Wagner, O. Rana (Eds.), Infrastructure for Agents, Multi-Agent Systems, and Scalable Multi-Agent Systems, LNAI 1887, International Workshop on Infrastructure for Scalable Multi-Agent Systems, Barcelona, Spain, June 2000, Revised Papers, Springer-Verlag, Berlin, 2001, pp. 192–198.

[46] W.W. Powell, Learning from collaboration: knowledge and networks in the biotechnology and pharmaceutical industries, California Management Review 40(3), 1998, pp. 228–240.

[47] E.A. Regan, B.N. O’Connor, End-User Information Systems: Implementing Individual and Work Group Technologies, 2nd ed., Prentice-Hall, New Jersey, 2002.

[48] Reticular, User Guide, Version 1.1, Rev. 4, 1999. www.reticular.com.

[49] A. Ricci, E. Denti, A. Omicini, Agent coordination infrastructures for virtual enterprises and workflow management, in: M. Klusch, F. Zambonelli (Eds.), Cooperative Information Agents V, LNAI 2182, Proceedings of the Fifth International Workshop, CIA 2001, Modena, Italy, September 2001, Springer-Verlag, Berlin, 2001, pp. 235–246.

[50] C.M. Ridings, D. Gefen, B. Arinze, Some antecedents and effects of trust in virtual communities, Journal of Strategic Information Systems 11(3–4), 2002, pp. 271–295.

[51] E. Scheirer, Music-listening systems, Ph.D. Dissertation, Massachusetts Institute of Technology, 2000.

[52] M. Schumacher, Objective Coordination in Multi-Agent System Engineering: Design and Implementation, Lecture Notes in Artificial Intelligence, Springer-Verlag, 2001.

[53] R. Sikora, M.J. Shaw, A multi-agent framework for the coordination and integration of information systems, Management Science 44(11), 1998, pp. S65–S78.

[54] M. Smith, Tools for navigating large social cyberspace, Communications of the ACM 45(4), 2002, pp. 51–55.

[55] R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, MIT Press, Cambridge, MA, 1998.

[56] J. Swan, S. Newell, H. Scarbrough, D. Hislop, Knowledge management and innovation: networks and networking, Journal of Knowledge Management 3(4), 1999, pp. 262– 275.

[57] L.L. Tung, P.L.J. Tan, P.J.T. Chia, Y.L. Koh, An empirical investigation of virtual communities and trust, in: Proceedings of the 22nd International Conference on Information Systems, New Orleans, LA, USA, 2001, pp. 307–320.

[58] P.J. Turner, N.R. Jennings, Improving the scalability of multiagent systems, in: T. Wagner, O. Rana (Eds.), Infrastructure for Agents, Multi-Agent Systems, and Scalable Multi-Agent Systems, LNAI 1887, International Workshop on Infrastructure for Scalable Multi-Agent Systems, Barcelona, Spain, June 2000, Revised Papers, Springer-Verlag, Berlin, 2001 , pp. 246–262.

[59] E. Wenger, Communities of Practice: Learning, Meaning, and Identity, Cambridge University Press, Cambridge, 1998.

[60] R.P. Yager, A new methodology for ordinal multiobjective decision based on fuzzy sets, Decision Sciences 12(3), 1981, pp. 589–600.

[61] L.A. Zadeh, Fuzzy Sets, Information and Control 8, 1965, pp. 338–353.

[62] K.G. Zerfiridis, H.D. Karatza, File distribution using a peer-topeer network––a simulation study, The Journal of Systems and Software 73, 2004, pp. 31–44.

[63] H. Zhuge, Workflow- and agent-based cognitive flow management for distributed team cooperation, Information and Management 40(5), 2003, pp. 419–429.

![](/api/attachments/BSQ5BJWZ/fulltext/images/2b8243288143b5fcaa4de4e9b2316c893250a5837ae4c0ed468e138d4312a8b4.jpg)  
Xiaoqing Li is currently an Assistant Professor at the Department of Management Information Systems from the University of Illinois at Springfield (USA). He obtained his PhD degree in Management Information Systems at McMaster University (Canada). His research interests are in intelligent agent systems, knowledge management and decision support systems.

![](/api/attachments/BSQ5BJWZ/fulltext/images/351f22902d1794ee6f0d8bb86c08982346176bd86a1c2d1ca81912e32ad331b9.jpg)

Ali R. Montazemi is the Director of eBusiness at DeGroote School of Business, McMaster University, Canada. He has served on the editorial board of European Journal of Information Systems, and Canadian Journal of Administrative Sciences. His research interests include business application of artificial intelligence in business, decision support system modeling and assessment, business process design

through information technology. His publications have appeared in journals such as MIS Quarterly, Journal of Management Information Systems, Decision Support Systems, Communications of the ACM, Journal of Electronic Commerce Research, Journal of Artificial Intelligence in Education, and IEEE Transactions on Systems, Man and Cybernetics.

![](/api/attachments/BSQ5BJWZ/fulltext/images/7129a5f93b78d016d8386fa22dc58e67456d3f3508026b6639ef62642f65c65b.jpg)

Yufei Yuan is the Wayne C. Fox Chair in Business Innovation and a Professor of Information Systems at DeGroote School of Business, McMaster University, Canada. He received his PhD in Computer Information Systems from The University of Michigan in U.S.A. and BS in Mathematics from Fudan University in China. His research interests are in the areas of mobile commerce, web-based negotiation support sys-

tem, business model of electronic commerce, approximate reasoning with fuzzy logic, matching problem, and decision support in health care. He has published 49 papers in professional journals such as Communications of ACM, Internet research, International Journal of Mobile Communication, International Journal of Electronic Markets, Fuzzy Sets and Systems, European Journal of Operational Research, Management Sciences, Decision Sciences, Academic Medicine, Medical Decision Making, International Journal of Human–Computer Systems, Human Systems Management and others. His name is listed in Who’s Who in Canada.
