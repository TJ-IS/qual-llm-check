---
otero_id: 26588
otero_key: "W2FNDREM"
title: "The Effects and Limitations of Automated Text Condensing on Reading Comprehension Performance"
authors: "Andrew H. Morris; George M. Kasper; Dennis A. Adams"
year: "1992"
journal: "Information Systems Research"
doi: "10.1287/isre.3.1.17"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/W2FNDREM/fulltext/images/9449fbb10b8b220d6221462a827e9a1684ce5110ec591f4375d60c4a802949d6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# The Effects and Limitations of Automated Text Condensing on Reading Comprehension Performance

Andrew H. Morris, George M. Kasper, Dennis A. Adams,

To cite this article:

Andrew H. Morris, George M. Kasper, Dennis A. Adams, (1992) The Effects and Limitations of Automated Text Condensing on Reading Comprehension Performance. Information Systems Research 3(1):17-35. http://dx.doi.org/10.1287/isre.3.1.17

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1992 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/W2FNDREM/fulltext/images/05db7f140724e2ecac080373bd87daf356509c944a474c2c6ca7bc084702a089.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Effects and Limitations of Automated Text Condensing on Reading Comprehension Performance

Andrew H. Morris\* formerly of Department of Information and Management Sciences College of Business Florida State Universuty Tallahassee, Florıda 32306

George M. Kasper Department of Information Systems and Quantitative Sciences College of Business Administration Texas Tech University Lubbock, Texas 79409

Dennis A. Adams Department of Deciston and Injormation Scuences College of Business Administraton University of Houston Houston, Texas 77204

The optimal amount ofinformation needed in a given decision-making situation lies somewhere along a continuum from “not enough" to “too much". Ackoff proposed that information systems often hinder the decision-making process by creating information overload. To deal with this problem, he called for systems that could filter and condense data so that only relevant information reached the decision maker. The potential for information overload is especially critical in text-based information. The purpose of this research is to investigate the effects and theoretical limitations of extract condensing as a text processing tool in terms of recipient performance. In the experiment described here, an environment is created in which the effects of text condensing are isolated from the effects of message and individual recipient differences. The data show no difference in reading comprehension performance between the condensed forms and the original document. This indicates that condensed forms can be produced that are equally as informative as the original document. These results suggest that it is possible to apply a relatively simple computer algorithm to text and produce extracts that capture enough of the information contained in the original document so that the recipient can perform as if he or she had read the original. These results also identfy a methodology for assessing the effectiveness of text condensing schemes. The research presented here contributes to a small but growing body of work on text-based information systems and, specifically, text condensing.

Text-based information systems—Iext condensingAbstracting/extracting—Performance

## Introduction

he optimal amount of information needed in a given decision-making situation lies somewhere along a continuum from “not enough" to “too much" (Schroder et al. 1967). Over two decades ago, Ackoff (1967) proposed that information systems (IS) often hinder the decision-making process by creating information overload. To deal with this problem, he called for systems that could filter and condense data so that only relevant information reached the decision maker. In the years since Ackoff's challenge, the rapid growth of the information processing industry has reinforced the importance of filtering and condensing data. However, as Rappaport (1968) was quick to note, the danger of over-filtering and over-condensing also exists.

The potential for information overload is especially critical in text-based information (Hiltz and Turoff 1985). Communication is arguably the most critical and time consuming process in organizations (Culnan and Bair 1983; Rice and Bair 1984); it is a vital supporting routine that permeates the process of problem solving and decision making (Mintzberg et al. 1976). Yet, the amount of attention that a manager can devote to any single form or source of information is extremely limited (Kahneman 1973), and organizations can perform only a finite amount of information processing. Computer-mediated communication systems (CMCS) are rapidly becoming commonplace and, if the history of computing is any indication, they will result in an increase in the volume of text messages. Denning (1982) described the increase of unwanted computer mail as “electronic junk." Tools to control electronic communication must be in place to prevent the potential deluge (Hiltz and Turoff 1985). Unless practical filtering and condensing tools are developed, this increase is likely to place an excessive strain on the very limited resource of managerial attention (Denning 1982).

In addition to the increasing volume of communication generated within the organization, there exists an overwhelming and growing number of potential sources of information external to the firm; again, the majority of which are in the form of text. Resource and technological limitations (Blair and Maron 1985; Blair 1990) force managers to restrict their scanning activities to a very small subset of the potential sources of external information (El Sawy 1985). This can adversely affect performance as executives in successful organizations have been shown to engage in broader and more effective scanning activities than do their counterparts in poorer performing firms (Daft et al. 1988). Information systems that can “pre-scan" potential sources and identify sources of information have been developed (Jacobs and Rau 1990). Despite the obvious need and potential benefits, text condensing has proven to be a very difficult problem and has received very little attention from information systems (IS) researchers. As used here, text condensing refers to any text summary or reduction, and two approaches exist: (1) an “extract" is a summary based on a set of sentences or phrases selected virtually verbatim (allowing for very minor modifications) from a document; and (2) an “abstract" refers to a summary that restates the original document in a more concise manner.

The purpose of this research is to investigate the effects and theoretical limitations of extract condensing as a text processing tool in terms of recipient performance. Specifically, the effectiveness of applying a relatively simple extract technique to text-based information is assessed in terms of reading comprehension. Based on the library science literature, an efficient extracting algorithm for condensing text is empirically tested to determine the extent of reduction that results in effective message comprehension.

In the next section, current approaches to text-based processing are reviewed. This is followed by a discussion of text condensing techniques. Next, hypotheses are developed and empirically investigated. Specifically, a relatively simple algorithm for extracting text is developed, and the limits of its effectiveness are empirically investigated. Finally, the results of the work are summarized, and recommendations and conclusions are presented.

## Background

The application of computers to the problem of information overload and, in particular, text processing is not new. Luhn (1958b) was probably the first to propose a computer-based “business intelligence system" designed to automatically produce “auto-abstracts" and to selectively disseminate information based on “action-point profiles." Later, Ackoff (1967) formalized this position, arguing that the purpose of information systems is to filter and condense information. To filter is to disseminate by deciding between relevant and irrelevant information; whereas condensing reduces relevant information to a more compact, summarized form. Filtering might combine the use of automatic routing schemes (Tsichritzis 1984), perhaps based on search strategies (Blair 1984), system-maintained profiles of the user's area(s) of interest (Luhn 1958a, b; Ewusi-mensah 1981) and already available automatic indexing systems (van Rijsbergen 1979, Dillon and Gray 1983, Salton 1989), which are able to classify documents according to the topic(s) addressed within them. Filtering can be aided by condensing (Swanson 1977). Condensing text, however, appears to be a much more difficult task. When a human condenses text (i.e., creates an abstract), he or she must understand the essence of what is explicitly stated as well as that implied in the document (Cremmins 1982). Designing computer-based systems that “understand" the content of a document has proven to be very difficult. However, it may not be necessary to wait until efficient artificial intelligence-based natural language processing systems that mimic the human's abstracting abilities are available before svstems to effectively condense text can be emploved.

## Text Processing Systems

