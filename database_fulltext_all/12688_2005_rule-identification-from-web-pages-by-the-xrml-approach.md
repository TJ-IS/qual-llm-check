---
otero_id: 12688
otero_key: "SC44ASXG"
title: "Rule identification from Web pages by the XRML approach"
authors: "Juyoung Kang; Jae Kyu Lee"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.01.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Rule identification from Web pages by the XRML approach

Juyoung Kang <sup>a,T</sup>, Jae Kyu Lee <sup>b</sup>

<sup>a</sup>School of Business Administration, Ajou University, San 5, Wonchon-Dong Yeongtong-Gu, Suwon 443-749, Korea <sup>b</sup>Graduate School of Management, Korea Advanced Institute of Science and Technology, 207-43 Cheongryangri, Seoul 130-012, Korea

Available online 3 March 2005

## Abstract

In the world of Web pages, there are oceans of documents in natural language texts and tables. To extract rules from Web pages and maintain consistency between them, we have developed the framework of XRML (eXtensible Rule Markup Language). XRML allows the identification of rules on Web pages and generates the identified rules automatically. For this purpose, we have designed the Rule Identification Markup Language (RIML), which is similar to the formal Rule Structure Markup Language (RSML), both as parts of XRML. RIML 2.0 is designed to identify rules not only from texts, but also from tables on Web pages, and to transform to the formal rules in RSML syntax automatically. While designing RIML 2.0, we considered the features of sharing variables and values, omitted terms, and synonyms.

We have conducted an experiment to evaluate the potential benefit of the XRML approach with real world Web pages of Amazon.com, BarnesandNoble.com, and Powells.com. We found that 100.0% of the rules and 99.7% of the rule components could be identified and automatically generated if we do not count the statements for linkages, which generically do not exist on the Web pages. Since the linkage components occupy 11.2% of all components in the rule base, the overall limitation of automatic rule generation is 88.8%. In this setting, 88.5% of the overall rule components could be generated from the identified rules from the Web pages. The result provides solid proof that XRML can facilitate the extraction and maintenance of rules from Web pages while building expert systems in the Semantic Web environment

Keywords: Rule identification; Rule acquisition; Knowledge engineering; Knowledge acquisition; XRML; RuleML; XML

## 1. Introduction

Web technology was developed to provide a common browsing platform for human comprehension. As the next step for making the Web intelligent, Semantic Web research [34] attempts to extract data and rules from the Web pages. In order to formally represent the data structure, XML [7,49] is widely adopted as the basic platform. Moreover, to formally represent the rules, rule markup language research is widely undertaken [42]. The primary focus of rule markup language research is to represent rules with appropriate tags, imposing logical inference capability over the markup rules.

## 1.1. Framework of XRML

A critical issue in adopting rule markup language is the acquisition and maintenance of formal rules from Web pages where the rules are expressed in natural language texts and tables. Concerning rule acquisition, Hulth et al. [19] pointed out that direct conversion of natural language text to formal representation is extremely complex, so the intervention of a knowledge engineer is unavoidable [44]. To handle this issue, we propose the eXtensible Rule Markup Language (XRML) approach as a framework of extracting rules from texts and tables. XRML consists of three components as depicted in Fig. 1: Rule Identification Markup Language (RIML), Rule Structure Markup Language (RSML), and Rule Triggering Markup Language (RTML) [27]. RIML identifies the rules implicitly expressed in Web pages; RSML represents the formal rule structure that corresponds to the rule syntax in commercial rule-based systems; and RTML defines the conditions that trigger the inference of certain rules.

In the traditional rule-based system, rules are extracted from their sources without tracing the formal association between them. However, in the XRML environment, we can identify the rules on the Web pages first using RIML, and then transform them to the RSML form.

The procedure of the XRML approach is depicted in Fig. 1 with the step numbers in parentheses. These steps are defined here

(1) Select relevant Web pages: A knowledge engineer, who is responsible for building and maintaining rule bases, plans the kind of rule base that is necessary and selects the relevant Web pages.

(2) Identify rules: S/he identifies the rules from the browsed Web pages which display the text, tables, and pictures. Then the knowledge editor (named XRML Editor here) generates HTML/ RIML files where the RIML statements are embedded in the HTML files.

(3) Automatic transformation: The identified rules in HTML/RIML can be automatically transformed to the rule syntax in RSML. The set of identified rules derived in this manner may not be complete, so these are called draft rules.

(4) Interactive refinement: The draft rules may need refinement to make them complete. This interactive refinement will be much easier than making the rules from scratch.

(5) Local inference: The complete RSML rule set may be used for its own local inference.

![](/api/attachments/SC44ASXG/fulltext/images/2060b80f552a25050af2679430b6f7f5c1de389a46c10b588418b5f2627d371b.jpg)  
Fig. 1. Rule acquisition process by the XRML approach.

(6) Merge: The RSML rules may be transformed to the syntax of a commercial rule-based system, and merged to the corporate rule base.

(7) Inference: The rule base can be used to make an inference for human.

(8) Trigger with RTML: An inference against the rule base may be triggered by the software agents according to the specified triggering condition.

(9) Maintenance with consistency: If any change happens on the Web pages or rule bases that are generated by the XRML framework, we can detect their counterparts effectively and efficiently. Thus, maintaining consistency between them can be easily implemented.

The knowledge acquisition tools developed so far mostly assist the drawing of rule structures. There has been little attention paid to marking the rules on the original Web pages and maintaining consistency between the generated rules and original texts. For simple and disposable rule-based systems, the RIML approach may not be essential. However, for the largescale institutional rule-based systems which have to be developed by multiple experts and maintained for a long period of time, the RIML approach is essential for consistent maintenance of Web pages and formal rules.

The XRML approach will be useful whenever the rule-based system is necessary based on the knowledge on the Web pages; thus XRML can be applied to a broad spectrum of rule-based systems on the Web. The current applications developed using XRML include automated form processing in workflow environments [25], auditing user agreements in Internet shopping malls [54], and inter-organizational knowledge exchange and integration among heterogeneous organizations [22].

## 1.2. Research objectives and organization of paper

The first stage of XRML 1.0 research has naturally focused on the design of tags that annotate the existence of rules, variables, and values in the texts. In this paper, as the second step of this research, XRML 2.0 investigates the integrated extraction of rules both from natural language texts and tables. For instance, to compute the delivery cost of items purchased from online shops like Amazon.com, customers need to look at both the relevant texts and tables together to derive a conclusion. In this process, we experience situations where some terms are not explicitly stated (thus omitted because readers can implicitly understand without the terms); some terms used as variables are shared by many other terms whose role is values; and some terms are expressed by other synonyms or pronouns.

So the first objective of this research is the design of XRML 2.0 (which consists of RIML 2.0 and RSML 2.0; see Sections 3.1 and 3.2) considering the above features (see Section 4). We excluded the description on RTML 2.0 here because it is not directly related with the scope of this paper.

The second objective of this research is whether XRML 2.0 can perform well with the real world Web pages. So we have applied the XRML framework to three real world Web pages from typical online bookstores (Amazon.com, BarnesandNoble.com, and Powells.com) with 36 Web pages in total. The rule identification and generation process is demonstrated with Amazon.com (see Section 3.3).

While we identify the rules from the Web pages, we noticed that we could not identify all the rules if the pages did not have all the knowledge necessary for the rule base. For instance, the linkages between rules and inferential conclusions are not explicitly expressed in the Web pages. Sometimes, identification on the Web pages is not efficient because the complex numeric expressions and logical relationship are not easily expressed in markup language. In these cases, it is desirable to postpone such difficult identifications to the rule refinement stage with RSML. Thus, analyzing the postponement strategy is the third objective of this research (see Section 5).

The fourth objective of this research is the evaluation of the effectiveness and efficiency of the XRML approach. For this purpose, we need to define the measures for effectiveness and efficiency and conduct an experiment. The measures are defined in Section 6, and the experiment is conducted with 36 Web pages of three online bookstores (see Section 6).

Since rule identification is similar to rule extraction from the natural language, we have reviewed the relevant literature on knowledge acquisition, natural language processing, and machine learning, and discussed their relationship with XRML. We have also contrasted XRML with the other rule markup languages (see Section 2).

There are other important issues such as assisting the identification of RIML and refinement of RSML.

The limitations will be discussed in Section 6.6, and the future research agenda is discussed in Concluding Summary and Discussion.

## 2. Review on rule markup languages and knowledge acquisition

To understand the role of XRML, we review the literature on rule markup languages and knowledge acquisition, and contrast them with the distinctive goals of XRML.

## 2.1. Rule markup languages

Recently, there have been many studies on rule markup languages. The RuleML Iinitiative [42] organized the online resources about rule markup languages. Typical languages include XRML [26] and RuleML version 0.7 [5]. The primary purpose of rule markup languages is to express the logical rules with the annotating tags of meta-knowledge, thereby expanding the rules’ expressive power. Most rule markup languages are designed to be compatible with ontology languages like RDF(S) [8,24], DAML+OIL [11,17], and OWL [18,46] because they are also based on XML.

The Rule Markup Language Workshop was held at the International Semantic Web Conference in Florida in 2003, and it explored the standard representation of rules and the extension of rules to various representations. Typical markup standards and initiatives include:

<sup>!</sup> RSML [26], which is the XML-based rule structuring language as a part of XRML. A unique feature of RSML is its association with RIML embedded in HTML files.

<sup>!</sup> DARPA Agent Markup Language (DAML)- RULES [14], which permits the representation of Horn rules [28]. The current DAML+OIL [17] does not include a specification of explicit inference rules yet.

<sup>!</sup> Predictive Model Markup Language, which is an XML-based language that can define various models in data mining such as association rules [15].

<sup>!</sup> Attribute Grammars’ semantic rules [39], which suggest various XML markups that are similar to Horn rule markup [28].

<sup>!</sup> Extensible Stylesheet Language Transformation (XSLT) [10], which is a restricted term-rewriting system of rules written in XML.

<sup>!</sup> Mathematical Markup Language [9], which focuses on defining functions rather than rules.

Recently, the RuleML has attempted to integrate all necessary features into a standard platform. However, it still does not cover the issue of extracting the markup rules from the Web pages, as the XRML approach attempts. Thus the key distinction of XRML with other rule markup languages is that XRML supports the rule identification stage on the Web pages to assist rule generation from the natural Web pages. This framework is also useful to assure the consistency between Web pages and rules during the maintenance stage because XRML can pinpoint the position of a counterpart when one side of Web pages or rules is changed.

## 2.2. Knowledge acquisition

The process of extracting rules from Web pages resembles the knowledge acquisition process from natural languages. So we need to review the literature on Expert’s Diagram, rule verification, natural language processing, and machine learning. Then we can describe the relationship of the XRML approach with them more clearly.

## 2.2.1. Expert’s Diagram approach

Knowledge acquisition has been an everlasting bottleneck in building expert systems. To help domain experts such as lawyers in structuring domain knowledge, the Expert’s Diagram [27], which can be used by experts without the aid of knowledge engineers, is widely utilized. The conceptual graph [2,38,48,52], decision table [38,45], and influence diagram [6,21,33] belong to this category. These diagrams aim at assisting experts to explicitly represent knowledge without making logical mistakes by visually confirming the reasoning process. The diagram can be an intermediary representation that assists the communication between knowledge engineers and experts who understand the knowledge in text form.

So the knowledge engineer may mark rules on the Web pages using RIML while constructing diagrams of the eventual rules that should be extracted from the Web pages. The Expert’s Diagram can be transformed to rules automatically, so it is efficacious to associate the diagram with the rules, but not the original text and the rules. Once a diagram is precisely drawn, the diagram may be complementarily used to assist the rule identification on the Web pages.

## 2.2.2. Rule verification and circumscription

The popular schemes of rule verification are to check whether there is missing link, syntactic error, redundancy, inconsistency, and subsumption [25,29,37]. By transforming the rules into an AND/ OR graph, the rule structure can be verified as to whether such defects exist. The verification techniques can be applied to the draft rules in RSML form because the identified rules may not be complete.

In the XRML environment, the Web pages may be changed after the initial establishment, and the rules from the Web may have to merge with the existing rules, which may be generated from other sources. So interaction of new rules with existing rules is very important, and needs verification between them.

It is very difficult to detect semantic incompleteness automatically. However, if an ontology exists, which can detect the hierarchical relationship between objects of variables and the circumscription of their value set, the existing rules can be specialized or generalized by adding rules [32].

For instance, Amazon.com deals with seven categories of items such as electronics. Electronics has eight sub-categories such as computers and audio and video. So we can confirm the circumscription if the all categories are listed. Suppose there is an overall shipping policy for electronics, but the marketing manager would like to apply a special promotion policy to computers. In this case, the rules for the electronics level should be specialized to the audio and video level after having added the new rule about computers. This is an example of specialization during the refinement stage, which is one of followup research topics in the XRML project.

## 2.2.3. Natural language processing for ontology extraction

Achieving perfect natural language processing is difficult because the natural language texts may imply more than one valid interpretation as Wetter and Nuˆse pointed out [53]. Using the natural language processing capability to acquire rules from the Web is also very difficult because Web sites can handle many diverse domains. Recently, ontology has become popular for specifying the knowledge of a particular domain on the Web [16,43,50]. For certain domains, ontology may help in selecting the right interpretation of vocabulary [13,19,51]. On the other hand, the natural language processing may be used to automatically extract terms to add to the ontology using grammar analysis [4,30,40], linguistic patterns [41,44] such as regulatory sentences [35,36], and predefined templates [48,55]. However, the quality of automatically extracted knowledge from natural language sources is not accurate enough yet, so the draft should be manually refined by knowledge engineers [44,53].

The primary idea of the XRML approach is to assist the knowledge engineer’s rule extraction process by assuming that natural language processing is not reliable enough. However, some text analysis technologies can be adopted in designing the XRML Editor so that the knowledge engineer can search for terms from the text and retrieve their synonyms while identifying rules on the Web pages and editing rules in the rule base.

## 2.2.4. Machine learning and Web mining

Machine learning techniques such as inductive learning, neural networks, and statistical models may be applied under the umbrella term of data mining— specifically Web mining when the log data are collected from Web pages [20,23]. If a structured data set is available, we can induce them to more generalized and abstract knowledge. Several methods and tools [1,3,12,47] have been developed using this approach. However, since extracting rules from the natural texts and tables usually aims to acquire the knowledge at the same level of abstraction, inductive learning [3,12,47] is not the primary issue in extracting rules from Web pages.

## 2.2.5. Research objective revisited

The current rule markup languages do not have any facility to extract the rules from the Web pages and to signal the inconsistency between the originating Web pages and rules. XRML attempts to overcome such limitations by adopting the rule identification procedure and its automatic transformation to formal rules. In this sense, XRML can be regarded as a framework of the Web and Rule Management System in the context of the Semantic Web.

Although all of the earlier knowledge acquisition, refinement, and verification techniques and tools can be merged with XRML tools, we will not repeat these issues in this paper. Instead, we focus on describing the four research objectives described in Section 1.2 one by one in the following sections.

## 3. The eXtensible Rule Markup Language approach

This section describes the representation of rule identification and process of rule extraction from Web pages using XRML. The entire process is demonstrated in Figs. 2–6 in Section 3.3 with an example of the shipping and return policy of Amazon.com.

## 3.1. Representation of Rule Identification Markup Language

To fulfill the goal of RIML 2.0 described earlier, let us formally define its syntax. Earlier versions of RIML 1.0 covered the simple statements of Rule-

Group, Rule, variable, and value. These statements are marked up within the paired <sup>dbNT</sup> symbols like the XML statements. For instance, according to the illustration described in Section 3.3 with the Amazon. com site, a variable items is identified as<sup>b</sup>variable<sup>N</sup> items<sup>b</sup>/variable<sup>N</sup>. Let us suppose the sentence in Fig. 3 <sup>b</sup>We are currently able to ship books, CDs, VHS videos, music cassettes, and vinyl records to Asia and Pacific Islands addresses,<sup>Q</sup> whose corresponding statement is coded in HTML in Fig. 4. The knowledge engineer recognizes that the terms books and CDs are the values of items. Then s/he marks them as values such as <sup>b</sup>We are currently able to ship<sup>b</sup>value<sup>N</sup>books <sup>b</sup>/value<sup>N</sup>,<sup>b</sup>value<sup>N</sup>CDs<sup>b</sup>/value<sup>N</sup>,. . .<sup>Q</sup>. This statement corresponds to the identified Rule 1 in the HTML/ RIML, which has embedded RIML statements in HTML (see Fig. 5). The RIML may be simply eliminated to browse the original document on the Web. The HTML/RIML statements can also generate rule statements (Rule 1) in RSML syntax as demonstrated in Fig. 6. The comprehensive explanation is illustrated in Section 3.3.

<table><tr><td>BookStore</td><td>Book Info</td><td>Shipping Info</td><td>Total Cost</td></tr><tr><td>Amazon</td><td>Enterprise Knowledge Management: The Data Quality Approach, $ 49.95, Qty: 1The Complete E-Commerce Book: Design, Build &amp; Maintain a Successful Web-based Business, $ 20.97, Qty: 1The Lovely Bones: A Novel, $ 13.17, Qty: 1What Should I Do With My Life, $ 14.97, Qty: 1XML in a Nutshell, 2nd Edition, $ 27.97, Qty: 1Total Book Price: $ 127.03</td><td>Shipping Method: Priority International CourierTrackable And Insured: YesTime: 2 to 4 Business DaysPerShipment: $ 29.99PerItem: $ 8.99Shipping Cost: $ 74.94</td><td>$ 201.97</td></tr><tr><td>BarnesandNoble</td><td>Enterprise Knowledge Management: The Data Quality Approach, $ 39.96, Qty: 1The Complete E-Commerce Book: Design, Build &amp; Maintain a Successful Web-based Business, $ 23.96, Qty: 1The Lovely Bones: A Novel, $ 13.17, Qty: 1What Should I Do With My Life, $ 14.97, Qty: 1XML in a Nutshell, 2nd Edition, $ 31.96, Qty: 1Total Book Price: $ 124.02</td><td>Shipping Method: International ExpressTrackable And Insured: YesTime: 1 to 5 business daysPerShipment: $ 30PerItem: $ 5.95Shipping Cost: $ 59.75</td><td>$ 183.77</td></tr><tr><td>Powells</td><td>Enterprise Knowledge Management: The Data Quality Approach, $ 32.5, Qty: 1The Complete E-Commerce Book: Design, Build &amp; Maintain a Successful Web-based Business, $ 21, Qty: 1The Lovely Bones: A Novel, $ 14.98, Qty: 1What Should I Do With My Life, $ 24.95, Qty: 1XML in a Nutshell, 2nd Edition, $ 27, Qty: 1Total Book Price: $ 120.43</td><td>Shipping Method: International ExpressTrackable And Insured: YesTime: 2-7 business daysPerShipment: $ 35PerItem: $ 8Shipping Cost: $ 75</td><td>$ 195.43</td></tr></table>

