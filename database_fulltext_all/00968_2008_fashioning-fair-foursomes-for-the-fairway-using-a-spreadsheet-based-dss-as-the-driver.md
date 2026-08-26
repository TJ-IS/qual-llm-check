---
otero_id: 968
otero_key: "S9PBP89P"
title: "Fashioning fair foursomes for the fairway (using a spreadsheet-based DSS as the driver)"
authors: "Cliff T. Ragsdale; Kevin P. Scheibe; Michael A. Trick"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.03.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fashioning fair foursomes for the fairway (using a spreadsheet-based DSS as the driver) <sup>☆</sup>

Cliff T. Ragsdale <sup>a,</sup>⁎, Kevin P. Scheibe <sup>b,1</sup>, Michael A. Trick <sup>c,2</sup>

<sup>a</sup> Pamplin College of Business, Virginia Tech, Blacksburg, Virginia 24061, United State

<sup>b</sup> College of Business, Iowa State University, Ames, IA 50011, United States

<sup>c</sup> Tepper School of Business, Carnegie Mellon University, Pittsburgh, PA 15213, United States

## a r t i c l e i n f o

Article history: Received 6 August 2007 Received in revised form 24 March 2008 Accepted 30 March 2008 Available online 12 April 2008

Keywords: Golf scramble problem Scheduling Spreadsheets Mixed-integer programming

## a b s t r a c t

Golf teams at most public universities derive much of their support for player scholarships from external donors. Relationships with current and potential donors are often created and maintained via annual golf tournaments that pair donors with varsity players and team coaches in a scramble format tournament. This paper introduces a new spreadsheet-based DSS tool for optimizing the formation of teams for multi-round, unique-team, golf scramble tournaments. The DSS uses mixed-integer programming to create unique teams for each round of play while considering the handicaps of all teams and individual players to ensure a reasonable level of fairness in the tournament.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Golf has become one of the most popular recreational sporting activities in the world, providing young and old alike with a forum for socializing, networking, exercising, and experiencing the thrill of victory and (perhaps more often) the agony of defeat. To allow competitors with varying skill levels to play against one another on a fair and competitive basis, most amateur golf competitions employ a handicap system where players with lesser skills have their scores adjusted downward by a certain number of strokes—representing their “handicap.” In this way, the winner of a tournament may not be the best overall golfer, but the person who played the best given his or her skill level.

