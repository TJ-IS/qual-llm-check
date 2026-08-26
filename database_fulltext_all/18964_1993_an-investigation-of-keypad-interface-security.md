---
otero_id: 18964
otero_key: "NX4FZJA6"
title: "An investigation of keypad interface security"
authors: "Dennis A. Adams; Stanley Y. Chang"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90054-w"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# An investigation of keypad interface security

Dennis A. Adams

University of Houston, Houston, TX, USA

Stanley Y. Chang

Arizona State University-West, Phoenix, AZ, USA

Keypad interfaces are popular input devices for a wide variety of systems. Automatic teller machines (ATMs), point-of-sale (POS) and process control systems are just some of the applications to which these interfaces have been put. However, these systems are protected with security procedures that are substantially less sophisticated than their data processing counterparts. A theory of the search of associative memory is used to anticipate what subjects will choose for passwords or personal identification numbers (PIN). A laboratory experiment to understand how users create passwords for system access indicates that they create words or phrases when prompted for passwords and number patterns when asked for PINs. Also, when users are given visual prompting of a numeric keypad, they create longer passwords or PINs than when there is no prompt. This indicates that security can be improved by asking users to create passwords and providing users with a keypad.

Keywords: Computer security; Passwords; Personal identification numbers; Keypad; Automatic teller machine; Point of sale

![](/api/attachments/NX4FZJA6/fulltext/images/0326259130de1e2b6701a439115ab71bb78afa991673303d83e3128f86c8e8ab.jpg)  
Stanley Y. Chang, CPA, CMA, CIA is an assistant professor of Accountancy at Arizona State University West. His research interests include internal/organizational control, operational audit, and behavioral aspects of auditing.  
Correspondence to: Dennis A. Adams, Department of Decision & Information Sciences, College of Business Administration, University of Houston, 4800 Calhoun, Houston, TX 77204-6282, USA.

## Introduction

Computer security technologies have had a difficult time keeping pace with the advances in computing. The growing emphasis on “user friendliness” has, to some extent, adversely affected the deployment of some control mechanisms. Specifically, the easy access feature of many systems often leads to compromises in security design and causes problems for systems controllers and auditors.

Various devices and approaches have been developed and used to provide access control to electronic data processing systems. However, while many alternatives are available, password controls are often their first line of defense. Under most circumstances, including some very sophisticated system environments, password controls may be the only security barrier $[14]$ .

Many algorithms and control mechanisms have been provided to reinforce the defensibility of passwords (e.g., [1,7]). However, the tremendous growth of automatic teller machines (ATMs) and point-of-sale (POS) systems which incorporate keypad rather than keyboard data entry has severely restricted the application of password controls. For the convenience of the average user, many bank accounts are guarded only by a four or five digit Personal Identification Number (PIN).

![](/api/attachments/NX4FZJA6/fulltext/images/6e72fcd489f0918ca81040c6a7602f6f2200273cfc38a5c7512c7ea1d11d525d.jpg)  
sectors.  
Dennis A. Adams is an assistant professor of Management Information Systems in the College of Business Administration at the University of Houston. His research interests include the uses of information technology for competitive advantage, management of telecommunication technologies, and the analysis and design of parallel systems. He has designed and implemented business, scientific and system software on a wide range of hardware in the public and private

In order to assess the risk or costs of such a compromise, one must have knowledge of how PINs and passwords are created. Previous studies (e.g., [2]) investigated the predictability and common structure of passwords but did not provide a discussion of a foundational theory to interpret the phenomena of password selection. Further, no studies were found that addressed the use of PINs and keypad entry devices as an alternative to passwords created on a keyboard. Based on a theory of working memory, this paper reports the results of an experiment with a keypad exploring possible creation patterns of passwords and PINs.

## Background

