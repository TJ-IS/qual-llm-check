---
otero_id: 12168
otero_key: "J8PWSV3A"
title: "An information delivery system with automatic summarization for mobile commerce"
authors: "Christopher C. Yang; Fu Lee Wang"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 43 (2007) 46 – 61

www.elsevier.com/locate/dss

# An information delivery system with automatic summarization for mobile commerce

Christopher C. Yang <sup>a,\*</sup>, Fu Lee Wang b

<sup>a</sup>Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Shatin, Hong Kong, China <sup>b</sup>Department of Computer Science, City University of Hong Kong, Kowloon Tong, Hong Kong, China

Available online 14 July 2005

## Abstract

Wireless access with handheld devices is a promising addition to the WWW and traditional electronic business. Handheld devices provide convenience and portable access to the huge information space on the Internet without requiring users to be stationary with network connection. Many customer-centered m-services applications have been developed. The mobile computing, however, should be extended to decision support in an organization. There is a desire of accessing most update and accurate information on handheld devices for fast decision making in an organization. Unfortunately, loading and visualizing large documents on handheld devices are impossible due to their shortcomings. In this paper, we introduce the fractal summarization model for document summarization on handheld devices. Fractal summarization is developed based on the fractal theory. It generates a brief skeleton of summary at the first stage, and the details of the summary on different levels of the document are generated on demands of users. Such interactive summarization reduces the computation load in comparing with the generation of the entire summary in one batch by the traditional automatic summarization, which is ideal for wireless access. The three-tier architecture with the middle-tier conducting the major computation is also discussed. Visualization of summary on handheld devices is also investigated. The automatic summarization, the three-tier architecture, and the information visualization are potential solutions to the existing problems in information delivery to handheld devices for mobile commerce <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Document summarization; Mobile commerce; Fractal summarization; Handheld devices; Financial news delivery

## 1. Introduction

The advance of mobile network creates business opportunities and provides value-added services to users. Access to the Internet through mobile phones and other handheld devices is growing significantly in recent years. Many m-services applications have been developed for the handheld devices [5–8,38]. However, most current applications are customer-centered applications, for example, users can now surf the web, check e-mail, read news, and quote stock price, etc., using handheld devices. The mobile computing should not be limited to user-centered applications only. In this age of information, mobile applications should be extended to decision support in an organization. With a fast paced economy, organizations need to make decisions as fast as possible, they must gain competitive advantage by having access to the most current and accurate information available. For instance, a huge amount of financial news is generated everyday, and access to update financial information is important during decision making. On the other hand, the executives of an organization need make decision when they are on the road. As a result, there is an urgent need of information access through handheld devices.

There are many shortcomings associated with handheld devices although the development of handheld devices is fast in the recent years. The short comings include limited screen size with low resolution, low bandwidth, and low memory capacity. It is impossible to search and visualize the critical information on a small screen with an intolerable slow downloading speed using handheld devices. Automatic summarization summarizes a document for users to preview its major content. Users may determine if the information fits their needs by reading the summary instead of browsing the whole document one by one. The amount of information displayed and downloading time are significantly reduced. Active researches on automatic summarization have been carried out. Summarization techniques have been applied to delivery of information on handheld devices [3,42]. Traditional summarizations do not consider the hierarchical structure of document but consider the document as a sequence of sentences. Most traditional summarization systems extract sentences from the source document and concatenate together as summary. However, it is believed that the document summarization on handheld devices must make use of <sup>b</sup>tree view<sup>Q</sup> [7] or <sup>b</sup>hierarchical display<sup>Q</sup> [32]. Similar techniques have been applied to web browsing, an outline processor organizes the web page in a tree structure and the user click the link to expand the subsection and view the detail [4]. Hierarchical display is suitable for navigation of a large document and it is ideal for small area display. Therefore, a new summarization model with hierarch ical display is required for summarization on handheld devices. Summarization of web pages on handheld devices has been investigated [5–8]. However, a large document exhibits totally different characteristics from web pages. A web page usually contains a small number of sentences that are organized into paragraphs, but a large document contains much more sentences that are organized into a more complex hierarchical structure [48,49]. Besides, the summarization on webpage is mainly based on thematic features only [6]. However, it has been proved that other document features play a role as important as the thematic feature [10,22]. Therefore, a more advance summarization model combined with other document features is required for browsing of large document and other information sources on handheld devices [49–51]. With powerful summarization tool, the ability of handheld devices will be greatly enhanced. Visualization of various information sources becomes feasible, for example, financial news delivery to hand held devices. It provides an information visualization tool for m-commerce.

The information access through mobile devices has drawn attention from researchers in recent years. Mobile devices support instant information and data access that is capable to support decision making. For example, Mendelsohn [35] has presented how physicians may request information to answer questions that occur at the point-of-care through mobile devices. A number of researchers have worked on advanced text input entry for handheld device [29,30,39]. More specifically, there are researches that focus on navigation of documents on mobile devices. Lamming et al. [26] have presented the Satchel system that used tokens to represent documents on mobile device and developed a context-sensitive user interface. In this work, we focus on the delivery of information to handheld devices with the support of automatic summarization. Example of how the proposed system supports the delivery of Yahoo! financial information is presented.

The paper is organized as follows. Section 2 discusses the shortcomings of handheld devices and information visualization on handheld devices. The three-tier architecture, which reduces the computing load of the handheld devices, is used. Section 3 proposes the fractal summarization model based on the statistical data and the hierarchical structure of documents. Thematic, location, heading and cue features are adopted. Experiments have been conducted and the results show that the fractal summarization outperforms the traditional summarization. Fractal summarization is further extended to information browsing on handheld devices. Section 4 will demonstrate the financial news delivery on handheld devices.

## 2. Document delivery architecture on handheld devices

Traditionally, two-tier architecture is typically utilized for Internet access. The user’s PC connects to the Internet directly, and the content loaded will be fed to the web browser and present to the user as illustrated in Fig. 1.

However the information available online has increased explosively, it results in a well-recognized problem of information overloading. Advance-searching techniques solve the problem by filtering most of the irrelevant information. However, the precision of most of the commercial search engines is not high. Users may find only a few relevant documents out of a large pool of searching result. Due to the huge volume of documents, it will take a lot of time for the users to browse the searching result one by one and identify the relevant information using desktop computers. Automatic summarization summarizes a document for users to preview its major content. Users may determine if the information fits their needs by reading their summary instead of browsing the whole document one by one. The amount of information displayed and downloading time are significantly reduced. An automatic summarizer is therefore introduced to summarize a document for the users to preview before presenting the whole document. As shown in Fig. 2, the content will be first fed to the summarizer after loading to the user’s PC. The summarizer connects to database server when necessary and generates a summary to display on the browser.

