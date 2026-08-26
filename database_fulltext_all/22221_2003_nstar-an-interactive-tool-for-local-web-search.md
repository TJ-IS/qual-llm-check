---
otero_id: 22221
otero_key: "NSZBCAJN"
title: "Nstar: an interactive tool for local web search"
authors: "Tao Guan; Kam Fai Wong"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(03)00049-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Nstar: an interactive tool for local web search

Tao Guan<sup>a</sup>, Kam Fai Wong

<sup>a</sup>StorageNetworks, Inc., 225 Wyman Street, Waltham, MA 02451, USA <sup>b</sup>Department of System Engineering & Engineering Management, The Chinese University of Hong Kong, Shatin, NT, Hong Kong Accepted 7 February 2003

## Abstract

Defining Web query languages has received much attention in the last few years. A typical system consists of a wrapper which maps a data source to a common data model and on which semantic integration is provided. However, constructing wrappers is time-consuming and can cater for tens, but not thousands of data sources. New methods should thus be investigated and then developed. In this paper, we present a novel model to retrieve information from the WWW. It is designed for ad hoc users and employs sample-based mining to extract the desirable data. Our method is more flexible than the wrapper approach. <sup>#</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Web mining; Search engine; Web query; Wrapper; Internet searching

## 1. Introduction

The amount of information available over the Internet has grown considerably over the past decade. This causes difficulties for users because much material is not relevant. Search engines (e.g. AltaVista and Infoseek) and Web query languages, e.g. W3QS, WebOQL, WebLog, StruQL, are two popular technologies developed to address this problem. Although both are effective, they suffer from the following problems:

 Web query languages (see survey in [7]), are mainly applied to well-structured sites (e.g. [19]) or require specially coded wrappers or filters to provide structured (or semistructured) information. They are timeconsuming to use and are only applicable to a few information sources [4]. The availability of data in XML format can simplify this, but information sources may contain relevant data that is not tagged with specific items. Sometimes data is simply not tagged and at other times, the tags used for similar items are different. In addition, different users may look for different information from the same page and it is hard to identify all by specific XML tags in advance. We thus need methods to support ad hoc information extraction (or mining) from Web pages, especially when they are represented in unstructured texts (e.g. online news).

 Conventional search engines are designed for global search (i.e. over the entire World Wide Web). They are ineffective for users who seek exact information from a specific Web site. This is analogous to searching in structured databases, e.g.:

List the name and e-mail address of all professors at the University of Regina.

In practice, only a few Web sites provide local search functions [16]. Thus, users have to use general search-engines such as Netscape or Information

Explorer (IE) to browse the Web site manually. However, large Web sites may contain thousands of pages, e.g. the Web site of the University of Regina has more than 10,000 pages. Although these pages are organized in a hierarchical graph, the information in which one is interested may be distributed in different places. For example, manual searching for the information about professors at a university would be ineffective, as it is often listed in the homepages of different departments. Even if the number of pages visited is small, it is a boring task to check each page. Some local search tools are available at large Web sites, but they only support simple keyword searching and more specific conditions cannot be expressed. Hidden information that exists on a Web page cannot necessarily be accessed from outside the site, e.g. information on names and e-mails abound but they often appear in random places and in different formats.

In this paper, we propose a tool, Nstar, designed for information retrieval from one known Web site. Our goal is to retrieve relevant information with minimal human intervention. The major difference between Nstar and similar approaches [3,10,21] is that Nstar does not require site-specific knowledge or a wrapper. Searching in Nstar involves two operational steps:

 Probing, which is initiated using one or more keywords provided by the users. The result is a set of potential Web pages.

 Extraction, which is a means of mining the desirable information from the potential result list based on samples provided by the users.

The first step is similar to searching using a conventional search engine, e.g. Alta Vista. The users need to inform Nstar which Web pages they expect by providing one or more keywords. Next the scope of the search is determined. If the search focuses on a remote Web site, a starting point should be given; otherwise, the default case is the local server, i.e. where Nstar is installed. It next searches objects automatically starting from that point until restricted conditions are satisfied or the site is exhausted. The output of this step is a potential result set which contains URLs pointing to pages potentially relevant to the query. Finally, a sample is specified by the users to indicate what information is further required. Nstar applies a set of heuristic rules to extract information based on the sample. The final output is a list of relevant pages ranked according to their significant scores.

The key technical issues behind the Nstar approach are: (1) how to mine the desirable information from semistructured Web pages; (2) how to control the complexity of query processing over the original data. Since the second issue has been addressed in [11], we only focus on the first issue.

## 2. Related work

