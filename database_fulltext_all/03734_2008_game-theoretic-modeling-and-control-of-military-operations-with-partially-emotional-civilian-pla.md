---
otero_id: 3734
otero_key: "ZQCUKFPB"
title: "Game-theoretic modeling and control of military operations with partially emotional civilian players"
authors: "Mo Wei; Genshe Chen; Jose B. Cruz; Leonard Hayes; Martin Kruger; Erik Blasch"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.07.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Game-theoretic modeling and control of military operations with partially emotional civilian players

Mo Wei, Genshe Chen <sup>⁎</sup>, Jose B. Cruz Jr., Leonard Hayes, Martin Kruger, Erik Blasch

Intelligent Automation, Inc, 15400 Calhoun Dr., Suite 400, Rockville, MD 20855, USA

Received 2 June 2006; received in revised form 23 July 2007; accepted 26 July 2007 Available online 6 August 2007

## Abstract

Civilians are not just passively static but might purposefully take actions to help one side in a battle. Sometimes civilians might directly join one side if they are excessively agitated by the other side. In this paper, a three-player attrition-type discrete time dynamic game model is formulated, in which there are two opposing forces and one civilian player that might be neutral, biased, or even joining one side publicly. Emotions of civilians are dynamically updated via anger mechanism. An example scenario and extensive simulations illustrate possible applications of this model, and comparative discussions further clarify the benefits. © 2007 Elsevier B.V. All rights reserved.

Keywords: Attrition-like model; Civilian player; Emotion; Game theory

## 1. Introduction

In recent years substantial effort has been devoted to modeling and control of enterprises which are controlled by two or more teams of, possibly adversarial, decision agents. Attrition-type models were proposed to model such situations as accurately as possible [2,3,8,12,13,17,21]. The foundation of these models is the mathematical analysis for attritions of forces in an air combat [11,14,22] developed by Lanchester in 1916. Since the models were not expressed using the state space approach and hence were not amenable to the application of results from modern optimal control and dynamic game theories [1,6,19,20], Cruz et al. [7] extended the model to dynamic discrete time state space, which greatly facilitated the combination of attrition-type models and modern computer-aided game theoretic analyses. Furthermore, some scientists have written papers on collateral damage calculations [4,9,23] and in one paper [5] collateral damage was considered in a non-zero sum game setting to deal with possible asymmetric adversaries in battlefields and to model the influences of civilians in modern wars. A typical such model is stated in Eq. (1).

The game situation represented in Eq. (1) consists of at least three aspects of asymmetry: 1) the asymmetry about the attrition weights; 2) asymmetry about the input sets; and 3) asymmetry about the assessments/ tolerances.

$$
\begin{array}{l} J ^ {B} = B _ {f} + B _ {b} - 0. 2 R _ {f} - 0. 3 R _ {b} + W \\ J ^ {R} = - 1. 5 B _ {f} - 2. 3 B _ {b} + R _ {f} + R _ {b} \end{array}\tag{1}
$$

where $J ^ { B }$ and $J ^ { R }$ are the normalized payoff functions being maximizing by Blue and Red (the labels of two fighting forces), respectively. $B _ { f }$ and $B _ { b }$ are the values of undestroyed Blue fighters and Blue bombers, respectively. $R _ { f }$ and $R _ { b }$ are the counterparts of the Red side. W is the value of undestroyed (neutral) civilian. The differences between the absolute values of the coefficients of $B _ { f } ^ { > } \mathrm { s }$ stand for the first asymmetry and implies that Red cares more about destroying the enemy than keeping themselves safe. The coefficients of W stands for the fact that Red might not care about damages of the civilian properties while Blue does care. Blue and Red can choose inputs from different sets, say $u ^ { B }$ and $u ^ { R } ,$ respectively, to update $B _ { f } , B _ { b } , R _ { f } , R _ { b } ,$ , and $J ^ { B }$ and $J ^ { R }$ Their own input sets might be different according to different technology levels, financial status, morale, etc., which stand for the second asymmetry. Blue and Red will assess $J ^ { B }$ and $J ^ { R }$ according to different standard, which will stand for the third asymmetry. For example, a 10,000 soldier/platform casualty might be intolerable for Blue while Red can easily ignore such casualty.

It seems that the modeling methodology illustrated by Eq. (1) is reasonable because it is easy to deal with classical game framework. However, as pointed out in [25], it has a key disadvantage: civilians are treated as “passive objects” without any desires or capabilities to take actions to affect Blue or Red. In this way, the strategies of Blue and Red have effect on neutral people, while the neutral civilians can only passively watch the battle process and do not take an active role. In a coarse scenario, this might be reasonable. However, in modern counter-strike wars, such as the Iraqi War, it has been observed that the “neutral” civilians either have intent and capabilities or threatened by insurgents so that they would do or have to do something to maximize their own benefits. For example, if civilian people guess that there might be battles around their block, they might consolidate or build up more and higher walls to protect themselves, which might cause more obstacles for missiles and heavy weapons. Moreover, some people might think the existence of US forces in Iraq is undesirable no matter how US forces do favors for them. Therefore, they show some sympathy to insurgents. Suicide bomber commanders might threaten civilians to help terrorists hide and attack, too.

Under such situations, civilians are slightly adversarial to US force and not exactly “neutral”. Although US forces know this perfectly, US forces cannot treat them as enemies due to some social–political–military constraints. However, US forces should at least be able to consider the effect of courses of actions (COAs) of such “slightly adversarial civilian” and base decisionmaking on the combination of COAs from both enemy and such civilians. In other words, a more accurate tool should be developed to model neutral civilian as a “White” player and considering the coupling between civilian’s actions and Blue/Red payoffs. This will allow Blue player to make decisions on a more comprehensive and accurate background and greatly reduce unnecessary losses. Based on the above simple argument, a more accurate model for such a scenario might be a 3-player game represented by Eq. (2)

$$
\begin{array}{l} J ^ {B} = B _ {f} + B _ {b} - 0. 2 R _ {f} - 0. 3 R _ {b} + W \\ J ^ {R} = - 1. 5 B _ {f} - 2. 3 B _ {b} + R _ {f} + R _ {b} \\ J ^ {W} = - 0. 0 0 1 B _ {f} - 0. 0 0 1 B _ {b} + 0. 0 0 1 R _ {f} + 0. 0 0 1 R _ {b} + W \end{array}\tag{2}
$$

where $J ^ { W }$ is the payoff of the civilian player and the civilian player also deserves an input set $\mathbf { \Delta } \stackrel { \bullet } { u } ^ { W } .$ In this way, civilians are treated as a player that is at the same level with two opposing forces, which are often labeled as Blue Force and Red Force.

In addition, as many researchers [10,15,18] pointed out, emotion plays an important role in decision making almost everywhere. No one is absolutely rational, especially for civilians in battlefield. This is because civilians are not militarily organized and their emotions can vary greatly if they experience collateral damages from different forces. Driven by angers, sometimes they might purposefully affect the battlefield or even publicly join one side of the fighting forces.

In the model stated in Eq. (2), civilians are ideally rational, that is to say, without any emotions. It does not analyze situations such as what a civilian family will think or do when a member would be killed or their house is destroyed by one force in an attack. If Blue or Red collaterally damages a civilian family, the relatives might deeply hate Blue or Red, respectively, and take non-cooperative or even adversarial actions to affect the battle. Such actions might be telling one side (say Red) everything they know about the other side (say Blue) while telling the other side “slightly misleading” information or simply keeping silent when asked by the other side, or directly join the Red force to fight against Blue. Quantitatively modeling such emotion dynamics in battlefield could refine the model stated in $\operatorname { E q . }$ (2) via modeling the civilian player as partially rational and partially emotional.

To the best knowledge of the authors, existing tools for modeling and control of military air operations do not explicitly consider the civilians as a role that can act partially rational and partially emotional. In this paper, we formulate a multiple-players attrition-type discrete time dynamic game model, in which there are two

opposing forces and one partially emotional civilian player that might be neutral or slightly biased to one side. The main idea of this paper is to expand the research in [25] so that the model can be dynamically adapted to cope with changes in civilian player's attitude during the battle environment. We model the objective functions, control strategies of different players, and identify the associated constraints on the control and state variables. In this new model, all players are exactly at the same level, and each of them will have desires and capabilities to affect other players. In addition, civilians have dynamic emotion and rationality. Traditional models will be special cases of this new model. Via this model, asymmetric features of modern military situations can be more accurately captured. Thus, the generated control strategies could be more reasonable. The model can be easily extended to hierarchical situations, in which each player might have several sub-teams following similar approaches stated in [7].

