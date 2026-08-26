---
otero_id: 620
otero_key: "NGB5ZNDB"
title: "Caveat mercator in electronic commerce: An update"
authors: "Daniel G. Conway; Gary J. Koehler"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.06.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Caveat mercator in electronic commerce: An update

Daniel G. Conway <sup>a,</sup>⁎, Gary J. Koehler <sup>b</sup>

<sup>a</sup> Operations and Decision Technologies, 570 Kelley School of Business, Indiana University, Boomington, IN 47405, United States

<sup>b</sup> Information Systems and Operations Management, 351 BUS, The Warrington College of Business Administration, University of Florida, Gainesville, FL 32611, United States

## a r t i c l e i n f o

Article history: Received 24 October 2007 Received in revised form 4 June 2008 Accepted 19 June 2008 Available online 6 July 2008

Keywords: Interface Agent Seller beware eCommerce

## a b s t r a c t

Conway and Koehler presented a new type of software agent that converted merchant interfaces into middleware that enabled a user to bring to bear powerful decision support tools in eCommerce transactions. They called them Interface Agents. These agents operated directly through the human interface and were largely indistinguishable from a human user. They illustrated their ideas with an agent that could play optimal Blackjack at the then emerging online casinos. They discussed possible merchant countermeasures. In this paper we look back at this setting and see what evolved and how such agents have fared. We reassess their proposed countermeasures and update them based on the ever evolving cat-and-mouse game between such agents and merchants.

© 2008 Elsevier B.V. All rights reserved.

## 1. Background

Based on research started in 1997, Conway and Koehler [9] (CK forthwith) presented a new type of software agent that converted merchant interfaces into middleware that enabled a user to bring to bear powerful decision support tools in eCommerce transactions. They called them Interface Agents (see Fig.1). These agents operated directly through the human interface and were largely indistinguishable from a human user.

At the time, considerable academic research attention was directed at consumer issues in online commerce like privacy, trust, vendor viability, product quality, etc. “As a result, CK raised a related but seldom considered concern in eCommerce. They stated “Consumers can do things in an on-line environment that are simply not possible otherwise. In an online environment, consumers have computing resources not normally available in face-to-face transactions.” They termed this situation “Caveat mercator” — seller beware. Their proposed Interface Agent made this clear.

As a pre-cursor to their proposed agent, CK noted that an early software agent, BargainFinder, led to merchants blocking its usage.

These tools enable an agent to discover hard-to-see opportunities — or opportunities never exploited when the tools could not be used or not used effectively. These may not be anticipated by merchants nor easily thwarted.” Conway and Koehler [9]