Sample-based (sometimes referred to as casebased) mining has been shown to be effective over unstructured textual data [15]. The Lore system [9,20] is a database management system for semistructured data. This was applied to XML data management [8]. The interactive query interface of Lore is based on DataGuide, which is structural information automatically extracted from the original data graph. Data-Guide is effective for query formulation. But it is difficult to transform original textual Web information into a data graph.

A number of Web query languages have been developed. They aimed to combine the content-based queries in information retrieval with structure-based queries in DBMS. These languages have evolved from the first generation Web query languages, e.g. W3QS, WebSQL and WebLog, to the second generation Web data manipulation languages, e.g. WebOQL and StruQL. These approaches are different from ours as they require site-specific wrappers.

Structural information extraction from textual Web pages has recently been studied. Ashish and Knoblock [2] worked on syntax analysis and applies font size and indentation to structure a page. This method, however, is rather hard to use. Hammer et al. [13] and Smith and Lopez [22] helped users to define a pattern or declarative language to aid systems in extracting structures. Although these methods give high precision, much user intervention must be involved. In contrast, other approaches (such as [1,5,6,17]) attempted to apply AI techniques (KDD and machine learning) to mine structured information (or knowledge) from semistructured Web pages. Also, Wang et al. applied clustering techniques to extract structured information from semi-structured data. Most of these works require domain-specific semantic knowledge and/or learning on corpus, which are dif ferent from our method.

## 3. Search model

The Nstar search model comprises of the following two steps:

 Probing: In this, users first specify one or more keywords to define the scope of the search, i.e. a local or remote site, and then trigger the search. If this is Local, searching will be initiated on the homepage in which Nstar is installed, and then along the links embedded in the Web pages. The result is a set of URLs that point to the page containing the keywords. Alternatively, the search can be applied to a remote URL site explicitly specified by the user.

Since the search is performed on original data and the communication costs for accessing the Web pages via the Internet is large, the response time for local or remote searches can be very long. To overcome this, two approaches are adopted in Nstar. Firstly, users can explicitly control the run-time. For example, they can limit the search by specifying a maximum waiting time, a number of expected results or depth. Secondly, an effective optimizing technique based on semantics similarity between words, is used to guide the search in the most promising direction.

 Extraction: We apply a sample-based mining algorithm to extract the required information. Here, a sample (an excerpt from a Web page) is specified by the users to indicate what information is expected. The system then looks for similar parts from other pages automatically based on the pattern and style of the sample. The method is based on the observation that many Web sites are organized by the same institute and thus the pages therein commonly exhibit very similar stylistic properties.

## Consider the following example:

List the name and e-mail address of all professors at the University of Regina.

The initial Nstar interface is shown in Fig. 1.

We first specify the keyword professor to initiate retrieval. We assume Nstar is installed at the University of Regina.

Thus, the scope of searching is skipped (i.e. the default is Local search). The run time can be controlled by specifying the maximum waiting time or number of desired results. When the start button is clicked, the search is triggered and the result is shown in Fig. 2.

![](/api/attachments/NSZBCAJN/fulltext/images/a071992a8ecfcb7a9e871da795587ca2528999e2607cca3d39c3879d48e9974e.jpg)  
Fig. 1. The Nstar interface.

![](/api/attachments/NSZBCAJN/fulltext/images/c3385d21c13c0a76f3aa915124bce6fdcf88b97d184e74167224c7f2ac0505a6.jpg)  
Fig. 2. The result after probing.

Next we need to indicate which information is to be mined in the extraction step. This is done by specifying some samples from a potential page. For experienced users, we may browse a part of the result quickly, e.g. the first five pages, and find samples which are best in highlighting characteristics of the desired information. Or we simply choose samples from the first correct page returned by probing. For example, we may use the name and email from Dr. Slaney’s homepage as samples in this case, see Fig. 3.

![](/api/attachments/NSZBCAJN/fulltext/images/f81d30fdb3c1a4608b293496ef0f54e9eb26293cc517858203bff299b3cdc182.jpg)  
Fig. 3. Choosing samples.

![](/api/attachments/NSZBCAJN/fulltext/images/c961e391546683f9b3d1152141612a97285785a84b031f4c2b515a84dd1128f1.jpg)  
Fig. 4. The final results.

When the samples are chosen, a set of heuristic rules is applied to extract other names and e-mails from all potential pages. The results are ranked and hits with highest values are returned to the users (see Fig. 4).

Note: Some unexpected pages may be returned in probing, e.g. the first page introduction. The information from these pages is not necessarily of interest. These pages, however, could easily be filtered by ranking as their scores are relatively low (the pattern and style similarities are worse than others).

Of course, the result does not cover all the desirable information and errors may occur (e.g. the name for Dr. Bryan Hillis was not expected to be followed by Ph.D.). Nevertheless, it provides a practical approach to extracting more precise information from the Web pages. In particular, it can be used as a complementary tool for conventional search engines to obtain a list of potential URLs.