When played in a team format, one typical golf tournament is a “scramble”, comprised of four-person teams. In this type of tournament, players are <sup>fi</sup>rst rank-ordered into four equally sized “<sup>fl</sup>ights” based on their handicaps. Next, one person from each <sup>fl</sup>ight is selected to make-up each team. (This helps prevent any team from being loaded with exceptionally good or poor players.) On each hole, each team member hits a tee shot (the <sup>fi</sup>rst team stroke); the best ball location is chosen and each team member hits from that position (the second team stroke). This process is repeated until a ball is in the hole. The number of team strokes determines the score on each hole. (Another common name for this type of tournament is “captain's choice.”) Handicaps are not used for scoring purposes in a scramble format. Thus, a “fair” competition occurs when the total handicap for each team is approximately equal.

Random assignment of players from each <sup>fl</sup>ight to teams ensures some measure of equity in each team's ability. Optionally, the assignment of players to teams can be formulated as a relatively easy mathematical programming problem with the objective of balancing the total handicap of each team. Balancing team handicaps provides a psychological bene<sup>fi</sup>t by creating a sense of fairness as well as an operational bene<sup>fi</sup>t by creating teams likely to play at somewhat similar speeds.

Recently, a more complex variation of a golf scramble tournament was brought to our attention by the assistant golf coach of the <sup>fi</sup>rst author's university. This university's golf team holds an annual tournament involving its coaches, varsity players, and benefactors. It is a three-day, three-round event where the organizers desire to ensure no two people play together more than once and, for each round, all teams have approximately the same handicap. To complicate matters, they also have side-constraints to ensure that certain people play together once (e.g., each scholarship player plays one round with the benefactor who provided the scholarship) and other constraints to prevent certain people from playing together at all (for a variety of reasons). Each player's total team score over the tournament determines the winner and <sup>fi</sup>nal rankings for the tournament.

We describe this interesting and dif<sup>fi</sup>cult scheduling problem and discuss a novel spreadsheet-based decision support system (DSS) to solve it. Prior to the creation of the DSS, the assistant golf coach would spend hours trying to <sup>fi</sup>nd a feasible solution to the problem using a spreadsheet. The proposed system not only locates feasible solutions but also can optimize the problem on various objectives using readily available software. The proposed mixed-integer programming (MIP) DSS delivered in an accessible software package (Microsoft Excel) provides an important decision support tool for decision makers like the university golf coach. This DSS is relatively inexpensive to implement and does not require substantial training. It can be easily explained, allowing the decision maker to begin using it quickly.

In the game of golf, the player chooses the most appropriate club for a shot based upon the environment. For example, when teeing off, it is generally the custom to use some sort of driver or iron, and when putting the ball, the golfer uses a putter. Maximum performance requires the right club choice for each shot. Additionally, the quality of clubs used matters less than the skill of the golfer. So, if a golfer lacks skill, his or her game will not greatly improve with the purchase of the best clubs. We draw the reader's attention to these points because they relate to our choice of DSS tools in two ways: First, this research meets a unique need of an actual decision maker—the university golf coach. While we acknowledge there are some very excellent alternative tools and techniques for solving this problem, the one proposed in this paper meets (and exceeds) the needs of the decision maker. Second, the objective function in this DSS is based upon human performance (golf handicap). Consequently, while the model may <sup>fi</sup>nd the optimal solution for fair team assignments, the players may still perform better or worse than usual, creating landslide victories or agonizing defeats. The proposed DSS cannot prevent such outcomes but should help the golf coach plan the best golf tournament he can with the tools at his disposal.

The remainder of this paper is organized as follow: Section 2 reviews the literature on operations research in sports and presents some background on college sports funding and the impetus for this research. Section 3 presents the mathematical formulation of the problem considered here. Section 4 discusses the problem implementation and solution using a spreadsheet-based DSS. Section 5 provides an example showing the bene<sup>fi</sup>ts of using the DSS in the context of an actual instance of this problem. In Section 6, we report on additional computational testing that provides insight about how our proposed solution methodology performs on larger instances of this problem. Finally, Section 7 provides implications and conclusion.

## 2. Background

There has been growing interest in the application of operations research techniques to the world of sports as problems in this domain can be mathematically complex and present interesting research challenges [9,31,41,44,49]. The dif<sup>fi</sup>culties associated with scheduling sporting events have provided ample potential for research [19,20,36,46,50]. One example is the alternation of home and away games for a sports league. de Werra [9] used graph-theory to minimize the number of breaks between home and away games. Similar “timetabling” issues in sports have piqued the interest of many researchers [2,12,14,22,34,36,40,43–46,49,50]. Applications of operations research have been identi<sup>fi</sup>ed in multiple sporting domains including baseball [35,44], basketball [21,31,47,48,50], soccer [2,4,11,13,25,41], American football [30,37], tennis [12,24], cricket [1], and golf [10,15,18,33,38].

In 2003, the reported mean university expenditure on NCAA, Division 1-A football was \$6.3 million and basketball was \$2 million [27]. Unfortunately, for less prominent athletic programs, universities spent substantially less. As a result, lower-pro<sup>fi</sup>le collegiate sports often rely heavily on donors for scholarships and support, so it is especially important to manage these donor relations well. University golf teams sometimes do this, in part, by hosting scramble tournaments to cultivate good relationships among key donors and the players and coaches. In these tournaments, it is important to give proper attention to team pairings to help ensure fairness, foster networking among donors, and pair the donors with the most appropriate university players and/or coaches. An additional factor adding complexity to this problem is that these tournaments are sometimes multi-day events, where it may be desirable to vary the make-up of teams from one day to the next.

Over the last 30 years, the game of golf has been the focus of several operations research studies. Of particular interest to some researchers is the fairness of handicapping [15,33,38,39]. Hall and Swartz [17,18] address the location of handicap strokes and its effect on golf scores and golf matches. Smith and Prockow use simulation to show weaknesses in match play golf tournaments [42], and Dear and Drezner use metaheuristics to address grouping players into teams according to their handicaps—the golf scramble problem [10]. The problem of assigning players to teams so that the teams are fair and balanced is not new, but to our knowledge, the problem of creating multi-day tournament team assignments with speci<sup>fi</sup>c restrictions of member allocation has not been considered before, and it is here we make a novel and unique research contribution.

## 3. Problem formulation and discussion

As mentioned earlier, the golf scramble problem involves taking a set of golfers with varying handicaps and placing them into teams of four that are as equally balanced as possible. Here, we consider the extension of this problem to a multi-day/round tournament where unique teams are desired for each round of play. Teams are unique when no two players are paired on the same team more than once. A number of side-constraints on feasible player pairings may also be speci<sup>fi</sup>ed. We refer to this as the multi-round unique-team golf scramble (MUGS) problem. A variety of objectives may be considered for this problem. We <sup>fi</sup>rst consider a formulation of the MUGS problem that minimizes the sum of absolute deviations (or the $\mathsf { L } _ { 1 } \mathrm { - N o r m } )$ from the theoretically optimal team handicap across all days of the tournament and, thus, create a tournament with reasonably fair and balanced foursomes [10].

To describe the MUGS problem more formally, let $N _ { \mathrm { P } } { = }$ the total number of players in the tournament, $N _ { \mathrm { T } } { = } \mathrm { t h e }$ number of teams per round, and $N _ { \mathrm { R } } { = }$ the number of rounds to be played. We assume $N _ { \mathrm { P } }$ is an even multiple of four. The $N _ { \mathrm { P } }$ players are <sup>fi</sup>rst ranked by handicap in ascending order and then identi<sup>fi</sup>ed by the index variable $i { = } 1 , 2 , . . . , N _ { \mathrm { P } }$ . Let H denote the handicap for player i. We assume there are four <sup>fl</sup>ights of players with $S { = } N _ { \mathrm { T } } { = } N _ { \mathrm { P } } / 4$ players in each <sup>fl</sup>ight and de<sup>fi</sup>ne $F _ { n } = \{ i$ | player i is in <sup>fl</sup>ight $n \} = \{ ( n - 1 ) S + 1 , ( n - 1 ) S + 2 , . . . , n S \} ,$ , for $n = 1 , 2 , 3 , 4 .$

To accommodate possible side-constraints on player pairings let $V = \{ ( i , r )$ | players i and r must never play on the same team} and $P { = } \{ ( i , r )$ | players i and r must play on the same team exactly once}. De<sup>fi</sup>ne $X _ { i j k l d } = 1$ if player i from <sup>fl</sup>ight 1, j from <sup>fl</sup>ight 2, k from <sup>fl</sup>ight 3, and l from <sup>fl</sup>ight 4, are paired together on day d; and 0 otherwise. Let $C _ { i j k l }$ represent the absolute deviation of each team's handicap from the theoretical optimal team handicap of $\begin{array} { r } { \overline { { H } } _ { \mathrm { T } } = \frac { 1 } { N _ { \mathrm { T } } } \sum _ { i } H _ { i } \ \overline { { ( \mathrm { i } . \mathrm { e } . , \ C _ { i j k l } = \left| H _ { i } + H _ { j } + H _ { k } + H _ { l } - \hat { H } _ { \mathrm { T } } \right| ) } } } \end{array}$ <sup>¼</sup>A mixed-integer programming (MIP) formulation of the MUGS problem can be stated as follows:

Minimize

$$
\sum_ {i} \sum_ {j} \sum_ {k} \sum_ {l} \sum_ {d} C _ {i j k l} X _ {i j k l d}\tag{1}
$$

Subject to:

$$
\sum_ {j} \sum_ {k} \sum_ {l} X _ {i j k l d} = 1, \quad \forall i, d\tag{2}
$$

$$
\sum_ {i} \sum_ {k} \sum_ {l} X _ {i j k l d} = 1, \quad \forall j, d\tag{3}
$$

$$
\sum_ {i} \sum_ {j} \sum_ {l} X _ {i j k l d} = 1, \quad \forall k, d\tag{4}
$$

$$
\sum_ {i} \sum_ {j} \sum_ {k} X _ {i j k l d} = 1, \quad \forall l, d\tag{5}
$$

$$
\sum_ {d} \sum_ {k} \sum_ {l} X _ {i j k l d} \leq 1, \quad \forall i, j\tag{6}
$$

$$
\sum_ {d} \sum_ {j} \sum_ {l} X _ {i j k l d} \leq 1, \quad \forall i, k\tag{7}
$$

$$
\sum_ {d} \sum_ {j} \sum_ {k} X _ {i j k l d} \leq 1, \quad \forall i, l\tag{8}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {l} X _ {i j k l d} \leq 1, \quad \forall j, k\tag{9}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {k} X _ {i j k l d} \leq 1, \quad \forall j, l\tag{10}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {j} X _ {i j k l d} {\leq} 1, \quad \forall k, l\tag{11}
$$

$$
\sum_ {d} \sum_ {k} \sum_ {l} X _ {i j k l d} = 0, \quad \forall i, j \in V\tag{12}
$$

$$
\sum_ {d} \sum_ {j} \sum_ {l} X _ {i j k l d} = 0, \quad \forall i, k \in V\tag{13}
$$

$$
\sum_ {d} \sum_ {j} \sum_ {k} X _ {i j k l d} = 0, \quad \forall i, l \in V\tag{14}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {l} X _ {i j k l d} = 0, \quad \forall j, k \in V\tag{15}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {k} X _ {i j k l d} = 0, \quad \forall j, l \in V\tag{16}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {j} X _ {i j k l d} = 0, \quad \forall k, l \in V\tag{17}
$$

$$
\sum_ {d} \sum_ {k} \sum_ {l} X _ {i j k l d} = 1, \quad \forall i, j \in P\tag{18}
$$

$$
\sum_ {d} \sum_ {j} \sum_ {l} X _ {i j k l d} = 1, \quad \forall i, k \in P\tag{19}
$$

$$
\sum_ {d} \sum_ {j} \sum_ {k} X _ {i j k l d} = 1, \quad \forall i, l \in P\tag{20}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {l} X _ {i j k l d} = 1, \quad \forall j, k \in P\tag{21}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {k} X _ {i j k l d} = 1, \quad \forall j, l \in P\tag{22}
$$

$$
\sum_ {d} \sum_ {i} \sum_ {j} X _ {i j k l d} = 1, \quad \forall k, l \in P\tag{23}
$$

$$
X _ {i j k l d} \in \{0, 1 \}\tag{24}
$$

The objective in Eq. (1) seeks to minimize the total absolute deviation $\left( \mathrm { L } _ { 1 } { - } \mathrm { N o r m } \right)$ of the teams' handicaps from the optimal value $( \overrightharpoon { H } _ { \mathrm { T } } )$ across the entire tournament. Constraints (2) through (5) require that each player is assigned to exactly one team in each round of play. Constraints (6) through (11) require that no two players play on the same team more than once. Constraints (12) through (23) implement possible side-constraints. Constraints (12) through (17) ensure that player pairings identi<sup>fi</sup>ed in V do not appear in the optimal solution. Similarly, constraints (18) through (23) ensure that player pairings identi<sup>fi</sup>ed in P do appear in the optimal solution.

In general, there are $N _ { \mathrm { T } } ^ { 4 } N _ { \mathrm { R } }$ decision variables in the MUGS problem and $4 N _ { \mathrm { T } } N _ { \mathrm { R } } { + } 6 _ { \mathrm { T } } ^ { 2 }$ constraints (not counting problemspeci<sup>fi</sup>c side-constraints in (12) through (23). In general, the MUGS problem has $( N _ { \mathrm { T } } ^ { 4 } N _ { \mathrm { R } } ) ^ { 2 }$ possible solutions for its binary variables. Table 1 summarizes how the dimensions of the problem grow rapidly as the number of players in a three-day tournament increases from 44 to 88.

Table 1  
MUGS problem dimensions for a three-day tournament

<table><tr><td>Players</td><td>Variables</td><td>Constraints</td><td>Possible binary solutions</td></tr><tr><td>44</td><td>43,923</td><td>858</td><td>1.9 billion</td></tr><tr><td>56</td><td>115,248</td><td>1344</td><td>13.3 billion</td></tr><tr><td>68</td><td>250,563</td><td>1938</td><td>62.8 billion</td></tr><tr><td>88</td><td>702,768</td><td>3168</td><td>493.8 billion</td></tr></table>

## 4. Solving the problem as a mixed-integer program

Although the formulation of the MUGS problem given above is not exceedingly dif<sup>fi</sup>cult to those familiar with mathematical programming, the organizers of most golf tournaments would likely <sup>fi</sup>nd it rather intimidating and dif<sup>fi</sup>cult to understand. Additionally, solving the problem for a 44-player tournament would require expensive optimization software requiring specialized knowledge. To overcome these obstacles, we sought to solve the MUGS problem in a spreadsheet-based DSS using the XPRESS MIP optimizer in Frontline's Premium Solver Platform [16]. One advantage of this approach is the users' familiarity with the spreadsheet environment. Indeed, when the golf coach originally approached the authors with the problem, he had already tried to formulate it in a spreadsheet. He simply did not have the requisite skills or knowledge to implement and solve the problem. Premium Solver is expensive, but Frontline offers a run-time library at a substantially reduced cost. This allows the golf coach, and others, to use the DSS without paying the high cost of the development library. Other optimization packages offer application program interfaces (API) for software like Excel, (e.g. CPLEX [23], LINDO [26]). Therefore, it is possible to develop the MUGS DSS using a variety of LP engines and some DSS designers will prefer one engine to another. Our objective was to bring a decision support tool to the golf coach where one did not previously exist using a familiar and accessible software platform.

Spreadsheet DSS have increased in popularity in both research and practice. The domains of application for spreadsheet DSS are as varied as the data and models used for decision support (e.g. [3,5,28,29,32]). One reason for the surge in the use of spreadsheet-based DSS is the near ubiquity of products like Microsoft Excel. Today, millions of professionals have the powerful modeling capabilities of a spreadsheet available on their personal computers [7]. At least one research study suggests that people have become so comfortable with spreadsheets that they are reluctant to adopt other software packages, even if the other packages are more suitable for speci<sup>fi</sup>c applications [6]. Another reason for this surge in popularity is the spreadsheet's increasing ability to integrate various decision support components under one application umbrella [28]. Many modeling tools not inherently built into Excel can be integrated in a spreadsheet-based DSS at minimal cost through add-ins.

## 5. Example

The approach to modeling and solving the MUGS problem using a spreadsheet allows the decision maker to use a software package he is accustomed to and easily comprehends. The DSS uses the MIP formulation given in Section 3, but implements it in a way that is transparent to the user. As a result, the spreadsheet DSS approach excels in terms of enduser acceptance. We now present an actual example of a MUGS problem faced by the university golf team and discuss the results. The data in this example are the actual player handicaps the golf coach used in his attempt to create, by hand, a three-day tournament. The task was very frustrating to the coach because he was unable to <sup>fi</sup>nd a satisfactory solution, thus prompting the request for help.

The data for the problem are given in Table 2, where the handicaps of 44 golfers are listed. The eleven players in <sup>fl</sup>ight 1 are all members of the varsity golf team or golf coaches. Each of these players has a handicap of zero. The remaining players are sorted by handicap and assigned to the remaining <sup>fl</sup>ights.

Recall, the goal is to assign one player from each <sup>fl</sup>ight to one of eleven teams on each day of the three-day tournament with no two players paired on the same team more than once while also minimizing the variability (L -Norm) in the team handicap for the tournament. For instance, if players in each row of Table 2 are assigned to teams on one day of the tournament, the team composed of players 1, 12, 23, and 34 has a team handicap of 34 while the team composed of players 11, 22, 33, and 44 has a team handicap of 56. Thus, the <sup>fi</sup>rst team has an apparent advantage over the last team. It is this type of advantage that the MUGS DSS attempts to mitigate. (Note that in this example, a theoretically optimal solution would combine players such that the resulting teams all have a team handicap of $\bar { H } _ { \mathrm { T } } { = } 5 0 6 / 1 1 { = } 4 6 . )$

Table 2 Player handicap data

<table><tr><td colspan="2">Flight 1</td><td colspan="2">Flight 2</td><td colspan="2">Flight 3</td><td colspan="2">Flight 4</td></tr><tr><td>Player</td><td>Handicap</td><td>Player</td><td>Handicap</td><td>Player</td><td>Handicap</td><td>Player</td><td>Handicap</td></tr><tr><td>1</td><td>0</td><td>12</td><td>1</td><td>23</td><td>13</td><td>34</td><td>20</td></tr><tr><td>2</td><td>0</td><td>13</td><td>2</td><td>24</td><td>14</td><td>35</td><td>20</td></tr><tr><td>3</td><td>0</td><td>14</td><td>4</td><td>25</td><td>15</td><td>36</td><td>21</td></tr><tr><td>4</td><td>0</td><td>15</td><td>5</td><td>26</td><td>16</td><td>37</td><td>21</td></tr><tr><td>5</td><td>0</td><td>16</td><td>7</td><td>27</td><td>16</td><td>38</td><td>22</td></tr><tr><td>6</td><td>0</td><td>17</td><td>7</td><td>28</td><td>16</td><td>39</td><td>24</td></tr><tr><td>7</td><td>0</td><td>18</td><td>8</td><td>29</td><td>16</td><td>40</td><td>24</td></tr><tr><td>8</td><td>0</td><td>19</td><td>9</td><td>30</td><td>17</td><td>41</td><td>24</td></tr><tr><td>9</td><td>0</td><td>20</td><td>10</td><td>31</td><td>18</td><td>42</td><td>25</td></tr><tr><td>10</td><td>0</td><td>21</td><td>10</td><td>32</td><td>18</td><td>43</td><td>27</td></tr><tr><td>11</td><td>0</td><td>22</td><td>10</td><td>33</td><td>18</td><td>44</td><td>28</td></tr></table>

Table 3  
Side-constraints on player pairings

<table><tr><td>A. Put 34 with 12 and 13.</td></tr><tr><td>B. Make sure that 34, 38 and 39 are not paired together; none of them should be paired with 2 or 11 either.</td></tr><tr><td>C. Put 11 with 21 and with 35; but never with 18, 17, 14, or 27.</td></tr><tr><td>D. Scholarship players need to play with their donor one day: pair 3 and 30; 1 and 19; 8 and 44; 5 and 42; 4 and 43.</td></tr></table>

Additionally, the tournament organizer requested that the side-constraints listed in Table 3 be integrated in the team assignments for the tournament. Note that such sideconstraints may be at odds with the objective of minimizing the team handicap variability. For instance, side-constraint A requires player 34 to be paired with players 12 and 13 on different days. Because player 34 is the best player in <sup>fl</sup>ight 4 and players 12 and 13 are the best players in <sup>fl</sup>ight 2, the teams that include these pairings will tend to have low team handicaps, potentially causing other teams to have higher handicaps. Furthermore, notice side-constraint B. The coach desires that players 34, 38, and 39 not play together, but all three players are in the same <sup>fl</sup>ight thereby preventing them from playing together even without the side-constraint. Nevertheless, we retained this side-constraint in the problem description because if the golf coach decides to treat the problem differently by changing the requirements on team formation, or if the player's handicaps changed such that they might be placed in different <sup>fl</sup>ights, then this constraint might become important in ensuring the desired player separations.

The MIP formulation of the MUGS problem given in Section 3 was created and solved using Frontline's Premium Solver [16]. This model required 43,923 variables and 880 constraints (including all side-constraints) and solved to optimality in approximately 10 min. All computations were carried out on a 3.2 GHz Pentium 4 machine with 1.0 GB of RAM. The scheduling results are summarized in Fig. 1. The optimal solution contained a maximum team handicap of 50 and minimum team handicap of 39. As expected (and desired), most teams had handicaps close to the theoretically optimal value of $\scriptstyle { \overline { { H } } } _ { \mathrm { T } } = 4 6$

While minimizing the absolute team handicap variations from the theoretical optimal value provides some measure of fairness across teams, it does not guard against possible scheduling inequities for individual players in the tournament. We de<sup>fi</sup>ne a player's tournament handicap to be the sum of the team handicaps to which the player is assigned over the tournament. The player with the largest tournament handicap might feel that the schedule is personally unfair even if the variability of team handicaps is minimized. This impression might be especially problematic if a substantial difference exists between the tournament handicaps to which this player is assigned and the minimum tournament handicap for all players. To address this issue, we made minor modi<sup>fi</sup>cations to the MUGS formulation presented earlier to minimize the sum of absolute deviation of tournament handicaps for each individual player from the theoretical optimal value of $\bar { H } _ { \mathrm { T } }$ (or 138 for our example problem). Fig. 2 summarizes the result of this effort.

Fig. 2 shows the tournament handicap for each player produced by the solutions to the original MUGS model (represented by Team Variability) and the modi<sup>fi</sup>ed model (represented by Individual Variability). The tournament handicaps resulting from minimizing the team variability gave the most disadvantaged player a tournament handicap of 143 and the most advantaged player a tournament handicap of 125, resulting in a range of 18 between the highest and lowest tournament handicaps. The tournament handicaps resulting from minimizing the individual players tournament handicap variability varied from a high of 144 to a low of 123, producing a range of 21. While the range for the team handicap variability is three less than the individual tournament handicap variability, Fig. 2 shows a greater dispersion of golfers with either high or low tournament handicaps when optimizing team variability than is observed when the individual players' tournament handicap variability is minimized. Thus, individual golfers might view the teams formed by minimizing the players' tournament handicap variability as being fairer overall than those formed by minimizing team handicap variability. It should be noted, however, that this is a much more dif<sup>fi</sup>cult problem to solve, requiring hours of solution time.

![](/api/attachments/S9PBP89P/fulltext/images/73dd8abdaace66df82497fda75724c167c64b5ead8e2ac19a2a25bde998e21e5.jpg)

<table><tr><td>Max Handicap</td><td>50</td></tr><tr><td>Min Handicap</td><td>39</td></tr><tr><td>Range</td><td>11</td></tr></table>

Fig. 1. Minimized team handicap variability

Tournament Handicap Variability  
![](/api/attachments/S9PBP89P/fulltext/images/b640e20b3ffa847d712f3ab8815562afdb00e7e860441f23deed00e8d299e14b.jpg)

<table><tr><td></td><td>Individual Variability</td><td>Team Variability</td></tr><tr><td>Max Tournament Handicap</td><td>144</td><td>143</td></tr><tr><td>Min Tournament Handicap</td><td>123</td><td>125</td></tr><tr><td>Range</td><td>21</td><td>18</td></tr></table>

Fig. 2. Individual player tournament handicap based on minimum variability.

Recall that the golf coach had speci<sup>fi</sup>c side-constraints preventing some players from being on the same team, and requiring other players to be on the same team. Such sideconstraints may greatly affect the overall quality of the solution.

For example, in Fig. 1 there are two relatively advantaged teams and two relatively disadvantaged teams. The two relatively advantaged teams result from the two side-constraints produced by condition A in Table 3, requiring the top player in <sup>fl</sup>ight 4 to be paired with the top 2 players from <sup>fl</sup>ight 2. To demonstrate this side-constraint's effect, we ran the same models as before, but with these two side-constraints removed. Fig. 3 displays the resulting solution. By removing these two side-constraints, the solution improves signi<sup>fi</sup>cantly. The range in team variability changes from 11 to three with a maximum team handicap of 47 and a minimum team handicap of 44. Moreover, Fig. 4 shows the individual player tournament handicaps for the model with all side-constraints present and the same two side-constraints removed. The range in handicap improves by 17 shots when the two side-constraints are removed.

Team Handicap Variability  
![](/api/attachments/S9PBP89P/fulltext/images/e69028878ac607a9fd30ac6f37e63d338ea9cc8b7b145015ac33e0725f5bd1a3.jpg)

<table><tr><td></td><td>Less Two Constraints</td><td>All Constraints</td></tr><tr><td>Max Handicap</td><td>47</td><td>50</td></tr><tr><td>Min Handicap</td><td>44</td><td>39</td></tr><tr><td>Range</td><td>3</td><td>11</td></tr></table>

Fig. 3. Minimized team handicap variability with all constraints and less two constraints.

![](/api/attachments/S9PBP89P/fulltext/images/37f97f78b66709a379ade222352a2fba6d766f0d36ee57a32cddd1e7508cee54.jpg)

<table><tr><td></td><td>Less Two Constraints</td><td>All Constraints</td></tr><tr><td>Max Tournament Handicap</td><td>139</td><td>144</td></tr><tr><td>Min Tournament Handicap</td><td>135</td><td>123</td></tr><tr><td>Range</td><td>4</td><td>21</td></tr></table>

Fig. 4. Individual player tournament handicap based on minimum variability

This type of “what-if” analysis represents an important decision tool for the golf coach in understanding the impact of side-constraints on the fairness of teams within the tournament and underscores the value of our proposed DSS. The MUGS DSS allows the coach to <sup>fi</sup>nd various solutions to the problem, presents a graphical and numerical summary of the problem, and visually highlights potential tournament unfairness. The golf coach can then decide if pairing or separating certain players is worth the potential (or actualized) increase in unfairness across teams.

Another bene<sup>fi</sup>t of the DSS proposed in this research is the option of alternate objective functions. The objective function presented earlier is based on minimizing the sum of absolute deviations $\left( \mathrm { L } _ { 1 } { - } \mathrm { N o r m } \right)$ for the variation in team handicap for the tournament. An alternate objective function would minimize the range between the maximum team handicap and the minimum team handicap. While this particular objective function may not always yield a fairer tournament, it could be useful in the presence of certain side-constraints.

Table 4 summarizes the numerical results from using four different objectives on the problem with all constraints present (denoted by “All Constraints”) and with the two side-constraints identi<sup>fi</sup>ed by condition A in Table 3 removed (denoted by “Less Two Constraints”). The four objectives considered are identi<sup>fi</sup>ed as: 1) Team Variability (minimize team handicap variability or L -Norm), 2) Team Range (minimize team handicap range), 3) Individual Variability (minimize individual tournament handicap variability or $\mathrm { L } _ { 1 } -$ Norm), 4) Individual Range (minimize individual tournament handicap range). The shaded cells represent the optimal objective function value for each particular model.