Password protection of computer resources has been a concern for security analysts for some time $[4,6]$ . Tales of computer crimes perpetrated with purloined user identifications and passwords are rife in the computing community $[5]$ . However, this concern is not unfounded. Studies have shown that computer passwords can be very easily predicted and defeated $[11,16]$ . When unconstrained, users are likely to create very short passwords consisting almost exclusively of lower case letters. As would be expected, because of this small length, the frequency of vowels is very high in proportion to consonants. In addition, the passwords are frequently proper names and easily remembered nouns. Word lists taken from dictionaries, telephone books, and building directories often contain over 80% of the passwords resident in a given system. An analysis of human memory systems gives some insight into password construction.

Cognitive psychologists have spent more than one hundred years studying human memory. Theorists and experimental researchers have strived to find answers to various questions about how the human mind receives, retains, and retrieves information. It is hypothesized that memory processes serve as the glue that holds together all higher forms of cognition – attention, perception, language, and reasoning $[3,9]$ .

Current memory models divide memory into three types: sensory, short-term (STM) and long-term (LTM). Sensory memory is limited in duration (its longest persistence is only a few seconds) and is usually more important to sensing than learning. STM and LTM, on the other hand, have been the focal points of cognitive science.

While virtually all human knowledge is stored in LTM, it must be accessed through STM, which consists of perceptions and associations at a given time. Conventional models presume STM to be transient in nature. Further, early research has found STM to be limited in capacity and to last only a short period of about 18 seconds [12]. A frequent assumption in cognitive psychology is that STM's limited capacity restricts decision making and planning [10].

Some recent experiments, however, suggest STM to be more dynamic than just a passive storehouse for data. Researchers have proposed a new concept of working memory which implies that STM is the mind's central processor. While the definition and dimension of information processing is changing, it is generally agreed that items must be stored in LTM to be remembered. A theory of the search of associative memory (SAM) predicts memory recall based on an associative network [13]. Some important guiding principles of the theory propose that long term memory is a highly interconnected, multi-topological network with multiple levels, and that retrieval of memory is dependent on cues and is a noisy, hence probabilistic process. Finally, the basic unit of storage is temporal-contextual information.

This theory can be used to explain why computer system users prefer security passwords that relate to various aspects of their lives. For example, a triathlete might have a password of 3SPORT; a new parent may have, as a password, the first name of their child; a fan of Tolkien's Lord of the Rings might choose FRODO. In all these examples, the password is chosen to associate system use with another important, easily associated area of their lives. Passwords that are associated with information that frequently resides in STM will be more easily recalled than that stored in LTM. An exception to this would occur when the password is regularly employed and hence is more likely to be a long term memory association. This also explains why passwords that fall into disuse are more difficult to recall because their association within or through STM decays and become noisier.

SAM theory makes no explicit statements about what is actually stored in memory, but specifies that associations are critical components to the subsequent recall of the information. Consequently, other than the temporal and contextual nature of the information and the relationships, the theory makes no distinction between the storage of words, numbers, smells, etc.

To a computer auditor, SAM theory bodes ill, because it predicts that users, who infrequently access computer accounts will create passwords that reflect the frequent content of the user's STM and frequent users of accounts will choose passwords based upon LTM with STM cues. The use of keypad interfaces in security systems is a further complication. The common keypad interface resembles a telephone keypad. Because SAM makes no assertions about the content of memory, using the numbers on a keypad to interact with a security system requires the user to associate numerals with other items that are frequently in STM. The potential number of numeric items found in STM is probably less than their textual counterpart. Consequently, security systems that employ keypad systems may be more vulnerable than those that use keyboards. It is the purpose of this exploratory study to gain an understanding of how users create passwords and PINs using keypad interface systems.

## The keypad experiment

One hundred and thirteen junior and senior information system and accounting majors were asked to create an access code for a hypothetical voice messaging system. Although many of the students had some experience with a keypad system and its functions, the entire group of participants were briefed on its use and were instructed to create a password or a PIN to allow themselves to have frequent access into their hypothetical accounts. The voice messaging system was selected, because the subjects frequently come into contact with it at school, although few actually have voice mailboxes. A substantial number of the subjects (72%) frequently used ATMs and all had used an ATM at least once.

