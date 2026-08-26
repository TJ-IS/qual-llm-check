---
otero_id: 18936
otero_key: "MZ6B49PM"
title: "Quality control in software documentation"
authors: "Franz Lehner"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90036-s"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Quality control in software documentation Measurement of text comprehensibility

Franz Lehner

The Koblenz School of Corporate Management, Vallendar, Germany

The importance of software documentation and the effects of poor documentation in data processing are often underrated. Little research has been published that evaluates its quality. Software quality, on the other hand, is almost a buzzword. Discussions of software quality measurement often make reference to software documentation; however, the literature on the subject of software quality assurance has offered little adequate operationalization or usable instrument for quality measurement and quality control in software documentation. The paper provides a presentation of existing comprehensibility measures for texts and an inventory of available tools, a summary of experience with comprehensibility measures and tools published in the literature, the development of a tool for the computation of readability formulae, and the application of these measurement methods to software documentation in the context of an explorative case study.

Keywords: Documentation quality; Quality; Quality control; Quality measures; Readability; Software documentation; Text comprehensibility; Text comprehension

![](/api/attachments/MZ6B49PM/fulltext/images/b359b264e750419c6098d5f7b5659eed42d9cf4fc4b50fc2e06813ced55f10d1.jpg)

Franz Lehner, born in 1958, has been assistant at the Institute for Organizational Research at the University of Linz, Austria, since 1986. Before this he gathered experience in the field of EDP as head of the educational center at a software house and as an independent consultant. He specialises in the management of computer applications, the development of informatic strategies, and the effects of technological change on organisational structures. Since 1993 he is professor for business informatics and information management at the Koblenz School of Corporate Management. Correspondence to: F. Lehner, Institute for Business Informatics, The Koblenz School of Corporate Management, Burgplatz 2, D-76179 Vallendar, Germany.

## 1. Introduction

Documentation – as an activity and as the result of an activity – is increasingly being integrated into the process of software development or into the resulting software product. Regardless of the increasing use of new media and documentation methods due to integration of documentation, the importance of textual documentation, i.e., handbooks, functional descriptions, tutorials, “help” features, etc., is not expected to decline. The evaluation of textual attributes, such as comprehensibility, readability, etc. has seen a larger number of papers providing relatively sound results. Thus this paper exclusively handles textual documentation.

## 1.1. Task description and goals

Software documentation includes program and system documentation and the entire spectrum of user documentation (e.g., user handbooks for commercial software, tutorials and reference cards). Inasmuch as the operationalization of quality attributes is possible, quality metrics can improve the objective evaluation of software documentation quality. Readability formulae make a contribution in this area.

1.2. Approaches to the measurement of text comprehensibility

There are numerous approaches and studies on effective text writing and on the measurement of text comprehensibility. Most conceptions are based, to varying degrees, on two perceptions: text comprehensibility as a characteristic of the text and as a characteristic of the reader. Overviews, summaries and references to in-depth literature can be found in the cited references [e.g., 12,21]. We distinguish the following research results:

\- Cloze Tests. These can be viewed as a special case of the completion method introduced by Ebbinghaus, a recognized psychological test method. The name is derived from the “closure construct” of Gestalt psychology, i.e., a human characteristic that permits us to complete familiar but incomplete characters. In its most general form the method employs systematic deletion of individual words in a representative text excerpt that is presented for completion. Cloze Tests are distinguished from fill-in-the-blank tests in which precisely specified words or groups of words are deleted. The best-known example of a Cloze Test is Taylor’s Cloze Procedure.

\- Comprehensibility formulae. The readability and comprehensibility of texts is determined by measures of degree of formal, lexical, and syntactic text attributes. These approaches are normally based on study results that show that shorter words are more common than longer ones or that the sentence length influences text comprehensibility, etc. Likewise the vocabulary and results of information theory studies of the limited assimilation capacity of the human brain are frequently used in this context. Examples of this approach are Flesch's Reading Ease, Dale/Chall's Readability Index and Gunning's Fog Index.

\- Ordering of information. The measurement of comprehensibility on the basis of word or syllable count neglects the organization as an important element in creating text. This deals with cognitive structures and leads to a recommendation to include an introduction (advance organizer) and to present the content by moving from the general to the specific (sequential arrangement). There are no known measures for determining text comprehensibility for this.

\- Use of specialized media. The influence of repetition in text, comprehension questions, etc. are considered here. Empirical results support the use of such media; however, no concrete measures are available generally.

\- Intuitive application of experience. This type of approach is free from experimental influences. A relatively high degree of recognition has been attained by “Reiners’ dos and don’ts of style”. He also attempted to measure the comprehensibility of texts. This was done with four variables whose results are shown in Table 1. Text passages of 100 words form the basis of computation. The overall comprehensibility is calculated by averaging the four individual values.

\- Impression methods. These methods are closely coupled with the process of reading itself. The evaluation takes place by means of subjective impressions. The method of Langer et al. can be cited as an example; it is also known as the Hamburg comprehensibility concept. The comprehensibility is established by means of evaluation of four text attributes (simplicity, organization, brevity/pregnancy, and additional stimulation) by specially trained test persons.

\- Interrelation of text and reader attributes. Text comprehensibility with this approach uses certain text attributes with relation to a given recipient. The Groeben method serves as an example.

Groeben's theoretical approach is oriented toward cognitive theories, whereby text comprehension is viewed as “active cognitive construction of a semantic structure”. The comprehension is seen as an interaction between the reader and the text. Groeben derives his questioning perspectives therefrom:

Table 1  
Measurement of comprehensibility on the basis of four variables by Reiners [source: 17]

<table><tr><td></td><td>words/sentence</td><td>active verbs</td><td>personal names</td><td>abstract nouns</td></tr><tr><td>1. Very easily comprehensible</td><td>1-13</td><td>over 14</td><td>over 12</td><td>0-4</td></tr><tr><td>2. Easily comprehensible</td><td>14-18</td><td>13-14</td><td>10-11</td><td>5-8</td></tr><tr><td>3. Comprehensible</td><td>19-25</td><td>9-12</td><td>6-9</td><td>9-15</td></tr><tr><td>4. Hard to comprehend</td><td>25-30</td><td>7-8</td><td>3-5</td><td>15-20</td></tr><tr><td>5. Very hard to comprehend</td><td>over 30</td><td>0-6</td><td>0-2</td><td>over 20</td></tr></table>

![](/api/attachments/MZ6B49PM/fulltext/images/b09ed24c5af3d57c209b0afbd643aca78bae6200ecfd995aafc3ae502c2182fc.jpg)  
Fig. 1. Decomposition of quality attributes according to Arthur/Stevens.

\- Individual text comprehension. Which processes in text comprehension occur relatively uniformly for all texts and independent of reader attributes?

\- Intercultural text comprehensibility. Which processes in text comprehension occur relatively uniformly for all texts but dependent on reader attributes?

The concept of text comprehension thus considers the influence of reader attributes, while text comprehensibility describes the influences of text attributes on the comprehension process. In order to improve text comprehension, Groeben introduces a set of aids and techniques that are intended to have the following results: improvement of sensual perception, speed-reading, adaptive reading, critical/creative reading, and self-controlled text processing. Text comprehensibility is evaluated with these concepts, based on four text dimensions that can be justified theoretically and empirically:

\- Cognitive structuring (prestructuring, advance organizer, sequential arrangement of text content, summarizing, accenting and underlining, headlines and marginal notes, questions, learning goals, etc.).

\- Linguistic simplicity and semantic brevity (short, common, concrete, attractive and personal words; clarity via examples, graphics and figures; short and grammatically simple sentences, etc.).

\- Redundancy.

\- Stimulating cognitive conflict (incongruent reference to the familiar, contradictory alternatives, novelty and surprise, incoherence and complexity, etc.).

Newer approaches attempt to overcome the limits of classical comprehensibility concepts in two ways; they attempt to incorporate both reader (learner) and text attributes in concepts of text comprehensibility. Also, these approaches are based on the state of knowledge in the field of text comprehension (i.e., processing attributes). The many and sometimes contradictory results of studies thus provide a basis for the development of global comprehensibility concepts.

One approach that specifically treats software documentation and defies classification in the above list is that of Document Quality Indicators (DQIs) by Arthur/Stevens [1]. This revolves around two questions: What makes up appropriate documentation, and how can appropriateness be measured? A study of these questions led to the formulation of a general taxonomy for the evaluation of computer documentation. This is described by a tri-level model in the form of a tree. Figure 1 shows the decomposition of the quality attributes into factors and quantifiable measures. Details can be found in [25].

## 2. Methods for the measurement of documentation quality

## 2.1. Comprehensibility and readability of texts

The definition of a suitable quality measure for documentation is difficult. Everyday experience indicates, and numerous studies verify, that various texts covering the same content achieve differing degree of being understood and remembered. What is perceived as comprehensible varies by person, yet there are several factors that can generally detect weak points in a given text. Characteristics include [22]:

\- vocabulary; appropriate to the knowledge of the user, unfamiliar concepts should be defined or a definition should be locatable.

\- sentence structure; simple sentence structure, avoidance of long sentences and nested clauses.

\- sequence of presentation of information; first the basics, then increasing in degree of difficulty, etc.

\- use of examples; e.g., for explanation of abstract concepts.

Some factors that have an influence on the comprehensibility of documentation can be determined objectively, i.e., by means of counting or measurement. These include word length (e.g., syllable count), sentence length (number of words per sentence), and the structure of the sentences. Readability formulae and readability indices often use average word length and average sentence length for the determination of the readability or of the comprehensibility [e.g., 24].

## 2.2. Flesch's reading ease

Flesch devised one of the first approaches to measuring text comprehensibility with a weighted combination of sentence length and word length [7]. Word length is measured as the average number of syllables; sentence length is the average number of words. As a rule, the entire text is not measured; instead, one or more text passages of approximately 100 words are selected. The readability formula is:

$$
\begin{array}{r l} \text { Reading   ease } & = 2 0 6. 8 5 - 0. 8 4 6 * \text { WL } \\ & - 1. 1 0 5 * \text { SL }, \end{array}
$$

where

WL = average word length,

SL = average sentence length.

The constants 0.846 and 1.105 are the empirically determined weights for the combination of sentence length and word length.

## 2.3. Fog index

A relatively well-known measure of documentation quality is the fog index, introduced by Gunning [10]. It was developed to measure the degree of readability of software documentation written in natural language. The fog index is used as an indicator of the comprehensibility of the text. The lower the value, the less the complexity of the text and the less difficulty the reader should have in reading and understanding it.

The fog index is defined as follows:

$$
\mathrm{F} = 0. 4 * (\mathrm{W} + \mathrm{L}),
$$

W = average sentence length computed from the total number of words in a statistically selected text excerpt of 100 to 200 words, divided by the number of sentences.

L = percentage of long words in the total number of words; all words with three or more syllables are considered to be long; proper nouns are excepted, as are verb forms with “-ed” and “-es” endings.