Fig. 2. An illustrative expert system that compares book prices including specific delivery cost.

![](/api/attachments/SC44ASXG/fulltext/images/338cf536074f061464257bfc0d422a76b158fe3eb9611f7d5f3b696e53e921db.jpg)  
Fig. 3. A Web page on shipping rates at Amazon.com.

In the current version of RIML 2.0, we extend the statements by adding the primitive statements RuleTable, IF, THEN, connectives (such as AND, OR, and NOT), and comparison operators (such as GT, GE, LT, and LE). Rules derived from the tables can be integrated with the rules from texts to conduct integrated reasoning.

The statements for RIML 2.0 that we have developed are formally specified in Document Type Definition (DTD) syntax in Appendix A. We intend to use the same tags in RIML and RSML as much as possible to make the symbols mutually comprehensible. However, one unavoidable difference is the addresses of the counterpart resources. RIML has to identify the associated rule base and rules; while RSML, the associated Web pages. Although RSML has a complete tag set for rule specification, RIML may use only the tags that are useful to identify rules on the context of Web pages. Identifying overly sophisticated numeric functions will be neither easy to express with tags, nor effective to specify completely. It will be better to postpone such specifications to the rule refinement stage in RSML as described in Section 5.

![](/api/attachments/SC44ASXG/fulltext/images/e2847af036fe22066c1ce30ea9fb4f1cd8bcd59a2f38a05b055adbb2d2b852b0.jpg)  
Fig. 4. An illustrative HTML file of the Web page in Fig. 3.

3.2. Process of rule extraction from Web pages by XRML

As mentioned earlier, the XRML approach aims at identifying rules using RIML on the screen of the Web pages and transforming the identified rules to the draft rules in RSML syntax as depicted in Fig. 1. The process of rule extraction using XRML is composed of the following steps. The steps in Fig. 1 are noted in parentheses.

I. Plan the rule base and select Web pages.

– Determine the goals and topics of the rule base, and compose the rule groups and rules.

Select the Web pages that are relevant to the rule base (Step 1).

II. Identify rules using RIML.

Identify the RuleGroups, Rules, variables, values, IF–THEN relationships, and connectives such as AND and OR on the Web pages (Step 2).

Build the HTML/RIML file, which has the RIML statements embedded in HTML statements.

III. Transform the HTML/RIML statements to the draft rules in RSML syntax (Step 3).

The identified rules on the Web pages can be automatically transformed to rules in

![](/api/attachments/SC44ASXG/fulltext/images/e99f4eba2870682b056e3ed04b919726ab8c5bf108cde0b1abb93d052f71c69f.jpg)  
Fig. 5. An illustrative HTML/RIML file with RIML added to HTML in Fig. 4.

RSML syntax, but the generated draft rules may be incomplete.

IV. Refine the RSML draft rules and add new rules to build a complete rule set (Step 4).

The rule components not specified in the identification step need to be refined at this stage to make the rules complete.

Additional rules are necessary to link the generated rules with the inferential conclusions.

The complete RSML rule set generated in this manner may be further transformed to the syntax of target commercial rule-based systems if necessary. The remaining steps (5)–(8) are not described here because they are beyond the scope of this paper. The knowledge engineer is involved in the three steps of the rule acquisition process: Plan the Rule base, Identify the Rules, and Refine the Rules. These interactive steps should be assisted by the XRML

![](/api/attachments/SC44ASXG/fulltext/images/430d52c63e06ab13d370bad8f02545c166cf04b96a5bf559dc624621c2235483.jpg)  
Fig. 6. An illustrative draft rules file generated in RSML syntax from Fig. 5.

Editor, while the transformation step will be automatically executed.

## 3.3. An example on shipping and return policy

Let us demonstrate the rule extraction process from an example Web page in Amazon.com. This example attempts to build a rule-based expert system on shipping and return policy, which can be merged to the Price Comparison Site that considers not only the price of items, but also the delivery cost. We have built a prototype of a comparison site ConsiderD as demonstrated in Fig. 2. The example compares three sites in terms of the total book price of five books and their shipping cost to Seoul by Priority International Courier. Note the lowest book price does not mean the lowest total cost.

## 3.3.1. Plan the rule base and select Web pages

Suppose Amazon.com has decided to build an expert system which can consult the complex shipping and return policy. On behalf of the knowledge engineer, we have searched through the Web pages relevant to the subject, and selected 21 pages. The selected pages explain the places to where shipping is provided, shipping rates, free shipping conditions, delivery time, the number of days within which a full refund is permitted, and conditions in which a return is not allowed. The rules could be grouped into four categories: Shipping Rates, Modifying Orders, Shipping Guide, and Returns and Refunds. It will be helpful for the knowledge engineer to get familiar with the rules described in the texts and tables possibly with the aid of knowledge acquisition diagrams.

## 3.3.2. Identify rules using RIML

The next step is to identify the existence of rules in the selected pages. We have identified 4 RuleGroups, 120 Rules, 35 RuleTables, 313 variables, 808 values, 13 operators, 119 IF statements, 120 THEN statements, and 107 connectives. In total, we have identified 1635 rule components.

For instance, suppose we have picked the page as shown in Fig. 3 that explains the rules on the shipping rate of books to Seoul, Korea. The HTML file of the Web page is shown in Fig. 4. Note that the page has text, numeric functions, and three tables on Standard International Shipping, Expedited International Shipping, and Priority International Shipping. We can see that the shipping rate depends upon shipping region, items purchased, number of items, and priority type.

On this page, we need to identify the existence of RuleGroup, Rules, variables, values, and IF–THEN relationships, and connectives like AND and OR. Note that the screen editing should be supported by the XRML Editor although the example is explained with an HTML file. The rules from the tables also need to be identified as RuleTable. The embedded RIML tags are written in italic style in Fig. 5. In this example, the RuleGroup is identified with its title=Shipping Rates. The first rule is identified as <sup>b</sup>Rule rid=1<sup>N</sup> with its THEN part in which the first variable, <sup>b</sup>variable vid=1<sup>N</sup>able to ship<sup>b</sup>/variable<sup>N</sup>, and its omitted value, True, are identified. The knowledge engineer intentionally added the value True.

## 3.3.3. Transform the HTML/RIML statements to the draft rules in RSML syntax

The HTML files with embedded RIML statements can be used for two purposes. One is for display to humans in the HTML file format via the regular browser by eliminating the RIML statements. The other is to transform the HTML/RIML statements to the draft rules in RSML syntax. The RIML statements in Fig. 5 can be transformed to the draft rules in Fig. 6.

In this manner, we have generated 2520 rule components as summarized in Table 1. According to the columns IC (Number of Identified Rule Components in the RIML stage) and GC (Number of All Generated Rule Components in the RSML Stage), the numbers of identified Rules, RuleTables, IF, THEN, and operator components in RIML are the same as those in RSML. However, the numbers of variable and value are increased by 614 (66.2%) and 119 (12.8%), respectively, owing to the shared components. There are also 148 (57.1%) AND statements automatically generated as a default connective.

## 3.3.4. Refine the RSML draft rules to build a complete rule set

Based on the draft rules demonstrated in Fig. 6, we need to refine the rules to make them syntactically and semantically complete. This is an interactive refinement process to the knowledge engineer with the assistance of rule editor. The rule editor may highlight the position that has syntactic error such as ’Missed IF Statement<sup>T</sup> or <sup>d</sup>Missed Rule Statement.<sup>T</sup> In the draft rules in the column GC of Table 1, some generated rules may not be complete, while some rules are not identified at all. The column rC of Table 1 shows the number of rule components added to make the identified rules complete. Three numeric operators and five connectives (AND or OR) are added at the RSML stage to refine the identified rules.

The knowledge engineer also needs to add the statements or rules to link with conclusions or other rules. For instance, in Rules 2 and 3 in Fig. 6, we need the statement <sup>b</sup>Set\_Shipping\_Rates<sup>N</sup>Computed<sup>b</sup>/ Set\_Shipping\_Rates<sup>N</sup> in the THEN part of the rules. Thus, we added 206 rule components to link with the inferential conclusions, which amounts to 7.5% of all the rule components as shown in the column lC of