The convenience of handheld devices allows information access without geometric limitation; however, there are other limitations of handheld devices that restrict their capability. Although the development of wireless handheld devices is fast in recent years, there are many shortcomings associated with these devices, such as screen size, bandwidth, and memory capacity. There are two major categories of wireless handheld devices, namely WAP-enabled mobile phones and wireless PDAs. At present, the typical display size of popular WAP-enabled handsets and PDAs are relatively small in comparison with a standard PC. The memory capacity of a handheld device greatly limits the amount of information that can be stored. A large document cannot be entirely downloaded to the handheld device and present to user directly. The current bandwidth available for WAP is relatively narrow. It is not comparable with the broadband internet connection for PC. The handheld devices impose other constraints that do not exist on desktop computers. The two-tier architecture cannot be applied on handheld devices since the computing power of handheld devices is insufficient to perform summarization and the network connection of mobile network does not provide sufficient bandwidth for navigation between the summarizer and other servers.

![](/api/attachments/J8PWSV3A/fulltext/images/945f174c6ea7c850512cd247cc5f2f26eb5c121a8e879bcb00663e319056e73e.jpg)  
Fig. 1. Document browsing on PC.

![](/api/attachments/J8PWSV3A/fulltext/images/234636362564e9219d5806a46b60e9d045f7aff6d413e3d1104a51124f6f0816.jpg)  
Fig. 2. Document browsing with summarizer on PC.

The three-tier architecture as illustrated in Fig. 3 is proposed. A WAP gateway is setup to conduct the summarization. The WAP gateway connects to Internet trough broadband network. The wireless handheld devices can conduct interactive navigation with the gateway through wireless network to retrieve the summary piece by piece. Alternatively, if the PDA is equipped with more memory, the complete summary can be downloaded to PDA through local synchronization.

![](/api/attachments/J8PWSV3A/fulltext/images/0573129608f9dfd6c1894f3785b1e2a8e24d4250bcdfa8a43678a574702e03ce.jpg)  
Fig. 3. Document browsing with summarizer on WAP.

## 3. Automatic summarization

## 3.1. Traditional summarization

Traditional automatic text summarization is the selection of sentences from the source document based on their significance to the document [10,28]. The selection of sentences is conducted based on the salient features of the document. The thematic, location, heading, and cue features are the most widely used summarization features.

<sup>!</sup> The thematic feature is first identified by Luhn [28]. Edmundson proposed to assign the thematic weight to keyword based on term frequency, and the sentence thematic score as the sum of thematic weight of constituent keywords [10]. In information retrieval, absolute term frequency by itself is considered as less useful than term frequency normalized to the document length and term frequency in the collection [18]. As a result, the tfidf (Term Frequency, Inverse Document Frequency) method is proposed to calculate the thematic weight of keyword [41].

<sup>!</sup> The significance of sentence is indicated by its location [2] based on the hypotheses that topic sentences tend to occur at the beginning or in the end of documents or paragraphs [10]. Edmundson proposed to assign positive weights to sentences as sentence location score according to their ordinal position in the document, i.e., the sentences in the first and last paragraphs and the first and last sentences of the paragraphs. There are several functions proposed to calculate the location weight of sentences. Alternatively, the preference of sentence location can be stored in a list called Optimum Position Policy, and the sentences will be selected base on their order in the list [27].

<sup>!</sup> The heading feature is proposed based on the hypothesis that the author conceives the heading as circumscribing the subject matter of the document. When the author partitions the document into major sections, he summarizes them by choosing appropriate headings [10]. The formulation of heading weight is very similar to the thematic feature. A heading glossary is a list consisting of all the words in headings and subheadings. Positive weights are assigned to the heading glossary, where the heading words will be assigned a weight relatively prime to the subheading words. The sentence heading score of sentence is calculated by the sum of heading weight of its constituent words.

<sup>!</sup> The cue phrase feature is proposed by Edmundson [10] based on the hypothesis that the probable relevance of a sentence is affected by the presence of pragmatic words such as <sup>b</sup>significant<sup>Q</sup>, <sup>b</sup>impossible<sup>Q</sup>, and <sup>b</sup>hardly<sup>Q</sup>. A pre-stored cue dictionary is used to identify the cue phases, which comprises of three sub-dictionaries: (i) bonus words, that are positively relevant; (ii) stigma words, that are negatively relevant; and (iii) null words, that are irrelevant. The sentence cue score of sentence is calculated by the sum of cue weight of its constituent words.

Typical summarization systems select a combination of summarization features [10,25,27], the total sentence significance score (SSS) is calculated as,

$$
\begin{array}{r l} \mathrm{SSS} & = a _ {1} \times \mathrm{SS} _ {\text { thematic }} + a _ {2} \times \mathrm{SS} _ {\text { location }} + a _ {3} \\ & \times \mathrm{SS} _ {\text { heading }} + a _ {4} \times \mathrm{SS} _ {\text { cue }} \end{array}\tag{1}
$$

where $\mathrm { S S _ { t h e m a t i c } , \ S S _ { l o c a t i o n } , \ S S _ { h e a d i n g } }$ and ${ \mathrm { S S } } _ { \mathrm { c u e } }$ are sentence scores based on thematic feature, location feature, heading feature and cue phrase feature, respectively; and $a _ { 1 } , a _ { 2 } , a _ { 3 }$ , and $a _ { 4 }$ are positive integers to adjust the weighting of four summarization features. The sentences with sentence significant score higher than a threshold are selected as part of the summary. It has been proved that the weighting of different summarization features does not have any substantial effect on the average precision [25]. In our experiment, the maximum score of each feature is normalized to one, and the sentence significant score is calculated as the sum of scores of all summarization features without weighting.

![](/api/attachments/J8PWSV3A/fulltext/images/cb99893c05b92e1afb7bd09dc779ce2a728967cc68446704f216e9ba2155802c.jpg)  
Fig. 4. Koch curve at different abstractions level.

## 3.2. Fractal theory and fractal view for controlling information displayed

Fractals are mathematical objects that have high degree of redundancy [31]. These objects are made of transformed copies of themselves or part of themselves (Fig. 4). Mandelbrot was the first researcher who investigated the fractal geometry and developed the fractal theory [31]. In his well-known example, the length of the British coastline depends on measurement scale. The larger the scale is, the smaller value of the length of the coastline is and the higher the abstraction level is. The British coastline includes bays and peninsulas. Bays include subbays and peninsulas include sub-peninsulas. Using fractals to represent these structures, abstraction of the British coastline can be generated with different abstraction degrees. Fractal theory is grounded in geometry and dimension theory. Fractals are independent of scale and appear equally detailed at any level of magnification. Such property is known as self-similarity. Any portion of a self-similar fractal curve appears identical to the whole curve. If we shrink or enlarge a fractal pattern, its appearance remains unchanged.

Fractal view is a fractal-based method for controlling information displayed [23]. Fractal view provides an approximation mechanism for the observer to adjust the abstraction level and therefore control the amount of information displayed. At a lower abstraction level, more details of the fractal object can be viewed.

