---
otero_id: 24758
otero_key: "7N7CM28V"
title: "Natural Language Access to Multiple Databases: A Model and a Prototype"
authors: "Phillip Ein-Dor; Israel Spiegler"
year: "1995"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1995.11518074"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Natural Language Access to Multiple Databases: A Model and a Prototype

## Phillip Ein-Dor & Israel Spiegler

To cite this article: Phillip Ein-Dor & Israel Spiegler (1995) Natural Language Access to Multiple Databases: A Model and a Prototype, Journal of Management Information Systems, 12:1, 171-197, DOI: 10.1080/07421222.1995.11518074

To link to this article: https://doi.org/10.1080/07421222.1995.11518074

![](/api/attachments/7N7CM28V/fulltext/images/d2ca6d76bec9aa72df1a9bc42a4acebdca5b16fd4f037158ea856decae625e2d.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/7N7CM28V/fulltext/images/11eb84dd65f2ae68e44f90c416da0f3517c19450b5802eed54e1bbe1c7b82afc.jpg)

Submit your article to this journal ↗

![](/api/attachments/7N7CM28V/fulltext/images/e30676b9b3055def751dde5ef720c35076e51bf7d1866994d26853dde23a5278.jpg)

Article views: 1

![](/api/attachments/7N7CM28V/fulltext/images/23e196ba70e95a088e131a00a6e4b1d79a1390421ce4cce49e7fcea817960264.jpg)

View related articles ↗

![](/api/attachments/7N7CM28V/fulltext/images/0998410ae97ad6300ddf56cf370517ca6467d0fccd888ad2227491ccced54b46.jpg)

Citing articles: 5 View citing articles ↗

# Natural Language Access to Multiple Databases: A Model and a Prototype

PHILLIP EIN-DOR AND ISRAEL SPIEGLER

PHILLIP EIN-DOR is a Professor and Director of the Marcel and Annie Adams Institute for Business Management Information Systems in the Faculty of Management, Tel-Aviv University. His research and teaching interests include IS theory, computer economics, knowledge representation, and national IT policy. He is a member of the editorial boards of Information & Management, MIS Quarterly and Journal of Information Resource Management, a board Member of the Society for Information Management (SIM), and a council member of the Information Processing Association of Israel.

ISRAEL SPIEGLER is an Associate Professor and chair of the Information Systems Department at Tel-Aviv University Graduate School of Management. He holds an M.Sc. and a Ph.D. in computers and information systems from UCLA. He was an Associate Professor at Boston University and Visiting Associate Professor at Claremont Graduate School and UCLA. His main areas of interest are information systems, database management, systems analysis, artificial intelligence, and human-machine interface, areas in which he has published extensively.

ABSTRACT: A model is proposed that defines “context” for natural language queries in a multiple database environment and a suggested implementation for this model is described. The approach developed in this study relaxes the assumption usually made for natural language query systems that the context, in the form of a specific database, is given. The formal model defines a universe of discourse consisting of multiple contexts, each of which is represented by a database, which consists of a dictionary, a thesaurus, relations, columns, and values. A mechanism for identifying and selecting the appropriate context for a query and its implementation as a prototype are described. The integration of this mechanism into the general model of natural language query processing is indicated and implementational issues are discussed.

KEY WORDS AND PHRASES: context, database, dictionary, index, lexical analysis, natural language queries, semantics, synonyms, syntax, thesaurus.

Words have “meaning” when there is an association or a conditioned reflex connecting them with something other than themselves.
Bertrand Russell, Human Knowledge

## Introduction

ORGANIZATIONS OF EVERY SIZE AND IN EVERY FIELD OF ACTIVITY are becoming ever more dependent on computerized databases. The longer this trend continues, the more pressing the need to permit access to databases by naive users, that is, users with no expertise in databases and database management systems. The preferred solution to this problem is to provide user-friendly natural language interfaces so that users with no expertise at all are able to communicate their requests in the manner most congenial to them.

The pressure to provide natural language access arises from two sources. On the one hand, management would like employees to be able to access the data they need without recourse to the assistance of scarce and expensive data-processing professionals; natural language interfaces are a method to absolve the experts from having to help naive users. On the other hand, people find themselves increasingly required to interact with a variety of computer systems in a constantly expanding spectrum of activities, both at work and in their private capacities. They expect, and with some justification, that these systems become communicative to the point of conversing in the users' natural languages. Systems are expected to acquire human language and modes of communication, and not the other way around.

Much natural language research has focused on systems that permit access to formal databases by queries posed in natural language. Good examples of systems containing useful ideas or potential building blocks are BASEBALL [4], LUNAR [14], LIFER [6], PLANES [11], CHAT-80 [12], UNIX Consultant [13], QPROC [10], and TEAMS [5]. All of these systems to date have assumed a given context represented by a domain-specific database. By restricting their systems to a limited domain, developers simplify the linguistic processing problem. (For a discussion of this point, see [10] and [11].)

While domain dependence simplifies the developer's task, it places on the user the onus of knowing which database contains the information required. In an organization with tens, or even hundreds of databases, this is an unreasonable requirement. It is even more so with respect to the ever increasing variety of databases in the public domain. The basic premise of the research described here is that users should be able to submit their queries, in natural language, in an environment of multiple, heterogeneous databases and expect the system to find the database containing the answer. The intelligence of the system should be substituted for that of the user searching for a database appropriate to his or her query. Developers would also benefit from such a capability as they would not have to develop a separate, domain-independent interface for each database. A methodology for developing an architecture for managing distributed heterogeneous databases has been suggested by Sheth and Larson [8]. The present study actually undertakes the design and prototypical implementation of such a system.

The “bottom-up” approach adopted here consists of expanding existing methods for querying databases in natural language. While the universe of discourse studied is highly formalized, it is nevertheless characterized by numerous contexts. The authors believe that, in this environment, the elusive concept of context has been pinned down sufficiently to permit construction of systems for its processing and maintenance. Specifically, the universe is one that consists of a number of databases. Context is formally defined for this universe and a mechanism is suggested for processing natural language queries in it. The principal task of the mechanism is to choose the appropriate database from which to extract a reply to each query. As explicated later, a context in this universe of discourse is equivalent to a database.

## Structure of the System

THE PROBLEM OF IDENTIFYING THE DATABASE APPROPRIATE to answering a query is analogous to that of identifying a context for utterances in natural language in general. Although the contexts under discussion here are more formally structured than in general natural language, the analogy provides a useful conceptual framework. The words “database” and “context” are also used interchangeably in subsequent discussion.

Just as the words of a natural language sentence provide clues to the context in which the sentence was generated, so are the words of queries utilized in the system under discussion in order to identify the relevant databases.

Current natural language query systems designed to access a single database generally proceed by the following steps:

1. Eliminate unnecessary or redundant lexical terms so that only content words remain. For example, in the query "Who is president of the US?" the words "who," "is," "of," and "the" are not essential. The two words "president, US" contain the content of the query.

2. Analyze the syntactic structure of the query. This step frequently requires referral of semantic values to contextual knowledge, such as appropriate synonym lists, and cannot be performed unless a context has been identified. Herein lies the reason why all natural language systems to date have been context-bound.

3. If the query is semantically and syntactically acceptable, it is recast in a form suitable for database access and an answer is retrieved.

Examples of such systems are IRUS [2] and QUAN [9].

The principal contribution of the work described here is development of the additional knowledge required in the databases, and a mechanism utilizing that knowledge, in order to select the database most likely to contain the desired response in a universe of discourse consisting of multiple databases. Feasibility of the mechanism has been demonstrated in the form of a prototype.

The system described here performs the three steps outlined above, but is augmented to allow for multiple databases. The additional mechanism is realized in modules 3 and 4 of the six-module system consisting of:

1. query intake,

2. a lexical preprocessor,

3. the database identification mechanism,

4. a parser

5. a query formulation mechanism, and

6. the database access mechanism.

After unnecessary lexical elements have been removed by the lexical preprocessor, the semantic core of the query is analyzed by the context identification mechanism in order to determine the context—that is, to identify the appropriate database. Once a context has been identified, an attempt is made to validate the query for it, that is, to establish the relevance of the context. A priori validity is determined by the ability of the parser to correctly parse the sentence with the linguistic knowledge provided by the database. If successful, an attempt is made by the query formulation mechanism to state the query in terms suitable for database access. If unsuccessful, another context is evaluated, and so on, until either a database is successfully identified and a response retrieved or no candidate database remains to be tried.