The fog index can be computed with little effort and without software support. First the text excerpts are selected (ca. 100 words). Random selection takes one text passage per four pages; the selection must begin and end with a complete sentence. The simplicity of the formula, the clear instructions for its use, and the standardization of the readability levels help to assure the objectivity of this readability measure.

## 2.4. Cloze Procedure

Understanding of text can be determined by means of Cloze Tests $[11]$ . These tests delete words at regular intervals in the text and replace them with blanks. They are also known as $5 + 5$ tests because five text passages are often randomly selected from the entire text, and every fifth word is blanked $[3]$ . The test reader attempts to fill in the blanks with the correct words. The number of errors is a measure of how well the text has been understood.

The Cloze Procedure was developed by Taylor [26]; it was originally employed in the field of journalism. Later the Cloze Procedure proved to be an efficient method for testing the comprehensibility of literary texts in the fields of translation and literature. It is necessary that the test readers understand both the meaning and the form of the individual words, and the context of the text passage; i.e., that they understand the meaning of the whole text.

The subjects, who should be a representative sample of potential readers, receive a copy of the prepared text and are instructed to fill in the missing words. There is no time limit, but the text should be filled in relatively quickly. The time could be the first indicator of the comprehensibility and readability of the original text.

The evaluation of the completed test forms determines how often how many persons filled in the correct word. Only the exact word is construed as correct, and synonyms – per the developer of the procedure – are not accepted. The more often the correct word was inserted, the more readable the text is construed to be. The greater the number of the test persons, the more stable the results. Places left blank are considered incorrect. The frequency of occurrence of blanks also provides an indicator of the readability and comprehensibility of the original text.

The results are evaluated by calculating the comprehensibility coefficient p as follows: The number of subjects is multiplied by the number of blanks in the text. The total number of correct substitutions is then divided by this product to yield p. See Figure 2. The comprehensibility coefficient represents the percentage of the text that the readers understood.

<table><tr><td></td><td>Number of omissions per text</td><td>Total number of correct substitutions</td><td>Number of test persons</td><td>p</td></tr><tr><td>Text A</td><td>43</td><td>225</td><td>8</td><td>0.654</td></tr><tr><td>Text B</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Fig. 2. Sample for representing results in the Cloze Procedure.

## 2.5. Flesch / Kincaid index

The Flesch/Kincaid index is a formula for the determination of readability on the basis of the number of syllables. The lower the index, the easier it is for the reader to understand the text. Depending on the length of the text, index values for text excerpts of about 100 words are computed and the average is calculated. The index can be determined for the entire document. Selection of one text excerpt per ten pages is recommended.

The Flesch/Kincaid index is [14,23]:

$$
\begin{array}{r l} \mathrm{FKindex} & = 0. 3 9 * (\mathrm{W/S}) + 1 1. 8 * (\mathrm{Si/W}) \\ & - 1 5. 5 9, \end{array}
$$

where

W = number of words in text excerpt,

S = number of sentences in text excerpt,

Si = number of syllables in text excerpt.

The domain ranges from 1 (= very simple and easily comprehensible) to about 20 (= very difficult). There are no recommendations on the best index value for a document; it depends on the readership. For example, training documents for a Saudi Arabian naval unit required that the value 7 not be exceeded. The index is often used in the U.S. Department of Defense (DoD) for user handbooks and training material and is their official standard. The Flesch/Kincaid index is recommended only for English texts. There is neither an adapted version nor experience in using it on German language texts. The computed index value is only a very general indicator for the degree of difficulty of a text. However, it can help an author to aim a text at a particular readership.

## 2.6. Steiwer's readability formulae

Steiwer developed her readability formulae especially for German texts for testing and improving the readability of schoolbooks and learning materials. The “computer readability formula” and the “shortcut readability formula” (a simplified variant that can be computed manually with acceptable effort), also seem to be suitable for application to software documentation [5]. Computer formula:

$$
\begin{array}{r l} \mathrm{V} ^ {*} = 1 9 9. 5 3 4 4 5 - (\text { Var2 } * 6 4. 1 3 4 8 6) \\ & - (\text { Var1 } * 1 1. 7 3 9 1 6) - (\text { Var15 } * 0. 8 9 6 5 1) \\ & - (\text { Var3 } * 1 9. 9 4 5 0 8) + (\text { Var8 } * 0. 7 1 9 1 5) \\ & + (\text { Var9 } * 1. 8 5 7 7 6), \end{array}
$$

Shortcut formula:

$$
\begin{array}{r l} \mathrm{V} ^ {*} = 2 3 5. 9 5 9 9 3 - (\text {Var2} * 7 3. 0 2 1) \\ & - (\text {Var1} * 1 2. 5 6 4 3 8) - (\text {Var3} * 5 0. 0 3 2 9 3), \end{array}
$$

where

$$
\operatorname{Var} 1 = \ln ((\text { AWOR } / \text { ASAT }) + 1),
$$

$$
\operatorname{Var} 2 = \ln ((\mathrm{ABUC/AWOR}) + 1),
$$

$$
\text { Var3 } = \text { AUWO / AWOR },
$$

$$
\text { Var8 } = (\text { APDR / AWOR }) * 1 0 0,
$$

$$
\operatorname{Var} 9 = \ln \left(\left(\text { (APEZ   /   AWOR) } * 1 0 0\right) + 1\right),
$$

$$
\text { Var15 } = (\text { APRA / AWOR }) * 1 0 0,
$$

$$
\mathrm{AWOR} = \text { number   of   words },
$$

ASAT = number of sentences,

ABUC = number of letters,