## 4. Sample-based mining

The sample-based mining method extracts information based on a sample specified by the users. It is based on the assumption that a small group of Web pages is probably written in similar structure and styles. This is typically the case for the Intranet of an institute in which all Web pages are designed by a webmaster. Therefore, when a user is looking for something (e.g. email address), he/she may first locate one (e.g. the sample in this paper) from a page manually and then informs the system that is an example of what he/she would like to obtain. The system will then search other pages automatically.

## 4.1. Formal model

Let $w = ( w _ { 1 } , w _ { 2 } , \ldots , w _ { n } )$ be a group of Web pages which have similar style. Considering the source code, each HTML page w<sub>i</sub>, can be broken down into a list of fields: $w _ { i } = ( f _ { i _ { 1 } } , f _ { i _ { 2 } } , \ldots , f _ { i _ { k } } )$ ; where each field may be:

 a word, e.g. Good, Kelly, CL506;

 a number, e.g. 189.23, 67, 0.67;

 a date, e.g. Jun 30, 2002, 30/06/02, 30-06-2002;

 a time, e.g. 12:00, l:00 p.m., 15:45:56;

 a price, e.g. US\$ 26.99, CND\$ 78, HK\$ 56.89;

 a specific ASCII character except ‘0’–‘9’, ‘a’–‘z’, ‘A’–‘Z’ and, e.g. þ, , :;

 a HTML tag, e.g. <B>, </B>, or <P>.

Note that these definitions of a field are not exhaustive.

Definition 1. An object o is a list of continuous fields appearing in the body of a Web page and the first and last elements cannot be HTML tags. For example, consider the first HTML example in Appendix A. The professor’s name Bill Brown may be represented as an object $o = ( { \mathrm { \bf B i l l } } , { \mathrm { \bf B r o w n } } ) . ^ { \mathrm { \scriptsize ~ \mathrm { 1 } } }$ 1

Furthermore, a sample is a specific object indicated by the users. Usually, they choose the sample by a browser interface and thus they do not know the HTML tags hidden in it.

We consider two types of similarities between the sample and potential objects: pattern similarity and style similarity.

## 4.2. Pattern similarity

Pattern similarity measures how much two objects match with one another. We first define the concept of matched fields.

Definition 2. A field $f _ { i }$ matches with another field $f _ { j } ,$ denoted by $f _ { i } \approx f _ { j } ,$ , if

 both $f _ { i }$ and $f _ { j }$ are words and their values are equal;

 both $f _ { i }$ and $f _ { j }$ are HTML tags and they are the same;

 both $f _ { i }$ and $f _ { j }$ are special ASCII characters and their values are equal;

 both $f _ { i }$ and $f _ { j }$ are numbers;

 both $f _ { i }$ and $f _ { j }$ are dates;

 both $f _ { i }$ and $f _ { j }$ are times;

 both $f _ { i }$ and $f _ { j }$ are prices.

For example,

<table><tr><td>&lt;B&gt; ≈ &lt;B&gt;</td><td>‘good’ ≈ ‘good’</td><td>123 ≈ 17.86</td></tr><tr><td>‘10 Jun 1988’</td><td>HK$ 100</td><td>“≈”</td></tr><tr><td>≈ ‘01/06/67’</td><td>≈ US$ 20</td><td></td></tr></table>

However, <B> does not match with ${ \tt < } / \mathrm { B } >$ and nor does ‘good’ with ‘hot’. The intuition behind this is that words are general elements in the Web pages so that they cannot be used to identify an object (only the same words may suggest the similarity to some extents). In contrast, HTML tags, numbers, dates, times, prices and symbols are special data and thus characterize an object. However, we find that HTML tags and symbols are usually fixed among a set of similar objects, but number, dates, times and prices are variable. Therefore, we require that the former have the same values, but not the latter.

Definition 3. An object $p = ( p _ { 1 } , p _ { 2 } , \ldots , p _ { m } )$ is a subobject of $q = ( q _ { 1 } , q _ { 2 } , \ldots , q _ { n } )$ if there is a sublist of $q ( q _ { i _ { 1 } } , q _ { i _ { 2 } } , \ldots , q _ { i _ { m } } )$ such that for each $k , 1 \le k \le m -$ $1 \Rightarrow i _ { k } < i _ { k + 1 }$ and $1 \leq k \leq m \Rightarrow p _ { k } = q _ { i _ { k } }$

Definition 4. An object $p = ( p _ { 1 } , p _ { 2 } , \ldots , p _ { m } )$ matches with the object $q = ( q _ { 1 } , q _ { 2 } , \ldots , q _ { n } )$ , denoted by $p \approx q ,$ if $m = n$ and for each $k , 1 \le k \le m \Rightarrow p _ { k } \approx q _ { k }$

