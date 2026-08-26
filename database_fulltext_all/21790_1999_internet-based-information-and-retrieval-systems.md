---
otero_id: 21790
otero_key: "GDASTD6V"
title: "Internet-based information and retrieval systems"
authors: "Daniel E O'Leary"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00054-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com<sup>r</sup>locate<sup>r</sup>dsw

# Internet-based information and retrieval systems

Daniel E. O’Leary )

Marshall School of Business, UniÕersity of Southern California, Los Angeles, CA 90089-1421, USA

## Abstract

There is limited reliability of internet-based information systems. For example, Internet search engines provide results that have limited reliability and data available on the Internet is limited in its reliability. As a result, the purpose of this paper is to elicit sources of the lack of reliability, develop a model that can be used to study the impact of reliability and propose some solutions to mitigate reliability issues. The model couches Internet data as an ‘‘intermediary report.’’ For example, use of a search engine will generate an intermediary ‘‘report’’ providing a list of relevant universal resource locators URL andŽ . a corresponding brief description that may or may not correctly describe the label being searched. This ‘‘report’’ structure is used to model Internet information and retrieval systems as an intermediate step between users of the system and the original or expected information. The basic model of information relevance in the information retrieval process is reviewed, where the precision is a function, in part, of the recall and fallout rate. Reliability is found to have an impact on precision and fallout rates. Alternatives are proposed to mitigate the impact of this lack of reliability. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Internet; Information retrieval; Reliability

## 1. Introduction

The purpose of this paper is to investigate issues of reliability of internet-based information and retrieval systems, including data such as ‘‘home pages’’. The paper elicits issues that cause a concern for reliability. Then this paper investigates one model of that reliability to find that in some settings reliability has a major impact on issues such as relevance. A probability model is used to study the impact of unreliable information on traditional information retrieval measures, in order to help establish alternative optimal strategies that account for reliability. In addition, this paper briefly explores some potential approaches to mitigating particular reliability issues.

There has been substantial analysis of the quality of information systems, with an investigation of concepts such as precision, recall and fallout, discussed further below. As a result, the primary focus of information retrieval has been on the releÕance of the information retrieved. However, with internetbased information systems there is an additional concern that has received little attention. Oftentimes databases on the Internet are administered locally, where administrators have limited resources and do not have accountability for the quality of the information. As a result of these and other concerns, Internet information retrieval systems can result in information that may not be as reliable as data in other settings.

As an example, using LYCOS yielded the following erroneous information

Electronic Commerce Course Cases Page

International Journal of Intelligent Systems in Accounting, Finance and Management IJISAFM :( ) Call for Papers Editor: Daniel E. O’Leary UniÕ. http:<sup>rr</sup>www.usc.edu<sup>r</sup>dept<sup>r</sup>sba<sup>r</sup>atisp<sup>r</sup>AI<sup>r</sup> IJISAFM<sup>r</sup>call-for.htm

In actuality, the description is one of a call for papers in artificial intelligence and the real hyperlink address for the label ‘‘Electronic Commerce Course Cases Page’’ is http:<sup>rr</sup>www.usc.edu<sup>r</sup>dept<sup>r</sup>sba<sup>r</sup> atisp <sup>r</sup> ec <sup>r</sup> cases <sup>r</sup> case2.htm. For some reason, whether it was because of the information submitted or the processing of submitted information, the search engine has incorrect descriptor and universal resource locator URL information. In this case theŽ . actual information on ‘‘Electronic Commerce Course Cases Page’’ is not the same as the report contained in the search engine.

As a result, in order to address the issue of reliability, internet information retrieval systems are modeled as an intermediate step between the origi nal ‘‘correct’’ information to be retrieved e.g., theŽ ‘‘correct’’ descriptor and URL for electronic commerce course page , and the actual information which. is available to be retrieved and the user of the information e.g., the wrong information about theŽ call for papers . Ultimately, information retrieved is. a computer-based ‘‘report’’ using the aÕailable information in its database. The available retrieved information is only a representation of the original text. That representation may be a URL, a few key words, the system’s version of an abstract, the system’s version of the entire text or the system may not actually have a version of the text. Requests are made of search engines and addresses and descriptors are provided to the users. The responses to the queries are ‘‘reports’’ that may or may not differ from the actual data.

In any case, the relationship between the available version and the original text will be used to model the reliability of the system. Reliability is introduced by distinguishing between the report of information available to the system and the correct version of the original documents or sources of information by the user. In particular, if the system’s version is $\mathbf { \boldsymbol { x } } \#$ and the actual version is x, then Pr xŽ a<sup><</sup>x will be used to. represent the reliability of the representation.

## 2. Limited reliability of internet information systems

There are a number of reasons why Internet information systems can have limited reliability, i.e., why Pr xŽ a<sup><</sup>x is not 1, including errors, ontological differ-. ences, asymmetric knowledge, developer motives, limited resources and expertise, limited accountability and changes in referenced pages.

## 2.1. Errors on web pages

Perhaps the most apparent source of reliability problems in Internet information systems is errors. These errors can be generated through typing, mapping the directories incorrectly and other types of errors. Errors can be made in data available on web pages; errors can be made in the links from one page to another. In the following example, hyperlinks on a home page are apparently mislabeled bringing the visitor to a different location than expected. At the web page http:<sup>rr</sup>www.usc.edu<sup>r</sup>dept<sup>r</sup>sba<sup>r</sup>atisp<sup>r</sup> AI<sup>r</sup>research<sup>r</sup>ai-reeng.htm there is a link to a ‘‘Call for Papers . . . ’’, however, that link does not connect to a general call for papers, but instead is connected to the AAAI Special Interest Group on AI in Business, http:<sup>rr</sup>www.usc.edu<sup>r</sup>dept<sup>r</sup>sba<sup>r</sup>atisp<sup>r</sup>AI<sup>r</sup> AI-Bus<sup>r</sup>sigaibus.htm.

## 2.2. Errors with search engines

As seen in the ‘‘Electronic Commerce’’ example in the introduction, errors can penetrate search engines. Errors can be made in search engine queries; errors can be made in information reported to search engines; and search engines can make errors indexing pages. Internet search engines index pages using a number of approaches, such as keywords provided by developers or by human indexers, or generated by web crawlers. In any case, errors or omissions can be introduced into the system, because of the frailties of humans and software. Such limitations can include erroneous information provided to search engines or problems with processing information submitted to search engines.