AUWO = number of different words (all derivations of a word and declined or conjugated word forms, etc., are valued as different),

APDR = number of personal pronouns in the third person,

APEZ = number of personal pronouns in the first and second persons,

APRA = number of prepositions.

The comprehensibility V' is represented by a value on the ordinal scale between 1 and 100. The higher this value, the more comprehensible the text. As yet there are no empirical data or values in the field of software documentation. The exact measurement guidelines practically preclude subjective influence.

## 2.7. Farr / Jenkins / Patterson's new reading ease index

Farr et al. developed a simplified formula based on Reading Ease. This requires only determination of the number of monosyllabic words and is computed as $[6,2]$ :

New Reading Ease index = 1.599 \* NOSW

$$
- 1. 0 1 5 \mathrm{SL} - 3 1. 5 1 7,
$$

where

NOSW = percentage of words with one syllable,
SL = average sentence length in words.

## 2.8. Automated readability index (ARI) by Smith / Kincaid

The Automated Readability Index (ARI) is derived from the relationship between attributes that reflect the degree of difficulty of words (number of letters per word) and of sentences (number of words per sentence). The ARI is a quantitative readability measure. Studies of its reliability and validity had positive results and demonstrated its practicality.

The formula was derived using regression equations for determination of grade level for reading in the American school system (junior high school, senior high school, etc.):

$$
\mathrm{GL} = 0. 5 * (\mathrm{WS}) + 4. 7 1 * (\mathrm{SW}) - 2 1. 4 3.
$$

The following simplified formula correlates with the readability of the text, but does not indicate the correlating grade level [23]:

$$
\mathrm{ARI} = \mathrm{WS} + 9 * \mathrm{SW},
$$

where

WS = average number of words per sentence (sentence length),

SW = average number of letters per word (word length).

## 3. Tools for the measurement of readability of texts

Most tools for the automatic measurement of readability of texts originated in the 60s and 70s, when questions of readability and comprehensibility were of interest. Few of the studies and applications treated software or software documentation; the best-known example that did is Gunning's fog index. No new tools have evolved. Meanwhile the subject of quality assurance for software documentation has gained importance. New methods need to be developed or existing methods need to be adapted.

## 3.1. Overview of existing tools

There are a number of tools that support automation and allow the analysis of sentence structures; i.e., the use of certain words, passive constructs, etc. can be detected. Examples include Readability by the Encyclopedia Britannica Educational Corporation and Epistle by IBM. Their comments and results deal with the lack of agreement in person between subject and verb, inconsistency in tense, singular and plural, unconventional phrases, ambiguous references, etc. We limit the selection of tools to ones that are able to compute concrete readability indices (but do not give suggestions for revising the text). Our literature study produced surprisingly few references. Some additions are $[8,4]$ .

\- At California State University Barry developed a Fortran program that supports the computation of the following formulae: Dale/Chall's readability index, fog index, Flesch's Reading Ease, Spache's readability index, Farr/Jenkins/Patterson's New Reading Ease index, and the Spaulding index (for Spanish texts).

\- Danielson/Bryan created a program for the computation of the Farr/Jenkins/Patterson index, an adaption of Reading Ease.

\- The program Star was written in Basic at the Human Engineering Laboratory of the US Army and computes the Flesch Reading Ease.

\- The Readability Assessment Program is a General Motors Corporation product and computes the Flesch/Kincaid index.

\- CRES (Computer Readability Editing System) calculates the Flcsch/Kincaid index and also contains a Dale/Chall list, i.e., a dictionary with approximately 4300 generally used words, as well as three additional lists of technical terms. These latter lists serve to identify less-used words.

\- The ARI program was developed for the Lockheed-Georgia Company and calculates the Automated Readability Index.

\- The Writer's Workbench by Bell Laboratories was developed for Unix systems and calculates the Flesch/Kincaid index.

These systems are technically antiquated today, but they can provide ideas for the structure of new applications.

## 3.2. Development of a new tool with hypercard

The need for a new tool is indicated by the inadequate portability and the low level of recognition of the mentioned systems. The tools were mainly developed on old hardware. Other disadvantages include the limited number of implemented methods, the form of evaluation, and the restricted manipulability of texts.

The user interface for accessing texts is important. We assume that the texts are already in machine-readable form or can be scanned with little manual intervention (correction of unrecognized characters or of errors).

![](/api/attachments/MZ6B49PM/fulltext/images/60796b1ad23700db52f663fc4b039afa77b6a723c8a2e580b88566194b307986.jpg)  
Fig. 3. Start card for RMS.

![](/api/attachments/MZ6B49PM/fulltext/images/c2e1a2fc13348638efb0ff3b248893973bb80f48a712f43546f9e58a62e74985.jpg)  
Fig. 4. Overview representation of the computed readability indices.

## 3.3. RMS - Readability measuring system

As the target system for RMS we chose the Apple Macintosh; our development environment was Hypercard. The development of the tool took place in two phases:

\- Phase 1: development of a functional prototype.

\- Phase 2: improvement of the operation and functionality, extension to provide further readability formulae, help text, improved maintenance.

Experience in the first tests with the prototype version led to several modifications and improvements. Errors were corrected, but the functionality was extended to facilitate the application of RMS. One important goal was to make the system self-explanatory. At this time RMS supports the following functions:

![](/api/attachments/MZ6B49PM/fulltext/images/56438f3202b080d720bb71fe8bdea5320de8aaa9f60257c6d8a27bf49d1a55d7.jpg)  
Fig. 5. Generation of a fill-in-the-blank text with RMS.