Most systems designed to process¹ text-based information fall in two categories: (1) systems that are intended to support document archival and retrieval and (2) systems that are primarily intended to support organizational communication functions. Identified as “document-based systems" by Swanson and Culnan (1978), the first category includes automated bibliographic databases (e.g.. ERIC, ABI/INFORM). image processing (e.g., Image Plus), on-line text searching systems (e.g.. SCISOR), hypertext systems (e.g., Hypercard), and other document archival and retrieval systems. The second category, organizational communication systems, is characterized by CMCS (Kerr and Hiltz 1982).

Document-based systems differ from those that process alphanumeric data in several important ways. Focusing on the distinction between document and data retrieval, Blair (1984) identifies four differences: the way the retrieval is answered, the relation between the formal request and user satisfaction, the factors that influence retrieval speed, and the criterion for successful retrieval. In data retrieval a query is deterministic, while a document retrieval query is nondeterministic. Rather than answering a specific question, document retrieval is indirect providing a set of documents that are likely to contain the desired information. This uncertainty makes document retrieval fundamentally a trial-and-error process (Swanson 1977). This lack of specificity also makes the efficiency of document retrieval less dependent on the speed of the system and more dependent upon the user's decisions. In terms of the criterion used to evaluate system performance, Blair states that, for data-based systems, performance is measured by correctness: the system responds with the right answer to a factual question. For document-based systems, the performance criterion is utility: the system must provide a response that is useful to the person requesting the information. Brookes (1983) also recognizes that the meaning of text is often ambiguous and thus difficult for automated systems to process, a problem well known to researchers in natural language processing.

Extensive research on document-based systems has been conducted in the area of library science, but relatively little attention has been paid to document processing by business and IS researchers (Swanson and Culnan 1978; Schwartz et al. 1980; Slonim et al. 1981). One of the most significant trends in information processing is the growth of CMCS (Kiesler et al. 1984), and most IS research that addresses text-based information processing falls into this category. Surveys of major business firms have consistently projected significant growth of CMCS well into the next decade (Kolodziej 1985, Kriebel and Strong 1984, Dickson et al. 1984, Brancheau and Wetherbe 1987, Adams and Weiss 1989). The application of CMCS has important implications for text-based information systems in that much of the basic technology for transmitting text (computer networks, protocols, communication equipment, etc.) is already in place. What remains is for advances to add value to these systems by providing, among other things, text condensing and filtering tools.

## Text Condensing

Conceptually, the efficacy of text condensing is founded in statistical information and control theory (Wiener 1961) and, in particular, related developments in human information processing such as complexity theory (Schroder et al. 1967), information redundancy, and information overload. In an early review of the sciences of management, Goode (1958) identifies the relationship between Wiener's work and the human's capacity to process information:

. . . the capacity [of an indivıdual] to accept information, act on it, and put out a response, rises lınearly at first, then less quickly, and after reaching a peak performance does not contınue at peak, but falls off rapidty remınd{s} {me] of Wiener's discussion of the performance of a telephone exchange. (pp. 369–370)

This inverted U-shaped relationship exists between the quantity of information provided to a decision maker and his or her performance (Schroder et al. 1967, Chervany and Dickson 1974, Davis and Olson 1985, p. 237). “Information processing by people in general' . . . reaches a maximum level at some level of environmental complexity . . ." (Schroder et al. 1967, p. 36) beyond which information overload is experienced and performance actually deteriorates. Directly related to information overload and human information processing performance is redundancy.

Communication rarely, if ever, exists without redundancy. Redundancy occurs when more data are transmitted than are strictly required to convey the information (Davis and Olson 1985, p. 206). While redundant data can be used for error detection and correction, an objective of text condensing is the elimination of redundancy without reducing human information processing performance (i.e., successful communication). In fact, based on entropy theory, Shannon (1951) estimated that printed English has a redundancy of about 75 percent. Confirmed by Burton and Licklider (1955), this suggests a theoretical limit to nonexpository text condensing. In these studies, subjects were presented with a series of texts ranging from zero to 10,000 letters and were required to continue guessing until they named the next letter in the text correctly. Burton and Licklider found that, from 32 to 10,000 characters. there was no difference in the subject's ability to predict the next letter; the constraint imposed by 10,000 preceding letters is no different than that imposed by 32. Beyond 32 characters, the relative redundancy of written English is approximately 75 percent. “Written English does not become more and more redundant as longer and longer sequences are taken into account" (Burton and Licklider 1955, p. 652). Whether this is simply a reflection of printed English's redundancy of characters and words as suggested by Kibby (1980) or extends to message comprehension is unknown. However, for text-based information systems it suggests a measure of condensing, a theoretical limit to the effectiveness of extraction, beyond which expository abstracting is necessary.

## Abstracting

The best known form of text condensing is the abstract—an abbreviated, accurate representation of the contents of a document (American National Standards Institute 1979).² Three main types of abstracts are generally recognized: indicative, informative, and critical (Borko and Bernier 1975, Weil 1970, Cremmıns 1982). Briefly, the indicative (sometimes called descriptive) abstract describes what the text is about and helps the reader decide if the original full text should be consulted; the informative abstract tries to summarize the information in the text so that the reader will not need to consult the full text; and the critical abstract evaluates the text, expressing the reviewer's opinion of the original document. Because relatively few applications require critical abstracts, and because the technology needed to provide this subjective assessment is beyond that needed to produce the other two types of abstracts, research in automated text condensing has focused on the development of informative abstracts.

## Automated Text Condensing

Until recently, automated text condensing has received relatively little research attention (Jacobs and Rau 1990). Three reasons have been suggested for this. First, if the original full text must first be physically entered into the computer, the cost effectiveness of automated condensing is questionable. However, Paice (1977, p. 144) predicted that when the input inefficiencies were resolved, “the interest in automatic extracting will be revived." Since then, optical character readers have become more sophisticated and less expensive, and fewer source documents are entered into the computer by hand. At the same time, more text is being created with the aid of computers, and therefore is already available in a computer-readable form for condensing.

A second issue influencing research in automated text condensing techniques is the lack of an objective measure of the quality of the reduction. Without such a measure, there is no guide for judging the success of a condensing technique. However, while literary quality remains largely a subjective issue, the information quality of a reduction can be objectively assessed by, for example, comparing reading comprehension performance of the condensed reduction to that of the original document.

Finally, two approaches to automated text condensing exist: (1) using natural language processing techniques to construct a map of the knowledge in a document from which an abstract is produced; and (2) employing an algorithmic system to extract important sentences and phrases from the document. Natural language processing requires syntactic, semantic and pragmatic knowledge. Syntactic knowledge is comprised of the rules for structuring a language, while semantic and pragmatic knowledge are increasingly domain specific (Hale et al. 1991). Analysis of syntax is relatively domain independent, and several important syntax-based systems have been built (Taylor and Krulee 1977, Miller 1980, Miller et al. 1981, Heidorn et al. 1982). Probably the best known of these is EPISTLE (Heidorn et al. 1982, Schriber 1983). Unfortunately, the use of syntax alone sometimes results in totally incorrect interpretations, particularly of idiomatic phrases such as “he threw the book at me" (Smeaton and van Rijsbergen 1986). Largely because of the knowledge domain constraints, systems that can fully analyze the semantic information of a broad domain of free text have been beyond the scope of technology (Epstein 1985), and are likely to remain so for the foreseeable future. The few prototype systems that do make use of semantic knowledge require an understanding of the subject-domain's “deep" knowledge, and are restricted to a single, typically very narrow domain (Smeaton and van Rijsbergen 1986). In a recent article, for example, Jacobs and Rau (1990) discuss a state-of-the-art natural language system which parses every word in a sentence, identifying linguistic structures and mapping these structures into a conceptual framework such as a semantic network. This very resource intensive process is capable of processing financial news at about six stories per minute with 80 to 90 percent recall (the proportion of relevant material retrieved) and precision (the proportion of retrieved materials that are relevant) in constrained texts. However, it “would also produce almost nothing useful, for instance, in reading the entire Wall Street Journal" (Jacobs and Rau 1990, p. 96).

