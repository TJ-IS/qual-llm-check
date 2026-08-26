---
otero_id: 24776
otero_key: "AD7UNBQE"
title: "Requirements Validation via Automated Natural Language Parsing"
authors: "Sastry Nanduri; Spencer Rugaber"
year: "1995"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1995.11518088"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Requirements Validation via Automated Natural Language Parsing

Sastry Nanduri & Spencer Rugaber

To cite this article: Sastry Nanduri & Spencer Rugaber (1995) Requirements Validation via Automated Natural Language Parsing, Journal of Management Information Systems, 12:3, 9-19, DOI: 10.1080/07421222.1995.11518088

To link to this article: http://dx.doi.org/10.1080/07421222.1995.11518088

![](/api/attachments/AD7UNBQE/fulltext/images/35c6e366ada7cf6f3d770a2a7c72d3543ebeed2bee2530cdf321ec53e072faea.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/AD7UNBQE/fulltext/images/722777e9211d11ad15d3d995b32ca7c7fa85a315a59540a556e817e98bb2a00b.jpg)

Submit your article to this journal ↗

![](/api/attachments/AD7UNBQE/fulltext/images/57dcbd382ac46339fd047d575eee4e41274fa0bae0746c96795fc899c65c6f59.jpg)

View related articles ↗

# Requirements Validation via Automated Natural Language Parsing

SASTRY NANDURI AND SPENCER RUGABER

SASTRY NANDURI was a graduate student in the College of Computing at Georgia Tech when the work described in this paper was performed. He has since graduated with a master's degree in computer science.

SPENCER RUGABER is a Senior Research Scientist in the College of Computing at the Georgia Institute of Technology. Since receiving his Ph.D. from Yale University in 1978, Dr. Rugaber has worked in industry where he was responsible for the development of programming language tools, TEN/PLUS, an integrated environment for interacting with the UNIX operating system, and environments for improving software productivity. Since January 1988, Dr. Rugaber has been at Georgia Tech where he teaches courses in programming language and systems and software engineering. His research has concentrated on software engineering, specifically program understanding and user interface design. He is currently Vice Chair of the Reverse Engineering committee of the IEEE Technical Council on Software Engineering.

ABSTRACT: Object-oriented analysis (OOA) has become a popular method for analyzing system requirements. Unfortunately, however, none of the current versions of OOA has included a validation technique tailored to the object-oriented approach. Most, instead, merely recommend document reviews without specifying the kinds of problems to look for. This paper explores the question by applying a natural language parser to a requirements document, extracting candidate objects, methods, and associations, composing them into an object model diagram, and then comparing the results with those determined by manual OOA. To do this, we have adapted an automated natural language parser and used it to examine several high-level system descriptions. The results indicate that, with a modest amount of effort, the technique can give valuable feedback to the analyst.

KEY WORDS AND PHRASES: link grammars, natural language processing, object-oriented analysis, systems analysis.

THE FIRST STEP IN MOST OBJECT-ORIENTED ANALYSIS METHODS is the construction of an object model. Many guidelines exist for identifying object classes, their relationships, and their attributes from a problem statement. Are these guidelines comprehensive enough for automating the construction process? Probably not, but can we instead use automatic analysis to generate a model against which a manually generated analysis can be validated? The best way to answer these questions is by actually trying to implement a program for generating an object diagram from a system description.

There are several papers that discuss the possibility of automatic construction of an object model. Honiden et al. [6] developed a standardized, formal OOA specification process as a precursor to automation. Seki et al. [11] describe a process for incrementally deriving a formal specification from an informal specification. Abbott [1] details a method for generating a program design from an informal English description. All these papers only give suggestions as to how to automate the analysis process. We could find no description in the published literature of the actual implementation of an object model constructor. The purpose of this paper is to describe one such implementation.

Traditional approaches, such as Structured Analysis, focus mainly on the functionality of a system. OOA, on the other hand, focuses on the objects or static entities of the system and the associations among them. A main reason for its popularity is the fact that a system designed around static entities is less affected by subsequent changes in the requirements than one organized functionally.

Booch [2] was the first to formalize the object-oriented approach. Now there are several popular object-oriented methods such as OOA by Coad and Yourdon [4], object-oriented design (OOD) by Booch [3], and object modeling technique (OMT) by Rumbaugh et al. [10]. The methods have much in common. They all start with the detection of objects in the system by textual analysis of a specification document. After objects are identified, the system is modeled in terms of their attributes and the interactions among them. As originally proposed, nouns in the specification document are good indicators of objects. Similarly, verbs and adjectives are good signals for the associations among and attributes of the objects.