\- input and management of the text samples,

\- preparation of the text samples for further processing (support of syllable count),

\- determination of parameters (number of characters, letters, words, sentences, long words, varying words, etc.) for the implemented readability indices,

\- computation of the readability indices,

\- presentation of the results in a comparative overview,

\- generation of fill-in-the-blank texts (complete with the substitution list) as a basis for the execution of Cloze Tests.

Figs. 3 to 5 give a general impression of the functionality and use of RMS. Further details can be found in the literature [see 18].

## 4. Study results

## 4.1. Procedure and selection of the documents

A primary goal of this study was to examine readability measures: their practicality for quality testing of software documentation. Language-specific modifications of the formulae are precluded, because no new revelations are anticipated in the field of language research, and the application of readability formulae to other fields has already been well researched.

Four user handbooks were selected for testing. Two were provided by a large Austrian software house, the other two were the English and the German handbooks to Microsoft Word. A comparison of the language-specific formula characteristics between the two versions was planned. However, the German version was not a direct translation of the English handbook, so that the planned comparison was not carried out. The first two handbooks were recommended by experts at the software house as “easily readable” (AIS Bookkeeping) and poor documentation (HP Financial Bookkeeping). This evaluation showed the subjective character of expert opinions. The author views all four handbooks as typical and considers them all relatively poor.

For all studies and measurements, the same documentation material was used. The selection of the text samples was random. The selected text passages were scanned and the character recognition errors were first corrected. Further processing and evaluation was done with the tool support of RMS after the text files were transferred to RMS.

## 4.2. Results for the measurement of text comprehension

In selecting the Cloze Procedure as a method to measure readability, it was clear that this method only returns empirical hints on the intentions of the author. The method was carried out with omission of every sixth word. In order to safeguard the validity of the results, the tests were repeated starting at a different word. This was intended to preclude the random omission of particularly difficult words.

Table 2  
User handbook for AIS Bookkeeping

<table><tr><td>text sample</td><td>114A</td><td>137A</td><td>148A</td><td>217A</td><td>51A</td><td>59A</td><td></td></tr><tr><td>number of test person</td><td>5</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td></td></tr><tr><td>number of blanks</td><td>22</td><td>25</td><td>28</td><td>42</td><td>27</td><td>27</td><td></td></tr><tr><td>correct substitutions</td><td>55</td><td>92</td><td>76</td><td>138</td><td>88</td><td>100</td><td></td></tr><tr><td>p</td><td>50.00%</td><td>61.33%</td><td>45.24%</td><td>54.76%</td><td>54.32%</td><td>61.73%</td><td></td></tr><tr><td>text sample</td><td>114B</td><td>137B</td><td>148B</td><td>217B</td><td>51B</td><td>59B</td><td>total / average</td></tr><tr><td>number of test persons</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>5.916</td></tr><tr><td>number of blanks</td><td>22</td><td>25</td><td>27</td><td>42</td><td>27</td><td>27</td><td>28.416</td></tr><tr><td>correct substitutions</td><td>79</td><td>83</td><td>71</td><td>136</td><td>71</td><td>83</td><td>89.333</td></tr><tr><td>p</td><td>59.85%</td><td>55.33%</td><td>43.83%</td><td>53.97%</td><td>43.83%</td><td>51.23%</td><td>53.13%</td></tr></table>

Table 3  
User handbook for HP Financial Bookkeeping

<table><tr><td>text sample</td><td>2-3A</td><td>3-39A</td><td>3-19A</td><td>3-11A</td><td>3-16A</td><td>3-3A</td></tr><tr><td>number of test persons</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td></tr><tr><td>number of blanks</td><td>36</td><td>42</td><td>49</td><td>23</td><td>40</td><td>46</td></tr><tr><td>correct substitutions</td><td>89</td><td>128</td><td>146</td><td>52</td><td>140</td><td>135</td></tr><tr><td>p</td><td>41.20%</td><td>50.79%</td><td>49.66%</td><td>37.68%</td><td>58.33%</td><td>48.91%</td></tr><tr><td>text sample</td><td>3-31A</td><td>3-61A</td><td>4-34A</td><td>4-44A</td><td></td><td></td></tr><tr><td>number of test persons</td><td>6</td><td>6</td><td>6</td><td>6</td><td></td><td></td></tr><tr><td>number of blanks</td><td>28</td><td>40</td><td>48</td><td>23</td><td></td><td></td></tr><tr><td>correct substitutions</td><td>99</td><td>141</td><td>109</td><td>94</td><td></td><td></td></tr><tr><td>p</td><td>58.93%</td><td>58.75%</td><td>37.85%</td><td>68.12%</td><td></td><td></td></tr><tr><td>text sample</td><td>2-3B</td><td>3-39B</td><td>3-31B</td><td>3-61B</td><td>4-34B</td><td>4-44B</td></tr><tr><td>number of test persons</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td></tr><tr><td>number of blanks</td><td>36</td><td>42</td><td>49</td><td>23</td><td>40</td><td>40</td></tr><tr><td>correct substitutions</td><td>89</td><td>128</td><td>146</td><td>52</td><td>140</td><td>140</td></tr><tr><td>p</td><td>41.20%</td><td>50.79%</td><td>49.66%</td><td>37.68%</td><td>58.33%</td><td>58.33%</td></tr></table>

Table 4  
Microsoft Word zum Nachschlagen (German, Version 4)