## 2.3. Ontological differences

Internet databases cover a wide range of topics, possibly leading to different definitions of terms by users and developers, ‘‘ontological differences.’’ For example, as noted in his speech to the 1995 AAAI Fall Symposium Workshop on Knowledge NaÕigation, Tom Gruber’s home page has the ‘‘misleading’ Ž . different ontology? verbiage ‘‘Nude Photos In response to user requests . . . ’’ Ž http:<sup>rr</sup> wwwksl.stanford.edu<sup>r</sup>people<sup>r</sup>gruber<sup>r</sup>index.html . . . as of 4<sup>r</sup>15<sup>r</sup>98 . The link leads to some pictures of cats . Žhttp:<sup>rr</sup> www-ksl.stanford.edu <sup>r</sup> people <sup>r</sup> gruber <sup>r</sup> photos<sup>r</sup> and http:<sup>rr</sup>www-ksl.stanford.edu<sup>r</sup>people <sup>r</sup>gruber<sup>r</sup>photos<sup>r</sup>10-c-portrait.gif ., probably not what most visitors would be expecting.

Users may have an alternative meaning for terms established in the ontology. For example, many people might think that a CPA could refer to a ‘‘certified public accountant,’’ while others according toŽ the ‘‘Style Guide’’ of the IEEE Computer Society. would think it refers to ‘‘computer press association.’’ Experimental studies, such as Zunde and Dexter 7 , have found that different human<sup>w</sup> <sup>x</sup> indexers frequently will index the same document differently. As a result, the same page is likely to be indexed differently by different developers. In addition, the same indexer will index the same document differently at different times. Such differences can be the result of different ontologies and can result in descriptors not meaning what investigators expect.

Further, some search engines employ an ontology to aid the search. As noted by Yahoo! a query can result in multiple different meanings depending on the ontology. For example,

A Yahoo! Web site match is listed within the category that contains it. This offers you the opportunity to go directly to the site, or to click on the category for a list of related sites. If you’re not searching for something specific, we suggest the latter. Again, Yahoo! categories can yield a number of worthwhile options.

Alternative ontologies can result in differences between x and xa.

2.4. Asymmetric knowledge between database user and deÕeloper

As noted by Brown et al. 1 , there is asymmetric<sup>w</sup> <sup>x</sup> knowledge between suppliers and users of information on the Internet. Asymmetric knowledge allows a developer to deliberately ‘‘mislabel’’ homepage links in order to accomplish particular objectives, such as guiding a user to see particular home page material or advertising. Such deliberate mislabeling would result in reliability concerns where x was not the same as xa.

## 2.5. DeÕeloper motiÕes

There are a wide range of motives attributed to the generation of web pages, e.g., in order to provide some set of information or just as fun. Further, as seen by the many visitor counters that typically are on home pages, a number of developers apparently want to attract visitors to their pages. Brown et al. 1<sup>w</sup> <sup>x</sup> suggests that information can be misrepresented in order to generate visitors to web pages. Such misrepresentation could result in reliability concerns where x was not the same as xa.

## 2.6. Limited resources and expertise

Many Internet databases are developed and maintained by a single developer or by small companies. Since there may not be supporting organizations, developers can face resource constraints. Further, developers are limited to their own expertise and learning capabilities. These limitations can manifest themselves as limitations to the reliability of the information.

## 2.7. Limited accountability

Developers of internet-based databases have limited accountability for the databases that they generate. Use of internet-based databases often is a buyer or user beware setting. Information is frequently available at no cost, but there is no guarantee as to the quality or reliability of the information. As a result, even when errors are found, there may be no incentives to fix the errors. Accordingly, this can influence the reliability of the system.

## 2.8. Changes in referenced pages

Pages need to be updated over time. As pages are updated, their relationship to other pages can change and the pages that they reference may change. Since there is not likely to be a reciprocal arrangement between page developers to send information about page changes to developers of pages who reference their page, addresses and content can change without the referencing page developer knowing. As a result, in this setting, reliability can be impacted because of changes outside the control of the referencing page developer.

## 3. Performance measures and a relevance model of information retrieval

This paper couches its analysis in a classic information retrieval model 6 , that allows extension to<sup>w</sup> <sup>x</sup> the examination of the impact of reliability. That model assumes a retrieved data item is either relevant R to the user or it is not relevant NR . TheŽ . Ž . model also assumes that, if ‘‘we have a set of documents 6 , p. 557 that the criteria for selectionŽ<sup>w</sup> <sup>x</sup> . indicate either the document data item should be selected S or not selected NS .’’Ž . Ž .

There are a number of performance measures used by system designers to measure the effectiveness of information retrieval in the context of this model. These measures include the ‘‘precision,’ ‘‘recall,’’ and ‘‘fallout.’’ Precision also is referred to as ‘‘acceptance rate’’, recall sometimes is referred to as ‘‘hit rate’’ and the fallout often is called ‘‘type II error’’ or ‘‘false drop’’ 2,5 . <sup>w</sup> <sup>x</sup>

Let Pr a be the probability of a and let Pr a andŽ . Ž b be represented as Pr a,b . In the context of the . Ž . model used in this paper, the precision is equal to Pr R S , the recall is equal to Pr S R and type IIŽ <sup><</sup> . Ž <sup><</sup> . error is Pr S NR . Salton 3 has noted that in aŽ <sup><</sup> . <sup>w</sup> <sup>x</sup> situation where there is an inverse trade-off between the precision and recall, users tend to favor precision maximizing searches. The rationale behind this choice is that, particularly in very large databases, these types of searches would yield a smaller, yet relevant set of documents. The primary focus here is on the precision, but, recall and fallout also are examined.

Table 1  
Costs of information retrieval

<table><tr><td></td><td>Relevant</td><td>Not relevant</td></tr><tr><td>Select</td><td>V1</td><td>K1</td></tr><tr><td>Not select</td><td>K2</td><td>V2</td></tr></table>

Associated with the design of an information retrieval system are some costs and values to the user. Using the cost notation of Swets 5 , V1 is the<sup>w</sup> <sup>x</sup> value to the user of retrieving a relevant item; V2 is the value of not retrieving an irrelevant item; K1 is the cost of retrieving a non-relevant item; K2 is the cost of failing to retrieve a relevant item. The user incurs V2 because by not retrieving the item the user does not lose time investigating the item. K1 is a cost because the user will spend time investigating a non-relevant item. K2 is an opportunity cost of not examining a relevant item. These costs and values are summarized in Table 1.