A physical tree is one of the classical examples of fractal objects. A tree is made of a lot of sub-trees; each of them is also a tree. By changing the scale, the different levels of abstraction views are obtained (Fig. 5). The idea of fractal tree can be extended to any logical tree. The degree of importance of each node is represented by its fractal value. The fractal value of root is 1, it propagated to other nodes with the following expression:

$$
\left\{ \begin{array}{l} F v _ {\text { root }} = 1 \\ \text { Fv } _ {\text { child   mode   of   } x} = C \frac {\text { Fv } _ {x}}{N _ {x} ^ {1 / D}} \end{array} \right.\tag{2}
$$

where $\operatorname { F v } _ { x }$ is the fractal value of node x; C is a constant between 0 and 1 to control rate of decade; $N _ { x }$ is the number of child nodes of node x; and D is the fractal dimension. Mandelbrot had shown that the fractal dimension of a tree is 1, because its total length is finite and positive [31]. To simplify our discussion, both C and D are considered to be 1.

A threshold value is chosen to control the amount of information displayed, the nodes with a fractal value less than the threshold value will be hidden (Fig. 6). By changing the threshold value, the user can adjust the amount of information displayed.

## 3.3. Fractal summarization

Advance summarization techniques take the document structure into consideration to compute the probability of a sentence to be included in the summary. Many studies of human abstraction process had shown that the human abstractors extract the topic

![](/api/attachments/J8PWSV3A/fulltext/images/0db6dcfd165a2e563369c2364fa6222f57ecfeb248b9090a38da716a9f0d674b.jpg)  
Fig. 5. Fractal view for logical tree at different abstraction level.

![](/api/attachments/J8PWSV3A/fulltext/images/7b83fe4e282053f4d9ac68adff0862f7986c395f35cbf9307a4a4a0c6ecaa398.jpg)  
Fig. 6. An example of the propagation of fractal values.

sentences according to the document structure from the top level to the low level until sufficient information has been extracted [11,15]. However, most traditional automatic summarization models consider the source document as a sequence of sentences but ignoring the structure of document. Some summarization systems may calculate sentence weight partially based on the document structure, but they extract sentences in a linear space. None of the current summarization model is developed on the foundation of the hierarchical structure of documents. Fractal Summarization Model is proposed here to generate summary based on document structure. Fractal summarization generates a brief skeleton of summary at the first stage, and the details of the summary on different levels of the document are generated on demands of users. Such interactive summarization reduces the computation load in comparing with the generation of the entire summary in one batch by the traditional automatic summarization, which is ideal for m-commerce.

Fractal summarization is developed based on the fractal theory. In fractal summarization, the important information is captured from the source text by exploring the hierarchical structure and salient features of the document. A condensed version of the document that is informatively close to the original document is produced iteratively using the contractive transformation in the fractal theory. Similar to the fractal geometry applying on the British coastline where the coastline includes bays, peninsulas, sub-bays, and sub-peninsulas, large document has a hierarchical structure with several levels, chapters, sections, subsections, paragraphs, sentences, and terms. A document is considered as prefractal that are fractal structures in their early stage with finite recursion only [12]. A document can be represented by a hierarchical structure as shown in Fig. 7. A document consists of chapters. A chapter consists of sections. A section may consist of subsections. A section or subsection consists of paragraphs. A paragraph consists of sentences. A sentence consists of terms. A term consists of words. A word consists of characters. A document structure can be considered as a fractal structure. At the lower abstraction level of a document, more specific information can be obtained. Although a document is not a true mathematical fractal object since a document cannot be viewed in an infinite abstraction level, we may consider a document as a prefractal. The smallest unit in a document is character;

![](/api/attachments/J8PWSV3A/fulltext/images/74c1e3b06ab9621cff6389a3117d6f782fa3b0f41059bba0bd7d0f506b943b3d.jpg)  
Fig. 7. Prefractal structure of document.

however, neither a character nor a word will convey any meaningful information concerning the overall content of a document. The lowest abstraction level in our consideration is a term.

The Fractal Summarization Model applies techniques from fractal view and fractal image compression [1,21]. In fractal image compression, an image is regularly segmented into sets of non-overlapping square blocks, called range-blocks, and then each range-block is sub-divided into subrange-blocks, until a contractive mapping can be found to represent this subrange-block. The Fractal Summarization Model generates the summary by a recursive deterministic algorithm based on the iterated representation of a document. The original document is represented as fractal tree structure according to its hierarchical document structure. Then, the system calculates the fractal value of each node and allocates the sentence quota base on the fractal value. The calculation of fractal value will be discussed later in this section.

Given a document, a user can specify compression ratio to indicate the amount of information displayed. The summarization system calculates the number of sentences to be extracted as summary accordingly and the system assigns the number of sentences to the root of document tree as the quota of sentences. The quota of sentences is allocated to child nodes by propagation, i.e., the quota of parent node is shared by its child nodes directly proportional to the fractal value of the child nodes. The quota is then iteratively allocated to child nodes of child nodes until the quota allocated is less than a threshold value and the range-block can be transformed to some key sentences by traditional summarization methods (Fig. 8). The detail of the Fractal Summarization Model is shown as the following algorithm:

## Fractal Summarization Model

1. Choose a Compression Ratio.

2. Choose a Threshold Value.

3. Calculate the Sentence Number Quota of the summary.

4. Divide the document into range-blocks.

5. Transform the document into fractal tree.

6. Set the current node to the root of the fractal tree.

## 7. Repeat

7.1 For each child node under current node, Calculate the fractal value of child node.

7.2 Allocate Quota to child nodes in proportion to fractal values.

7.3 For each child nodes, If the quota is less than threshold value Select the sentences in the range-block by extraction Else Setthecurrentnodetothechildnode Repeat Step 7.1, 7.2, 7.3

8. Until all the child nodes under current node are processed

The compression ratio of summarization is defined as the ratio of number of sentences in the summary to the number of sentences in the source document. It was chosen as 25% in most literatures because it has been proved that extraction of 20% sentences can be as informative as the full text of the source document [36], those summarization systems can achieve up to a 96% precision [10,22,44]. However, Teufel pointed out the high-compression ratio abstracting is more useful, and 49.6% of precision is reported at 4% compression ratio [43,44]. In order to minimize the bandwidth requirement and reduce the pressure on computing power of handheld devices, the default value of compression ratio is chosen as 4% for fractal summarization on handheld devices. On the other hand, a threshold value is the maximum number of sentences can be extracted from a range-block that is a node in the document tree. If the quota allocated is larger than the threshold value, the range-block must be divided into subrange-block. Document summarization is different from image compression, more than one attractor can be chosen in one range-block. The summarization by extraction of fixed number of sentences is proven; the optimal length of summary is 3 to 5 sentences [16]. The default value of threshold is chosen as 5 in our system.

The fractal value Fv of range-block r is computed based on Range-block Significance Score (RBSS), where the RBSS is computed as the sum of the normalized weights of the sentence scores based on the four salient features as introduced in Section 3.1.

![](/api/attachments/J8PWSV3A/fulltext/images/254cc88bab6b2ac00f2e001f988ef3e3dabd9aff1c8c43b3071ee5d6452bec6a.jpg)  
Fig. 8. An example of fractal summarization model.

$$
\operatorname{Fv} (r) = \left\{ \begin{array}{l l} 1 & \text {   if   } r \text {   is   root   } \\ C \operatorname{Fv} (\text {   parent   of   } r) \times \left(\frac {\mathrm{RBSS} (r)}{\sum \mathrm{RBSS} (x)}\right) ^ {\frac {1}{D}} & \text {   otherwise   } \\ x \in \text {   sibling   of   } r \end{array} \right.\tag{3}
$$

The system utilizes the fractal value to compute the sentence quota of each range-block by sharing the quota of parent node directly proportional to the fractal value of the child nodes, until the sentence quota allocated is less than the threshold value, and the system can extract sentences directly from the range-block. During extraction of sentences in the range-block, the system will extract the sentences according to the fractalized sentence weight of the sentences.

## 3.4. Experimental result

It is believed that a full-length text document contains a set of subtopics [20] and a good quality summary should cover as many subtopics as possible, experiments showed that the fractal summarization model produces a summary with a wider coverage of information subtopic than traditional summarization model.

Experiment of fractal summarization and traditional summarization with four unweighted features described in Section 3.1 was conducted on Hong Kong Annual Report 2000. In the experiment, it is found that the traditional summarization model extracts most of sentences from few chapters. As shown in Table 1, the traditional summarization extracts 29 sentences from one chapter when the sentence quota is 80 sentences, and 53 sentences are extracted from top 3 chapters out of total 23 chapters, no sentence is extracted from 8 chapters. However, the fractal summarization extracts the sentences evenly from each chapter. It extracts maximum 8 sentences and minimum 1 sentence from each chapter (Table 1). The standard deviation of sentence number extracted from chapters is 2.11 sentences in fractal summarization against 6.55 sentences in traditional summarization. Researchers believed that a good summary should find diverse topic areas in the text and reduce the redundancy of information contents in the summary [37]. Fractal summarization extracts the sentences distributively from the document, therefore it finds diverse topic areas and reduces the redundancy of information at the same time.

A user evaluation is conducted. Ten subjects were asked to evaluate the quality of summaries of 23 documents generated by fractal summarization and traditional summarization. Both summaries of all documents are assigned to each subject in random order without telling the generation methods of the summaries. The results show that all subjects consider the summary generated by fractal summarization method as a better summary. In order to compare the result in more great detail, we calculate the precision as the number of relevant sentences in the summary accepted by the user divided by the number of sentences in the summary (Table 2). The fractal summarization can achieve up to 91.25% precision and 87.16% on average, while the traditional summarization can achieve up to a maximum of 77.50% precision and 67.00% on average. One-tailed T-test has shown that the precision of fractal summarization model outperforms the traditional summarization significantly at 99% confidence level. Experiment of fractal summarization and traditional summarization with four unweighted features described in Section 3.1 was conducted on Hong Kong Annual Report 2000. In the experiment, it is found that the traditional

Table 1 Number of sentences extracted by two summarization models from Hong Kong Annual Report 2000

<table><tr><td>Chapter ID</td><td>Chapter title</td><td>Number of sentences extracted in fractal summarization model</td><td>Number of sentences extracted in traditional summarization model</td></tr><tr><td>1</td><td>Hong Kong: Asia&#x27;s World City</td><td>6</td><td>3</td></tr><tr><td>2</td><td>Constitution and Administration</td><td>4</td><td>1</td></tr><tr><td>3</td><td>The Legal System</td><td>2</td><td>0</td></tr><tr><td>4</td><td>The Economy</td><td>5</td><td>14</td></tr><tr><td>5</td><td>Financial and Monetary affairs</td><td>8</td><td>29</td></tr><tr><td>6</td><td>Commerce and Industry</td><td>6</td><td>10</td></tr><tr><td>7</td><td>Employment</td><td>2</td><td>2</td></tr><tr><td>8</td><td>Primary Production</td><td>1</td><td>0</td></tr><tr><td>9</td><td>Education</td><td>2</td><td>1</td></tr><tr><td>10</td><td>Health</td><td>1</td><td>0</td></tr><tr><td>11</td><td>Social Welfare</td><td>1</td><td>0</td></tr><tr><td>12</td><td>Housing</td><td>1</td><td>0</td></tr><tr><td>13</td><td>Land, Public Works and Utilities</td><td>4</td><td>0</td></tr><tr><td>14</td><td>Transport</td><td>5</td><td>3</td></tr><tr><td>15</td><td>Infrastructure</td><td>1</td><td>0</td></tr><tr><td>16</td><td>The Environment</td><td>4</td><td>1</td></tr><tr><td>17</td><td>Travel and Tourism</td><td>1</td><td>1</td></tr><tr><td>18</td><td>Public Order</td><td>5</td><td>2</td></tr><tr><td>19</td><td>Communications, the Media and Information Technology</td><td>6</td><td>6</td></tr><tr><td>20</td><td>Religion and Custom</td><td>2</td><td>0</td></tr><tr><td>21</td><td>Recreation, Sport and the Arts</td><td>5</td><td>3</td></tr><tr><td>22</td><td>Population and Immigration</td><td>3</td><td>1</td></tr><tr><td>23</td><td>History</td><td>5</td><td>3</td></tr></table>

summarization model extracts most of sentences from few chapters. As shown in Table 1, the traditional summarization extracts 29 sentences from one chapter when the sentence quota is 80 sentences, and 53 sentences are extracted from top 3 chapters out of total 23 chapters, no sentence is extracted from 8 chapters. However, the fractal summarization extracts the sentences evenly from each chapter. It extracts a maximum of 8 sentences and a minimum of 1 sentence from each chapter (Table 1). The standard deviation of sentence number extracted from chapters is 2.11 sentences in fractal summarization against 6.55 sentences in traditional summarization. Researchers believed that a good summary should find diverse topic areas in the text and reduce the redundancy of information contents in the summary [37]. Fractal summarization extracts the sentences evenly from the document; therefore it finds diverse topic areas and reduces the redundancy of information at the same time.

We have also conducted another experiment using the tested TIPSTER Text Summarization Evaluation (SUMMAC) data. The TIPSTER Text Summarization Evaluation (SUMMAC) is the first large-scale, developer-independent evaluation of automatic text summarization systems [33]. The documents for the TIPSTER evaluation are drawn from Text Retrieval (TREC) [19] CDs 4 and 5. The categorization task in SUMMAC focuses on generic summaries. The task sought to find out whether a generic summary could effectively present sufficient information to allow an analyst to quickly and correctly categorize a document. In order to compare the performance with other summarization systems, we have conducted the categorization task to evaluate the performance of the fractal summarization model. We have followed the standard TIPSTER setting to conduct the classification task using fractal summarization. 100 documents are selected from the TIPSTER corpus, and 10% of sentences are extracted from each document by fractal summarization system. 15 subjects are involved in the experiment. The subjects need to classify the documents based on the sentences extracted for each document. The experiment result shows that the fractal summarization system has a similar precision as other summarization systems, and it has a better recall. The fractal summarization achieves an Fscore [40] of 0.63 but other summarization systems achieve a mean F-score of 0.42. Therefore, the fractal summarization system outperforms other summarization systems. As the documents used are relatively shorter in their length, most of them contain less than 100 sentences.

Precision of summaries of Hong Kong Annual Report 2000 for two summarization models

<table><tr><td>User ID</td><td>Fractal summarization model (%)</td><td>Traditional summarization model (%)</td></tr><tr><td>User 1</td><td>81.25</td><td>71.25</td></tr><tr><td>User 2</td><td>85.00</td><td>67.50</td></tr><tr><td>User 3</td><td>80.00</td><td>56.25</td></tr><tr><td>User 4</td><td>85.00</td><td>63.75</td></tr><tr><td>User 5</td><td>88.75</td><td>77.50</td></tr><tr><td>User 6</td><td>81.25</td><td>61.25</td></tr><tr><td>User 7</td><td>91.25</td><td>76.25</td></tr><tr><td>User 8</td><td>86.25</td><td>58.75</td></tr><tr><td>User 9</td><td>85.00</td><td>65.00</td></tr><tr><td>User 10</td><td>87.50</td><td>72.50</td></tr></table>

## 3.5. Visualization of fractal summarization on hand held devices

The summary generated by Fractal Summarization Model is represented in a hierarchical tree structure. The hierarchical structure of summary is suitable for visualization of information on handheld devices. However, a summary displayed in a small area of handheld devices without visualization effect is still difficult to read, it can be further enhanced by displaying the sentences in different font sizes according to their importance to help user to focus on important information and search for information easily.

WML is the markup language supported by wireless handheld devices. The basic unit of a WML file is a deck; each deck must contain one or more cards. The card element defines the content displayed to users, and the card cannot be nested. Each card links to another card within or across decks. Nodes on the fractal tree of fractal summarization model are converted into cards, and anchor links are utilized to implement the tree structure. Given a card of a summary node, there may be a lot of sentences or child nodes. A large number of sentences in a small display area make it difficult to read. Fisheye View is a visualization technique to enlarge the focus of interest and diminish the information that is less important [13]. When a user look at an object, the objects nearby are shown in a larger visual size; and the visual size of other objects is decreased inversely proportional to their distances to the focus point.

In our system, we have modified the fisheye view. The size of an object does not depend on its distance from the focus point, but depends on the significance of the object. The sentences are displayed in different font sizes according to their importance. We have implemented the fisheye view with 3-scale font mode available for WML. The sentences or child nodes are sorted by their sentence weights or fractal value and separated evenly into three groups. The group with highest value is displayed in <sup>b</sup>Large<sup>Q</sup> font size, and the group with middle value and the group with lowest value are displayed in <sup>b</sup>Normal<sup>Q</sup> and <sup>b</sup>Small<sup>Q</sup> font size, respectively.

![](/api/attachments/J8PWSV3A/fulltext/images/cc20ce1c1eb57bcecc5be59285e73cfd33824d84737298f24042772b07a52ff7.jpg)  
(a)

![](/api/attachments/J8PWSV3A/fulltext/images/a3a0fd4b9e990ec9a6b49989e2b85919ac45b934a5544726a966076124a46c1c.jpg)  
(b)  
Fig. 9. Screen capture of WAP summarization system. (a) Hong Kong Annual Report 2000; (b) Chapter 19 of Hong Kong Annual Report 2000, <sup>d</sup>Communication, the Media and Information Technology<sup>T</sup>.

The prototype system using Nokia Handset Simulator is presented in Fig. 9. The document presenting is the Hong Kong Annual Report 2000. There are totally 23 chapters in the annual report, 8 of them are in large font, which means that they are more important, and the rest are in normal font or small font according to their importance to the report (Fig. 9a). The number inside the parentheses indicates the number of sentences under the node that are extracted as part of the summary. The main screen of the Hong Kong Annual Report 2000 gives user a general idea of overall information contents and the importance of each chapter. If the user wants to explore a particular node, user can click the anchor link, and the handheld device sends the request to the WAP gateway, and the gateway then decides whether to deliver another menu or the summary of the node to the user depends on its fractal value and quota allocated. Fig. 9b shows the summary of Chapter 19 of Hong Kong Annual Report 2002, <sup>b</sup>Communication, the Media and Information Technology<sup>Q</sup>.

A handheld PDA is usually equipped with more memory, and the complete summary can be downloaded as a single WML file to the PDA through local synchronization. To read the summary, the PDA is required to install a standard WML file reader, i.e., KWML for Palm [24].

## 4. Summarization for financial news delivery on handheld devices

Fractal summarization model summarizes the documents based on hierarchical document structure. In addition to large text document, a lot of other information sources also exhibit hierarchical document structure, such as web-site and newspaper. Due to the huge information available, it is difficult to browse these information sources on handheld devices. Automatic summarization is a possible solution. Theoretically, the fractal summarization is capable to summarize to all these information sources as long as the calculation of fractal value is well formulated. As financial news is critical in decision making, we shall modify the fractal value formula of generic fractal summarization in order to summaries the financial news and we shall demonstrate financial news delivery with fractal summarization on handheld devices.

## 4.1. Fractal summarization of financial news

Fractal summarization model performs the summarization based on hierarchical document structure. In addition to large text documents, a lot of other documents also exhibit hierarchical tree document structure, such as web-site, newspaper, etc. The fractal summarization model is capable to summarize these documents based on their structure and their relationships in categorization; therefore, it is a powerful tool in providing m-services of real time information delivery. As present, a lot of electronic news delivery services have been provided. An example of the fractal summarization model being used to summarize the financial news available from Internet is presented in this section.

Newspaper is one of the documents that exhibit the well-defined hierarchical document structure. At present, there is a lot of electronic news delivery services provided for PC, and most of them provide summarization tools to help user to search information, such as Lycos Financial Feed System with summarization system from Diyatech [9], Yellow-Brix with Inxight’s Summarizer [52] and Columbia’s Newsblaster [34]. However, summarizers for PC platform are not adaptable to mobile devices directly. Moreover, the existing commercial summarizers are indeed extracting the first few sentences from the document or using the primitive summarization model without considering the hierarchical structure of documents or the organization of information. Yahoo!News [47] is one of the most popular online content providers. There are 21 categories in the Yahoo!News. Moreover, each of the categories will be sub-divided into subcategories. Take the Business category as an example (Fig. 10), this category contains financial news and it is sub-divided into six sub-categories, namely, Economy, Stock Markets, Earnings, Personal Finance, Industries and Commentary. Each sub-category contains around 10 news articles. Each news article is a tree structure by itself. For some longer news article, there may exist more than one section, and each section contains few paragraphs, and paragraph contains sentences.

The Fractal Summarization of Yahoo!News is very similar to the fractal summarization of large text document, only some minor modifications are required to demonstrate the characteristic of the Yahoo!News.

![](/api/attachments/J8PWSV3A/fulltext/images/31df3bf1b116f558e1126383b74a6497a41ae27cd9118ed4aebddd1ea0724066.jpg)  
Fig. 10. Fractal summarization of yahoo! news-<sup>d</sup>business<sup>T</sup> category.

<sup>!</sup> Firstly, the headings of categories and subcategories do not have a direct impact on the content of news under the branch; it serves for classification purpose only. As a result, the heading method will consider the headings of news articles only. In addition, the headings of categories can be used for personalization of news delivery, the user can set his preference of each category in advance and the system will adjust the weights accordingly. Alternatively, the preference can be constructed by autolearning of machine in the middle-tier. The WAP gateway can analyze the reading behavior of user and predict the user’s preference.

<sup>!</sup> The location feature in traditional summarization assumes that the text unit in the beginning or ending is more important. The news articles inside a subcategory are sorted in chronological order. The most recent news is usually considered as more important. Therefore, we propose calculating the location weight of a news article by its chronological position in the subcategory or the time-lag between the news event and browsing time. However, when the system traces the summarization tree down to a node inside a news article, the generic location method in fractal summarization will be adopted.

<sup>!</sup> In order to provide a glimpse of every article, each news article will receive a sentence quota with at least one sentence.

## 4.2. Financial news delivery to handheld devices

In order to minimize the bandwidth requirement and reduce the pressure on computing power of handheld devices, the summarization of Yahoo!News will be conducted in two levels. As high-compression ratio abstracting is more useful [43] and it can save the network bandwidth, the fractal summarization system generates a brief skeleton of summary with compression ratio equals to 4% at the first stage. The details of the summary at different levels of the news tree are generated on demands of users.

When handheld device retrieves the financial news from Yahoo! News-Business, the system will first show a card containing with 6 subcategories of <sup>d</sup>Business<sup>T</sup> category (Fig. 11). In the figure, three subcategories of Business category are displayed in large font, which means that they are more important; and the rest are in normal font or small font according to their importance. The skeleton of news gives user a general idea how the news articles are organized, and the user can decide which subcategory to go into details. When the user clicks the anchor link of subcategory, the WAP gateway will deliver a card depends on the quota allocated. If a large quota is allocated to the subcategory, the system will show another card containing of index of news article. However, if the quota is less than a threshold value of 5 sentences, the system will show a card with the summary of all news articles in the subcategory. In the summary page, when the user clicks the anchor link <sup>d</sup>More<sup>T</sup> at end of sentences, the system will generate the summary for the corresponding news articles with compression ratio 20%, because it has been proved that extraction of 20% sentences can be as informative as the full text of the source document [36]. On the other hand, the user can click the anchor link <sup>d</sup>Full<sup>T</sup> to view the full text of the news articles. Such interactive summarization reduces the computation load in comparing with the generation of the entire summary in one batch by the traditional automatic summarization, which is ideal for m-services.

## 4.3. Future work

In current stage, the fractal summarization is capable to process textual information only. However, there is a lot of information available in multimedia format on the Web. Information delivery of multimedia document will be one of the key research topics in the near future. As the multimedia documents require a much higher bandwidth than textual documents, this problem cannot be resolved solely by the current steaming technology. Summarization of multimedia documents is required for information delivery to mobile devices. The research work of spoken document was initiated in the spoken language track of TREC 1997 [14]. The research of spoken document summarization starts in 2000 [53,54]. Summarization of video has also been investigated [45,46]. It would be a great challenge to move the proposed model to multimedia documents.

![](/api/attachments/J8PWSV3A/fulltext/images/0d394a81ad49d124bfe5db8a1203ac834fe41a0aceced5db3c726f1a95d5faa9.jpg)  
Fig. 11. Financial news delivery system on mobile devices.

The summarization of multimedia document is a complementary to the proposed model. Nowadays, most of the mobile devices are speech-based. With the summarization of spoken documents, the information can be easily delivered to speech-based mobile devices. This will certainly increase the popularity of the proposed model. Moreover, it can provide information access for the blind as well [17].

## 5. Conclusion

Mobile commerce is a promising addition to the electronic commerce by the adoption of portable handheld devices. However, the mobile computing should not be limited to user-centered m-services applications only, it should be extended to decision making in an organization. With a fast paced economy, organization need to make a decision as fast as possible, access to large text documents or other information sources is important during decision making. Unfortunately, there are many shortcomings of the handheld devices, such as limited resolution and narrow bandwidth. In order to overcome the shortcomings, fractal summarization and information visualization are proposed in this paper, which are critical in decision support in an m-organization. The fractal summarization creates a summary in hierarchical tree structure and presents the summary to the handheld devices through cards in WML. The adoption of keyword feature, location feature, heading feature, and cue feature are discussed. Users may browse the selected summary by clicking the anchor links from the highest abstraction level to the lowest abstraction level. Fractal views are utilized to filter the less important nodes in the document structure, sentences are displayed in different font size to enlarge the focus of interest and diminish the less significant sentences. Such visualization effect draws users’ attention on the important content. The three-tier architecture is presented to reduce the computing load of the handheld devices. The proposed system creates an information visualization environment to avoid the existing shortcomings of handheld devices for mobile commerce.

## References

[1] M.F. Barnsley, A.E. Jacquin, Application of recurrent iterated function systems to images, Proceedings of SPIE Visual Communications and Image Processing (VCIP’88), Cambridge, MA, USA, vol. 1001, SPIE, 1988 (Nov.), pp. 122–131.

[2] P.B. Baxendale, Machine-made index for technical literature— an experiment, IBM Journal of Research and Development 2 (4) (1958 (Oct.)) 354–361.

[3] B. Boguraev, R. Bellamy, C. Swart, Summarization miniaturization: delivery of news to handhelds, Proceedings of Workshop on Automatic Summarization 2001, pp. 99–110, in conjunction with The Second Meeting of the North American Chapter of the Association for Computational Linguistics (NAACL 2001), Association for Computational Linguistics, Pittsburgh, PA, USA, 2001 (Jun.).

[4] M.H. Brown, W.E. Weihl, Zippers: a Focus+Context display of web pages, Proceedings of World Conference of the Web Society (WebNet<sup>T</sup>96), San Francisco, CA, USA 1996 (Oct.), DEC SRC Technical Report 140, (1996 (May)).

[5] O. Buyukkokten, H. Garcia-Molina, A. Paepcke, T. Winograd, Power browser: efficient web browsing for PDAs, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI 2000), ACM Press, Hague, Netherlands, 2000 (Apr.), pp. 430– 437.

[6] O. Buyukkokten, H. Garcia-Molina, A. Paepcke, Seeing the whole in parts: text summarization for web browsing on handheld devices, Proceedings of the 10th International Conference on World Wide Web (WWW10), ACM Press, Hong Kong, China, 2000 (May), pp. 652–662.

[7] O. Buyukkokten, H. Garcia-Molina, A. Paepcke, Accordion summarization for end-game browsing on PDAs and cellular phones, Proceedings of the SIGCHI Conference on Human Factors in Computing System (CHI 2001), ACM Press, Seattle, WA, USA, 2001 (Mar.), pp. 213– 220.

[8] O. Buyukkokten, H. Garcia-Molina, A. Paepcke, Text summarization of web pages on handheld devices, Proceedings of Workshop on Automatic Summarization 2001, in conjunction with The Second Meeting of the North American Chapter of the Association for Computational Linguistics (NAACL 2001), Association for Computational Linguistics, Pittsburgh, PA, USA, 2001 (Jun.).

[9] Diyatech Homepage, http://www.diyatech.com/clycos.htm.

[10] H.P. Edmundson, New method in automatic extraction, Journal of the ACM 16 (2) (1969 (Apr.)) 264–285.

[11] B. Endres-Niggemeyer, E. Maier, A. Sigel, How to implement a naturalistic model of abstracting: four core working steps of an expert abstractor, Information Processing and Management 31 (5) (1995 (Sep.)) 631– 674.

[12] J. Feder, Fractals, Plenum, New York, 1988.

[13] G.W. Furnas, Generalized fisheye views, Proceedings of the SIGCHI Conference on Human Factors in Computing System (CHI ’86), ACM SIGCHI Bulletin, vol. 17 (4), 1986 (Apr.), pp. 16 – 23.

[14] J.S. Garofolo, E.M. Voorhess, V.M. Stanford, K.S. Jones, TERC-6 1997 spoken document retrieval track overview and results, Proceeding of the Sixth Text REtrieval Conference (TREC 6), National Institute of Standards and Technology (NIST), Gaithersburg, MD, USA, 1997 (Nov.), pp. 83– 91.

[15] B.G. Glaser, A.L. Strauss, The Discovery of Grounded Theory; Strategies for Qualitative Research, Aldine de Gruyter, New York, 1967.

[16] J. Goldstein, M. Kantrowitz, V. Mittal, J. Carbonell, Summarizing text documents: sentence selection and evaluation metrics, Proceedings of the Twenty-Second Annual International ACM-SIGIR Conference on Research and Development in Information Retrieval, (SIGIR’99), Berkeley, California, USA, ACM Press, 1999 (Aug.), pp. 121– 128.

[17] G. Grefenstette, Producing intelligent telegraphic text reduction to provide an audio scanning service for the blind, Working Notes of the American Association for Artificial Intelligence 1998 Spring Symposium (AAAI’98) on Intelligent Text Summarization, Stanford, California, AAAI Press, 1998 (Mar.), pp. 111 –117.

[18] D.K. Harman, Ranking algorithms, in: W.B. Frakes, R. Baeza-Yates (Eds.), Information Retrieval: Data Structures and Algorithms, Prentice-Hall, 1992, pp. 363 – 392 (Ch. 14).

[19] D.K. Harman, E.M. Voorhees, The Fifth Text REtrieval Conference (TREC-5), NIST Special Publication, vol. 500-238, National Institute of Standards and Technology, Gaithersburg, MD, USA, 1996 (Nov.).

[20] M.A. Hearst, Subtopic structuring for full-length document access, Proceedings of the 16th Annual International ACM SIGIR Conference on Research and Development in Informa tion Retrieval (SIGIR’93), Pittsburgh, Pennsylvania, USA, 1993 (Jun.), pp. 56 – 68.

[21] A.E. Jacquin, Fractal image coding: a review, Proceedings of the IEEE, vol. 81 (10), 1993 (Oct.), pp. 1451 – 1465.

[22] J. Kepiec, J. Pedersen, F. Chen, A trainable document summarizer, Proceedings of the 18th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR’95), Seattle, Washington, USA, 1995 (Jul.), pp. 68 – 73.