Now we can define the pattern similarity measure between two objects.

Definition 5. For objects $p$ and $q ,$ the pattern similarity measure, denoted by PSM, is the maximum size of the sub-objects $p _ { i }$ and $q _ { j }$ such that $p _ { i } \approx q _ { j }$

For example, for objects $p = ( P h o n e , : , ~ ( , ~ 3 0 6 , )$ $7 8 1 , \mathrm { ~ - , ~ } 7 4 8 8 )$ and $q = ( T e l , : , 1 , - , 3 0 6 , - , 7 8 1 , - ,$ 7453), the maximum matched sub-objects are: (:, 306, $7 8 1 , - , 7 4 8 8 ) \approx ( : , 1 , 3 0 6 , - , 7 8 1 )$ . Thus, PSM(p, $q ) = 5 .$

In order to reduce the effect of false matches between large objects, we first consider the ratio of PSM to the average size of the objects to reflect the real pattern similarity. For two objects whose average size is 10 and PSM is 5, the ratio is 50% and this is the same as the ratio of objects whose average size is 2 and PSM is 1. In practice, the former should have a higher similarity since the one matched field in the latter may be a false match. Therefore, we multiply the ratio by the PSM to reflect it. The final result is called pattern similarity score (denoted by PSS).

$$
\begin{array}{c} \operatorname{PSS} (p, q) = \left(\frac {\operatorname{PSM} (p , q)}{(\operatorname{size} (p) + \operatorname{size} (q)) / 2}\right) \\ \times \operatorname{PSM} (p, q) \times 1 0 0 \end{array}
$$

In the above example, $\mathrm { P S S } ( p , q ) = ( 5 / ( ( 8 + 9 ) / 2 ) ) \times$ $5 \times 1 0 0 = 2 9 0$

If we assume the object p is the sample, then the PSS is enough to distinguish the object q from other parts. However, if there is another object l ¼ (Fax, :, 1, –, 306, –, 781, –, 7453) (e.g. in the second example in Appendix A), then it is hard to determine which (q or l) should match with p since PSS(p, q) ¼ PSS(p, l). In this case, context should be taken into consideration.

Definition 6. A segment is a list of continuous fields in a Web page. If we consider all HTML tags as segment delimiters in Web pages, then the body (between <body> and </body>) can be viewed as a list of segments. For instance, Example 1 in Appendix A can be represented as

Segment1 ¼ (Faculty, Profile);

Segment2 ¼ (Bill, Brown, –, Associate, Professor);

Segment3 ¼ (brown, @, cs, . , usask, ., ca);

Now we define Pre-marker which is used to iden tify the beginning and end of an object.

Definition 7. For object o, the Pre-marker is defined as follows:

If the first element of o is the first field of a segment

and the segment is the first segment in the page, then

Pre-marker is beg-file>;

else if the first element is the first field of a segment, then

Pre-marker is beg-seg>;

else

Pre-marker is the field immediately before the first element.

Definition 8. For object o, the After-marker is defined as follows:

If the last element of o is the last field of a segment

and the segment is the last segment in the page, then

After-marker is <end-file>;

else if the last element is the last field of a segment, then

After-marker is <end-seg>;

else

After-marker is the field immediately after the last element.

For example, Pre-Marker(o) ¼ <beg-seg> and After-Marker(o) ¼ ‘–’ in Example 1, where o is (Bill, Brown).

Furthermore, Pre-part and After-part are used to identify the context of an object.

Definition 9. The Pre-part of an object o is defined as:

If the first element of o is the first field of a segment

and the segment is the first segment in the page, then

Pre-part is <beg-file>;

else if the first element of o is the first field of a segment, then

Pre-part is the segment immediately before the segment containing the first element of o; else

Pre-part is the list of fields from the beginning of the segment containing the first element of \$o\$ until the pre-marker (including it).

Definition 10. The After-part of an object o is defined as:

If the last element of o is the last field of a segment

and the segment is the last segment in the page, then

After-part is <end-file>;

else if the last element of o is the last field of a segment, then

After-part is the segment immediately after the segment containing the last element of o;

else

After-part is the list of fields from the After-marker until the end of the segment containing it.

For example, for the object o in Example 1, we have,

Pre-part(o)¼<beg-seg> and After-part(o) ¼ (–, Associate, Professor);

Table 1  
PPS for special fields

<table><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>100</td><td>0</td><td>20</td><td>0</td></tr><tr><td></td><td>0</td><td>100</td><td>0</td><td>20</td></tr><tr><td></td><td>20</td><td>0</td><td>50</td><td>0</td></tr><tr><td></td><td>0</td><td>20</td><td>0</td><td>50</td></tr></table>

