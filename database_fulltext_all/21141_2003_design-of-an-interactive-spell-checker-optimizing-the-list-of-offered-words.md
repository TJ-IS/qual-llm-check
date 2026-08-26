---
otero_id: 21141
otero_key: "X4C9ZDB9"
title: "Design of an interactive spell checker: optimizing the list of offered words"
authors: "Robert Garfinkel; Elena Fernandez; Ram Gopal"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00115-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design of an interactive spell checker: optimizing the list of offered words

Robert Garfinkel <sup>a,</sup>\*, Elena Fernandez <sup>b</sup>, Ram Gopal <sup>a</sup>

<sup>a</sup>Operations and Information Management, School of Business, University of Connecticut, New Business Administration Unit 1041-411M, Storrs, CT, USA

<sup>b</sup>Statistics and Operations Research Department, Technical University of Catalonia, Barcelona, Spain

Received 1 January 2002; accepted 1 April 2002

## Abstract

Interactive spell checking is an instance of a general problem that is characterized by doubt as to the correctness of an input, and the need to correct the input or offer a set of possible corrections. Our contention is that a well-defined model can provide a basis to improve the performance of spell checkers and other similar applications such as voice recognition, historical document searches, and data imputation among others. In this paper, we introduce a model designed to help the spell checkers within word processors place the correct word at, or near, the top of the list of offered words. A prototype spell checker (SP) is developed based on the model. It is tested on documents typed by subjects and found to be very accurate. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Word processors; Spell checking; Optimization

## 1. Introduction

With the advent of the personal computer, it can be assumed that mistyping of words has become increasingly prevalent since, even in the business world, professional typists no longer do the overwhelming majority of the typing. Thus, for many of us who do our own typing, the spell checkers in our word processors or other software have become indispensable. These programs are used to indicate that the correctness of a word is in doubt. Spell checkers are distinguished from grammar checkers that indicate whether a sentence follows acceptable grammatical rules. The basic steps required of any spell checker are outlined in Ref. [11].

Various studies (e.g. Refs. [4,9,13]) have indicated a variety of average error rates depending on the skill of the typist. In general, the studies, including the results of our own experiments, yield nonword errors (the incorrect ‘‘word’’ is not found in a dictionary) of between 0.2% and 6%. Of course, error rates can also be expected to depend on other factors besides typing skill. For instance, one would be expected to type more accurately while transcribing rather than composing. Error rates based on misspelling rather than mistyping should also decrease dramatically in a phonetic language like Spanish or Hindi as compared to a nonphonetic language such as English. By a phonetic language we mean one for which there is more or less a one-to-one correspondence between spelling and pronunciation. To give one example of how nonphonetic English is, consider that the vowel string ou can have at least five different pronunciations as indicated by the words rough, soul, bought, cougar, and foul. To make matters worse, each of these five pronunciations are found in other vowel strings including u, o, aw, oo, and ow in the words ruff, sole, awl, fool, and fowl.

Spell checking generally consists of two basic tasks. The first is to determine if a word is in the dictionary of the spell checker. The second, in automatic mode, is to seek the most likely replacement word and to effect the replacement. In interactive mode, it is simply to offer an ordered list of possible replacements.

Automatic spell checking seems to have been the subject of the vast majority of the research on spell checking (see for example Ref. [8]). It is clearly the appropriate model when time, cost, or other considerations preclude the option of letting the user make the final corrections. Interactive spell checking has received much less research attention, despite being the mode in which most of us work. Of course, the two models are closely related in that any technique that generally produces the correct replacement word will undoubtedly produce ‘‘good’’ lists as well. On the other hand, we note that in very sensitive applications, where it is critically important that the replacement word be correct, it may be appropriate to devise complex and relatively time-consuming algorithms. These may, for instance, take the context of the writing into account. In this work, since we assume that the typist will always have the chance to correct any mistakes, and since the algorithm will be part of a commercial word processing package, fast heuristics would seem to be the most appropriate.

All modern word processors have spell checkers, and although they generally work quite well, their algorithms for choosing the list of replacement words are not well documented. Note that spell checkers within commercial word processing are generally attributed to other companies. For instance, Microsoft Word 97 (hereafter abbreviated as MSW97) attributes its spell checker to International CorrectSpell [6].

To some extent, our interest in spell checkers was motivated by the observation that from time to time, the list of offered words seems counterintuitive. For instance, MSW97 does not include idea in the list of offerings when the typed word is iedea. This seems strange because the two words differ by only one letter and, furthermore, most English speakers when presented with iedea would probably assume that the typist meant to type idea. Stranger yet, the only word offered is the French word idee. Table 5 in Section 4.3 contains a number of similar anomalies. For the moment, we leave open the precise definition of such an anomaly, hoping that the above example makes the concept clear. This omission will be rectified in Section 4 once a model has been presented that defines the closeness of two words.

We have discovered the same sorts of anomalies in all word processors that we have encountered. We focus on MSW97 when we refer to commercial word processors only because it was one of the respected standards of the field at the time of our experiments. We also emphasize that we have compared our prototype spell checker (SP) to MSW97 for the same reason. Thus, it was chosen as a benchmark to see if our approach was viable. Our hope was simply that, by the measures listed above, SP would be competitive with MSW97. It should be noted that since the completion of the experiments, WORD 2000 and WORD XP have appeared. We have observed that many of the anomalies, noted in Section 4.3, of MSW97 are not anomalies of MSW00 and MSWXP. That is an encouraging observation since spell checkers are being continuously improved and perhaps are using models similar to that which we develop later to achieve this improvement. If that were true (and we have not been able to confirm this conjecture from Microsoft), it would serve as further validation that such models can be useful in this and other similar applications listed below.

In Section 2.2, we develop a systematic way to construct the replacement list based on a likelihood function. The goal is to be able to consistently place the correct word not only in the list, but near the top. The maximum size of the list is one of the parameters of the prototype spell checker, and is described in Section 3. In the experiments of Section 4, the actual size never exceeds 10. We define the following measures of good lists.

AV: the average location of the correct word in the lists.

$P _ { \mathrm { { A } } } { \mathrm { { : } } }$ the percentage of lists for which the correct word appears at all.

$P _ { 1 }$ : the percentage of lists for which the correct word appears first.

$P _ { 5 } \colon$ the percentage of lists for which the correct word is among the first five.

The rationale for $P _ { \mathrm { { A } } }$ and AV are clear. $P _ { 1 }$ is of particular importance in the realm of automatic correction since presumably, the first word on the list would be the replacement. We add $P _ { 5 }$ since if one right clicks on a misspelled word in MSW97, the first five elements of the list are given.