Figure 1 exhibits the structure suggested in order to integrate numerous databases into a single universe of discourse in which databases are selected by queries. In addition to the databases themselves, the universe of discourse includes additional elements; these are a thesaurus and augmented dictionary for each database and context and parts of speech indices at the global level.

The knowledge found necessary in order to forge a single universe of discourse from multiple, disparate databases is as follows:

For individual databases:

1. a dictionary associated with each database,

2. a thesaurus associated with each database.

For the universe of discourse:

3. a context index to all databases constituting the universe of discourse,

4. a parts of speech index for words commonly appearing in queries in the universe of discourse but not generally associated with any particular database.

## A Formal Definition of Context

THIS SECTION PRESENTS A FORMAL DEFINITION OF THE STRUCTURE within which contexts for queries may be represented and identified. $^{1}$ The components of this structure are those exhibited graphically in figure 1.

Queries are submitted in a universe of discourse that consists of one or more contexts and indexes to those contexts. A context is defined as a database with associated dictionary and thesaurus:

```erlang
universe_of_discourse :: = {index, context | universe_of_discourse, context}
context :: = {data_base, dictionary, thesaurus}.
```

![](/api/attachments/7N7CM28V/fulltext/images/387dd6a63a9a34ffdf19f0f59eb3ea2613bb591b3bebea9db7d023ce2ce24289.jpg)  
Figure 1. Structure of Multiple Database Universe of Discourse

The index constitutes a knowledge base for the universe of discourse. This contains two types of information—an index of contexts in the universe of discourse, and an index of parts of speech for common words in English whose grammatical function is context-free. The first index consists of key words in the databases; the second index contains words not in the databases. For reasons of convenience and computational efficiency, each index is maintained as a separate relation. Examples of these indexes are presented in appendix A.

1. The index of contexts (c\_index) contains entries (c\_entry) each of which consists of a word (e.g., “born”) or a phrase (e.g., “item\_name”) which is either a column name, a relation name, or a database name in the universe of discourse being defined. This is followed by indication of the names of all the databases in which it appears in the role of a column, relation, or database name. A c\_entry may play several different roles in the same or in different databases. In addition, the index contains common synonyms for its entries. For example, if a database contains an employee relation, as in appendix C, the system should identify this as relevant to questions relating to workers. Thus, the question “Who works in the toy department?” should be recognized as equivalent to “Who are the employees in the toy department?” This is the reason “works” appears in the Context Index of our universe of discourse—appendix A1—even though it does not appear explicitly as a database, relation, or column name. $^{2}$

Given a database name, it is assumed that a physical database is uniquely and completely identified.

2. The index of parts of speech (p\_index) contains grammatical information for words not contained in the databases, but sufficiently common so that their inclusion is essential. This is especially true of verbs, which are not generally used as column, relation, or database names, but which are essential for processing many queries. Thus, each entry in the parts\_of\_speech\_index (p\_entry) contains a common word and its part of speech; multiple parts of speech for a single word are reflected in multiple entries. For example, in the Parts of Speech Index (appendix A2), the word “which” is defined as either a pronoun or a question word; “is” may be either a verb or superfluous. The decision process here is a manual one as described in note 2.

Formally:

```txt
index :: = {c_index,p_index}
c_index :: = {c_entry | c_index,c_entry}
p_index :: = {p_entry | p_index,p_entry}
c_entry :: = {col_name,database_name | rel_name,database_name |
    c_entry,database_name}
```

```txt
p_entry :: = {common_word, part_of_speech}.
data_base :: = {database_name | data_base, relation}
dictionary :: = {rel_list, col_list, val_list}.
```

Databases are assumed to be relational in form and, therefore, composed of relations over columns which contain values:

```txt
relation :: = {rel_name | relation, column}
column :: = {col_name | column, value}
value :: = {string | expression}.
```

All names throughout this definition consist of words, no matter what the names refer to. A word is a string. Thus,

```txt
database_name :: = {name}
rel_name :: = {name}
col_name :: = {name}
name :: = {word | name_word}
common_word :: = {word}
word :: = {string}
```

The dictionary component of a specific context consists of lists of relation definitions, column definitions, and value definitions $^{3}$ :

```txt
rel_list :: = {rel_def | rel_list, rel_def}
col_list :: = {col_def | col_list, col_def}
val_list :: = {val_def | val_list, val_def}
rel_def :: = {rel_name, RELATION, part_of_speech, ancestor}
col_def :: = {col_name, COLUMN, part_of_speech, ancestor, c_type, q_word}
val_def :: = string, VALUE, part_of_speech, ancestor}.
```

The relation, column, and value definitions (rel\_def, col\_def, and val\_def) all consist of an identifying string, a generic classifier—RELATION, COLUMN, or VALUE, the part of speech of the identifying string, and structural information in the form of an ancestor name. For relations and columns, the identifying strings, rel\_name and col\_name respectively, are the names of the relations and columns as defined in the database management system. In value definitions, the identifying string is the value of a data element—for example, a catalog number or an address—but not a numeric datum. Numeric data are not included in the dictionary as most numbers, especially those representing quantities, do not provide unique search keys; it makes little sense to list in the dictionary all numbers that happen to appear in the database. When numbers serve as codes for nonnumeric data such as dates or catalog numbers, there is no reason why they should not be defined as strings.

The function of the part\_of\_speech field is to permit comparison of the syntactic values of words obtained from query parses with the syntactic roles specified in the dictionary. Each database string is defined as being a unique part of speech:

$$
\text { part\_of\_speech }:: = \{\text { NOUN } \mid \text { VERB } \mid \text { ADJECTIVE } \mid \text { ADVERB } \mid \dots \}.
$$

As in natural language contexts, a given lexical value can have multiple grammatical functions in a database. It is assumed, however, that being in a given column in a given relation uniquely defines the syntactic value of a data item. For example, “black” can be either an adjective, a proper noun, or a verb. In the Stationery Vendors Database of appendix B it appears in two of these roles, in one case as an adjective in the color column and in the other as a proper noun in the president column.

The ancestor field provides the structure of the database by indicating the immediate ancestor of each value, column, and relation. Thus, the ancestors of relations are normally database names; relations are in turn generally ancestors for columns, which are themselves antecedents of values; the values in columns may, of course, be either strings or expressions. Ancestor is defined as:

$$
\text { ancestor }: := \{\text { database\_name } \mid \text { rel\_name } \mid \text { col\_name } \}.
$$

Column definitions contain two additional items—column type (c\_type) and query word (q\_word). The column type is either “string” or “expression”; as defined below, strings are character strings and expressions are numbers or algebraic formulae; which type is assigned to a column definition depends on the nature of the data contained in the column defined, and determines which types of operators may legitimately be applied to values in it. In the Department Store database dictionary of appendix C2, for example, the “item\_name” column is defined as containing string values while the “salary” column contains values which are expressions; from the database in appendix C1 it can be seen that in this case these are numbers. The query word field indicates the principal type of query to which the data contained in the column respond; the principal values of this field are WHO, WHEN, WHERE, WHAT, and WHICH. These entries assist in disambiguating queries, as will be demonstrated in the examples toward the end of the article. Formally,

c\_type :: = {string | expression}

$$
q \_ w o r d:: = \{\text { WHO } \mid \text { WHEN } \mid \text { WHERE } \mid \text { WHAT } \mid \text { WHICH } \mid \dots \}.
$$

The thesaurus component of a database is a file of values in the database indexed by their synonyms. Synonyms are strings that are either names or numeric values not in the database to which the thesaurus belongs, but synonymous to one or more values in it. Thus, if a query word cannot be identified directly as a database, relation, or column name, or as a value, a search can be made in the thesaurus to see whether it is a synonym for one or more terms which are defined in the database. A Thesaurus consists of thesaurus entries (t\_entries), each of which contains a synonym as identifier and one or more strings found in the database:

```txt
thesaurus :: = {t_entry | thesaurus,t_entry}
t_entry :: = {string,synonym | t_entry,synonym}
string :: = {string}
synonym :: = {string}.
```

Consider the thesaurus of appendix B3, for example. In it, “variegated” appears as a valid string that indexes, and so may be transformed into, the value “multiple” which appears in the “color” column of the “product” relation in the database (appendix B1).

Since database values may include numeric strings, this implies that a word might be a synonym for a number and vice-versa: for example, "4" can be a synonym for "four," and sometimes for "April." An example of a t\_entry from the Stationery Vendors Database in appendix B is the synonym "goods," which might be equivalent to "product" or "item," which are both in the database.

To round out the definitions, expressions, strings, and characters are defined conventionally:

```txt
expression :: = {number | alg(expression, expression)}
```

```txt
number :: = {INTEGER | REAL}
```

```txt
alg :: = {+ | - | * | /}
```

```txt
string :: = {character | string, character}.
```

Characters are defined as the letters of the alphabet, digits, and any generally used special characters.

A summary of the context definitions is exhibited in figure 2.

## Queries

HAVING DEFINED A UNIVERSE OF DISCOURSE, we now briefly define the queries that may be presented in it. Queries comprise words that may or may not be values in the universe of discourse. The order of words in a query is significant, so words are numbered in order of their appearance:

query :: = {word[1] | query, word[n]}

```txt
n ::= {2 ... N}
```

N :: = {number of words in query}.

All words are considered to be in English:

```txt
universe_of_discourse :: = {index | universe_of_discourse,context}

index :: = {c_index,p_index}
    c_index :: = {c_entry | c_index,c_entry}
    p_index :: = {p_entry | p_index,p_entry}
    c_entry :: = {col_name,database_name | rel_name,database_name |
    c-entry,database_name}
    p_entry :: = {common_word,part_of_speech}

context :: = {data_base,dictionary,thesaurus}.
    data_base :: = {database_name | data_base,relation}
    database_name :: = {name}
    relation :: = {rel_name | relation, column}
    rel_name :: = {name}
    column :: = {col_name | column, value}
    col_name :: = {name}
    value :: = {string | expression}

dictionary :: = {rel_list,col_list,val_list}
    rel_list :: = {rel_def | rel_list,rel_def}
    rel_def :: = {col_def | col_list,col_def}
    col_def :: = {col_name,COLUMN,part_of_speech,
    ancestor,c_type,q_word}
    part_of_speech :: = {NOUN | VERB | ADJECTIVE |
    ADVERB | ...}
    ancestor :: = {database_name | rel_name | col_name}
    c_type :: = {string | expression}
    q_word :: = {WHO | WHEN | WHERE | WHAT | WHICH | ...}
    expression :: = {number | alg(expression,expression)}
    number :: = {INTEGER | REAL}
    alg :: = {+ | - | * | /}
    val_list :: = {val_def | val_list,val_def}
    val_def :: = {string,VALUE,part_of_speech,ancestor}
    name :: = {word | name,_word}
    common_word :: = {word}
    word :: = {string}

thesaurus :: = {t_entry | thesaurus,t_entry}
    t_entry :: = {synonym,string | t_entry,string}
    synonym :: = {string}
    string :: = {character | string, character}
```  
Figure 2. Summary of Context Definition

$$
\supset \text { word }: \text { word } \in \{\text { english } \}.
$$

where {english} is the set of words of the English language. If the universe of discourse is expressed in any other natural language, this could of course be substituted for {english}, provided all alphabetic, lexical, semantic, and syntactic processes were also adapted accordingly.

Since the objective is to permit querying by naive users who are unaware of the overall database structure, or of the content and structure of individual databases, it is further assumed that

$$
\text { string }: := \text { string } \in \{\text { english } \},
$$

In other words, database elements are words or other common strings of the English language. This assumption can be relaxed by assuming that the synonym list for each database would translate query words into non-English database equivalents where necessary.

## Context Identification

IN THE STRUCTURE ASSUMED HERE FOR THE UNIVERSE OF DISCOURSE, identification of a database as an appropriate target for a query proceeds in two stages; first a candidate database is selected from the index. This selection utilizes only partial information from both the query and the index so that the validity of a chosen database for the query can only be tentatively established. Once a database has been chosen at this level, an attempt is made to validate it using all the information available in both the database and the query.

Databases are first selected by accessing the context index to the universe of discourse by the context words in the query. Each entry is indexed by a potential query word and points to databases in which that word is part of a column, relation, or database name, or a common synonym to one of these. A count is then made of the number of query words found in each database name retrieved by the procedure. The database that contains the largest number of query words (the highest hit count) is considered the best candidate for responding to the query, and an attempt is made to parse the query and to formulate an access path in that context. If successful, a response is retrieved and the procedure terminates. If no response is possible, the next most likely database is tried—that is, the database with the next highest query word count. This procedure continues until either a response is presented or until no candidate databases remain.

Typically, some of the names in an index, $\{name_{1} \ldots name_{m}\}$ , of a finite universe of discourse are a subset of the words of a query, $\{word_{1}, \ldots word_{n}\}$ . Each of the index names is associated with one or more databases. We may then define the sigma-count of a database for a query as

$$
\text { sigma - count } (D B) = \sum_ {i} u _ {D B} \left(q _ {i}\right)
$$

where u is a number; DB is a specific database; and $q_{i}$ is the ith word in the query under consideration.

Thus, sigma-count(DB) is the degree to which the words of the query are incorporated in the index entries for the database. Specifically:

$$
u _ {D B} \left(q _ {i}\right) = \left\{ \begin{array}{l l} 0 & \text {if} \exists \mathrm{word} _ {\mathrm{j}}: \mathrm{word} _ {\mathrm{j}} \text {name} (D B _ {i}) \\ 1 & \text {if} \exists \mathrm{word} _ {\mathrm{j}}: \mathrm{word} _ {\mathrm{j}} \notin \text {name} (D B _ {i}) \end{array} \right.
$$

where i or j are ordinal numbers over the range of the number of words in the sentence.

Thus, sigma-count(DB) is the number of words in both the query and the database. The relative sigma-count, sigma-count(DB/q), is the proportion of words from the query found in the database. This is computed as:

$$
\operatorname{sigma} - \operatorname{count} (D B / q) = \frac {\operatorname{sigma} - \operatorname{count} (D B)}{\operatorname{sigma} - \operatorname{count} (q)},
$$

where sigma-count(DB) is as computed above and sigma-count(q) is the number of words, N, in the query itself.

## Design and Design Considerations

THE TRANSFORMATION OF NATURAL LANGUAGE QUERIES INTO DATABASE access paths is an iterative process that is highly context-dependent. In a given context it encompasses the following steps (these steps are numbered in accordance with the modules performing them as outlined in the Structure of the System section):

## 1. Query intake (module 1 in the Structure section).

2. Lexical preprocessing: extracts content words, remembers interrogatives, and discards articles, pronouns, etc. (module 2 in the Structure section).

The reduction of queries to their contextually significant lexical components is performed by a lexical preprocessor that eliminates those words that are not likely to contribute to context identification. A preprocessor of this type, albeit with more limited functions, is incorporated in virtually all natural language query systems (see, e.g., [5, 6, 7]). It is necessary, however, to retain the interrogatives for later use in resolving ambiguities in the roles of query words.

3. Lexical analysis: determines which databases best fit the query, and ranks them accordingly (module 3 in the Structure section).

Given a query stripped to its essentials, a search is made in the index of the universe of discourse for that database that best fits the query. The goodness of fit of a database as a query context is determined by computing the hit count defined above and rank-ordering the databases accordingly.

4. Syntactic analysis: assigns parts of speech to query words, determines if the query parses, and if the parts of speech and query words correspond (module 4 in the Structure section).

Since the system is designed to answer queries, it will not permit general English-language inputs, but only queries. This reduces to a subset of English sentences the variety of inputs the system is prepared to accept. This restriction reduces the number of permissible syntactic structures and reduces the value of semantic elements whose purpose is to differentiate queries from other discourse. Interrogatives such as “who,” “when,” and “what” become redundant in their query establishment role since the prior assumption is that any input is a query. This simplifying assumption would not be valid, of course, for general-purpose natural language processors.

Interrogatives are also generally useless for initial context determination, as defined here, since words of this type would rarely serve as database values. They become necessary again, however, in evaluating the validity of a context; if a query formalization can apply in principal to more than one database, an interrogative may provide clues to distinguish between them. For example, the query “Who is president of Beautex?” becomes, after preprocessing:

## "president,Beautex."

In the Stationery Vendors database of appendix B, this may refer to either a person who heads the company or to an item model sold by the company; the interrogative “who” would indicate the first possibility whereas “how many” would point to the second. The preprocessing and later lexical and syntactic processing of queries is based on common-sense heuristic knowledge of query structures.

5. Query formalization (module 5 in the Structure section). An attempt is made to recast the query into a retrieval command in the context provided by the highest ranking database for which a valid parse is found. It should be stressed that this is the point at which the choice of context becomes crucial since formulating a query in the retrieval language depends on the lexical and syntactic values of query words in that context, and so is highly context-dependent. The lexical and syntactic values are contained in the database dictionary.

In the example under point 4 above, both the Stationery Vendors and Department Store databases (appendices B and C) would have hit counts of 1 and both would have to be entertained as possible contexts until one can be positively chosen; the initial choice between them would be essentially random. However, when the interrogative “who” is reintroduced in the parsing process, it is possible to identify that database in which “president” is a person.

Having successfully parsed the sentence, it is mapped into a retrieval command in the context under consideration, and submitted for retrieval from the database.

6. Database access (module 6 in the Structure section). Retrieval commands are executed by the relational database management system. The process is iterative in nature because attempts to overcome failure can be made at any stage by backing up one or more steps. Thus, if a syntactic analysis is unsuccessful, alternative parses can be tried. If that does not help, the system can back up to lexical analysis to look for alternative instances of query words or synonyms for them. If all this fails, it is possible to back up to the query input stage and to request that the query be rephrased.

In attempting to devise systems that can operate in multiple-context universes, it is necessary to decide to which point the processing may be context-free and from which point it becomes context-dependent.

Since the goal is to permit submission of any query in natural language, the query input stage must clearly be context independent. The preprocess stage depends on a heuristic knowledge of the general structure of queries and so is also context-independent.

At the level of assigning parts of speech, if the context is left open down to this point, it becomes necessary to consider all instances of query words, and synonyms for them, in the entire universe of discourse. This might well lead to an intractable combinatorial explosion in the number of possible query formulations that would then have to be evaluated for contextual candidacy. It would seem to be essential to enhance the probability of an early hit by performing context selection before this point.

Syntactic analysis might be considered as context-independent; this, however, would require the maintenance of a single parts-of-speech table for the entire universe of discourse. As a result, each word would potentially be open to multiple grammatical interpretations so that many possible parsings might be valid, with a consequent large number of possible contexts. As an example, assume the universe of discourse to include the Department Store databases of appendix C and also a database on members of households. Then consider the query,

"Who works in the household?"

After preprocessing, this becomes:

"works, household?"

Syntactically, this could be interpreted as either

(verb, noun) or (verb, adjective).

The first parse would represent a valid query to a household database about members of households who work. The second phrase represents a valid query to the Department Store database about those employed in the household department.

It would seem to be much more parsimonious to first determine the most likely context and to perform all analysis within its confines, which would offer far fewer alternatives than the entire universe of discourse. Thus, lexical analysis (number 3 above) is context-free. Once a context has been isolated by lexical analysis, any further processing, such as synonym search, is context-dependent. In syntactic analysis, the grammatical role of query words is localized to the given context, and any word may have different syntactic values in different contexts.

Viewed in the light of the preceding discussion, context selection may be seen as a search process. The earlier in the process context selection is performed, the more rapidly the search tree should be pruned and the less iteration should be necessary.

Figure 3 contains a pseudo-code formulation for a query-answering algorithm in a multiple-context universe of discourse based on the above design considerations.

## Implementation

![](/api/attachments/7N7CM28V/fulltext/images/106b4c66d00158f262ca15efec17cd4b488fb48c0a2a89f27d494e55ca273b3b.jpg)  
Figure 3. Multiple Database Query Response Algorithm

```vhdl
else failed;
assign part of speech;
match rules of syntax;
continue parsing;
until successfully parsed;
if failed
then find appearance in parts of speech
index;
if found
then assign part of speech;
match rules of syntax;
continue parsing;
else exit failed;
end;

begin {MAIN PROGRAM}
preprocess_query;
determine_context;
qnf; {if failed, try next data base}
end;
```  
Figure 3. Continued

the original design were uncovered during implementation and initial experimentation with the prototype. These are discussed in the Conclusions section.

Following are some brief notes on implementation of the six modules specified in previous sections. One of the principal building blocks for this system was QUAN [9]; this is a prototype natural language query system for a single database which employs QNF (Query Normal Form—[3]) as the formal language into which natural language queries are mapped. In adapting it to use in the current system, it was found necessary to intersperse it with elements of the additional modules. The lexical preprocessor remained largely unchanged; however, parsing is now deferred until after context selection, while query formalization follows checks for validity of the database for the query.

The following two brief examples are intended to illustrate operation of the prototype in a small universe of discourse consisting of three databases—a Stationery Vendors database, a Department Store database, and a U.S. President database. The Department Store database has stock, supplier, employee, and item relations. The Stationery Vendors database contains product and vendor relations, and the U.S. Presidents database comprises a vitae relation. Some sample data for this universe of discourse are presented in appendices A through D, which exhibit the apparatus for context determination—namely, the index, databases, dictionaries, and thesauri. Note the multiple use and duality of some of the values in the databases such as “president” which refers to presidents of the United States in the U.S. Presidents database, president of a stationery vending corporation in the Stationery Vendors database, and the name of a model of pencil in the Department Store database; similarly, “item” is a relation name in the Department Store database and a column name in the Stationery Vendors database.

Now consider the query,

## "Who works in the toy department"

Lexical preprocessing yields the following inferences from the sources indicated:

<table><tr><td>word</td><td>inference</td><td>source</td></tr><tr><td>who</td><td>question-word</td><td>parts of speech index</td></tr><tr><td>works</td><td>common verb</td><td>context index (DEPT)</td></tr><tr><td>in</td><td>preposition</td><td>parts of speech index</td></tr><tr><td>the</td><td>no content</td><td>parts of speech index</td></tr><tr><td>toy</td><td>???</td><td></td></tr><tr><td>department</td><td>keyword</td><td>context index (DEPT)</td></tr></table>

Thus, two words in the query identify the department store database (DEPT) as the relevant context, and do not identify any other. Having identified the relevant database, parsing then proceeds on the basis of the following information:

<table><tr><td>word</td><td>inference</td><td>source</td></tr><tr><td>who</td><td>question-word</td><td>parts of speech index</td></tr><tr><td>works</td><td>common verb</td><td>context index</td></tr><tr><td>in</td><td>preposition</td><td>parts of speech index</td></tr><tr><td>the</td><td>no content</td><td>parts of speech index</td></tr><tr><td>toy</td><td>noun</td><td>dictionary</td></tr><tr><td>department</td><td>keyword</td><td>context index</td></tr></table>

Note that the word department appears as a column name in two separate relations in the database—namely, stock and employee, and is identified as a noun in each. The relevant relation—employee—is identified thanks to the identification of works as a synonym for employee.

The process so far has yielded the content words:

$$
[ \text { who,works,in,toy,department } ].
$$

This parses as

$$
s (n p) (q (w h o)), v p (v (w o r k s), p p (p (i n), n p (c n (n (t o y), n (d e p a r m e n t)))))). ^ {4}
$$

The query is formulated, in PROLOG, as:

return(employee,[name],[[condition(employee,department,eq,toy)]],\_n)

yielding the responses [henry] and [nelson].

As the next example, consider the request,

$$
" \text { List   location   of   vp }"
$$

The syntax of this request is not standard, and it would be more natural to request locations of vps. The nonstandard syntax is necessary at present as the system does not yet possess a morphological component to establish the identity, in terms of grammatical function, of singular and plural. This is a technical rather than a substantive issue from the point of view of the problem under consideration.

Lexical preprocessing yields the following information:

<table><tr><td>word</td><td>inference</td><td>source</td></tr><tr><td>list</td><td>????</td><td></td></tr><tr><td>location</td><td>column name</td><td>context index (STAT)</td></tr><tr><td>of</td><td>preposition</td><td>parts of speech index</td></tr><tr><td>vp</td><td>column name</td><td>context index (STAT, PRES)</td></tr></table>

The Stationery Vendors and U.S. President databases are both offered here as potential contexts. However, since the first has a higher count of recognized content words, it is tried first.

Parsing is based on the following information:

<table><tr><td>word</td><td>inference</td><td>source</td></tr><tr><td>list</td><td>unnecessary</td><td>not found</td></tr><tr><td>location</td><td>noun</td><td>dictionary</td></tr><tr><td>of</td><td>preposition</td><td>parts of speech index</td></tr><tr><td>vp</td><td>noun</td><td>dictionary</td></tr></table>

This parses as

$$
\mathrm{s} (\mathrm{np} (\mathrm{n} (\text { location }), \mathrm{pp} (\mathrm{p} (\mathrm{of}), \mathrm{np} (\mathrm{n} (\mathrm{vp})))))
$$

yielding the formal query,

$$
\text { return } (\text { vendor }, [ \text { location } ], [ 0 ], \_ n).
$$

Finally, the answer is returned [hoboken], [new york].

## Conclusion

THE PROTOTYPE DESCRIBED HERE DEMONSTRATES THE FEASIBILITY of retrieving natural language queries in a small universe of discourse comprising multiple databases. Experience has shown, however, that a considerable amount of apparatus is necessary beyond that required for natural language retrieval in a single database.

The additional apparatus consists of a global knowledge base for the universe of discourse and a dictionary and thesaurus for each database. The global knowledge base contains an index of instantiations of words in databases and an index in parts of speech of common words in English.

Considerable manual effort was required to implement the additional information required concerning the databases. Initially, we anticipated that the thesauri would of necessity be constructed manually, but that it would be possible to construct the database index and part of the dictionaries automatically. However, incorporating common synonyms in the database index and dictionaries can only be done manually. Furthermore, most of the information in the dictionaries is context-dependent and must be entered manually. Even more seriously, the need for a parts-of-speech index for common words in English was not anticipated at all, and its need became apparent only in the course of experimentation. A mitigating factor for this last index is that it contains the most common words of the language, which are largely context-free; thus, it would need to be developed only once for all universes of discourse and should be transportable between various universes.

The most troubling implication of the work done so far is the difficulty of scaling up to a full-blown system containing many large databases. Some of the open questions requiring considerable additional research are as follows:

1. As the number of databases increases, so will the number of instances of content words appearing in numerous databases. This raises the question whether the hit count method adopted here to select a database will be able to differentiate between databases with sufficient accuracy.

2. As experience is gained with systems of this type, and as they grow, it will be constantly necessary to add entries to the various indexes, dictionaries, and thesauri. As pointed out above, most of this activity is manual in nature and therefore very costly. It would be beneficial to include machine learning facilities to the greatest extent possible.

3. As currently constituted, the prototype cannot handle quantifiers, inflections, or times, even though these should be perfectly valid in a natural language retrieval system. Incorporating appropriate capabilities will require considerable additional effort, although in this case it need only be expended once for all such systems.

4. Processing time will clearly increase significantly as the number and size of databases increase. No work has been done on this yet, but it could clearly affect the feasibility of systems of this type.

We therefore conclude that the a priori feasibility of natural language retrieval from multiple database universes of discourse has been established. Much additional research will be required before such systems can be implemented on a realistic scale.

## NOTES

1. The formalism used here to describe the structure of a universe of discourse employs the following symbols:

{} a set of components

As examples, consider the first two such descriptions:

(1) universe\_of\_discourse :: = {index, context | universe\_of\_discourse, context}. This should be read: a universe of discourse comprises at least an index AND a context; this minimum may be augmented (recursively) by additional contexts.

(2) index :: = {c\_index, p\_index}.

This reads: an index consists of a c\_index (content index) AND a p\_index (parts\_of\_speech index).

2. The question may validly be asked, "How are these synonyms decided?" In the current version of the prototype the decision was made for each entry on the basis of commonsense knowledge of language usage. In a full-scale system, the decision could be based on analysis of questions that failed to receive correct answers. In any case, the operation is a manual one. An alternative would be to provide access to a general thesaurus of English in addition to the specific thesauri for each of the contexts as at present.

3. It has been pointed out to us that these definitions imply the need to update the dictionary every time a new and unrecognized value is added. This is true, but not a serious problem as all value definitions can be updated automatically at run time. Only a restructuring of the database requires manual intervention. Taking in turn each of the columns of, for example, the dictionary in appendix B2:

a. The function values “column” and “relation” are set once at database initialization and would be changed only if the structure of the database is altered.

b. The part\_of\_speech is determined by the column in which a value appears; for example, any value in the "color" column must be an adjective while any value in the "item" column must be a noun. This would need to be built into the dictionary.

c. The value of the “ancestor” column is determined by the structure of the database and can be derived automatically at update time.

d. Only the column type (c\_type) and query word (q\_word) values need to be updated manually; but these relate to column names and so would rarely need to be updated.

4. Details of the parsing mechanism are available in [3]. The initials stand for parts of speech and syntactic constructs as follows: s = sentence; q = query word; v = verb; p = preposition; n = noun; np = noun phrase; vp = verb phrase; pp = preposition phrase; cn = common noun.

## REFERENCES

1. Allen, J. Natural Language Understanding. Menlo Park, CA: Benjamin/Cummings, 1987.

2. Bates, M., and Bobrow, R.J. Information retrieval using a transportable natural language interface. Proceedings of the Sixth Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. Bethesda, MD, June 1983.

3. Ein-Dor, P., and Spiegler, I. Answerability of database queries. Information Systems, 10, 3 (1985), 261–270.

4. Green, B.F.; Wolf, A.K.; Chomsky, C.; and Laughery, K. Baseball: an automatic question answerer. Proceedings of the Western Joint Computer Conference, 19 (1961), 219–224.

5. Grosz, B.J.; Appelt, D.; Martin, P.; and Pereira, F. TEAM: an experiment in the design of transportable natural-language interfaces. Artificial Intelligence, 32, 2 (1987), 172–244.

6. Hendrix, G.G. Human engineering for applied natural language processing. Proceedings of the International Joint Conference on Artificial Intelligence. Cambridge, MA: MIT Press, 1977.

7. Roberts, S.A., and Gahegan, M.N. Supporting the notion of context within a database environment for intelligent reporting and query optimization. European Journal of Information Systems, 1, 1 (1991), 13–22.

8. Sheth, A.P., and Larson, J.A. Federated database systems for managing distributed, heterogeneous, and autonomous databases. ACM Computing Surveys, 22, 3 (September 1990), 183–236.

9. Spiegler, I., and Elata, S. A priori analysis of natural language queries. Information Processing and Management, 24, 5 (1988), 619–631.

10. Wallace, M. Communicating with Databases in Natural Language. Ellis Horwood, 1984.

11. Waltz, D.L. An English language question answering system for a large relational database. Communications of the ACM, 21, 7 (July 1978), 526–539.

12. Warren, D.H.D., and Pereira, F.C.N. An efficient easily adaptable system for interpreting

natural language queries. Computational Linguistics, 8, 3–4 (1982), 110–122.

13. Wilensky, R. Talking to UNIX in English: an overview of an on-line UNIX consultant. AI Magazine, 5, 1 (Spring 1984), 29–39.

14. Woods, W.A. Progress in natural language understanding—an application to lunar geology. Proceedings of the National Computer Conference. Montvale, NJ: AFIPS Press, 1973.

## APPENDIX A: Indexes to Universe of Discourse