[23] H. Koike, Fractal views: a fractal-based method for controlling information display, ACM Transactions on Information Systems (TOIS) 13 (3) (1995 (Jul.)) 305–323.

[24] KWML. KWML-KVM WML (WAP) Browser on Palm. PALM Inc., http://www.jshape.com/kwml/index.html, (2002).

[25] M. Lam-Adesina, G.J.F. Jones, Applying summarization techniques for term selection in relevance Feedback, Proceedings of the 24th Annual International ACM SIGIR Conference on Research and Development in Information Retrieva (SIGIR’01), New Orleans, Louisiana, USA, ACM Press, 2001 (Sep.), pp. 1 – 9.

[26] M. Lamming, M. Eldridge, M. Flynn, C. Jones, D. Pendlebury, Satchel: providing access to any document, any time, anywhere, ACM Transactions on Computer-Human Interaction (TOCHI), special issue on human–computer interaction with mobile systems 7 (3) (2000 (Sep.)) 322–352.

[27] Y. Lin, E.H. Hovy, Identifying topics by position, Proceedings of the Workshop of Intelligent Scalable Text Summari zation, in conjunction of the Fifth Conference on Applied Natural Language Processing (ANLP-97), Washington, DC, Association for Computational Linguistics, 1997 (Mar.), pp. 283 – 290.