Comparing the <sup>fi</sup>rst four rows of data in Table 4 with the last four rows quickly allows the golf coach to assess the impact of the relevant side-constraints on the variability, range, and maximum and minimum values of the team handicaps and individual tournament handicaps. Again, only the golf coach can decide if the bene<sup>fi</sup>t of enforcing the sideconstraints is worth the cost it requires in terms of reducing the various “fairness” metrics. Similarly, pairwise comparisons of the rows of data in Table 4 may yield other insights. For instance, the solution obtained by minimizing the range of team handicaps (shown in the second row of the table) dominates, or is as good as or better than, the solution obtained by minimizing the variability of team handicaps (shown in the <sup>fi</sup>rst row).

Comparison of results for different objectives and constraints

<table><tr><td rowspan="2" colspan="2">Objective</td><td colspan="4">Team handicap</td><td colspan="4">Individual tournament handicap</td></tr><tr><td> $L_{1}$ -Nom</td><td>Range</td><td>Max</td><td>Min</td><td> $L_{1}$ -Nom</td><td>Range</td><td>Max</td><td>Min</td></tr><tr><td rowspan="4">All constraints</td><td>Team variability</td><td>26</td><td>11</td><td>50</td><td>39</td><td>98</td><td>18</td><td>143</td><td>125</td></tr><tr><td>Team range</td><td>26</td><td>8</td><td>47</td><td>39</td><td>92</td><td>15</td><td>140</td><td>125</td></tr><tr><td>Individual variability</td><td>52</td><td>11</td><td>50</td><td>39</td><td>70</td><td>21</td><td>144</td><td>123</td></tr><tr><td>Individual range</td><td>46</td><td>10</td><td>49</td><td>39</td><td>104</td><td>14</td><td>141</td><td>127</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">Less two constraints</td><td>Team variability</td><td>6</td><td>3</td><td>47</td><td>44</td><td>22</td><td>4</td><td>139</td><td>135</td></tr><tr><td>Team range</td><td>6</td><td>3</td><td>47</td><td>44</td><td>24</td><td>5</td><td>140</td><td>135</td></tr><tr><td>Individual variability</td><td>12</td><td>3</td><td>47</td><td>44</td><td>22</td><td>4</td><td>139</td><td>135</td></tr><tr><td>Individual range</td><td>24</td><td>5</td><td>49</td><td>44</td><td>34</td><td>3</td><td>140</td><td>137</td></tr></table>