This paper is organized as follows. In Section 2, we will summarize the technical approach, which includes problem description, identification and modeling of state variables, commands and controls, state equations, emotions, objective functions, and calculation of optimal control strategies. Section 3 describes the experimental results and explanations. Section 4 provides conclusions for the paper.

## 2. Technical approach of attrition model with emotional civilian player

Suppose a military operation is ongoing in a battlefield, say a city district, where there are Unmanned Aerial Vehicles (UAVs), Unmanned Ground Vehicles (UGVs), removable Surface-to-Air Missile (SAM) defense systems, Rocket Propelled Grenade (RPG) launchers, and other possible weapon platforms. These weapon platforms belong to two opposing forces, labeled as Blue and Red, respectively. Each force wishes to destroy the platforms of the foe as much as possible while at the same time maximizing its own remaining platforms. In this district, there are civilians that are labeled as White, and Red platform operators often hide themselves among these civilians. Since some Red platform operators are previously civilians living in the battlefield district or other close districts, the civilians in the battlefield initially show slight sympathy to the Red platform operators. This implies that although the civilians’ focus is to minimize the losses of their properties, they might still feel a little “happy” when Blue loses something or Red gains something. In addition, the civilians might historically have an initial “action bias” which tends to slightly “help” Red due to various reasons, such as literature, religion, language, etc.

The civilians' preferences may change during the battle. If they feel their initial strategy is not the best way to minimize loss, they might change their action mode and choose to help Red more or simply help Blue according to some reasonable goals. If they are excessively agitated, they might even join Red or Blue. Obviously, the adaptations of civilians will affect both Blue and Red, while at the same time Blue and Red's choices will affect civilians' action, too. Due to the tight coupling among one another, a multiple player state-space game will be a good model. The basic logic is to model the civilians as a rational White civilian player if they are not excessively agitated, and model them as part of Blue or Red if they are once excessively agitated. This is because if a civilian platform is too angry at one force, it might join the enemy of that force and will not be a civilian platform any more.

## 2.1. State vector of the entities

Let $N ^ { B } ( k ) , N ^ { R } ( k )$ , and $N ^ { W } ( k )$ denote the number of entities (platforms) of Blue, Red, and White, respectively, at timestep k. The White platforms might be considered as blocks with arbitrary sizes that can calculate their losses and implement some COAs based on those calculations. To facilitate computer analyses, we assume that time is sampled into stages $k { = } 0 , 1 , 2 { \mathrm { , . . . , } } K .$ Corresponding continuous time model can be derived accordingly and will be considered as an extension of this model later. Consider the ith platform of type X, where X is an element of set $\{ B , R , W \}$ . We use Eq. (3)