The Pre-part and After-part can be used to calculate the pattern similarity between the context of the objects. For special fields, e.g. <beg-file> and <endfile>, the PSS is obtained from Table 1. Thus, the total pattern similarity score (TPSS) between two objects is

$$
\begin{array}{l} \text { TPSS } (p, q) = \text { PSS } (p, q) + 0. 5 \\ \quad \times \text { PSS } (\text { Pre - part } (p), \text { Pre - part } (q)) \\ \quad + 0. 5 \times \text { PSS } (\text { After - part } (p), \\ \quad \text { After - part } (q)); \end{array}
$$

Let us look at the above example again, we already have

PSSðp; qÞ ¼ PSSðp; lÞ ¼ 290;

However,

PSS(Pre-part(p), Pre-part(q)) ¼ PSS((Office, :, 145, Engineering, Building), (Office, :, 153, Engineering, Building)) ¼ 500;

PSS(After-part(p), After-part(q)) ¼ PSS-((Fax, :, (, 306, ), 781, –, 6754), (Fax, :, 1, –, 306, 781, –, 6754)) ¼ 290;

```txt
PSS((Fax, :, (, 306, ), 781, -, 6754), (Research, Interests)) = 0;
```

Thus, q should match p rather than l.

## 4.3. Style similarity

Although HTML tags are primarily used for formatting, they also provide important clues for data extraction. Usually, pages in an institute are designed by the same professionals. Thus, it is not uncommon to find Web pages presented in similar styles. This can be used for Web searching. The style of a Web page is determined by the HTML-path of an object. Although HTML tags are used in Web pages for cosmetic reasons, they provide important clues in locating the desired information. Usually, pages from an institute have a similar style since many public pages are designed by the same professionals. Thus, it is not uncommon to find Web pages presented in similar styles. This information can be used for Web searching. Since the style can be determined by the HTML tags in Web pages, we first introduce the concept HTML-path of an object.

Definition 11. For an object o, the HTML-path is a list of HTML tags $( t _ { 1 } , t _ { 2 } , \ldots , t _ { m } )$ , where

$t _ { i }$ is a HTML tag (except <body>) before the first element of o in the page and if it has a corresponding end tag (i.e. </B> for <B> and </H2> for <H2>), the end tag must be after the first element of o in the page;

 there is no other HTML tags after $t _ { m } ,$ which satisfy the above conditions.

Actually, the HTML-path is a maximum length list of HTML tags, which may take effect on the objects. For example, two objects o ¼ (Bill, Brown) in Example 1 and m ¼ (Alan, Bell) in Example 2 (see Appendix A),

HTML-path (o) ¼ (<table>, <tr>, <td>, <p>); HTML-path (m) ¼ (<table>, <tr>, <td>, <p>).

When the HTML-path of an object is determined, we may compare it with the HTML-path of the sample. The more they are matched, the more similar they are in style. Therefore, if we assume the HTMLpath to be a special object (a list of HTML tags), the Style Similarity Score (SSS) can be used to quantify style similarity:

$$
\begin{array}{c} \operatorname{SSS} (p, q) = \left(\frac {\operatorname{PSM} (p , q)}{(\operatorname{size} (p) + \operatorname{size} (q)) / 2}\right) \\ \times \operatorname{PSM} (p, g) \times 1 0 0. \end{array}
$$

For example,

SSSðHTML-pathðoÞ; HTML-pathðmÞÞ

$$
= \left(\frac {4}{(4 + 4) / 2}\right) \times 4 \times 1 0 0 = 4 0 0;
$$

## 4.4. The algorithm

Concepts of pattern similarity and style similarity can be used in extracting desired information based on a sample specified by the users. The following is the algorithm:

 split the body of the page containing the sample into a list of segments;

 locate the Pre-marker, After-marker, Pre-part and After-part of the sample;

 determine the HTML-path of the sample;

 for each potential page,

split the body of the page into a list of segments; search the Pre-marker and After-marker in the page;

the object between the Pre-marker and Aftermarker is marked as a potential object;

mark all segments which do not appear in any potential object as potential objects;

for each potential object:

– locate the Pre-part and After-part;

– determine the HTML-path of the sample;

– calculate the TPSS and SSS between it and the sample;

 rank all potential objects by the sum of TPSS and SSS;

 choose the object with the highest value as the output.

Note that the Pre-marker and After-marker does not account for every situation. Consider the object o ¼ (Bill, Brown), the Pre-marker is <beg-seg> and After-marker is ‘–’. If we use them to identify names in other pages, e.g. Example 2 in Appendix A, it is correct. However, it is possible for some pages that names were not followed by the character ‘–’ and title, and thus Pre-marker and After-marker could not reflect the real situation. To overcome this, all segments that are not between Premarker and After-marker are marked as potential values.