The resource requirements of semantic-based condensing systems have been and will remain for the foreseeable future, a serious limitation to the application of this approach. However, even if resources suddenly became available and semantic-based condensing systems were a reality, research and development of extracting techniques would remain important for several reasons. First, if extracts can be produced that are informationally equivalent to the original text, these more efficiently produced extracts could be used directly in many cases. If the subjective literary quality of these informationally equivalent reductions was critical, they could be used as an intermediate product to be refined by a semantic-based system to a more literary pleasing, abstract equivalent, reduction. Moreover, even if literary refinement is essential, it may not require very intelligent processing because relatively simple rule-based parsing techniques can greatly improve the readability of extracts (Paice 1981).

Second, for many applications, literary refinement may not be needed for extract produced reductions to be just as effective as semantic-based reductions. particularly if the objective of the condensing operation is to enhance the user/manager's ability to scan internal and/or external sources of information. Finally, compared to syntax and semantic-based systems, extracting algorithms are much less domain dependent and are not prone to dramatic, sometimes complete, errors in interpretation such as those associated with idiomatic phrases.

## Extracting

Mathematical and statistical information can be derived from text and used in the condensing process. Based on the frequency and relative position of nontrivial words in a document, many of the early so-called automated abstracting systems actually produced extracts. Luhn (1958a, b) pioneered this work with a system designed to produce “auto-abstracts," extracts consisting of sentences selected verbatim from the original document (Weil 1970). Extensive reviews of mathematical models of text can be found in Edmunson (1977, 1984).

During the 1960s, Edmunson and Wyllys (1961) and Edmunson (1964, 1969) developed four methods of weighting sentences for extract selection. Briefly, the Location method uses the position of the sentence in the document as an indication of its importance, and is based on the work of Baxendale (1958), who found that so-called “topic sentences" are most likely to occur as either the first (85%) or the last (7%) sentence in a paragraph. The Cue method uses a dictionary of pragmatic words such as “significant" and “purpose" to weight and select sentences to include in the extract. The Key Word method selects sentences for extracting based on the relative use of nontrivial words found in the document. Finally, the Title method uses nontrivial words in the title and subtitles as indicative of the sentence's relative importance to the extract. Based on subjective and statistical similarity ratings, Edmunson (1969) attained the best results when these methods were used in combination.

Perhaps the most successful extracting system was developed in the 1970s and reported by Rush et al. (1971), Mathis et al. (1973), and Pollock and Zamora (1975). Called ADAM (Automatic Document Abstracting Method), this system was based primarily on the Cue method, applied through a list known as a “word control list" (WCL). A WCL contains terms that when present in a sentence increase or decrease the likelihood that it will be included in the extract. Negative terms. such as “for instance," "perhaps," and “possible," imply a sense of qualification or hedging, or a statement of obvious fact or known research, or pertain to a peripheral topic. Positive words and phrases that increase the likelihood of a sentence being selected for extraction include “it was found," “results," and “conclusion." Parenthetical material is removed.

The subjective literary quality of extracts has never been as good as a well-written abstract (Bernier 1985, Cremmins 1982). To improve the quality of these reductions, Paice (1981) described an extracting approach that uses exophoric references to identify clusters of sentences that should be treated as a unit. Exophoria are words within a sentence that require reference to material in some other sentence(s) for resolution: the most common example of this is a pronoun that has its antecedent in previous text. To resolve exophoria, the sentence(s) containing the material referred to should also be included in the reduction. Thus, a sentence to be extracted serves as a nucleus around which all or a segment of the extract is developed, greatly reducing the sometimes disjointed appearance of extracts. Commenting on extracting, Paice (1981, p. 172) states:

The possibility of producing abstracts by computer has not received very much attention. There are perhaps two main reasons for this. First, it appears that the production of well-constructed abstracts is an artificial intelligence problem, and therefore unlikely to be either feasible or worthwhile until well into the future; the alternative of picking sentences here and there in a document is a rather unattractive proposition. Second, the cost of key-punching texts for input into an abstracting program can hardly be justified—especially since the program will then in effect discard most of the text which has been so laboriously prepared. It now appears that the first of these objections is exaggerated—reasonable-looking abstracts can often be produced by quite “unintelligent" programs—while with advances in technology the second problem should soon disappear.

## Research Hypotheses

To assess the theoretical limits and effectiveness of extracting as an approach to text condensing, three hypotheses were investigated. To assess whether the theoretical level of redundancy in printed English also holds for reading comprehension performance, extracts of varving degrees of reduction were produced, This was done by varying the extracting algorithm's stopping rule to produce reductions containing approximately 30% and 20% of the original text. Formally, this question can be stated in the null form as:

$\mathrm { H } 1 _ { 0 }$ . In terms of reading comprehension, no difference in performance exists between the original document and extracts containing 20% or 30% of the original document.

Failure to reject $\mathrm { H } 1 _ { 0 }$ would indicate that extracts containing 20% or 30% of the original document are equally effective surrogates for the original document. This would suggest that Shannon's and Burton and Licklider's estimate of the redundancy of printed English is limited to prediction of character or word sequence, but does not hold for message comprehension and more informative chunks of information such as sentences. On the other hand, rejecting $\mathrm { H } \mathsf { l } _ { 0 }$ would indicate that printed English is less redundant in terms of message comprehension than expected. Finally, rejecting $\mathrm { ~ H ~ I _ { 0 } ~ }$ for the 20% extracts but finding no difference in performance between the 30% extracts and the original document would suggest that to condense text beyond the redundancy limit of 75% requires natural language processing and the production of informative abstracts. This can be stated in the null form as:

$\mathrm { H } 2 _ { 0 }$ . In terms of reading comprehension performance, there is no difference between the informative abstract whose length is less than 75% that of the original document and the extracts (20% and 30%).

As discussed below, to produce the high quality informative abstracts expected of future very intelligent condensing systems, a human expert was employed. Failure to reject $\mathrm { H } 2 _ { 0 }$ would suggest that there is no difference in reading comprehension performance between the informative abstracts and the algorithm-produced extracts.

Finally, because these abstracts and extracts represent only a fraction of the length of the original text, they “rarely equal and never surpass the information content of the basic document" (Cremmins 1982, p.3). Yet, the literature also supports the argument that quality reductions might actually enhance the subject's comprehension of the information contained in the original document, because the concise and summarized presentation sufficiently reduces distracting information that would otherwise impede performance through information overload. Stated in the null form, the hypothesis of interest is:

H30 In terms of reading comprehension performance, there is no difference between the condensed forms (abstract and extract) and the original document.

Failure to reject the null hypothesis would indicate that the condensed forms are of sufficient quality that reading comprehension scores are not significantly reduced in the condensing treatments. If there is a significant treatment effect, then it will be necessary to examine the nature of the effect more carefully by constructing contrasts that investigated the differences between the specific treatments of interest. Collectively, these hypotheses begin to investigate the limits of text condensing, an issue that Ackoff (1967) argued was a critical function of information systems, but has been mostly ignored by IS.