<table><tr><td rowspan="2">Word</td><td colspan="3">Database</td></tr><tr><td>Department Store</td><td>Stationery Vendors</td><td>U.S. Presidents</td></tr><tr><td>born</td><td></td><td></td><td>X</td></tr><tr><td>color</td><td>X</td><td>X</td><td></td></tr><tr><td>department</td><td>X</td><td></td><td></td></tr><tr><td>died</td><td></td><td></td><td>X</td></tr><tr><td>earns</td><td>X</td><td></td><td></td></tr><tr><td>elected</td><td></td><td></td><td>X</td></tr><tr><td>employee</td><td>X</td><td></td><td></td></tr><tr><td>governed</td><td></td><td></td><td>X</td></tr><tr><td>item</td><td>X</td><td></td><td></td></tr><tr><td>item_name</td><td>X</td><td></td><td></td></tr><tr><td>item_number</td><td>X</td><td></td><td></td></tr><tr><td>location</td><td></td><td>X</td><td></td></tr><tr><td>makes</td><td></td><td>X</td><td></td></tr><tr><td>manager</td><td>X</td><td></td><td></td></tr><tr><td>model</td><td>X</td><td>X</td><td></td></tr><tr><td>name</td><td>X</td><td>X</td><td>X</td></tr><tr><td>party</td><td></td><td></td><td>X</td></tr><tr><td>president</td><td></td><td>X</td><td>X</td></tr><tr><td>product</td><td></td><td>X</td><td></td></tr><tr><td>salary</td><td>X</td><td></td><td></td></tr><tr><td>sells</td><td>X</td><td>X</td><td></td></tr><tr><td>seller</td><td></td><td>X</td><td></td></tr><tr><td>stock</td><td>X</td><td></td><td></td></tr><tr><td>size</td><td>X</td><td></td><td></td></tr><tr><td>stationery</td><td></td><td>X</td><td></td></tr><tr><td>store</td><td>X</td><td></td><td></td></tr><tr><td>supplier</td><td>X</td><td>X</td><td></td></tr><tr><td>type</td><td>X</td><td></td><td></td></tr><tr><td>US</td><td>X</td><td></td><td></td></tr><tr><td>vendor</td><td></td><td>X</td><td></td></tr><tr><td>vp</td><td></td><td>X</td><td>X</td></tr><tr><td>vitae</td><td></td><td></td><td>X</td></tr><tr><td>works</td><td>X</td><td></td><td></td></tr></table>

A2. Parts-of-Speech Index

<table><tr><td>Common word</td><td>Part of speech</td></tr><tr><td>a</td><td>unnecessary</td></tr><tr><td>all</td><td>unnecessary</td></tr><tr><td>also</td><td>unnecessary</td></tr><tr><td>an</td><td>unnecessary</td></tr><tr><td>any</td><td>unnecessary</td></tr><tr><td>are</td><td>verb</td></tr><tr><td>are</td><td>unnecessary</td></tr><tr><td>as</td><td>preposition</td></tr><tr><td>at</td><td>preposition</td></tr><tr><td>average</td><td>noun</td></tr><tr><td>by</td><td>preposition</td></tr><tr><td>choose</td><td>verb</td></tr><tr><td>count</td><td>imperative</td></tr><tr><td>count</td><td>verb</td></tr><tr><td>different</td><td>comparative</td></tr><tr><td>for</td><td>preposition</td></tr><tr><td>from</td><td>preposition</td></tr><tr><td>has</td><td>verb</td></tr><tr><td>have</td><td>verb</td></tr><tr><td>his</td><td>pronoun</td></tr><tr><td>in</td><td>preposition</td></tr><tr><td>is</td><td>verb</td></tr><tr><td>is</td><td>unnecessary</td></tr><tr><td>less</td><td>comparative</td></tr><tr><td>look</td><td>verb</td></tr><tr><td>lower</td><td>comparative</td></tr><tr><td>maximum</td><td>noun</td></tr><tr><td>minimum</td><td>noun</td></tr><tr><td>more</td><td>comparative</td></tr><tr><td>number</td><td>noun</td></tr><tr><td>of</td><td>preposition</td></tr><tr><td>on</td><td>preposition</td></tr><tr><td>or</td><td>conjunction</td></tr><tr><td>other</td><td>comparative</td></tr><tr><td>same</td><td>comparative</td></tr><tr><td>some</td><td>unnecessary</td></tr><tr><td>than</td><td>preposition</td></tr><tr><td>that</td><td>pronoun</td></tr><tr><td>the</td><td>unnecessary</td></tr><tr><td>their</td><td>pronoun</td></tr><tr><td>there</td><td>unnecessary</td></tr><tr><td>was</td><td>unnecessary</td></tr><tr><td>what</td><td>question word</td></tr><tr><td>when</td><td>question word</td></tr><tr><td>where</td><td>question word</td></tr><tr><td>which</td><td>question word</td></tr><tr><td>which</td><td>pronoun</td></tr><tr><td>who</td><td>question word</td></tr><tr><td>who</td><td>pronoun</td></tr><tr><td>whose</td><td>pronoun</td></tr></table>

## APPENDIX B

## B1. Stationery Vendors Database

<table><tr><td>Product item</td><td>Model</td><td>Color</td><td>Vendor</td></tr><tr><td>pen</td><td>executive</td><td>maroon</td><td>Beautex</td></tr><tr><td>pen</td><td>president</td><td>green</td><td>Beautex</td></tr><tr><td>pen</td><td>scribe</td><td>black</td><td>Pencraft</td></tr><tr><td>pen</td><td>vp</td><td>yellow</td><td>Pencraft</td></tr><tr><td>pencil</td><td>hi_lite</td><td>black</td><td>Beautex</td></tr><tr><td>pencil</td><td>scribbler</td><td>grey</td><td>Flic</td></tr><tr><td>pencil</td><td>computa</td><td>grey</td><td>Flic</td></tr><tr><td>pencil</td><td>rainbow</td><td>multiple</td><td>Flic</td></tr><tr><td>ink</td><td>freeflo</td><td>red</td><td>Pencraft</td></tr><tr><td>ink</td><td>freeflo</td><td>black</td><td>Pencraft</td></tr><tr><td>ink</td><td>freeflo</td><td>green</td><td>Pencraft</td></tr><tr><td>Vendor name</td><td>President</td><td>Vp</td><td>Location</td></tr><tr><td>Beautex</td><td>Anderson</td><td>White</td><td>New_York</td></tr><tr><td>Chemco</td><td>Black</td><td>Morton</td><td>Hoboken</td></tr><tr><td>Flic</td><td>Green</td><td>Smith</td><td>New_York</td></tr><tr><td>Pencraft</td><td>Adams</td><td>Schubert</td><td>Hoboken</td></tr></table>

B2. Stationery Vendors Database: Dictionary

<table><tr><td>Name</td><td>Function</td><td>part_of_speech</td><td>ancestor</td><td>c_type</td><td>q_word</td></tr><tr><td>adams</td><td>VALUE</td><td>PROPER NOUN</td><td>president</td><td></td><td></td></tr><tr><td>anderson</td><td>VALUE</td><td>PROPER NOUN</td><td>president</td><td></td><td></td></tr><tr><td>beautex</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>beautex</td><td>VALUE</td><td>PROPER NOUN</td><td>vendor</td><td></td><td></td></tr><tr><td>black</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>black</td><td>VALUE</td><td>PROPER NOUN</td><td>president</td><td></td><td></td></tr><tr><td>chemco</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>color</td><td>COLUMN</td><td>NOUN</td><td>product</td><td>STRING</td><td>WHAT</td></tr><tr><td>computa</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>executive</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>flic</td><td>VALUE</td><td>PROPER NOUN</td><td>vendor</td><td></td><td></td></tr><tr><td>flic</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>freeflo</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>green</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>green</td><td>VALUE</td><td>PROPER NOUN</td><td>president</td><td></td><td></td></tr><tr><td>grey</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>hi-lite</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>hoboken</td><td>VALUE</td><td>PROPER NOUN</td><td>location</td><td></td><td></td></tr><tr><td>ink</td><td>VALUE</td><td>NOUN</td><td>item</td><td></td><td></td></tr><tr><td>item</td><td>COLUMN</td><td>NOUN</td><td>product</td><td>STRING</td><td>WHICH</td></tr><tr><td>location</td><td>COLUMN</td><td>ADVERB</td><td>vendor</td><td>STRING</td><td>WHERE</td></tr><tr><td>maroon</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>model</td><td>COLUMN</td><td>NOUN</td><td>product</td><td>STRING</td><td>WHICH</td></tr><tr><td>morton</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>multiple</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>name</td><td>COLUMN</td><td>NOUN</td><td>vendor</td><td>STRING</td><td>WHICH</td></tr><tr><td>new york</td><td>VALUE</td><td>PROPER NOUN</td><td>location</td><td></td><td></td></tr><tr><td>pen</td><td>VALUE</td><td>NOUN</td><td>item</td><td></td><td></td></tr><tr><td>pencil</td><td>VALUE</td><td>NOUN</td><td>item</td><td></td><td></td></tr><tr><td>pencraft</td><td>VALUE</td><td>PROPER NOUN</td><td>vendor</td><td></td><td></td></tr><tr><td>pencraft</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>president</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>president</td><td>COLUMN</td><td>NOUN</td><td>vendor</td><td>STRING</td><td>WHO</td></tr><tr><td>product</td><td>RELATION</td><td>NOUN</td><td></td><td></td><td></td></tr><tr><td>rainbow</td><td>VALUE</td><td>ADJECTIVE</td><td>model</td><td></td><td></td></tr><tr><td>red</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>schubert</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>scribbler</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>scribe</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>smith</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>vendor</td><td>RELATION</td><td>NOUN</td><td></td><td></td><td></td></tr><tr><td>vendor</td><td>COLUMN</td><td>NOUN</td><td>product</td><td>STRING</td><td>WHICH</td></tr><tr><td>vp</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>vp</td><td>COLUMN</td><td>NOUN</td><td>vendor</td><td>STRING</td><td>WHO</td></tr><tr><td>white</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>yellow</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr></table>