## 5. Experimental results

Although our approach cannot guarantee 100% success in mining the desired information from a specific Web site, initial experience shows that it is practical. The following describes our experiment for evaluating the practicality of the approach.

We tried to extract the names and email addresses of all professors in an academic institute, i.e. a university or a department. In the experiment, we considered 10 Web sites selected from the WWW (see Table 2). Different characteristics were observed from these Web sites. For example, the site at the University of Regina (site 1) contained more than 300 faculties whose homepages were written in various styles. In contrast, the site (site 4) of the faculty of engineering at the University of Alberta was much smaller and had 95 professors coming from four departments. Other sites were departmental sites. Some of them (e.g. site 3) were developed by the same webmaster and others were written by the professors themselves (e.g. site 2).

Table 2  
The experimental results

<table><tr><td rowspan="2">http address</td><td colspan="2">Name</td><td colspan="2">e-mail</td></tr><tr><td>Recall (%)</td><td>Precision (%)</td><td>Recall (%)</td><td>Precision (%)</td></tr><tr><td>1. http://www.uregina.ca/facdepts.html</td><td>36.4</td><td>12.8</td><td>45.5</td><td>16.1</td></tr><tr><td>2. http://www.cs.uregina.ca/directory/faculty-page.shtrnl</td><td>46.7</td><td>70</td><td>53.3</td><td>80</td></tr><tr><td>3. http://www.cs.usask.ca/people/faculty-profiles</td><td>100</td><td>100</td><td>100</td><td>95.2</td></tr><tr><td>4. http://www.engineering.ualberta.ca/facultymembers.htm</td><td>47.4</td><td>56.2</td><td>81</td><td>91.6</td></tr><tr><td>5. http://www.usc.edu/dept/chemistry/faculty/idx-alpha.html</td><td>62</td><td>60</td><td>62</td><td>94.7</td></tr><tr><td>6. http://www.uri.edu/pharm/facframe.htm</td><td>62</td><td>72.2</td><td>62</td><td>76.5</td></tr><tr><td>7. http://www.med.unc.edu/wrkunits/2depts/derm/faculty.html</td><td>83.3</td><td>83.3</td><td>100</td><td>100</td></tr><tr><td>8. http://www.me.uic.edu/html/faculty/index.htm</td><td>59.4</td><td>63.3</td><td>84.3</td><td>90</td></tr><tr><td>9. http://www.cse.cuhk.edu.hk:80/people/Index.html</td><td>68</td><td>70.8</td><td>84</td><td>87.5</td></tr><tr><td>10. http://www.cz3.nus.edu.sg/staff-teaching.html</td><td>33.4</td><td>33.4</td><td>77.7</td><td>77.7</td></tr><tr><td>Average</td><td>59.9</td><td>62.2</td><td>75</td><td>80.9</td></tr></table>

![](/api/attachments/NSZBCAJN/fulltext/images/f6e81541e88484377405c8b91f62f8c6f0ceab7c8f2654b3c4aa60fcb6f176b2.jpg)  
Fig. 5. The main page of http://www.cz3.nus.edu.sg/staff-teaching.html.

Of course, the result of sample-based mining usually depends on the sample specified by the users. For simplicity, we assumed that the users always selected the sample from the first page they encountered. For example, Fig. 5 shows the main page of site 10. A user may click the link ‘‘Chen Kan’’ (as pointed to by the arrow) to obtain the sample.

The testing result is shown in Table 2. The recalls for both name and e-mail were reasonable even for large sites (e.g. site 1) or sites in which homepages were written by different people, e.g. site 2 and site 4. Since large sites have a higher chance of involving multiple authors, the chance of deviation from the sample is also higher. By the same token, precision for such Web sites tended to be low; but they were still acceptable, e.g. 70% for the name and 80% for the e-mail of site 2. In contrast, recall and precision for small sites or sites involving few people in the designing process were relatively higher. For example, the computer science department of the University of Saskatchewan (site 3), gave 100% recall for both name and e-mail; and 100% precision for name and 95.2% for e-mail. Overall, the average recall for name and e-mail were 59.9 and 75%, respectively, and the average precision were 62.2 and 80.9%, respectively. This showed that sample-based mining was adequate for locating information which did not have typical patterns. Although recall and precision could not favorably compare with those of traditional database systems, incomplete answers were tolerable in Web searching.

Furthermore, we also attempted to compare our algorithm with other proposed algorithms, including also [14,18]. However, the comparisons were difficult since there was no common evaluation platform available for Web information extraction, such as the Message Understanding Conference (MUC) for information extraction on textual documents. Most systems are tested on a number of selected Web sites, but the contents or formats of the Web sites may not be consistent, i.e. they change. For example, we have also applied sample-based mining to the site at The Australian Bureau of Meteorology to extract weather information (i.e. location, day, condition, high, low). Recall and precision were both 80% for location. This, was much better than the result presented by Soderland, where the recall was 23.8% and the precision was 81.4% for the same information. However, Soderland’s test was performed some years ago and the test data may have changed.