The experimental results of Section 3 will show that our model is quite successful in terms of these four measures. Even so, it would be too simplistic to suggest that commercial word processors should discard their spell checkers and use one based on our prototype. Our intent is simply to suggest a welldefined model and algorithm that could be the basis of commercial spell checkers of the future.

The model-based approach outlined in the paper can also be employed in a number of related application areas. Such applications all have in common the presence of (1) doubt as to the correctness of an input and (2) the need to correct the input or offer a set of possible corrections. Some of these application areas are presented below.

Search engines on the Internet. Spell checking user queries can improve the efficiency (of search) and effectiveness (of obtaining useful documents). This may grow in importance as the number of non-native English speakers using the Internet grows.

Enhancing communication between speech or language-impaired individuals [9]. Text-to-speech conversion is an important issue in facilitating effective communication via telecommunication devices. Spell checking is critical to produce intelligible speech.

Historical document search [12]. Over the centuries, the English language and word spelling have evolved. There was little proofreading of earlier documents and variant spellings were fairly common. Performing an effective search on these documents requires an awareness of spelling errors.

Genetic research applications [10]. Properties and behavior of molecules depend on the sequence of basic elements (much the same way as words are sequences of the alphabets). Similar techniques to ours can be applied to study the relationship between molecules.

Data imputation [3]. Responses to some queries of a questionnaire may be known to be in error because they fail one or more ‘‘edits’’. The problem is to determine the true intended response.

Search on music databases [14]. Recent growth in digital representation of music has led to the creation of large music databases. There is considerable interest in efficient retrieval techniques from such music collections. ‘‘Query-by-humming’’ systems permit a user to hum a tune and retrieve songs with similar tunes. A significant issue that arises in this context is that users vary significantly in their vocal abilities.

The model used to evaluate possible replacement words is introduced in Section 2. The prototype spell checker, SP, is described in Section 3. Section 4 contains the results of experiments with SP and comparison to MSW97. Results and possible future research are the subject of Section 5.

## 2. The model

Define a typed word m to be a sequence of consecutive symbols (throughout the paper, italics indicate the input to or output of a spell checker). In general, these symbols will be letters, but for the moment, other symbols such as numbers or apostrophes can be considered to be contained in m. The symbol m stands for ‘‘mistyped’’, and is used for the typed word because it will be of interest to us only if m is wrong in the sense that it does not appear in the relevant dictionary D.

It is important for the testing of the model of Section 3.2 that there be a ‘‘correct’’ word $w ^ { * } \in \mathrm { D } .$ which is the word that the typist intended to type. Because of this concept of a correct word, the requirement that the sequence of symbols in m be consecutive is quite important. For instance, if the typist created a split word by inserting a space or a run-on word by omitting one, then it is not clear which word is $w ^ { * }$ . We avoid these ambiguities in the computational testing of Section 4 by removing split and runon words. An extension of our proposed model could deal with split and run-on words by concatenating a word with its neighbors and performing multiword searches on the dictionary.

Once it is determined that mgD, an offering list $L ( m ) { = } \{ w _ { 1 } ( m ) , w _ { 2 } ( m ) , . . . \}$ is created. In the model of Section 3.2, the order of the words in the list of offerings is intended to indicate a corresponding order in the probability of being the correct word, with the first word having the greatest probability. Although the same statement is not made explicitly, an implication of similar intent is found in International CorrectSpell [6]. Its documentation states that it $^ { 6 6 } \cdot$ . .provides the desired correction for a misspelled word early (usually first) in a short list of candidates. $\therefore { \vec { \cdot } } ^ { \flat } .$

## 2.1. Some factors that may influence the list of offered words

The cause of mistyping is naturally attributed to typing errors or spelling errors. Typing errors are simply physical mistakes, while a spelling error is made because the typist does not know how to spell the word. An examination of the offerings of MSW97 makes it clear that both categories are considered. Typing errors are exemplified by $\begin{array} { r } { m = j s u t } \end{array}$ resulting in $L ( m ) { = } ( j u s t , j u t )$ . It would be hard to imagine that if either element of $L ( m )$ were correct, the error could be attributed to spelling. On the other hand, MSW97 seems to take spelling mistakes into account as distinct from typing mistakes. For example, for $m = o f r ,$ $o \nu e r \in L ( m )$ but our g $L ( m )$ implying that the typist was searching for a word sounding like over. Similarly for $m = t y p , t i p \in L ( m )$ but $t o p \notin L ( m )$ .

Our model, as described in Section 2.2, does not specifically take spelling errors into account. The reason is that our aim is to present a general framework of a model and then to see how well a simple realization works. If that is successful, and depending on the application, further research can look at various levels of increased complexity, including spelling errors. Typing errors are much simpler to model than spelling errors. Each of us can hit the key for the letter q when we meant to hit the neighboring key of the letter a and it signifies nothing more than a physical mistake. A rudimentary approach that simply looks at the set of words that can be found by reversing a typing error involving a single letter is described in Ref. [2]. It is reported that 80% of words can be corrected by this device. On the other hand, there are many possible reasons for spelling errors. It may be that two different combinations of letters sound the same, or possibly even that the typist does not know how to say the word correctly. In Ref. [5], the efficacy of some commercial spell checkers with regard only to spelling errors is tested.

Despite not considering spelling errors, we will see from the results of Section 4 that our model performs quite well. Perhaps that is because the population tested are connected to a university, so that the subjects might be less likely to make spelling errors (even in English) than is the population in general.

## 2.2. A flexible likelihood function

Here, we develop a likelihood function $g ( w , m )$ to be used in determining the placement and ordering of the elements of $L ( m )$ . In fact, $g ( w , m )$ could better be called an anti-likelihood function in the sense that as $g ( w , m )$ increases, our likelihood that w is the correct replacement for m decreases. That is, $w _ { 1 }$ is considered to be more likely to be the correct word than $w _ { 2 }$ if $g ( w _ { 1 } , m ) < g ( w _ { 2 } , m )$ . Therefore, if $w _ { 1 }$ and $w _ { 2 }$ both merit placement in L(m), $w _ { 1 }$ will appear before $w _ { 2 }$

There are many options for the form of such a function. The likelihood function that we use is quite simple and, as shown in Section 3, a particular realization has proven quite effective in our experiments.

## 2.2.1. The subarguments

The arguments w and m of $g$ are broken down into three subarguments. These are the following.

$e _ { w m } \colon$ The fewest single-errors which could transform the word w into the word m. The possible individual errors are:

$$
\text { delete   a   letter   (del.); }
$$

insert a letter (ins.);

substitute one letter for another (sub.);

interchange two adjacent letters (int.).

Note that if $e _ { w m } = 1$ , the single-error is unique. This is not true in general if $e _ { w m } > 1$ . For example, if $w = t h i n k$ and $m = t i h k$ , then $e _ { w m } = 2$ . Two possibilities for the intermediate word after the first error would be tihnk and thihk. In the first case, m would result from w after an interchange and a deletion, while in the second, it would be a substitution and a deletion.