## Experimental Design

The effectiveness of text condensing is a function of the message, the condensing procedure, and the recipient. In the experiment described here, an environment is created in which the effects of text condensing are isolated from the effects of message and individual recipient differences. To isolate individual differences, a blocked design in which each subject receives all treatments of interest was used. This takes advantage of the statistical power inherent in multiple measures of the same unit (Horton 1978), as each block consists of a nonrepeating combination of all treatments. To prevent any carryover effect from confounding the results, all possible treatment orderings occurred an equal number of times in the experimental design. Each treatment consisted of either some condensed form or the original text followed by a reading comprehension test designed to assess the subject's understanding of the original full-length document. Because the subject served as the block, receiving more than one treatment, it was necessary that different text appear within the block; otherwise, the learning effect would overwhelm any other effect. The different texts were also ordered and assigned within the experimental design across treatments. The final treatment/text combinations, shown in the appendix, result in a partially balanced incorplete block design that provides a powerful test of the hypothesis and has been used in other studies (Morris 1988, Kasper and Morris 1988, Hale and Kasper 1989).

## Treatments

In total, six treatments were administered: four condensing treatments, a no-extract treatment consisting of only the reading comprehension questionnaire and no text, and the original full-length text. Each block of the research design contained the four condensing treatments. Written by an expert, one treatment consisted of a high quality informative abstract of the text. The other three treatments were extracts. Two of these were extracts generated by the algorithm described below: one containing approximately 20% and the other about 30% of the original document. The third extract was generated by selecting sentences at random from the text. Each of these is discussed further below.

## Full Text Treatment

Four passages were randomly selected from a set of twelve sample Graduate Management Aptitude Test (GMAT) reading comprehension tests (Educational Testing Service 1986). These tests averaged 453 words, ranging in length from 430 to 470 words and covered very diverse topics, including: medieval literature, 18th-century Japan, minority-operated businesses, and Florentine art. A well-known indicator of the difficulty of reading material, the Fog Index (Gunning 1968) was calculated for each passage. Considered an estimate of the educational grade level required to read and understand a passage, the index ranged from 15.5 to 18.9, indicating that the selected passages were all about the same level of relatively moderate difficulty. The use of moderately difficult passages was intentional in an effort to encourage treatment differences.3

## Informative Abstract Treatment

To produce the high quality abstracts expected of future very intelligent condensing systems, a human expert (a professional abstracter) was employed. The expert was never shown the reading comprehension questions. He was simply instructed to produce informative abstracts. The four abstracts ranged in length from 90 to 129 words, with an average of 106 words or 23% of the original documents.

## Extract Treatments

Three extract treatments were developed. To produce extracts containing 20% and 30% of the original full-length document an algorithm that combined and developed the approaches discussed earlier was used. The basic structure of the extracting algorithm consisted of three phases: (1) remove parenthetic material, (2) determine the sentence weights for the remaining material, and (3) build the extract by selecting the highest weighted sentences and resolving the exophoric references.

In the first phase, a three-step process is used to remove all parenthetic material, First, all text contained within parentheses or between a pair of dashed lines is removed. Second, any material contained within a pair of commas where the second comma is followed immediately by a verb or verb form, or by an infinitive, is assumed to be parenthetic and is deleted. Third. “padding" expressions such as “in fact," “indeed," “of course," “in any case." etc., are deleted

The second phase in the procedure is to determine a weight for each sentence. Based on Edmunson's (1969) work, a simple summate of weighting functions is used that can be easily adjusted to reflect both the content of the document and user requirements. The variables used in the summate are: (1) the number of nontrivial title and subtitle words found in the sentence, (2) the number of words in the sentence that is in each of the categories of the WCL, (3) binary indicators to designate the first and the last sentences in a paragraph, and (4) a count of the high-frequency nontrivial words contained in the sentence (the definition of high frequency is also a parameter). A matrix containing the values of each variable for each sentence is constructed, and a vector of parameter weights is then applied, producing the vector of sentence weights.

3 Other tests of reading comprehension exist. For example, cloze is a widely accepted measure of readıng comprehension; however, it has been seriously questioned, especially in this type of application (Kibby 1980). Accordıng to Kıbby, cloze may only measure the subject's abılıty to predıct the next word in the text, rather than comprehend the meaning of the whole message

The third phase in the procedure is to build the extract. This is accomplished by (1) adding the highest weighted as-yet-unselected sentence to the extract; (2) checking to see if this sentence has any exophoric references, and, if so, adding the referenced sentence(s) n the order of their weights to the extract; (3) recursively resolving the exophoric references of sentences added in step (2); and (4) counting the number of words in the sentences selected for the extract thus far and returning to step (1) if the count is less than the stopping rule. Before this algorithm can be applied. the parameter weights must be established. Working with four passages used in a earlier study (Kasper and Morris 1988), one of the researchers adjusted the parameter weights until the algorithm produced reasonable extracts; however, little effort was spent “optimizing" the weights, as only two iterations were performed. In a production system, these terms and weights would be adjusted to reflect the user's interests and the position, role, and function performed for the organization.

Based on Shannon's and Burton and Licklider's theoretical estimates of the redundancy in printed English, stopping rules were selected to produce extracts greater than and less than the theoretical reduction limit of 25% of the original without loss of information. The intent was to produce two sets of extracts: one set consisting of approximately 30 percent of the original document, and a second set containing about 20 percent of the original document, the latter exceeding the theoretical limits of nonexpository reduction. These are hereafter referred to as 30% extracts and 20% extracts, respectively.

According to the extracting algorithm, once a sentence is selected, sentences related through exophoric references are also selected without checking the stopping parameter until all exophoria is resolved. Therefore, the length of the extracts could not be predetermined exactly, as is the case with words or character sets. On average. the 30% extracts contained 31% of the original document, plus or minus 5%. The 20% extracts contained an average 19.2% of the original document, ranging from 19% to 21%. The extracts bounded both sides of the theoretical limit of 75% reduction very closely. Because the passages were randomly selected and the algorithm applied strictly as developed, no modifications or other original texts were considered.

To provide a control and a further assessment of the effectiveness of the abstract and the 20% and 30% extract algorithm, reductions produced by a totally “unintelligent" procedure were developed. These extracts were produced by randomly selecting sentences without replacement from the original full-length text until the reduction consisted of at least 25% of the original document. Once this amount was exceeded, the sentences were arranged by the order of their occurrence in the original document. This process resulted in random extracts that contained on average 26% of the words in the original document

## No-Extracı Treatment

To provide a control and to investigate the possibility that the examination questions themselves contained information, a no-extract treatment was developed. The no-extract treatment contained only the examination questions and no other information. Like each of the other treatments, the no-extract treatment consisted of eight multiple-choice questions, each containing five possible responses

## Subjects

A total of 72 graduate students participated in the study. These students represented three classes of 24 students that elected to participate in the study. These subjects are appropriate for the task of reading and comprehending a text passage because the GMAT is intended to be administered to the same population. To motivate their performance subjects were given monetary prizes and class credit based on their performance

TABLE 1  
Sample Means, V’ariances and Standard Errors by Treatment for the Dependent Variable Percent Readıng Comprehension