[28] H.P. Luhn, The automatic creation of literature abstracts, IBM Journal of Research and Development 2 (2) (1958 (Apr.)) 159–165.

[29] I.S. MacKenzie, R. Soukoreff, Text entry for mobile comput ing: models and methods, theory and practice, Human–Com puter Interaction 17 (2 and 3) (2002) 147– 198.

[30] I.S. MacKenzie, Mobile text entry using three keys, Proceedings of the Second Nordic Conference on Human Computer Interaction. (NordiCHI 2002), ACM Press, Aarhus, Denmark, 2002 (Oct.), pp. 27– 34.

[31] B. Mandelbrot, The Fractal Geometry of Nature, W.H. Freeman, New York, 1983.

[32] I. Mani, Recent development in text summarization, The Proceedings of the tenth International Conference on Information and Knowledge Management (CIKM’01), ACM Press, Atlanta, GA, USA, 2001 (Nov.), pp. 529– 531.

[33] I. Mani, D. House, G. Klein, L. Hirschman, T. Firmin, B. Sundheim, The TIPSTER SUMMAC text summarization evaluation, Proceedings of the Ninth Conference on European

Chapter of the Association for Computational Linguistics (EACL’99), University of Bergen, Bergen, Norway, 1999 (Jun.), pp. 77–85.