Verhoeff et al. 6 developed a model that indi-<sup>w</sup> <sup>x</sup> cates that the information system retrieval system is maximized if the probability of relevance Pr R isŽ Ž .. greater than a critical probability $\mathrm { P C R } = \left( \mathrm { K } 1 + \right.$ $\nabla 2 ) / ( \mathrm { K } 1 + \mathrm { K } 2 + \mathrm { V } 1 + \mathrm { V } 2 )$ . That model is developed as follows. Let p equal the probability that the item is relevant and $( 1 - p )$ equal the probability that the item is not relevant. The critical probability at which the costs and benefits of retrieving and not retrieving are equal is $p \mathbf { V } 1 - ( 1 - p ) \mathbf { K } 1 = - p \mathbf { K } 2 + \mathbf { \Lambda }$ $( 1 - p ) \mathrm { V } 2$ . Thus, the above relationship holds. This result is not new, but the critical point nature of the process is important to the results established later in the paper. However, if only the prior probability Ž Ž .. Pr R is used then that ignores the direct search of the database by the user. Bayes’ Theorem can be used to relate the posterior probability, the precision and in general Pr R x , to the prior probability that Ž <sup><</sup> . the item is relevant, $P ^ { \prime } = \mathrm { P r } ( \mathbf { R } )$ prior to our observa-Ž tion of x, the direct inspection of the system yielding indications that we should select or not select the item ..

$$
\begin{array}{l} P = \operatorname * {P r} (\mathrm{R} | \mathrm{x}) \\ \operatorname * {P r} (\mathrm{R} | \mathrm{x}) = \operatorname * {P r} (\mathrm{R}, \mathrm{x}) / \operatorname * {P r} (\mathrm{x}) \\ \operatorname * {P r} (\mathrm{R} | \mathrm{x}) = \left[ \operatorname * {P r} (\mathrm{x} | \mathrm{R})   P ^ {\prime} \right] / \left[ \operatorname * {P r} (\mathrm{x} | \mathrm{R})   P ^ {\prime} \right. \\ \qquad \qquad \qquad + \operatorname * {P r} (\mathrm{x} | \mathrm{NR}) (1 - P ^ {\prime}) \big ]. \\ \operatorname * {P r} (\mathrm{R} | \mathrm{x}) = P ^ {\prime} / \left[   P ^ {\prime} + (1 - P ^ {\prime})   L (\mathrm{x})   \right], \end{array}\tag{1}
$$

$$
L (\mathrm{x}) = \operatorname * {P r} (\mathrm{x} | \mathrm{NR}) / \operatorname * {P r} (\mathrm{x} | \mathrm{R})\tag{2}
$$

Thus, for x <sup>s</sup> S, the precision Pr R S is related to Ž <sup><</sup> . $L ( \mathbf { S } ) = \mathrm { P r } ( \mathbf { S } \| \mathbf { N R } ) / \mathrm { P r } ( \mathbf { S } | \mathbf { R } )$ , which is the ratio of the fallout to recall. LŽ . S is the ratio analyzed by Swets <sup>w</sup> <sup>x</sup> <sub>5</sub> <sub>.</sub>

The retrieval information changes the prior probability $( \mathbf { P } ^ { \prime } = \operatorname* { P r } ( \mathbf { R } ) )$ that the item is relevant to yield $P = \mathrm { P r } ( \mathbf { R } | \mathbf { x } )$ . If Pr R x exceeds the critical valueŽ <sup><</sup> . then it is desirable to retrieve the data item. Thus, if there is reason to suppose that LŽ . x is understated or overstated for any reason, such as reliability, then the cutoff nature of the process can lead to inappropriate decision being made. Extension of this model provides the basis of the discussion in the next section.

## 4. Modeling reliability

Unfortunately, in the above model, as noted in Verhoeff et al. 6 , ‘‘we assume that the inquirer<sup>w</sup> <sup>x</sup> expects a certain reference list, namely the one he would have procured had he himself probed the documents in the set.’’ However, as noted in the ‘‘Electronic Commerce’’ example discussed above, the information retrieval system reports on information it has retrieved from its database, it does not retrieve perfectly from the entire set of feasible source documents. Thus, the information system reports a value IS i.e., the information system sug- Ž gests that the data item be selected — it does not. provide S. Alternatively, the information system reports a value of INS Ž . not selected rather than NS. Mathematically, the distinction between the report of the evidence xŽ . a from the system and the actual occurrence in the original data x can be introducedŽ . into the probability Pr R xŽ <sup><</sup> a. by introducing it into the only factor that includes the variable x, LŽ . x . Let $\mathbf { x } ^ { \prime } = \mathbf { \cdots } \mathbf { n o t } ~ \mathbf { x } . ^ { \prime }$