<table><tr><td>Rule component</td><td>Identified at RIML stage (IC)</td><td>Automatically generated from shared components (sC)</td><td>Automatically generated from default operators (dC)</td><td>All generated from RIML statements (GC=IC+sC+dC)</td><td>Interactively added for rule refinement (rC)</td><td>After refinement (RC=GC+rC)</td><td>Effectiveness (%)=[GC/RC]×100 (%)</td><td>Added to provide linkages (IC)</td><td>Total in complete rules (TC=RC+IC)</td><td>Linkage effort (%)=[IC/TC]×100 (%)</td><td>Overall effectiveness (%)=[GC/TC]×100 (%)</td></tr><tr><td>RuleTable</td><td>35</td><td>0</td><td>0</td><td>35</td><td>0</td><td>35</td><td>100.0</td><td>0</td><td>35</td><td>0.0</td><td>100.0</td></tr><tr><td>Rule</td><td>120</td><td>0</td><td>0</td><td>120</td><td>0</td><td>120</td><td>100.0</td><td>4</td><td>124</td><td>3.2</td><td>96.8</td></tr><tr><td>Variable</td><td>313</td><td>614</td><td>0</td><td>927</td><td>0</td><td>927</td><td>100.0</td><td>94</td><td>1021</td><td>9.2</td><td>90.8</td></tr><tr><td>Value</td><td>808</td><td>119</td><td>0</td><td>927</td><td>0</td><td>927</td><td>100.0</td><td>94</td><td>1021</td><td>9.2</td><td>90.8</td></tr><tr><td>Operator</td><td>13</td><td>0</td><td>0</td><td>13</td><td>3</td><td>16</td><td>81.3</td><td>1</td><td>17</td><td>5.9</td><td>76.5</td></tr><tr><td>IF</td><td>119</td><td>0</td><td>0</td><td>119</td><td>0</td><td>119</td><td>100.0</td><td>5</td><td>124</td><td>4.0</td><td>96.0</td></tr><tr><td>THEN</td><td>120</td><td>0</td><td>0</td><td>120</td><td>0</td><td>120</td><td>100.0</td><td>4</td><td>124</td><td>3.2</td><td>96.8</td></tr><tr><td>Connectives</td><td>107</td><td>4</td><td>148</td><td>259</td><td>5</td><td>264</td><td>98.1</td><td>4</td><td>268</td><td>1.5</td><td>96.6</td></tr><tr><td>Total</td><td>1635</td><td>737</td><td>148</td><td>2520</td><td>8</td><td>2528</td><td>99.7</td><td>206</td><td>2734</td><td>7.5</td><td>92.2</td></tr></table>

Table 1. Since the linkage knowledge with the inferential conclusions does not exist in the Web pages, the generic limitation of rule generation is 92.5%. In this example, we can see that 92.2% of the rule components are identified in practice from the Web pages during the identification stage.

## 4. Issues in rule identification

There are four additional issues in rule identification with XRML 2.0: rule extraction from tables, and handling of omitted components, shared components, and synonyms.

## 4.1. Extracting rules from tables

The earlier study of RIML started with identifying the rules from the natural language texts on the Web pages. However, many rules are effectively represented in tables on the Web pages as is the case in Fig. 3, which describes the shipping rate. So we need to have a common rule representation that can integrate the rules from both texts and tables. For this purpose, we need to specify the tag <sup>b</sup>RuleTable<sup>N</sup>.

The contents in the table correspond to the value of the rules’ THEN parts with their column head titles as variable names. The record names in the rows correspond to the values of condition statements with their head titles as their variables. When multiple tables exist in the same format, the table title statement should be added in the conditional statement. If the value statements around the tables have different levels of detail (such as country name Korea and region name Asia and Pacific), we need an additional statement that links them. In the example in Fig. 7, customers need to identify the region where a country belongs because the table is defined by region. So we need to refer to the texts below the table that defines the region. This requires adding a rule (the Rule id=4 in Fig. 6) from the texts <sup>b</sup>Countries and Territories Included in the Asia and Pacific Islands Shipping Region. . .<sup>Q</sup> described at the bottom of Fig. 3.

In the experiment described in Section 6, we found that all rules from tables need some statements from the texts as well. In Section 3, an example table is shown in Fig. 3, whose HTML file is specified in Fig.

![](/api/attachments/SC44ASXG/fulltext/images/7f426bf779b4f7369321565f65a8ab00de64c4142e204753e4769de5cb8456da.jpg)  
Fig. 7. Example of shared components in Web page.

4. The RuleTable is identified in Fig. 5 generating Rules 2 and 3 in Fig. 6.

The XRML Editor needs to support the highlighting of table, columns, rows, and relevant texts to identify the rules from the tables. Even though the identified rules will be internally specified in the HTML statements, the XRML Editor should support a user-friendly GUI dialogue for identification.

## 4.2. Omitted terms

Some terms used in the rules may not be explicitly expressed in the Web pages. The terms might have been omitted because readers of the natural language texts and tables will be able to understand them without explicit vocabularies. Let us call such terms Omitted Terms. The vocabulary level omission here does not imply the frame problem, which points out that not all implicit preconditions and actions easily understood by humans can be specified in formal rules [31]. It is desirable to explicitly identify the omitted terms with their standard terms in RIML so as to associate them without ambiguity. Particularly when an omitted term is shared by other terms, it is beneficial to specify them in RIML to generate the multiple variable-value pairs of RSML automatically.

In the table in Fig. 7, the variable names of the values <sup>b</sup>Priority International Courier<sup>Q</sup> and <sup>b</sup>2 to 4 business days<sup>Q</sup>—Delivery Method and Delivery Time—are omitted, respectively. In Section 6.5, we observe that 25.3% of terms are omitted in practice.

## 4.3. Shared components

Some rule components may be defined once and shared multiple times by other components. For instance, a variable may be shared by multiple values, and a statement may be repeated in multiple rules. In the table, the same column title will be repetitively used as a variable with multiple values in the column. So the variable will be shared by multiple values. Variables are frequently shared by multiple values in the context of tables. However, it can also happen in the natural texts as well.

For instance in Fig. 7, Per Shipment in the head of a table is written once, but its values are listed twice depending upon the item types. Another sharing example exists outside of the table. The value Priority International Courier along with its omitted variable name Delivery Method will be repeated in the IF statement of all rules generated from the table. The variable name Country will also be shared by all listed countries.

The identification of shared variables in the Web pages is very useful because it can reduce the effort of rule coding. We simply do not have to repeat the coding of the same variables and values. Instead, we need to provide the serial identifier so that the corresponding variables and values can be recognized. For this purpose, we have designed the XRML Editor to generate the serial number of variables and values to mutually combine them (see an example in Fig. 5). The omitted variable items in line 11 has its id number vid=2 as expressed <sup>b</sup>variable vid=2 name=<sup>b</sup>items<sup>Q</sup>/<sup>N</sup>. The books and CDs are the values of items as expressed <sup>b</sup>value vid=2<sup>N</sup>books<sup>b</sup>/value<sup>N</sup> and <sup>b</sup>value vid=2<sup>N</sup>CDs<sup>b</sup>/value<sup>N</sup>. In this manner, the values books and CDs can share the variable items. The generated identifier may be purposefully changed to a semantic name when it is not easy to remember the id number.

This sharing can improve the degree of automatic rule structuring, and reduce the effort of rule maintenance in the RSML stage because the variable may be identified once, and revised once when the change is necessary. So the degree of automatic rule generation from the shared variables is an important ingredient in measuring the efficiency of using RIML. In Section 6.2, we found that 16.8% of the rules are generated from the shared variables.

## 4.4. Synonyms

Some terms may be phrased in different synonyms. To handle the synonyms, we need to build a thesaurus which pops up whenever the synonyms exist. To reduce the annoying pop ups in wrong contexts, the identification of synonyms may be triggered only upon request. The synonyms may also have a representative term, namely a standard term.

In the earlier example, the terms item and items may be regarded as synonyms. In the Barnes and Noble site, the term Standard Surface Mail is used in the heading of a table, which is simply expressed as International Surface in the table. In this example, the term Standard Surface Mail may be regarded as a standard term. The standard term is useful particularly when we add tags for omitted terms. If the application system already has an ontology, the ontology facility may support the synonyms. Synonyms need to be managed both at an individual site and domain level. According to the experiment presented in Section 6.5, 14% of terms in the rules are expressed in synonyms.

## 5. Postponement strategy in rule identification

The benefit of identifying the rules in the RIML stage is that it is easier to generate the rules from Web pages and to maintain consistency between the Web pages and the rule base. So it is desirable to identify the rules on the Web as many as possible. Although most rules on the Web can be effectively identified, some statements are not easy to identify in the context of Web pages. For such cases, it is recommendable to postpone the identification to the refinement stage with RSML.

For a given situation, the knowledge engineer should balance the effort among rule identification, rule refinement, and rule maintenance so as to minimize the total effort.

Typical situations recommended to postpone identification are:

(1) The Linkages between the Rules and Conclusion are Missing.

(2) Numeric and Logical Expressions are too Complex.

(3) Pages containing a Rule are too Scattered.

(4) External Sources of Statements are Additionally Necessary.

## 5.1. Linkages between rules and conclusion

Every rule-based inference needs conclusion rules, which stop the inference. The conclusion rules should be intentionally defined by the knowledge engineer who decides the purpose of expert systems. Therefore the conclusion rules and their linkages with intermediate rules usually do not exist in the Web pages. Thus, it is better to postpone adding such linkages to the RSML stage because the rule editor for refinement can assist the detection of missing linkages between rules.

For example, in Rules 2 and 3 in Fig. 6, we need the statement <sup>b</sup>Set<sup>\_</sup>Shipping<sup>\_</sup>Rates<sup>N</sup>Computed <sup>b</sup>/Set<sup>\_</sup>Shipping<sup>\_</sup>Rates<sup>N</sup> in the THEN part of the rule, respectively, to link each rule with the conclusion rule. In the Amazon case, four new rules are added for such linkages.