<table><tr><td colspan="4">Percentage Score (N = 72)</td></tr><tr><td>Treatment Levels</td><td>Mean (n = 24)</td><td>Variance</td><td>Standard Error</td></tr><tr><td>No Extract</td><td>0.346</td><td>0.011</td><td>0.021</td></tr><tr><td>Random Extract</td><td>0.489</td><td>0.047</td><td>0.044</td></tr><tr><td>20% Extract</td><td>0.552</td><td>0.031</td><td>0.036</td></tr><tr><td>30% Extract</td><td>0.609</td><td>0.017</td><td>0.026</td></tr><tr><td>Full Text</td><td>0.620</td><td>0.040</td><td>0.041</td></tr><tr><td>Abstract</td><td>0.630</td><td>0.024</td><td>0.031</td></tr></table>

## Procedures

One of the three groups of 24 students was assigned the no-extract treatment. In this treatment no extract was given and only the examination questions were administered to the 24 subjects. At the other extreme, the full-length original text was administered to a second group of 24 subjects. Finally, a third group of 24 subjects was given all four condensing treatments according to the design described in the appendix. The groups as a whole were randomly assigned one of the three treatment regimes and the subjects within a group were randomized. However, because the data were collected in a classroom setting, complete randomization was not possible. Each group of subjects completed their assigned treatment(s) in a single session. At the beginning of the experiment, subjects were given a set of instructions. Next, the treatment(s) were administered. All treatments were administered on paper, and subjects with text to read were instructed not to return to the text once they began answering the questions. Each examination consisted of eight multiple-choice questions, each containing five possible responses. The subject's percentage correct score on these examinations served as the dependent variable for analysis.

## Analysis and Results

Table 1 presents the sample means, variances, and standard errors for the dependent variable for each treatment level. Because each question had five multiple choice answers, the probability of a correct response without any information was 0.20 (a random guess). However, as the data show, all the treatments, even the no-extract treatment, exceeded this value by a considerable amount.

As can be seen from the data in Table 1, the mean performance by treatment is consistent with expectations. Ranked by decreasing order of performance, the treatment means are: informative abstract, original full text, 30% extract, 20% extract, random extract, and no extract. These results are consistent with Burton and Licklider's findings and suggest that the 75% limit to reduction may also hold for text condensing based on sentence extraction.

The analysis of variance for this data, including the type III sum of squares tests for the main effects and passage by treatment interaction model, is presented in Table 2. These results show that both the passage and treatment effects are significant at the alpha = 0.05 level; however, neither the subject nor the passage by treatment interaction is significant. The latter indicates that the relative performance of the treatment levels remained the same across passages and that no single passage accounted for these results.

TABLF 2  
Analysis of Variance for Readıng Comprehension Performance

<table><tr><td>Source</td><td>df</td><td>Sum of Squares</td><td>F-value</td><td>R-square</td></tr><tr><td>Model</td><td>86</td><td>4.007</td><td>2.00**</td><td>0.751</td></tr><tr><td>Subject</td><td>66</td><td>1 849</td><td>1.20</td><td></td></tr><tr><td>Passage</td><td>3</td><td>0 252</td><td>3.61*</td><td></td></tr><tr><td>Treatment</td><td>3</td><td>0.287</td><td>4.11*</td><td></td></tr><tr><td>Passage × Treatment</td><td>9</td><td>0.158</td><td>0.75</td><td></td></tr><tr><td>Error</td><td>57</td><td>1.326</td><td></td><td></td></tr><tr><td>Total</td><td>143</td><td>5.333</td><td></td><td></td></tr></table>

\*\* = alpha ≤ 0.01: \* = alpha ≤ 0 05 level of significance.

To investigate the nature of the treatment effect, mean differences were computed and are presented in Table 3. For each comparison, the difference between the means is presented. Based on the least significant difference (LSD), a test of the hypotheses of equal means was computed for each comparison.

An examination of the mean differences in Table 3 shows that all the treatments including the random extract performed significantly better than the no-extract treatment. The data also show that the performances of the condensing treatments—the 20% extract, the 30% extract, and the informative abstract—were no different from that of the original full-text. Only the random, and the no-extract treatment means were significantly below the full-text treatment mean. Likewise, both the 30% extract and the informative abstract performed better than the randomly produced extract. However, the 20% extract mean performance was not significantly different from that of the random extract treatment. $\mathrm { Y e t }$ , there was no difference in performance between the two extract treatments, the two extract treatment levels and the original full text, and the two extract treatment levels and the informative abstract.

TABLE 3  
Treatment Level Mean Differences (Row-Column)

<table><tr><td rowspan="2"></td><td colspan="3">Treatment Levels</td><td rowspan="2">Abstract</td><td rowspan="2">30% Extract</td></tr><tr><td>No Extract</td><td>Random Extract</td><td>Full Text</td></tr><tr><td>Random Extract</td><td>0.143**</td><td></td><td></td><td></td><td></td></tr><tr><td>Full Text</td><td>0.273**</td><td>0.130**</td><td></td><td></td><td></td></tr><tr><td>Abstract</td><td>0.284**</td><td>0.141**</td><td>0.010</td><td></td><td></td></tr><tr><td>30% Extract</td><td>0.263**</td><td>0.120**</td><td>-0.010</td><td>-0.021</td><td></td></tr><tr><td>20% Extract</td><td>0.206**</td><td>0.063</td><td>-0.068</td><td>-0.078</td><td>-0.057</td></tr></table>

df = 57 for all comparisons.  
Least Significant Difference (LSD) for alpha ≤ 0.01 = 0.118, alpha ≤ 0 05 = 0.088.  
\*\* The hypothesis of equal means is rejected at alpha ≤ 0.01 level of significance.

Collectively, these comparisons suggest that it is possible to produce extracts that exceed the 75% redundancy limit. Consistent with Brookes (1983), these results might also reflect the subjects' ability to compensate, in this case interpolating information from the 20% extract, and even the random treatment. In sum, $\mathrm { H } \mathfrak { l } _ { 0 }$ cannot be rejected; in terms of reading comprehension, the data show that no difference in performance exists between the original document and extracts containing 20% or 30% of the original document. Likewise, $\mathbf { H } 2 _ { 0 }$ cannot be rejected; in terms of reading comprehension performance, the data show no difference between the informative abstract and either the 20% or the 30% extracts. Apparently, the extract algorithm produced extracts that were as informative as the human-expert produced abstracts.

Finally, $\mathsf { H } 3 _ { 0 }$ cannot be rejected; the data show no difference in reading comprehension performance between the condensed forms (abstract and extract) and the original document. This indicates that condensed forms can be produced that are equally as informative as the original document. While not significant, the mean performance of the informative abstract treatment actually exceeded that of the original document treatment, suggesting that quality reductions might actually enhance the subject's comprehension of the information contained in the original document Failure to reject the null hypotheses, however, reflects a strict interpretation of the results. The results also show that the mean performance of the 20% extract was not statistically different than the random extract treatment. This may be a reflection of the loss of information as the 20% extract exceeded the 75% redundancy level of printed English or this may indicate that the random extracts were particularly informative. Support for the latter is provided by the finding that the random extract performed significantly better than the no-extract treatment.

## Summary and Conclusions

