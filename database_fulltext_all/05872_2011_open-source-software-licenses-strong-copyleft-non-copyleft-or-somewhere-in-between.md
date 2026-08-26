---
otero_id: 5872
otero_key: "G3B3SH9H"
title: "Open source software licenses: Strong-copyleft, non-copyleft, or somewhere in between?"
authors: "Ravi Sen; Chandrasekar Subramaniam; Matthew L. Nelson"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.07.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Open source software licenses: Strong-copyleft, non-copyleft, or somewhere in between?

Ravi Sen <sup>a</sup>, Chandrasekar Subramaniam <sup>b,</sup>⁎, Matthew L. Nelson <sup>c</sup>

<sup>a</sup> Department of Information and Operations Management, Texas A&M University, United States

<sup>b</sup> Department of Business Information Systems and Operations Management, University of North Carolina, Charlotte, United States

<sup>c</sup> Department of Accounting and Business Information Systems, Illinois State University, United States

## a r t i c l e i n f o

Article history: Received 20 January 2010 Received in revised form 1 July 2011 Accepted 16 July 2011 Available online 23 July 201

Keywords: Open source Software license OSS FLOSS Copyleft Copyright

## a b s t r a c t

Studies on open source software (OSS) have shown that the license under which an OSS is released has an impact on the success or failure of the software. In this paper, we model the relationship between an OSS developer's utility, the effort that goes into developing an OSS, his attitude towards the freedom to choose an OSS license, and the choice of OSS license. We <sup>fi</sup>nd that the larger the effort to develop OSS, the more is the likelihood that the OSS license would be free from restrictions. Interestingly, the result holds even when all OSS developers prefer restrictive licenses or less-restrictive license. The results suggest that least-restrictive or non-copyleft license will dominate other types of OSS license when a large effort is required to develop derivative software. On the other hand, most-restrictive or strong-copyleft licenses will be the dominant license when minimal effort is required to develop the original OSS and the derivative software.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Stallman's revolutionary idea in 1984 about free software subsequently evolved into the current open source software (OSS) movement [21]. Some notable examples of OSS are Linux (operating system), Firefox (web browser), Apache (web server), Sendmail (email server), Bind (DNS server), and Open Of<sup>fi</sup>ce (suit of productivity software). The mobile software developers now have the Android open source operating system. The success of open source software can be attributed, in part, to its lessrestrictive licenses. Unlike commercial software licenses, an OSS license allows users access to the source code of the software, and gives them the freedom to modify the software and create derivative works, and to redistribute the modi<sup>fi</sup>ed software/derivative works for free or for pro<sup>fi</sup>t. Open source development avoids the inef<sup>fi</sup>ciencies of a strong intellectual property regime [5,11,14] and can create at least as much total welfare as traditional closed licenses [13]. Recent developments in the theory of diffusion of technologies with network externalities suggest that OSS is here to stay [1,17].

Within the overall philosophy of open license, there is considerable heterogeneity among the various OSS licenses [16]. For example, some OSS licenses require that the derivative software uses the same license as the original software, while some other OSS licenses do not impose such restrictions. Open source licenses are reviewed and approved by

OSI (Open Source Initiative).<sup>1</sup> OSS project administrators, who are themselves developers, use the license to signal their intentions to other developers and users about the project. Studies on open source software have also shown that developers choose to participate in open source projects that are aligned with their motivations and attitudes [15]. Since an OSS license, once chosen, typically does not change over the life of the project [4] and the license choice affects the success of the OSS project [e.g. 22,23], it is important to understand the nature of these licenses and how the license choices are made. Despite the signi<sup>fi</sup>cance of OSS license for the open source community, there is limited research on understanding OSS license choice from a developer's perspective.

This paper uses utility maximizing approach to investigate OSS developers' optimal choice of OSS license and its implication for the future of OSS licenses. The paper models the interactions between OSS developer's utility, his preferred license, the effort that goes into developing an OSS, and the importance of the freedom to choose an OSS license. The model is then solved to identify the optimal license that maximizes the OSS developer's utility from OSS development. Our research is one of the few analytical works on the topic of OSS license from a developer perspective and can help to improve our understanding of the dynamics of this choice as faced by the developers. Previous studies have looked at the developers' preference for a speci<sup>fi</sup>c OSS license type [10,18], but have not examined the actual license choice. Our study also extends beyond the current models of two extremes of license choices (i.e., most-restrictive and least-restrictive) and uses a generalized license that covers the range of restrictiveness between the extremes. Our analytical <sup>fi</sup>ndings provide some interesting insights into open source project managers' optimal license choice which we discuss in the conclusion. The remainder of the paper is organized as follows. The next section presents a review of related literature followed by our model of OSS license choice and its analysis. The results of the analysis and their implications for theory and practice are discussed next. We conclude the paper by acknowledging our study limitations and suggesting potential research opportunities.

## 2. Related literature

Researchers have recently used different perspectives, including innovation diffusion [e.g., 4,27] and social participation [e.g., 2,8], to understand open source development. However, the open source software license, which allows software to be freely modi<sup>fi</sup>ed and redistributed, distinguishes open source software from other types of software [22] and needs greater attention. According to the Open Source Initiative (OSI at www.opensource.org), a non-pro<sup>fi</sup>t body for reviewing and approving open source licenses, an Open Source Software License is one that complies with the Open Source De<sup>fi</sup>nition and goes through the OSI approval process. Since the license of open source software de<sup>fi</sup>nes the conditions for using, modifying, updating and distributing the software, the license can signal the overall utility of the software to potential users.