$c _ { w } .$ The commonness of w. In our program, $c _ { w }$ is measured on a scale from zero to nine, with zero being assigned to the most common words (e.g. a and the).

$f _ { w m } .$ Zero if w and m have the same first letter and one otherwise.

## 2.2.2. Why these subarguments?

It is simple to defend $e _ { w m }$ as a model of ‘‘closeness’’. A factor that may seem less fundamental is the ‘‘commonness’’ of w. It seems logical that if all else is equal, a more common word is more likely to be correct than a less common word. Of course, the definition of commonness is quite flexible. A word that is common to you may not even be part of the vocabulary of someone else. Two examples from MSW97 illustrate that commonness does not seem to consistently play an important role in the ordering of their lists. First, $w _ { 1 } ( a l o s ) { = } L a o s .$ , while the seemingly more obvious choice is $a l s o = w _ { 2 } ( a l o s )$ . Similarly, w (nerver) is the obscure word nervure, while the more obvious choices are nerve = w<sub>3</sub>(nerver) and never = w<sub>6</sub>(nerver).

Related to this point is another quote from Ref. [6]. ‘‘. . .The quality of a spelling correction system does not increase in direct proportion to the size of its lexicons: bigger is not always better. A wordlist that is too large can include obscure words that coincide with misspellings of common words. For example, calendar could be misspelled as calender, which is a technical term for a machine that smoothes paper or fabric. Smaller is not always better either. A small lexicon can come at the expense of thorough coverage. A wordlist that is too small will not recognize correct words because the database is missing certain commonly used words. Small spelling correction databases often lack adverbs, geographical and cultural terms, and abbreviations and acronyms. International CorrectSpell’s databases include words that comprise the core of contemporary written language. . . .’’.

The measure $c _ { w }$ is, to us, one of the keys to improving the performance of spell checkers. Note that International CorrectSpell addresses this point when they say that a comprehensive dictionary may be detrimental to the attempt to find the correct word in that there may be very many choices, some of which are too obscure to be likely replacements.

However, limiting the size of the dictionary only affects the existence or lack of existence of a word on the list. Our definition of commonness within the likelihood function influences the order of the placement. Furthermore, it allows for individual flexibility in the assignment of commonness values.

The third subargument, $f _ { w m } ,$ is harder to defend than the first two. In Ref. [9], it is reported that in some studies, up to 93% of erroneous words have correct first letters. In our experiments, the percentage reaches 90%. Thus, there may be some justification in having more confidence in the first letter than in other letters. Another reason why we included $f _ { w m }$ is that, especially for long words, we have observed that L(m) from WORD is generally unlikely to contain elements w with different first letters from that of m.

## 2.2.3. The function

In the prototype spell checker SP, we use the linear function

$$
g (w, m) = e \left(e _ {w m} - 1\right) + c \cdot c _ {w} + f \cdot f _ {w m}.\tag{1}
$$

where $e , \ c ,$ and f are nonnegative constants. For example, if $c _ { t h e } = 0$ , then g(teh, the) = 0 since only one interchange is needed to transform the into teh and since the two words both begin with the letter t. Thus, the would, at worst, be tied for the most likely replacement for teh.

## 2.3. Customizing and learning

An appealing aspect of creating L(m) from a function g(w,m) such as Eq. (1) is the possibility of customizing the function based on the type of errors made by an individual or group of individuals. Here, there are clearly many options. Different set of weights for the subarguments of Section 2.2 may be more appropriate under different conditions. For instance, the weights associated with $e _ { w m }$ could be differentiated by the type of error. An individual who is most likely to make insertion errors would give higher weight to that type than to deletions, etc. Even more finely, one could differentiate among substitution of letters on neighboring keys, etc. Similarly, not only could individuals use their own measures of commonness $c _ { w }$ but they could estimate them by keeping track of the relative frequencies of the words they use.

A further option would be to allow the function to be updated by training it based on typing experience. Once the arguments have been chosen, ‘‘optimal’’ weights can be determined by ‘‘training’’ the function via any of a number of artificial intelligence techniques. This could be done within customizing for individuals or groups or to try to find ‘‘universal constants’’.

## 3. A prototype spell checker: SP

## 3.1. The dictionary used in SP

In the interest of simplicity and control, SP uses its own dictionary (DICT) rather than a standard one. The elements of DICT come primarily from two sources: emails received by the authors and the complete set of words offered by commercial spell checkers in our experiments. Thus, every word offered by WORD in the experiments of the next section is in DICT. Currently, DICT contains about 3500 entries.

Every word in DICT is a string of lower case letters. Thus, capitalized letters are changed to lower case and dashes, apostrophes, numbers, etc. are simply ignored. We do that because all of those symbols can change the meaning of a word and would therefore require a more complex code than that of SP to find the appropriate list of offerings. Since SP is simply a prototype, these kinds of complications are left for future developments (note that proper names and words containing symbols that impart meaning, e.g. apostrophes, are not considered in our experiments when we compare SP to MSW97).

Attached to each word is its commonness rating. For instance, two entries in DICT are the 0 and represtinate 9. The commonness values are assigned to the words whenever SP does not find a word in DICT and the user chooses to add the word to DICT. For the sake of consistency, all values have been assigned by the same person, namely one of the authors. They are done in a fairly ad hoc manner. There is no intent to say, with any scientific justification, that a word with $c _ { w } = 4$ is more common than a word with $c _ { w } = 5$ . On the other hand, such distinctions could easily be made in future versions of the program. For us, the intention is to at least be able to distinguish among the four categories: very common; fairly common; relatively uncommon; and very rare. If a spelling corresponds to two or more words, the commonality will go with the most common. For instance, if the entry quick 4 appeared, it would refer to the concept of speed rather than to a painfully sensitive part of the body, such as the area under the fingernails.

As usual, the words of DICT are ordered alphabetically and if $w _ { 1 }$ and $w _ { 2 }$ are any two words then $w _ { 1 } < w _ { 2 }$ means that $w _ { 1 }$ would precede $w _ { 2 }$ in DICT.

## 3.2. The SP algorithm

On initiation of the algorithm, the user is asked to input the following parameters:

$L ^ { + }$ : the maximum number of words in L(m); $g ^ { + }$ : an upper bound on the objective value of any word in $L ( m )$ ;

$e , c ,$ and f: the parameters of the function g in Eq. (1).

An overview of the algorithm is given below. Procedure Spellcheck

While not end of document do:

```ruby
Read next word from text: t_word
Select a word from DICT: d_word
If t_word ≠ d_word then
    If user declines to add t_word to DICT then
    Give list of possible alternatives to t_word
    Endif
Endif
End
```