<table><tr><td>text sample</td><td>D125c</td><td>D342c</td><td>D18c</td><td>T497C</td><td>A49C</td><td></td></tr><tr><td>number of test persons</td><td>7</td><td>5</td><td>8</td><td>3</td><td>6</td><td></td></tr><tr><td>number of blanks</td><td>29</td><td>36</td><td>39</td><td>30</td><td>24</td><td></td></tr><tr><td>correct substitutions</td><td>97</td><td>94</td><td>158</td><td>63</td><td>79</td><td></td></tr><tr><td>p</td><td>47.78%</td><td>52.22%</td><td>50.64%</td><td>70.00%</td><td>54.86%</td><td></td></tr><tr><td>text sample</td><td>D18d</td><td>D49d</td><td>S342D</td><td>DI2SD</td><td>T497D</td><td>total / average</td></tr><tr><td>number of test persons</td><td>10</td><td>8</td><td>6</td><td>6</td><td>8</td><td>6.7</td></tr><tr><td>number of blanks</td><td>39</td><td>24</td><td>36</td><td>30</td><td>29</td><td>31.6</td></tr><tr><td>correct substitutions</td><td>182</td><td>101</td><td>99</td><td>92.</td><td>138</td><td>110.3</td></tr><tr><td>p</td><td>46.67%</td><td>52.60%</td><td>45.83%</td><td>51.11%</td><td>59.48%</td><td>52.10%</td></tr></table>

Table 5  
Microsoft Word Made Easy for the Macintosh (English, 3rd edition)

<table><tr><td>text sample</td><td>F1</td><td>F2</td><td>F3</td><td>F4</td><td>F5</td><td></td></tr><tr><td>number of test persons</td><td>14</td><td>13</td><td>10</td><td>11</td><td>9</td><td></td></tr><tr><td>number of blanks</td><td>48</td><td>56</td><td>64</td><td>33</td><td>45</td><td></td></tr><tr><td>correct substitutions</td><td>191</td><td>307</td><td>217</td><td>156</td><td>137</td><td></td></tr><tr><td>p</td><td>28.42%</td><td>42.17%</td><td>33.91%</td><td>42.98%</td><td>33.83%</td><td></td></tr><tr><td>text sample</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>ES</td><td>total / average</td></tr><tr><td>number of test persons</td><td>6</td><td>7</td><td>9</td><td>8</td><td>9</td><td>9.6</td></tr><tr><td>number of blanks</td><td>47</td><td>57</td><td>63</td><td>33</td><td>44</td><td>49</td></tr><tr><td>correct substitutions</td><td>112</td><td>133</td><td>232</td><td>92</td><td>164</td><td>174.1</td></tr><tr><td>p</td><td>39.72%</td><td>33.33%</td><td>40.92%</td><td>34.85%</td><td>41.41%</td><td>37.01%</td></tr></table>

The subjects were juniors and seniors in business informatics at the University of Linz. They were assumed to have sufficient knowledge in the field to fill in the blanks. In addition, most of them used Microsoft Word in their daily work. The results are depicted in detail in Tables 2 to 5.

The evaluation of the results raises the question: what percentage of correct words is to be expected? One normally distinguishes texts that are intended to be used independently and texts that are used with instruction. In the former, a threshold of 57% is recommended, and in the latter 44% [9]. Since a user handbook normally is used without instruction, the higher threshold of 57% was assumed. This level is not attained in any of the cases here (the averages were between 50% and 53%). The English Microsoft Word manual is significantly lower (37%); this could also reflect the mastery of English of the test persons. For various reasons Guillemette uses the lower 44% threshold in a study of Cobol handbooks. Given this criterion, the documents in this study can be said to at least attain adequacy in comprehension. Although the texts are usable, the test results indicate room for linguistic improvement.

## 4.3. Results for the measurement of text comprehensibility

A large number of studies have been carried out, especially in the Anglo-American area. The computation of all the values took place without consideration of headlines and subheadlines.

Flesch's Reading Ease normally assumes values between 100 (optimal comprehensibility) and 0 (minimal comprehensibility). Most of the formulae were developed for English texts and thus are valid only for English. Reading Easc was applied in unmodified form to the German language; this caused a shift of the evaluation due to the longer average word length in German. Table 6 shows the comparison for German and English texts.

The evaluation tables show that all studied texts are rated as difficult to very difficult, even if very high variances are employed. The English Microsoft Word handbook with its index value of

Table 6  
Reading Ease values for German and English texts

<table><tr><td>test characteristic</td><td>German texts</td><td>English texts</td><td>word length</td><td>sentence length</td></tr><tr><td>very difficult</td><td>-20 to +10</td><td>0 to 30</td><td>&gt;2.2</td><td>&gt;30</td></tr><tr><td>difficult</td><td>10 to 30</td><td>30 to 50</td><td>1.9</td><td>25</td></tr><tr><td>challenging</td><td>30 to 40</td><td>50 to 60</td><td>1.78</td><td>21</td></tr><tr><td>normal</td><td>40 to 50</td><td>60 to 70</td><td>1.7</td><td>17</td></tr><tr><td>simple</td><td>50 to 60</td><td>70 to 80</td><td>1.62</td><td>14</td></tr><tr><td>easy</td><td>60 to 70</td><td>80 to 90</td><td>1.54</td><td>11</td></tr><tr><td>very easy</td><td>70 to 80</td><td>90 to 100</td><td>&lt;1.45</td><td>&lt;9</td></tr></table>

64 has a normal level of difficulty. This corresponds to the subjective evaluation of experts and can be seen as an indicator that Reading Ease should only be used with caution for German-language texts.