One of the dimensions of variance across OSS licenses is the restrictiveness of the license and these restrictions affect users' perception of the likely costs and bene<sup>fi</sup>ts of software and reduce its perceived usefulness among potential users [22]. However, some studies on open source have shown that OSS licenses can create at least as much total welfare as traditional closed licenses [13]. The decision to choose a particular license for an OSS project is important as the license, once chosen, typically does not change over the life of the project [6] and has a signi<sup>fi</sup>cant impact on the success of the project [22]. OSS projects could use the license to signal their intentions to other developers and users about the project's directions.

Studies on open source software have shown that developers choose to participate in open source projects that are aligned with their motivations and attitudes [15,24]. In studying the antecedents of open source license, Lerner and Tirole [10] focus on OSS project characteristics such as operating system on which the OSS will run, and the programming language used to develop the OSS. A more recent study investigates the relationship between OSS developers' motivations and attitudes and their preferred OSS license [18]. They <sup>fi</sup>nd that developers may not always prefer lower restrictions on open source software and the trade-off between developers' beliefs about “open source” and the consequences of the project decisions based on those beliefs, such as the impact on project activity or success, may be important in license choice. While preference for an OSS license might signal intent to use that license in their next OSS project, the intent might not necessarily translate into the actual choice of that preferred license. For example, in the context of marketing, it is well known that consumers' self-reported purchase intentions do not perfectly predict their future purchase behavior, nor do these differences cancel each other out when intentions and behavior are aggregated across consumers [12,20]. Therefore, there is a gap in OSS research and a need to go beyond understanding the determinants of preferred OSS license and study the determinants of actual OSS license choice.

## 3. Model

Since the license of open source software de<sup>fi</sup>nes the conditions for using, modifying, updating and distributing the software, the license can signal the overall utility of the software to potential users. The proposed analytical model is based on the assumption that open source projects are initiated by a need for software that is not currently available in the form preferred by the OSS developer [19]. However, the choice of license is guided by the OSS developer's desire to maximize his utility by improving the likelihood of his OSS project's success, as measured by the adoption of OSS by others, and its integration into other open source software [23]. The key elements of the model are described below and a table of the notations used is provided in Appendix A.

## 3.1. Open source software license

All open source licenses are essentially the same in terms of freedom to use, modify, and redistribute the original version of the OSS. However, one key characteristic that differentiates various OSS licenses is the degree of restrictions imposed on the ability of the user to redistribute modified version(s) of this OSS or derivative work(s) based on this OSS[6]. Lerner and Tirole [10] propose three classes of OSS licenses based on the restrictiveness of redistribution rights, namely highly restrictive, restrictive, and unrestrictive. Fershtman and Gandal [6] also use the three levels of relative restrictiveness, i.e. very restrictive, moderately restrictive, and non-restrictive, in their empirical study. Finally, Sen et al. [18] classify OSS licenses along similar lines into three categories which they call strong-copyleft (most-restrictive), weak-copyleft (moderately restrictive), and non-copyleft (least-restrictive).

While the existing classi<sup>fi</sup>cations of OSS licenses capture the true essence of the most-restrictive and the least-restrictive OSS licenses, they do not accurately de<sup>fi</sup>ne the licenses that fall in between these two extremes. The model proposed in this study uses a more general classification. We assume that OSS licenses, represented by l, lie on a linear scale ranging from 0 to 1. On one extreme (i.e. l=0) we have the most-restrictive OSS licenses. These licenses ensure that once an OSS is licensed by a developer, the subsequent derivative software must be licensed similar to the original software. These licenses would correspond to the strong-copyleft licenses [18], highly restrictive licenses [10], and very restrictive licenses [6] de<sup>fi</sup>ned in earlier studies. An example from this category is the GNU General Public License (GPL). At the other extreme on our OSS license scale (i.e. l=1), OSS licenses place practically no restrictions on the license of the derivative software. The developers of derivative software are not obliged to inherit the license of the original software, as long as credit for the underlying code is given to relevant copyright holders. These licenses would correspond to the non-copyleft licenses [18], least-restrictive licenses [10], and non-restrictive licenses [6] de<sup>fi</sup>ned in earlier studies. An example in this category is Berkeley Software Distribution License (BSD license). Between these two extremes (i.e., 0blb1) lie OSS licenses that provide that once open source software is licensed by a developer, the subsequent derivative software can be released under a different license under certain conditions. An example in this category is GNU Lesser General Public License (LGPL). Lower value of l represents more restrictive OSS license and higher value of l represents less-restrictive OSS license.

When a new OSS development project is started, the project leader and/or core group of developers decide on the OSS license. They can choose any license, l (0≤l≤1). For the project owners/administrators/ leaders, the utility from this OSS development project is de<sup>fi</sup>ned as follows:

$$
U _ {0} = D (V _ {0} - | L - l |) - a\tag{1}
$$

where,

• D → The expected number of other software projects that would work on the cumulative enhancements of the original OSS or on derivative software. The minimum value of D is 1 since the OSS is always available in its original form.

$V _ { O } $ The intrinsic value derived from the original OSS by the core developers(s) working on the project. This value is realized even when no derivative work is developed for this OSS (i.e. D=1).

• L → Preferred license of the primary developer(s).

• l → The license choice that primary developer(s) have to make to maximize their utility.