Collectively, these results suggest that it is possible to apply a relatively simple computer algorithm to text and produce extracts that capture enough of the information contained in the original document so that the recipient can perform as if he or she had read the original. In this study, subjects performed as well reading extracts as they did reading the original full length text, even though the text was relatively difficult and the measure of performance, reading comprehension, was intended to be very discriminating. Under less discriminating conditions, where the objective is to provide a more general overview of the original document or to help the reader decide if the full text should be consulted, these results indicate that the extracting algorithm would produce reductions containing more information than that needed for the task. Moreover, these results were achieved over an atypically broad set of problem domains (medieval literature, 18th-century Japan, minority business opportunities, and Florentine art). It seems unlikely that the typical business user would encounter such a diverse set of domains on any regular basis, nor does it seem reasonable to expect any condensing technique using a single set of parameters, including any future natural language-based abstracting system, to perform any better over such a diverse set of topics. As the breadth of topics is narrowed, the extracting algorithm could be tuned and thus potentially produce even better reductions.

The reader should note that the “abstract" at the beginning of this paper is actually an extract that was generated using the algorithm discussed here. In this case, the algorithm was modified slightly to reflect the academic research nature of the article. For example, slightly more emphasis was placed on introductory and summary sections than on the intervening text. In addition, this paragraph was excluded from analysis. The extract itself was not modified after extraction.

In terms of reading comprehension, these results also failed to support Shannon's and Burton and Licklider's estimate that printed English has a redundancy of about 75 percent. Reductions of 80% were shown to be effective in this study. These results support Kibby's (1980) suggestion that the 75 percent prediction rate of Shannon and Burton and Licklider may simply reflect printed Englısh's redundancy of characters and words and does not extend to information units or chunks into message comprehension. As both Kibby (1980) and Brookes (1983) have observed, these results might also reflect the subjects’ ability to compensate and interpolate information from text. Compensation and interpolation increase with experience in the subject matter. The diversity of the topics used in this study probably understated this ability. One might expect that experienced people in the domain of the condensed text might need even less text to attain a high level of comprehension.

These results also have implications for designers of natural language processing systems. It is important to realize that the extracting algorithm is not without intelligence. Mathematical information has (Edmunson 1977, 1984) and is currently (Jacobs and Rau 1990) being used to process text. However, much of the effectiveness of the extracting algorithm used here can be attributed to its resolution of exophoria. This resulted in the identification of clusters of sentences that were treated as a single information unit. In this way, sentences served as a nucleus around which all or a segment of a mapping of the information or semantic content of the message was developed. For natural language processing researchers thıs suggests that rather than focusing on words as the unit of analysis, much more effective and efficient systems might result from constructing a conceptual framework such as semantic networks at an information unit level (e.g., the sentence). The results of this study suggest that the resolution of exophoria is a very powerful technique for mapping the linguistic structure of information units such as groups of sentences.

These results also identify a methodology for assessing the effectiveness of text condensing schemes. Future text condensing schemes must produce reductions that contain less than 80% of the original full-length text and produce reductions that result in reading comprehension performance that is equal to or exceeds that attained from the original full-length document. Quality reductions might actually enhance the subject's comprehension of the information contained in the original document, because the concise and summarized presentation sufficiently reduces distracting information that would otherwise impede performance through information overload. Such a finding is supported by research in condensing numerical data (Chervany and Dickson 1974).

While these results are informative, both in practice and theory, several limitations of the research should be noted. First, the subjects were university students, but there is no reason to expect that their reading comprehension varies greatly from that of the “real world" population. A second more severe limitation of the study is the type of passage used in the research—difficult and relatively short. The use of easier to read, more typically constructed communication may influence the findings. Also, the lengths of the original passages used here were all about 450 words. While this length is consistent with many business magazine articles and reading comprehension examinations, many documents are much longer. Although short, the length of the passages used in this study is consistent with newspaper⁴ and magazine columns and short stories (Neff 1990, Mandell 1987, Peterson and Kesselman-Turkel 1987), as well as frequently used business correspondence such as letters, memoranda and short reports (Kirtz and Reep 1990). However, the use of relatively short documents probably understated the true difference between the extracts, particularly the 20% extracts, and the random treatments.⁵ A third limitation is that the abstracts were, as part of the research design, not expository, likely understating the potential performance of the abstracting treatment. Despite these limitations, a number of implications for text-based information systems research and practice can be drawn.

Demonstrating that a relatively simple text condensing algorithm can be used to generate highly effective reductions, these results suggest a number of important research questions. Text condensing techniques are represented as a continuum ranging from randomly generated extracts to critical abstracts. This research developed one extracting algorithm, but others may prove more appealing. Future research should also investigate the degree to which the subjects' ability to compensate, interpolating information from that provided, is related to text condensing and the maximum reduction possible without loss of information.

In summary, more than 20 years ago Ackoff argued that condensing is critical for dealing with information overload, especially when the information is in the form of text. As the volume of text being transported by information systems increases, so will the potential for information overload. To deal with this problem, efficient and effective text condensing techniques will become essential. The research presented here suggests one near-term approach for dealing with this growing problem and an approach for assessing the effectiveness of future condensing schemes. The research presented here contributes to a small but growing body of work on text-based information systems and, specifically, text condensing.\*

Because the original passages consısted of from 15 to 20 sentences. the probability of randomly selecting a sentence from the document that was also selected by the extracting algorithm was great, thereby understating the difference between the extract and random treatments. In fact, approximately 20 percent of the extract sentences were also included in the random reduction

\* Barbara Gutek, Associate Editor. Thıs paper was received on February 7, 1991 and has been with the authors 2 months for 1 revision

Appendix. Order and Combination of Treatments and Passage in Experimental Design