## 6. Additional computational testing

The foregoing discussion presented the results for a DSS that matched the technical skills of our target user. This user had minimal background in optimization methods and little interest in gaining such expertise. We therefore tried to streamline our approach as much as possible, ignoring possible technical improvements. In particular, we did little tuning of the optimization algorithm, using just the default values. While we might have obtained improved results on our example by tuning the parameters, we had little real data to allow us to measure the robustness of any changes, and we did not have con<sup>fi</sup>dence in how generalizable the results from arti<sup>fi</sup>cial data would be.

Without more “real” data, any comment on generalizability must necessarily be speculative, but we have performed further testing on arti<sup>fi</sup>cial data and can provide some guidance. For our testing, we generated random instances with varying numbers of golfers, handicaps and days. In order to match up with real-world aspects, our instances had the following characteristics:

## 1. The golfers are divided into four <sup>fl</sup>ights, and

2. Golfers in <sup>fl</sup>ight 1 are all scratch (0 handicap golfers); those in <sup>fl</sup>ight 2 have handicaps uniformly distributed from 1– 10; those in <sup>fl</sup>ight 3 have handicaps uniformly distributed from 11–20; those in <sup>fl</sup>ight 4 have handicaps uniformly distributed from 21–30.

The <sup>fi</sup>rst characteristic is due to the “foursome” aspect of competitive golf: more players do not typically result in larger playing groups. The second characteristic re<sup>fl</sup>ects real-world handicaps: golfers with handicaps much over 30 are unlikely to <sup>fi</sup>nd golf a particularly satisfying way of spending an afternoon.