Lemma 1 ŽBased on Schum and Du Charme 4<sup>w</sup> <sup>x</sup>. $( \mathrm { x } \# ) \ = \ [ \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { N R } , \mathrm { x } ) ) \mathrm { P r } ( \mathrm { x } | \mathrm { N R } ) \ + \ \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { N R } , \mathrm { x } ^ { \prime } ) )$ $\mathrm { P r } ( \mathrm { x } ^ { \prime } | \mathrm { N R } ) ] / \left[ \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { R } , \mathrm { x } ) ) \mathrm { P r } ( \mathrm { x } | \mathrm { R } ) + \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { R } , \mathrm { x } ^ { \prime } ) ) \mathrm { P r } \right.$ x R . <sup><</sup> .<sup>x</sup>

Proof $L ( \mathrm { x } \# ) = \operatorname* { P r } ( \mathrm { x } \# | \mathrm { N R } ) / \operatorname* { P r } ( \mathrm { x } \# | \mathrm { R } ) = [ \operatorname* { P r } ( \mathrm { x } \# ,$ $\mathrm { N R ) / P r \ ( N R ) ] / [ P r ( x \# , R ) / P r ( R ) ] } \ = \ [ \{ \operatorname* { P r } ( x \# , x , N R )$ $+ \mathrm { P r } ( \mathrm { x } \# , \mathrm { x } ^ { \prime } , \mathrm { N R } ) \} / \mathrm { P r } ( \mathrm { N R } ) ] / [ \{ \mathrm { P r } ( \mathrm { x } \# , \mathrm { x } , \mathrm { R } ) + \mathrm { P r }$ $\begin{array} { r l r } { ( \mathrm { x } \# , \mathrm { x } ^ { \prime } , \mathrm { R } ) \} / \mathrm { P r } ( \mathrm { R } ) ] } & { { } = } & { [ \{ \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { N R } , \mathrm { x } ) ) \mathrm { P r } ( \mathrm { x } | \mathrm { N R } ) \mathrm { P r } }  \end{array}$ $\mathrm { ( N R ) } + \mathrm { P r } ( \mathrm { x } \# | \mathrm { ( N R , x ' ) } ) \mathrm { P r } ( \mathrm { x } ^ { \prime } | \mathrm { N R } ) \mathrm { P r } ( \mathrm { N R } ) \} / \mathrm { P r } ( \mathrm { N R } ) ] /$ $[ \{ { \mathrm { P r } } ( \mathrm { x } \# | { \mathrm { ( R , x ) } } ) { \mathrm { P r } } ( \mathrm { x } | \mathrm { R } ) { \mathrm { P r } } ( \mathrm { R } ) + { \mathrm { P r } } ( \mathrm { x } \# | { \mathrm { ( R , x ' ) } } ) { \mathrm { P r } } ( \mathrm { x } ^ { \prime } | \mathrm { R } )$ $\mathrm { P r } ( \mathrm { R } ) \} / \ \mathrm { P r } | ( \mathrm { R } ) ] \ = \ [ \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { N R , x } ) ) \mathrm { P r } ( \mathrm { x } | \mathrm { N R } ) + \mathrm { P r }$ $( \mathrm { x } \# | ( \mathrm { N R } , ~ \mathrm { x } ^ { \prime } ) ) \mathrm { P r } ( \mathrm { x } ^ { \prime } | \mathrm { N R } ) ] / [ \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { R } , \mathrm { x } ) ) \mathrm { P r } ( \mathrm { x } | \mathrm { R } ) + \mathrm { P r }$ $( \mathrm { x } \# | ( \mathrm { R } , \mathrm { x } ^ { \prime } ) ) \mathrm { P r } ( \mathrm { x } ^ { \prime } | \mathrm { R } ) ] / /$

The factors in LŽ .xa that relate to $\operatorname* { P r } ( \mathrm { x } \# | . )$ reflect what Schum and Du Charme 4 refer to as the<sup>w</sup> <sup>x</sup> reliability of the reported evidence. If $\operatorname* { P r } ( \mathbf { x } \# | ( \mathbf { N R } , \mathbf { x } ) )$ <sup>s</sup>1 and $\mathrm { P r } ( \mathbf { \boldsymbol { x } } \# | ( \mathrm { N R } , \mathbf { \boldsymbol { x } } ^ { \prime } ) ) = 0$ and if $\mathrm { P r } ( \mathbf { \boldsymbol { x } } \# | ( \mathbf { \boldsymbol { R } } , \mathbf { \boldsymbol { x } } ) ) = 1$ and $\mathrm { P r } ( \mathbf { \boldsymbol { x } } \# | ( \mathbf { \boldsymbol { R } } , \mathbf { \boldsymbol { x } } ^ { \prime } ) ) = 0$ then $L ( \mathbf { x } ) = L ( \mathbf { x } \# )$ . The report would be 100% reliable. Then the model in Lemma 1 would reduce to model 2 . However, ifŽ . $\operatorname* { P r } ( \mathbf { x } \# | ( \mathbf { N R } , \mathbf { x } ^ { \prime } ) )$ and $\operatorname* { P r } ( \mathbf { x } \# | ( \mathbf { R } , \mathbf { x } ^ { \prime } ) )$ are not zero and <sup>r</sup>or $\operatorname* { P r } ( \mathbf { x } \# | ( \mathbf { N R } , \mathbf { x } ) )$ and $\displaystyle \operatorname* { P r } ( \mathbf { x } \# | ( \mathbf { R } , \mathbf { x } ) )$ are less than one, then there is non-zero probability that the reported value is dependent on either the relevance R of theŽ . item, the actual value of the occurrence x , or both.Ž .

## 4.1. Reliability assumptions

The model in Lemma 1 has four different reliability parameters. In order to make the discussion more tractable and to focus on the impact of reliability, one special case of $\operatorname* { P r } ( \mathbf { x } \# | . )$ will be analyzed. The assumption on reliability is that the probability distribution of the reported version of x, xa, is not dependent on probability distribution of the status of whether or not a document is relevant NR or R andŽ . that Pr xŽ a <sup><</sup>x is symmetric, i.e.,. $\operatorname* { P r } ( \mathbf { x } \# | \mathbf { x } ) =$ $\operatorname* { P r } ( \mathbf { x } \# ^ { \prime } | \mathbf { x } ^ { \prime } ) = r .$ . In this case there is a certain amount of confusion as to whether x or $\mathbf { \boldsymbol { x } } ^ { \prime }$ actually occurs. These probabilities are summarized in Table 2. The impact of this assumption is summarized in Theorem 1. Although the remainder of this paper is concerned with symmetric probabilities, the results can be extended to asymmetric and other types of probabilities.

Table 2  
Symmetric reliability probabilities<sup>a</sup>

<table><tr><td rowspan="2">Reported value $^{\mathrm{c}}$ </td><td colspan="2">Actual value $^{\mathrm{b}}$ </td></tr><tr><td>S</td><td>NS</td></tr><tr><td>IS</td><td>r</td><td>1-r</td></tr><tr><td>INS</td><td>1-r</td><td>r</td></tr></table>

<sup>a</sup> With symmetric reliability the probabilities are independent of whether the system is R relevant or NR not relevant .Ž . Ž . $^ { \mathrm { b } } \mathrm { S }$ and NS refer to the states ‘‘select the data item’’ and ‘‘do not select the data item,’’ assuming there is direct access to original documents or system access to perfect representation of original. <sup>c</sup> IS and INS refer to the states ‘‘information system indicates that data item should be selected’’ and ‘‘information system suggests that data item not be selected.’’ ..

Theorem 1 If reliability is symmetric and $I \geq r \geq 0 ,$ then, $L ( x \# ) = L ( r , x ) = \left. \int r P r ( x | N R ) + ( I \ : - \right.$ $r ) ( P r ( x ^ { \prime } | N R ) J / [ r P r ( x | R ) + ( I - r ) ( P r ( x ^ { \prime } | R ) J $

Proof by Lemma $1 , L ( \mathrm { x } \# ) = [ \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { N R } , \mathrm { x } ) ) \mathrm { P r }$ $( \mathrm { x } | \mathrm { - N R } ) + \operatorname* { P r } ( \mathrm { x } \# | ( \mathrm { N R , x ^ { \prime } } ) ) \mathrm { P r } ( \mathrm { x } ^ { \prime } | \mathrm { N R } ) ] / [ \operatorname* { P r } ( \mathrm { x } \# | ( \mathrm { R , x } ) ) $ $\mathrm { P r } ( \mathrm { x } | \mathrm { R } ) + \mathrm { P r } ( \mathrm { x } \# | ( \mathrm { R } , \mathrm { x } ^ { \prime } ) ) \mathrm { P r } ( \mathrm { x } ^ { \prime } | \mathrm { R } ) ] \mathrm { I f }$ we assume that the reported version of x, xa, is not dependent on whether the data is relevant or not relevant then $L ( \mathbf { \boldsymbol { x } } \# ) = [ \operatorname* { P r } ( \mathbf { \boldsymbol { x } } \# | \mathbf { \boldsymbol { x } } ) \mathbf { P r } ( \mathbf { \boldsymbol { x } } | \mathbf { N R } ) + \operatorname* { P r } ( \mathbf { \boldsymbol { x } } \# | \mathbf { \boldsymbol { x } } ^ { \prime } ) \mathbf { P r } ( \mathbf { \boldsymbol { x } } ^ { \prime } | \mathbf { N R } ) ] / \binom { } { }$ <sup>w</sup> Ž <sup><</sup> . Ž <sup><</sup> . Ž <sup><</sup> . Ž Pr xa x Pr x R <sup>q</sup> Pr xa x Pr x R Since reliabil-<sup><</sup> .<sup>x</sup> ity is symmetric $r = \operatorname* { P r } ( \mathbf { x } \# | \mathbf { x } )$ and $1 - r = \operatorname* { P r }$ $( \mathbf { x } \# | \mathbf { x } ^ { \prime } ) . / \prime$

Thus, in the case of symmetric reliability, $\mathrm { P r } ( \mathrm { R } | \mathrm { x } \# ) = P ^ { \prime } / [ P ^ { \prime } + ( 1 - P ^ { \prime } ) \dot { L } ( \mathrm { x } \# ) ]$ . The precision of the information retrieval system becomes, $\mathrm { P r } ( \mathrm { R } | \mathrm { I S } ) = P ^ { \prime } / [ P ^ { \prime } + ( 1 - P ^ { \prime } ) L ( \mathrm { I S } ) ]$ . The recall becomes $\operatorname* { P r } ( \mathrm { I S } | \mathrm { R } ) = ( [ r \operatorname* { P r } ( \mathrm { S } | \mathrm { R } ) + ( 1 - r ) ( \operatorname* { P r } ( \mathrm { N S } | \mathrm { R } ) ] .$ The fallout rate becomes $\mathrm { P r } ( \mathrm { I S } | \mathrm { N R } ) = [ r \mathrm { P r } ( \mathrm { S } | \mathrm { R } ) + ( 1 $ $- \ r ) ( \mathrm { P r } ( \mathrm { N S } | \mathbf { R } ) ]$ . The behavior of LŽ .xa and $\operatorname* { P r } ( \mathbb { R } | \mathbf { x } \# )$ , as a function of the reliability level is illustrated in an example later in the paper. However, it is important to note $L ( \mathbf { x } \# )$ Ž and, thus, Pr R x<sup><</sup> a. are highly sensitive to reliability.

4.2. The impact of reliability on recall and fallout rate

The reliability model introduced in Section 3 has an impact on both the recall and the fallout rate. Let the recall at reliability r be expressed as $H ( r )$ and the fallout rate be $F ( r )$

Theorem 2 — recall $L e t \ r ^ { \prime \prime }$ and r be two different reliability leÕels, $r ^ { \prime \prime } > r ^ { \prime } . ( a )$ If $P r ( S | R ) > 0 . 5$ then $H ( r ^ { \prime \prime } ) > H ( r ^ { \prime } )$ ( ) , b If $P r ( S | R ) < 0 . 5$ then $H ( r ^ { \prime \prime } ) <$ $H ( { \boldsymbol { r } } ^ { \prime } )$

ProofŽ . a Proof by contradiction. Assume that $\mathrm { P r } ( \mathbf { S } | \mathbf { R } ) > 0 . 5$ and $H ( r ^ { \prime \prime } ) < H ( r ^ { \prime } )$ . Thus, $r ^ { \prime \prime } \mathrm { P r } ( \mathbf { S } | \mathbf { R } )$ $+ \ ( 1 \ - \ \mathbf { r } ^ { \prime \prime } ) \mathbf { P r } ( \mathbf { N S } \mid \mathbf { R } ) \ \leq \ r ^ { \prime } \mathbf { P r } ( \mathbf { S } \mid \mathbf { R } ) \ + \ \left( 1 \ - \ \right.$ $r ^ { \prime } ) \mathrm { P r } ( \mathrm { N S } | \mathrm { R } ) r ^ { \prime \prime } [ 2 \mathrm { P r } ( \mathrm { S } | \mathrm { R } ) - 1 ] \leq r ^ { \prime } [ 2 \mathrm { P r } ( \mathrm { S } | \mathrm { R } ) - 1 ] \mathrm { B u t } ,$ since $r ^ { \prime \prime } > r ^ { \prime }$ and Pr $\mathbf { ( S | R ) } > 0 . 5$ there is a contradiction. b Similar to partŽ . $\mathsf { a . / / }$

Theorem 3 — fallout rate Let $r ^ { \prime \prime }$ and r be two different reliability leÕels, $r ^ { \prime \prime } > r ^ { \prime } . ( a )$ If $P r ( S | N R ) >$ 0.5 then $F ( r ^ { \prime \prime } ) > F ( r ^ { \prime } )$ . b If ( ) $P r ( S | N R ) < 0 . 5$ then $F ( r ^ { \prime \prime } ) < F ( r ^ { \prime } )$

## Proof — Similar to Theorem 2.<sup>rr</sup>

These two theorems indicate that by not taking into account the reliability of the information retrieval system, the fallout rate and the recall can be underestimated or overestimated. Assuming that the reliability was not accounted for, i.e., $r = 1$ , indicates that for $\mathrm { P r } ( \mathbf { S } | \mathbf { R } ) < 0 . 5$ the recall and, thus, the quality of the system on this dimension is understated. Alternatively, assuming that the reliability was not accounted for, indicates that for $\mathrm { P r } ( \mathbf { S } | \mathbf { R } ) < 0 . 5$ the fallout rate is understated.

## 4.3. Impact of reliability on precision

Assuming a symmetric reliability model, the relationship between recall and fallout establishes the impact of reliability changes on precision. The results of this section indicate that in some cases, precision generally, Pr R xŽ Ž <sup><</sup> a.. increases as reliability decreases and in other cases decreases as reliability decreases. In particular, if the probability of the fallout is less than or equal to the recall and more generally, $\mathrm { P r } \mathrm { ( x | N R ) } \le \mathrm { P r } \mathrm { ( x | R ) }$ then under symmetric reliability, as r increases that means that there is Ž <sup><</sup> .decreasing reliability on Pr x NR and $\operatorname* { P r } ( \mathbf { x } ^ { \prime } | \mathbf { R } )$ based on Theorem 1. Since $\mathrm { P r } ( \mathbf { \boldsymbol { x } } | \mathbf { \mathrm { N R } } ) < \mathrm { P r } ( \mathbf { \boldsymbol { x } } | \mathbf { \mathrm { R } } )$ that means that $L ( \mathbf { x } \# )$ will decrease. Since $L ( \mathbf { x } \# )$ is in the denominator of Pr R xŽ <sup><</sup> a. Ž that means that P R x<sup><</sup> a. will increase. Further, P R xŽ <sup><</sup> a. as a function of the reliability, is found to be monotonically increasing or decreasing. These results are summarized in Lemma 2 and Theorem 4.

Lemma 2 — recall greater than or equal to fallout Let $r ^ { \prime \prime }$ and r be two different reliability. If $P r ( x | N R ) \leq P r ( x | R )$ and $r ^ { \prime \prime } \geq r ^ { \prime }$ then $L ( r ^ { \prime \prime } , x ) \leq$ $L ( r ^ { \prime } , x ) ,$ , that is $L ( r , x )$ is monotone decreasing in r.

ProofProof by contradiction. Assume that $r ^ { \prime \prime } > r ^ { \prime }$ and $L ( r ^ { \prime \prime } , x ) \ge L ( r ^ { \prime } , x )$ . Let $p _ { 1 } = \mathrm { P r } ( \mathbf { x } | \mathbf { N R } )$ and $p _ { 2 } =$ Pr x R .Ž <sup><</sup> .

$$
[ r ^ {\prime \prime} p _ {1} + (1 - r ^ {\prime \prime}) (1 - p _ {1}) ] / [ r ^ {\prime \prime} p _ {2} + (1 - r ^ {\prime \prime}) (1 - p _ {2}) ]
$$

$$
\left. p _ {2}) \right] \geq \left[ r ^ {\prime} p _ {1} + \left(1 - r ^ {\prime}\right) \left(1 - p _ {1}\right) \right] / \left[ r ^ {\prime} p _ {2} + \left(1 - r ^ {\prime}\right) \right.
$$

$$
(1 - p _ {2}) ]
$$

$$
[ r ^ {\prime \prime} p _ {1} + (1 - r ^ {\prime \prime}) (1 - p _ {1}) ] [ r ^ {\prime} p _ {2} + (1 - r ^ {\prime}) (1 - p _ {2}) ]
$$

$$
\geq [ r ^ {\prime} p _ {1} + (1 - r ^ {\prime}) (1 - p _ {1}) ] [ r ^ {\prime \prime} p _ {2} + (1 - r ^ {\prime \prime})
$$

$$
(1 - p _ {2}) ]
$$

$$
r ^ {\prime} p _ {2} \left(1 - p _ {1}\right) \left(1 - r ^ {\prime \prime}\right) + r ^ {\prime \prime} p _ {1} \left(1 - p _ {2}\right) \left(1 - r ^ {\prime}\right) \geq
$$

$$
r ^ {\prime} p _ {1} (1 - p _ {2}) (1 - r ^ {\prime \prime}) + r ^ {\prime \prime} p _ {2} (1 - p _ {1}) (1 - r ^ {\prime})
$$

$$
r ^ {\prime} p _ {2} + r ^ {\prime \prime} p _ {1} \geq r ^ {\prime} p _ {1} + r ^ {\prime \prime} p _ {2}
$$

$$
r ^ {\prime} (p _ {2} - p _ {1}) \geq r ^ {\prime \prime} (p _ {2} - p _ {1})
$$

But $r ^ { \prime \prime } \geq r ^ { \prime }$ so there is a contradiction and $L ( r ^ { \prime \prime } , \mathbf { x } ) \leq$ $L ( r ^ { \prime } , \mathbf { x } ) / \lambda$

Theorem 4 — recall greater than or equal to fallout If $P r ( x | N R ) \leq P r ( x | R )$ and $r ^ { \prime \prime } \geq r ^ { \prime }$ then $P r ( R | ( r ^ { \prime \prime } , x ) ) \geq P r ( R | ( r ^ { \prime } , x ) )$ $P r ( R | ( r , x ) )$ is monotone increasing in r.

In Theorem 4, if an information retrieval model is used that does not account for reliability, then that assumes $r = 1$ . Thus, when $r < 1$ , Pr R xŽ <sup><</sup> a. is assumed to be higher than it actually is, i.e., the precision is overestimated if reliability is not accounted for. By assuming that $r = 1$ , the user may be retrieving data elements that are not relevant under the model 1 . Thus, it is clear that it is important to Ž . include reliability in information retrieval models, otherwise more data items may be investigated than is warranted statistically. Similar results can be developed when the recall is less than or equal to the fallout, and more generally, $\operatorname* { P r } ( \mathbf { x } | \mathbf { N R } ) \geq \operatorname* { P r } ( \mathbf { x } | \mathbf { R } )$ . The results are summarized in Lemma 3 and Theorem 5. In contrast to Theorem 4, however, $\operatorname* { P r } ( \mathbf { R } | ( r , \mathbf { x } ) )$ is monotonically decreasing in r.

Lemma 3 — recall less than or equal to fallout If $P r ( x | N R ) \geq P r ( x | R )$ and $r ^ { \prime \prime } \geq r ^ { \prime }$ then $L ( r ^ { \prime \prime } , x ) \ge$ $L ( r ^ { \prime } , x ) ,$ , that is $L ( r , x )$ is monotonically increasing in r.

Proof — Similar to Lemma $2 . / \AA$

Theorem 5 — recall less than or equal to fallout If $P r ( x | N R ) \geq P r ( x | R )$ and $r ^ { \prime \prime } \geq r ^ { \prime }$ then $P r ( R | ( r ^ { \prime \prime } , x ) ) \leq$ $P r ( R | ( r ^ { \prime } , x ) )$ , i.e., $P r ( R | ( r , x ) )$ is monotonically de - creasing in r.

Proof — similar to Theorem 4.<sup>rr</sup>

The results in Theorem 5 indicate that $\operatorname* { P r } ( \mathbf { R } | ( r , \mathbf { X } ) )$ is monotonically decreasing in r. If the information retrieval model does not take into account reliability, then this assumes $r = 1$ . Thus, when $r < 1 ,  { \mathrm { P r } } (  { \mathrm { R } } |  { \mathrm { x } } \# )$ is assumed to be lower than it actually is. By assuming that $r = 1$ , the decision-maker may not be retrieving data items that are relevant under the model Ž . 1 .

## 4.4. Example

An example was developed to illustrate the impact of reliability on precision Pr R IS , recall Ž Ž <sup><</sup> . Ž Ž Pr IS R and fallout rate Pr IS NR , as illustrated <sup><</sup> .. Ž Ž <sup><</sup> .. in Table 3. The results indicate that, assuming symmetric reliability, there is a substantial impact on precision due to reliability. Movement of r from 1.00 to 0.99, yielded a change of 26.3% in Pr R IS ,Ž <sup><</sup> . while a drop in r from 1.00 to.90, lead to a change of 73.4%.

Table 3  
Example — symmetric reliability

<table><tr><td>Pr(S|NR)</td><td>Pr(S|R)</td><td>Pr(R)</td><td>r</td><td>Pr(R|IS)</td><td>Pr(IS|R)</td><td>Pr(IS|NR)</td></tr><tr><td>0.005</td><td>0.2</td><td>0.1</td><td>1.00</td><td>0.816</td><td>0.20</td><td>0.0050</td></tr><tr><td>0.005</td><td>0.2</td><td>0.1</td><td>0.99</td><td>0.601</td><td>0.21</td><td>0.0149</td></tr><tr><td>0.005</td><td>0.2</td><td>0.1</td><td>0.95</td><td>0.319</td><td>0.23</td><td>0.0545</td></tr><tr><td>0.005</td><td>0.2</td><td>0.1</td><td>0.90</td><td>0.217</td><td>0.26</td><td>0.1040</td></tr><tr><td>0.005</td><td>0.2</td><td>0.1</td><td>0.50</td><td>0.100</td><td>0.50</td><td>0.5000</td></tr><tr><td>0.005</td><td>0.2</td><td>0.1</td><td>0.25</td><td>0.088</td><td>0.65</td><td>0.7475</td></tr><tr><td>0.005</td><td>0.2</td><td>0.1</td><td>0.00</td><td>0.082</td><td>0.80</td><td>0.9950</td></tr><tr><td>0.02</td><td>0.2</td><td>0.3</td><td>1.00</td><td>0.811</td><td>0.20</td><td>0.0050</td></tr><tr><td>0.02</td><td>0.2</td><td>0.3</td><td>0.99</td><td>0.749</td><td>0.21</td><td>0.0296</td></tr><tr><td>0.02</td><td>0.2</td><td>0.3</td><td>0.95</td><td>0.592</td><td>0.23</td><td>0.0680</td></tr><tr><td>0.02</td><td>0.2</td><td>0.3</td><td>0.90</td><td>0.490</td><td>0.26</td><td>0.1160</td></tr><tr><td>0.02</td><td>0.2</td><td>0.3</td><td>0.50</td><td>0.300</td><td>0.50</td><td>0.5000</td></tr><tr><td>0.02</td><td>0.2</td><td>0.3</td><td>0.25</td><td>0.273</td><td>0.65</td><td>0.7400</td></tr><tr><td>0.02</td><td>0.2</td><td>0.3</td><td>0.00</td><td>0.259</td><td>0.80</td><td>0.9800</td></tr></table>

## 5. Approaches to mitigating reliability issues

Section 4 illustrates the impact of reliability. This section provides an example that illustrates development of probabilities for reliability models. In addition, the development of these probability estimates can give insight into some potential technology-based approaches that can provide a basis for improving that reliability.

There is substantial information available that can facilitate an empirical development of the probabilities for the models developed in this paper. For example, consider the case discussed earlier with the link from ‘‘Electronic Commerce Course Cases Page’’ to http:<sup>rr</sup>www.usc.edu<sup>r</sup>dept<sup>r</sup>sba<sup>r</sup>atisp<sup>r</sup> AI<sup>r</sup>IJISAFM<sup>r</sup>call-for.htm. An empirical analysis of an ‘‘Excite’’ search found that of the first 50 entries for the request ‘‘electronic commerce’’ 19 out of 50 had ‘‘e’’ and ‘‘c’’ as adjacent letters in the URLs and 40 out of 50 had either the adjacent letters ‘‘e’’ and ‘‘c’’ or ‘‘electronic commerce’’ in the short description. Similarly, an ‘‘Excite’’ search on ‘‘artificial intelligence’’ found the adjacent letters ‘‘a’’ and ‘‘i’’ or ‘‘artificial intelligence’’ in 35 out of 50 directories and descriptors. Using information of this type we can begin to generate estimates of some of the probabilities in the above model that the above URL is a pointer to an ‘‘Electronic Commerce Course Cases Page.’’

However, this information is not just useful to generate probabilities. In addition, this same information can be used to generate tools to further mitigate reliability problems, e.g., such as provide the necessary domain intelligence for an intelligent agent who could review URLs to hypothesize whether or not they met retrieval criteria. Those same descriptive terms provide insight into whether or not the label ‘‘electronic commerce’’ corresponds to the description and URL. In particular, a knowledgeable assistant or intelligent agent would look at the directory and the URL address and draw at least two conclusions. First, the address probably relates to ‘‘AI,’’ an abbreviation for artificial intelligence. In any case, it does not seem to relate to electronic commerce. Second, the file name is an apparent abbreviation of a call for papers. As a result, rather than ‘‘cases’’ it seems to be a ‘‘request for papers’’. Further, an agent could examine the description to determine that it apparently does not relate to electronic commerce, but instead does relate to artificial intelligence, substantiating the hypothesis created by the term ‘‘AI’’ in the directory structure. Technology has rapidly progressed so that now there are many intelligent agent shells available that could be used to exploit and narrow the search through this kind of information Žhttp:<sup>rr</sup> www.primenet.com <sup>r</sup> terry <sup>r</sup> New\_Home\_Page <sup>r</sup> ai\_info <sup>r</sup> intelligent\_agents.html and http:<sup>rr</sup>www.botspot.com<sup>r</sup>site\_map<sup>r</sup>..

Finally, as noted earlier in the paper, some of the reliability problems are a function of the lack of existence of an ontology that clearly defines its terms or interlinking ontologies that accommodate multiple ontologies. As a result, additional research in ontologies can provide an important capability to increase Pr xŽ a<sup><</sup>x by mitigating ontology ambiguity. As with . the use of intelligent agents, the topics being searched and the directory structures of the references being given, can guide the choice of the ontologies. In the ‘‘electronic commerce’’ example, ontologies for ‘‘electronic commerce,’’ ‘‘AI’’ and ‘‘artificial intelligence’’ provide a starting point of analysis.

## 6. Summary, contributions and extensions

This paper has argued that reliability is a critical aspect of Internet-based information systems. A number of sources of problems with reliability were elicited and reviewed. Internet information systems were modeled as intermediary report between the actual data and the system’s representation of that data, in order to capture the ‘‘reporting’’ nature of information retrieval. Since reports cannot always be perfectly accurate, there is a reliability issue. Reliability was characterized as a probability relationship between the actual data items and the report of the data items by the system, Pr xŽ a<sup><</sup>x . Reliability char-. acterizes information search relationships between ‘‘reports’’ e.g., searches and the actual informa-Ž . tion, or between ‘‘reported’’ hyperlink information and actual hyperlinks.

This paper has a number of contributions. First, the paper elicits reliability issues with Internet information systems. Second, the model integrates reliability into the classic information retrieval model of relevance, precision, recall and fallout. Third, it is found that even small changes in reliability can have a material effect on those information retrieval measures. Fourth, since classic models of information retrieval characterize relevance as a critical point decision, and since reliability influences the value that is compared to the critical point, then by not including reliability into the decision making process, it is found that non-optimal decisions will be made. Monotonicity results are used to study the behavior around the critical point due to reliability. Fifth, accounting for reliability has a relatively small cost: in the simplest case only one additional parameter beyond the classic model needs to be estimated. Sixth, reliability on the Internet is characterized so that we can study its impact on internet-based information systems. Finally, the paper finds that reliability is an important component in the design and development of internet-based information systems and provides some other approaches that can mitigate reliability problems.

This paper can be extended in a number of directions. First, the set of categories that are at the root of reliability issues in Internet systems could be further analyzed. For example, a sample of pages could be assessed for reliability problems and the relative frequency of problems from different categories, e.g., ‘‘Errors on Web Pages.’’ Such a study would give insight into the source of reliability problems in Internet information systems. Second, some of the sources of errors, e.g., ‘‘changes in referenced pages’’, suggest organizational relationships that could improve reliability. For example, since changes that others make can influence the reliability, that suggests that reliability can be improved by facilitating communication between those that reference each others pages. Given a list of developers that have referenced a page, when that page was changed its developers could contact those that reference it indicating the nature of the change. In so doing, ‘‘reliability relationships’’ could be established. Third, the mathematical model could be extended based on alternative assumptions, e.g., asymmetric probabilities. This would lead to additional results relating reliability and traditional information retrieval measures. Fourth, approaches to mitigating reliability could be extended and implemented. For example, an intelligent agent could be implemented using some of the specific knowledge discussed here.

## Acknowledgements

An earlier version of this paper was presented at WITS 97. The author wishes to acknowledge the comments of the anonymous referees and the participants at the presentation. In addition, the author would like to thank the anonymous referees for their comments on a revised version of this paper. The author would like to thank an anonymous WITS referee for suggesting a section on how some of the problems discussed in Section 2 could be addressed. The author would like to thank an anonymous referee for the suggestion of discussing the extensions in greater detail.

## References

<sup>w</sup> <sup>x</sup> 1 C. Brown, L. Gasser, D. O’Leary, A. Sangster, AI on WWW: supply and demand agents, IEEE Expert 10 4 1995 50–55.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 M. Kochen, Principles of Information Retrieval, Melville Publishing, Los Angeles, CA, 1974.

<sup>w</sup> <sup>x</sup> 3 G. Salton, Another look at automatic text-retrieval systems, Communications of the ACM 29 7 1986 648–656.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 D. Schum, W. Du Charme, Comments on the relationship between the impact and the reliability of evidence, Organizational Behavior and Human Performance 6 1971 111–131.Ž .

<sup>w</sup> <sup>x</sup> 5 J. Swets, Information-retrieval systems, Science 141 1963Ž . 245–250.

<sup>w</sup> <sup>x</sup> 6 J. Verhoeff, W. Goffman, J. Belzer, Inefficiency of the use of Boolean functions for information retrieval, Communications of the ACM, Vol. 4, 1961, pp. 557–558 and p. 594.

<sup>w</sup> <sup>x</sup> 7 P. Zunde, M. Dexter, Indexing consistency and quality, American Documentation 20 3 1969 259–264.Ž . Ž .

Daniel E. O’Leary is a Professor in the Marshall School of Business at the University of Southern California. Dan received his PhD from Case Western Reserve University, his MBA from the University of Michigan and his BS from Bowling Green State University. Professor O’Leary has published papers in a wide range of journals including Communications of the ACM, IEEE Intelligent Systems, IEEE Computer and Management Science.