<table><tr><td>Subject</td><td>Position 1</td><td>Position 2</td><td>Position 3</td><td>Position 4</td></tr><tr><td>49</td><td>Random Extract, D</td><td>Abstract, C</td><td>20% Extract, B</td><td>30% Extract, A</td></tr><tr><td>50</td><td>Random Extract, C</td><td>Abstract, D</td><td>30% Extract, B</td><td>20% Extract, A</td></tr><tr><td>51</td><td>Random Extract, B</td><td>20% Extract, D</td><td>Abstract, A</td><td>30% Extract, C</td></tr><tr><td>52</td><td>Random Extract, A</td><td>20% Extract, B</td><td>30% Extract, C</td><td>Abstract, D</td></tr><tr><td>53</td><td>Random Extract, A</td><td>30% Extract, D</td><td>Abstract, B</td><td>20% Extract, C</td></tr><tr><td>54</td><td>Random Extract, D</td><td>30% Extract, A</td><td>20% Extract, C</td><td>Abstract, B</td></tr><tr><td>55</td><td>Abstract, D</td><td>Random Extract, C</td><td>20% Extract, A</td><td>30% Extract, B</td></tr><tr><td>56</td><td>Abstract, C</td><td>Random Extract, B</td><td>30% Extract, D</td><td>20% Extract, A</td></tr><tr><td>57</td><td>Abstract, B</td><td>20% Extract, A</td><td>Random Extract, C</td><td>30% Extract, D</td></tr><tr><td>58</td><td>Abstract, A</td><td>20% Extract, B</td><td>30% Extract, D</td><td>Random Extract, C</td></tr><tr><td>59</td><td>Abstract, B</td><td>30% Extract, C</td><td>Random Extract, A</td><td>20% Extract, D</td></tr><tr><td>60</td><td>Abstract, B</td><td>30% Extract, A</td><td>20% Extract D</td><td>Random Extract, C</td></tr><tr><td>61</td><td>20% Extract, D</td><td>Random Extract, B</td><td>Abstract, C</td><td>30% Extract, A</td></tr><tr><td>62</td><td>20% Extract, C</td><td>Random Extract, A</td><td>30% Extract, D</td><td>Abstract, B</td></tr><tr><td>63</td><td>20% Extract, C</td><td>Abstract, D</td><td>Random Extract, A</td><td>30% Extract, B</td></tr><tr><td>64</td><td>20% Extract, A</td><td>Abstract, C</td><td>30% Extract B</td><td>Random Extract, D</td></tr><tr><td>65</td><td>20% Extract, B</td><td>30% Extract, C</td><td>Random Extract, D</td><td>Abstract, A</td></tr><tr><td>66</td><td>20% Extract, C</td><td>30% Extract, B</td><td>Abstract, A</td><td>Random Extract, D</td></tr><tr><td>67</td><td>30% Extract, D</td><td>Random Extract, B</td><td>Abstract, A</td><td>20% Extract, C</td></tr><tr><td>68</td><td>30% Extract, C</td><td>Random Extract, A</td><td>20% Extract, B</td><td>Abstract, D</td></tr><tr><td>69</td><td>30% Extract, B</td><td>Abstract, D</td><td>Random Extract, C</td><td>20% Extract, A</td></tr><tr><td>70</td><td>30% Extract, A</td><td>Abstract, C</td><td>20% Extract, D</td><td>Random Extract, B</td></tr><tr><td>71</td><td>30% Extract, D</td><td>20% Extract, A</td><td>Random Extract, B</td><td>Abstract, C</td></tr><tr><td>72</td><td>30% Extract, A</td><td>20% Extract, D</td><td>Abstract, C</td><td>Random Extract, B</td></tr></table>

A-D = the passages; subjects 1–24 were administered the No Extract treatment (1 e . questions only) and subjects 25-48 received the original Full Text treatment

## References

Ackoff, R. L., "Management Misinformation Systems," Management Sctence. 14, 4 (1967). B147–156

Adams, D. A. and I. R. Weiss, “Organızational Connectivity Systems: Is the Function Being Effectively Managed?," Data Base, 20, 1 (1989), 16–20

American National Standards Institute, Inc., 1merican Nattonal Standard for W'ntıng Abstracts ANSI Inc., New York. 1979

Baxendale. P B., “Machine-Made Index for Technical Literature—An Experıment," /BM1 Journal of Research ard Development. 2, 4 (1958), 354–361.

Bernier, C. L., “Abstracts and Abstractıng," in Subject and Informaton . 1nalyss E D. Dym (Ed.), Marcel Dekker. Inc , New York, 1985

Blair, D. C., Language and Representatton in Informaton Retrieval, Elsevier Seience Publications, Am sterdam. 1990.

- , “The Data-Document Distinction in Information Retrieval." Communicattons of the' 4CM. 27, 4 (1984), 369–374.

and M. E. Maron, "An Evaluation of Retrieval Effectiveness for a Full-Text Document Retreval System." Communucattons of the ACM. 28. 3 (1985), 289–299

Borko, H. and C. L. Bernier, Abstracting Concepts and Methods, Academıc Press, New Y ork, 1975

Brancheau, J. C. and J. C. Wetherbe, "Key Issues in Information Systems Management," MIS Quarterly 11, 1 (1987), 23–45

Brookes, C. H. P., "Text Processing as a Tool for DSS Design." in Procesves and Tools for Decrston Support, H. G. Sol (Ed.), North-Holland Publishıng Company, Amsterdam, 1983, 131–138.

Burton, D. and J. Licklider, "Long-Range Constraints in the Statistical Structure of Printed English," American Journal of Psvchology, 68 (1955). 650–653.

Chervany, N. L and G W. Dickson, “An Experimental Evaluation of Intormation Overload ın a Production Envirorment," Management Sctence. 20, 10 (1974), 1335–1344

Cohen, J., Statısttcal Power Analysıs for the Behavtoral Sctences, (Revısed Ed ), Academıc Press, New York, 1977.

Cremmins, E. T., The Art of Abstracttng. ISI Press, Phıladelphia, 1982.

Culnan, M J. and J H. Baır, “Human Communıcation Needs and Organızational Productivıty The Potential Imoact of Office Automation," Journal of the American Soctety for Informaton Science. 34, 3 (1983), 215–221

Daft, R. L., J. Sormunen and D. Parks, "Chief Executives Scannıng. Envıronmental Characterıstics, and Company Performance: An Empirical Study," Strategıc Management Journal, 9. 2 (1988). 123–139.

March 1992

Davıs, G. D. and M. H. Olson, Management Information Systems Conceptual Foundauons, Structure, and Development, (Second Ed.), McGraw-Hill, Inc., New York, 1985

Denning, P., “Electronic Junk," Communications of the ACM, 25, 3 (1982), 163–165.

Dickson, G. W , R. L. Leitheiser, J. C. Wetherbe and M Necıs, “Key Information Systems Issues for the 1980's," MIS Ouarterly, 8, 3 (1984). 135-159.

Dillon, M. and A. S. Gray, “FASIT: A Fully Automated Syntactically Based Indexing System." Journal of the American Society for Information Science, 34, 2 (1983), 99–108.

Edmunson, H. P., “Problems in Automatic Abstracting." Communications of the ACM, 7, 4 (1964), 259-263.

, “New Methods in Automatic Extracting," Journal of the AC'M, 16, 2 (1969), 264–285

- , “Statistical Inference in Mathematical and Computational Linguistics." International Journal of Computer and Information Sciences, 6, 2 (1977), 95–129.

“Mathematical Models of Text," Information Processing and Management, 20, 1–2 (1984), 261-268.

and R. E. Wyllys, “Automatic Abstracting and Indexıng—Survey and Recommendations," Communicatons of the ACM. 4. 5 (1961). 226–234

Educational Testing Service, The Official Gude for GMAT' Revtew, Graduate Management Admıssions Council, Princeton, NJ, 1986

El Sawy, O. A., “Personal Information Systems for Strategıc Scanning in Turbulent Environments: Can the CEO Go On-Line?," MIS Ouarterly, 9, 1 (1985), 53–60

Epstein, S. S., “Transportable Natural Language Processing Through Sımplicity—The PRE System," ACM T'ransacuons on Offce Information Systems, 3, 2 (1985), 107–120.

Ewusi-mensah, K., “The External Organızational Environment and Its Impact on Management Information Systems," Accounting, Organtzattons and Soctety. 6, 4 (1981), 301–316

Goode, H. H., “Greenhouses of Science for Management," Management Sctence, 4, 4 (1958), 365–381.

Gunnıng, R., The Technıque of Clear W'riting. (Revised Ed.), McGraw-Hill, New York, 1968

Hale, D. P, J. E. Hurd and G M. Kasper, “A Knowledge Exchange Architecture for Collaborative Human-Computer Communication." IEEE Transactions on Systems, Man, and Cybernetics, (1991) (forthcoming).

and G. M. Kasper, “The Effect of Human-Computer Interchange Protocol on Decision Performance," Journal of Management Information Systems, 6, 1 (1989), 5–20.