We chose OMT because of its popularity and extensive documentation. Of the three OMT models (object, dynamic, and functional), we are only concerned with the object model since it is the most conducive to textual analysis. The approach recommended by Rumbaugh et al. for object modeling has the following steps:

1. Identify objects and classes (nouns);

2. Identify associations between objects (verb phrases);

3. Identify attributes of objects and associations (adjectives);

4. Identify operations (verbs and adjectives);

5. Organize and simplify object classes using inheritance $^{1}$ ;

6. Iterate and refine the model.

## Approach

THE APPROACH WE TOOK TO AUTOMATING THE ANALYSIS PROCESS is as follows. We first collected a list of guidelines on object modeling from Rumbaugh et al. [10]. We expressed the guidelines in terms of the parsing rules for a publicly available natural language parser. We then applied these guidelines to the parser output of several high-level system descriptions and analyzed the results. After refining the parsing rules, we repeated the process for several other documents. Finally, we implemented a program that used the refined guidelines and a graph drawing tool to display object diagrams for the systems analyzed.

More precisely, the steps we followed in building our analyzer were:

1. We gathered guidelines for creating an object model and for identifying nouns, verbs, and the like, from the OMT text.

2. We used a publicly available natural language parser to parse a system description document. We chose a link grammar-based parser because it was easily available, because it was able to parse a wide range of English sentences, and because its dictionary was easily extended.

3. We wrote a rule-based postprocessor. These rules are nothing but the guidelines gathered in step 1 expressed in terms of the parser's links.

4. We extended our tool to accumulated knowledge between sentences. The parser we used parsed each sentence of the input independently. So, for the construction of an object model from a multisentence document, we had to accumulate knowledge gained from each of the sentences. Since there is no foolproof way of connecting the pronouns in a sentence with the appropriate antecedent in the previous sentence, we also had to apply some ad hoc rules for doing this.

5. Finally, we built and displayed the object model. For displaying the object diagram graphically, we used a publicly available graph drawing tool called EDGE [8]. EDGE is an easy to use, extendible graph editor. Graphs can be constructed either interactively or by creating an input file consisting of a list of nodes and edges. The program we developed for step 3 took the latter course and wrote the accumulated knowledge about the objects and associations into a file in a format understandable by EDGE.

## Natural Language Parsing Using Link Grammars

The parser we used was developed by Daniel D. Sleator and Davy Temperley at Carnegie Mellon University [12]. This parser is based on the theory of link grammars. A link grammar consists of a set of words (the terminal symbols of the grammar), each of which has one or more linking requirements. A sequence of words is a sentence of the language defined by the grammar if there is a way to assign links among the words so as to satisfy the following three conditions:

1. Planarity—the links do not cross;

2. Connectivity—the links suffice to connect all the words of the sequence together;

3. Satisfaction—the links satisfy the linking requirements of each word in the sequence.

The linking requirements of each word are contained in a dictionary where they are expressed as a formula involving the operators and or, parentheses, and connector names. The + or - suffix on a connector name indicates the direction relative to the word being defined in which the matching connector must lie. For example, the linking requirements for the words "Mary" and "ran" are shown below:

Mary: $O-$ or $S+$

ran: S-

That is, “Mary” can act as a direct object if a corresponding verb is on the left or as a subject if a corresponding verb is on the right. “Ran” expects a subject on its left. The linking requirements are satisfied in the sentence “Mary ran” but not in the sentence “ran Mary.” Hence, the latter is not accepted by the parser.

The output of the parser consists of all the words along with the links satisfying the linking requirements. We found that the connectors used to express the linking requirements (O and S in the example above) are useful in identifying the nouns and verb phrases of a sentence and, thereby, the object classes and their associations. For example, the output upon running the parser on the sentence “Mary ran” consists of the following connectors:

![](/api/attachments/AD7UNBQE/fulltext/images/7e772e49779b1cc70a8f637ced14ddfd7a3425125521051912bec97f1e8e989f.jpg)

This output indicates that the word “Mary,” which is on the left side of the link, has the connector $S+$ and that the word “ran” has the connector $S-$ . We can gather by looking at the $S+$ connector that “Mary” is the subject in the above sentence. Likewise, “ran” is identified as a verb because it has the connector $S-$ .

For a better understanding of how the output of the parser can be used to identify the classes, relationships, and so on, consider the following sentence “The company pays the employees.” The parser’s output for this sentence is:

![](/api/attachments/AD7UNBQE/fulltext/images/c11b0b2003474be704d6f0b90413ef7e2970a175e28730cdf4cdb69b4d98bc26.jpg)

“Company” is recognized as a noun (the “.n” suffix); “the” is a determiner; “pays” is a verb expecting a subject and a direct object, with “the employees” serving the latter role.

By using the guideline that any sentence of the form Subject -S- verb -O- Object implies that the classes Subject and Object have the association named by the verb, we can infer that company and employees are classes and that pays is an association between them. Most of the guidelines for object identification can be expressed in terms of links in this way.

## Object and Association Detection Guidelines

Rumbaugh et al. [10] give some practical tips on how to find classes, associations, and attributes in a problem statement. They also suggest how to eliminate bad classes, associations, and the like. Both these and the other guidelines in the literature are very general. A guideline of the form “names that primarily describe individual objects should be restated as attributes,” though helpful for a human designer, cannot easily be incorporated into program logic. The main problem when trying to incorporate such knowledge is how the program can find out which names describe individual objects. Most of our effort in working on this project was spent on expressing the existing guidelines in terms of the connectors. That is, we transformed the guidelines into precise rules in terms of the parser’s output.

Examples of the rules that we used to implement our program are given below. For every word in the input sentence, the program checks if any of the guidelines are satisfied. If this is the case, then the corresponding inference is made.

1. If a word is “with” and if it has J (preposition) and M (participle) connectors, then the class described by the word with the M connector is an aggregation $^{2}$ of the class described by the word with the J connector. Example: A sentence containing “building with floors . . .” indicates that building is an aggregation of floors.

2. For every verb, if there is an EV (verb used with prepositional phrases) connector, get the J connector of the EV connector, if it exists. Or if there is a V connector, and the V connector has an I connector and the I (indirect object) connector has a TO (infinitive) connector and the TO connector has an S connector, get the final S connector. If either of the above-mentioned connectors exists, the two words are candidate classes, and they have an association named by the verb. Example: A sentence of the form “A system is to be installed in a building” indicates that system and building have an association installed.

3. If a verb has a V connector followed by an S connector, get the S connector. Also get the J connector following the EV connector. These words are classes, and they have the association given by the verb. Example: A sentence containing “candidate is fired by the company” indicates that there is an association fired between candidate and company.

4. If a verb is “becomes,” then the O connector is a state (attribute) of the S connector. Example: A sentence containing “person becomes candidate” indicates that candidate (candidacy) is an attribute of the class person.

## The Postprocessor

The postprocessor that we developed applies the guidelines to the parser output and produces the list of objects, their attributes, and the associations among them. The postprocessor is written in the C programming language and is integrated into the parser code. We took this approach because the number of guidelines that we had was not very large. If the number of guidelines becomes larger, it may prove advantageous to separate the postprocessor code from the parser code.

The postprocessor also makes use of a file of synonyms while processing the output of the parser. The synonyms are used for two purposes:

\- To avoid creating redundant objects for synonymous nouns in a document; and
- To recognize plurals (e.g., “companies,” “company”) and different tenses of verbs (“fire,” “fires,” “fired,” etc.) as the same. $^{3}$

After all the sentences of the input document are parsed and processed, the postprocessor writes the gathered information into two files: Output\_file and "graph." Output\_file, the name of which is specified by the user, contains the results in English. That is, it will have statements like "building is an aggregation of floors." The file with the name "graph" has the same information written in a form understandable by EDGE.

## Example

THIS SECTION DESCRIBES THE ACTION OF THE SYSTEM in analyzing a description of a small database system for an employment agency. It is taken verbatim from [7].

## The Original Description

Persons apply for positions, companies subscribe by offering positions, and companies hire candidates or fire employees. A person may apply only once, thus becoming a candidate, losing this status when hired by a company but regaining it if fired; a company may subscribe several times, the positive number of offerings being added up; finally, only persons that are currently candidates may be hired, and only by companies that have vacant positions. There are queries to check whether a person is a candidate, for finding out the company a person works for (provided that the person is not a candidate), and for finding out the number of vacant positions a company still has (provided that the company has ever subscribed). Initially, no person is a candidate and no company has subscribed.

## Modified System Description

The link grammar parser has difficulty parsing certain constructs, requiring manual modification of the input text. Our intent is to only make modifications dependent on the parser and not on domain knowledge required to understand the text. After modification, the text reads as follows:

Persons apply for positions, companies subscribe by offering positions, and companies hire candidates or fire employees. A person may apply only one time. The person becomes a candidate when he applies. A person loses his status as a candidate when hired by a company. A person becomes a candidate again if he is fired by the company. A company may subscribe several times. Only persons that are still candidates can be hired by companies. Only companies that have vacant positions can hire candidates. There is a query to check if a person is a candidate. There is a query to find the company a person works for. There is a query to find out the number of vacant positions at a company. Initially, no person is a candidate and no company has subscribed.

## Program Output

The program generates the output shown in Table 1, where associations are indicated by triples of the form: Object Class—Association—Object Class; operations and attributes are indicated by stating their name and the class to which they belong; inheritance and aggregation associations are suggested; and synonyms are placed in parentheses. Note also that the parser may produce duplicate suggestions, which have been manually removed from Table 1.

## Object Diagram

The results of running the parser are placed in a file that is then fed to the EDGE graph drawing tool. For the input text given above, the diagram shown in Figure 1 is produced. Classes are contained in rectangles; arcs denote associations. Classes contain three parts: the class name, its attributes, and its operations. Note that there are several ways in which the diagram could be easily improved. For example, an association that holds between one class and a second as well as between the first class and a subclass of the second could be replaced by a single association. Also, situations where an operation and an association on a class have the same name could be detected and resolved.

## Results

WE APPLIED THE PARSER TO FOUR HIGH-LEVEL SYSTEM DESCRIPTIONS commonly chosen as examples in software engineering textbooks.

## Helicopter Landing

The helicopter system description has been taken from [5]. Before running the parser on it, we had to rephrase some of the sentences as simple sentences. There was not much information that we could gather from the parser's output. The main problem was with the system description itself, which described the history of the problem rather than stating the requirements. We feel that even manual construction of an object diagram from this description is not possible.

## Automatic Teller Machine (ATM)

We obtained another system description from chapter 8 of reference [10]. Here, the problem was stated very clearly, probably because it was used to illustrate the construction of an object model. The result of applying our rules to this description was encouraging. The resulting object diagram was reasonably close to that produced by hand. There were some differences, but these were all minor. For example, several extra classes such as system and cost were suggested. The main reason why our approach produced them was because recognizing these classes as bad classes required domain knowledge, which neither the parser nor the postprocessor had.

Table 1. Parser Output for Employment Database Example

persons (person) — apply — positions
companies (company) — hire — candidates (candidate)
companies (company) — fire — employees (employee)
person — apply — time
candidate is an attribute value of class person
becomes (become) is an operation of class person
applies (apply) is an operation of class he (person)
person — loses (lose) — status
loses (lose) is an operation of class person
company — hired (hire) — person
candidate is an attribute value of class person
he (person) — fired (fire) — company
company — subscribe — times
still is an attribute value of class candidates (candidate)
hired (hire) is an operation of class persons (person)
vacant is an attribute value of class positions
hire is an operation of class companies (company)
class candidate can be a subclass of class person
subscribed (subscribe) is an operation of class company

## The Lift System

The lift system description is taken from $[9]$ . Most of the differences in the object diagram produced from using our approach and that produced manually were due to the inadequacy of the parser in capturing some aspects of English grammar. And the rules that we used were not powerful enough to offset the parser's weakness. Here is an example of the type of problem we experienced. In the sentence, “Each lift has a set of buttons, one for each floor,” ideally the parser should have recognized that the word “one” refers to a button. From the parser’s output, we could not derive a general rule for recognizing the classes and associations correctly in a sentence of this form.

## Employment Database

The results of applying our approach to this system description were also encouraging. We realized, however, that the rules approach to finding objects and association has some drawbacks. We found that some guidelines cannot easily be expressed with rules. For example, from the sentence, “there is a query to check if a person is a candidate,” our program identified “query” as an object instead of an operation, which would be desirable if we were building a general database management system but is suboptimal for a small, special-purpose program. Furthermore, because of the way the rule is defined, our program would have identified “way” as an object in the following sentence: “There is a way to check if a person is a candidate.”

![](/api/attachments/AD7UNBQE/fulltext/images/e933291d50973a58cafbd8d6942ac91448af49cca0db4c43c03ed31d888eb36b.jpg)  
Figure 1. Object Diagram for Employment Database Example

## Conclusions and Future Work

WITH A RELATIVELY SMALL AMOUNT OF WORK (about three weeks and under 800 lines of code), we were able to build a tool capable of producing object diagrams that could be compared with those produced by hand. Among the uses of the resulting diagram would be detection of missing classes, suggestion of alternative modeling choices (attribute versus class or operation versus association), and discovery of missing associations.