## 5.2. Complex numeric and logical expressions

When the numeric functions and logical expressions are very complex, it is recommendable to identify only the key arguments postponing the full specifications to the rule refinement stage. Adding complex operators with the identified arguments will be easier to edit. In Fig. 3, there is an equation that calculates the total shipping cost, which is not easy to express with the markup tags.

## 5.3. Scattered pages for a rule

Frequently, Web pages do not explain a set of rules in appropriate order. When the statements for a rule are scattered in multiple pages, it may not be easy to link the associating identifiers. Multiple windows, possibly with double monitors, may help alleviating this problem to some extent. When the association of all relevant components for a rule is not easy, we may intentionally postpone the full identification. In this case, the knowledge engineer needs to put a warning flag in the rule with a description about its incompleteness so that s/he can be alerted in the RSML stage.

## 5.4. External sources of statements

Some rules may require extra statements that do not exist in the Web pages. Some rules may not be allowed to publish on the Web. In this case, the knowledge engineer may also put up a flag on the missing statements along with their source if s/he knows it. This will be an effective helper to make the rule complete during the refinement stage. In the rule refinement stage, the rules in RSML need to be transformed to the AND/OR graphic relationships so that the missed linkages and dead locks can be detected automatically [27,29,37].

## 6. Performance of using RIML

## 6.1. Experiment design for evaluation

This section evaluates the effect of rule identification using RIML. For this evaluation, we selected three well known online book selling Web sites: Amazon.com, BarnesandNoble.com (in short BN), and Powells.com. From these sites, we analyzed the 36 relevant pages on the shipping and return policy, and identified the rules to discover the full potential of the rule identification from the Web pages. The rules generated from these sites were used to build a comparison site, which compares book prices including the delivery cost for particular orders as was demonstrated in Fig. 2.

Our concerns in the evaluation of performance here include the following:

1. What is the proportion of rule components that can be potentially identified during the rule identification stage?

2. What is the composition of rules generated from texts and tables respectively?

3. What is the effect of shared components in rule generation?

4. What proportion of variables and values that are omitted in the natural language texts and tables should be explicitly specified during the rule identification stage?

5. How many synonyms are used in the Web pages?

The intention of this experiment is to explore the potential benefit of using the XRML approach. At this stage, we do not intend to test the practical performance of using the XRML tools, whose result will depend upon the intelligence of the XRML Editor, the type of applications, and the proficiency of the knowledge engineer in terms of the XRML approach and domain. The evaluation of practical performance needs follow-up experiments.

To measure the effectiveness of rule identification, we define the metrics at the rule or rule component level as follows.

IR: Number of rules identified at the RIML stage nR: Number of new rules added at the RSML stage TR: Total number of rules necessary to build a complete rule-based system.

At the rule level, the identified rules do not necessarily mean complete ones. The Effectiveness of Rule Identification can be defined in Eq. (1) as illustrated in Table 2.

Effectiveness of Rule Identification %ð Þ

$$
= [ \mathrm{IR} / \mathrm{TR} ] \times 1 0 0\tag{1}
$$

Table 2  
Performance of identifying rules on the Web pages

<table><tr><td rowspan="2">Book store</td><td rowspan="2">Number of Web pages</td><td rowspan="2">Number of rule groups</td><td rowspan="2">Number of tables</td><td colspan="3">Number of identified rules</td><td rowspan="2">Number of new rules for linkage (nR)</td><td rowspan="2">Number of total rules (TR)</td><td rowspan="2">Percentage of IR/TR (%)</td></tr><tr><td>From tables</td><td>From texts</td><td>Total (IR)</td></tr><tr><td>Amazon</td><td>21</td><td>4</td><td>35</td><td>79</td><td>41</td><td>120</td><td>4</td><td>124</td><td>96.8</td></tr><tr><td>BN</td><td>8</td><td>4</td><td>7</td><td>54</td><td>43</td><td>97</td><td>4</td><td>101</td><td>96.0</td></tr><tr><td>Powells</td><td>7</td><td>4</td><td>3</td><td>242</td><td>13</td><td>255</td><td>3</td><td>258</td><td>98.8</td></tr><tr><td>Total</td><td>36</td><td>12</td><td>45</td><td>375</td><td>97</td><td>472</td><td>11</td><td>483</td><td>97.7</td></tr></table>

We can observe the performance more precisely at the rule component level. Rule components consist of the statements RuleTable, Rule, Variable, Value, Operator, IF, THEN, and Connectives.

IC: Number of rule components identified at the RIML stage

sC: Number of rule components automatically generated from the shared components

dC: Number of rule components automatically generated from the default operators

GC: Number of rule components generated from the RIML statements.

$$
\mathrm{GC} = \mathrm{IC} + \mathrm{sC} + \mathrm{dC}\tag{2}
$$

rC: Number of rule components interactively added for rule refinement in the RSML stage. RC: Number of rule components after refinement.

$$
\mathrm{RC} = \mathrm{GC} + \mathrm{rC}\tag{3}
$$

With these notations, the Effectiveness of Rule Component Identification (in short Effectiveness) is defined as $\operatorname { E q . }$ (4) to measure the degree that the identified rules can cover:

$$
\text{Effectiveness} (\%) = \left[ \mathrm{GC} / \mathrm{RC} \right] \times 100\tag{4}
$$

The Efficiency Ratio by Sharing is defined as Eq. (5) by measuring the ratio of automatically generated rules in proportion to the number of identified components:

$$
\text { Efficiency   Ratio   by   Sharing } = \mathrm{sC} / \mathrm{IC}\tag{5}
$$

Efficiency implies the effort of rule coding that can be saved due to the automatically generated rules from the shared components. A higher ratio means a larger number of components can be automatically generated from the identified components. By the same token, we can define Efficiency Ratio by Default as Eq. (6):

$$
\text { Efficiency   Ratio   by   Default } = \mathrm{dC} / \mathrm{IC}\tag{6}
$$

To sum the total effect of sharing and default, let us define the term Efficiency Ratio by Automation:

$$
\mathrm{aC} = \mathrm{sC} + \mathrm{dC}\tag{7}
$$

$$
\text { Efficiency   Ratio   by   Automation } = \mathrm{aC/IC}\tag{8}
$$

To make the complete rule set, the knowledge engineer needs to add the linkage statements which are generically impossible to identify from the Web pages. To measure the effort level of adding the linkage statements, let us define the measure Linkage Effort (%) as the percentage of linkage components to total components. Linkage effort can be classified by its type whether it requires linkage statements with conclusions, or with other rules, or adding new rules for conclusions.

lC: Number of rule components added to provide linkages

TC: Total number of rule components necessary to build a complete rule-based system.

$$
\mathrm{TC} = \mathrm{RC} + 1 \mathrm{C}\tag{9}
$$

$$
\text { Linkage Effort } (\%) = [ \mathrm{IC/TC} ] \times 100\tag{10}
$$

Since the potential effectiveness of rule identification is limited by the linkage effort requirement, the Limit of Identification can be defined as Eq. (11):

Limit of Identification %ð Þ

$$
= 1 0 0 - \text { Linkage   Effort }\tag{11}
$$

Effectiveness in Eq. (2) may be defined as GC/TC reflecting the potential limitation by linkage requirement. So let us call the metric Overall Effectiveness as Eq. (12):

$$
\text{Overall Effectiveness} (\%) = \left[ \mathrm{GC} / \mathrm{TC} \right] \times 100\tag{12}
$$

The three online bookstore sites are evaluated with these metrics.

## 6.2. Overall experiment results

The overall experiment results are summarized in Table 2. Amazon has 21 relevant Web pages; BN 8 Web pages; and Powells Web 7 pages. The number of rule groups is four for all of the three cases. The total number of rules generated from each is 124, 101, and 258, respectively. Note that even though the number of pages in Powells is smaller than that in Amazon, the number of rules generated is higher because Powells uses bigger tables to describe the shipping rate.

In Amazon, the four rule groups are scattered in 21 Web pages. Seventy-nine rules are generated from 35 tables along with the texts in the titles and annotations, and 41 rules are generated from the texts, which amounts to 34.2% of all generated rules. The large number of rules from the tables contributes to the computational role necessary for shipping cost estimation. One hundred twenty rules were identified at the RIML stage, and four rules should have been added in the RSML stage. This shows that 96.8% of the rules could be identified from the context of Web pages. The four new rules were necessary for the logical linkages between rules and inferential conclusion. Likewise, BN needs four new rules, and Powells three. Since all of the new rules are the ones for conclusions, all rules extractable from the Web pages are identified. Overall, the effectiveness of rule identification is 97.7% for the Web pages in three sites, which is very high, showing that RIML is quite dependable.

However, not all identified rules are complete yet. To study the completeness of the generated rules, we need to observe performance at the rule component level as summarized in Table 3. In Amazon, the number of identified rule components at the RIML stage was 1635. From them, 737 rule components were automatically generated from the shared components, and 148 from default AND connectives. Thus, all rule components generated at the RIML stage total 2520. To make the incomplete draft rules complete, eight rule components should be added. So the effectiveness of rule component identification is 99.7% (=2520/2528). However, we have to add 206 components to link with the conclusions, which amounts to 7.5% of all rule components. Thus, the generic limit of automatic identification is 92.5%, and the overall effectiveness achieved is 92.2%. For the three sites, the effectiveness of rule components identified without counting the linkage statement (GC/RC) is 99.7%. However, due to the fact that there is an 88.8% identification limit, the achieved overall effectiveness of rule component identification (GC/TC) is 88.5%. So the potential of rule identification seems significant.