In the experiment, we found that much information was actually highlighted by common patterns and similar styles in the Web site. Of course, there were exceptions. The worst cases are Web pages that had multiple designers with different design styles (e.g. the Web site of University of Regina). However, a group of pages sometimes shares common structures. For example, most professors’ homepages have name, title, address, biography, research interests and publication listed in the same order. Some items, such as title, addresses and publications, contain common patterns. Therefore, the extraction is sometimes possible even if they are developed by different persons.

In practice, users may choose different mining algorithms by the characteristics of the site [12]. For example, in a research database, publications or research interests are best mined by keyword-based mining since most of them are highlighted by the same keywords in the ‘paper’ on the Web; on the other hand, mail address would be handled better by pattern-based mining as they almost have the same pattern in a directory. Name, however, is best mined by the sample-based approach.

## 6. Conclusion

In this paper, we present a novel approach to retrieving information from a Web site. We first introduce the Nstar search model and then discuss the key technique: mining information from Web pages by samples. This approach is more flexible than existing Web query languages (e.g. no site-specific wrapper is required) and the result is acceptable.

## Appendix A

Example 1. Excerpt of a Web page

```html
<body bgcolor="#fff8dc">
<div align=center>
    <div align=center><img src="gif/header.gif" alt="Department of Computer Science"><br>
    <br><hr><br></div><h1 align=center> Faculty Profile</h1></div>
    <table border=1 units="en" clear="no" align=center>
    <tr><td rowspan=5><img src="faculty/frank/frank.gif"></td>
    <td align=right><p>Bill Brown—Associate Professor</P></td></tr>
    <tr><td align=right><p><a href="mailto:brown@cs.usask.ca">brown@cs.usask.ca</a></p>
    </td></tr>
    <tr><td align=right><p>Office: 145 Engineering Building</p></td></tr>
    <tr><td align=right><p>Phone: (306) 781-7488</p></td></tr>
    <tr><td align=right><p>Fax: (306) 781-6754</p></td></tr>
    </table>
    <h2> Research Interests:</h2>
    Dr. Brown's primary research interest ...
    <h2> Research Affiliations: </h2>
```

## Appendix A (Continued )

## Example 2. Excerpt of a Web page

<body bgcolor¼‘‘#fff8dc’’>

<div align¼center><img src¼‘‘gif/header.gif’’ alt¼‘‘Department of Computer Science’’><br> <br><hr><br> </div><h1 align¼center> Faculty Profile</h1></div>

<table border¼1 units¼‘‘en’’ clear¼‘‘no’’ align¼center> <tr><td rowspan¼5><img src¼‘‘faculty/bell/bell.gif’’></td> <td align¼right><p>Alan Bell—Professor</P></td></tr>

<tr><td align¼right><p><a href¼‘‘mailto:bell@cs.usask.ca’’>bell@cs.usask.ca</a></p> </td></tr>

<tr><td align¼right><p>Office: 153 Engineering Building</p></td></tr>

<tr><td align¼right><p>Fax: 1-306-781-6754</p></td></tr>

</table>

<h2> Research Interests:</h2>

<ui><li>Databases . . .

<h2> Research Affiliations: </h2>

</body>

## References

[1] B. Adeberg, NoDOSE—A tool for semi-automatically extracting structured and semistructured data from text documents, in: Proceedings of SIGMOD’98, Washington, USA, 1998, pp. 283–294.

[2] N. Ashish, C. Knoblock, Wrapper generation for semistructured Internet sources, in: Proceedings of the 1st Workshop on Management of Semistructured Data, Arizona, 1997.

[3] C. Beeri, et al., WebSuite—a tool suite for harnessing Web data, in: Proceedings of the 1st International Workshop on the Web and Databases, Valencia, Spain, 1998, pp. 152–171.

[4] S. Brin, Extracting patterns and relations from the World Wide Web, in: Proceedings of the 1st Workshop on Management of Semistructured Data, Arizona, 1998.

[5] W. Cohen, Y. Singer, Learning to query the Web, in: Proceedings of AAAI Workshop on Internet-Based Information Systems, 1996.

[6] M. Craven, et al., Learning to extract symbolic knowledge from the World Wide Web, in: Proceedings of AAAI-98, Wisconsin, USA, 1998, pp. 509–516.

[7] D. Florescu, A. Levy, A. Mendelzon, Database techniques for the World Wide Web: a survey, SIGMOD Record 27 (3), 1998, pp. 59–74.