B3. Stationery Vendors Database: Thesaurus

<table><tr><td>String</td><td>Synonym list</td></tr><tr><td>ballpoint</td><td>pen</td></tr><tr><td>CEO</td><td>president</td></tr><tr><td>chief executive</td><td>president</td></tr><tr><td>city</td><td>location</td></tr><tr><td>company</td><td>vendor</td></tr><tr><td>corporation</td><td>vendor</td></tr><tr><td>executive</td><td>president, vp</td></tr><tr><td>goods</td><td>products,—items</td></tr><tr><td>head</td><td>president</td></tr><tr><td>hue</td><td>color</td></tr><tr><td>india_ink</td><td>ink</td></tr><tr><td>item</td><td>product</td></tr><tr><td>ivory</td><td>white</td></tr><tr><td>make</td><td>model</td></tr><tr><td>manager</td><td>president, vp</td></tr><tr><td>multi_colored</td><td>multiple</td></tr><tr><td>number_two</td><td>vp</td></tr><tr><td>ny</td><td>new_york</td></tr><tr><td>ochre</td><td>yellow</td></tr><tr><td>off_white</td><td>white</td></tr><tr><td>paper_goods</td><td>stationery</td></tr><tr><td>place</td><td>location</td></tr><tr><td>rainbow</td><td>multiple</td></tr><tr><td>saffron</td><td>yellow</td></tr><tr><td>seller</td><td>vendor</td></tr><tr><td>shade</td><td>color</td></tr><tr><td>supplier</td><td>vendor</td></tr><tr><td>tint</td><td>color</td></tr><tr><td>town</td><td>location</td></tr><tr><td>type</td><td>model</td></tr><tr><td>variegated</td><td>multiple</td></tr><tr><td>version</td><td>model</td></tr><tr><td>vice_president</td><td>vp</td></tr><tr><td>wares</td><td>products,—items</td></tr><tr><td>whitish</td><td>white</td></tr><tr><td>writing materials</td><td>ink, pen, pencil, stationery</td></tr><tr><td>yellowish</td><td>yellow</td></tr></table>

## APPENDIX C

## C1. Department Store Database

<table><tr><td colspan="2">Stock</td></tr><tr><td>Department</td><td>item_number</td></tr><tr><td>cosmetics</td><td>132</td></tr><tr><td>hardware</td><td>111</td></tr><tr><td>hardware</td><td>141</td></tr><tr><td>household</td><td>121</td></tr><tr><td>household</td><td>311</td></tr><tr><td>stationery</td><td>122</td></tr><tr><td>stationery</td><td>131</td></tr><tr><td>toy</td><td>122</td></tr><tr><td>toy</td><td>133</td></tr></table>

Supplier

<table><tr><td>item_number</td><td>supplier</td></tr><tr><td>111</td><td>Chemco</td></tr><tr><td>121</td><td>Beautex</td></tr><tr><td>122</td><td>Pencraft</td></tr><tr><td>131</td><td>Pencraft</td></tr><tr><td>132</td><td>Flic</td></tr><tr><td>133</td><td>Flit</td></tr><tr><td>311</td><td>Chemco</td></tr></table>

Employee

<table><tr><td>name</td><td>salary</td><td>manager</td><td>department</td></tr><tr><td>Henry</td><td>9,000</td><td>Smith</td><td>toy</td></tr><tr><td>Lewis</td><td>12,000</td><td>Long</td><td>stationery</td></tr><tr><td>Long</td><td>7,000</td><td>Morgan</td><td>cosmetics</td></tr><tr><td>Morgan</td><td>10,000</td><td>Lee</td><td>cosmetics</td></tr></table>

<table><tr><td>Murphy</td><td>8,000</td><td>Smith</td><td>Household</td></tr><tr><td>Nelson</td><td>6,000</td><td>Murphy</td><td>toy</td></tr></table>

Item

<table><tr><td>item_number</td><td>item_name</td><td>model</td><td>color</td><td>size</td></tr><tr><td>111</td><td>ink</td><td>ivory</td><td>white</td><td>small</td></tr><tr><td>121</td><td>pen</td><td>president</td><td>green</td><td>small</td></tr><tr><td>122</td><td>pen</td><td>scribe</td><td>black</td><td>large</td></tr><tr><td>132</td><td>pencil</td><td>carmen</td><td>red</td><td>small</td></tr></table>

## C2. Department Store Database: Dictionary