Using a factorial design, the subjects were randomly divided into nearly equal groups that were told to create a password or a personal identification number. The subjects could answer using numbers or the letters customarily present on a keypad.

![](/api/attachments/NX4FZJA6/fulltext/images/368426aad3db549a270fcf6372f750d82b9abc0e7e8d2639dd679d23bda74d00.jpg)  
Fig. 1. Keypad replica.

Approximately half of the subjects are given replicas of the standard Touchtone $^{©}$ (Dual Tone, Multiple Frequency – DTMF) keypad shown in Figure 1, while the other half were given no visual support at all. The Touchtone $^{©}$ telephone keypad has most of the letters of the alphabet associated with a number. Although not present on the standard telephone keypad, the letters Q and Z were assigned to the numeral zero. The absence or presence of the keypad prompt was used in an effort to ascertain the effects of a visual stimulus on short term memory retrieval. Because SAM theory suggests that memory search and associations are cued by external stimuli, it is believed that the prompt would affect the password/PIN selected.

Two research questions were posed to determine how users create passwords/PINs on standard keypads. In both cases, the overall question was: does a visual cue change the outcome? The first part asks whether there is a difference between the way users create passwords and the way they create PINs. If no difference is found, the SAM theory would appear to be correct: the passwords/PINs are similarly selected and are simply associated with short or long term memory. For this test, the length of the passwords/PINs was compared. The null hypothesis is

$H_{1}0$ : There is no difference between the length of passwords and the length of PINs.

In a similar fashion, the research question also addresses the use of the keypad prompt as a stimulus for password/PIN creation. If no difference is found with and without visual prompts, it suggests that different search patterns are not incorporated when subjects are presented with different stimuli. It might be expected that shorter passwords/PINs would be created when the keypad is present than when it is not, because the physical manipulation of the keypad would constrain the search task. However, SAM theory does not directly suggest this. Consequently, the two-tailed associated null hypothesis would be

$H_{2}0$ : There is no difference between the lengths of passwords/PINs with a keypad prompt and those without a prompt.

The second research question asks how the passwords/PINs are created. Given that all subjects were instructed to visualize or use a standard keypad for data entry, it is assumed that there would be no measurable difference between the passwords and the PINs. Because SAM does not specify the contents of memory but only the fact that memories are associated and hierarchically structured, we assume that there should be no difference in the way users create passwords/PINs. However, it is expected that if users are told to create passwords they will create text and if they are told to create personal identification numbers, they will create numbers. Consequently, the type of password/PIN created (text or numeric) is the dependent variable. The null hypothesis for this test is

$H_{3}0$ : There is no difference between the type of input for passwords and that of PINs.

This can also be addressed by determining whether the presence of the keypad prompt affects the type of password/PIN created. Because both numbers and letters are present on the prompt, we expect that there will be no difference. The null hypothesis for this test is

$H_{4}0$ : There is no difference between the type of passwords/PINs created with a keypad prompt and those without a prompt.

## Research findings

Tables 1 and 2 show the results of statistical analysis performed on length of passwords/PINs and type of input. Subjects were asked to create either passwords or PINs, but were not told how to create them. The average length of a password was 5.0 characters ( $\sigma = 1.71$ ), while the average length of a PIN was 4.75 characters ( $\sigma = 1.75$ ). These small differences perhaps reflect the current limitations imposed by most ATMs of four or five character PINs and has probably caused a bias because relatively longer passwords are routinely incorporated into computer systems. (The general rule of passwords was six or more alphanumeric characters [17].)

The results suggest that we reject $H_{2}0$ : the length of the password/PIN is related to the absence or presence of the keypad prompt. The length of the passwords/PINs when the users are presented with no keypad is longer (5.26) than if they were given a prompt (4.5). This could be explained by the confusion of finding the proper letter might encourage users to design shorter passwords when faced with creating a password on a keypad. As previously discussed, no significant difference was found in the length of PINs versus the length of the passwords indicating that we cannot reject $H_{1}0$ .