Boehm et al. consider a fog index between 12 and 16 for specifications and technical reports to be acceptable. Gunning himself recommends the fog index not as a rigid formula but as a warning system; values over 12 are considered to be in the danger zone. With this as a basis for the interpretation of the measurement results, the computed values between 6.2 and 7.4 indicate average comprehensibility.

Budde notes that the fog index needs to be language-adapted before it can be used for testing or improving software documentation in German. The adaptation to German-language texts could be achieved either by modifying the evaluation scale (with unchanged formula) or modifying the formula itself. Such an adaptation was not undertaken. This study indicates no difference in index value between German-language texts and English texts. This tends to indicate that only the value range, but not the formula, needs to be adapted.

Values for the Flesch/Kincaid index range from 1 (very simple and easily comprehensible) to approximately 20 (very difficult). There are no recommendations as to what index value should be attained for a document. The calculated index value according to Kincaid et al. is only a very general indicator of the degree of difficulty of a text. However, it can help the author to match a text to the target group. The computed average for the English Microsoft Word handbook was 8.65 (variance 0.9), and this agrees with other results.

The application of the Flesch/Kincaid index is recommended only for English texts. Values computed here were between 15 and 20 with little variance. As with the fog index, this can be seen as an indicator that the adaptation of the formula alone suffices.

The comprehensibility V\* according to the Steiwer Readability Formula, which was especially developed for German-language texts, returns a value on the ordinal scale that is normally between 1 and 100. Considering the variances, the German-language samples varied between 6 and 20. Since this formula was developed especially for German texts, the low level of comprehensibility is seen as particularly significant. An interpretation of the index values for English texts is not viewed as practical.

The Farr/Jenkins/Patterson New Reading Ease index represents a simplification of the Flesch Reading Ease and it may be interpreted analogously: the higher the computed value, the more comprehensible the text. The computed index values show a high degree of correlation with Reading Ease.

For the Smith/Kincaid Automated Readability Index (ARI), a high index value indicates a high level of difficulty. In a study carried out by Smith/Kincaid, the index assumes a value around 50 for simple texts, for medium difficulty around 60, and for difficult texts over 70. In this study the index value 58 was calculated for the English Microsoft Word handbook. This indicates medium difficulty.

The number of syllables, which is strongly language-specific, is not used to calculate the ARI, so that this measure can be viewed as language-independent. This is also seen in the results of the German-language text samples, which demonstrate a correlation between the ARI and the Readability Formula of Steiwer. The computed index value is, however, on average 15 points higher for German texts (ca. 75). This can be seen as a correlation to the value of the Steiwer formula, but the value range may have shifted.

In summary, readability formulae are limited to the linguistic surface structure of texts. They evaluate texts with respect to their linguistic difficulty. The most constructive potential application is to derive instructions for writing and linguistic formulation. The anticipated language-specific differences were mainly confirmed. The sensitivity of the individual formulae varies. The computed index values represent a uniform and stable group of results and confirm that readability formulae are a useful instrument for quality testing.

## 4.4. Consequences

The problems resulting from poor software documentation are generally known today. The results of this study should not give the impression that documentation quality can be reduced to quantitative measures: it is an initial step toward comprehensive operationalization. The measurement and analysis of quantitative quality attributes can already be seen as an instrument for achieving an appropriate quality niveau. Understandably, even less reports are available on tool support in the measurement of documentation quality.

Cloze Tests are among the most-studied methods in the area of comprehensibility testing. The suspicion that a high recognition rate in the Cloze Procedure indicates low information content of the text could be raised, along with other criticisms. A high degree of correlation to other readability measures has been shown. Since the end of the 60s Cloze Tests have generally been recognized as a predictive measure of the readability of prose texts. Since the Cloze Items themselves are part of the text, the influence of the formula of the measuring procedure is avoided.

Readability formulae are usually regression equations whose variables represent certain linguistic or stylistic text attributes (the surface structure of a text). Many of these variables correlate well with difficulty in text comprehension. The best single indicator is usually considered to be the vocabulary (normally measured in terms of how unusual or difficult the words are), variety of words, and word length. A second important indicator is the sentence structure, whereby sentence length is the usual measurement.

Readability indices cannot measure how well a text is really understood. Thus some authors doubt whether such values return adequate predictability of comprehensibility [20]. The most frequent criticisms include:

\- The formula does not consider proveable reader-specific factors, such as intelligence, motivation, competence, expectations, maturity, and experience. The usefulness of the formulae strongly depend on the basic assumptions about the target group and purpose of the texts.

\- The formulae concentrate on easily quantifiable stylistic text attributes. Other important factors such as content, organization and text preparation, format, length, density, and explanations are neglected.

\- The difficulty of a text depends on simple stylistic variables, while the correlation between the computed values and the text comprehensibility has only a limited predictive value.

\- The traditional formulae use models that do not consider the mutual interaction of syntactic and semantic variables.

\- The validation of the formulae was done with respect to persons rather than tasks.

The individual methods include greatly varying characteristics and attributes of texts. In some cases the computed values are complementary, but they cannot be employed for the mutual testing of the results. Still, the measured values correlate to comprehensibility problems in the respective texts. Despite the limited extent of the study, its results do permit the conclusion that using methods for quality testing of software documentation is practical.

Our experience with the use of RMS is mostly positive. The automated calculation of the readability formulae provides significant time savings compared to manual testing. Improvements are necessary above all in the algorithms. The identification of words, syllables and sentences still requires significant manual intervention. A complete algorithmic solution of the automatic recognition of sentences and syllables is not expected in the near future.

## 5. Summary