<table><tr><td>Name</td><td>Function</td><td>Part of speech</td><td>ancestor</td><td>c_type</td><td>answers</td></tr><tr><td>beautex</td><td>VALUE</td><td>PROPER NOUN</td><td>supplier</td><td></td><td></td></tr><tr><td>black</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>carmen</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>chemco</td><td>VALUE</td><td>PROPER NOUN</td><td>supplier</td><td></td><td></td></tr><tr><td>color</td><td>COLUMN</td><td>NOUN</td><td>item</td><td>STRING</td><td>WHAT</td></tr><tr><td>cosmetics</td><td>VALUE</td><td>ADJECTIVE</td><td>department</td><td></td><td></td></tr><tr><td>department</td><td>COLUMN</td><td>NOUN</td><td>stock</td><td>STRING</td><td>WHICH</td></tr><tr><td>department</td><td>COLUMN</td><td>NOUN</td><td>employee</td><td>STRING</td><td>WHICH</td></tr><tr><td>employee</td><td>RELATION</td><td>NOUN</td><td></td><td></td><td></td></tr><tr><td>flic</td><td>VALUE</td><td>PROPER NOUN</td><td>supplier</td><td></td><td></td></tr><tr><td>green</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>hardware</td><td>VALUE</td><td>ADJECTIVE</td><td>department</td><td></td><td></td></tr><tr><td>henry</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>household</td><td>VALUE</td><td>ADJECTIVE</td><td>department</td><td></td><td></td></tr><tr><td>item</td><td>RELATION</td><td>NOUN</td><td></td><td></td><td></td></tr><tr><td>item_name</td><td>COLUMN</td><td>NOUN</td><td>item</td><td>STRING</td><td>WHAT</td></tr><tr><td>item_number</td><td>COLUMN</td><td>NOUN</td><td>stock</td><td>STRING</td><td>WHICH</td></tr><tr><td>item_number</td><td>COLUMN</td><td>NOUN</td><td>supplier</td><td>STRING</td><td>WHICH</td></tr><tr><td>item_number</td><td>COLUMN</td><td>NOUN</td><td>item</td><td>STRING</td><td>WHICH</td></tr><tr><td>ivory</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>large</td><td>VALUE</td><td>ADJECTIVE</td><td>size</td><td></td><td></td></tr><tr><td>lee</td><td>VALUE</td><td>PROPER NOUN</td><td>manager</td><td></td><td></td></tr><tr><td>lewis</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>long</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>long</td><td>VALUE</td><td>PROPER NOUN</td><td>manager</td><td></td><td></td></tr><tr><td>manager</td><td>COLUMN</td><td>NOUN</td><td>employee</td><td>STRING</td><td>WHO</td></tr><tr><td>medium</td><td>VALUE</td><td>ADJECTIVE</td><td>size</td><td></td><td></td></tr><tr><td>model</td><td>COLUMN</td><td>NOUN</td><td>item</td><td>STRING</td><td>WHICH</td></tr><tr><td>morgan</td><td>VALUE</td><td>PROPER NOUN</td><td>manager</td><td></td><td></td></tr><tr><td>morgan</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>murphy</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>murphy</td><td>VALUE</td><td>PROPER NOUN</td><td>manager</td><td></td><td></td></tr><tr><td>name</td><td>COLUMN</td><td>NOUN</td><td>employee</td><td>STRING</td><td>WHO</td></tr><tr><td>nelson</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>paper</td><td>VALUE</td><td>NOUN</td><td>item_name</td><td></td><td></td></tr><tr><td>pen</td><td>VALUE</td><td>NOUN</td><td>item_name</td><td></td><td></td></tr><tr><td>pencil</td><td>VALUE</td><td>NOUN</td><td>item_name</td><td></td><td></td></tr><tr><td>pencraft</td><td>VALUE</td><td>PROPER NOUN</td><td>supplier</td><td></td><td></td></tr><tr><td>president</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>red</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr><tr><td>salary</td><td>COLUMN</td><td>NOUN</td><td>employee</td><td>EXPRES- SION</td><td>.</td></tr><tr><td>scribe</td><td>VALUE</td><td>PROPER NOUN</td><td>model</td><td></td><td></td></tr><tr><td>size</td><td>COLUMN</td><td>NOUN</td><td>item</td><td>STRING</td><td>WHAT</td></tr><tr><td>small</td><td>VALUE</td><td>ADJECTIVE</td><td>size</td><td></td><td></td></tr><tr><td>smith</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>smith</td><td>VALUE</td><td>PROPER NOUN</td><td>manager</td><td></td><td></td></tr><tr><td>stationery</td><td>VALUE</td><td>ADJECTIVE</td><td>department</td><td></td><td></td></tr><tr><td>stock</td><td>RELATION</td><td>VERB</td><td></td><td></td><td></td></tr><tr><td>supplier</td><td>RELATION</td><td>NOUN</td><td></td><td></td><td></td></tr><tr><td>supplier</td><td>COLUMN</td><td>NOUN</td><td>supplier</td><td>STRING</td><td>WHO</td></tr><tr><td>toy</td><td>VALUE</td><td>NOUN</td><td>department</td><td></td><td></td></tr><tr><td>white</td><td>VALUE</td><td>ADJECTIVE</td><td>color</td><td></td><td></td></tr></table>

C3. Department Store Database: Thesaurus

<table><tr><td>String</td><td>Synonym list</td></tr><tr><td>earn</td><td>earns</td></tr><tr><td>employees</td><td>employee</td></tr><tr><td>makes</td><td>earns</td></tr><tr><td>names</td><td>name</td></tr><tr><td>sell</td><td>sells</td></tr><tr><td>supply</td><td>supplies</td></tr><tr><td>toys</td><td>toy</td></tr><tr><td>work</td><td>works</td></tr><tr><td>worker</td><td>employee</td></tr><tr><td>workers</td><td>employee</td></tr></table>

## APPENDIX D

D1. U.S. Presidents Database

<table><tr><td colspan="6">Vitae</td></tr><tr><td>Name</td><td>Born</td><td>Died</td><td>Elected</td><td>VP</td><td>Party</td></tr><tr><td>Washington_G.</td><td>1732</td><td>1799</td><td>1789</td><td>Adams</td><td>n.a.</td></tr><tr><td>Washington_G.</td><td>1732</td><td>1799</td><td>1792</td><td>Adams</td><td>Federalist</td></tr><tr><td>Adams_J._Q.</td><td>1735</td><td>1826</td><td>1797</td><td>Jefferson</td><td>Federalist</td></tr><tr><td>Harrison_W._H.</td><td>1833</td><td>1901</td><td>1888</td><td>Morton</td><td>Republican</td></tr><tr><td>Roosevelt_T.</td><td>1858</td><td>1919</td><td>1908</td><td>Fairbanks</td><td>Republican</td></tr><tr><td>Roosevelt_F._D.</td><td>1882</td><td>1945</td><td>1936</td><td>Garner</td><td>Democratic</td></tr><tr><td>Roosevelt_F._D.</td><td>1882</td><td>1945</td><td>1940</td><td>Garner</td><td>Democratic</td></tr><tr><td>Roosevelt_F._D.</td><td>1882</td><td>1945</td><td>1944</td><td>Wallace</td><td>Democratic</td></tr><tr><td>Roosevelt_F._D.</td><td>1882</td><td>1945</td><td>1944</td><td>Truman</td><td>Democratic</td></tr></table>

D2. U.S. Presidents Database: Dictionary

<table><tr><td>Name</td><td>Function</td><td>part_of_speech</td><td>ancestor</td><td>c_type</td><td>q_word</td></tr><tr><td>Adams</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>Adams</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>born</td><td>COLUMN</td><td>VERB</td><td>vitae</td><td>EXPRES-SION</td><td>WHEN</td></tr><tr><td>Democratic</td><td>VALUE</td><td>ADJECTIVE</td><td>party</td><td></td><td></td></tr><tr><td>died</td><td>COLUMN</td><td>VERB</td><td>vitae</td><td>EXPRES-SION</td><td>WHEN</td></tr><tr><td>elected</td><td>COLUMN</td><td>VERB</td><td>vitae</td><td>EXPRES-SION</td><td>WHEN</td></tr><tr><td>initials</td><td>COLUMN</td><td>PROPER NOUN</td><td>vitae</td><td>STRING</td><td>WHO</td></tr><tr><td>Fairbanks</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>Federalist</td><td>VALUE</td><td>ADJECTIVE</td><td>party</td><td></td><td></td></tr><tr><td>Garner</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>HARRISON</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>Jefferson</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>Morton</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>n.a.</td><td>VALUE</td><td>ADJECTIVE</td><td>party</td><td></td><td></td></tr><tr><td>name</td><td>COLUMN</td><td>NOUN</td><td>vitae</td><td>STRING</td><td>WHO</td></tr><tr><td>party</td><td>COLUMN</td><td>NOUN</td><td>vitae</td><td>STRING</td><td>WHICH</td></tr><tr><td>Republican</td><td>VALUE</td><td>ADJECTIVE</td><td>party</td><td></td><td></td></tr><tr><td>Roosevelt</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr><tr><td>Truman</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>vp</td><td>COLUMN</td><td>NOUN</td><td>vitae</td><td>STRING WHO</td><td></td></tr><tr><td>vitae</td><td>RELATION</td><td>NOUN</td><td></td><td></td><td></td></tr><tr><td>Wallace</td><td>VALUE</td><td>PROPER NOUN</td><td>vp</td><td></td><td></td></tr><tr><td>Washington</td><td>VALUE</td><td>PROPER NOUN</td><td>name</td><td></td><td></td></tr></table>

D3. U.S. Presidents Database: Thesaurus

<table><tr><td>String</td><td>Synonym list</td></tr><tr><td>biography</td><td>vitae</td></tr><tr><td>birth_date</td><td>born</td></tr><tr><td>CEO</td><td>president</td></tr><tr><td>chief executive</td><td>president</td></tr><tr><td>commander_in_chief</td><td>president</td></tr><tr><td>FDR</td><td>Roosevelt_F_D</td></tr><tr><td>GOP</td><td>Republican</td></tr><tr><td>head</td><td>president</td></tr><tr><td>number two</td><td>vp</td></tr><tr><td>passed_away</td><td>died</td></tr><tr><td>pick</td><td>elect</td></tr><tr><td>president</td><td>name</td></tr><tr><td>vice_president</td><td>vp</td></tr></table>