ANOVA of password/pin length

<table><tr><td>Source</td><td>DF</td><td>Sum of Squares</td><td>Mean square</td><td>F</td><td>Prof &gt; F</td></tr><tr><td>Password/pin</td><td>1</td><td>1.78</td><td>1.78</td><td>0.61</td><td>0.4346</td></tr><tr><td>Keypad presence</td><td>1</td><td>13.05</td><td>13.05</td><td>4.51</td><td>0.0360</td></tr><tr><td>Error</td><td>111</td><td>321.45</td><td>2.90</td><td></td><td></td></tr><tr><td>Total</td><td>113</td><td>332.28</td><td></td><td></td><td></td></tr></table>

Table 2
ANOVA of password/pin input type

<table><tr><td>Source</td><td>DF</td><td>Sum of squares</td><td>Mean square</td><td>F</td><td>Prof &gt; F</td></tr><tr><td>Password/pin</td><td>1</td><td>7.55</td><td>7.55</td><td>47.14</td><td>0.0001</td></tr><tr><td>Keypad presence</td><td>1</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.8754</td></tr><tr><td>Error</td><td>111</td><td>17.78</td><td>0.16</td><td></td><td></td></tr><tr><td>Total</td><td>113</td><td>25.34</td><td></td><td></td><td></td></tr></table>

Another analysis indicates that users create words or identifiable numbers when asked for passwords and number patterns when asked for PINs. The results of an analysis of variance (ANOVA) shows that the subjects created words when instructed to make passwords and numbers when asked for PINs. When asked to create a password, almost 87% of the subjects created words that contained only the twenty-six letters of the alphabet. Consequently, we reject $H_{3}0$ . Many of these passwords contained the subject's first name or the name of an acquaintance. Almost 93% of those who were instructed to create a PIN, used only numerals creating PINs representing a social security number, a date or a phone number. As with passwords, this indicates that the chances of gaining access to the resources protected by a PIN increases with the knowledge level of the user's personal life, just as it does with passwords. The presence of the keypad did not affect the type of input and we cannot reject $H_{4}0$ .

Most common keystroke pairs. $^{a}$

<table><tr><td>Keystroke</td><td>% Found</td><td>Keystroke</td><td>% Found</td></tr><tr><td>1 to 2</td><td>2.5%</td><td>5 to 3</td><td>2.5%</td></tr><tr><td>2 to 2</td><td>4.3%</td><td>6 to 2</td><td>2.5%</td></tr><tr><td>2 to 7</td><td>2.7%</td><td>6 to 6</td><td>2.7%</td></tr><tr><td>4 to 6</td><td>2.3%</td><td>7 to 7</td><td>2.5%</td></tr><tr><td>Total 22.0%</td><td></td><td colspan="2">(8 pairs/100 possible)</td></tr></table>

$^{a}$ 8 % of the possible keystrokes pairs account for 22% of those used. One hundred combinations are possible because there are one hundred two-digit patterns using the numerals zero through nine (00 through 99).

The study also investigated the keystroke patterns used (Table 3). A keystroke pattern is the movement from one push button to another. For example, pressing a two followed by a seven would be a two-to-seven keystroke. Results show that over 1/5 of the keystroke patterns used needed only eight of the one hundred possible keystroke patterns. However, a nonparametric chi-squared test employed to test whether there was a difference between keystroke patterns for passwords versus PINs found no significant difference ( $\chi^{2}=111.713$ , d.f.=94, prob=0.103). Similar results were found for the test of whether the keypad prompt affected the keystroke patterns ( $\chi^{2}=90.187$ , d.f.=94, prob=0.592).