[8] R. Goldman, J. McHugh, J. Widom, From semistructured data to XML: migrating the Lore data model and query language, in: Proceedings of WebDB99, Pennsylvania, USA, 1999, pp. 25–30.

[9] R. Goldman, J. Widom, Interactive query and search in semistructured databases, in: Proceedings of the 1st Workshop on Management of Semistructured Data, Arizona, 1998.

[10] P.B. Golpher, A.H.F. Laender, A.S. da Silva, B. Ribeiro-Neto, An example-based environment for wrapper generation, in: Proceedings of the 2nd International Workshop on the World Wide Web and Conceptual Modeling, 2000.

[11] T. Guan, M. Liu, L.V. Saxton, Structure-based queries over the World Wide Web, in: Proceedings of the 17th International Conference on Conceptual Modeling, Singapore, 1998, pp. 107–120.

[12] T. Guan, K.F. Wong, KPS: a Web information mining algorithm, Computer Networks 31, 1999, pp. 1495–1507.

[13] J. Hammer, H.G. Molina, J. Cho, R. Aranha A. Crespo, Extracting semistructured information from the Web, in: Proceedings of the 1st Workshop on Management of Semistructured Data, Arizona, 1997.

[14] C. Hsu, Generating finite-state transducers for semi-structured data extraction from the Web, Information Systems 23 (8), 1998, pp. 521–538.

[15] S.C. Hui, G. Jha, Data mining for customer service support, Journal of Information & Management 38, 2000, pp. 1–13.

[16] E.K.R.E. Huizingh, The content design of Web sites: an empirical study, Journal of Information & Management 37, 2000, pp. 123–134.

[17] T.I. Jefferson, T.J. Nagy, A domain-driven approach to improving search effectiveness in traditional online catalogs, Journal of Information & Management 39, 2002, pp. 559–570.

[18] N. Kushmerick, D.S. Weld, R. Doorenbos, Wrapper induction for information extraction, in: Proceedings of the 15th International Joint Conference on Artificial Intelligence, Nagoya, Japan, 1997, pp. 729–737.

[19] A.H.F. Laender, B. Ribeiro-Neto, A.S. da Silva, E.S. Silva, Representing Web Data as Complex Objects, in: Proceedings of the First International Conference on Electronic Commerce and Web Technologies EC-Web, 2000.

[20] J. McHugh, S. Abiteboul, R. Goldman, D. Quass, J. Widom, Lore: a database management system for semi-structured data, SIGMOD Record 26 (3), 1997, pp. 540–566.

[21] A. Mendelzon, G. Mihaila, T. Milo, Querying the World Wide Web, in: Proceedings of First International Conference on Parallel and Distributed Information System, FL, USA, 1996, pp. 80–91.

[22] D. Smith, M. Lopez, Information extraction for semistructured documents, in: Proceedings of the 1st Workshop on Management of Semistructured Data, Arizona, 1997.

![](/api/attachments/NSZBCAJN/fulltext/images/10d2f78b566f9daa26e85218d4dedd2c76df8850f31bbc3eee372316ac61d492.jpg)  
Tao Guan received his PhD degree in computer science from the University of Regina, Canada in 1999; and MSc and BSc from Peking University, China, in 1992 and 1989, respectively. He is currently a senior software engineer at StorageNetworks, USA. His research interests include Webbased information retrieval, knowledge discovery over the web and web database.

![](/api/attachments/NSZBCAJN/fulltext/images/92ba77c53ef0be4830f882435edc2360b962601ca4d22b76239b0c480c375977.jpg)

K.F. Wong obtained his PhD from Edinburgh University, Scotland, in 1987. After his PhD, he has performed research in Heriot–Watt University (Scotland), UniSys (Scotland) and ECRC (Germany). At present he is an associate professor in the Department of Systems Engineering and Engineering Management, the Chinese University of Hong Kong (CUHK) and in parallel serves as the director of the Center for Innovation and Technology

(CINTEC), CUHK. His research interest centers on Chinese computing and parallel database and information retrieval. He has published over 100 technical papers in these areas in various international journals and conferences and books. He is a member of the ACM, CLCS, IEEE-CS AND IEE (UK). He is the founding Editor-in-Chief of ACM Transactions on Asian Language Processing (TALIP) and a member of the editorial board of the Journal on Distributed and Parallel Databases, International Journal on Computer Processing of Oriental Languages and International Journal on Computational Linguistics and Chinese Language Processing. He is the panel chair of VLDB2002, PC co-chair of ICCPOL01 and ICCPOL99 and General Chair of IRAL00 and also PC members of many international conferences, e.g. some recent ones are: WISE02, ICWL02, COLING02, DASFAA03, IRAL03 and ICCPOL03.