We solved <sup>fi</sup>ve instances of each of four sizes, corresponding to 24, 44, 60, and 72 players. The maximum of 72 players is reasonable for this application as that corresponds to having a “shotgun start” where one foursome begins at each of the 18 holes on a golf course and the players begin their rounds simultaneously. Tournaments with more than 72 players would likely be divided into smaller groups for scheduling.

Table 5 gives the results for each of the 20 instances. In the table, we report the initial relaxation value (Initial), the <sup>fi</sup>nal solution value (Final), where an “⁎” indicates the solution was not proved optimal, the number of nodes in the branch and bound tree (Nodes), and the computation time in seconds (Time). Our machine for this test had a 2.2 GHz processor and 2 GB of memory. Here we used OPL 3.7 with CPLEX as the solver. We set a time limit of 1800 s (one half hour) for the two smaller instance sizes and 21,600 s (6 h) for the larger instance sizes, corresponding to roughly an overnight run.

There are striking aspects of this test. First, it is clear that the lower bound of this formulation is very tight; very few of the solved instances had an optimal solution not equal to this lower bound. Second, the approach works well for up to 60 players, but 72 players take more time than most users would desire. This is not due to the size of the branch and bound tree; the tree remains small, but the instances become so large (with more than 300,000 variables) that the underlying linear programs take a long time to solve. Third, some instances are very dif<sup>fi</sup>cult to solve to optimality. We let instance 44b run for more than 14,000 s until it ran out of memory having explored more than 76,000 nodes in the branch and bound tree without proving 4 as the optimal solution (or <sup>fi</sup>nding a better solution).