Every t<sup>\_</sup>word, is compared to a single d<sup>\_</sup>word where

$$
d \_ w o r d = \min \{w: w \geq t \_ w o r d \text {   and   } w \in \text {   DICT } \}.
$$

If t<sup>\_</sup>word = d<sup>\_</sup>word, then t<sup>\_</sup>word is already in DICT. Otherwise, since it is possible that t<sup>\_</sup>word is a correct word not yet present in DICT, the user is given the option to add t<sup>\_</sup>word to DICT. If that option is declined, t<sup>\_</sup>word is assumed to be mistyped. That is, m = t<sup>\_</sup>word and the list $L ( m )$ is generated.

In the prototype SP, every $w \in L ( m )$ satisfies $e _ { w m } \leq 2 . \mathrm { O f c o u r s e } , e _ { w m } > 2$ could easily be incorporated but the computational burden within our algorithmic framework would increase (see Section 3.3). Since the input to SP is m rather than w, we define four basic transformations that can operate on m in the search for the correct word w. Because of symmetry, these are, of course, the same basic operations defined in Section 2.2, namely delete, insert, substitute, and interchange. From $e _ { w m } \leq 2 , w \in L ( m )$ only if w can be obtained from m by a single basic transformation, or by composition of any two basic transformations.

The basic and composite transformations are defined below. Let $n _ { m }$ denote the number of letters of a word m and $\ell _ { m , i }$ be the ith letter of m. Also, let $\ell ^ { * }$ and $\ell ^ { \prime }$ be any two letters in $\mathrm { A } { = } \{ \mathsf { a } , . . . . , z \}$ . Two of the arguments of each composite transformation are numbers i and $j ,$ each between 1 and $n _ { m } .$ In all cases, they refer to places in the original word m rather than in the word that results from the first of the two basic transformations. All distinct basic and composite transformations are listed below. For composite transformations, it is assumed that they are applied in the order indicated.

Basic transformations