In fact, soon after BargainFinder was blocked, Jango (http://www.jango.com/) side-stepped the merchant blocking ability. Intelligent software agents continue to evolve [15,25]. Since the CK study, online merchants have had to contend with ever more creative technologies and users. Often such users' goals are fraud related rather than just smart usage of computers in business decisions and transactions. For example, Goldsmith and Wu [12] noted recently that eBay had earlier relied on self-policing with a feedback forum to control fraud but by 2005 had a staff of 800 full-time security professionals.

The architecture of a typical Interface Agent is shown in Fig. 2 and builds on previous agent architectures [6]. Brie<sup>fl</sup>y, sensors observe the human interface — consisting of icons, buttons, lists, images, etc. — to capture the state of an application. For example, screen scraping and optical character recognition methods capture graphical text; window messaging techniques capture text from lists and structural information such as titles; and pattern recognition methods help decipher images or fanciful text displays. Actuators would perform actions like button clicking, keyboard input to text-<sup>fi</sup>elds, mouse movements, and the like. These are indistinguishable from human actions but are issued using programmatic methods controlled by the Interface Agent. The assessment component decided on how to navigate the interface, <sup>fi</sup>ll-in information or call up a decision support system (DSS) component to make decisions. It also monitored responses to check for consistency, merchant “cheating” or mistakes.

![](/api/attachments/NGB5ZNDB/fulltext/images/bdd8aa616a973f5cfb6793552dcf89631a901b46cd60cc6239b337c018064fa0.jpg)  
Fig. 1. Interface Agent

Li and Sun [24] extend the idea of an Interface Agent “to provide a causal connection between the application interfaces and the knowledge model of the Interface Agent.” They term these Re<sup>fl</sup>ective Intelligent Interface Agents. Others have offered related ideas. For example Vahidov and Kersten [29] promote an architecture, called decision stations, that merge an active DSS with agent technology. Vahidov and Fazlollahi [28] look at yet another approach.

CK illustrated their ideas with an agent that could play optimal Blackjack at one of the then emerging online casinos. Brie<sup>fl</sup>y, some casino games can be beaten by an astute player employing optimal (or at least near-optimal) game play. Under the then prevailing rules, Blackjack is one such game.

“Playing blackjack optimally is not easy for a human being. One must track the state of the remaining cards and vary their playing and betting strategy. Optimal play depends only on the state of the deck, the dealer's exposed card, one's hand and the rules of play. Optimal bets depend on the current state of a blackjack deck, the rules of play and the current bank size of the bettor. The sheer number of states possible prohibits one from knowing optimal betting in a traditional casino setting where such information must be memorized. Optimal play beyond that for a full deck is virtually impossible to know with certainty. Both optimal betting and optimal play are approximated by professional blackjack players in real casinos ….” Conway and Koehler [9]“However, in on-line casino gambling, one can employ computer-assisted play and betting with impunity and play optimally.” Conway and Koehler [9]

Using an Interface Agent having a DSS that could determine optimal play given the current Blackjack game state, they tested their agent to play at Island Casino (an online casino that has since seen been absorbed by a competitor) which used a browser-based java applet to deliver the game interface.

CK reported the results of roughly 85 hours of play (28,910 hands) by their Interface Agent. Each hand of play

“… includes interpreting the screen (determining the original cards dealt, the new cards dealt during the hand's play, the outcome, any status messages, etc.) deciding how much to bet, deciding how to optimally play the hand (both with the original hand and any subsequent decisions as the hand was played-out), all the back and forth communication to the casino, etc.” Conway and Koehler [9]

The net result was pro<sup>fi</sup>table as predicted. Furthermore, the monitoring component detected no signi<sup>fi</sup>cant deviations from expected outcomes. That is, it appeared the casino was offering a fair game.

In the long run, no merchant (the casino in their study) could survive if a signi<sup>fi</sup>cant portion of its consumer base used an Interface Agent to attain unanticipated transactional advantages. CK documented changes made by Island Casino to thwart professional play during the course of their research (about a 9 month period). They also discussed possible merchant countermeasures.

In Section 2 we review the merchant countermeasures recommended by CK and look back over the almost 10 years since their research to see what happened to provide a backdrop to suggest a new slate of possible merchant countermeasures in Section 3. In the intervening years several Interface Agents emerged. Two were proprietary and not available for general use. One, LS, played at a large number of different online casinos and games. A second one, called PRO, played in online games of skill. These systems and WinHoldEm (http://www.winholdem.net/) developed by Ray E. Bornert II to play Texas Hold'Em, are documented in the Appendix. The experiences with these are used as anecdotal information in the remainder of the paper. Although these agents were used in online casino games and in online games of skill, they are not the only enterprises vulnerable to Interface Agent use. In Section 4 we discuss other examples and general characteristics of vulnerable businesses. Finally in Section 5 we provide a summary and several conclusions.

![](/api/attachments/NGB5ZNDB/fulltext/images/d35f77701b31a4c0efb0c0a4e64243ba021aedb11585310697b3cc2dae72638e.jpg)  
Fig. 2. Interface Agent architecture.

Table 1  
Original proposals and assessments by CK with a brief summary of observed countermeasures since then

<table><tr><td>Original proposal by CK</td><td>Original assessment by CK</td><td>Some observed countermeasures</td></tr><tr><td>A merchant could dynamically change the user interface itself so the Interface Agent would have to be continuously updated.</td><td>However, if done frequently, this would likely frustrate conventional users and is thus considered poor design. It also imposes a continuous redesign effort by the merchant. The secret then is to create a stable user interface that disrupts the agent.</td><td rowspan="2">1. Positions were varied in a display.2. Fonts were varied often.3. Dynamic layouts and backgrounds were used.4. Some browser-based offerings looked unique for each user.5. Window names were made dynamic or indistinguishable.</td></tr><tr><td>CK suggested such changes via changes in “screen placement, color, and other design features” of the window components.</td><td>CK did not say how to create a stable user interface that disrupts the agent.</td></tr><tr><td>If a user interface incorporates complex graphics, a human user could more readily absorb the inherent information than could a completely automated agent performing image recognition and parsing of graphical objects.</td><td>This poses a temporary stumbling block, at best. Although a completely automated agent might find this challenging, an Interface Agent could be trained to match portions of images with a set of important cases. These cases can be prepared by a human agent who performs the recognition of important portions of the image.</td><td>1. Obscuring images were moved in and out of key areas.2. Images were rotated and telescoped.3. Rare outcomes used different graphics and required unique interaction.4. Captchas were added to many applications.5. Vendors introduced semi-transparent menus with dynamic backgrounds.</td></tr><tr><td>The matching abilities of image recognition software may allow for simple disruptions.</td><td>... these maneuvers can be overcome by a slightly more sophisticated filtering and recognition component in the agent.</td><td>1. Dynamic (changing) cards were introduced.2. Text was displayed as graphical images.</td></tr><tr><td>If timing is involved, there may be mechanisms available to the merchant to change the speed or order of an interface so as to disrupt the timing of the agent.</td><td>... the timing would have to be subtle so as not to disrupt the user. ... Of course, a human user might miss it too.”</td><td>1. Fast moving text provided critical information.2. Rollover menu selections were introduced that relied on how a mouse was moved, not just on clicks at a location.3. Once a hand was finished, cards were immediately removed making capture difficult.</td></tr><tr><td>Merchants should track the behavior of the customers.</td><td>Of course, an agent can simply program such delay mechanisms or other simulated human behavior to defeat such triggers.</td><td>1. MAC addresses, IP&#x27;s and other means of identifying a particular machine were employed.2. Quality of play was tracked and used for expulsion.3. Unusual play was quickly noted.</td></tr><tr><td>Change the rules.</td><td>[Speaking of casino games] the casino was simply forced to change the rules of the game ... making the game significantly less attractive to both professional and casual players.</td><td>1. Online versions of this game quickly evolved to negative expected value rules.2. Others implemented countermeasures like dynamic game rules.3. Opportunities became less and less attractive.</td></tr></table>

## 2. Conway and Koehler proposals and merchant countermeasures

Interface Agents can be detrimental for eCommerce merchants, it is of considerable interest to understand what merchants can do to thwart their activity. CK suggested a number of countermeasures and their likely success. Table 1 summarizes the original CK recommendations, their assessment of the value of each and then gives a brief summary of some of the changes noted in the intervening years. The latter points are based on observations over almost 10 years since the CK study, wherein many changes were detected in the various domains. Some were brilliant, direct countermeasures and some were likely the result of fortuitous programming (possibly errors). These observations are discussed in more detail below.

Some supplemental details are useful for reading Table 1. Regarding point (2), many sites have added captchas (an acronym for “Completely Automated Public Turing test to tell Computers and Humans Apart”) [30]. For example, to get a free Yahoo email account a user must type in what is displayed such as (from [30])

## pUY

Although this is hard for a software agent to decipher, it is relatively easy for a human. Nonetheless, even captchas have been deciphered by software agents sometimes even doing better than humans (see [7] for example). Alternatively, armies of low-paid humans can be used to defeat captchas (see Petmail Design — http://petmail.lothar.com/design.html).

![](/api/attachments/NGB5ZNDB/fulltext/images/41ba1b9de6533aca8ac4e45204c12f0fe34985485e1415b12a78c7bf70d571fc.jpg)  
Fig. 3. Four different captured red king images. All are the same size.

![](/api/attachments/NGB5ZNDB/fulltext/images/30fb6e9ba3aa2b81c54f0ac6088242c32ece9d48ddc3a418cb727b5dd9d756a8.jpg)  
Fig. 4. Playtech Blackjack hand

As an illustration of Point (3), if the Interface Agent expects an image to occur at a particular spot (like a card image) then a small change in position, perhaps implemented dynamically, could thwart the agent's ability to detect the image. At the least, this would complicate <sup>fi</sup>nding the image. As for timing-critical events of Point (4), a button may have to be clicked within a brief time span or a critical message might brie<sup>fl</sup>y be displayed.

Detecting non-human behavior might be an effective strategy as mentioned in Point (5). For example, if a Blackjack playing Interface Agent played more than a very few number of hours straight of perfect play, a monitoring casino might guess it was a software agent and not a human. In games of skill, solving a complex problem in a short period of time likely indicates agent play.

Finally, Point (6) is simplest to implement. In their study, Island Casino successively changed the rules to decrease the Blackjack game's expected value until it was negative even under optimal play. Many game-of-skill sites and casino gaming sites just implemented “no robots” allowed rules which were seldom enforceable unless monitoring as suggested in Point (5) was used. This is likely to decrease revenue as players of all caliber start paying more for less bene<sup>fi</sup>t. In the presence of competition that does not undertake such changes, business is likely to decrease further as consumers migrate to these “greener-grass” sites. Blogs and other mass communication mechanisms quickly disseminate such information.

In the following we detail some of the changes observed over the intervening years in Table 1.

## 2.1. Dynamic countermeasures

Perhaps the clearest evolution of countermeasures was made evident within the game of Blackjack. Online versions of this game quickly evolved to negative expected value. However, even then, the games were near break-even with relatively low variance (compared to alternatives like Jacks or Better video poker that also had near break-even expected values but much higher variances) so they remained prime targets for professional gamblers targeting casino promotion bonuses (see the Appendix for details about promotions). Some casinos merely counted on their house edge and hoped the majority of players were novices and unable to take advantage of such situations. Others implemented countermeasures.

![](/api/attachments/NGB5ZNDB/fulltext/images/f1182f322a7808cbc6c99388633f9b5da8210e859affc1174719d6e5e6e2cdd8.jpg)  
Fig. 5. Playtech Blackjack hand totalling 18.

![](/api/attachments/NGB5ZNDB/fulltext/images/c6cb55a3ae9608c289637c06c002658a99c840bc612c9747b4211dcdad4845e0.jpg)  
Fig. 6. Playtech obscured hand total.

One countermeasure was in dynamic game rules. RealTime Gaming casinos (http://www.realtimegaming.com/) enabled their operators to dynamically set and alter the rules of play even while a player was playing, possibly increasing the number of decks and other aspects of the game. This made it impossible to play an optimal game since the rules were unknown at any point in time.

Others casinos were more subtle. For example, Playtech casinos (http://www.playtech.com/) used what we call “dynamic cards”. Every time a card was displayed, it was slightly different. For example, in Fig. 3 are magni<sup>fi</sup>ed, captured images from four different hands containing a red king (suits are unimportant in Blackjack). As one can readily see, a simple pixel comparison recognition method will not work for these. Simple alternative recognition methods (e.g., converting color to grey-scale and then doing a pixel compare) also would fail. To the human eye, these four cards look identical (see Fig. 4 showing the true size of the displayed cards having the <sup>fi</sup>rst king displayed in Fig. 3). This is even more pronounced for numbers that can easily be made to look similar (e.g., 5 and 6 or 3 and 8). For these dynamic cards, Interface Agent LS used a complex recognition method with a training process that constructed 10 features from each image that then were fed into a decision list induction method that produced linear discriminant functions.

Although this scheme was very effective, when Playtech altered their mechanism which would have required LS to develop a new training set, LS took another, simpler strategy. When Playtech displayed a hand, they also displayed the card total in a small box next to the cards (see Fig. 5). These totals were easy to recognize but did not convey complete information. For example, a hard two-card hand total of 16 (i.e., a hard hand is a hand where an Ace is counted as a “1” not as an “11”) could be composed of a 10+6 or 9+7 or 8+8. The optimal play for a 10+6 or 9+7 is identical, but the optimal play for an 8+8 is different. As it turns out, other easily discernible items (like a button offering a split option when an 8+8 was displayed) could be used to ascertain hand components and thus correct play. Only a few hands of 3 or more cards could not be discerned at the level needed for optimal play, but the loss in expected value from optimal play was minimal.

![](/api/attachments/NGB5ZNDB/fulltext/images/4acc7799b36218a73bf5f396d166cc92fe78ed5138b98ba0293f9956875e9372.jpg)  
Fig. 7. RealTime gaming Blackjack hand.

![](/api/attachments/NGB5ZNDB/fulltext/images/059f788fde2110ef8aa6e21b396ba4447c1cec6889a3bda6104b847a6241ef86.jpg)  
Fig. 8. Scrolling jackpot value.

Eventually Playtech started altering the position of the totals and <sup>fi</sup>nally, for some casino instances and Blackjack-like games, obscured the total with a moving arrow (see Fig. 6). In the <sup>fi</sup>gure, the Arrow moves up and down, making recognition of the covered area very dif<sup>fi</sup>cult. Whether this was done intentionally or not is unknown. This tactic was used to a lesser extent by RealTime Gaming casinos, although probably by accident. Although their cards were not dynamic and were easily recognized (see Fig. 7), in some instances a hand would need too many cards to <sup>fi</sup>t in its allotted display space and the cards would be shifted left and an arrow would obscure a portion of the newest cards. This made the recognition task more complicated.

The most sophisticated method observed by LS was used by Boss Media casinos (http://www.bossmedia.com/) in their single-deck, Blackjack games. They used dynamic cards similar to those in Fig. 3. In addition, split hands were slightly rotated and as a hand got larger, the cards telescoped to look smaller. A human could readily discern these cards but Interface Agents would be challenged. Finally, once the dealer's hand was shown, all cards were removed within seconds. All of this made card recognition nearly impossible. Surprisingly, all these casinos used normal, easily recognized cards in other non-Blackjack games, such as their video poker games.

## 2.2. Detection

Interestingly, no detection methods were employed by casinos directly against LS. The closest encounter by LS had to do with multiple user accounts at casinos. Casinos did not offer sign-up bonuses to multiple accounts of the same user. Initially, many casinos recorded IP addresses across users to determine multiple accounts tied to a single IP. However, with many ISPs using dynamic IP addresses, this proved ineffective in tracking multiple accounts by a single user. For players running multiple accounts from the same computer, most casinos tried to catch them by identifying the machine's MAC address and tracking this information across user accounts. The MAC address is a unique value associated with a network adapter on a LAN. This was easily circumvented by changing the network card or through software like running different instances of VMWare (http://www.vmware.

com/) on a machine which creates virtual machines having their own virtual hardware (and hence their own MAC addresses).

Unlike LS, PRO and Interface Agent WinHoldEm encountered signi<sup>fi</sup>cant direct detection countermeasures. Within PRO's domain of usage, WorldWinner (http://www.worldwinner.com/) states in their rules (in bold):

“Anyone who displays behavior consistent with the use of unfair methods on the Site, including but not limited to … the use of unauthorized or altered software or hardware to assist play…, be subject to immediate sanction (as determined by the Site in its sole discretion), up to and including account termination and blocking of Site access .... Additionally, all winnings (if any) may be voided at the sole discretion of the Site.”

PRO was used on several games to see whether their words were backed-up with some actual detection device and, indeed, it was caught and the account terminated. All winnings were voided but the deposit was returned. At no other game site was PRO detected. It was also clear that many other users were using sophisticated Interface Agents at these other sites.

Although we do not have detailed, direct knowledge of WinHoldEm, its website has a detailed discourse of the detection and anti-detection methods used. The problem is described as:

“Online poker casinos do not want you to run WinHoldem. Some poker clients actively attempt to detect WinHoldem on your computer. There is nothing you can do to control how far they will go to do this. If they detect WinHoldem you are essentially at their mercy. Their reactions can range from just simply closing the poker software to closing your account and possibly conscripting your entire bankroll.”

The countermeasure taken by WinHoldEm in its simplest form was to install the casino software on a machine not having WinHoldEm software and to control the game using

![](/api/attachments/NGB5ZNDB/fulltext/images/58ffb4daacb03649902d4bc0db3fd2f7706735066d42f5e06072a0b414dc513e.jpg)  
Fig. 9. The HOLD values are text displays.

![](/api/attachments/NGB5ZNDB/fulltext/images/651b62671672c27db686f73c41921282730bb2f1d39d11914065aaf70637ac5d.jpg)  
Fig. 10. A RealTime gaming lobby.

WinHoldEm installed on another machine operating over a PCAnywhere (http://www.symantec.com/) connection to the computer where play took place. Although this setup avoids direct detection, it certainly imposes a higher technical expertise on the user's part.

## 2.3. Text tricks

Text plays a critical role in understanding and controlling many applications. Lists, buttons, registry entries, etc. contain options, choices, and other valuable information that an Interface Agent may need. Even the communication channel may yield useful text. CK noted that:

“Strangely, some of the communication from the web server to the applet was in cleartext, providing us with the important information concerning reshuf<sup>fl</sup>e points which our network sniffer detected and relayed to our software agent's monitor.”

This turned out to be an exception. In the intervening years, all network communication LS monitored was encrypted.

Much text is readily captured from applications or from the registry. Window messaging techniques enable a program to send a message to an application to retrieve text from lists, buttons, text <sup>fi</sup>elds, etc. The registry often contains important data that is easily retrieved by an Interface Agent.

LS encountered several countermeasures used by casinos to make text harder to discern. One way is to change text to a graphic image. For example, for progressive games, LS had to determine the current, ever-changing, jackpot value. Without the current jackpot value, optimal play cannot be determined. Playtech casinos would display the current value in a horizontally scrolling line (see Fig. 8 — here we show the current jackpot value is \$1,095.11). The font is not <sup>fi</sup>xed and the value moves, <sup>fl</sup>ashes and changes often so screen scraping or OCR detection is challenging. Surprisingly, although these values were very hard to capture within a game, many Playtech casino websites displayed the current jackpot values and these were readily downloaded by the Interface Agent using simply HTML protocols. Other casinos, like Random Logic's Casino On Net (http://www.888holdingsplc. com/) displayed the jackpot within the game but had a <sup>fi</sup>xed font and <sup>fi</sup>xed position that OCR methods readily determined.

RealTime Gaming casinos used text to display various important items. For example, in Fig. 9, the “HOLD” buttons are displaying text. They used different fonts on different machines, and possibly even on the same machine. As it happens, LS could discern these by focusing on the non-text area of the “HOLD” message, which was constant across machines.

LS used registry information often to set play options (like turning off sound, setting card sizes and play speed, etc.) and to determine things like the casino install directory. Almost all families of casinos stored useful information in the registry for downloaded casinos. Some critical options were only accessible through the registry (like setting Microgaming casinos — http://www.microgaming.com/ — to use a full-screen directx display which LS found the best display mode for this family of casinos.) Eventually some of this type of information was removed from registry entries as casino countermeasures.

## 2.4. Navigation

Another type of dynamic aspect was employed at RealTime Gaming casinos. Since LS loaded a casino, signedin and then navigated to the chosen game, it was imperative that the navigation be possible. Fig. 10 shows a portion of the “lobby” of a RealTime Gaming casino with a one hand Jacks or Better game being selected. Eventually, RealTime Gaming allowed the casino operators to dynamically alter this layout. This sometimes occurred multiple times in a day. The LS countermeasure was to offer a “Static Worker” component where the user navigated to the game of choice and then launched the worker to play the game. This was not ideal but suf<sup>fi</sup>ced.

![](/api/attachments/NGB5ZNDB/fulltext/images/e7b66d23a233151fc3578ed60d09b02ffca3714c3e48de2559814fabbca7f6be.jpg)  
Fig. 11. Boss Media menu.

Probably in an effort to ease user navigation, Boss Media casinos and some Playtech casinos used rollover menus. When selecting menu items, mouse movement, not mouse clicking, was critical. In Fig. 11 a human easily moves the mouse over the rollover menus, having sub-menus appear when the mouse pauses on a selection. Controlling smooth movements of a mouse by an Interface Agent is not so easy whereas issuing a click instruction at a point is trivial. Here is a case where easing human usage actually acts as a countermeasure for an Interface Agent.

Another feature was employed at several Playtech casinos. Key navigation information was displayed on a semi-transparent menu with dynamic background material. The dynamically changing background made recognition of graphical text menu items dif<sup>fi</sup>cult. This may become more pronounced as user interfaces become more customizable and employ features such as semi-transparent windowing (for example, in Microsoft's Vista (http://www.microsoft.com/) and in technologies such as Accelerated Indirect GLX — http://www.x.org/) .

## 2.5. Critical information

With LS and WinHoldEm, the most critical information needed by the Interface Agent was the value (ace, two, …, king) and, for most games, the suit (clubs, diamonds, hearts and spades) of all displayed cards. Some casino software readily supplied the raw card images they used in <sup>fi</sup>les that an Interface Agent could load and use for comparison and recogniztion, for example, OddsOn casinos (http://www.oddson.com/) and Random Logic casinos. Others made a small effort to hide the cards. For example, Microgaming casinos clearly identi<sup>fi</sup>ed card <sup>fi</sup>les but gave them an extension of “. dat” when they were actually “.pcx” <sup>fi</sup>les. Boss Media casinos supplied cards as slightly disguised “.bmp” <sup>fi</sup>les by subjecting each byte to an exclusive — or with “0×55”. Some casino families contained cards as part of their attached resources which could be readily queried and obtained using standard dynamic link library protocols. For example, Max Skyweb casinos (http://www.maxskyweb.com/) used this approach. Others, like RealTime Gaming proved elusive to obtain directly. However, once the card images were displayed in a game they could be captured and labeled by a human to form a training set. Often they were identical across virtually all the casino instances of this software (there were minor exceptions in the white background color at one or two casinos). For video poker games, Playtech cards similarly proved elusive to retrieve directly but only used a small variation in cards across all their casino instances so once captured and trained-for were readily available.

Other critical information included state information during game play, usually in the form of various buttons that could be clicked to choose play options (like splitting, doubling-down, etc. in Blackjack). With the exception of font differences at RealTime Gaming casinos, most used images that were constant across all casinos. In later releases, Playtech added some differences across casinos, but once LS was trained for these, they remained fairly static over time.

One interesting piece of critical information had to do with rare outcomes. For example, under optimal play, a Royal Straight Flush in Jacks or Better video poker occurs, on average, roughly every 43,423 hands. Some casinos would display something unusual when such rare events occurred. Unless the Interface Agent was prepared to handle these rare situations, unexpected results might ensue. This was true at Random Logic's Royal Diamonds game. This game would pay out the jackpot when a Royal Straight Flush in Diamonds was obtained. Since the game cost \$5 per hand and had a high house advantage ignoring high progressive pools, LS never was trained to see what happened when this rare event occurred. As expected, when users of LS did get the rare outcome, LS was unable to properly deal with the situation. This was undesirable because it would typically occur when no human user was around to take charge and handle the event.

## 2.6. Limiting opportunities

As reported in CK, they observed a number of rule changes in Blackjack that successively made the game less attractive. Their study ended noting that money could still be made with the attractive promotional bonuses like that discussed in the Appendix.

“Actually, most Internet casinos offer deposit bonuses of 5– 20% of a deposit. One need only wager each dollar of deposit and bonus once to keep the bonus. Hence, playing a breakeven game with an agent can still net a nice return.”

That is, most casinos at that time required a 1-time playthrough to earn the bonus. Over the years such opportunities changed from one to four then to ten and then twenty-times play-throughs. Even sixty-times and one-hundred-times play-throughs were not uncommon for some games.

Some casinos stopped offering these types of bonuses and switched to what are called “sticky-bonuses”. These bonuses could not be cashed-out yet still required a play-through. The idea was that one had more gambling money which protected against gambler's ruin. These bonuses were often used by professionals in do-or-die strategies discussed in the Appendix.

On top of these restrictions, some casinos imposed a slew of constraints that often would take a small research project to properly sort-out and understand. For example, the RealTime Gaming franchise Connect 2 Casino (http://www.connectocasino. com/) offers at the time of this writing a seemingly incredible <sup>fi</sup>rst purchase bonus:

“2000% Connect2 Welcome Bonus! On all deposits of \$20-\$500"

The “rules” associated with this bonus are, in small part:

“Unless stated otherwise all bonuses are sticky bonuses meaning that the bonus itself may not be withdrawn at any time. In the event of quick withdrawal attempts remember that losses are deducted off of deposits not bonuses. You have to meet wagering requirements to cash out/withdraw any winnings generated through your bonus. You may forfeit all winnings and bonuses and cash out the balance at any time without meeting playthrough requirements. TO MAKE IT CLEARER, bonuses are lost last after you've lost all deposits and winnings. The wagering requirements on all bonuses of 1000% and above are 60 times the amount of the deposit+bonus. The maximum withdrawable amount on such bonuses is half that of the bonus. All remaining funds will be removed from your account once your withdrawal is processed. A zero out is de<sup>fi</sup>ned as any balance of \$ 1 or less. Playthrough requirements carry over if you don't zero out and redeem 2 or more bonuses. Please ENSURE that you logout after zeroing out and depositing again otherwise the zero out will not be recorded. Wagering & all other bonus requirements carry over irrespective of zeroing out if any or all of the conditions mentioned below are satis<sup>fi</sup>ed:1N If you zero out, deposit again and don't take a bonus on your next deposit.2N If you zero out and your next deposit is less than half of your previous depositConnect 2 Casino does not … Etc.”

## 2.7. Mistakes

The authors are aware of groups who make a nice income searching for errors in online businesses and taking advantage of these errors. One common ploy in eCommerce settings is to use software agents to scan distributor inventory records daily looking for obvious day-to-day pricing errors. These errors often percolate to dealer sites. Large orders for items improperly priced far below their true value are then placed at such dealer sites with the intention of selling the goods on eBay (http://www.ebay.com/) or other auction sites.

LS saw different types of errors with casino games that were easily capitalized upon. For example, at one point Cytech casinos (http://aquagaming.com/) made an obvious mistake in their payout table for the video poker game 10's or Better. Normally this game is not attractive because of its low expected value. With the seemingly erroneous payout table, playing only 3 coins instead of the usual 5 coin game (which usually has the best payouts in a video poker game) had better per-coin payouts making the game a positive expected value game. As usual, LS was able to play this game optimally at a positive expected value. It didn't take the casinos long to observe this unusual focus by users on 3-coin play and <sup>fi</sup>x the error.

PRO playing at an early version of Flipside (http://<sup>fl</sup>ipside. com/) accumulated tens of thousands of credits when their server started randomly awarding credits, regardless of PRO's play.

A famous example of an error in online casino history was Random Logic's Casino On Net's “007 Contest” which offered double payout when zero–zero was hit in roulette. This makes the game an attractive positive expected value game. They stopped the game soon after starting it after losing more than \$1 million (much to their credit, they honored these losses).

Not all errors were in the player's favor. A now (apparently) defunct family of casinos by Max Skyweb had improper play in their Blackjack game. When a player had a Blackjack, the dealer would play and if he busted, the player's Blackjack was ignored and paid at the normal non-blackjack rate. In another case, RealTime Gaming brie<sup>fl</sup>y added discarded cards in video poker games to their pool of cards used to replace discards. This latter problem was corrected quickly when users complained.

## 2.8. Making interface interaction harder

Almost all interaction by an Interface Agent with a Microsoft Window's application requires the use of the handle for the target window component. The operating system assigns a handle when a window is created. For most of the period LS operated, window handles were easily obtained using the window name and/or class. Two casinos attempted to thwart this (again we do not know if this was done intentionally). First, Random Logic started dynamically changing the window names by using the window name to scroll various messages to a player. In effect the window name became dynamic. Later, Playtech gave the same window name to a large number of different windows. Determining which one corresponded to a particular interface component of interest was not trivial.

## 2.9. Browser-based offerings

Most online casinos are offered in two forms — either as a downloaded application or as a browser-based application. The downloaded games are usually more comprehensive, fullerfeatured and faster. Browser-based games were usually delivered as java applets, <sup>fl</sup>ash or shockwave applications or the like. Some casinos were exclusively downloaded applications and some exclusively browser-based. For casinos with both offerings, sometimes one environment offered better versions (i.e., better expected value games) than the other environment. LS experience found browser-based games more challenging than downloaded games for a number of reasons.

For example, a now defunct family of casinos, World Gaming (http://www.worldgaming.com/), offered browserbased java applets. These applets were notorious for not refreshing their components properly and LS had dif<sup>fi</sup>culty discerning the actual state of the application as a result.

Because browsers are often customized by users, a generic Interface Agent sometimes has a more dif<sup>fi</sup>cult challenge interfacing to browser-based games. Every client instance looks different. The Australian regulated Lasseters group (http://www.lasseterscorporationlimited.com/) offers a number of browser-based casinos. Much of the navigation is through normal HTML web pages and LS user customization of their browsers made navigation particularly challenging.

A feature introduced with Microsoft's IE 6 security upgrade displayed a loaded url in the title bar unless it was in a trusted site. This changed the top window name making it slightly harder to obtain a window's handle. The simple solution was to force programmatically an addition of needed urls to one's trusted sites. Likewise, the windowing structure (needed to determine a handle to needed information) for java-based casinos in browsers depended on whether Sun's (http://www.sun.com/) or Microsoft's java runtime environment was being used.

These problems were challenging within the same browser family (e.g., Internet Explorer). The problem is much more challenging if an Interface Agent supports multiple browsers (for example, Firefox — http://www.<sup>fi</sup>refox.com/ — and others) each having their own idiosyncrasies and quirks.

## 3. Merchant countermeasures: new recommendations

In the last section we see that all of the merchant countermeasure recommendations made by CK were seen over the ensuing years, plus some additional ones. Some were effective, at least for a period. Most were not and were easily overcome. We now summarize our insights in several key recommendations. We separate the recommendations into strategic and tactical suggestions, the latter organized as preventive and detective. The <sup>fi</sup>rst two recommendations are strategic.

## 3.1. Sound business model

An obvious but strategically important <sup>fi</sup>rst step is a sound business model. As exploitive agents can replicate and participate quickly and in large numbers, any business model <sup>fl</sup>aws would also be exploited at a much faster rate than in the physical world. In particular, if the internet environment allows an advantage to customers using decision support assets or relaxes controls in comparison to the physical world, then the business model may require review.

Early eCommerce models often were based on luring customers to sites in order to generate click-through traf<sup>fi</sup>c on ads appearing with their content. Often customers were lured with one-time rewards in the hopes of long-term market participation. Most of these types of sites were forced to alter their models over time, as one-time rewards were not suf<sup>fi</sup>cient to induce customer lock-in.

The competitive aspect of a business model is often related to the location, the value of time, information asymmetry, and customer lock-in, and often these aspects change in relevance in eCommerce businesses. Location and relative location as competitive aspects are obviously strategically altered in eCommerce. Models that assume a customer can only be in one place at one time are also at risk. Many business models based on the value of location assume that the time required to evaluating options is suf<sup>fi</sup>ciently high, as is often the case in the physical world, but that assumption is not valid in eCommerce models.

Business models that assume the customers cannot collude are at risk, collusion being de<sup>fi</sup>ned as having informational value contributed by other persons or agents not expected by the merchant to be present at the marketplace. This tends to reduce any information asymmetry advantage of the merchant. In the case of models that hold a mathematical advantage, this advantage can be eroded by computational or expert assistance from previously unavailable sources. Such sources cannot be prevented in the eCommerce world, though with some consideration a merchant can attempt to lessen the impact either contractually or via technology solutions as suggested below.

Along with a good business model is good business management. Even with an overall sound business model, deviations such as promotional events need to be properly assessed and vetted. If this cannot be done through a simulated environment, it should be restricted to a small enough subset of customers that can be assessed in real time. If the marketplace accepts more customers than the assessment mechanism can properly monitor, the merchant is potentially subject to signi<sup>fi</sup>cant losses. This implies that the assessment mechanism must be integral to the system and must scale with the system itself.

## 3.2. Systems design consideration

To the entire systems analysis and development process, we recommend that groups add considerations raised by

Conway and Koehler [10] who extended the idea of the third dimension of information design initially raised by Ba et al. [2]. Brie<sup>fl</sup>y,

“Systems designers must recognize the inherent shortcoming of any business information system and design an IS solution that monitors itself and is integrated with some form of risk/reward context. Some design facets are incentive based in nature. These are designed to raise the probability of positive system outcomes. Other design facets are deterrent in nature, attempting to discourage users from choosing negative system outcomes. The incentives and deterrents can be classi<sup>fi</sup>ed as preemptive, and are the subject of Ba et al. (2001). Other design facets must be forensic in nature, conceding that some intentional misuse is unavoidable and thus must be expected, detected, measured, and managed in real-time.”[10]

To this we add determining what information is critical for an Interface Agent to understand and operate their interface. This step should become an integral component of the analysis stage of software development.

The third dimension is about design that has built-in measures for behavioral variance, that is, it is about measuring differences from expected system behavior. Most applications are developed to be executed within a context that includes business process controls, and thus those controls are not explicitly designed into the solution. This research describes roughly how such systems can be exploited by malicious intentions when such code is executed outside of its intended context. It requires a designer be more aware of key informational elements of the operational model.

As this applies to Interface Agents, the design key is to note the environmental differences between a physical commerce exchange and a virtual commerce exchange. Just as analysts routinely specify business events and business activities during systems analysis (e.g., see [14] or [21]), so too should they inventory information that would be needed by an Interface Agent to operate the system. These components must be viewed as strategic elements that might need countermeasures in the design stages of software development. Once identi<sup>fi</sup>ed, such informational items must be scrutinized across all applications, so that a key piece of information is not protected in one place just to be made easily available in another.

The design stages must look at all aspects of a system — the graphical user interface, supporting resource <sup>fi</sup>les, registry entries, communication streams, test suites, etc., cataloging and tracking the <sup>fl</sup>ows and repositories of key information and validating the correctness of such information. For the third dimension, we also need to track key behavioral measures and compare them with expected behavioral measures. A measurable difference would imply one of the following: (1) the system is not being used as intended; (2) the system has a previously unknown <sup>fl</sup>aw; or (3) the system does not represent the business model as we understand the model. From that point, corrections would be required depending on the magnitude and direction of the deviation.

Once these are all understood, we make the following tactical recommendations. These should not be perceived as independent.

## 3.3. Dynamically alter display

The most effective overall strategy combines ideas (1)–(4) recommended by CK (see Table 1). Namely, dynamically alter displayed, critical information using graphics that humans can readily discern but are very hard for pattern recognition methods and do so in a way that timing becomes critical. That is, don't give such algorithms much time to capture and discern information nor make it easy to understand what is being displayed. This serves to increase the vocabulary with which the agent must reconcile to determine a match, preferably baf<sup>fl</sup>ing the agent entirely.

Baf<sup>fl</sup>ing an Interface Agent is also a reasonable way for a merchant to detect if the customer is in fact a software agent. This is often of short term value only, as the agent will likely learn and adapt. In fact, an agent could be designed to contact a human for ‘advice’ in real-time as a training mechanism, and depending on the value of the transaction, might request a ‘second opinion’ in cases of ample stakes. One could also occasionally compensate human victims of such intentional confusion in order to root out agents.

For textual information, avoid displaying text through easily retrieved components such as lists or buttons, and instead use graphical means altering fonts randomly if possible. When possible, obfuscate displayed critical information using movement or semi-transparent displays with randomly varying backgrounds, fonts and colors. Ensure that humans are not bothered with these methods, though in most cases legitimate users would likely support an effort to discourage Interface Agents anyway. Backgrounds and foregrounds, or even contrasts, are all legitimate candidates for agent input.

Avoid storing or transmitting text except in encrypted form. Even within an executable program, do not store plain text or key information in resources. Either read encrypted text from a <sup>fi</sup>le or registry, or store it as an encrypted resource or retrieve it dynamically (in encrypted form) from the merchant server. Note that client-side encryption can be observed by spyware monitoring CPU registers, and thus should not be critical to a business model.

## 3.4. Navigational obstacles

Navigation through an application should be constructed to be easy for humans but hard for an Interface Agent. Again, this might consist of slightly randomizing layouts, mousesensitive rollover menus, or transparent menus with dynamic backgrounds. Using browser-based applications with high graphical content helps here since the browser itself often entails high levels of user customization. Beware, though, that browser technologies like XML [18] make information more transparent.

## 3.5. Understand agent architecture

As a follow-up to the second strategic suggestion, try to understand the techniques an Interface Agent would have to use to get at or manipulate application interface information. For example, as discussed, under Microsoft Windows most such techniques need the handle of the window containing the needed information or the window providing the form of interaction (mouse, keyboard, etc.). Make it hard to <sup>fi</sup>nd and/ or use this handle. The easy ways to <sup>fi</sup>nd a handle rest on knowing a window's title and/or class. Make this hard either through redundancy (i.e., giving many windows the same names) or through dynamic alteration of the names.

Collusion is also a problem in many business models as described by CK. Agents participating in associations across a public internet will be less responsive due to the additional communication time, even in cases when the decision is trivial. Detecting collusion based on how agents are performing is dependent on the nature of the transaction and the executable time of the various decision support systems. Preventing collusion is nearly impossible in applications conducive to Interface Agents, as all external communication is decoupled from the client application. In the event of detection, proof of collusion would be equally challenging. This area remains open to further research.

## 3.6. Exploit rare events

If an application has important, rare events (like many casino games had as well as auctions), use previously unknown ways to show or announce these events. These might include unexpected or unique pop-up windows, displays of colors, or other unanticipated and even bothersome signals. Since they are rare and usually positive events for the customer, a legitimate user won't be irritated by their frequency. Again, legitimate users might be happy that the site is discouraging Interface Agents if they felt disadvantaged by such competition.

Rare events might also be decoupled into two stages of interaction, an announcement stage (e.g., ”congratulations”!) and a “click here to complete the transaction” stage. If it were a rare event and if the agent were unprepared for it, likely an unusually long delay in stage two, within the context of the outcome, could reveal an Interface Agent's presence. Along these lines, a merchant could occasionally post a simple challenge similar to a Turing challenge to test if the customer were human. Of course, if the agent could dynamically ask for human help in such situations, then rare events would be of little value to the merchant.

## 3.7. Monitor user behavior

Our weakest recommendation follows suggestion (5) by CK to track behavior. This is best manifested by direct detection devices. If the eCommerce activity involves some aspect of superior performance, the application should be monitored for this activity for possible sanction or study. Detection of possible collusion or shilling, when this can be used to advantage, is likewise important. Such detection would likely involve maintaining and analyzing transactions across time.

Screen scraping, image capturing, pattern recognition, determining optimal play, etc. all consume substantial CPU cycles and can easily be detected. Monitoring system processes of many high-performance customers can narrow the possibilities on which processes are involved in such activities. Of course, these processes could be named differently across users or even across usage instances, but will likely have some “<sup>fi</sup>ngerprint” that can be correlated. A merchant can then use these processes as indicators of potential Interface Agent usage. This of course brings up issues of privacy, and many client-side technologies might not have permissions for this level of access to the operating system. A negative of detection is that such methods can be technically defeated and that these methods have been known to generate false positives.

## 4. Other related settings

Before summarizing and presenting concluding remarks, we discuss several non-gaming settings that bear similar issues involved with Interface Agents. In general, any eBusiness situation where DSS tools can provide an advantage not present in face-to-face transactions is likely a candidate for exploitation by an Interface Agent. Even in eBusiness settings that are usually not face-to-face but where the normal interaction does not involve a DSS, Interface Agent use might be valuable. For example, situations where collusion or sophisticated DSS applications might give the consumer an advantage are commonplace. In particular, any activity where arbitrage across a variety of offerings exists is likely to be exploitable by Interface Agents. For example, auctions and complex market security trades are exploitable using DSS models to compute optimal positions (see Gregg and Walczak [13] for an auction agent) and even more so using shills and collusion (see Wang et al. [31]).

Interface Agents are attractive technologies for consumers because they are indifferent to the technical complications of encryption, dynamic middleware, and access control. They see what the intended user sees. The operations of data acquisition are used by many applications in the form of screen scrapers and keystroke loggers, and the other operations are common to decision support systems. Interface Agents provide an ideal way to implement such data acquisition. The cat-and-mouse struggle between merchants and customers will continue as the communication type extends to voice and other rich streaming media, a topic left for future research.

Most merchants desire to compete on something more than price, for example reputation, image or brand, trustworthiness, delivery/performance, or quality. Information aggregators tend to ignore these other properties and commoditize merchant offerings, forwarding a characterization of products represented only by price. Interface Agents magnify an aggregator's ability to acquire information from many sites, especially when these sites are designed to thwart agent access yet allow human access. Interface Agents can act like the intended human user.

The merchant then is in an awkward position of not being able to directly market themselves through information aggregators according to their own strategy, while at the same time wanting to be found attractive by general informational search engines like Google. In this case, the merchant would want to distinguish (a) the presentation of the marketing strategy using an easy to consume-by-agent structure (like Google's) from (b) the presentation of the pricing strategy using a dif<sup>fi</sup>cult to consume-by-agent structure. In this case, the strategy for the merchant would be to design a site that would be appealing to human consumers but appealing only to a subclass of agents excluding Interface Agents.

Related settings and technologies having similar challenges as Interface Agents are common too. One familiar merchant application is the digital market for attention — spam. In this market, spammers attempt to reach their human audience by creating content that <sup>fi</sup>ltering agents are unable to recognize as advertisement, and thus generally forward the message to avoid the chance of eliminating legitimate content. The <sup>fi</sup>ltering agents are not true Interface Agents, but have similar obstacles to overcome in the “Filtering & Recognition” and “Monitor & Assessment” activities. Frequently, the spammer attempts to bypass these operations by formatting their content as images. This signi<sup>fi</sup>cantly increases the size of the vocabulary used by the <sup>fi</sup>ltering activity, and thus makes the operation signi<sup>fi</sup>cantly more dif<sup>fi</sup>cult to perform in a short time period. Thus far, it has been a very effective solution for spammers. IBM reports [17] that “Image-based spam has increased linearly since 2005, and accounted for more than 40% of spam messages by the end of 2006.”

As another example, consider the following intellectual property application. A vehicle manufacturer hopes to produce language neutral repair manuals by publishing certain CAD drawings. A certi<sup>fi</sup>ed repair facility can then acquire these drawings and search the image database in order to obtain a visual idea of how components should appear and how they should <sup>fi</sup>t together. The downside is that any spyware on repair shop computers can also access the drawings, and thus steal the associated intellectual property. Eventually, mock parts could be reproduced with this information. Thus, the key is to produce information that a human can meaningfully consume while an agent cannot, similar to the Interface Agent problem.

The intellectual property problem above has some other interesting characteristics as it relates to the time-value of information. In the casino examples, we had a digital product with a simple vocabulary and a short life (a casino would log the Interface Agent off if it did not respond in a reasonable time). In the intellectual property example, agents could work for years toward understanding the more complicated digital product, and if successful, could use that information for years afterwards. In the intellectual property world, a key solution might be to alter the mathematics of the drawing so that a human could still “get the idea” without the product being capable of being used by numerically controlled machines. Of course, screen scraping technologies are inherently two dimensional, whereas a CAD drawing is three-dimensional (or four with a motion dimension), thus making the obfuscation process more natural.

## 5. Summary and conclusions

Interface Agents are software agents that assist in making eCommerce decisions based on information intended solely for human consumption, and attempt to participate with behavior indistinguishable from human users. This paper presents an update to the state of Interface Agents <sup>fi</sup>rst presented ten years ago by the same authors, and provides a history of internet merchant attempts to prevent and detect such agents. Many of the issues identi<sup>fi</sup>ed in the earlier research were indeed addressed during the ten year period, and several other merchant responses are discussed here. We provide further suggestions for merchants who are involved in transactional business where decision support systems can lead to negative merchant outcomes.

As any eCommerce site must use an interface for its intended audience, we provide tactical suggestions for merchants to discourage Interface Agents, including suggestions on dynamically altering the display in an attempt to confuse an agent, creating navigational obstacles, understanding the agent architecture, exploiting rare event where agents are likely not important though are the business model implications. Certain business models which prevent decision support systems made available by informative contacts (collaboration, collusion) or the advantage of advanced mathematics or computational assistance may simply not be pro<sup>fi</sup>table in an internet setting, where such support is impossible to prevent.

![](/api/attachments/NGB5ZNDB/fulltext/images/1f1511d1348d928faa4b2c8313d838e003449cbf767e50a2703cc21d6953bcb9.jpg)  
Fig. 12. LS schedule page (top portion).

We end with a <sup>fi</sup>nal observation. An assumption made by CK was that Interface Agents can be detrimental for eCommerce. This need not always be true. In many settings that the PRO and WinHoldEm agents played, the sites took a percentage of each fee or wager (a rake). Since they get the same fee from a software agent as a real human, they may not have an incentive to restrict software agents except to the extent that human players may eventually avoid their site to avoid playing against the superior software agents or, in a more general view, provide the additional revenue to merchants to make up for the higher opportunities enjoyed by Interface Agents. This moral hazard should be explored further.

Much effort in the past several years has gone into the integration of people, processes, and technology. The application-to-application integration is known as enterprise application integration (EAI) [20]. It was made possible by the standardization of web service protocols. People-to-people integration is known as work<sup>fl</sup>ow, and work<sup>fl</sup>ow has also received signi<sup>fi</sup>cant attention [32]. Finally, business process management systems are emerging which enable communication between people and applications in any combination [20]. In all cases, the communication is designed to enable easy communication between pairings. We consider the problem of designing application-to-people applications that are explicitly not application-to-application.

![](/api/attachments/NGB5ZNDB/fulltext/images/0ecd4ad2847e2bd5d74890670fa70129f1146389e9795e1bb2fb3154275bbeb1.jpg)

In most cases, the design goal is not perfect prevention, but rather system design to be more dif<sup>fi</sup>cult for an agent to exploit than a competing site with otherwise similar business rules over a typical transaction's time period of interest.

Our experience and contribution applies to agents who interact with either text or graphically displayed information. While the agents we describe have been successful in defeating the merchant designs, we anticipate continuing catand-mouse tactics will continue to evolve with each side having some degree of success. Design issues with communication in the format of streaming media are not addressed in this research.

## Appendix A

Below we discuss the three Interface Agents: LS, PRO and WinHoldEm.

## LS Interface Agent

The online casino industry grew from its beginning around 1997 to a \$3.3 billion industry in 2005 with a compound annual growth rate of approximately 26% (http://www.partygaming. com/about\_us/bingo\_casino.html)<sup>1</sup>. Software <sup>fi</sup>rms specializing in such systems quickly dominated the initial offerings. For example, Playtech, a publicly traded company on the AIM market of the London Stock Exchange (PTEC.L), started in 1999 and (at the time of this writing) licenses its software to about 70 operators such as Royal Dice Casino (http://www.royaldice. com/) and Casino King (http://www.casinoking.com/). Each Playtech operator's casino software has a unique look and feel, although the game screens have a lot of similarity.

“Playtech's online casino features over ninety richly themed games to suit all markets and player types, from classical table & card games, multi-line & multi-spin slots and video poker & keno, to progressive bonus-stage jackpot games, Asian games, live dealer games and Playtech's exclusive Blackjack Switch.”

Other big software providers are RealTime Gaming, Microgaming, OddsOn, Boss Media and Cryptologic (http:// www.cryptologic.com/) with many smaller <sup>fi</sup>rms. Some popular operators have their own software such as Random

![](/api/attachments/NGB5ZNDB/fulltext/images/b783ab47b47f247e068042e5183a971711d88767415ac95218ec43cfedb64992.jpg)  
Fig. 13. Num Runner.

Logic. All in all, LS interfaced with over 25 such software families which included roughly 1,000 different operator run casino sites. Part of the LS system collected statistics to monitor outcomes of play. A small group of professional gamblers used LS, racking up close to \$500 million in total wagers over the years. This provided a wealth of data to determine casino honesty, to monitor casino countermeasures and to gather experience to suggest possible Interface Agent countermeasures.

Games supported by LS included various versions of Blackjack including related variants like Pontoon and Caribbean 21, many regular and progressive video poker games including

<table><tr><td>Aces and Faces</td><td>Loose Deuces</td></tr><tr><td>All Aces</td><td>Jacks or Better</td></tr><tr><td>All American</td><td>Joker Poker</td></tr><tr><td>Deuces Wild</td><td>Royal Diamonds</td></tr><tr><td>Double Bonus</td><td>10s or Better</td></tr><tr><td>Double Jackpot</td><td>Two Way Royals</td></tr><tr><td>Double Double Jackpot</td><td></td></tr></table>

and miscellaneous slot games, and other specialty games (e.g., War and 3 Card Poker).

Not all these games could be played to yield positive expected returns directly (but were required to meet various additional goals.) There are several clever ways around this that LS users developed. We detail three such strategies below to give a <sup>fl</sup>avor of the usage and bene<sup>fi</sup>t of an Interface Agent such as LS.

Casinos often offered promotions in the form of bonuses for deposits which could tip a negative expected value game into the positive region. These bonuses would require a many times play-through of the deposit amount. For example, at the time of this writing, Royal Dice Casino offered: “Deposit \$500 receive \$500, play with \$1000.” The wagering requirement was “For play on all games other than as speci<sup>fi</sup>ed below — 20× the aggregate value of the bonus+deposit before withdrawing any winnings …” So one would have to place wagers of at least \$20,000. For example, optimal play of the typical Jacks or Better video poker game has an expected value of \$0.995439 on a \$1 bet so the expected outcome would be a loss of \$91.22 on the \$20,000 wager leaving an overall expected pro<sup>fi</sup>t of \$500–\$91.22=\$408.78. (By the time of this writing, Jacks or Better could not be used for this wagering unless 60 times the aggregate was wagered which would still yield an expected pro<sup>fi</sup>t of \$226.34). For this strategy, care is needed to minimize gambler's ruin [11] which results when one has suf<sup>fi</sup>ciently long runs of losses to wipe out their gambling resources (here the \$1000). Making wagers suf<sup>fi</sup>ciently small relative to the \$1000 reduces this risk to negligible values. Of course, the number of hands required to play-through \$20,000 or \$60,000 in wagers with small bet sizes would be long. But an Interface Agent can play without fatigue or boredom, with or without the human present.

A second strategy, called a do-or-die strategy, was used when bonus rules were restricted to very low expected value games (like slots games). In such situations it is optimal to place few very large wagers (sometimes on allowed but nonqualifying) games having high payout variances in hopes of hitting one of the high-payoff outcomes (the “do” part of door-die) and then to work off the wager requirements on the required low expected value game. LS would do the grinding work-off. More often than not, the deposit and bonus would be quickly lost (the “die” part of do-or-die), but over the long run the net can be positive since a sizeable part of all wagers was free bonus money.

A third strategy involved progressive games. With progressive games, a casino takes a small part of each wager (e.g., 5%) and adds this into a jackpot pool. For example, with Jacks or Better, the highest payout (for a Royal Straight Flush) wins the total pool. The pool is then reset to a value that is typically lower than the non-progressive form of the game. For example, the non-progressive payout is \$1000 for a \$1.25 game of Jacks or Better. The reset value for the progressive game at Royal Dice casino was just over \$300. As the progressive jackpot grows, the games switches to a positive expected value game when the pool hits around \$1220. LS could be scheduled to watch the level of the payout and then start play when it hits this point (or higher as users speci<sup>fi</sup>ed) and play optimally for the current payout level thus ensuring positive expected value play. Playing optimally would be very hard for a human since optimal play changes often with the changing jackpot value.

LS operated as follows. A control component let users manage their gambling. One screen enabled the user to manage account ids and passwords for the various online casinos. The schedule screen (a portion shown in Fig. 12) enabled one to set up a set of game schedules at various casinos. For example, one might schedule \$5,000 of play of Blackjack at casino A with bets ranging from \$1 to \$10; \$6,000 of Jacks or Better at casino B betting <sup>fi</sup>ve \$1 coins per hand; etc. Various options were available to mimic human behavior such as random pauses, random click positions on buttons, rest breaks, etc. Even sub-optimal play that gave up very little expected value could be selected to avoid being observed as a “perfect player”. Other screens gave access to statistical analyses across all or select user's games, provided gambler's ruin analyses, managed sub-accounts, etc.

Once schedules were prepared, a second component, the worker, was launched. The worker agent was the actual Interface Agent and would work through the schedules, <sup>fi</sup>rst loading the casino application, sign-in typing ids and passwords, navigate to the desired game by working through menus, clicking options, etc., and then play optimally (or otherwise as selected by the user) and exit cleanly when done. A schedule might be partially completed and the game and casino exited to switch to another casino so as not to alert the casino to extraordinarily long play. This continued until all schedules were completed. Local logs showed the details of each hand of play for possible review by the human user. All game details were collected on a central server for statistical analysis across all LS users.

Of course, the human user need not be physically present during any of this play. Indeed, for progressive games a schedule includes a jackpot start point. A third LS component, called “watcher” would monitor the jackpot and start the worker agent once the jackpot reached the scheduled trigger.

## PRO Interface Agent

Skill games are offered in cash tournaments where players pay cash entry fees and play against other such players to win cash or merchandise prizes. Skill games rely mainly on a player's logic, speed, dexterity and problemsolving skills, while casino games are controlled mainly by chance. By de<sup>fi</sup>nition, skill gaming eliminates (or greatly reduce) chance and thereby avoids laws prohibiting gambling (although some US states outlaw games of skill). Examples of skill games are strategy games, word games, sports games (like online pool), arcade games, and even card games (see WorldWinner for instance). This market segment generated “\$100 million in revenue in 2005. With a compound annual growth rate of between 25 and 35%, skill game tournament entry fees should exceed \$1 billion by the year 2009 [27]”.

Entrants to a cash-based, skill game pay an initial fee from which the house extracts a service fee. The remainder forms the pool. For two-person games, a simple match determines the winner. Multiple player games often go through a knockout elimination process. The winner wins the pool. Some progressive versions have multiple “placed” winners. Variants of this model don't require fees but instead reward winners with tokens that can be used to trade-in for gifts or to buy lotteries for prizes (e.g., FlipSide or iWin — http://www. iwin.com/).

There are many websites, such as GameAccount (http:// www.gameaccount.com/) and WorldWinner that pit users against each other. For example:

“Established in the United Kingdom in April 2001, GameAccount Global Limited (“GameAccount”) operates a network of websites (“the GameAccount Network”) dedicated to person-to-person games of skill for real money. Every week the equivalent of millions of dollars are won by players competing within the GameAccount Network from over 130 countries worldwide.”

PRO was developed to play slightly over 10 different games of skill. PRO used the basic Interface Agent model developed for LS but had more dedicated DSS components. For example, for the game Num Runner (see Fig. 13), one tries to clear the most blocks from the board without hitting a bomb or picking a move that would run off the board or into an already cleared spot. A move entailed picking a block next to the green ball which then resulted in the green ball moving in that direction the number of blocks indicated on the selected block. Usually there is a small time limit (like 3 minutes). The player scoring the highest number of blocks removed in the time limit wins. PRO would start the game, scan the board to determine the positions of bombs, the green ball and all the numbered blocks and then invoke its DSS component. The DSS component performed a multi-threaded, depth-<sup>fi</sup>rst search of moves that would time-out leaving suf<sup>fi</sup>cient time to actually let PRO click-through the game to implement the best path found during the search phase. This heuristic was suf<sup>fi</sup>cient to beat human players, but sometimes lost against what we believe were other “bots”.

## WinHoldEm Interface Agent

Online Poker, in particular, the game Texas Hold'Em, started around 1998 but became very popular after TV coverage of the World Poker Tour (http://www.worldpokertour.com/) and ESPN's World Series of Poker (http://www. worldseriesofpoker.com/) started in 2003. “Nearly one in <sup>fi</sup>ve American adults played poker during the previous 12 months” (PartyGaming — http://partygaming.com/). A leader in online poker games is PartyGaming which started in 1997 and went public in June of 2005. PartyGaming Plc is listed on The London Stock Exchange under the ticker: PRTY. They report that “online poker players generated gross revenue in 2005 of \$2.6 billion … this was almost double the \$1.4 billion achieved in 2004.” Of course, these numbers are all expected to decrease as discussed earlier<sup>1</sup>.

Texas Hold'Em is played on a table with, typically, 2 to 10 players and a dealer who deals cards and removes a small percentage of each bet for the house (the rake). Initially, players receive two cards face down. This is followed by a round of betting. Then three face-up, community cards, are exposed followed by another round of betting. Two more rounds of exposing another community card followed by betting are carried out. The highest poker hand formed from the best combination of any remaining player's two private cards and 5 community cards wins the <sup>fi</sup>nal pot (less the rakes, of course).

Unlike Video Poker or games of skill, like Num Runner, optimal play of Texas Hold'Em cannot be easily computed. Strickly speaking, a Nash Equilibrium exists and in principle could be computed [22] (although efforts to do so have not yet completely succeeded but are getting close [3] at least for the two-person version). The two-person Texas Hold'Em poker game requires O (10<sup>18</sup>) size to represent [3]. However, it has been shown that the meager edge that a Nash Equilibrium offers can be exceeded by including consideration of psychological factors [4]. Bluf<sup>fi</sup>ng, laying traps, understanding opponent's quirks and behaviors all can increase the expected win as demonstrated in [19]. Collusion offers even greater advantages.

Considerable effort has been invested in developing computer-based poker players, especially by the University of Alberta's Computer Poker Group [8]. Their software is state of the art, easily beating other software agents (see the 2006 AAAI Computer Poker Competition [1]) and most human players.

The most popular commercial Interface Agent for playing online poker is WinHoldEm. WinHoldEm was created by ex-RealTime Gaming programmer Ray E. Bornert II around 2001 and was described in an interesting popular-press article [23] and brie<sup>fl</sup>y discussed in an earlier article [5]. This software agent has two general forms — a single player form (which has several versions — basic, speed and pro) and a team form. The latter version allows collusion between separate players (on a team) playing in the same game. WinHoldEm didn't offer a complete DSS to play poker, but rather an engine into which users could craft their own strategies. Users build “formulas” that tell the software how to handle the various decisions needed in poker — e.g., calling, raising, etc. These rule-based formulas have been re<sup>fi</sup>ned, shared, and expanded by users in forums.

## References

[1] AAAI Computer Poker Competition, at the Twenty-First National Conference on Arti<sup>fi</sup>cial Intelligence in Boston, MA, July 16–20, 2006, http://www.cs.ualberta.ca/\~pokert/.

[2] S. Ba, J. Stallaert, A.B. Whinston, Research commentary: introducing a third dimension in information systems design — the case for incentive alignment, Information Systems Research 12 (3) (2001) 225–239.

[3] D. Billings, N. Burch, A. Davidson, R. Holte, J. Schaeffer, T. Schauenberg, D. Szafron, Approximating game-theoretic optimal strategies for full-scale poker, Proceedings of the 2003 International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI-03), 2003

[4] D. Billings, A. Davidson, J. Schaeffer, D. Szafron, The challenge of poker, Arti<sup>fi</sup>cial Intelligence Journal 134 (2002) 201–240.

[5] Brunker, M. Are Poker ‘Bots’ Raking Online Pots? MSNBC, September, 2004. http://www.msnbc.msn.com/id/6002298/.

[6] T. Bui. I. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (1999) 225–237.

[7] K. Chellapilla, K. Larson, P. Simard, M. Czerwinski, Computers beat humans at single character recognition in reading based Human Interaction Proofs (HIPs), Microsoft Research, Redmond, WA 98053, 2006.

[8] Computer Poker Research Group, University of Alberta. http://www.cs. ualberta.ca/\~games/poker/, 2006.

[9] D. Conway, G.J. Koehler, Interface Agents: caveat mercator in electronic commerce, Decision Support Systems 27 (4) (2000) 355–366.

[10] D. Conway, G.J. Koehler, Information Systems Design: In<sup>fl</sup>uence Assets, Counter-Interests, and Risk Management, Department of Decision & Information Sciences, Warrington College of Business, University of Florida, Gainesville, FL., 2003.

[11] W. Feller, An Introduction to Probability Theory and Its Application (chapter XIV: Random Walk and Ruin Problems), vol. 1, John Wiley & Sons, New York, 1968.

[12] J. Goldsmith, T. Wu, Who Controls the Internet? Illusions of a Borderless World, Oxford University Press, New York, NY, May, 2006.

[13] D.G. Gregg, S. Walczak, Auction advisor: an agent-based online-auction decision support system, Decision Support Systems 41 (2) (2006) 449–471.

[14] J.A. Hoffer, J.F. George, J.S. Valacich, Modern Systems Analysis and Design, Fourth EditionPearson Education, Upper Saddle River, NJ 07458, 2005.

[15] R.E. Hostler V.Y. Yoon T. Guimaraes Assessing the impact of internet agent on end users' performance, Decision Support Systems 41 (1) (2005) 313–323.

[16] H.R. 4954, the “Security and Accountability For Every Port Act of 2006”. http://www.cbo.gov/ftpdocs/76xx/doc7681/hr4954pgo.pdf.

[17] IBM Internet Security Systems, X\_Force 2006 Trend Statistics, Jan 2007 http://www.iss.net/documents/whitepapers/X\_Force\_Exec\_Brief.pdf.

[18] S. Jacobs, Beginning XML with DOM and Ajax: From Novice to Professional, Apress, Inc., Berkeley, CA, June, 2006.

[19] U. Johansson, L. Niklasson, Why settle for optimal play when you can do better, International Conference on Application and Development of Computer Game Conference in 21st Century, 22 – 23 November, 2001.

[20] Rashid N. Kahn, Business Process Management: A Practical Guide, Meghan–Kiffer press, 2004.

[21] K.E. Kendall, J.E. Kendall, Systems Analysis and Design, Pearson Education, Upper Saddle River, NJ 07458, 2005.

[22] D. Koller, A. Pfeffer, Representation and solutions for game-theoretic problems, Intelligence Journal 94 (1997) 167–215.

[23] Kushner, D. On the Internet, Nobody Knows You're a Bot. Wired Magazine, 13.09, 2005, pp. 96-100. http://www.wired.com/wired/ archive/13.09/pokerbots.html.

[24] X. Li, X. Sun, Re<sup>fl</sup>ective Intelligent Interface Agent. Paper submitted to 14th Australian Joint Conference on Arti<sup>fi</sup>cial Intelligence, Adelaide, Dec. 2001.

[25] N.G. Shaw, A. Mian, S.B. Yadav, A comprehensive agent-based architecture for intelligent information retrieval in a distributed heterogeneous environment, Decision Support Systems 32 (4) (2002) 401–415.

[26] Swoboda, E. I-Gaming 2010 — A Dismal Outlook. Interactive Gaming News, Dec. 1, 2006, http://www.igamingnews.com/index.cfm? page=artlisting&tid=7161.

[27] The IGDA Casual Games SIG, Casual Games White Paper, , 2006 http:// www.igda.org/casual/IGDA\_CasualGames\_Whitepaper\_2006.pdf.

[28] R. Vahidov, R. Fazlollahi, A multi-agent DSS for supporting e-commerce decisions, Journal of Computer Information Systems 44 (2) (2003) 87–94.

[29] R. Vahidov, G.E. Kersten, Decision station: situating decision support systems, Decision Support Systems 38 (2) (2004) 283–303.

[30] L. von Ahn, M. Blum, N.J. Hopper, J. Langford, CAPTCHA: using hard AI problems for security, Eurocrypt, 2003, Warsaw, Poland.

[31] W. Wang, Z. Hidvegi, A.B. Whinston, Shill bidding in multi-round online auctions. HICSS, Proceedings of the 35th Annual Hawaii Internationa Conference on System Sciences, Jan. 7–10, 2002.

[32] Work<sup>fl</sup>ow Handbook, 2006. Published in association with the Work<sup>fl</sup>ow Management Coalition.

Daniel G. Conway is a clinical associate professor at the Kelley School of Business, Indiana University. He received his Ph.D. from Indiana University in 1992. He has held academic positions at Virginia Tech, the University of Florida, and the University of Notre Dame. His research interests include enterprise risk management, enterprise computing, business process management, and decision support systems. He has published in journals including Decision Support Systems, the European Journal on Operational Research, Annals of Operations Research, and Production & Operations Research and others.

Gary J. Koehler is the John B. Higdon Eminent Scholar of Management Information Systems at the University of Florida. He received his Ph D. from Purdue University in 1974. He has held academic positions at Northwestern University and Purdue University and between 1979 and 1987 was a cofounder and CEO of a high-tech company which grew to over 260 employees during that period. His research interests are in areas formed by the intersection of the Operations Research Artificial Intelligence and Information Systems areas and include such areas as genetic algorithm theory, machine learning, eCommerce, and decision support systems. He has published in journals including Management Science, Operations Research, Journal on Computing, Evolutionary Computation, Decision Sciences, Decision Support Systems, the European Journal on Operational Research, Computer Technologies and Information Systems: IIE Transactions on Operations Engineering, SIAM Journal on Control and Optimization, Discrete Applied Mathematics, and many more. He is an area editor for Decision Support System and is on several other editorial boards. He has served as an expert witness for many large <sup>fi</sup>rms (including AT&T), has been an Externa Examiner for several Universities and has worked under grants from IBM and the National Science Foundation.