Table 5  
Additional computational testing

<table><tr><td>Problem</td><td>Players</td><td>Initial</td><td>Final</td><td>Nodes</td><td>Time</td></tr><tr><td>24a</td><td>24</td><td>25</td><td>25</td><td>80</td><td>7.5</td></tr><tr><td>24b</td><td>24</td><td>15</td><td>15</td><td>2090</td><td>38.8</td></tr><tr><td>24c</td><td>24</td><td>17</td><td>19</td><td>11989</td><td>157.8</td></tr><tr><td>24d</td><td>24</td><td>11</td><td>11</td><td>253</td><td>8.9</td></tr><tr><td>24e</td><td>24</td><td>22</td><td>22</td><td>137</td><td>10.9</td></tr><tr><td>44a</td><td>44</td><td>23</td><td>23</td><td>30</td><td>253.4</td></tr><tr><td>44b</td><td>44</td><td>2</td><td>4*</td><td>3088</td><td>1800.0</td></tr><tr><td>44c</td><td>44</td><td>21</td><td>21</td><td>10</td><td>131.6</td></tr><tr><td>44d</td><td>44</td><td>7</td><td>7</td><td>0</td><td>57.2</td></tr><tr><td>44e</td><td>44</td><td>21</td><td>21</td><td>0</td><td>50.6</td></tr><tr><td>60a</td><td>60</td><td>30</td><td>30</td><td>10</td><td>672</td></tr><tr><td>60b</td><td>60</td><td>42</td><td>42</td><td>39</td><td>2,672</td></tr><tr><td>60c</td><td>60</td><td>15</td><td>15</td><td>10</td><td>893</td></tr><tr><td>60d</td><td>60</td><td>36</td><td>36</td><td>29</td><td>1,355</td></tr><tr><td>60e</td><td>60</td><td>6</td><td>6</td><td>30</td><td>2,943</td></tr><tr><td>72a</td><td>72</td><td>3</td><td>3</td><td>30</td><td>19,261</td></tr><tr><td>72b</td><td>72</td><td>6</td><td>6</td><td>30</td><td>14,769</td></tr><tr><td>72c</td><td>72</td><td>30</td><td>30</td><td>30</td><td>4,670</td></tr><tr><td>72d</td><td>72</td><td>48</td><td>48</td><td>48</td><td>6,634</td></tr><tr><td>72e</td><td>72</td><td>6</td><td>6</td><td>30</td><td>6632</td></tr></table>