Performance of identifying rule components on the Web pages Table 3

<table><tr><td>Book store</td><td>Identified at RIML stage (IC)</td><td>Automatically generated from shared components (sC)</td><td>Automatically generated from default operators (dC)</td><td>All generated from RIML statements (GC=IC+sC+dC)</td><td>Efficiency ratio by sharing (sC/IC)</td><td>Efficiency ratio by default (dC/IC)</td><td>Interactively added for rule refinement (rC)</td><td>After refinement (RC=GC+rC)</td><td>Effectiveness (%)=[GC/RC]×100 (%)</td><td>Added to provide linkages (IC)</td><td>Total in complete rules (TC=RC+IC)</td><td>Linkage effort (%)=[IC/TC]×100 (%)</td><td>Overall effectiveness (%)=[GC/TC]×100 (%)</td></tr><tr><td>Amazon</td><td>1635</td><td>737</td><td>148</td><td>2520</td><td>0.451</td><td>0.091</td><td>8</td><td>2528</td><td>99.7</td><td>206</td><td>2734</td><td>7.5</td><td>92.2</td></tr><tr><td>BN</td><td>1151</td><td>494</td><td>109</td><td>1754</td><td>0.429</td><td>0.095</td><td>8</td><td>1762</td><td>99.5</td><td>175</td><td>1937</td><td>9.0</td><td>90.6</td></tr><tr><td>Powells</td><td>1616</td><td>730</td><td>484</td><td>2830</td><td>0.452</td><td>0.300</td><td>3</td><td>2833</td><td>99.9</td><td>519</td><td>3352</td><td>15.5</td><td>84.4</td></tr><tr><td>Total</td><td>4402</td><td>1961</td><td>741</td><td>7104</td><td>0.445</td><td>0.168</td><td>19</td><td>7123</td><td>99.7</td><td>900</td><td>8023</td><td>11.2</td><td>88.5</td></tr></table>

The efficiency ratio by sharing is 0.445 (=1961/ 4402), and the efficiency ratio by default is 0.168 (=741/4402). Thus, 0.613 times of the identified components are automatically generated during the transformation process, saving this amount of the rule coding effort.

## 6.3. Contribution of rule identification from the texts

We were curious about the relative contribution of texts and tables in building a rule base, although it depends upon the characteristics of Web pages rather than the technical potential of the XRML approach. In the domain of the shipping and return policy, the number of rules identified from the natural language texts on the Web is 41, 43, and 13 for Amazon, BN, and Powells, respectively, as listed in Table 4. They correspond to 34.2%, 44.3%, and 5.1% of all rules without counting the linkage components. In this example, the effectiveness of rule identification is 100% because the example Web pages are quite selfcontained and do not need extra rules from other sources.

At the rule component level, 959 rule components in Amazon are identified, and eight rule components are added during the rule refinement stage. This corresponds to an effectiveness of 99.2%, while it is 98.9% in BN, and 98.0% in Powells. The average effectiveness of rule component identification from texts is 99.0%. The result demonstrated that the potential effectiveness of the identifying rules from texts is very high.

## 6.4. Contribution of tables in generating rules

Rules are generated from not only texts but also tables. Amazon has 35 tables, while BN and Powells have seven and three tables, respectively. Powells describes the shipping rate for each country without grouping them, so the number of tables is small, and each table is very big. The layouts of tables can be quite different in this manner. It is interesting to note that all rules from the tables should be complemented by the texts near the tables such as titles and annotations.

The contribution of rules generated from tables of the three Web sites is summarized in Table 5. The number of rules identified from each is 79 in Amazon, 54 in BN, and 242 in Powells. They correspond to 65.8%, 55.7%, and 94.9% of all rules without counting linkage rules. The figure in Powells is particularly high because the site heavily depends upon tables.

Table 4  
Performance of texts in generating rules and components

<table><tr><td>Book store</td><td>Rules and components</td><td>Number of rule components at RIML stage (IC)</td><td>Number of generated rule components at RSML stage (GC)</td><td>Number of interactively added rule components for rule refinement (rC)</td><td>Number of generated rule components after rule refinement (RC)</td><td>Effectiveness disregarding linkages (GC/RC) (%)</td></tr><tr><td rowspan="2">Amazon</td><td>Rules</td><td>41</td><td>41</td><td>0</td><td>41</td><td>100.0</td></tr><tr><td>Components</td><td>680</td><td>959</td><td>8</td><td>967</td><td>99.2</td></tr><tr><td rowspan="2">BN</td><td>Rules</td><td>43</td><td>43</td><td>0</td><td>43</td><td>100.0</td></tr><tr><td>Components</td><td>603</td><td>717</td><td>8</td><td>725</td><td>98.9</td></tr><tr><td rowspan="2">Powells</td><td>Rules</td><td>13</td><td>13</td><td>0</td><td>13</td><td>100.0</td></tr><tr><td>Components</td><td>135</td><td>144</td><td>3</td><td>147</td><td>98.0</td></tr><tr><td rowspan="2">Total</td><td>Rules</td><td>97</td><td>97</td><td>0</td><td>97</td><td>100.0</td></tr><tr><td>Components</td><td>1418</td><td>1820</td><td>19</td><td>1839</td><td>99.0</td></tr></table>

Table 5  
Performance of tables in generating rules and components

<table><tr><td>Book store</td><td>Rules and components</td><td>Number of rule components at RIML stage (IC)</td><td>Number of generated rule components at RSML stage (GC)</td><td>Number of interactively added rule components for rule refinement (rC)</td><td>Number of generated rule components after rule refinement (RC)</td><td>Effectiveness disregarding linkages (GC/RC) (%)</td></tr><tr><td rowspan="3">Amazon</td><td>RuleTable</td><td>35</td><td>35</td><td>0</td><td>35</td><td>100.0</td></tr><tr><td>Rule</td><td>79</td><td>79</td><td>0</td><td>79</td><td>100.0</td></tr><tr><td>Components</td><td>955</td><td>1561</td><td>0</td><td>1561</td><td>100.0</td></tr><tr><td rowspan="3">BN</td><td>RuleTable</td><td>7</td><td>7</td><td>0</td><td>7</td><td>100.0</td></tr><tr><td>Rule</td><td>54</td><td>54</td><td>0</td><td>54</td><td>100.0</td></tr><tr><td>Components</td><td>548</td><td>1037</td><td>0</td><td>1037</td><td>100.0</td></tr><tr><td rowspan="3">Powells</td><td>RuleTable</td><td>3</td><td>3</td><td>0</td><td>3</td><td>100.0</td></tr><tr><td>Rule</td><td>242</td><td>242</td><td>0</td><td>242</td><td>100.0</td></tr><tr><td>Components</td><td>1481</td><td>2686</td><td>0</td><td>2686</td><td>100.0</td></tr><tr><td rowspan="3">Total</td><td>RuleTable</td><td>45</td><td>45</td><td>0</td><td>45</td><td>100.0</td></tr><tr><td>Rule</td><td>375</td><td>375</td><td>0</td><td>375</td><td>100.0</td></tr><tr><td>Components</td><td>2984</td><td>5284</td><td>0</td><td>5284</td><td>100.0</td></tr></table>

We can see that the effectiveness of rule component identification from tables is 100.0% for all of them. According to the performance from the tables, we can see that rule extraction from them along with complementary texts is highly reliable. It is interesting to note that although Powell has used more tables than text and bigger tables than the other two, it does not make a significant difference in performance.

## 6.5. Identification of omitted components and synonymous components

We analyzed the impact of omitted components and synonymous components in this experiment. A common thesaurus for the three online bookstores is built with 583 words. For the three sites, the original terms are used at 73.4%, 59.9%, and 37.0% levels from the texts, while 78.0%, 86.0%, and 98.3% are from the tables. Original terms are used more often from the tables because titles and headings of tables are more formally specified than ordinary texts.

The percentage of omitted terms from texts is 13.6%, 25.3%, and 24.7%, respectively, and 18.6%, 2.0%, and 0.4% from the tables. It seems that there are fewer omitted terms from tables because the terms associated with tables are usually formally annotated to improve the readability of tables. Adding omitted components in RIML will make the consistency maintenance easier between the Web pages and the rule base.

The percentage of synonyms used is 13.0%, 14.8%, and 38.3%, respectively, from the texts, and 3.5%, 12.0%, and 1.3% from the tables. Natural texts used more synonyms than tables because natural texts use many pronouns, which are treated as synonyms. To identify synonyms, RIML supports the facility to label the standard term in the tag.

According to the experimental results, effective treatment of omitted terms and synonyms is very important to make rule identification more complete.

## 6.6. Limitations of experiment results

Although the exploratory experiment has demonstrated the potential benefit of using XRML, the experiment has many limitations. The generic potential of XRML may be validated by regarding the number of Web pages as data points. However, the hypotheses about the relative performance of tables and texts need more data points regarding the Web sites as data points. When we have a larger number of data points in various contexts, we will be able to investigate the other interesting phenomena. The contexts may vary depending upon the application domains, and structural characteristics of pages.