In posttest interviews, subjects reported using familiar names of relatives, acquaintances, and pets as passwords. Length was often cited as reason for password selection when multiple potential passwords were possible. Phone numbers, social security numbers and house addresses were the most frequently reported genesis for PINs. A few indicated they wished to use PINs that were easily patterned on the keypad (e.g., 111, 2486, 1793).

## Discussion

Implications for SAM theory. SAM theory predicts that users of keyboard and keypad interface security systems will employ passwords or PINs that are frequently associated with information that is often found in STM. Even though the keypad (present or described) contained both numbers and letters, when users were asked to create text (passwords), they formed words; when asked to use numerals (PINs), they complied. This would indicate: (1) that the search of associative memory is affected by the type of information for which we are searching, (2) that the users are taking the “cue” they are given in the instructions, or (3) the class of information (numeric or text) is another association that we maintain.

The interaction between associative memory and short term memory also seems to be supported. There is no requirement for subjects to associate the password/PIN with personal information (names, social security numbers, phone numbers, etc.). However, because these items are frequently moved from LTM to STM, their retrieval is more natural and is associated with the use of the keypad interface.

Implications for system security. Because the passwords were slightly longer than the PINs and because there are more characters from which to choose, the chances of “breaking” a password should be less than those of breaking a PIN. In addition, by asking the user to visualize a keypad replica (rather than provide one to use) before they create the password/PIN, the resulting pattern will be longer than that created by an aided subject. More importantly, because the types of words used to create passwords are more varied than the numbers associated with PINs, it would seem to be more difficult to break a password. Unfortunately, the choice of a password comes from a fairly standard set of potential passwords (names, activities, etc.). The result is that even though the numbers are less robust, they may present a better security device at least for untrained/uninformed users.

Security suggestions for keypad interface systems. Based on the discussion and results, the following procedures are suggested for improvement of the security of keypad systems. These suggestions include passive approaches, such as control promotion and policy establishment, and active tactics, such as constant monitoring and random investigation of the systems to deter inadequate or illegal use.

(1) Penetration and exposure analysis. Random or comprehensive analysis of individual user accounts attempting to determine use of a system default password or other overly obvious one (such as the telephone extension or mail code) should be performed. Individuals who do not follow established password guidelines should be notified or their proposed password rejected. Follow-up procedures should always be performed. Repeat violations or continued noncompliance would entail informing the appropriate higher level management. Unfortunately, when system use is voluntary, such procedures could discourage people from using the system. However, positive management leadership and careful administration should prevent this, and such procedures would only further enhance the results of education. It should be noted that the access attempts and follow-ups may cause conflicts and privacy violation concerns. Such analyses also may not be suitable for ATM or POS systems. in addition, the frequent use of experienced professionals, with methods similar to those of a hacker, to perform penetration analysis to test the controls and overall vulnerability of the system may be warranted [8].

(2) Security promotion. Education programs should be developed and implemented with strong management support to promote the seriousness of security controls and the proper ways to use and benefit from a system. It is beneficial to have an established guideline for choosing passwords – such as the federal Password Management Guideline [15] which defines acceptable password practices for sensitive information. For systems with a large number of unsophisticated users (such as ATMs), the users should be made aware of the vulnerability of simply structured passwords/PINs and the implications of password/PIN selection.

(3) Access failure reports. “Trial and error” is the most common way to attempt illegal system access. Thus, a log or journal should be established and reviewed daily by system managers or appropriate personnel (e.g., internal auditors) with summaries periodically distributed to all management. Denied access, especially when occurring consecutively during a short period of time, should always be flagged and investigated.

(4) Personnel record control and administration. The knowledge of personal information may provide easy access to the system. Thus, personnel records should be appropriately controlled. Further, more stringent administrative policies may need to be designed for the personnel department, as its employees may have relatively unrestricted access to individual records. Operationally, personnel department supervisors need to be aware of the possibility that their subordinates could utilize information available in their daily work for illegal gains.