$$
e _ {i} ^ {X} (k) = \left\{ \begin{array}{c l} [ x _ {i} ^ {X} (k) y _ {i} ^ {X} (k) z _ {i} ^ {X} (k) t _ {i} ^ {X} (k) f _ {i} ^ {X} (k) v _ {i} ^ {X} (k) ] ^ {T}, & \text {if X\in\{B,R\}} \\ [ x _ {i} ^ {X} (k) y _ {i} ^ {X} (k) z _ {i} ^ {X} (k) t _ {i} ^ {X} (k) f _ {i} ^ {X} (k) v _ {i} ^ {X} (k) \\ ... g _ {i} ^ {X} (k) g t _ {i} ^ {X} (k) g f _ {i} ^ {X} (k) ] ^ {T}, & \text {if X\in\{W\}} \end{array} \right.\tag{3}
$$

where $i = 1 , 2 , \dots , N ^ { X }$ ; and $k = 0 , 1 , 2 , \ldots , K$ to denote the ith platform's location, number of weapons, and <sup>¼ ¼</sup>remaining value at time k. The superscript Tstands for matrix transpose. Note the difference between the superscript (capital) X and the vector element x. Similarly for the transpose symbol T and vector element t.

$x _ { i } ^ { X } ( k ) , y _ { i } ^ { X } ( k ) .$ , and $ z _ { i } ^ { X } ( k )$ are the corresponding coordinates of the ith platform. $t _ { i } ^ { X } ( k )$ is the value of an individual weapon. $f _ { i } ^ { X } ( k )$ denotes the remaining number of weapons of ith platform. $\nu _ { i } ^ { X } ( k )$ is the total value of this platform, including the remaining weapons. If $\nu _ { i } ^ { X } ( k )$ is set to zero, it implies that the platform is destroyed and can not do anything, no matter how many weapons remain. At this time, for simplification, we assume a platform carries only one type of weapon, thus $t _ { i } ^ { X } ( k )$ is a constant for each $i . g _ { i } ^ { X } ( k )$ is an identity flag indicating whether this civilian platform is still civilian or not and will be set to zero when game starts.

$$
g _ {i} ^ {X} (k) = \left\{ \begin{array}{l l} 0, & \text { if   it   is   still   civilian } \\ 1, & \text { if   it   becomes   Red } \\ - 1, & \text { if   it   becomes   Blue } \end{array} \right.\tag{4}
$$

$g t _ { i } ^ { X } ( k )$ is the cost of a unit-size biased action from a civilian platform. $g f _ { i } ^ { X } ( k )$ is the possible maximum number of such unit-size biased actions from this civilian platform. When a civilian platform is still civilian, it can and only can make such biased actions to help or harm Blue or Red’s kill probabilities (see later sub-sections) while Blue and Red will still treat it as civilian. This is to say, after this biased action the civilian platform will still be civilian. Civilians can not use the weapons corresponding to ${ \bf \bar { \Psi } } _ { t _ { i } } X _ { \bf \bar { ( } k \bar { ) } }$ and $f _ { i } ^ { X } ( k )$ . In addition, even if Blue or Red knows the civilian platform is biased for enemy, they can not choose the civilian platform as target for firing. However, if a civilian platform becomes Red or Blue at some time point, it will do everything like a Red platform or Blue platform, such as using the weapons corresponding to $t _ { i } ^ { X } ( k )$ and $f _ { i } ^ { K } ( k )$ . From that time point, its superscript $W$ will become R or B. It is no longer “White” and will be treated as enemy by Blue or Red, respectively.

Note that after a civilian platform becomes a Blue or Red platform, it will be the same as an original Blue or Red platform in every aspect, respectively, including labeling, control variables and constraints, state update mechanisms, etc. In this paper we assume a Blue (or Red) platform can not become a Red (or Blue) platform within a battle. After a white civilian platform joins one side, say Blue, it can not come back (that is, become White again) or become Red.

## 2.2. Control variables and constraints

Each platform is subject to the following command/control variables at each time k.

## 2.2.1. Relocate control

Ask an undestroyed platform to stay at the current place or move to an adjacent grid. Based on precision requests, platform speeds, computational capabilities, and other factors, users will determine the size of the grid. The relocate control for the ith platform is

$$
r _ {i} ^ {X} (k) = \left[ r _ {i x} ^ {X} (k) r _ {i y} ^ {X} (k) r _ {i z} ^ {X} (k) \right] ^ {T}\tag{5}
$$

where each element of this vector is taken from the set {−1, 0, 1}. For every platform that can move 3-dimensionally, there are 27 choices. For moving-on-plane platforms such as UGVs, the number of choices is 9, and we assume the plane on which such platforms can move is the $x - y$ plane, which is illustrated in Fig. 1 (according to the format requirement, all figures are put at the end of the paper on separate pages).

![](/api/attachments/ZQCUKFPB/fulltext/images/4b4144e453433f8e47498768088570efd196c763dddaa010614e9c5d74b44d88.jpg)  
Fig. 1. Relocate control.

## 2.2.2. Fire control

Each undestroyed platform of type X will choose to fire with a salvo size $c _ { i } ^ { X } ( k )$ or not fire. $\mathrm { I f } X { \in } \{ B , R \} , c _ { i } ^ { X } ( k )$ is a non-negative integer which takes values from $[ 0 , f _ { i } ^ { X } ( k ) ] . \mathrm { I f } f _ { i } ^ { X } ( k )$ is already zero, this platform can not fire at any target. Note that in this model a civilian platform (White) can also $\mathrm { { \bar { \Omega } f i r e } ^ { \mathrm { { \infty } } } }$ , which means it will impose its biased action on a Red or Blue platform. According to the state equations that will be discussed later, this action might affect the kill probabilities of weapons fired from the targeted platform. When $X { = } W , c _ { i } ^ { X } ( k )$ is a positive or negative integer. When $c _ { i } ^ { X } ( k )$ is positive, it means that the action from this White platform is to help the target to improve the kill probability of the weapons launched. When $c _ { i } ^ { X } ( k )$ is negative, it is for reducing such kill probability.

## 2.2.3. Choice of target

Each undestroyed platform that wishes to fire upon the opposing force will have to select one target of the opposing force. In such situations, that is, when $X \in \{ B , R \}$ and the platform with type X wishes to fire, we use a positive integer $d _ { i } ^ { X } ( k )$ to denote the index of the targeted platform in the opposing force. If a White platform with type X wishes to fire at a target whose index is $q ( k )$ in the sequence of type Y platforms, then $d _ { i } ^ { X } ( k )$ is determined as follows

$$
d _ {i} ^ {X} (k) = q (k) s (Y)\tag{6}
$$

where

$$
s (Y) = \left\{ \begin{array}{l l} 1, & \text { if } \quad Y = B \\ - 1 & \text { if } \quad Y = B. \end{array} \right.\tag{7}
$$

If a platform does not fire, $d _ { i } ^ { X } ( k )$ will be set to zero no matter X is (B, R, or W).

Combining the controls, we get the following control vector for each platform:

$$
u _ {i} ^ {X} (k) = [ r _ {i x} ^ {X} (k) r _ {i y} ^ {X} (k) r _ {i z} ^ {X} (k) c _ {i} ^ {X} (k) d _ {i} ^ {X} (k) ] ^ {T}.\tag{8}
$$

## 2.2.4. Relocate-fire constraint

It is assumed that one time step from k to $k { + 1 }$ is the time required the fastest platform to move one position on the grid. Slower platform's relocate control can be modeled as activated after some number of time steps elapsed. In addition, to reduce computational complexity, it is assumed that a unit or platform can fire only at time k when $r _ { i } ^ { X } ( k ) =$ $r _ { i y } ^ { X } ( k ) = r _ { i z } ^ { X } ( k ) = 0$ . That is x

$$
\left| \left| r _ {i} ^ {X} (k) \right| \right| _ {\infty} + \operatorname{step} \left(c _ {i} ^ {X} (k) - 1\right) \leq 1\tag{9}
$$

where

$$
| | r _ {i} ^ {X} (k) | | _ {\infty} = \left\{ \begin{array}{l l} 0, & \text { if } \\ 1, & \text { otherwise } \end{array} \right. r _ {i x} ^ {X} (k) = r _ {i y} ^ {X} (k) = r _ {i z} ^ {X} (k) = 0\tag{10}
$$

and step(m) is the discrete time unit step sequence

$$
\operatorname{step} (m) = \left\{ \begin{array}{l l} 0, & m <   0 \\ 1, & \text { otherwise } \end{array} \right.\tag{11}
$$

## 2.2.5. Corridor

Some grids on the map might be appropriate for relocating units, while some grids might not. For different types of units, there might be different corridors. The relocate control should not command platforms into forbidden grids.

## 2.3. State equations

The following state equations calculate state variables at time $k { + 1 }$ based on the state variables and control variables at time k.

## 2.3.1. Position and weapon value

$$
x _ {i} ^ {X} (k + 1) = \left\{ \begin{array}{l l} x _ {i} ^ {X} (k) + r _ {i x} ^ {X} (k), & \text { if } \quad v _ {i} ^ {X} (k) > 0 \\ x _ {i} ^ {X} (k), & \text { otherwise } \end{array} \right.\tag{12}
$$

$$
y _ {i} ^ {X} (k + 1) = \left\{ \begin{array}{l l} y _ {i} ^ {X} (k) + r _ {i y} ^ {X} (k), & \text { if } \quad v _ {i} ^ {X} (k) > 0 \\ y _ {i} ^ {X} (k), & \text { otherwise } \end{array} \right.\tag{13}
$$

$$
z _ {i} ^ {X} (k + 1) = \left\{ \begin{array}{l l} z _ {i} ^ {X} (k) + r _ {i z} ^ {X} (k), & \text { if } \quad v _ {i} ^ {X} (k) > 0 \\ z _ {i} ^ {X} (k), & \text { otherwise } \end{array} \right.\tag{14}
$$

$$
t _ {i} ^ {X} (k + 1) = t _ {i} ^ {X} (k), \quad g t _ {i} ^ {X} (k + 1) = g t _ {i} ^ {X} (k).\tag{15}
$$

## 2.3.2. The number of weapons of each platform

$$
f _ {i} ^ {X} (k + 1) = \left\{ \begin{array}{l} f _ {i} ^ {X} (k) - c _ {i} ^ {X} (k), \quad \text { if } \quad v _ {i} ^ {X} (k) > 0 \text { and } X \neq W \\ f _ {i} ^ {X} (k), \quad \text { if } v _ {i} ^ {X} (k) \leq 0 \text { and } X \neq W \end{array} \right.\tag{16}
$$

$$
g f _ {i} ^ {X} (k + 1) = \left\{ \begin{array}{l} g f _ {i} ^ {X} (k) - c _ {i} ^ {X} (k), \quad \text { if } \quad v _ {i} ^ {X} (k)   >   0 \text { and } X = W \\ g f _ {i} ^ {X} (k), \quad \text { if } v _ {i} ^ {X} (k)   \leq   0 \text { and } X = W. \end{array} \right.
$$

## 2.3.3. The remaining value of platforms

If a platform is already destroyed, the value of this platform will always be zero. If an undestroyed platform is killed by the actions launched at time $k ,$ its value at time $k + 1$ will also be set to zero, no matter how many weapons remain. Otherwise, the value will be adjusted according to the salvo size launched by it. The mechanism is described as follows

$$
v _ {i} ^ {X} (k + 1) = \left\{ \begin{array}{l l} 0, & \text { if } \quad v _ {i} ^ {X} (k) \leq 0 \\ 0, & \text { if } \quad v _ {i} ^ {X} (k) > 0 \text { and } R _ {i} ^ {X} (k) \leq P _ {i} ^ {X} (k) \\ v _ {i} ^ {X} (k) - c _ {i} ^ {X} (k) t _ {i} ^ {X} (k), & \text { if } \quad v _ {i} ^ {X} (k) > 0 \text { and } R _ {i} ^ {X} (k) > P _ {i} ^ {X} (k) \text { and } X \neq W \\ v _ {i} ^ {X} (k) - c _ {i} ^ {X} (k) g t _ {i} ^ {X} (k), & \text { if } \quad v _ {i} ^ {X} (k) > 0 \text { and } R _ {i} ^ {X} (k) > P _ {i} ^ {X} (k) \text { and } X = W \end{array} \right.\tag{17}
$$

where

$R _ { i } ^ { X } ( k ) \colon \mathrm { A }$ uniform random variable that satisfies the probability requirement $P ( R _ { i } ^ { X } ( k ) \leq P _ { i } ^ { X } ( k ) ) = P _ { i } ^ { X } ( k )$

$P _ { i } ^ { X } ( k ) \colon$ The probability that the ith platform of force X is killed by actions launched at time k. It can be calculated via Eq. (18). Note that a White platform might experience losses from all weapons launched.

$$
P _ {i} ^ {X} (k) = \left\{ \begin{array}{l l} 1 - \prod_ {j = 1} ^ {N ^ {- X} (k)} (1 - P K _ {i j} ^ {X, - X} (k) \delta (i, d _ {j} ^ {- X} (k))) ^ {c _ {j} ^ {- X} (k)}, & \text { if } X \in \{B, R \} \\ 1 - \Big (\prod_ {j _ {1} = 1} ^ {N ^ {B} (k)} (1 - P K _ {i j _ {1}} ^ {X, B} (k)) ^ {c _ {j _ {1}} ^ {B} (k)} \Big) \times \\ \Big (\prod_ {j _ {2} = 1} ^ {N ^ {R} (k)} (1 - P K _ {i j _ {2}} ^ {X, R} (k)) ^ {c _ {j _ {2}} ^ {R} (k)} \Big), & \text { if } X \in W \end{array} \right.\tag{18}
$$

−X: The force type that might launch weapons (not including civilian's actions) to X. It is calculated as

$$
- X = \left\{ \begin{array}{l l} B, & \text { if } \quad X = R \\ R, & \text { if } \quad X = B \\ B & \text { or } \quad R, \quad \text { if } \quad X = W \end{array} \right.\tag{19}
$$

$N ^ { - X } { \mathrm { : } }$ The number of platforms of type −X. It is calculated as

$$
N ^ {- X} (k) = \left\{ \begin{array}{l l} N ^ {B} (k), & \text { if } \quad X = R \\ N ^ {R} (k), & \text { if } \quad X = B \\ N ^ {B} (k) + N ^ {R} (k), & \text { if } \quad X = W \end{array} \right.\tag{20}
$$

$\delta ( o , q ) \colon$ : Keonecker delta function defined as

$$
\delta (o, q) = \left\{ \begin{array}{l l} 1, & \text { if } \quad o = q \\ 0, & \text { otherwise } \end{array} \right.\tag{21}
$$

$P K _ { i j } ^ { X , - X } ( k ) ;$ : The probability that the ith platform of force X is killed by one weapon launched by the jth platform of force $- X$ at time k.

When $X \in \{ B , R \}$ , let

$$
\operatorname{Expon} _ {i j} ^ {X, - X} (k) = \sum_ {m = 1} ^ {N ^ {W} (k)} \left(c _ {m} ^ {W} (k) + B i a s ^ {X, - X}\right) \delta (s (- X) j, d _ {m} ^ {W} (k))\tag{22}
$$

then $P K _ { i j } ^ { X , - X } ( k )$ can be calculated as

$$
P K _ {i j} ^ {X, - X} (k) = \left\{ \begin{array}{l} P K O _ {i j} ^ {X, - X} + (1 - P K O _ {i j} ^ {X, - X}) \times \\ (1 - (B a s e _ {u p} ^ {X, - X}) ^ {- E x p o n _ {i j} ^ {X, - X} (k)}), \text {   if   } \operatorname{Expon} _ {i j} ^ {X, - X} (k) > 0 \\ P K O _ {i j} ^ {X, - X} (\operatorname{Base} _ {\text { down }} ^ {X, - X}) ^ {\operatorname{Expon} _ {i j} ^ {X, - X} (k)}, \text {   if   } \operatorname{Expon} _ {i j} ^ {X, - X} (k) \leq 0 \end{array} \right.\tag{23}
$$

where Bias $X , - X$ reflects the initial social preference extent of civilians for the two sides X and $- X$ due to literature, religion, and other possible reasons. When Bia $\scriptstyle \cdot ^ { X , - X } = \operatorname { B i a s } ^ { - X , X } = 0$ , it means initially the civilians are ideally neutral. In many scenarios, $\mathrm { B i a s } ^ { X , - X } = - \mathrm { B i a s } ^ { - X , X } = 0$ holds. The explanation of $P K O _ { i j } ^ { X , - X }$ is the ideal kill probability when the battle is in an ideally neutral environment, which means no civilian will affect any kill probabilities. $P \dot { K } O _ { i j } ^ { X , - X }$ is a constant in [0, 1] and is defined before the game starts according to different combination of attacker type and the type of target. Note that for a civilian platform and a type $- X ( X \in \{ B , R \} )$ platform there is also a predefined $P K O _ { i j } ^ { X , W }$ . Note that for each civilian platform, there are also predefined $P K O _ { i j } ^ { \dot { X } , W \bullet } \bf { s } ,$ which represent the original kill probabilities after the civilian platform become Red or Blue. For example, if a civilian platform becomes Red, corresponding $P K O _ { i j } ^ { B , W }$ will be used to replace $P K O _ { i j } ^ { X , - X }$ in Eq. (23), where j is the new index for the transformed civilian platform in Red team and i is the index of its possible target in Blue team. If a white civilian platform becomes Blue, the situation is similar. $\mathrm { B a s e } _ { \mathrm { u p } } ^ { X , - X }$ and $\mathrm { B a s e } _ { \mathrm { d o w n } } ^ { X , - X }$ are factors that exponentially calculate the influence of civilians and are usually greater than one. $\mathrm { E x p o n } _ { i j } ^ { X , - X } ( k )$ can be seen as the overall effect of all the actions doing by all White platforms for the jth platform with type −X. If it is positive, it means the killing probability of the weapon launched by jth platform with $\mathrm { t y p e } - X$ should be improved. Otherwise, this killing probability should be reduced.

When $X = W ,$ strictly speaking, the collateral killing probability $P K _ { i j } ^ { X , - X } ( k )$ should also be adjusted based on the original collateral kill probability $\overline { { P K O W _ { i j } ^ { X , - X } } }$ . This is because: when a White platform decides to help one side, it might have both risks and benefits (the benefit–risk tradeoff). For example, if it helps a Blue platform, the probability that the Blue platform being helped creates collateral damage for this White platform will be reduced, while the probability that a Red platform firing on that Blue platform creates collateral damage for this White platform might improve. Considering this, when $X { = } W , P K _ { i j } ^ { X , - X } ( k )$ can be calculated as

$$
P K _ {i j} ^ {X, - X} (k) = \left\{ \begin{array}{l} P K O W _ {i j} ^ {X, - X} + (1 - P K O W _ {i j} ^ {X, - X}) \times \\ (1 - (B a s e _ {u p} ^ {X, - X}) ^ {- W \text { Expon } _ {i j} ^ {X, - X} (k)}), \text {   if   } W \text { Expon } _ {i j} ^ {X, - X} (k) > 0 \\ P K O W _ {i j} ^ {X, - X} (\text { Base } _ {\text { down }} ^ {X, - X}) ^ {W \text { Expon } _ {i j} ^ {X, - X} (k)}, \text {   if   } W \text { Expon } _ {i j} ^ {X, - X} (k) > 0 \end{array} \right.\tag{24}
$$

where

$$
\begin{array}{c} W \text {Expon} _ {i j} ^ {X, - X} (k) = - (c _ {i} ^ {X} (k) + B i a s ^ {X, - X}) (\delta (j s (- X), d _ {i} ^ {X} (k)) \\ - \delta (- s (- X) d _ {i} ^ {X} (k), d _ {j} ^ {- (- X)} (k) (1 - \delta (0, d _ {i} ^ {X} (k))))). \end{array}\tag{25}
$$

Explanations of Eqs. (24) and (25) are similar to the explanations of Eqs. (22) and (23). Note that now −X might be either B or $R ,$ determined by context of Eq. (18). $W { \mathrm { E x p o n } } _ { i j } ^ { X , - X } ( k )$ calculates the comprehensive influence on a White platform resulting from its action. If a White platform is helping a Blue platform that is being attacked by a Red platform, in Eq. (25) the part $- ( c _ { i } ^ { X } ( k ) + B i a s ^ { \bar { X } , - X } ) \delta ( j s ( - X ) , d _ { i } ^ { \bar { X } } ( k ) )$ will stand for the benefits resulting from the helped Blue platform. The other part of $W { \mathrm { E x p o n } } _ { i j } ^ { X , - X } ( k )$ calculates the improvement of risks resulting from the Red platform which is attacking the helped Blue platform.

## 2.3.4. White identity and anger update

$$
g _ {i} ^ {W} (k + 1) = \left\{ \begin{array}{l} g _ {i} ^ {W} (k), \text {   if   } g _ {i} ^ {W} (k) \neq 0 \\ 1, \text {   if   } g _ {i} ^ {W} (k) = 0 \text {   and   } (A ^ {B} - A ^ {R}) \geq m _ {i} ^ {R} A ^ {B, R} \\ - 1, \text {   if   } g _ {i} ^ {W} (k) = 0 \text {   and   } (A ^ {R} - A ^ {B}) \geq m _ {i} ^ {B} A ^ {R, B} \end{array} \right.\tag{26}
$$

where $m _ { i } ^ { X }$ is the threshold factor so that ith white platform will join side X. $\boldsymbol { A } ^ { X , - X }$ is a constant that represents the anger factor $\operatorname { o f } - X$ towards X. Since −X and X are opposing forces in wars when $X \in \{ B , R \}$ , it is reasonable to assume that their angers towards each other are relatively stable and will not emotionally change like civilians do during the war. $A ^ { X }$ reflects White's anger factor towards X. If it is positive, it means White hates X. If it is negative, it implies White shows sympathy for $X . ~ { \cal { A } } ^ { \bar { X } }$ . updates according to following formulas.

$$
\begin{array}{l} A ^ {X} (k) = \left\{ \begin{array}{l} A _ {0} ^ {X}, \text {   if   } k = 0 \\ 0, \text {   if   } \sum_ {h = 1} ^ {N ^ {W} (k - 1)} v _ {h} ^ {W} (k - 1) = 0 \text {   and   } k > 0 \\ A _ {0} ^ {X} + (A ^ {X} (k - 1) - A _ {0} ^ {X}) \lambda^ {X} + A ^ {X, - X} \times \\ (\operatorname{Loss} ^ {X} (k - 1) / \sum_ {h = 1} ^ {N ^ {W} (k - 1)} v _ {h} ^ {W} (k - 1)), \text {   if   } \sum_ {h = 1} ^ {N ^ {W} (k - 1)} v _ {h} ^ {W} (k - 1) \neq 0 \text {   and   } k > 0 \end{array} \right. \\ \operatorname{Loss} ^ {X} (k) = \sum_ {h = 1} ^ {N ^ {W}} v _ {h} ^ {W} (k) \text { step } (P _ {i} ^ {W, B} (k) - R _ {i} ^ {W, B} (k)). \end{array}\tag{27}
$$

28

$A _ { 0 } ^ { X }$ reflects White's initial anger factor towards X due to literature, religion, and other possible reasons. If it is positive, it means White initially hates X. If it is negative, it implies White initially shows sympathy for X. In many scenarios, $\stackrel { \cdot } { A _ { 0 } ^ { X } } = - A _ { 0 } ^ { - X }$ holds. When $\overset { \triangledown } { \boldsymbol { A } _ { 0 } ^ { X } } = - \dot { \boldsymbol { A } } _ { 0 } ^ { - X } = 0$ , it means initially the civilians are ideally neutral. $\lambda ^ { \check { X } } ,$ , which is between zero and one, implies that White's anger towards X will decrease exponentially if no new collateral damage from X $\therefore \mathrm { L o s s } ^ { X } ( k )$ is the collateral damage caused by X. Note that if we use Loss(k) to denote the loss of white due to the actions launched at time $k , \mathrm { L o s s } ^ { B } ( k ) ^ { + }$ $\mathrm { L o s s } ^ { R } ( k ) \overset { \cdot } { \geq } \mathrm { L o s s } ( k )$ holds. This is because there might be cases weapons from both Blue and Red simultaneously kill some White lives/properties. For civilians, it is often not feasible to estimate the weapon from which side has larger collateral killing probability thus blame more to that side. The most direct way is to blame two sides simultaneously. However, the results of similar blaming might be different, reflected by the possible difference between $\mathrm { B a s e } _ { \mathrm { u p } } ^ { X , - X }$ and $\mathrm { B a s e } _ { \mathrm { d o w n } } ^ { X , - X }$

$N ^ { B } ( k ) , N ^ { R } ( k )$ , and $N ^ { W } ( k )$ update as follows.

$$
N ^ {X} (k + 1) = \left\{ \begin{array}{l} N ^ {B} (k) + \Delta N ^ {B} (k), \text {   if   } X = B \\ N ^ {R} (k) + \Delta N ^ {R} (k), \text {   if   } X = R \\ N ^ {W} (k) - \Delta N ^ {B} (k) - \Delta N ^ {R} (k), \text {   if   } X = W \end{array} \right.\tag{28}
$$

where $\Delta N ^ { B } ( k )$ and $\Delta N ^ { R } ( k )$ are the number of civilian platforms which join Blue or Red at timestep k. Note that if a civilian platform joins Blue or Red, the index i and corresponding states (such as $x _ { i } ^ { X } ( k ) , y _ { i } ^ { X } ( k )$ , etc.) will also be adjusted accordingly so that the association is still correct. This can be easily implemented via computer algorithm.

## 2.4. Objective functions

Objective functions are represented with kill probabilities.

$$
\left[ \begin{array}{c} J ^ {B} (k) \\ J ^ {R} (k) \\ J ^ {W} (k) \end{array} \right] = w \times \left[ \begin{array}{c} V ^ {B} (k) \\ V ^ {R} (k) \\ V ^ {W} (k) \end{array} \right] = w \times \left[ \begin{array}{c} V ^ {B} (k) = \sum_ {i = 1} ^ {N ^ {B} (k)} v _ {i} ^ {B} (k) \\ V ^ {R} (k) = \sum_ {i = 1} ^ {N ^ {R} (k)} v _ {i} ^ {R} (k) \\ V ^ {W} (k) = \sum_ {i = 1} ^ {N ^ {W} (k)} v _ {i} ^ {W} (k) \end{array} \right]\tag{29}
$$

where $k { = } 0 , 1 , 2 { \mathrm { , . . . , } } K$ . When $k { = } K , J ^ { X } ( k )$ stands for the comprehensive objective function of the whole battle. w is a $3 \times 3$ coefficient matrix defined in Eq. (30).

$$
w = \left[ \begin{array}{c c c} w _ {1 1} & w _ {1 2} & w _ {1 3} \\ w _ {2 1} & w _ {2 2} & w _ {2 3} \\ w _ {3 1} & w _ {3 2} & w _ {3 3} \end{array} \right].\tag{30}
$$

Different $w \mathbf { \hat { s } }$ describe different battlefield situations. For example, the w stated in Eq. (31)

$$
w = \left[ \begin{array}{c c c} 1 & - 0. 8 & 0. 7 \\ - 1. 5 & 0. 7 5 & 0. 0 0 1 \\ - 0. 0 0 1 & 0. 0 0 1 & 1 \end{array} \right]\tag{31}
$$

might be suitable to describe cases that a high-technology force with less tolerance of casualty fights with a lowtechnology force that holds slight sympathy from civilian.

According to Wei and Cruz [24], in some special conditions players might consider not only their own estimation about the warfare but also the estimation from their enemies. For example, if an achievement obtained by Red is very trivial in Red's original thoughts according to its tradition but it can cause large hurt in Blue's heart due to different historical and religious background, it might still be valuable for Red to execute. Considering this, an even more comprehensive model (normalized) might be as follows

$$
\left[ \begin{array}{c} J ^ {B c} (k) \\ J ^ {R c} (k) \\ J ^ {W c} (k) \end{array} \right] = W ^ {c} (k) \times \left[ \begin{array}{c} J ^ {B} (k) \\ J ^ {R} (k) \\ J ^ {W} (k) \end{array} \right] = \left[ \begin{array}{c c c} W _ {1 1} ^ {c} (k) & W _ {1 2} ^ {c} (k) & W _ {1 3} ^ {c} (k) \\ W _ {2 1} ^ {c} (k) & W _ {2 2} ^ {c} (k) & W _ {2 3} ^ {c} (k) \\ W _ {3 1} ^ {c} (k) & W _ {3 2} ^ {c} (k) & W _ {3 3} ^ {c} (k) \end{array} \right] \times \left[ \begin{array}{c} J ^ {B} (k) \\ J ^ {R} (k) \\ J ^ {W} (k) \end{array} \right]\tag{32}
$$

where the $\ " \mathrm { c } \ : \mathrm { \Omega }$ in superscript stands for “comprehensive”. In such conditions, the angers of civilians will affect $W ^ { c } ( k )$ according to following formulas.

$$
W _ {i j} ^ {c} (k) = \left\{ \begin{array}{l} W _ {i j} ^ {c 0}, \text {   if   } i \leq 2 \text {   or   } j = 3 \text {   or   } k = 0 \\ 0, \text {   if   } i = 3 \text {   and   } j \neq 3 \text {   and   } k > 0 \text {   and   } \sum_ {h = 1} ^ {N ^ {W} (k - 1)} v _ {h} ^ {W} (k - 1)) = 0 \\ W _ {3 1} ^ {c 0} + (W _ {3 1} ^ {c} (k - 1) - W _ {3 1} ^ {c 0}) \mu_ {3 1} + W _ {2 1} ^ {c 0} (\text { Loss } ^ {X} (k - 1) / \sum_ {h = 1} ^ {N ^ {W} (k - 1)} v _ {h} ^ {W} (k - 1)), \text {   if   } i = 3 \text {   and   } j = 1 \text {   and   } k > 0 \text {   and   } \sum_ {h = 1} ^ {N ^ {W} (k - 1)} v _ {h} ^ {W} (k - 1)) \neq 0 \\ W _ {3 2} ^ {c 0} + (W _ {3 2} ^ {c} (k - 1) - W _ {3 2} ^ {c 0}) \mu_ {3 2} + W _ {1 2} ^ {c 0} (\text { Loss } ^ {X} (k - 1) / \sum_ {h = 1} ^ {N ^ {W} (k - 1)} v _ {h} ^ {W} (k - 1)), \text {   if   } i = 3 \text {   and   } j = 2 \text {   and   } k > 0 \text {   and   } \sum_ {h = 1} ^ {N ^ {W} (k - 1)} v _ {h} ^ {W} (k - 1)) \neq 0 \end{array} \right.\tag{33}
$$

where $\mathcal { W } _ { i j } ^ { c 0 }$ is the initial coupling factor [25], $\mu _ { i j }$ is the exponential decay factor. Note that $\begin{array} { r } { \sum _ { h = 1 } ^ { N ^ { W } ( k - 1 ) } \nu _ { h } ^ { W } ( k - 1 ) ) = 0 } \end{array}$ <sup>¼ ð - ÞÞ ¼</sup>implies that all White civilians are collaterally killed. In this case although the dead White civilians still appear in the coupling factor updating equation, they will not be able to perform any actions in the game.

Based on the multiple player game models with civilian player, results from modern optimal control and dynamic game theories can be applied to calculate optimal control $\stackrel { \smile } { u } ^ { X ^ { * } } = u _ { 0 } ^ { X ^ { * } } , ~ u _ { 1 } ^ { X ^ { * } } , ~ u _ { 2 } ^ { X ^ { * } } , . . . , ~ u _ { K - 1 } ^ { X ^ { * } }$ according to the global maximization equilibrium of objective functions, or suboptimal control $\boldsymbol { u } ^ { X ^ { * } } = \boldsymbol { u } _ { 0 } ^ { X ^ { * } } , \boldsymbol { u } _ { 1 } ^ { X ^ { * } } \boldsymbol { u } _ { 2 } ^ { X ^ { * } } , . . . , \boldsymbol { u } _ { K - 1 } ^ { X ^ { * } }$ according to various approaches. For details, see [1,5,7,16,19,20].

Clearly, if we set some parameters in this model as zero, this model will be the same as existing attrition-like state space models. In other words, existing attrition-like state space model are special cases of the model proposed in this paper.

## 3. Experiments

We simulated several scenarios using the multiple player game model with a civilian player discussed in this paper. The focus is the control strategy of White player under different Blue–Red–White settings. We consider two categories of experiments. The first is “Rational scope”. This name implies that in the whole procedure of battle, no civilian platform is agitated to give up civilian identity and join one side. In other words, the emotion of civilians does not overwhelm the rationality and the civilians will always be civilians, which mean they can affect kill probabilities at most. The second is “Emotional–rational scope”, which means at some time the rationality of civilians is overwhelmed by their emotion. In this case, some civilian platform(s) might be so angry that they would give up civilian identity and join one side.

We use the initial w given in Eq. (30). The asymmetry among the elements of w stands for the differences in warfare estimations, literatures/religions, tolerance capabilities about casualties/losses, the attitudes towards avoiding collateral damages, and other possible reasons. To reflect the difference of high technology Blue force and low technology Red force, we set most of the original kill probabilities of Blue weapons to be higher than corresponding Red low technology weapons. Blue platform values and weapon values are also higher since the prices of high technology weapons are typically higher. The initial bias of civilians is set as ${ \bar { \mathrm { B i a s } } } ^ { B , \ { \bar { R } } } { = } { - } { \mathrm { B i a s } } ^ { B , \ R } { = } 0 . 5$ , reflecting the civilian’s initial slight favoring of Red.

For simplicity, we assume that there are two Blue platforms, three Red platforms, and four White platforms. As we can see here, initially the number of white platforms outweighs that of any armies. This reflects some characteristics of battles in districts, especially in modern anti-terrorism wars. From simulations we would observe that sometimes the large number of civilians might have great influences on results of battles (Figs. 8–10, will be explained in detail later), although they are generally weaker in fighting resources (such as weapons, fighting skills, etc.) when compared to (initial) Blue/Red fighters. A White platform has three choices: keep the original bias, help Blue, or help Red more. If at time k the ith White platform chooses “keep the original bias”, it implies that the corresponding $c _ { i } ^ { \dot { W } } ( k )$ and $\bar { d } _ { i } ^ { W } ( k )$ are both set to zero. If at time $k$ all White platforms are killed but there are still both Blue and Red with weapons, the battle will continue and the program will automatically set all later $c _ { i } ^ { W } ( k )$ and $d _ { i } ^ { W } ( k )$ as zero. The outputs of the White platforms will also be set as “keep the original bias”.

## 3.1. Rational scope

For convenience, we call the reduction of collateral kill probability by weapons launched by a Blue or Red platform M resulting from the action that the White platform helps $M ,$ as “reward from type $M ^ { \prime }$ . Similarly, we call the improvement of collateral kill probability by weapons launched by a Blue or Red platform M resulting from the action that the White platform reduces M's weapons' capabilities of killing opposing forces as “punishment from type $M ^ { \mathfrak { s } }$ . Obviously, there are $2 ^ { 4 } = 1 6$ cases of rewards/punishments. When reward from Red, reward from Blue, punishment from Red, punishment from Blue all exist in a battlefield, we have the case we discussed in last section, which is the most complex. A simulated battle process is shown in Fig. 2 (at the end of this paper).

![](/api/attachments/ZQCUKFPB/fulltext/images/8f9069f9a87a93da6fdd10c49a64b0f7d6672d51c79735b6c27f2a2188b78490.jpg)  
Fig. 2. Control strategy of White.

In Fig. 2, $z { = } 0 . 5$ stands for the original bias and the White platforms do not take special actions. $( \mathrm { f } z < 0 . 5 ,$ , it means White takes actions to help Blue. $z { > } 0 . 5$ implies that White takes actions (in addition to the natural bias) to help Red. From Fig. 2 we know that except at $k { = } 2$ White always chooses to keep the original bias. At k = 2, White chooses to help Blue. Fig. 3 (at the end of this paper) shows a plot of White outputs and the ratio between the number of weapons that might be launched by Blue and the counterparts of Red. The upper curve is the ratio curve, while the other is the White output curve.

An interesting but reasonable characteristic is that the White platforms tend to help the force that is more powerful for White under these settings. Here “more powerful force for White” means the force can give more rewards for White's help and more punishments for White's helping the force's enemy. As long as a force does not provide any rewards or punishment for civilians, no matter how powerful it seems, the civilians will not help it.

In real battles, due to different social–political– military factors, Blue or Red might not be able to reward or punish civilians. For example, Red might punish civilian for harm but might not be able to reward them for help, while Blue should reward civilian for help but should not punish civilian for harm. For this scenario, we should modify the kill probabilities in the state equations accordingly and a simulated procedure is plotted in Fig. 4 (at the end of this paper). Another scenario in which there is only reward from Red for help and punishment from Red for harm is shown in Fig. 5 (at the end of this paper). In Fig. 4, at time t = 2, all White are already killed. This is the reason why in later stages

![](/api/attachments/ZQCUKFPB/fulltext/images/2badc7b148f97522aa9f7cb75b67c069d40680fc5326c5c3dc16bd8ad821367e.jpg)  
Fig. 3. The ratio of numbers of weapons that might be launched.

White takes no actions although Blue is relatively more powerful than before.

Comparatively, using the multi-player model with civilian player can help players refine strategies and reduce losses in the long run than traditional two-player attrition-like models, since the new model describes battlefields more precisely. Figs. 6 and 7 are two cases for comparison. Fig. 6 (at the end of this paper) records a typical scenario in which Blue considers the possible weapon influences from a White player. Fig. 7 (at the end of this paper) is for a corresponding case in which the only difference is that Blue ignores such influences (that is to say, Blue uses traditional 2-player game to model the battle and ignore the influences from White civilian, although such influences do exist in the battle). All other parameters are the same for two situations. We can see that in Fig. 6 White lives longer and Blue wins the battle. This is because the careful modeling about White improves Blue's strategy. For White and Blue, this is a win–win result. On the contrary, since Blue fails to apply the new model thus ignores civilians possible retaliations, in Fig. 7 White lives shorter and Blue loses. Of course, for White and Blue, this is a lose– lose result.

![](/api/attachments/ZQCUKFPB/fulltext/images/888710ab9678878cdfeb4581a52fc96003206e9719a5eea09db16cfed7254505.jpg)  
Fig. 4. Only Red punishment and Blue reward.

![](/api/attachments/ZQCUKFPB/fulltext/images/fb0ad02c8194da0ca436b73ac478e55d8a9546b95d78846d6d35c04c4c7a6f7c.jpg)  
Fig. 5. Only Red reward and Red punishment.

## 3.2. Emotional–rational scope

When emotion overwhelms rationality, some white civilians might give up civilian identity and directly join one of the fighting forces. When they join one army, they will be treated as enemy by the other army. This is because when a civilian platform suddenly fires at you, say, with a small weapon such as handgun, it is a natural response to treat it as an enemy and fire back (if possible), no matter how weak its weapon is and how bad its fighting skill is. Note that when compared to well trained and organized Blue/Red fighters, civilians who joined one side in the middle of a battle are generally weaker in fighting powers. Although logically we have to treat the civilians who joined one army as new fighters of that army, their weapon number, value, salvo size limits, and kill probabilities are much smaller than those of initial Blue/Red fighters. This is because differences in weapons, training, organization and coordination, and other related factors. As a result, only if the number of changing-identity civilians is big enough, they can dramatically affect the result of the battle.

![](/api/attachments/ZQCUKFPB/fulltext/images/165a80cb5bcc61fed9d9750dfe69f9f56ff5d268d576693e28212c2176f21904.jpg)  
Fig. 6. Blue considers White as a player.

![](/api/attachments/ZQCUKFPB/fulltext/images/65392b07ec71b813d6a0d89142d6b7f6a65be09b64a2f137691e1bda50eec782.jpg)  
Fig. 7. Blue does not consider white as a player.

Fig. 8 (at the end of this paper) and Fig. 9 (at the end of this paper) are two typical scenarios for this situation.

![](/api/attachments/ZQCUKFPB/fulltext/images/8f90665fe664c0e4d94845653b6c9969d53150b36e9049871700356f348c6dcb.jpg)  
Fig. 8. Some civilians become Blue.

![](/api/attachments/ZQCUKFPB/fulltext/images/1cb9e1cfa91afc65504fac7ce1fb052294a6dc9a684f72deba104bd374f5d553.jpg)  
Fig. 9. Some civilians become Red.

In Fig. 8, since the civilians hate Red much more than hate Blue, some of them become Blue at time point 3. Similarly, in Fig. 9 the great anger toward Blue lead some civilians to join Red. Fig. 10 (at the end of this paper) is a typical plot of civilian anger updating (corresponding to Fig. 9). Note that in the plots of anger, if no civilian survives, anger of civilian will be set to zero. Although only part of civilians become Blue, since the rest of civilians are collaterally killed at time step 3, the angers toward Blue or Red are all zero after timestep 3.

Comparing Figs. 8 and 9, we can see that White civilians can greatly affect the final result of the battle. In Fig. 8, since civilians join Blue, Blue wins. On the contrary, when civilians join in Fig. 9, Red wins.

![](/api/attachments/ZQCUKFPB/fulltext/images/88fcbc3ac5895e0826f9d533253d807afe8a8a02d184779bf3f1f8ec36ae1162.jpg)  
Fig. 10. Anger update.

## 4. Conclusions

In this paper, we explained the importance and benefit of adding a partially-emotional–partially-rational civilian player to existing attrition-type models and developed the corresponding extended multiple player model. We defined and discussed components of the model, including state variables, control variables, control constraints, state equations, objective functions, emotion quantization, and control strategies. This paper focused on the adjustments of kill probabilities in state equations and the influences from civilian emotion, which can greatly affect the battle process and might even cause civilians to join Blue or Red. Existing attrition-type models can be seen as special cases of the extended model, and the extended model can describe real world situations more accurately if reasonable parameters are used. We performed extensive simulations to verify and illustrate the benefits and possible applications of this extended model. The hypothesis that a neutral player tends to help a player who can give more rewards is confirmed via computer simulations based on this model.

## Acknowledgements

This research was supported by the US Navy under contract number N00014-05-M-0205. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies or endorsements, either expressed or implied, of the Navy.

## References

[1] M. Athans, O.L. Falb, Optimal Control, Mcgraw Hill, New York, 1966.

[2] J.A. Battilega, J.K. Grange (Eds.), The Military Applications of Modeling, Air Force Institute of Technology Press, Washington, DC, 1984.

[3] H. Brackney, The dynamics of military combat, Operations Research 7 (1959) 30–49.

[4] H. Brooks, T. DeKeyser, D. Jaskot, D. Sibert, R. Sledd, W. Stilwell, W. Scherer, Using agent-based simulation to reduce collateral damage during military operations, Proceedings of the 2004 IEEE Systems and Information Engineering Design Symposium, 2004, pp. 71–77.

[5] J.B. Cruz Jr., G. Chen, D. Garagic, X. Tan, D. Li, D. Shen, M. Wei, X. Wang, Team dynamics and tactics for mission planning, Proceedings, IEEE Conference on Decision and Control, December 2003, pp. 3579–3584.

[6] J.B. Cruz Jr., M.A. Simaan, Multi-agent control strategies with incentives, Proceedings of the First DARPA/JFACC Symposium on Advances in Enterprise Control, San Diego, CA, Nov. 15–18, 1999, pp. 177–182.

[7] J.B. Cruz Jr., M.A. Simaan, A. Gacic, H. Jiang, B. Letellier, M. Li, Y. Liu, Game-theoretic modeling and control of a military air

operation, IEEE Transactions on Aerospace and Electronic Systems 37 (4) (October 2001).

[8] T.N. Dupuy, Attrition: Forecasting Battle Casualties and Equipment Losses in Modern War, Hero Books, Fairfax, VA, 1990.

[9] K.R. Foster, I.A. Lerch, Collateral damage: American science and the war on terrorism, IEEE Technology and Society Magazine 24 (3) (2005) 43–53.

[10] J. Gratch, S. Marsella, A domain-independent framework for modeling emotion, Journal of Cognitive Research 5 (4) (2004) 269–306.

[11] R.L. Helmbold, A modification of Lanchester's equations, Operations Research 13 (1965) 857–859.

[12] W.P. Hughes Jr. (Ed.), Military Modeling, The Military Operations Research Society, 1984.

[13] A. Kott, L. Ground, J. Langston, Estimation of battlefield attrition in a course of action analysis decision support system, Presented at The Military Operations Research Society Workshop on Land and Expeditionary Warfare, June 1999.

[14] F.A. Lanchester, Aircraft in Warfare: The Dawn of the Fourth Arm, Constable, London, 1916, pp. 39–46.

[15] M. Minsky, The Society of Mind, Simon and Schuster, New York, 1986.

[16] J.F. Nash Jr., Equilibrium points in n-person games, Proceedings of the U.S. National Academy of Sciences, vol. 36, 1950, pp. 48–59.

[17] J.S. Przemieniecki, Mathematical methods in defense analysis, Education Series, 3rd, AIAA, New York, 2000.

[18] M. Senglaub, D. Harris, A Modified Perspective of Decision Support in C2, SAND2005-1701C, February 2002.

[19] M. Simaan, J.B. Cruz Jr., On the Stackelberg strategy in nonzero sum games, Journal of Optimization Theory and Applications 11 (5) (1973) 533–555.

[20] A.W. Starr, Y.C. Ho, Nonzero-sum differential games, Journal of Optimization Theory and Applications 3 (3) (1969) 184–206.

[21] J.G. Taylor, Force-on-Force Attrition Modeling, The Military Operations Research Society, 1980.

[22] J.G. Taylor, Lanchester Models of Warfare, Operation Research Society of America, Arlington, VA, 1983.

[23] B. Toedtmann, S. Riebach, E.P. Rathgeb, The Honeynet quarantine: reducing collateral damage caused by early intrusion response, systems, man and cybernetics (SMC) information assurance workshop, Proceedings from the Sixth Annual IEEE, 2005, pp. 464–465.

[24] M. Wei, J.B. Cruz, Jr., Concepts for a Non-cooperative Coupling Game, International Journal of Control, submitted for publication.

[25] M. Wei, G. Chen, J.B. Cruz Jr., C. Kwan, M. Kruger, Gametheoretic control of military air operations with civilian players, AIAA, Guidance, Navigation, and Control Conference and Exhibit, 2006.

![](/api/attachments/ZQCUKFPB/fulltext/images/f740881192d280174d2123fb484900bd6283b4a02dcfd60a8e4fda5a04d449f1.jpg)

Mo Wei has a BS degree in EE from Northern JiaoTong University and a master's degree in EE from Tsinghua University. He received Ph. D degree from Department of Electrical and Computer Engineering, Ohio State University in Autumn of 2006. His research interests include game control and corresponding applications, such as non-ideal games, coupling game theory, sharing creditability game theory and bottom-line game theory, multi-

player games with civilian players, decentralized multiplayer pursuer– evader games, game application in networking, etc.

![](/api/attachments/ZQCUKFPB/fulltext/images/5c462eac3ff5114cdd4af5acc59387c4f20a50a843f66f3ad50aab2868b2f132.jpg)

Genshe Chen received his B.S. and M.S. in electrical engineering, Ph. D in aerospace engineering, in 1989, 1991 and 1994 respectively, all from Northwestern Polytechnical University, Xian, P.R. China.

He did postdoctoral work at the Beijing University of Aeronautics and Astronau tics and Wright State University from 1994 to 1997. He worked at the Institute of Flight Guidance and Control of the Technical University of Braunshweig

(Germany) as an Alexander von Humboldt research fellow and at the Flight Division of National Aerospace Laboratory of Japan as a STA fellow from 1997 to 2001. He was a Postdoctoral Research Associate in the Department of Electrical and Computer Engineering of The Ohio State University from 2002 to 2004. Since February 2004, Dr. Chen has been with the Intelligent Automation, Inc., Rockville, MD. He has served as the Principal Investigator/ Technical lead for more than 15 different projects, including maneuvering target detection and tracking, cooperative control for teamed unmanned aerial vehicles, a stochastic differential pursuitevasion game with multiple players, multi-missile interception, asymmetric threat detection and prediction, space and cyber situation awareness, etc. He is currently the program manager in Networks, Systems and Control, leading research and development efforts in target tracking, information fusion and cooperative control. His research interests include target tracking and information fusion, guidance and control of aerospace vehicle, GPS/INS/image integrated navigation systems, cooperative control and optimization for military operations, computational intelligence and data mining, hybrid system theory and Markov chain, signal processing and computer vision, cooperative and non cooperative game theory, Bayesian networks, Influence Diagram, and GIS.

![](/api/attachments/ZQCUKFPB/fulltext/images/40cd09d469ad5b9c6d56c7c902f8bd9d7603da1aa009769bcc4ea6465e31665c.jpg)

Jose B. Cruz, Jr. received his B.S. degree in electrical engineering (summa cum laude) from the University of the Philippines (UP) in 1953, the S.M. degree in electrical engineering from the Massachusetts Institute of Technology (MIT), Cambridge in 1956, and the Ph.D. degree in electrical engineering from the University of Illinois, Urbana-Champaign, in 1959. He is currently a Distinguished Professor of Engineering and Professor of Electrical and Computer

Engineering at The Ohio State University (OSU), Columbus. Previously, he served as Dean of the College of Engineering at OSU from 1992 to 1997, Professor of electrical and computer engineering at the University of California, Irvine (UCI), from 1986 to 1992, and at the University of Illinois from 1965 to 1986. He was a Visiting Professor at MIT and Harvard University, Cambridge, in 1973 and Visiting Associate Professor at the University of California, Berkeley, from 1964 to 1965. He served as Instructor at UP in 1953–1954, and Research Assistant at MIT from 1954 to 1956. He is the author or coauthor of six books, 21 chapters in research books, and numerous articles in research journals and refereed conference proceedings.

Dr. Cruz was elected as a member of the National Academy of Engineering (NAE) in 1980. In 2003, he was elected a Corresponding Member of the National Academy of Science and Technology (Philippines). He is also a Fellow of the American Association for the Advancement of Science (AAAS), elected 1989, a Fellow of the American Society for Engineering Education (ASEE), elected in 2004, and a Fellow of International Federation of Automatic Control (IFAC), appointed 2007. He received the Curtis W. McGraw Research Award of ASEE in 1972 and the Halliburton Engineering Education Leadership Award in 1981. He is a Distinguished Member of the IEEE Control Systems Society and received the IEEE Centennial Medal in 1984, the IEEE Richard M. Emberson Award in 1989, the ASEE Centennial Medal in 1993, and the Richard E. Bellman Control Heritage Award, American Automatic Control Council (AACC), 1994. In addition to membership in NAE, ASEE, and AAAS, he is a Member of the Philippine American Academy for Science and Engineering (Founding member, 1980, President 1982, and Chairman of the Board, 1998–2000), Philippine Engineers and Scientists Organization (PESO), National Society of Professional Engineers, Sigma Xi, Phi Kappa Phi, and Eta Kappa Nu. He served as a Member of the Board of Examiners for Professional Engineers for the State of Illinois, from 1984 to 1986. He served on various professional society boards and editorial boards, and he served as an officer of professional societies, including IEEE, where he was President of the Control Systems Society in 1979, Editor of the IEEE TRANSACTIONS ON AUTOMATIC CONTROL, a Member of the Board of Directors from 1980 to 1985, Vice President for Technical Activities in 1982 and 1983, and Vice President for Publication Activities in 1984 and 1985. Currently, he serves as Chair (2004– 2005) of the Engineering Section of the American Association for the Advancement of Science (AAAS).

![](/api/attachments/ZQCUKFPB/fulltext/images/b9a5c1fb8528a7038d37d91341318d7f0f718377ec9d0fd1a51abb7211ebcc55.jpg)

Leonard S. Haynes received his B.S. in Electrical Engineering from University of Maryland with high honors in 1967, the M. S. degree in electrical engineering from University of Pennsylvania in 1969, and the Ph.D. degree in Electrical Engineering/Computer Science from the University of Maryland in 1974.

Dr. Haynes is Founder and President of Intelligent Automation, Incorporated. He has 40 years experience in Electrical

Engineering and Computer Science. He has advanced to leadership roles throughout his career, but has insisted on performing a significant amount of direct hands on engineering and test work. His most important accomplishments are the many new areas of work first conceived of and organized by Dr. Haynes. This work has led to many new developments in a wide range of areas including hexapod-based machine tools, 3D ballistics analysis, software agent-based optimization and simulation, network intrusion detection, etc. Since founding IAI over 20 years ago, Dr. Haynes has personally generated over 150 winning proposals covering a range of innovative new technologies, some of which have developed into significant areas of research. Prior to founding IAI, Dr. Haynes was the Leader of the Real-time Control Systems Group at the National Institute of Standards and Technology (NIST). Before joining NIST, he was the Program Manager of the FAA's Automated En-Route Air Traffic Control System Program — the FAA's attempt to automate en-route air traffic control. He is the author of over 75 refereed papers including 17 published in international journals. He is the holder of 9 patents with several more pending, and is the recipient of numerous awards and commendations.

Martin Kruger is currently serving as the Intelligence, Surveillance and Reconnaissance Thrust Area Manager for the Expeditionary Warfare Maneuver Warfare & Combating Terrorism Science and Technology Department at the Office of Naval Research. In that capacity, he is responsible for maturing and transitioning applicable technology. Research interests include sensing, data fusion & visualization, resource management and information dissemination. The overall objective of the program is to increase the efficiency and effectiveness of the translation of intelligence requirements to actionable intelligence relevant to the Global War on Terror.

Before coming to ONR, Mr. Kruger served as a research and development manager for the Future Theater Air and Missile Defense program office at the Naval Sea Systems Command. He has also worked for the Marine Corps Warfighting Laboratory and for the Naval Surface Warfare Center Indian Head Division. Mr Kruger started his career as a Naval Officer, serving as an instructor at the Naval Nuclear Propulsion School.

After leaving active duty, CAPT Martin Kruger has continued serving the Navy as a drilling reservist. Reserve assignments have included four command tours, one each at a shipyard, a SUPSHIP, a NAVSEA field activity and a Weapon Station. He is currently serving as a Chief Ordnance Inspector.

Martin Kruger holds a bachelor in engineering in Chemical Engineering, a Masters of Science in Industrial Chemistry and a Masters in Business Administration. He is also a graduate of the Naval War College and is Level 3 Certified in Program Management.

![](/api/attachments/ZQCUKFPB/fulltext/images/b296c4f3bad9e2d740b9ce6114f70333541594cbd5b080db3745c1234813bcdd.jpg)

Erik Blasch received his B.S. in mechanical engineering from MIT and Masters in mechanical and industrial engineering from Georgia Tech and MBA, MSEE, from Wright State University and a PhD from WSU in EE. Dr. Blasch also attended Univ of Wisconsin for an MD/PHD in Mech. Eng until being called to Active Duty in the United States Air Force. Currently, he is a Fusion Evaluation Tech Lead for the Air Force Research Laboratory, Adjunct Profes-

sor at WSU, and a reserve Maj with the Air Force Office of Scientific Research.

Dr. Blasch was a founding member of the International Society of Information Fusion (ISIF) and the 2007 ISIF President. Dr, Blasch has many military and civilian career awards; but engineering highlights include team member of the winning ‘91 American Tour del Sol solar car competition, ’94 AIAA mobile robotics contest, and the '92 AUVs competition where they were first in the world to automatically control a helicopter. Since that time, Dr. Blasch has foused on Automatic Target Recognition, Targeting Tracking, and Information Fusion research compiling 160+ scientific papers and book chapters. He is active in IEEE and SPIE including regional activities, conference boards, journal reviews and scholarship committees.