This experiment has focused on the study of potential, rather than practical, benefit and cost of XRML. To evaluate the practical benefit and cost, we need to consider various factors such as the application’s practical necessity of consistency maintenance, the user interface capability of the XRML Editor, and the knowledge engineer’s familiarity with the domain and XRML approach. These experiments are good research opportunities.

## 7. Concluding summary and discussion

Knowledge acquisition and maintaining consistency with original sources have been the fundamental hurdles in knowledge engineering. In the world of Web pages, there are oceans of original documents in natural language texts and tables. If we are able to extract rules from Web pages and maintain consistency between them, the Web can be used more intelligently.

To attain this goal, we have developed the framework of XRML (eXtensible Rule Markup Language), which supports the identification of rules on the Web pages and generates the identified rules automatically. For this purpose, we have designed the Rule Identification Markup Language (RIML), which is similar to the formal Rule Structure Markup Language (RSML), both as parts of XRML. RIML is designed to identify rules not only from texts, but also from tables. So we can generate a rule set that can consider the texts and tables together. The beauty of RIML is that the rules identified on the Web pages can be automatically transformed to the formal rules in RSML syntax.

While designing RIML, we considered the feature of sharing variables and values, omitted terms, and synonyms. Handling them in RIML is beneficial because they may be coded or changed once, automatically generating its corresponding RSML rules. The significance of these features is demonstrated with the application concerning the Shipping and Return Policy.

We have conducted an experiment to observe the potential performance of the XRML approach with real world Web pages in Amazon.com, Barnesand-Noble.com, and Powells.com. We found that 97.7% of the rules could be detected from the Web pages because we need to add rules to make an inferential conclusion. If we disregard, the inferential conclusion rules that do not exist in the Web pages, we could detect 100.0% of rules and 99.7% of rule components. Since the linkage components occupies 11.2% of all components in the rule base, the overall limitation of automatic rule generation is 88.8%. In this setting, 88.5% of the overall rule components could be generated from the identified rules from the Web pages. The result provides solid proof that XRML can facilitate the extraction of rules from Web pages to build expert systems, and ensure the maintenance of consistency between the Web pages and rules. However, the result also implies that we need a powerful rule verification facility to assist the edition of linkage rules.

The application opportunity of the XRML approach seems various because every rule-based consulting system on tax, regulations, law, insurance underwriting, loan, funds, budgetary control, and salary systems, which have their counterpart Web pages, needs to adopt XRML to assure consistency. Since a different application may require extending the representation beyond rules, we need domain-specific research for key applications.

There are several topics that need further investigation in the XRML research agenda. The representation of rules should be extended to various target representations such as objects, constraints, mathematical expressions, and programming pseudocodes. This will open the new horizon of Consistent Web Computing along with heterogeneous representations. Another direction that requires development research is a user-friendly XRML Editor, which can assist knowledge engineers during rule identification and refinement. The capability of traditional rule refinement should be adopted to enhance XRML rule refinement. The capability of the XRML Editor will be enhanced by adding ontologies that can reuse the rules in the similar applications. XRML can be implemented on Web services platforms, building XRML-S. We expect XRML to become one of the key ingredients in the next-generation Semantic Web.

## Appendix A. The RIML version 2.0 document type definition