<table><tr><td>del(i,m)</td><td>Delete  $\ell_{m,i}$ .</td></tr><tr><td>ins( $\ell^{*},i,m$ )</td><td>Insert  $\ell^{*}$  directly before  $\ell_{m,i}$ .When  $i=n_{m}+1$ ,  $\ell^{*}$  isinserted at the end of m.</td></tr><tr><td>sub( $\ell^{*},i,m$ )</td><td>If  $\ell_{m,i}\neq\ell^{*}$ , let  $\ell_{m,i}=\ell^{*}$ .</td></tr><tr><td>int(i,m)</td><td>If  $\ell_{m,i}\neq\ell_{m,i+1}$ , interchange  $\ell_{m,i}$  and  $\ell_{m,i+1}$ , where \( i</td></tr></table>

Composite transformations

del $\mathrm { d e l } ( i , j , m )$ del(i,m) and $\operatorname { d e l } ( j , m ) ,$

$$
i \neq j.
$$

del<sup>\_</sup>ins(i,<sup>S</sup> \*, j,m) $\operatorname { d e l } ( i , m )$ and ins $( \ell ^ { * } , j , m )$

$$
i \neq j,
$$

$$
\operatorname{sub} \left(\ell^ {*}, i, m\right)
$$

del $s \mathrm { u b } ( i , \ell ^ { * } , j , m )$ $\operatorname { d e l } ( i , m )$ and $\operatorname { s u b } ( \ell ^ { * } , j , m )$

$$
i \neq j,
$$

$$
\text { to } \operatorname{sub} (\ell^ {*}, i, m)
$$

del $\mathrm { i n t } ( i , j , m )$ del(i,m) and int( j,m),

$$
j <   i - 1
$$

$$
j > i,
$$

$$
\text { Also } j <   n _ {m}.
$$

ins<sup>\_</sup> $\mathrm { i n s } ( \ell ^ { * } , i , \ell ^ { \prime } , j , m )$ $\mathrm { i n s } ( \ell ^ { * } , i , m )$ and ins $( \ell ^ { \prime } , j , m )$

$$
\text {   If   } i = j
$$

$$
\ell^ {\prime}.
$$

$$
\ell^ {*}
$$

<table><tr><td>ins_sub( $\ell^{*},i,\ell',j,m$ )</td><td>ins( $\ell^{*},i,m$ ) and sub( $\ell',j,m$ ).</td></tr><tr><td>ins_int( $\ell^{*},i,j,m$ )</td><td>ins( $\ell^{*},i,m$ ) and int( $j,m$ )where  $i \neq j+1$ , else it is equivalent to ins( $\ell^{*},j,m$ ).Also  $j < n_{m}$ .</td></tr><tr><td>sub_sub( $\ell^{*},i,\ell',j,m$ )</td><td>sub( $\ell^{*},i,m$ ) and sub( $\ell',j,m$ ), where  $i \neq j$ , else it is equivalent to sub( $\ell',j,m$ ).</td></tr><tr><td>sub_int( $\ell^{*},i,j,m$ )</td><td>sub( $\ell^{*},i,m$ ) and int( $j,m$ ), where  $i \neq j$ , else it is equivalent to sub( $j,m$ ).Valid for any other  $i$  and  $j$  but only applied when  $i \neq j-1$  and  $j \neq i+1$ , else the same result can be obtained with del_ins. Also  $j < n_{m}$ .</td></tr><tr><td>int_int( $i,j,m$ )</td><td>int( $i,m$ ) and int( $j,m$ ), where  $i \neq j$ . Also  $i < n_{m}$  and  $j < n_{m}$ .</td></tr></table>

The list of possible alternatives is generated in two phases corresponding to $e _ { w m } = 1$ and $e _ { w m } = 2$ . Each time a candidate word is considered, it is tested for possible inclusion in $L ( m )$ by the function Include described below.

Include(w,m)

Let $n _ { L ( m ) }$ be the number of words currently in $L ( m )$ Let $g ^ { * }$ be the value of the last word (word $n _ { L ( m ) } )$ in L(m))

Calculate g(w,m)

If $g ( w , m ) \leq g ^ { + }$ do

If $n _ { L ( m ) } { < } \mathrm { L } ^ { + }$ or $g ( w , m ) < g ^ { * }$ , then place w in $L ( m )$ ordered by g

For convenience, we use the loose notation $w = \mathrm { t r a n s } ( m )$ to mean that w is the word that results from the specified transformation. Thus, for instance, $t h e = \operatorname { i n t } ( 2 , t e h )$

Phase 1

For $i = 1 , n _ { m }$ do

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
If $w = \text{del}(i, m) \in \text{DICT}$, then Include(w, m)
If $w = \text{int}(i, m) \in \text{DICT}$, then Include(w, m)
For $\ell^* \in A$ do
    If $w = \text{ins}(\ell^*, i, m) \in \text{DICT}$, then Include(w, m)
    If $w = \text{sub}(\ell^*, i, m) \in \text{DICT}$, then Include(w, m)
End for
End for
</div>

In some cases, it may not be necessary to enter Phase 2. In particular, if $n ^ { * } = L ^ { + }$ , it is possible that the best word that could result from Phase 2 would be no better than the word currently residing in the place $L ^ { + }$ in $L ( m )$ . Let $c ^ { * }$ and $f ^ { * }$ be the values for commonness and first letter for the last word in $L ( m )$ , respectively. Then, Phase 2 should be entered only if

$$
c \cdot c ^ {*} + f \cdot f ^ {*} - e > 0.\tag{2}
$$

This follows since the left-hand side of Eq. (2) is the maximum improvement that any word found in Phase 2 can have over the worst word currently in $L ( m )$

Phase 2

```csv
Phase 2
For i = 1, n_m do
    For j = 1, n_m do
    If w = del_del(i,j,m) ∈ DICT, then Include(w,m)
    If w = del_int(i,j,m) ∈ DICT, then Include(w,m)
    If w = int_int(i,j,m) ∈ DICT, then Include(w,m)
    For ℓ* ∈ A do
    If w = del_ins(i, ℓ*,j,m) ∈ DICT, then Include(w,m)
    If w = del_sub(i, ℓ*,j,m) ∈ DICT, then Include(w,m)
    If w = ins_int(ℓ*,i,j,m) ∈ DICT, then Include(w,m)
    If w = sub_int(ℓ*,i,j,m) ∈ DICT, then Include(w,m)
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
For $\ell' \in A$ do
    If $w = \text{ins\_ins}(\ell^*, i, \ell', j, m) \in \text{DICT}$, then
    Include(w, m)
    If $w = \text{ins\_sub}(\ell^*, i, \ell', j, m) \in \text{DICT}$, then
    Include(w, m)
    If $w = \text{sub\_sub}(\ell^*, i, \ell', j, m) \in \text{DICT}$, then
    Include(w, m)
End for
End for
End for
End for
</div>

## 3.3. Complexity of the SP algorithm

Procedure spell check requires one dictionary lookup. This is a relatively simple special case of a string matching problem combined with a search in the data structure representing DICT. Techniques for this kind of lookup are discussed in Refs. [1,7,8]. Let the time needed for the lookup be $t _ { \mathrm { L o o k } }$

Assuming that w is stored in an ordered list, broadly speaking, the basic transformations are more or less done in constant time. In Phase 1, delete and interchange are performed once each, and insert and substitute AAA and $| \operatorname { A } | - 1$ or 26 and 25 times, respectively. Since a dictionary lookup accompanies each transformation, the order of Phase 1 is approximately $2 \left| \mathrm { A } \right| n _ { m } t _ { \mathrm { L o o k } } = 5 2 n _ { m } t _ { \mathrm { L o o k } }$ . Since we impose $e _ { w m } \leq 2$ , the order of Phase 2 is dominated by the three composite transformations sub\_sub, sub\_ins, and ins\_ins. Each takes about twice the time of the basic transformations. Thus, whenever Phase 2 is entered, the overall complexity of SP is approximately $6 t _ { \mathrm { L o o k } } ( 2 6 n _ { m } ) ^ { 2 }$

While efficiencies could be achieved by clever data structures, we have found that the list is offered virtually instantaneously, so that incorporation within a word processor should be feasible with respect to time.

## 4. The experiments

SP was programmed in FORTRAN on a Sun workstation. Experiments were carried out on typing by staff, faculty, and doctoral students of the business school at the University of Connecticut.

## 4.1. The data

The following request for help was sent electronically to all staff, faculty, and doctoral students of the Business School of the University of Connecticut.

Dear SBA colleague:We are doing a research project on spell checkers with colleagues of the Polytechnic Institute of Catalonia in Barcelona, Spain. The objective is to try to design an ‘‘optimal’’ spell checker in the sense that if you type an incorrect word, the correct word will be offered to you as one of the first alternatives. We are partially motivated by the sometimes strange options given by commercial word processors.We have designed a prototype and would like to test it based on the typing of real people like yourselves. We are therefore requesting that, if you can find the time, you do the following for us: Type this letter (i.e. actually retype what you’re reading right now); and Type a note of about the same size of your own creation without copying it from an existing document. The subject matter is irrelevant! Send us, either electronically or on a disk or on paper your version of this letter and the note. For the note, we will also need an indication of what the correct words were if you misspelled any.We want you to type at your normal pace and ask you not to correct any errors that you make. We want to see what kinds of mistakes people make! I’m an incredibly bad typist so it’s unlikely you can do worse than me.Any help you can give us will be greatly appreciated. We’d like to start our analysis as quickly as possible but certainly better late than never.

We hoped to be able to compare various typing abilities on the same document so as to eliminate the variability inherent in having each individual working on a different document. In addition, we asked for a copy of their own typing so as to be able to contrast typing on original against copied documents. The assumption being that error rates would increase when correct spellings are not present. We received a total of 29 documents from 21 people: 5 professors, 10 staff, and 6 doctoral students. The typing results are summarized in Table 1.

Table 1 Individual typing summary

<table><tr><td></td><td>Total</td><td>Percent</td></tr><tr><td>Total words</td><td>6721</td><td></td></tr><tr><td>Errors</td><td>344</td><td>5.12</td></tr><tr><td> $e_{wm}=1$ </td><td>309</td><td>94.21</td></tr><tr><td> $e_{wm}=2$ </td><td>18</td><td>5.49</td></tr><tr><td> $e_{wm}>2$ </td><td>1</td><td>0.30</td></tr><tr><td>Deletions</td><td>68</td><td>22.01</td></tr><tr><td>Insertions</td><td>96</td><td>31.07</td></tr><tr><td>Substitutions</td><td>68</td><td>22.01</td></tr><tr><td>Interchanges</td><td>77</td><td>24.92</td></tr><tr><td>Split words</td><td>6</td><td>1.74</td></tr><tr><td>Run-on words</td><td>10</td><td>2.91</td></tr><tr><td>First letter incorrect</td><td>35</td><td>10.17</td></tr></table>

The 344 total mistyped words include split and run-on words for which there is no correct word w. The remaining mistyped words are partitioned by path length and within $e _ { w m } = 1$ , and since the path is unique, they are further partitioned by error type.

Ninety four percent of words could be corrected by limiting the search to $e _ { w m } = 1$ . This is on the high end of the estimates in the literature [8], which range from 69% to 94%. Further, there was only one instance of $e _ { w m } > 2 ,$ , and that was for w = polytechnic and $m = p o l y -$ ytechnique, with $e _ { w m } = 3$ . Despite the presence of original documents, it became clear from careful examination of all errors that polytechnique was also the only error that could plausibly be attributed to spelling. Furthermore, since the misspelled word is the French equivalent of the original, even that classification is doubtful. It is intuitively likely that the lack of spelling errors would account for the lack of instances of $e _ { w m } > 2$ . Again, this can most likely be explained by the fact that the subjects were all associated with a university.

About 10% of errors involved the first letter. The estimates from Ref. [9] range from 7% to 15%. This would lead one to believe that some f >0 in Eq. (1) might lead to an improvement in performance, although we did not find it in our experiments.

The overall error rate, including ‘‘good’’ words, of 5.12% varied, but not dramatically, by classification of the subjects. The error rates were 5.5, 6.8, and 4.9 for faculty, students, and staff, respectively. Thus, although the staff had the lowest rate, there was not the kind of dramatic difference that would have been common in the days of secretary/typists. Finally, and perhaps surprisingly, the incidences of the four basic typing errors were fairly uniform, ranging from a high of 31.1% for insert to a low of 22% for delete and substitute. This contrasts with the results in Ref. [9] for which the range is 51.9% for insert and 7.6% for interchange.

Table 3  
Table 2 Test results

<table><tr><td>Total words = 266</td><td>MSW97</td><td>SP</td></tr><tr><td> $P_{1}$ </td><td>0.74</td><td>0.85</td></tr><tr><td> $P_{5}$ </td><td>0.90</td><td>0.98</td></tr><tr><td> $P_{A}$ </td><td>0.92</td><td>1.00</td></tr><tr><td>Average</td><td>2.64</td><td>1.36</td></tr><tr><td>Standard deviation</td><td>2.87</td><td>1.11</td></tr><tr><td>Average ignoring missing words</td><td>1.35</td><td>1.30</td></tr><tr><td>Standard deviation ignoring missing words</td><td>1.43</td><td>0.97</td></tr></table>

## 4.2. The results

Prior to the final experiments, a large number of runs were performed on all of the data to determine the best universal values in SP of the parameters $e , c ,$ and f from Eq. (1), in terms of the measures $\mathrm { A V } , P _ { \mathrm { A } } ,$ $P _ { 1 } ,$ , and $P _ { 5 }$ introduced in Section 1.

A range of all three parameters was tested and it became clear that, not only for average performance but also for virtually all typing instances, $( e , c , f ) { = } ( 1 0 , 1 , 0 )$ gave the best results. These numbers can be interpreted as follows. First, for the range of parameters that we considered, there was no advantage in considering a typing error in the first letter to be less likely than errors in other letters. That is, despite the fact (see Table 1) that only about 10% of errors were made in the first letter, $e _ { w m }$ and $c _ { w }$ dominated $f _ { w m } ,$ , so that we set $f { = } 0$ in our experiments. This leaves open the possibility that, for some data sets, $f { > } 0$ may be appropriate. Second, the values $( e , c ) { = } ( 1 0 , 1 )$ when the range of $c _ { w }$ is [0,9] mean that all words w with $e _ { w } = 1$ are offered before those with $e _ { w m } = 2$ and within each value of $e _ { w m }$ words are ordered by $c _ { w } .$ Finally, we note that the parameters (10,1,0) completely dominated $( 1 0 , 0 , 0 )$ in every document. That is, ordering by commonness provided significant advantages in predicting the correct word. Thus, in all the results of this section, the parameters $( e , c , f ) { = } ( 1 0 , 1 , 0 )$ are used uniformly to make comparisons to MSW97 straightforward.

The 266 distinct words m (some were duplicated), for which the correct words were defined, were checked by MSW97 and by SP using the following parameters:

$L ^ { + }$ : the maximum number of words in $L ( m ) = 1 0 ;$ $g ^ { + }$ : the upper bound on the objective value of any word in $L ( m ) = 2 0 ;$ ;

$e , c ,$ and f: the parameters of the function g in Eq. $( 1 ) , = 1 0 , 1$ , and 0.

Again, there was no intent to show that one program is ‘‘better’’ than the other, but only to see if model (1) is reasonable, as compared to a respected benchmark. $L ^ { + } = 1 0$ was selected because 10 words is the longest list that was offered by MSW97 in our experiments. If $L ^ { + }$ were decreased, at some point, the probability of $w \in L ( m )$ would decrease, although in this case, there would have been no decrease until $L ^ { + }$ reached six. A value of $g ^ { + } = 2 0$ means that no word was discarded because of score since $g ^ { + }$ cannot exceed 19 in our model. The influence of this parameter is discussed further in the analysis of Table 2 below.

The last four rows of Table 2 concern the average placement of $w ^ { * }$ . Statistics on placement are duplicated because of the dilemma of how to count missing words. In the AV row, missing words were given the score 11 since $g ^ { + } = 1 0$ in SP, and we are not aware that there is a parameter equivalent to $g ^ { + }$ in MSW97. $\mathrm { A V ^ { * } }$ is the average placement ignoring missing words.

From the data of Table 2, it is clear that SP is viable using MSW97 as a benchmark. In fact, based on these experiments, SP seems to outperform MSW97 as shown by the hypothesis tests of Table 3, where P refers to the population probability. Again, we recognize that the four significant comparisons are mainly due to MSW97 not including the correct word in $L ( m )$ from time to time, and that that event may very well not occur in MSW00 and MSWXP.

The list of words not found by MSW97 in our experiments is given in Table 4.

<table><tr><td>Hypotheses accepted</td><td>t-Statistic</td><td>Confidence</td></tr><tr><td> $P_{1}$ (SP) $>P_{1}$ (MSW97)</td><td>1.995</td><td>0.997</td></tr><tr><td> $P_{5}$ (SP) $>P_{5}$ (MSW97)</td><td>4.134</td><td>0.99998</td></tr><tr><td> $P_{A}$ (SP) $>P_{A}$ (MSW97)</td><td>4.477</td><td>0.999996</td></tr><tr><td>AV(SP)&lt;AV(MSW97)</td><td>4.705</td><td>0.999998</td></tr><tr><td>AV*(SP)&lt;AV*(MSW97)</td><td>0.437</td><td>0.669</td></tr></table>

Table 5  
Table 4 Not found by MSW97

<table><tr><td>m</td><td>w*</td><td>g(w*,m)</td><td>SP placement</td><td>First three WORD offerings</td><td>Range of g(w,m)</td></tr><tr><td>ahfve</td><td>have</td><td>11</td><td>1</td><td></td><td></td></tr><tr><td>artially</td><td>partially</td><td>6</td><td>1</td><td>artily</td><td>18</td></tr><tr><td>aspaces</td><td>spaces</td><td>5</td><td>1</td><td>aspics asperses asepses</td><td>17–29</td></tr><tr><td>bsed</td><td>based</td><td>5</td><td>5 to 6</td><td>bed</td><td>3</td></tr><tr><td>chekerd</td><td>checkers</td><td>17</td><td>7</td><td>checked cheered</td><td>15–17</td></tr><tr><td>fooice</td><td>office</td><td>15</td><td>1 to 2</td><td>foci</td><td>28</td></tr><tr><td>longwe</td><td>longer</td><td>13</td><td>1 to 2</td><td>longs Longview longs</td><td>13–29</td></tr><tr><td>motation</td><td>notation</td><td>8</td><td>2</td><td>mutation motivation motion</td><td>6–26</td></tr><tr><td>mt</td><td>my</td><td>1</td><td>3 to 4</td><td>mat met</td><td>2–4</td></tr><tr><td>oace</td><td>pace</td><td>5</td><td>4 to 5</td><td>ace oak</td><td>5–15</td></tr><tr><td>od</td><td>of</td><td>0</td><td>1 to 4</td><td>do odd old ode</td><td>0–8</td></tr><tr><td>owrkds</td><td>words</td><td>14</td><td>1 to 2</td><td>orchids</td><td>36</td></tr><tr><td>ptions</td><td>options</td><td>6</td><td>1</td><td>pitons</td><td>28</td></tr><tr><td>ral</td><td>real</td><td>3</td><td>2</td><td>al rail rally</td><td>5–15</td></tr><tr><td>ve</td><td>be</td><td>0</td><td>1 to 2</td><td>ver vet vex</td><td>6–9</td></tr><tr><td>versom</td><td>version</td><td>17</td><td>4</td><td>verso versos</td><td>9–9</td></tr><tr><td>weokrd</td><td>word</td><td>14</td><td>1</td><td>worked</td><td>23</td></tr><tr><td>ypte</td><td>type</td><td>15</td><td>8 to 10</td><td>yapped yipped</td><td>37</td></tr></table>

Anomalies of MSW97

<table><tr><td>m</td><td>w*</td><td>g(w*,m)</td><td>SP placement</td><td>First three WORD offerings</td><td>g(w,m)</td></tr><tr><td>ajbout</td><td>about</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>dal</td><td>deal</td><td>5</td><td>3</td><td>al dale Daly</td><td>6-9</td></tr><tr><td>dpoing</td><td>doing</td><td>0</td><td>1</td><td>doping</td><td>6</td></tr><tr><td>forom</td><td>from</td><td>0</td><td>1</td><td>form forum</td><td>4-6</td></tr><tr><td>fpr</td><td>for</td><td>0</td><td>1</td><td>fr</td><td>9</td></tr><tr><td>furst</td><td>first</td><td>3</td><td>1</td><td>frusta furs</td><td>4-19</td></tr><tr><td>hpe</td><td>hope</td><td>4</td><td>2</td><td>pH he</td><td>1-9</td></tr><tr><td>iedea</td><td>idea</td><td>4</td><td>1</td><td>idee</td><td>19</td></tr><tr><td>ih</td><td>in</td><td>0</td><td>1 to 5</td><td>hi</td><td>5</td></tr><tr><td>kelled</td><td>killed</td><td>4</td><td>1</td><td>keeled Kelley celled</td><td>6-8</td></tr><tr><td>lst</td><td>last</td><td>3</td><td>2 to 4</td><td>st</td><td>9</td></tr><tr><td>nd</td><td>and</td><td>0</td><td>1 to 2</td><td>Ned nod</td><td>5-8</td></tr><tr><td>neice</td><td>nice</td><td>2</td><td>1</td><td>niece</td><td>5</td></tr><tr><td>oa</td><td>of</td><td>0</td><td>1 to 4</td><td>au oak oaf</td><td>5-19</td></tr><tr><td>og</td><td>of</td><td>0</td><td>1 to 3</td><td>go Aug</td><td>0-17</td></tr><tr><td>oht</td><td>out</td><td>1</td><td>1</td><td>hot oh oho</td><td>3-8</td></tr><tr><td>olver</td><td>over</td><td>1</td><td>1</td><td>lover Oliver older</td><td>3-8</td></tr><tr><td>ou</td><td>you</td><td>0</td><td>1 to 4</td><td>au our out</td><td>2-9</td></tr><tr><td>psition</td><td>position</td><td>4</td><td>1</td><td>piston spittoon</td><td>16-28</td></tr><tr><td>ral</td><td>real</td><td>3</td><td>2</td><td>al rail rally</td><td>9-15</td></tr><tr><td>reating</td><td>rating</td><td>6</td><td>7</td><td>reassign reacting reading</td><td>3-26</td></tr><tr><td>resduced</td><td>reduced</td><td>6</td><td>1</td><td>rescued</td><td>15</td></tr><tr><td>sauares</td><td>squares</td><td>5</td><td>1</td><td>saucers soars</td><td>15-25</td></tr><tr><td>sedction</td><td>section</td><td>4</td><td>1</td><td>seduction sedation</td><td>6</td></tr><tr><td>solutions</td><td>solutions</td><td>6</td><td>1 to 2</td><td>sultans</td><td>37</td></tr><tr><td>syn</td><td>sun</td><td>3</td><td>1</td><td>sin sync sys</td><td>4-8</td></tr><tr><td>tlake</td><td>take</td><td>1</td><td>1</td><td>talkie talk</td><td>12-16</td></tr><tr><td>typ</td><td>top</td><td>3</td><td>1</td><td>tip type typo</td><td>4-5</td></tr><tr><td>wdo</td><td>who</td><td>1</td><td>2</td><td>do</td><td>0</td></tr><tr><td>yar</td><td>year</td><td>4</td><td>3 to 4</td><td>ear yard yarn</td><td>3-5</td></tr></table>

Column 4 gives the placement of $w ^ { * }$ in $L ( m )$ for SP, with ties indicated by $^ { 6 6 } \mathrm { t o } ^ { , 9 }$ . The last column gives g(w,m) for $L ( m )$ from MSW97. In the first row, $L ( m )$ was empty. Here, the role of $g ^ { + }$ becomes clear since in 8 of the 18 cases, $e _ { w } * _ { m } = 2$ . Also, the relatively small dictionary used by SP may have been an advantage, although it does seem striking that in 10 of the 18 cases, SP placed the correct word at worst tied for first in its list.

Only one word was not found by SP. The word was $m = p o l y t e c h n i q u e$ when $\begin{array} { r } { w ^ { * } = p o l y t e c h n i c . } \end{array}$ . It was not found since $e _ { w m } = 3$ . As mentioned earlier, this was also the only error undoubtedly not caused by mistyping in all the experiments!

## 4.3. Anomalies

As indicated in Section 1, the anomalies were compiled over time by the typing of the authors. There, we used a very loose definition of an anomaly but now, to us, it is the failure to offer a relatively common word with $e _ { w m } = 1$ , especially if less common words or those having $e _ { w m } > 1$ are offered. They are of particular interest to us because they would seem to indicate that the algorithm used by MSW97 does not resemble that of SP in the sense that it is based on a model using parameters similar to ours. Some of these anomalies are given in Table 5 along with the performance of $\mathrm { S P }$ on them. Note that if MSW97 were using a model based heavily on spelling rather than on typing, it would still be difficult to account for failure to correct the words forom, neice, and sulutions. SP correctly identifies all of these words with 23 out of 30 being at worst tied for first.

## 5. Conclusions and future research

The main contention of this paper is that a systematic and a model-based approach can provide a basis to improve the performance of spell checkers and other similar applications. We have introduced a model designed to help the spell checkers within word processors place the correct word at, or near, the top of the list of offered words. The proposed model also introduces the concept of ‘‘commonness’’ that incorporates the notion that if all else is equal, a more common word is more likely to be correct than a less common word. Based on the proposed model, a prototype spell checker has been developed, tested, and found to be quite accurate.

A number of issues deserve further investigation. An immediate extension is to expand the model to incorporate additional factors, including those related to spelling errors. Another useful avenue for further research is to explore customizing and learning possibilities, along the lines detailed in Section 2.3. Other application areas detailed in the paper, including query-by-humming techniques over music databases, can benefit from the model-based approach developed in the paper. With the growing use of online music, there is an important need to develop techniques for consumers to effectively search for and experience music offerings. We are currently working on some of these issues.

## Acknowledgements

The authors are grateful for the helpful comments of the referees and the area editor. The authors received support from TECI—The Treibick Electronic Commerce Initiative, Department of Operations and Information Management, University of Connecticut. The research of the first author was supported in part by Grant SAB94-0115 from the Spanish Interministerial Commission of Science and Technology. Computational resources were provided by the Booth Research Center for Computer Applications and Research of the University of Connecticut and by the Department of Statistics and Operations Research at the Polytechnic University of Catalonia, Spain. The authors are especially grateful to the students, staff, and faculty of the University of Connecticut who volunteered their time.

## References

[1] T.H. Cormen, C.E. Leirserson, R.L. Rivest, Introduction to Algorithms, MIT Press, Cambridge, MA, 1994.

[2] F.J. Damerau, A technique for computer detection and correction of spelling errors, Communications of the ACM 7 (1964) 171 – 176.

[3] R.S. Garfinkel, G.E. Liepins, A.S. Kunnathur, Error localization for erroneous data: a survey, TIMS Studies in the Management Sciences 19 (1982) 205– 219.

[4] J. Grudin, Error patterns in skilled and novice transcription

typing, in: W.E. Copper (Ed.), Cognitive Aspects of Skilled Typewriting, Springer-Verlag, New York, 1983, pp. 121–143.

[5] D.G. Hendry, T.R.G. Green, Spelling mistakes: how well do correctors perform? INTERACT ’93 and CHI ’93 Conference Companion on Human Factors in Computing Systems, Association for Computing Machinery, New York, 1993, pp. 83–84.

[6] International CorrectSpell. The web page at http://www.lhs. com/tech/icm/proofing/cs.asp (2000).

[7] D.E. Knuth, Sorting and searching, The Art of Computer Programming, vol. 3, Addison-Wesley, Reading, MA, 1973.

[8] K. Kukich, Techniques for automatically correcting words in text, ACM Computing Surveys 24 (1992) 378– 439.

[9] K. Kukich, Spelling correction for the telecommunication network for the deaf, Communications of the ACM 35 (1992) 80 – 90.

[10] S.B. Needleman, C.D. Wunsch, A general method application to the search of similarities in the amino acid sequence of two proteins, Journal of Molecular Biology 48 (1970) 443 – 453.

[11] J.L. Peterson, Computer programs for detecting and correcting spelling errors, Communications of the ACM 23 (1980) 676 – 684.

[12] A.B. Robertson, P. Willett, Searching for Historical Word-Forms in a Database of 17th Century English Text Using Spelling-Correction Methods, 15th Annual International SIGIR, Denmark, Association for Computing Machinery, New York, 1992, pp. 165 – 256.

[13] Y. Tsao, A lexical study of sentences typed by hearingimpaired TDD users, Proceedings of the 13th International Symposium on Human Factors in Telecommunications, Turin, Italy, Information Gatekeepers Incorporated, Boston, MA, 1990, pp. 197– 201.

[14] A. Uitdenbogerd, J. Zobel, Melodic matching techniques for large music databases, Proceedings: ACM Multimedia, Orlando, Florida, Association for Computing Machinery, New York, 1999, pp. 57 – 66.

![](/api/attachments/X4C9ZDB9/fulltext/images/3f2e5e6b8c1bf559ca80b44d4ec8b43720816c6a4e8fb981d69989c9563fc34a.jpg)

Robert Garfinkel is Professor of Operations and Information Management in the School of Business, University of Connecticut. He was previously on the faculties of the Universities of Rochester and Tennessee. His theoretical research focuses on such operations research problems as integer programming, network flows, vehicle routing, facility location, and combinatorial optimization. His current applied interests are mainly in data secur-

ity and economic control of data streams in networks. His research has appeared in Operations Research, Management Science, INFORMS Journal on Computing, Mathematical Programming, Networks, Journal of ACM, Transportation Science, and other journals. He has also published the book ‘‘Integer Programming’’.

![](/api/attachments/X4C9ZDB9/fulltext/images/947959e46d57a1e1c6452d27800509bdfb79ae588963c7ff3b672445b8598269.jpg)

Elena Fernandez is an Associate Professor in the Statistics and Operations Research Department at the Technical University of Catalonia in Barcelona, Spain. Her research interests include integer and combinatorial optimization, discrete location and routing problems, and application of metaheuristic methods to combinatorial optimization problems. Her papers have appeared in Operations Re-

search, European Journal of Operational Research, and other journals.

![](/api/attachments/X4C9ZDB9/fulltext/images/47f86425155d72fb567553bac97945634208edd9d451b0a9987506a297d7197c.jpg)

Ram D. Gopal is GE Capital Endowed Professor of Business and Associate Professor of Operations and Information Management in the School of Business, University of Connecticut. He currently serves as the PhD director for the department. His current research interests include economics of information systems management, data security, economic and ethical issues relating to intellectual property rights, and mul-

timedia applications. His research has appeared in Management Science, Operations Research, INFORMS Journal on Computing, Information Systems Research, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Decision Support Systems, and other journals and conference proceedings.