Heidorn, G. E., K. Jensen, L. A. Miller, R J. Byrd and M. S. Chodorow, "The EPISTLE Text-Critiquing System," IBM Systems Journal, 21, 3 (1982), 305–326.

Hiltz, S. R. and M. Turoff, “Structurıng Computer-Mediated Communication Systems to Avoıd Information Overload," Communicattons of the 4C'M, 28, 7 (1985), 680–689

Horton, R. L , The General Linear Model, McGraw-Hill, Inc., New York, 1978

Jacobs, P. S. and L. F. Rau, “SCISOR: Extracting Information from On-Line News," C'ommunicatons of the .A4CM, 33, 11 (1990), 88–97

Kahneman, D., Attention and Effort, Prentice-Hall, Inc , Englewood Cliffs, NJ, 1973

Kasper, G. M. and A H. Morrıs, “The Effect of Presentation Media on Recipient Performance in Text-Based Information Systems," Journal of Management Information Systems, 4, 4 (1988), 25–43.

Kerr, E B. and S R Hiltz, Computer-Medıated Communıcaton Systems Status and Evaluation, Academic Press, New York, 1982.

Kibby, M. W., "Intersentential Processes in Reading Comprehension," Journal of Readıng Behavtor, 12, 4 (1980), 299–312.

Kiesler, S., J. Siegel and T. M. McGuire, “Social Psychological Aspects of Computer-Mediated Communı- cation,"4merican Psychologist, 39, 10 (1984), 1123–1134.

Kirtz, M. K. and D. C Reep, “A Survey of the Frequency, Types, and Importance of Writing Tasks in Four Career Areas," The Bullettn, 53, 4 (1990), 3–4.

Kolodziej, S., "Where Is the Electronıc Messaging Explosion?," Cornputerworld Focus, 19, 41A (October 16, 1985), 21–23.

Kriebel, C H. and D. M. Strong, “A Survey of the MIS and Telecommunications Activities of Major Business Firms," MIS Quarterly. 8, 3 (1984), 171–178

Luhn, H. P., "The Automatic Creation of Literature Abstracts," IBM Journal of Research and Develop ment, 2, 2 (1958a). 159–165.

, “A Business Intelligence System." IBM1 Journal of Research and Development, 2, 4 (1958b) 314-319

Mandell, J., Magazine W'ruters Nonfctton Guidelines, McFarland and Company, Inc., Jefferson, NC, 1987.

Mathis, B. A.. J. E., Rush and C. E. Young, “Improvement of Automatic Abstracts bv the Use ofStructural Analysıs." Journal of the American Society of Informaton Science. 24 (1973). 101–109.

Miller, L. A., “Project EPISTLE: A System for the Automatic Analysis of Business Correspondence," Proceedıngs of the First 1nnual Nattonal Conference on 4rtificial Intelligence. Stanford Unıversity, 1980, 280–282.

, G. E. Heidorn and K. Jensen. “Text-Critiquıng with the EPISTLE System: An Author's Aıd to Better Syntax,"AFIPS Conference Proceedings, AFIPS Press, Arlington, VA, 1981, 649–655

Mintzberg, H. D. Raisinghanı and A. Theoret, "The Structure of' Un-structured' Decision Processes." 1dmunıstratve Science Quarterly. 21, 2 (1976), 246–275

Morris. A. H., “Supporting Envıronmental Scanning and Organizational Communication with the Processing of Text: The Use of Computer-Generated Abstracts." Unpublıshed Ph D Dissertation, Texas Tech Unıversity, 1988

Neff, G. T , 1991 W'riter's Market W'here and How to Sell W'hat You W'rute, Wrnter's Digest Books, Cincınnat, OH, 1990

Paice, C. D., Informatton Retrieval and the C'omputer, MacDonald and Jane's, London, 1977.

- , "T he Automatic Generation of Literature Abstracts: An Approach Based on the Identification of Self-indicating Phrases," in Informatton Retrteval Research Oddy, R N., Robertson, S E , van Rijsbergen, C. J., and Willams, P W. (Ed.), Butterworths. London, 198

Peterson, F. and J. Kesselman-Turkel, The Magazıne H'rıter's Handhook. Dodd, Mead and Company, New York, 1987.

Pollock, J. J. and A. Zamora, "Automatic Abstracting Research at Chemical Abstracts."Journal of Chemtcal Informction and Computer Sctence, 15, 4 (1975), 226-232

Rappaport, A., "Management Misinformation Systems—Another Perspecuve," Management Science, 15, 4 (1968), B133-136

Rice, R. E and J. H Bair, "New Organızational Medıa and Productivıt." ın The New Medıa. R. E. Rice (Ed.), Sage Publications, Beverly Hills, CA, 1984, 185–215

Rush, J. E , R Salvador and A Zamora, “Automatıc Abstracting and Indexıng. II. Production of Indıcative Abstracts by Application of Contextual Inference and Syntactic Coherence Criteria," Journal of the Amertcan Society for Information Science, 22 (1971). 260–274

Salton, G., Au'omatic Text Processung The Iransformaton, Analysts, and Reteval of Information by Computer. Addison-Wesley, Readıng, MA, 1989

Schrıber, J., "Move Over, Strunk and White," Forbes, (August 15, 1983), 100–101.

Schroder, H. M . M J. Driver and S. Streufert, Ihunan Informatton Procesuing, Holt, Rinehart, and Winston, New York, 1967.

Schwartz, R., J., Fortune and J. Horwich, “AMANDA: A Computerized Document Management Sys tem," MIS Quarterly. 4, 3 (1980). 41–49.

Shannon, C E., “Prediction and Entropy of Printed Enghısh," Bell Systems 1 echntcal Journal, 30 (1951), 50-64

Slonim. J , L J. MacRae, W. E. Mennie and N. Diamond, “NDX-100: An Electronıc Filing Machine for the Office of the Future," Computer. (May 1981), 24-36.

Smeaton, A. F and C. J. van Rıjsbergen, "Information Retrieval ın an Office Filıng Facılity and Future Work in Project Minstrel," Informatton Processıng and Management, 22, 5 (1986), 135–149

Swanson, D. R., “Information Retrieval as a Trial-and-Error Process," Lhrarr Quarter/y, 47, 2 (1977), 128-148.

Swanson, E. B. and M. J. Culnan, “Document-Based Systems for Management Planning and Control: A Classification, Survey, and Assessment," MIS Quarterly, 2, 4 (1978), 31–46.

Taylor, S. L. and G. K. Krulee, “Experiments with an Automatic Abstracting System," in Informatton Management in the 1980's, Proceedings of the ASIS Annual Meetng 1 ol 14, Knowledge Industry Publications, White Plains, NY, 1977, 83.

Tsichritzis, D., “Message Addressing Schemes," ACM I'ransactions on Ofue Inforimaton Svstems. 2, 1 (1984), 58-77.

van Rijsbergen C. J., Informatton Retrieval, (2nd Ed.), Butterworths, London, 1979.

Weil, B H., “Standards for Writing Abstracts." Journal of the Amerı an Society for Information Science. 21, 5 (1970), 351–357.

Wiener, N , Cyberneucs or Control and Communtcation in the Animal and the Machine (2nd Ed.). The MIT Press and John Wiley & Sons, Inc., New York, 1961