Because instance 44b quickly (in under 5 min) found the nearoptimal solution with value 4, we conclude that this approach is reasonable for the 24 and 44 player sizes, and is adequate for a patient user for the 60 player sizes. Larger instances will require overnight runs, but are still generally solvable. It is unlikely that any real-world application will have more than 72 players; so we believe this approach is suitable for real-world use, if we can extrapolate from random instances to the real-world.

We again note that trying to minimize the tournament handicaps of the individual players is much more time consuming. Our examples of this type of problem in the previous section required hours of computation and were still unable to prove global optimality. However, we again note that the assistant golf coach previously would spend hours trying to manually identify feasible solutions to the problem. Thus, we are con<sup>fi</sup>dent the coach would be happy to let a computer spend those hours working on <sup>fi</sup>nding optimal (or near-optimal) solutions while he gives his attention to other matters.

## 7. Implications and conclusion

Competition among universities to attract talented athletes drives athletic programs to offer scholarships and provide adequate resources for team players. For the programs that do not attract high visibility or high dollar support from their institutions, it is imperative to encourage external donor contribution. In many cases, golf tournaments involving current or potential donors are often a key element in fundraising efforts. To create a positive experience for donors, it is important to make these golf tournaments enjoyable by creating teams with comparable skill levels. To enhance the effectiveness of fundraising efforts, it is sometimes important to ensure that certain people are paired together on teams. This is not an easy task for the organizers of such events, and there are no readily available tools to create balanced and properly paired teams.

This paper introduces a new variation on the golf scramble problem, called the MUGS problem, and describes a spreadsheet-based decision support tool that allows tournament organizers to solve it. Because creating a fair golf tournament is dif<sup>fi</sup>cult, this tool provides a more appropriate means to solve the problem than by hand. The model allows for speci<sup>fi</sup>c pairing of individuals, creates new teams for each day, and balances the skills of all teams to ensure the greatest level of competition and enjoyment. The decision maker may choose alternate objective functions or vary the side-constraints thus allowing for greater tournament options. While the golf coach who initially brought this problem to our attention struggled to <sup>fi</sup>nd feasible solutions to the problem, this DSS not only <sup>fi</sup>nds feasible solutions but allows its user to compare and select among a number of solutions obtained by optimizing a variety of objectives. Schools that use multi-round golf tournaments as part of their development efforts could bene<sup>fi</sup>t from this type of DSS.

In terms of future research, the type of DSS presented here could also be of value for other team creation tasks. For example, it may be possible to adapt this type of DSS for other metrics such as GMAT scores for MBA team assignments. Cutshall, Gavirneni, and Schultz [8] used integer programming to form fair and balanced teams at Indiana University's Kelley School of Business core classes. Some differences between their approach and ours are that they use multiple objectives whereas we use one, and, secondly, they do not account for multiple periods while we do. A logical extension to this research is to develop a DSS that will take a pool of students and fairly group them for multiple periods (e.g. quarters, semesters, years) and multiple objectives such as sex, GMAT scores, GPA, race.

## References

[1] J. Armstrong, R.J. Willis, Scheduling the Cricket World Cup—a casestudy, Journal of the Operational Research Society 44 (11) (1993) 1067.

[2] T. Bartsch, A. Drexl, S. Kroger, Scheduling the Professional Soccer Leagues o Austria and Germany, Computers & Operations Research 33 (7) (2006) 1907.

[3] P.K. Bergey, C.T. Ragsdale, M. Hoskote, A decision support system for the electrical power districting problem, Decision Support Systems 36 (1) (2003) 1–17.

[4] A. Bruinshoofd, B. ter Weel, Manager to go? Performance dips reconsidered with evidence from Dutch football. European Journal of Operational Research 148 (2) (2003) 233.

[5] U. Buehlmann, C.T. Ragsdale, B. Gfeller, A spreadsheet-based decision support system for wood panel manufacturing, Decision Support Systems 29 (3) (2000) 207-227.

[6] Y.E. Chan, V.C. Storey, The use of spreadsheets in organizations: determinants and consequences, Information and Management 31 (3) (1996) 119–134.

[7] D. Conway, C. Ragsdale, Modeling optimization problems in the unstructured world of spreadsheets, Omega 25 (3) (1997) 313–322.

[8] R. Cutshall, S. Gavirneni, K. Schultz, Indiana University's Kelley School of Business uses integer programming to form equitable, cohesive student teams, Interfaces 37 (3) (2007) 265–276.

[9] D. de Werra, Some models of graphs for scheduling sports competitions Discrete Applied Mathematics 21 (1) (1988) 47–65.

[10] R. Dear, Z. Drezner, Applying combinatorial optimization metaheuristics to the golf scramble problem, International Transactions in Operationa Research 7 (4–5) (2000) 331-347.

[11] F. Della Croce, D. Oliveri, Scheduling the Italian Football League: an Ilpbased approach, Computers & Operations Research 33 (7) (2006) 1963.

[12] F. Della Croce, R. Tadei, P.S. Asioli, Scheduling a round robin tennis tournament under courts and players availability constraints, Annals of Operations Research 92 (1999) 349.

[13] S. Dobson, J. Goddard, Persistence in sequences of football match results: a Monte Carlo analysis, European Journal of Operationa Research 148 (2) (2003) 247

[14] A. Drexl, S. Knust, Sports League Scheduling: Graph- and Resource-Based Models, Omega 35 (5) (2007) 465.

[15] P.D. Francis Scheid, Golf competition between individuals, Proceedings of the 11th Conference on Winter Simulation—Volume 2. IEEE Press. San Diego, CA, United States, 1979.

[16] FrontLine Systems Incorporated, Premium Solver Platform, Incline Village, NV, 1999.

[17] C. Hall, C. Swartz, The effect of handicap stroke location on best-ball golf scores, Mathematical Modelling 2 (3) (1981) 161.

[18] C. Hall, C. Swartz, The effect of handicap stroke location on golf matches, Mathematical Modelling 2 (3) (1981) 153.

[19] J.P. Hamiez, J.K. Hao, Solving the sports league scheduling problem with Tabu search, Lecture Notes in Computer Science, 2001.

[20] J.P. Hamiez, J.K. Hao, A linear-time algorithm to solve the sports league scheduling problem (Prob026 of Csplib), Discrete Applied Mathematics 143 (1–3) (2004) 252.

[21] M. Henz, Scheduling a major college basketball conference—revisited, Operations Research 49 (1) (2001) 163.

[22] M. Henz, T. Muller, S. Thiel, Global constraints for round robin tournament scheduling, European Journal of Operational Research 153 (1) (2004) 92.