• a → Total effort that goes into developing the original OSS.

The utility of primary developer(s) has been de<sup>fi</sup>ned such that it

• Decreases, depending on the actual license for the OSS. The closer this actual license choice is to the preferred OSS license (i.e. |L−l|), lower is this reduction. When the actual license is the same as the preferred license, the developer(s) of original OSS get the full intrinsic value from the project.

• Decreases with an increase in the total effort (i.e. a) required to develop the OSS.

• Increases, with increasing number of other projects that develop derivative works based on the original OSS.

## 3.2. Derivative work

The success of the original OSS lies in its cumulative improvement and integration in other software products. This is considered a success because of the bene<sup>fi</sup>ts that accompany such improvements and integrations. One such bene<sup>fi</sup>t is in the form of enhanced reputation among peers [9,14,18], and the resulting economic opportunities such as possibility of better employment [9,18]. As per OSS licenses, derivative software has to credit the original software developer(s). This would enhance the reputation and status of the original OSS project team among their peers.

The improvements in and integrations of original OSS are often carried out by developers in the form of separate projects and could result in derivative software that needs to be redistributed. Therefore, the success of original OSS depends on the number of new projects that use the OSS either to enhance/improve it signi<sup>fi</sup>cantly or as an integral component in their own software, i.e. derivative work. Before we model the impact of derivative works on OSS license choice, we need to de<sup>fi</sup>ne derivative work. Mere bundling of two software programs on the same distribution medium is not considered derivative work. For example, a CD-ROM consisting of an open source operating system (e.g. SUSE Linux) and an open source application (e.g. Open Of<sup>fi</sup>ce) is not considered a derivative work. All software that are part of this bundle are distributed under their original licenses. However, if two or more open source software are combined together so that they form single larger software, or if existing open source software is used as an integral component in another software product, then the resulting software would be considered a derivative work.

In our study, a derivative work is de<sup>fi</sup>ned as any software that includes one or more OSS as its components and a mechanism of communication (e.g. function calls) is used between these various components. For example, when the different components are in the same executable <sup>fi</sup>le, and/or are designed to run linked together in a shared address space, then these would be considered derivative works of the OSS that are used in the software. In such cases the license choice of the derivative software is constrained by the mostrestrictive license among the OSS components used to develop the derivative work. This means that the derivative software must be released under the license that is most-restrictive among the component software used to develop the derivative work.

The model in our study assumes that the number of projects working on derivative OSS would be in<sup>fl</sup>uenced by the license under which the original OSS is distributed. For example, if the original OSS is distributed under a restrictive license, it may attract new developers who prefer this sort of license, but it may turn away those that prefer the freedom to choose the license for their derivative work. In our model, we ignore those projects that use OSS tools/software (e.g. GNU Emacs text editor to write the program and the GNU Compiler to transform it into object code) to create their own software, but the new software does not include code from the OSS tools/software used. We also exclude those projects that result in a derivative work, but this work is used internally, i.e. used only by the core developers or a limited number of users af<sup>fi</sup>liated with the core developers. Since the derivative work is not distributed to the public, the license of the original OSS (on which the derivative work is based) is irrelevant for such developers. This leaves only those developers who modify an existing OSS, integrate an existing OSS into their own software, and/or combine two or more OSS to develop new software and then widely distribute this new derivative software.