<?xml version="1.0" encoding="UTF-8"?> <!-- ENTITY Declarations --> <!ENTITY % op\_type"(LE|LT|GE|GT)"> <!-- ELEMENT and ATTLIST Declarations --> <!-- ELEMENT: RIML, RuleGroup, URL, RuleTable, Rule Declarations--> <!ELEMENT RIML (#PCDATA)> <!ATTLIST RIML version CDATA #REQUIRED> <!ELEMENT RuleGroup (URL+)> <!ATTLIST RuleGroup title CDATA #REQUIRED> <!ELEMENT URL (Rule | RuleTable| IF | THEN | variable | value | operator)+> <!ATTLIST URL rsml CDATA #REQUIRED> <!ELEMENT RuleTable ( (Rule| IF | THEN)\*, (value | variable | operator)\*)> <!ELEMENT Rule ( (IF | THEN)\*, (value | variable | operator)\*)> <!ATTLIST Rule rid ID #REQUIRED> title CDATA #IMPLIED> <!-- ELEMENT: IF, THEN, AND, OR, NOT Declarations--> <!-- rid attribute: rule id--> <!ELEMENT IF (THEN\*|AND | OR | NOT | (variable | value | operator)+)> <!ATTLIST IF rid IDREFS #IMPLIED>

<!ELEMENT THEN (IF\*|AND | OR | NOT | (variable | value | operator)+)> <!ATTLIST THEN rid IDREFS #IMPLIED> <!ELEMENT AND (AND | OR | NOT | variable | value | operator)+> <!ELEMENT OR (AND | OR | NOT | variable | value | operator)+> <!ELEMENT NOT (AND | OR | NOT | variable | value | operator)> <!--ELEMENT: variable, value, operator Declarations--> <!-- vid attribute: variable id-> <!-- name attribute: keyword of variable or value <!ELEMENT variable (#PCDATA)> <!ATTLIST variable vid ID #REQUIRED name CDATA #IMPLIED> <!ELEMENT value (#PCDATA)> <!ATTLIST value vid IDREF #REQUIRED name CDATA #IMPLIED> <!ELEMENT operator (#PCDATA)> <!ATTLIST operator vid IDREF #REQUIRED type %op\_type; #IMPLIED>

## References

[1] H. Alani, S. Kim, D.E. Millard, M.J. Weal, W. Hall, P.H. Lewis, N.R. Shadbolt, Automatic ontology-based knowledge extraction from Web documents, IEEE Intelligent Systems 18 (1) (2003) 14 – 21.

[2] G. Amati, I. Ounis, Conceptual graphs and first order logic, Computer Journal 43 (1) (2000) 1 – 12.

[3] C. Apte, F. Damerau, M.S. Weiss, Automated learning of decision rules for text categorization, ACM Transactions on Information Systems 12 (3) (1994) 233– 251.

[4] D. Babowal, W. Joerg, From information to knowledge: introducing WebStract’s knowledge engineering approach, Proceedings of the 1999 IEEE Canadian Conference on Electrical and Computer Engineering, Edmonton, Alberta, 1999 (May), pp. 1525–1530.

[5] H. Boley, S. Tabet, G. Wagner, Design rationale for RuleML: a Markup Language for Semantic Web rules, Proceedings of the Semantic Web Working Symposium, California, USA, 2001 (August), pp. 381–401.

[6] J.H. Boose, J.M. Bradshaw, J.L. Koszar, D.B. Shema, Knowledge acquisition techniques for group decision support, Knowledge Acquisition 5 (4) (1993) 405– 448.

[7] T. Bray, J. Paoli, C.M. Sperberg-McQueen, E. Maler, eXtensible Markup Language (XML) 1.0, 2nd edition of W3C, <sup>b</sup>http://www.w3.org/TR/RECxml<sup>N</sup> (2000).

[8] D. Brickley, R.V. Guha, Resource Description Framework (RDF) Schema Specification 1.0, W3C Recommendation, <sup>b</sup>http://www.w3.org/TR/2000/CR-rdf-schema-20000327/<sup>N</sup> (March 2000).

[9] D. Carlisle, P. Ion, R. Miner, N. Poppelier, Mathematical Markup Language (MathML) Version 2.0 (Second Edition), W3C Recommendation, <sup>b</sup>http://www.w3.org/TR/2003/REC-MathML2-20031021/<sup>N</sup> (October 2003).

[10] J. Clark, XSL Transformations (XSLT) Version 1.0, W3C Recommendation, <sup>b</sup>http://www.w3.org/TR/1999/REC-xslt-19991116<sup>N</sup> (November 1999).

[11] D. Connolly, F. van Harmelen, I. Horrocks, D.L. McGuiness, P.F. Patel-Schneider, L.A. Stein, DAML+OIL Reference Description, W3C Note <sup>b</sup>http://www.w3.org/TR/2001/ NOTE-daml+oil-reference-20011218<sup>N</sup> (2001).

[12] M. Craven, D. DiPasquo, D. Freitag, A. McCallum, T. Mitchell, K. Nigam, S. Slattery, Learning to construct knowledge bases from the World Wide Web, Artificial Intelligence 118 (1–2) (2000) 69 – 113.

[13] L. Crow, N. Shadbolt, Extracting focused knowledge from the Semantic Web, International Journal of Human–Computer Studies 54 (2001) 155– 184.

[14] B. Grosof, DAML rules phase II announcement, 2002 (October) <sup>b</sup>http://www.daml.org/rules/<sup>N</sup>.

[15] R.L. Grossman, S. Bailey, A. Ramu, B. Malhi, P. Hallstrom, I. Pulleyn, X. Qin, The management and mining of multiple predictive models using the Predictive Modeling Markup Language (PMML), Information and Software Technology 41 (1999) 589– 595.

[16] N. Guarino, Understanding, building and using ontologies, International Journal of Human and Computer Studies 46 (1997) 293– 310.

[17] I. Horrocks, DAML+OIL: a description logic for the semantic Web, IEEE Data Engineering 25 (1) (2002) 4– 9.

[18] I. Horrocks, P.F. Patel-Schneider, F. van Harmelen, From SHIQ and RDF to OWL: the making of a Web ontology language, Journal of Web Semantics 1 (1) (2003) 7 – 26.

[19] A. Hulth, J. Karlgren, A. Jonsson, H. Bostr<sup>f</sup>m, L. Asker, Automatic keyword extraction using domain knowledge, Proceedings of the Second Computational Linguistics and Intelligent Text Processing, Mexico City, Mexico, 2001, pp. 472 – 482.

[20] W. Jicheng, H. Yuan, W. Gangshan, Z. Fuyan, Web mining: knowledge discovery on the Web, Proceedings of the IEEE Conference on Systems, Man, and Cybernetics, Tokyo, Japan, 1999 (October).

[21] J.D. Kim, J.F. Courtney, A Survey of knowledge acquisition techniques and their relevance to managerial problem domains, Decision Support Systems 4 (3) (1988 September) 269 – 284.

[22] W.T. Kim, J.K. Lee, J. Kang, XRML-based knowledge sharing system by using XRML, Proceedings of the Korea Society of Management Information System, 2002 (Spring), pp. 706 – 715.

[23] D. Kim, H. Jung, G. Lee, Unsupervised learning of mDTD extraction patterns for Web text mining, Information Processing & Management 39 (4) (2003) 623 – 637.

[24] O. Lassila, R.R. Swick, Resource Description Framework(RDF) Model and Syntax Specification, W3C Recommendation, <sup>b</sup>http://www.w3.org/TR/REC-rdf-syntax/<sup>N</sup> (February 1999).

[27] J.K. Lee, I.K. Lee, S.M. Ahn, H.R. Choi, Automatic rule generation by the transformation of Expert’s Diagram: LIFT, International Journal of Man–Machine Studies 30 (1990) 275–292.

[25] J.K. Lee, M. Sohn, Enhanced knowledge management with eXtensible Rule Markup Language, Proceedings of the 36th Hawaii International Conference on System Sciences, 2003 (January), pp. 209– 216.

[26] J.K. Lee, M. Sohn, eXtensible Rule Markup Language— toward intelligent Web platform, Communications of the ACM 46 (2003 May) 59–64.

[28] A. Levy, M.C. Rousset, Combining horn rules and description logics in CARIN, Artificial Intelligence 104 (1998 September).

[29] J. Liebowitz, Foundation and application of expert system verification and validation, The Handbook of Applied Expert Systems, CRC Press LLC, 1998, pp. 111– 151.

[30] A. Maedche, S. Stabb, Mining ontologies from text, Proceedings of the European Knowledge Acquisition Workshop, Lecture Notes in Artificial Intelligence, vol. 1937, 2000, pp. 189 – 202.

[31] J. McCarthy, Epistemological problems of Artificial Intelligence, Proceedings of the 5th Joint Conference on AI, 1977.

[32] J. McCarthy, Circumscription—a form of nonmonotonic reasoning, Artificial Intelligence 13 (1–2) (1980) 171 – 172.

[33] J. McGovern, D. Samson, A. Wirth, Knowledge acquisition for intelligent decision systems, Decision Support Systems 7 (3) (1991 August) 263 – 272.

[34] E. Miller, R. Swick, D. Brickley, B. McBride, J. Hendler, G. Schreiber, Semantic Web introduction, specifications and related works, 2001 <sup>b</sup>http://www.w3.org/2001/sw/<sup>N</sup>.

[35] B. Moulin, D. Rousseau, Designing deontic knowledge base from regulation texts, Knowledge Based Systems 3 (2) (1990 June) 108– 120.

[36] B. Moulin, D. Rousseau, SACD: a system for acquiring knowledge from regulatory texts, Computers and Electrical Engineering 20 (2) (1994) 131– 149.

[37] T.A. Nguyen, W.A. Perkins, T.J. Laffey, D. Pecora, Knowledge base verification, AI Magazine 8 (2) (1987) 69 – 75.

[38] R.T. Plant, Techniques for knowledge acquisition from text, The Journal of Computer Information Systems 35 (1) (1994) 64 – 70.

[39] G. Psaila, S. Crespi-Reghizzi, Adding semantics to XML, Proceedings of the Second Workshop on Attribute Grammars and their Applications, Amsterdam, The Netherlands, 1999 (March), pp. 113 – 132.

[40] L.F. Rau, P.S Jacobsa, U. Zernika, Information extraction and text summarization using linguistic knowledge acquisition, Information Processing & Management 25 (4) (1989) 419– 428.

[41] J.M. Ruiz-Sa´nchez, R. Valencia-Garcı´a, J.T. Ferna´ndez-Breis, R. Martı´nez-Be´jar, P. Compton, An approach for incremental knowledge acquisition from text, Expert Systems with Applications 25 (1) (2003) 77 – 86.

[42] RuleML, The Rule Markup Initiative, <sup>b</sup>http://www.dfki.uni-kl. de/ruleml/<sup>N</sup> (2003).

[43] R. Sa´nchez-Carren˜o, J.T. Ferna´ndez-Breis, R. Martı´nez-Be´jar, P. Cantos-Go´mez, An ontology-based approach knowledge acquisition from text, Cuadernos de Filologia Inglesa 9 (1) (2000) 191 – 212.

[44] G. Schmidt, T. Wetter, Using natural language sources in model-based knowledge acquisition, Data and Knowledge Engineering 26 (1998) 327–356.

[45] J.P. Seagle, P. Duchessi, Acquiring expert rules with the aid of decision tables, European Journal of Operational Research 84 (1) (1995 July) 150 – 162.

[46] M.K. Smith, C. Welty, D. McGuinness, OWL Web Ontology Language Guide, W3C Working Draft, <sup>b</sup>http://www.w3.org/ TR/2003/WD-owl-guide-20030331/<sup>N</sup> (2003).

[47] S. Soderland, Learning information extraction rules for semistructured and free text, Machine Learning 34 (1) (1999) 233– 272.

[48] S. Szpakowicz, Semi-automatic acquisition of conceptual structure from technical texts, International Journal of Man– Machine Studies 33 (4) (1990) 385– 397.

[49] W.M.P. van der Alast, A. Kumar, XML-based schema definition for support of interorganizational workflow, Information Systems Research 14 (1) (2003) 23– 46.

[50] G. van Heijst, A.T. Schreiber, B.J. Wielinga, Using explicit ontologies in KBS development, International Journal of Human–Computer Studies 45 (1997) 183 – 292.

[51] M. Vargas-Vera, E. Motta, J. Domingue, S.B. Shum, M. Lanzoni, Knowledge extraction by using an ontology-based annotation tool, Proceedings of the Knowledge Markup and Semantic Annotation Workshop, Canada, 2001.

[52] E.C. Way, Conceptual graphs—past, present, and future, in: Lecture Notes in Computer Science, vol. 835, Springer-Verlag, 1994.

[53] T. Wetter, R. Nse, Use of natural language for knowledge acquisition: strategies to cope with semantic and programmatic variation, IBM Journal of Research and Development 36 (3) (1992 May) 435– 468.

[54] S.B. Yang, J.K. Lee, An XRML-based knowledge auditing system for the online shopping mall user agreement, Proceedings of the Korea Society of Management Information System, 2003 (Spring), pp. 1085 – 1094.

[55] J. Yang, H. Oh, K.G. Doh, J. Choi, A knowledge-based information extraction system for semi-structured labeled documents, Proceedings of the 4th Intelligent Data Engineering and Automated Learning, Lecture Notes in Computer Science, vol. 2412, 2002, pp. 105– 110.

![](/api/attachments/SC44ASXG/fulltext/images/bacac2ac541df92a186f06da38b0f96ed7c34dd6fc241ad4cdb17ac6eeb9ed9c.jpg)  
Juyoung Kang is an Assistant Professor of e-Business at Ajou University. She received a PhD degree in Management Engineering from the Graduate School of Management at Korea Advanced Institute of Science and Technology (KAIST), and served as a principal researcher at International Center for Electronic Commerce (ICEC). She received her BS in Computer Science from Pohang University of Science and Technology (POSTECH) and MS in

Computer Engineering from Seoul National University. She has developed Intelligent Information Systems and Electronic Commerce applications with various industrial partners. Her current research interests are in the fields of Semantic Web, Intelligent Information Systems, and Electronic Commerce.

![](/api/attachments/SC44ASXG/fulltext/images/6de4ea80f1a2ca013ebb7f8e3873e8d38f72fdb19452b07390a243dab5ace398.jpg)

Jae Kyu Lee is a Professor of Management Information Systems at the Korea Advanced Institute of Science and Technology and a Director of the International Center for Electronic Commerce. He received a PhD degree from the Wharton School, University of Pennsylvania. He was Chair of the International Conference on Electronic Commerce (ICEC 1998 and ICEC 2000) and the Third World Congress on Expert Systems (1996). He has authored

several books on electronic commerce and expert systems and published numerous papers in the following journals: Management Science, CACM, DSS, Expert Systems with Applications, International Journal of Electronic Commerce, Decision Science, etc. Currently, he is the Editor-in-Chief of the journal Electronic Commerce Research and Applications, and an editorial member of various international journals such as Decision Support Systems, Expert Systems with Applications, International Journal of Electronic Commerce, etc. His main research interests are in the fields of Electronic Commerce and Intelligent Information Systems.