(5) Password expiration. Many data processing systems have password protection schemes that force users to change passwords at predetermined times. This expiration date procedure insures that the passwords are not in use for a long period of time. The system keeps track of the last password change and all previous passwords. Upon password expiration, the system forces the user to create a new password that must be different from recently created ones. This type of scheme is often unfavorably considered by users who have to create the new passwords.

(6) Supplementary verification procedures. Double password setting (where one password could be assigned and changed periodically by administrators and the other created by the user) could be another method of control. Requiring additional items to gain access to a system such as a card or a key, also provides further protection, although there is no definite assurance of the identity of the interacting person. In more sophisticated environments, current technology enables the implementation of more biologically oriented controls such as retina vascularization, voice patterns, signature dynamics, hand geometry, keyboard latencies.

## Summary

In summary, keypad interface systems are very common. However, such systems should be carefully designed to minimize the possibility of unauthorized access and misappropriated information. It seems that if users are not presented with a keypad and asked to create passwords rather than personal identification numbers, the chances of a security system failure are lessened. As with all security systems, after implementation, such systems should also be constantly monitored and controlled with extreme caution so that maximum benefits could be enjoyed.

## References

[1] Ben F. Barton and Marthalee S. Barton, "User-Friendly Password Methods for Computer-Mediated information Systems," Computers and Security, vol. 3, 1984, pp. 186-195.

[2] John M. Carroll, Robert B. Mowat, Lynda E. Robbins, and David Wiseman, “The Password Predictor – A Training Aid for Raising Security Awareness,” Computers and Security, vol. 7, 1988, pp. 475–481.

[3] Martin, S. Chodorow and Susan Karp Manning, “Cognition and Memory: A Bibliographic Essay on the History and Issues,” Teaching of Psychology, vol. 10, no. 3, 1983, pp. 163–167.

[4] Horst Feistel, “Cryptography and Computer Privacy”, Scientific American, no. 228 (May 1973), pp. 15–23.

[5] Katie Hafner and John Markoff, Cyberpunk: Outlaws and Hackers on the Computer Frontier, (New York: Simon & Schuster), 1991.

[6] David Kahn, The Code Breakers, (New York: Macmillan), 1967.

[7] Ted D. Karren, “Typical System Access Control Problems and Solutions,” Information Age, vol. 10, January 1988, pp. 23–32.

[8] James H. Kates, “Computer System Penetration Analysis – Is It a Viable Option, in Audit, Control, and Security of Paperless Systems (Orlando: Institute of Internal Auditors Research Foundation), 1990. pp. 87–94.

[9] Walter Kintsch, “Memory for Text”, Discourse Processing, August Flammer and Walter Kintsch (eds), (Netherlands: North-Holland Publishing Company), 1982, pp. 186–204.

[10] S. Klapp and A. Netick, “Multiple Resources for Processing and Storage in Short-Tenn Working Memory,” Human Factors, 1988, pp. 617–632.

[11] Robert Morris and Ken Thompson, "Password Security: A Case History", Communications of the ACM, vol. 22, no. 11, (November 1979), pp. 594–597.

[12] B.B. Murdock, “The Retention of Individual Items,” Journal of Experimental Psychology, vol. 62, 1961, pp. 618–625.

[13] J. Raijmakers and R. Shiffrin, “Search of Associative Memory”, Psychological Review, vol 88, no. 2, March 1981, pp. 93–134.

[14] Bruce L. Riddle, Murray S. Miron, and Judith A. Semo, "Passwords in Use in a University Timesharing Environment," Computers and Security, vol. 8, 1989, pp. 560–579.

[15] U.S. Department of Defense, Computer Security Center, Department of Defense Password Management Guideline, 1986.

[16] Maurice V. Wilkes, Time-Sharing Computer Systems (New York: American Elsevier), 1972.

[17] Charles C. Wood, “Effective information System Security with Password Control,” Computers and Security, vol. 2, 1983, pp. 5–10.