[34] K. McKeown, R. Barzilay, J. Chen, D. Elson, D. Evans, J. Klavans, A. Nenkova, B. Schiffman, S. Sigelman, Columbia’s newsblaster: new features and future directions, Proceedings of the 2003 Human Language Technology conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL 2003), Demonstrations, Association for Computational Linguistics, Edmonton, Canada, 2003 (May), pp. 15 – 16.

[35] T. Mendelsohn, Content at the point-of-care: in the palm of a doctor’s hand, Proceedings of Online Information, London, U.K., 2001 (Dec.), pp. 169–174.

[36] A.H. Morris, G.M. Kasper, D.A. Adams, The effects and limitations of automated text condensing on reading comprehension performance, Information Systems Research 3 (1) (1992 (Mar.)) 17–35.

[37] T. Nomoto, Y. Matsumoto, A new approach to unsupervised text summarization, Proceedings of the 24th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR’01), ACM Press, New Orleans, LA, USA, 2001 (Sep.), pp. 26– 34.

[38] PALM. PALM: Providing Fluid Connectivity in a Wireless World. White Paper of Palm Inc., http://www.palm.com wireless/ProvidingFluidConnectivity.pdf, (2002).

[39] K. Perlin, Quikwriting: continuous stylus-based text entry, Proceedings of the 11th Annual ACM Symposium on User Interface Software and Technology (UIST’98), ACM Press, San Francisco, CA, USA, 1998 (Nov.), pp. 215– 216.