[23] ILOG, Cplex, http://www.ilog.com/products/cplex/.

[24] F.J.G.M. Klaassen, J.R. Magnus, Forecasting the winner of a tennis match, European Journal of Operational Research 148 (2) (2003) 257.

[25] R.H. Koning, M. Koolhaas, G. Renes, G. Ridder, A simulation model for football championships, European Journal of Operational Research 148 (2) (2003) 268.

[26] Lindo, Chicago, IL, 2007.

[27] R.E. Litan, J.M. Orszag, P.R. Orszag, The Empirical Effects of Collegiate Athletics: An Interim Report, National Collegiate Athletic Association. 2003, p. 53

[28] S.T. March, A.R. Hevner, Integrated Decision Support Systems: A Data Warehousing Perspective, Decision Support Systems 43 (3) (2007) 1031.

[29] T.J. McGill, J.E. Klobas, The role of spreadsheet knowledge in user-developed application success, Decision Support Systems 39 (3) (2005) 355–369.

[30] J.E. Mitchell, Realignment in the National Football League: did they do it right? Naval Research Logistics 50 (7) (2003) 683.

[31] G.L. Nemhauser, M.A. Trick, Scheduling a major college basketball conference, Operations Research 46 (1) (1998) 1–8.

[32] D.C. Novak, C.T. Ragsdale, A decision support methodology for stochastic multi-criteria linear programming using spreadsheets, Decision Support Systems 36 (1) (2003) 99–116.

[33] S.M. Pollock, Model for evaluating golf handicapping, Operations Research 22 (5) (1974) 1040.

[34] R.V. Rasmussen, M.A. Trick, A Benders Approach for the Constrained Minimum Break Problem, European Journal of Operational Research 177 (1) (2007) 198.

[35] R.A. Russell, J.M.Y. Leung, Devising a cost-effective schedule for a baseball league, Operations Research 42 (4) (1994) 614.

[36] R.A. Russell, T.L. Urban, A constraint programming approach to the multiple-venue, sport-scheduling problem, Computers & Operations Research 33 (7) (2006) 1895.

[37] R.M. Saltzman, R.M. Bradford, Optimal realignments of the teams in the National Football League, European Journal of Operational Research 93 (3) (1996) 469.

[38] F. Scheid, Least-squares family of cubic curves with an application to golf handicapping, Siam Journal on Applied Mathematics 22 (1) (1972) 77.

[39] F.J. Scheid, Nonlinear feature of golf course rating with application to handicapping, Siam Review 17 (2) (1975) 388.

[40] J. Schonberger, D.C. Mattfeld, H. Kopfer, Memetic algorithm timetabling for non-commercial sport leagues, European Journal of Operational Research 153 (1) (2004) 102

[41] J.A.M. Schreuder, Combinatorial aspects of construction of competition Dutch-professional-football-leagues, Discrete Applied Mathematics 35 (3) (1992) 301.

[42] L.A. Smith, I. Prockow, Simulating a match play handicapping system, Simulation & Gaming 12 (4) (1981) 417.

[43] A. Suzuka, R. Miyashiro, A. Yoshise, T. Matsui, Semide<sup>fi</sup>nite programming based approaches to home-away assignment problems in sports scheduling, Algorithmic Applications in Management, Proceedings, Springer-Verlag Berlin, Berlin, 2005, p. 95.

[44] M.A. Trick, Integer and constraint programming approaches for roundrobin tournament scheduling, Practice and Theory of Automated Timetabling IV, Springer-Verlag Berlin, Berlin, 2003, p. 63.

[45] M.A. Trick, A schedule-then-break approach to sports timetabling, Practice and Theory of Automated Timetabling III: Third International Conference, Patat 2000 Konstanz, Germany, August 16–18, 2000, Selected Papers. Springer Berlin / Heidelberg, Berlin, 2001, p. 242

[46] T.L. Urban, R.A. Russell, Scheduling sports competitions on multiple venues, European Journal of Operational Research 148 (2) (2003) 302.

[47] T. Van Voorhis, College basketball scheduling with travel swings, Computers & Industrial Engineering 48 (2) (2005) 163

[48] T. Van Voorhis, Highly constrained college basketball scheduling, Journal of the Operational Research Society 53 (6) (2002) 603.

[49] A. van Weert, J.A.M. Schreuder, Construction of basic match schedules for sports competitions by using graph theory, Practice and Theory of Automated Timetabling Ii, Springer-Verlag, Berlin, 1998, p. 201.

[50] M.B. Wright, Scheduling <sup>fi</sup>xtures for basketball New Zealand, Computers & Operations Research 33 (7) (2006) 1875.

Cliff T. Ragsdale is a Bank of America Professor of Business Information Technology in the Pamplin College of Business at Virginia Tech. He received his Ph.D. in Management Science and Information Technology from the University of Georgia. He also holds an M.B.A. in Finance and B.A. in Psychology from the University of Central Florida. Dr. Ragsdale's primary area of research interest center on the integration of computers, mathematics, and arti<sup>fi</sup>cial intelligence to solve business problems. He is a member of INFORMS, AIS and DSI. He has published in a variety of journals including Decision Sciences, Decision Support Systems, Naval Research Logistics, and OMEGA. He also serves on the Advisory Boards of INFORMS Transactions on Education and the International Journal of Information Technology & Decision Making. He is also author of the textbook Spreadsheet Modeling and Decision Analysis, 5ed published by South-Western.

Kevin P. Scheibe is an Assistant Professor of Management Information Systems at Iowa State University. His research interests include decision support systems, IT privacy and security, supply chain risk, wireless telecommunications, and IT outsourcing. He is a member of the Association for Information Systems and the Decision Sciences Institute. Dr. Scheibe has published in journals such as Decision Support Systems, Journal of Information Privacy and Security, Computers and Electronics in Agriculture and Computers in Human Behavior. He received his PhD. from Virginia Polytechnic Institute and State University.

Michael A. Trick is Professor of Operations Research at the Tepper School of Business, Carnegie Mellon University, where he has been on faculty since 1989. His research interests are in computational integer programming, constraint programming, and applications in sports. He received his Ph.D. from the School of Industrial and Systems Engineering at the Georgia Institute of Technology. In 2002, he was President of INFORMS and he is currently a Vice President of the International Federation of Operational Research Societies. He has consulted extensively with the United States Postal Service, the Internal Revenue Service and many sports leagues, including Major League Baseball. He is a Fellow of INFORMS.