## Limitations

As described in the previous section, the object diagrams generated by our approach were not completely satisfactory. The failure in producing completely acceptable object diagrams is due to the following factors:

\- Parser inadequacy: While the breadth of English text that the parser accepts is quite impressive, it still cannot handle many sentences. For example, the parser does not accept hyphenated words, idiomatic expressions, and quotation marks. And it cannot connect a pronoun with the corresponding noun. We have overcome these problems to some extent by rephrasing some input sentences in a form acceptable to the parser. For the process to be completely automated, the parser should be powerful enough to accept all types of sentences.

\- Ambiguous or incomplete descriptions: Sentences of the form “ATM accepts cash cards” can be difficult to deal with when the reader is a computer. Where does the ATM accept the cash card from? While an intelligent human understands this from the context, it is difficult for a program to do the same.

\- Lack of domain knowledge: In the ATM document a lot of domain knowledge was required to generate the object diagram. Knowledge such as “bank holds account” and “customers have cash cards” was assumed and not explicitly mentioned in the text. A practical automated analysis tool will need domain knowledge and common sense. There are two approaches to the solution of this problem. We can incorporate the domain knowledge in the parser. Or we can write the system description without assuming any domain knowledge on the part of the user. Both the approaches have practical difficulties.

\- Inadequacy of guidelines: Most of the rules we derived work for general cases. But they cannot handle special situations. For example, consider the following sentence from the employment database system description: "There is a query to check if a person is a candidate." We can make query a class or an operation of the class person. A human needs to look at the overall structure of the object diagram and use his or her experience to decide whether to make query an object or an operation. Since all our rules are based on the structure of the sentence, such decisions cannot be made by the program.

## Future Work

As noted earlier, a program that will automatically produce a perfect object diagram from a system description document is not currently possible. But our program can be used to validate a manually produced object diagram and to generate a preliminary object diagram that can be refined by human designers. The following enhancements suggest themselves as future directions for our research:

\- Testing the tool on real-life (lower) level documents, particularly those with a specialized domain vocabulary.

\- Comparing the results of our semiautomatic validation with those produced in

a design review, both for thoroughness and cost-effectiveness.

\- Testing the program with a wide range of documents and refining the guidelines appropriately.

\- Using a parser other than the link grammar parser to see if some of the parsing limitations can be overcome.

## NOTES

1. Inheritance is a special kind of association indicating that one object class is a special case of another.

2. Aggregation is a special kind of association that indicates that objects in one class can be considered as part of objects in the other.

3. An alternative is a root word extractor such as that used by the UNIX "spell" command.

## REFERENCES

1. Abbott, R.J. Program design by informal English descriptions. Communications of the ACM, 12, 11 (November 1983), 882–894.

2. Booch, G. Object-oriented development. IEEE Transactions on Software Engineering, 12, 2 (February 1986).

3. Booch, G. Object-Oriented Design with Applications. Redwood City, CA: Benjamin/Cummings, 1991.

4. Coad, P., and Yourdon, E. Object-Oriented Analysis, 2d ed. Englewood Cliffs, NJ: Yourdon Press, 1991.

5. Davis, A.M. Software Requirements, Objects, Functions, and States. Englewood Cliffs, NJ: Prentice-Hall, 1993.

6. Honiden, S.; Kotaka, N.; and Kishimoto, Y. Formalizing specification modeling in OOA. IEEE Software, 10, 1 (January 1993), 54–66.

7. Jackson, M.I. Developing Ada programs using the Vienna Development Method (VDM). Software-Practice and Experience, 15, 3 (March 1985), 305–318.

8. Paulish, F.N., and Tichy, W. EDGE: an extendible graph editor. Software-Practice and Experience, 20, S1 (June 1990), 63–86.

9. Proceedings of the Fourth International Workshop on Software Specification and Design. April 3–4, 1987, Monterey, California, IEEE Computer Society, 1993.

10. Rumbaugh, J.; Blaha, M.; Premerlani, W.; Eddy, F.; and Lorensen, W. Object-Oriented Modeling and Design. Englewood Cliffs, NJ: Prentice-Hall, 1991.

11. Seki, M.; Horai, H.; and Enomoto, H. Software development process from natural language specification. Eleventh International Conference on Software Engineering, May 1989.

12. Sleator, D.D., and Temperley, D. Parsing English with a link grammar. Carnegie Mellon University, Department of Computer Science, March 1992.