Complaints about poor or unreadable documentation are quite frequent, but proof of its shortcomings based on objective criteria usually cannot be proven. Due to the lack of operationalized quality attributes, the application of readability formulae for testing software documentation is justified. Other supportive arguments are that the documents are either already in machine-readable form or can easily be transferred into such a form (e.g., using a scanner), that the documentation is usually in text form, and that the formulae can be computed with little effort. The automation of testing has clear limitations. It is practical to integrate the methods into a comprehensive quality assurances concept or to use them in the realm of quality assurance activities (e.g., reviews of software documentation).

We must also note that there are many other quality attributes that were not considered in this study. The readability, compared to other quality attributes, has the advantage that quantifiable measures are available. They cannot save the author the work of creating documentation, nor do they give concrete help in improving the readability. Many observe that low or high readability indices do not necessarily imply good or bad documentation. This is not an argument against the use of readability measures, but a note about their appropriate use. They can serve as a coarse measure of the degree of difficulty of a text and should be used accordingly. The possibility of automated support in the evaluation of these formulae and the importance of software documentation clearly suggest the use of readability measures.

## References

[1] Arthur, J.D., Stevens, K.T.: Assessing the Adequacy of Documentation Through Document Quality Indicators. Proceedings of the Conference on Software Maintenance, Miami 16.-19. Oct 1989, IEEE Computer Society Press, Washington 1989, 40-49.

[2] Barry, J.G.: Computerized Readability Levels. IEEE Transactions on Professional Communication. Vol PC-23, 2/1980, 88–90.

[3] Brockmann, J.R.: Writing Better Computer User Documentation. From Paper to Hypertext. New York et al. 1990.

[4] Danielson, W.A., Bryan, S.D.: Computer automation of two readability formulae. Journalism Quarterly, Vol 40, 1963, 201–206.

[5] Dickes, P., Steiwer, L.: Ausarbeitung von Lesbarkeitsformeln für die deutsche Sprache. Zeitschrift für Entwicklungsspsychologie und Pädagogische Psychologie. Band IX, 1/1977, 20–28.

[6] Fair, J.N., Jenkins, J.J., Patterson, D.G.: Simplification of Flesch Reading Ease Formula. Journal of Applied Psychology, Vol 35, 1951, 333–337.

[7] Flesch, R.A.: A new readability yardstick. Journal for applied Psychology, Vol. 32, 1948, 221–223.

[8] Gingrich, P.S. et al.: Writers's Workbench Trials: Final Report. Bell Laboratories, Piscataway, N.J., 1981.

[9] Guillemette, R.A.: The Cloze Procedure: An Assessment of the Understandability of Data Processing Texts. Information & Management 17, 1989, 143–155.

[10] Gunning, R.: The Technique of Clear Writing. New York 1968 (1st Ed. 1952).

[11] Hall, W.E., Zweben, S.H.: The Cloze Procedure and Software Comprehensibility Measurement. IEEE Transaction on Software Engineering, Vol SE-12, 5/1986, 608–623.

[12] Höcker, H. et al: Comparative Descriptions of Software Quality Measures. GMD-Studien Nr. 81, St. Augustin 1984.

[13] James, G.: Document Databases. New York 1985.

[14] Kincaid, J.P., Aagard, J.A., O'Hara, J.W., Cottrell, L.K.: Computer Readability Editing System. IEEE Transactions on Professional Communication, Vol PC-24, 1/1981, 38–41.

[15] Klare, G.: The Measurement of Readability. Iowa State University Press, Ames, Iowa 1963.

[16] Klare, G.: Assessing Readability. Reading Research Quarterly, Vol 10, 1/1974–1975, 62–102.

[17] Langer, I., Schulz von Thun, F., Tausch, R.: Verstandlichkeit in Schule, Verwaltung, Politik, Wissenschaft. München/Basel 1974.

[18] Lehner, F., Kreiner, A.: RMS – Readability Measuring System. Ein Werkzeug zur Messung der Lesbarkeit von Texten. Institutsbericht 91.04, Institut für Wirtschaftsinformatik, University of Linz, Austria, December 1991.

[19] Lehner, F.: Verständlichkeit und Lesbarkeit der Software-Dokumentation. Ergebnisse einer explorativen Studie über die Anwendung von Methoden zur Messung der Lesbarkeit von Texten. Institutsbericht 91.05, Institut für Wirtschaftsinformatik, University of Linz, Austria, December 1991.

[20] Redish, J.C., Felker, D.B., Rose, A.M.: Evaluating the Effects of Document Design Principles. Information Design Journal, Vol 2, No 3 und 4, 1981, 236–243.

[21] Robinson, C.: Cloze Procedure: A Review. Educational Research, Vol 23, 2/1981, 128–133.

[22] Rupietta, W.: Benutzerdokumentation für Softwareprodukte. Mannheim 1987.

[23] Smith, E., Kincaid, J.: Derivation and Validation of the Automated Readability Index for Use with Technical Materials. Human Factors, 5/1970, 457–464.

[24] Steinbach, I., Langer, I., Tausch. R.: Merkmale von Wissens- und Informationstexten im Zusammenhang mit der Lerneffektivität. Zeitschrift für Entwicklungspsychologie und Pädagogische Psychologie, Band IV, 2/1972, 130–139.

[25] Stevens, K.T., Arthur, J.D., Nance, R.E.: A Taxonomy for the Evaluation of Computer Documentation. Technical Report SRC-88-008, Systems Research Center, Virginia Tech, January 1988.

[26] Taylor, W.L.: “Cloze Procedure”: A New Tool For Measuring Readability. Journalism Quarterly, Fall 1953. 415–433.