The developers of derivative works are differentiated on the basis of their attitude towards freedom to choose the OSS license for their derivative works. We represent the importance of freedom (to choose one's own license) for these developers by f, where f is uniformly distributed between 0 and 1 (i.e.,0≤f≤1). For developers with f=0, this freedom is not at all important, while for developers with f=1 this freedom is a must. The utility function for these developers is as follows

$$
U _ {D} = V _ {D} + f [ l - a (1 - l) ] - b\tag{2}
$$

where

$V _ { D } $ The value of the derivative work for the developer(s) of this work;

• l → The license of original OSS on which the derivative work is based;

• a → Total effort that goes into developing the original OSS;

• b → Total effort that goes into developing the derivative work;

• f → Value of freedom for the developer(s) of derivative work to choose the license for the derivative work.

Developers with f=0 do not attach any value to the freedom to choose the license of their derivative work and therefore are not concerned about the license of the original OSS. If the original OSS is restrictive (i.e. l =0), they follow the same restrictive license and if the original license is not restrictive (i.e. l=1), these developers can choose any license. In this case the utility function is reduced to following

$$
U _ {D} = V _ {D} - b\tag{3}
$$

For developers with f=1, the freedom to be able choose the license for their derivative work is important and their the utility function is

$$
U _ {D} = V _ {D} + [ l - a (1 - l) ] - b \quad (\text { when } 0 <   1 <   1)\tag{4}
$$

$$
U _ {D} = V _ {D} - a - b \quad (\text { when } l = 0)\tag{4a}
$$

$$
U _ {D} = V _ {D} + 1 - b \quad (\text { when } l = 1).\tag{4b}
$$

As we can see from Eq. 4, utility for the developer(s) of derivative work is a function of the license of the original OSS. If the original OSS is highly restrictive (i.e. l = 0), then the developer(s) of derivative work are constrained in terms of the license that they can choose for the derivative, which reduces their valuation of the derivative work. Furthermore, since they want the freedom to choose their own license, they have to develop some part of or the complete original OSS themselves as the license of the original becomes more restrictive i.e. l moves towards the value 0 (see Eq. 4a). If the original license is non-restrictive (i.e. l=1), these developers use the original OSS and have the freedom to choose the license for their derivative work, which increases their utility. The utility functions for various values of l and f are summarized in Table 1.

Based on the generic utility function for the developer(s) of derivative software (Eq. 2), we can say that all the developers with $\frac { b - V _ { D } } { l ( 1 \mathrm { ~ + ~ } a ) - a } < f$ ≤1will develop a derivative using the original OSS. The number of such developers is

Table 1  
The utility functions for the developer(s) of derivative software.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Importance of freedom to choose the license of derivative work</td></tr><tr><td> $f=0$ </td><td> $0\( f=1$ </td><td> $f=1$ </td></tr><tr><td rowspan="3">License of the original OSS</td><td> $l=0$ </td><td> $V_D-b$ </td><td> $V_D-fa-b$ </td><td> $V_D-a-b$ </td></tr><tr><td> $0\( V_D-b$  $V_D+f[l-a(1-l)]-b$  $V_D+l-a(1-l)-b$ </td><td> $V_D-b$ </td><td> $V_D+f[l-a(1-l)]-b$ </td><td> $V_D+l-a(1-l)-b$ </td></tr><tr><td> $l=1$ </td><td> $V_D-b$ </td><td> $V_D+f-b$ </td><td> $V_D+1-b$ </td></tr></table>

$$
D = \frac {l (1 + a) + V _ {D} - a - b}{l (1 + a) - a}.\tag{5}
$$

Substituting the value of D from Eq. (5) in Eq. (1), we get the following two scenarios from the perspective of the developer of derivative OSS.

Scenario #1. When the preferred license of original OSS developer(s) is more restrictive than the license that the developer of derivative OSS must choose to maximize their utility $\left( \mathrm { i } . \mathrm { e } . \ l > L \right)$

$$
U _ {0} = D \left[ V _ {0} - (l - L) \right] - a = \left[ \frac {l (1 + a) + V _ {D} - a - b}{l (1 + a) - a} \right] \left[ V _ {0} - (l - L) \right] - a.\tag{6}
$$

Differentiating w.r.t. l and equating the derivative it to zero gives:

$$
l = \frac {a \pm \sqrt {[ L - a (1 - L) + (1 + a) V _ {0} ] (b - V _ {D})}}{(1 + a)}.\tag{7a}
$$

The utility $( i . e . , U _ { O } )$ from the original OSS is maximized at

$$
l = \frac {a + \sqrt {[ L - a (1 - L) + (1 + a) V _ {0} ] (b - V _ {D})}}{(1 + a)}.\tag{7b}
$$

Scenario #2. When the preferred license of original OSS developer(s) is less restrictive than the license that the developer of derivative OSS must choose to maximize their utility (i.e. l bL):

$$
U _ {o} = \left[ \frac {l (1 + a) + V _ {D} - a - b}{l (1 + a) - a} \right] [ V _ {o} - (L - l) ] - a.\tag{8}
$$

Differentiating w.r.t. l and equating the derivative to zero gives:

$$
l = \frac {a \pm \sqrt {[ L - a (1 - L) - (1 + a) V _ {0} ] (b - V _ {D})}}{(1 + a)}.\tag{9a}
$$

The utility (i.e. U ) from the original OSS is maximized at

$$
l = \frac {a - \sqrt {[ L - a (1 - L) - (1 + a) V _ {0} ] (b - V _ {D})}}{(1 + a)}.\tag{9b}
$$

## 4. Discussion

The optimal license choice for original OSS is summarized in Table 2.

Optimal license choice for original OSS

<table><tr><td>Relationship between l and L</td><td>Optimal value of l</td></tr><tr><td>l&gt;L</td><td>a+√[L-a(1-L)+(1+a)V0](b-VD) / (1+a) (Eq. 7b)</td></tr><tr><td>ll&gt;0.5</td><td>a-√[L-a(1-L)-(1+a)V0](b-VD) / (1+a) (Eq. 9b)</td></tr></table>

In our model, the optimal license choice for original OSS is a function of the preferred license of the original OSS's developer(s), the effort that goes into developing the original OSS and any derivative software base on this OSS, and the value to the other developers of the original OSS and any derivative OSS. In subsequent discussions we assume that the OSS being developed has high value for the developers working on the OSS project $( V _ { 1 } = V _ { 2 } = 1 )$ ). This assumption is based on the fact that most OSS developers work on a completely voluntary, non-contractual, noncommissioned basis and suggests that motivation plays a signi<sup>fi</sup>cant role in their behavior [3]. The key motivational factors identi<sup>fi</sup>ed in existing literature include the solving of information technology problems in dayto-day working [5,19], and reputation and recognition by peers [1,5,9,14]. In light of these motivational factors we can safely assume that the OSS being developed has a high intrinsic value for the developers. Therefore, we will focus our subsequent discussion on the impact of the developer effort on the optimal license for original OSS.

4.1. Impact of developer effort on optimal license choice for original OSS

4.1.1. For developers who prefer strong-copyleft license $( i . e . \ L = 0 )$

For these developers, l≥L. If we assume $V _ { 1 } = V _ { 2 } = 1$ , then Eq. (7b) gives the optimal license choice as $\begin{array} { r } { l = \frac { a + \sqrt { b - 1 } } { ( 1 + a ) } } \end{array}$ <sup>fi</sup>. The plot of this optimal license choice l against the effort required to develop the original OSS (i.e. a) and any derivative software (i.e. b) is shown in Fig. 1.

Analysis of Fig. 1 leads to the following propositions.

Proposition 1. Even when the preferred license of original OSS developer(s) is strong-copyleft, the optimal license restrictiveness for their original work should decrease with increasing effort that goes into developing the original OSS.

Proposition 1 implies that even when developer(s) of original OSS prefer highly restrictive license such as GPL, they would be better off by choosing a less-restrictive license if they anticipate spending a lot of effort in developing the original OSS. This could explain why despite GPL being the most preferred license of OSS developers, there are many OSS that are released under relatively less-restrictive licenses such as LGPL. Interestingly, Proposition 1 holds irrespective of the effort that goes into developing the derivative work. The derivative effort is not necessarily known to the developer(s) of the original OSS since the derivative work has yet to be started. In case the developers of original OSS have an estimate of the effort that might go into developing derivative software, we propose the following.

Proposition 2. The developer(s) of the original OSS should adopt lessrestrictive license for their OSS when they expect that a lot of effort is required to develop derivative works based on this original OSS.

One explanation for this proposition is that when developer(s) of derivative works are expected to invest a lot of time and effort in developing their derivative software, they are more likely to prefer to distribute this work under the license of their choice and therefore, would not want to be constrained by the license of the original OSS. Therefore, to encourage these developers to use the original OSS in their derivative work, the original OSS should be distributed under the leastrestrictive license, i.e. non-copyleft license. The corollary to this proposition is that developers who expect their original OSS to require minimal efforts for developing derivative OSS can use a license with stronger restrictions, such as strong-copyleft, to begin with.

4.1.2. For developers who prefer weak-copyleft license (assume $L = 0 . 5 )$ Case 1

In this case, we assume that $V _ { 1 } = V _ { 2 } = 1$ , and l NL (i.e., the optimal license is less restrictive than the preferred license). Then, Eq. (7b) gives the optimal license choice as $\begin{array} { r } { l = \frac { a + \sqrt { 0 . 5 ( 3 + a ) ( b - 1 ) } } { ( 1 + a ) } . } \end{array}$ . The plot of this optimal license choice l against the effort required to develop the original OSS (i.e. a) and any derivative software (i.e. b) is shown in Fig. 2.

![](/api/attachments/G3B3SH9H/fulltext/images/a7f052f10cd48961c3a818d3b47240c05dcbdd1cccee1e0b73790e884628b5cf.jpg)  
Fig. 1. Plot of l vs a and b for developers with L=0.

![](/api/attachments/G3B3SH9H/fulltext/images/4af5ec8026376204d3b0096711fd3cc4d56b13698d00838ca92ade911cb59d80.jpg)  
Fig. 2. Plot of l vs a and b for developers with L=0.5.

![](/api/attachments/G3B3SH9H/fulltext/images/8b759dfb1364207bbf74cf9ec6c41e105c331a3b79351e26d5138d36065190db.jpg)  
Fig. 3. Plot of l vs a and b for developers with L=0.5.

Analysis of Fig. 2 shows that the optimal license for original OSS essentially depends on the expected effort that would go into developing the derivative software using this OSS. We propose the following.

Proposition 3. Even when the preferred license of original OSS developers is weak-copyleft, the optimal license for their original work should be decreasing in restrictiveness with increasing effort that goes into developing the original OSS.

Proposition 4. Even when the preferred license of original OSS developers is weak-copyleft, the optimal license for their original work is one with even lower restrictions when a lot of effort is expected to develop derivative works based on this original OSS.

4.1.3. For developers who prefer weak-copyleft license (assume L = 0.5) Case 2

In this case, we assume that $V _ { 1 } = V _ { 2 } = 1$ , and l b L (i.e., the optimal license is more restrictive than the preferred license). Then Eq. (9b) gives the optimal license choice $\begin{array} { r } { \mathsf { a s } l = \frac { a - \sqrt { 0 . 5 ( 1 + 3 a ) ( 1 - b ) } } { ( 1 + a ) } } \end{array}$ . The plot of this optimal license choice l against the effort required to develop the original OSS (i.e. a) and any derivative software (i.e. b) is shown in Fig. 3. Analysis of Fig. 3 results in Propositions 5 and 6.

Proposition 5. Even when the preferred license of original OSS developers is weak-copyleft, the optimal license for their original work is always more restrictive irrespective of the effort that goes into developing the original OSS.

Proposition 6. Even when the preferred license of original OSS developers is weak-copyleft, the optimal license for their original work is strong-copyleft when a little effort goes into developing the original OSS and a little effort is expected to be required to develop derivative works based on this original OSS.

4.1.4. For developers who prefer non-copyleft license (assume L =1)

If we assume $V _ { 1 } = V _ { 2 } = 1$ , then Eq. (9b) gives the optimal license choice $\begin{array} { r } { \mathsf { a s } l = \frac { a - \sqrt { a ( 1 - b ) } } { ( 1 + a ) } . } \end{array}$ The plot of this optimal license choice l against the effort required to develop the original OSS (i.e. a) and any derivative software (i.e. b) is shown in Fig. 4. Analysis of Fig. 4 results in the following proposition.

Proposition 7. Even when the preferred license of original OSS developers is non-copyleft, the optimal license for their original work is always more restrictive irrespective of the effort that goes into developing the original OSS.

![](/api/attachments/G3B3SH9H/fulltext/images/5494087b1e1c4a1042cdf6b82410e5092b8a4b626c96d2c120daa7d4a298ad91.jpg)  
Fig. 4. Plot of l vs a and b for developers with L=0.5.

Impact of development effort on optimal license choice.

<table><tr><td colspan="4">Optimal license choice (l) when the preferred license of original OSS developer(s) is strong-copyleft (i.e. L=0)</td></tr><tr><td></td><td></td><td>Effort to develop original OSS (i.e. a)</td><td></td></tr><tr><td></td><td></td><td>Low</td><td>High</td></tr><tr><td rowspan="2">Expected effort to develop derivative work (i.e. b)</td><td>Low</td><td>Strong-copyleft</td><td>Weak-copyleft</td></tr><tr><td>High</td><td>Non-copyleft</td><td>Non-copyleft</td></tr><tr><td colspan="4">Optimal license choice (l) when the preferred license of original OSS developer(s) is weak-copyleft (i.e. L=0.5) and L</td></tr><tr><td></td><td></td><td>Effort to develop original OSS (a)</td><td></td></tr><tr><td></td><td></td><td>Low</td><td>High</td></tr><tr><td rowspan="2">Expected effort to develop derivative (b)</td><td>Low</td><td>Weak-copyleft</td><td>Weak-copyleft</td></tr><tr><td>High</td><td>Non-copyleft</td><td>Non-copyleft</td></tr><tr><td colspan="4">Optimal license choice (l) when the preferred license of original OSS developer(s) is weak-copyleft (i.e. L=0.5) and L&gt;1</td></tr><tr><td></td><td></td><td>Effort to develop original OSS (a)</td><td></td></tr><tr><td></td><td></td><td>Low</td><td>High</td></tr><tr><td rowspan="2">Expected effort to develop derivative (b)</td><td>Low</td><td>Strong-copyleft</td><td>Weak-copyleft</td></tr><tr><td>High</td><td>Weak-copyleft</td><td>Weak-copyleft</td></tr><tr><td colspan="4">Optimal license choice (l) when the preferred license of original OSS developer(s) is non-copyleft (i.e. L=1)</td></tr><tr><td></td><td></td><td>Effort to develop original OSS (a)</td><td></td></tr><tr><td></td><td></td><td>Low</td><td>High</td></tr><tr><td rowspan="2">Expected effort to develop derivative (b)</td><td>Low</td><td>Strong-copyleft</td><td>Weak-copyleft</td></tr><tr><td>High</td><td>Weak-copyleft</td><td>Weak-copyleft</td></tr></table>

Proposition 8. Even when the preferred license of original OSS developers is non-copyleft, the optimal license for their original work is one with stronger restrictions when little effort goes into developing the original OSS and a little effort is expected to be required to develop derivative works based on this original OSS.  
where

Propositions 1 to 8 are summarized in Table 3.

## 4.2. Empirical validation

A common theme among the results obtained from the analytical model is that less-restrictive license weakly dominates the more restrictive ones when higher effort goes into developing the original OSS. Therefore, we propose to test empirically the following hypothesis about the open source licenses of projects on Sourceforge.net.

Hypothesis. Irrespective of the preferred license and the effort that might go into developing derivative software, the optimal license for the original license becomes less restrictive as more effort goes into developing this software.

To test our hypothesis, the dependent variable, i.e. the original OSS license (i.e. LICENSE), is de<sup>fi</sup>ned as an ordered discrete variable with three values: 1 for the most-restrictive licenses, 2 for the semirestrictive licenses, and 3 for the least-restrictive licenses. We use the generalized ordered logit regression or GOLOGIT [7] model to represent the relationship between the determinants and the preferred disclosure timing of vulnerability researchers. A key advantage of GOLOGIT model over ordered logit model is that it is not constrained by the parallel lines assumption, i.e. the coef<sup>fi</sup>cients in a GOLOGIT regression model can differ across categories of the dependent variable [26]. The GOLOGIT model used in this study can be written as follows [26]:

$$
P \left(Y _ {i} > j\right) = g \left(\beta_ {j} X _ {i r}\right) = \frac {\exp \left(\alpha_ {j} + \beta_ {j} X _ {i r}\right)}{1 + \left[ \exp \left(\alpha_ {j} + \beta_ {j} X _ {i r}\right) \right]}, j = 1, 2, \dots , M - 1.\tag{1}
$$

From the above, it can be determined that the probabilities that Y will take on each of the values $1 , \ldots ,$ M is equal to:

$$
P (Y _ {i} = 1) = 1 - g \Big (B _ {j} X _ {i} \Big)\tag{1a}
$$

$$
P (Y _ {i} = j) = g \left(B _ {j - 1} X _ {i}\right) - g \left(B _ {j} X _ {i}\right), j = 2, \dots , M - 1\tag{1b}
$$

$$
P (Y _ {i} = M) = g (B _ {M - 1} X _ {i})\tag{1c}
$$

• M (=3) is the number of categories of the ordinal dependent variable (i.e. LICENSE).

• $Y _ { i }$ is a random variable such that $Y _ { i } = 1$ when LICENSE=1; Y =2 when the $L I C E N S E { = } ; Y _ { i } { = } 3$ when $L I C E N S E = 3 ;$ and

• X is the vector of covariates; and $B _ { j }$ denotes the associated vector of coef<sup>fi</sup>cients for category j.

The independent variable used in this model should provide us with a measure of the effort that goes into developing the OSS. We use the average number of developers working on an OSS project as a surrogate measure for the effort that goes into developing the OSS (i.e., higher the number of developers, more the effort spent in developing the software and vice versa).

To test the hypothesis we use data on open source software from Sourceforge.net repository. Sourceforge.net is a free service that maintains the largest database of software applications, which are preferably released under an open source license. For each project, the database provides a description of the software, links to download it and to obtain more information, and a history of the project's releases. We accessed data directly from a data warehouse, which is populated with Sourceforge.net data on a regular basis and maintained at the University of Notre Dame by Dr. Greg Madey.<sup>2</sup> The Sourceforge.net database contains information on more than 200,000 software projects. For the purpose of this study we considered only those projects for which complete information was available, and which had been registered between January 1999 and December 2005. The number of such projects was 10,094. Approximately 66% of these were licensed as strong-copyleft, about 16% as weak-copyleft and the rest as non-copyleft.

The coef<sup>fi</sup>cient estimate for the average number of developers working on the project in any month (β=.0157746) was signi<sup>fi</sup>cant at p=0.000, which provides support for our hypothesis. This means, that for our dataset, an addition of one more developer to the OSS project increased the likelihood by approximately 2% that the license choice of the original OSS will be less restrictive.

## 5. Conclusion

Existing literature has shown that OSS licenses play an important role in the success or failure of OSS projects. However, studies of the actual license choice among OSS developers have been rare and our study provides important insights to researchers and practitioners about the impact of this choice under utility maximizing scenarios. This study contributes to our understanding of OSS license choice in several ways.

$b$ Total effort that goes into development of derivative software

$a$ Total effort that goes into development of the original OSS $f$ Importance to developers of derivative software of the freedom to choose OSS license of their choice (0≤f≤1; f=0 represents freedom is not at all important and f=1 represents that complete freedom is a must)

First, unlike the existing studies on the subject which have focused on the impact of OSS project speci<sup>fi</sup>c attributes, and the motivational factors of OSS developers on OSS license, this study addresses the issue from the perspective of rational choice of developers. Second, our study provides analytical and empirical evidence that a whole range of OSS licenses will continue to coexist and compete with each other. Our results suggest that least-restrictive or non-copyleft license will dominate other types of OSS license when a large effort is required to develop derivative software. On the other hand, most-restrictive or strong-copyleft licenses will be the dominant license when minimal effort is required to develop the original OSS and the derivative software. Under most conditions, semi-restrictive or weak-copyleft licenses will end up dominating the two extreme options, i.e. most-restrictive and non-restrictive license (Table 3). This result is counter-intuitive to the current wisdom which says that either the most-restrictive (strong-copyleft licenses) [25] or least-restrictive (non-copyleft) licenses will eventually dominate the OSS landscape [13]. The current wisdom could be a result of either a misunderstanding of the alternative license choices [10], or considerations outside of the utility maximizing paradigms. For instance, suf<sup>fi</sup>cient external motivation, such as large royalties, network effects, or developer value-added, could make the least-restrictive license as a dominant choice for the developer [13]. An important managerial implication of our study is that, if OSS developers make a rational choice under utility maximizing conditions, the optimal licenses that bene<sup>fi</sup>t their OSS projects may not always match their preferred licenses. Hence, the sub-optimal license choices could be adversely affecting the success of their open source projects and project managers should more carefully evaluate future efforts required for their project as well as those of derivative projects before making the license choice.

There are some minor limitations of our model. The impact of the number of derivative projects on original developer's utility is assumed to be constant, even though a non-linear functional assumption will not change our results but would have made our model very complex and intractable. Our model focuses on individuals developing open source software voluntarily, but our results should hold for organizations developing or sponsoring open source software as long as their motivation is based on a wider adoption of their software in derivative works (e.g., Google's strategy for Android). Future research can survey OSS project managers to empirically evaluate the gap between the manager's preferred license and the project's actual license and study their relationships to factors outside of the rational decision-making paradigm. In addition, such empirical data can be combined with data from repositories, such as Sourceforge.net, to understand the impact of this gap in license choice on the actual success of the open source project.

## Appendix A. Table of key notations

l OSS license (0≤l≤1; l=0 represents maximum restrictions and l=1 represents no restrictions on the derivative software)

$L$ Preferred license of the original project developers/owners/leaders

$$
U _ {o}
$$

$U _ { D }$ Utility for developers of derivative software

$D$ Number of other software projects expected to work on enhancing the original OSS project or on derivative software

$V _ { o }$ Intrinsic value derived by core developers from the original OSS project

$V _ { D }$ Value of the derivative work for developers working on derivative software

## References

[1] A. Bonaccorsi, C. Rossi, Why open source software can succeed? Research Policy 32 (7) (2003) 243.

[2] G. Cheliotis, From open source to open content: organization, licensing and decision processes in open cultural production, Decision Support Systems 47 (3) (2009) 229–244.

[3] E.G. Clary, R.D. Ridge, A.A. Stukas, M. Snyder, J. Copeland, J. Haugen, P. Miene, Understanding and assessing the motivation of volunteers: a functional approach, Journal of Personality and Soc. Psych. 74 (6) (1998) 1516–1530.

[4] P.M. Di Gangi, M. Wasko, Steal my idea! Organizational adoption of user innovations from a user innovation community: a case study of Dell IdeaStorm Decision Support Systems 48 (1) (2009) 303–312.

[5] J. Feller, B. Fitzgerald, Understanding Open Source Software Development, Addison–Wesley, Boston, 2002.

[6] C. Fershtman, N. Gandal, Open source software: motivation and restrictive licensing, International Economics and Economic Policy 4 (2) (August 2007) 209–225.

[7] V.K. Fu, Estimating generalized ordered logit models, Stata Technical Bulletin 8 (1998) 160–164.

[8] K.L. Gwebu, J. Wang, Adoption of open source software: the role of social identi<sup>fi</sup>cation, Decision Support Systems 51 (1) (2011) 220–229.

[9] J. Lerner, J. Tirole, Some simple economics of open source, The Journal of Industria Economics 50 (2) (2002) 197–234.

[10] J. Lerner, J. Tirole, The scope of open source licensing, Journal of Law, Economics and Organization 21 (1) (April 2005) 20–56.

[11] B. Martin, Information Liberation, Available at, Freedom Press, London, 1998, pp. 29–56 www.uow.edu.au/arts/sts/bmartin/pubs/98il/il03.html, Last accessed 12/20/09.

[12] V.G. Morwitz, Methods for forecasting from intentions data, in: J.S. Armstrong (Ed.), Principles of Forecasting, Kluwer Academic Publishers, Norwell, MA, 2001, pp. 33–56.

[13] G. Parker, M. Van Alstyne, Innovation through optimal licensing in free markets and free software Available at, September 2005 http://ssrn.com/abstract=639165 Last accessed 12/20/09.

[14] E.S. Raymond, The Cathedral and Bazaar, O'Reilly, Sebastopol, CA, 1999.

[15] J.A. Roberts, I. Hann, S.A. Slaughter, Understanding the motivations, participation, and performance of open source software developers: a longitudinal study of the Apache projects, Management Science 52 (7) (2006) 984–999.

[16] L. Rosen, Open Source Licensing: Software Freedom and Intellectual Property Law, Prentice Hall, Upper-Saddle River, NJ, 2005.

[17] R. Sen, A strategic analysis of competition between open source and proprietary software applications, Journal of Management Information Systems 24 (1) (Summer 2007) 233–258.

[18] R. Sen, C. Subramaniam, M. Nelson, Determinants of open source software license choice, Journal of Management Information Systems 25 (3) (Winter 2008–2009) 207–240.

[19] S. Shah, Motivation, governance, and the viability of hybrid forms in open source software development, Management Science 52 (7) (July 2006) 1000–1014.

[20] B.H. Sheppard, J. Hartwick, P.R. Warshaw, The theory of reasoned action: a metaanalysis of past research with recommendations for modi<sup>fi</sup>cations and future research, Journal of Consumer Research 15 (1988) 325–343.

[21] R.M. Stallman, The GNU operating system and the free software movement, Available at, Open Sources: Voices from the Open Source Revolution, O'Reilly Media, Sebastopol, CA, 1999 http://www.oreilly.com/catalog/opensources/book stallman.html, Last accessed 12/20/09.

[22] K.J. Stewart, A.P. Ammeter, L.M. Maruping, Impact of license choice and organizational sponsorship on success in open source software development projects, Information System Research 17 (2) (2006) 136–144.

[23] C. Subramaniam, R. Sen, M. Nelson, Open source software: determinants of OSS project success: a longitudinal study, Decision Support Systems 46 (2) (2009) 576–585.

[24] R. Subramanyam, M. Xia, Free/Libre open source software development in developing and developed countries: a conceptual framework with an exploratory study, Decision Support Systems 46 (1) (2008) 173–186.

[25] D. Wheeler, Your Open Source Software GPL-Compatible. Or Else Available at, http://www.dwheeler.com/essays/gpl-compatible.html 2009 Last Accessed on 12/30/2009).

[26] R. Williams, Generalized ordered logit/partial proportional odds models for ordinal dependent variables, The Stata Journal 6 (1) (2006) 58–82.

[27] M.A. Zaffar, R.L. Kumar, K. Zhao, Diffusion dynamics of open source software: an agent-based computational economics approach, Decision Support Systems 51 (3) (2011) 597–608.

Dr. RAVI SEN is an Associate Professor in the Department of Information and Operations Management at the Mays Business School, Texas A&M University. He received his Ph.D. in 2003 from the University of Illinois at Urbana–Champaign. His research interests include economics of electronic commerce, open source software, and software security. He has published in Journal of management information Systems, Decision Support Systems, International Journal of Electronic Commerce, Communications of the AIS Electronic Markets and Journal of Electronic Commerce Research

Dr. CHANDRASEKAR SUBRAMANIAM is an Associate Professor in the Department of Business Information Systems and Operations Management at the Belk College of Business, University of North Carolina at Charlotte. He received his PhD from the University of Illinois at Urbana–Champaign. His research interests include electronic commerce and e-business, value of information technology, interorganizational systems, open source software, and IT security. He has published in Journal of management information Systems, Decision Support Systems, International Journal of Electronic Commerce, Communications of the AIS, and Information Systems Frontiers.

Dr. MATTHEW L. NELSON is an Associate Professor in the Department of Accounting and Business Information Systems at Illinois State University. He received his Ph.D. in 2003 from the University of Illinois at Urbana–Champaign. His research interests include information technology valuation, open source software, and information technology standards. He has published in Journal of Management Information Systems, Decision Support Systems, Information and Management, Communications of the AIS Electronic Markets, and Mathematical and Computer Modeling