[40] C.J. van Rijsbergen, Information Retrieval, Butterworths, London, 1979.

[41] G. Salton, C. Buckley, Term-weighting approaches in automatic text retrieval, Information Processing and Management 24 (5) (1998 (May)) 513– 523.

[42] Y. Seki, K. Eguchi, N. Kando, Compact Summarization for Mobile Phones, Proceedings of Mobile HCI 2003 International Workshop, Udine, Italy, 2003 (Sep.), In: F. Crestani, M. Dunlop, S. Mizzaro, (Eds.), Mobile and Ubiquitous Information Access, Lecture Notes in Computer Science, 2954, pp. 172–196, Springer, 2004.

[43] S. Teufel, M. Moens, Sentence extraction and rhetorical classification for flexible abstracts, Proceedings of the 1998 AAAI Spring Symposium on Intelligent Text Summarization, AAAI Press, Palo Alto, CA, USA, 1998 (Mar.), pp. 16– 25.

[44] S. Teufel, M. Moens, Sentence extraction as a classification task, Proceedings of the ACL’97/EACL’97 Workshop on Intelligent Scalable Text Summarization, Universidad Nacional de Educacio´n a Distancia (UNED), Madrid, Spain. Morgan Kaufmann Publishers, Madrid, Spain, 1997 (Jul.), pp. 58– 68.

[45] N. Vasconcelos, A. Lippman, Bayesian modeling of video editing and structure: semantic features for video summarization and browsing, Proceedings of 1998 IEEE International Conference on Image Processing (ICIP’98), vol. 3, IEEE Computer Society, Chicago, IL, USA, 1998 (Oct.), pp. 153–157.

[46] N. Vasconcelos, A. Lippman, A spatiotemporal motion model for video summarization, Proceedings of the IEEE Computer Society Conference on computer Vision and Pattern Recognition (CVPR’98), IEEE Computer Society, Santa Barbara, CA, USA, 1998 (Jun.), pp. 361–366.

[47] Yahoo!News, 2003, Yahoo!News homepage, http://news. yahoo.com.

[48] C.C. Yang, F.L. Wang, Fractal summarization: summarization based on fractal theory, Proceedings of the 26th Annual International ACM SIGIR Conference: Research and Development in Information Retrieval (SIGIR 2003), ACM Press, Toronto, Canada, 2003 (Jul.).

[49] C.C. Yang, F.L. Wang, Fractal summarization for mobile devices to access large documents on the web, Proceedings of the Twelfth International Conference on World Wide Web (WWW 2003), ACM Press, Budapest, Hungary, 2003 (May), pp. 215– 224.

[50] C.C. Yang, F.L. Wang, Automatic summarization for financial news delivery on mobile devices, Proceedings of the Twelfth International Conference on World Wide Web (WWW 2003), ACM Press, Budapest, Hungary, 2003 (May), pp. 391–392.

[51] C.C. Yang, F.L. Wang, Document summarization on handheld device: an information visualization tool for mobile commerce, Proceeding of The First Workshop on e-Business (WEB2002) in International Conference on Information Systems (ICIS 2002), Association for Information Systems, Barcelona, Spain, 2002 (Dec.).

[52] YellowBrix, 2003, YellowBrix Homepage, http://www. yellowbrix.com/.

[53] K. Zechner, A. Waibel, DiaSumm: flexible summarization of spontaneous dialogues in unrestricted domains, Proceedings of the 18th International Conference on Computational Linguistics (COLING-2000), Saarbruecken, Germany, Morgan Kaufmann Publishers, Universita¨t des Saarlandes, Saarbru¨cken, Germany, 2000 (Jul.), pp. 968–974.

[54] K. Zechner, A. Waibel, Minimizing word error rate in textual summaries of spoken language, Proceedings of the 1st Conference of the North American Chapter of the Association for computational Linguistics and the 6th Conference on Applied Natural Language Processing (NAACL/ANLP 2000), Association for Computational Linguistics, Seattle, WA, USA, 2000 (Apr.), pp. 186– 193.

Christopher C. Yang is an associate professor in the Department of Systems Engineering and Engineering Management at the Chinese University of Hong Kong. He received his BS, MS, and PhD in Electrical and Computer Engineering from the University of Arizona. Before he joined the Chinese University of Hong Kong, he was an assistant professor in the Department of Computer Science and Information Systems and the associate director of the Authorized Academic Java<sup>SM</sup> Campus<sup>SM</sup> at the University of Hong Kong. He has also been a research scientist in the Artificial Intelligence Laboratory in the Department of Management Information Systems at the University of Arizona. His recent research interests include cross-lingual information retrieval, multimedia information retrieval, digital library, information visualization, Internet searching, automatic summarization, information behavior, and electronic commerce. He has published over 100 refereed journal and conference papers in Journal of the American Society for Information Science and Technology, IEEE Transactions on Image Processing, IEEE Transactions on Robotics and Automation, IEEE Computer, Information Processing and Management, Decision Support Systems, Graphical Models and Image Processing, Optical Engineering, Pattern Recognition, International Journal of Electronic Commerce, Applied Artificial Intelligence, SIGIR, ICIS, WWW, and more. He was the chairman of the Association for Computing Machinery Hong Kong Chapter, the program co-chair of the First International Conference on Asia Digital Library, and a program committee and organizing committee member for several international conferences in digital library, information systems, electronic commerce, computer vision, image processing, and information retrieval. He has frequently served as an invited panelist in the NSF Digital Library Initiative Review Panel and the NSF Information Technology Research Review Panel in US.

Fu Lee Wang is an Instructor in the Department of Computer Science, City University of Hong Kong. He received B.Eng. (Hon) degree in Computer Engineering and M.Phil. degree in Computer Science and Information Systems from the University of Hong Kong, and PhD degree in Systems Engineering and Engineering Management from Chinese University of Hong Kong. His current research interests focus on document summarization, digital library, and information retrieval. His research work has been appeared in such journals as Journal of the American Society for Information Science and Technology, and Information Processing Letters.
