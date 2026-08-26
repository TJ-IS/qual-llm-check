---
otero_id: 21321
otero_key: "DETNBKY5"
title: "The economics of natural language interfaces: natural language processing technology as a scarce resource"
authors: "Sumali J. Conlon; John R. Conlon; Tabitha L. James"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00096-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

Short communication

# The economics of natural language interfaces: natural language processing technology as a scarce resource

Sumali J. Conlon<sup>a,</sup>\*, John R. Conlon<sup>b</sup>, Tabitha L. James<sup>c</sup>

<sup>a</sup> Department of MIS, School of Business Administration, University of Mississippi, University, MS 38677, USA

<sup>b</sup> Department of Economics, College of Liberal Arts, University of Mississippi, University, MS 38677, USA

<sup>c</sup> Department of Business Information Technology, Pamplin College of Business, Virginia Polytechnic Institute and State University, USA

Received 1 April 2000; accepted 1 October 2002 Available online 5 August 2003

## Abstract

This paper discusses appropriate application areas for natural language interfaces (NLIs) to databases. This requires comparing NLIs with competing approaches, including other user-friendly interfaces, and training of users with less userfriendly interfaces. Also, since NLI technology is still limited, users may need to learn how to use NLIs themselves. This suggests that NLI popularity may snowball at some point, as users become familiar with NLIs. We use a simple prototype NLI to illustrate when NLIs can achieve flexibility unattainable by simpler interfaces. Currently existing commercial NLIs and application-specific customization are also discussed. © 2003 E1sevier B V. All rights reserved

Keywords: Natural language interfaces; Database management systems; Network externalities; Economics of information systems

## 1. Introduction

Natural language interfaces (NLIs) have become increasingly sophisticated in recent years [1,4,5,13, 15,19,32,41,43,46]. However, practical application of these technologies has remained limited. This paper asks why applications have not been more widespread and also what approaches can potentially make NLI technologies more applicable in the future.

One way to understand the problem is to ask whether NLI applications have been uncommon (a)

because it is difficult to build a useful NLI or (b) because it is easy to get along without an NLI [35, p. 694]. A determination of the appropriate application areas for NLIs therefore requires a careful analysis of substitutes for NLIs.

There are two major alternatives to an NLI. The most obvious is some other type of user-friendly interface, such as a menu or report-based system. A second, less obvious alternative is the training of potential users to handle less user-friendly interfaces, such as spreadsheets, statistical packages, or programming languages such as $\mathrm { C } ^ { + + }$ . This suggests that NLIs are more appropriate if it is difficult to train the users to work with less user-friendly systems [1,13]. Also, since NLI technology is still limited, training in how to use limited NLIs themselves may substitute for better NLI technology. NLI popularity may therefore snowball at some point, as users become more comfortable with NLIs, so more organizations implement NLIs, and so on. Indeed, it is possible that current technology would become very successful if users were sufficiently familiar with existing NLIs.

On the other hand, an NLI is more expensive to develop than a menu or form-based interface. This cost has two components: the up-front cost of creating a sophisticated natural language understanding system and the organization or application-specific costs of customizing the NLI for the application areas needed by actual users.

A basic natural language understanding system represents essentially a sunk cost. Once a basic system is developed, it can be reproduced at very low cost. Unfortunately, it is so difficult to build a sophisticated system, that all existing systems still face serious limitations (though see Section 8 on some systems which are already commercially available). These limitations may be partly circumvented by customizing systems for more narrow application domains. This, however, involves significant application-specific costs.

Moreover, even a carefully customized system will be ineffective unless the problem domain is sufficiently well structured. However, if the domain is very well structured, other user-friendly interfaces, such as menu bases, may be more cost effective. Thus, the domain should be well structured, but not too well structured. We examine a typical prototype NLI (one currently under construction at the University of Mississippi), to examine whether an NLI can achieve levels of flexibility that are unattainable by menu, form, or report-based systems.

Section 2 considers an NLI as a substitute for user training in more difficult interfaces. It also considers the users’ need to learn how to use NLIs themselves. Section 3 examines implications of NLI cost structure. Section 4 shows how the recursive structure of natural languages, such as English, facilitate NLI technology. Section 5 describes a prototype NLI currently under construction at the University of Mississippi, and Section 6 uses this system to illustrate the relative challenges faced by an NLI versus simpler interface technologies. Section 7 considers customization of NLIs to a specific organization’s needs and also considers ways to economize on organization-specific customization costs. Section 8 discusses existing commercial NLIs, focusing on two: ELF and Easy-Ask, and Section 9 concludes.

## 2. The substitution between an NLI and user training

An NLI allows an organization to substitute a sophisticated interface for the training of the users of the system. Thus, an NLI is more appropriate if it is difficult to train the users to work with less userfriendly systems, such as spreadsheets, statistical packages, or programming languages like $\mathrm { C } ^ { + + }$ or SQL. This is discussed in Section 2.1. On the other hand, existing NLIs are highly imperfect. Thus, user training in how to work around the limitations of NLIs themselves may also substitute for better NLI technology, as discussed in Section 2.2.

## 2.1. Factors affecting user training costs

Five considerations affect users’ training costs: (1) the number of potential users, (2) the opportunity cost of the time of these users, (3) the complexity of the tasks these users perform with the system, (4) the prior skills of these users, and (5) the users’ relation to the organization.

First, a sophisticated interface such as an NLI is more appropriate, the larger the number of potential users. If a system has few users, then it may be cheaper to train these users to work with a less userfriendly interface. On the other hand, with many users to train, an NLI can reduce these training costs [1,13]. The same effect occurs if there is a high rate of turnover among employees using the system.

Second, the opportunity cost of the users’ time affects training costs. Training takes time and effort. If users are upper level executives, for example, then it may be a costly waste of their time to train them in less user-friendly interfaces. This would make NLIs more appropriate. In fact, this factor may often override the first consideration above. That is, it may make more sense to adopt an NLI for a few upper level executives as compared to many lower level employees, because of the higher cost of time for the upper level executives.

Third, with simple tasks, users should need very little training to work with menu-based interfaces, say. For example, hotel clerks need to work with a limited set of forms to make reservations, check in guests, etc. This requires very little training. By contrast, a mid or upper-level manager may need flexible access to the database in order to prepare ad hoc reports, and so, may require more extensive training. Of course, the sophistication of an application should also increase the cost of building an NLI (see Section 6).

Fourth, if users are highly trained, then their training will frequently include skill in using the computer software supporting their specialization. For example, users doing sophisticated statistical analysis will usually know how to use statistical packages such as SAS or SPSS. These employees will therefore not need an NLI to communicate with the system. However, employees with less technical training, such as some upper level managers, may need an NLI to access the statistical models developed by the employees with more technical training.

Fifth, if the user is not a formal member of an organization, then it may be difficult for the organization to train the user to work with an interface. This is because learning how to use a non-user-friendly interface is a relation-specific investment on the part of the user. If the user is not a member of the organization, then her relation with the organization is less stable, so she has less incentive to incur such relation-specific costs [22,44].

This becomes especially important in web-based applications. For example, an NLI might be valuable in business to consumer (B2C) web pages. Since customers have brief and sporadic relations with the firm, they will not learn how to use an interface unless it is very user-friendly. This problem is aggravated by the large number of customers that access a typical web page, and the lack of prior technical training of the typical customer.

A second example may be in web-based applications aimed at business to business (B2B) communication across firms in the supply chain. For example, suppose that a firm wants to allow executives from firms upstream or downstream in the supply chain to access information from the firm’s database through the web, say (subject to appropriate security constraints). Then, since supply chain partners are not formal members of the organization, they may be less willing to learn how to use a non-user-friendly interface. An NLI may therefore be more appropriate. An NLI might also be useful for two of the other reasons discussed above: the number of such users may be large, with nontrivial turnover, and the opportunity cost of these users’ time may be high if these users include higher level executives of the supply chain partners’ firms.

In summary, an NLI will be more appropriate the larger the number of potential users, the higher the opportunity cost of the time of these users, the less computer-related specialized training these users already have, and the more tenuous users’ relations to the firm. The complexity of the task will also increase user training costs, but there may be an offsetting increase in the cost of building an NLI sophisticated enough to handle the task.

## 2.2. Learning how to use an NLI, and implications for network externalities

The discussion so far has ignored the costs of learning how to use a natural language interface. However, these costs may be nontrivial, and also may have interesting implications. Existing NLIs can handle only a limited range of natural language input, and it is generally not obvious to the user what queries the system will and will not understand. This confusion can take two forms [5]. First, users might be overly optimistic about an NLIs capabilities, and become frustrated as NLIs fail to respond as expected to complicated queries. Alternatively, users may be overly pessimistic, so they fail to explore the full range of the NLIs capabilities. Thus, users generally need some practice with an NLI before they become familiar with the range of natural language queries the system can handle.

For users who are members of an organization, formal training may therefore be useful. For example, system administrators might create a set of sample questions, covering the users’ most frequent query types. Then, as users become more confident with the system, they might be encouraged to explore the full capabilities of the system, with oversight from the technical support staff (see Section 8.1 below for an example involving the commercial NLI ELF).

For users who are not members of the organization, training may be more difficult. One challenge may be presented by B2C Internet applications. Internet retailers cannot expect customers to devote much effort to learning how to use their NLIs. Users may therefore fail to take full advantage of the NLI. For example, according to Richard Wood of the e-commerce NLI firm EasyAsk, customers tend to type very short queries into the EasyAsk NLI, even though EasyAsk can handle longer, more precise queries. Thus, customers must undergo a self-training period before they learn how to make full use of a B2C NLI.

This would seem to create a major problem for B2C NLI use. However, if the NLIs of different retailers have similar linguistic capabilities, then customer experience with one retailer’s NLI may have positive spillovers to other retailers’ NLIs. That is, B2C NLIs may generate positive network externalities [37,38, Chapter 10,39].

There are at least five possible ways to cope with these externalities. First, an Internet retailer may take advantage of these externalities by adopting an NLI similar to the NLIs of other retailers. Customers who have learned how to use other retailers’ NLIs will then be able to use this new retailer’s NLI more effectively. For example, a retailer may adapt the NLI system, which is most popular among other Internet retailers.

Second, brand naming by NLI developers themselves may facilitate this process. For example, both Talbots and Bombay feature the EasyAsk logo on their product search web pages. Thus, users familiar with other web pages incorporating the EasyAsk NLI will be better able to use the NLIs on Talbots and Bombay’s web pages. However, other EasyAsk customers, such as Lands’ End and Coldwater Creek, do not currently display the EasyAsk logo.

Third, pricing by NLI developers may help to internalize this externality. If an NLI developer benefits from consumers learning how to work with its system, then it also benefits from retailers who adopt its system earlier. It should therefore give discounts to these early adopters, and so, bear some of the costs of this early adoption. Of course, it should require display of its logo in return, so consumers know whose NLI they are learning about.

Fourth, if the vendor can convince Internet retailers that consumers are becoming familiar with its NLI, more Internet retailers will adopt it, so more consumers will learn how to use it.

Finally, a vendor might make direct efforts to help consumers become familiar with its NLI interface. For example, it may give Internet retailers’ discounts if they include drop-down windows of sample requests that users can ask of the NLI. NLI vendors might also use focus groups to learn the types of requests users would ask if they understood the full capabilities of the NLI and include these requests in the drop-down windows.

The network externalities of NLIs in B2C e-commerce also suggest that these NLI applications may be subject to sudden, unexpected growth spirts. Initially, customers may become frustrated with these systems. However, as they become familiar with the strengths and limitations of these systems, these systems may become increasingly popular among users, and so, increasingly profitable to Internet retailers. In fact, it is theoretically possible that, even with current, existing technology, NLI applications may become dramatically more popular as users become familiar with them. As more users learn how to work with NLIs, more firms may adopt them, leading still more users to become familiar with them, creating a snowball effect.

However, one should be careful not to overemphasize the importance of network externalities [25]. A mistaken belief in the ubiquity of network externalities may have played an important role in the overpricing of internet stocks. In addition, it may have encouraged a winner-take-all mentality, and an exaggerated belief in the importance of first mover advantages. These may have led to overinvestment and rushed, unwise business decisions.

B2B applications may raise a different set of issues. First, to the extent that relationships between supply chain partners are more stable than relationships between consumers and Internet retailers, supply chain partners may be willing to learn how to use one another’s NLIs. Firms in an industry may also choose to follow a formal or informal industry standard. If all firms in the auto industry, say, worked with the same NLI provider, then that provider could standardize the NLIs capabilities so that a parts supplier familiar with GM’s supply chain NLI would have a pretty good idea how to work with Chrysler’s supply chain NLI. That is, in B2B applications, firms may be better able to internalize any network externalities that exist.

In summary, even given the limited nature of current NLI technology, existing NLIs may become more popular as more users learn how to work around these limitations. In fact, it may be a sign of progress when NLI limitations become a popular topic of conversation.

## 3. Implications of cost structure-dynamics, competition, and pricing

Like all software, NLIs have a cost structure involving a large initial fixed cost (the cost of developing the initial software) and a small variable cost [37]. This cost structure has three major implications: (i) a long period of development will be needed before truly reliable NLIs are built, but once the quality of the software crosses this threshold, applications may grow rapidly; (ii) firms must receive an average price per unit significantly above marginal cost in order to justify their initial investment, so a firm will only invest in the development of NLI software if it expects to have considerable market power once the system is developed; and (iii) this market power, combined with low marginal cost, means that NLI vendors will face nontrivial pricing problems. These three implications, however, are modified by the particular characteristics of NLIs, as explained below.

Natural languages are much more complicated than formal languages [13]. The up-front cost of developing workable NLIs is therefore very large, so it will be a while before truly versatile NLIs are developed. Thus, there may be a long period involving clever adaptations of limited NLI systems to specific areas. These clever adaptations may require significant organization-specific customization to transport these systems to new application domains [17,19,26]. See Section 7 below.

This imaginative use of limited NLI technology may, in turn, create a market for improved natural language processing (NLP) systems, and so, may speed up the development of such systems. Once this technology crosses a threshold level, adoption should then accelerate. This increased demand should then stimulate more rapid development in a snowball fashion, especially since these systems can be replicated at very low cost. This snowball effect reenforces the effect of the network externality, as mentioned in Section 2.2. Thus, potential users should expect rapid improvements, once these technologies begin to mature.

Next, low cost distribution conflicts with the initial developer’s incentive to incur the fixed cost of developing the system. A developer will only develop a system if she expects to sell it for significantly more than the marginal cost of producing an additional unit, since she will otherwise be unable to cover the upfront fixed development cost. Thus, imitation or the threat of parallel development of NLP systems by competing firms may reduce each firm’s incentives to devote resources to developing a sophisticated system. This yields a classic argument for the patent system, and for public support for the development of technology [38,Chapter9,40,Chapter10]. Put another way, firms will only incur the fixed costs of developing sophisticated systems if they do not expect markets to be perfectly competitive. Otherwise prices would be driven down to marginal cost, and so, would be much less than average cost. The firm could not then make a profit. Anticipating this, few firms would enter the market in the first place, so perfect competition would never be achieved [37].

On the other hand, since NLI applications usually involve considerable customization, this may reduce post-entry competition. First, customization leads to product differentiation. NLI vendors might differentiate themselves from each other by their ability to customize for different industries, and an NLI vendor’s team of programmers, who do the customization, may further differentiate the vendor from its competitors. Second, competition may also be affected by the capacity constraints imposed by the need to customize systems. If systems require significant customization, then a firm’s ability to expand is limited by the personnel it has available to customize systems for individual buyers. This, in turn, can reduce the aggressiveness with which firms compete [23].

In any case, competition will generally not be perfect, so firms retain significant control over prices. Pricing then becomes a nontrivial issue. In particular, since marginal cost is much less than average cost, it is optimal for vendors to sell ‘‘marginal’’ units for much less than the average unit. NLI vendors will therefore want to pursue some sort of price discrimination. For example, vendors will want to sell NLI systems to small firms for much less than they charge large firms. If small firms are ‘‘marginal’’ buyers, then vendors want to charge them a price closer to marginal cost, and so, much less than the prices it charges to larger firms. Thus, software vendors generally give implicit discounts to small firms by offering per-user licenses.

On the other hand, in terms of pricing for a single customer, the NLI vendor may want to charge some sort of analogue of a quantity discount. That is, rather than charge a simple per-user fee, the vendor might charge an ‘‘installation fee’’ for the basic setup of the system, but then charge a smaller fee for marginal improvements to the system. The installation fee would presumably be larger for larger organizations, but, for any given organization, the fee for marginal improvements would be close to marginal cost. Given the customer’s decision to adopt the system, this pricing structure would reduce the distortion in the customer’s decision of how extensively to use the NLI within the organization. This would maximize the overall gains from trade, which the vendor could then extract through the fixed fees [21,Chapter5]. The vendor would only want to charge a marginal per unit price significantly above marginal cost if the vendor felt that a customer’s demand for extra features revealed a higher overall willingness to pay [27,33,40, Chapter 3].

The customer should also be able to negotiate marginal improvements in the system at close to marginal cost, unless such requests revealed too much about its willingness to pay.

Since NLIs will be more useful to some users than to others (see Section 2.1), this should also affect the fixed fee. For example, an NLI may be very valuable to an executive with a high opportunity cost of time and a wide range of ad hoc questions to ask. By contrast, NLI systems may offer some convenience value for hotel clerks, but will presumably offer much less value per user, since a form or menu based system will be almost as good. Thus, it would make sense for NLI vendors to base fees on the type of user, as well as the size of the firm. In the related industry of voice recognition, for example, the company Kurzweil charges much more for systems aimed at doctors than for systems aimed at general users [37,p,60]. Prices could also depend on the types of customization requested by the users.

Customization of NLIs also implies lock-in once a system has been customized. Thus, customers will tend to renew licenses with the same NLI vendor. This reduces competition for established customers, so vendors may be tempted to charge established customers a lot for license renewals. This may make customers reluctant to commit to a system unless the vendor can commit itself to not exploit this lock-in too aggressively. If the vendor cannot commit itself in this way, it may need to offer a low initial price, to compensate for this lock-in.

Finally, as mentioned in Section 2.2, NLIs may experience significant network externalities, where users who become familiar with one website’s NLI, say, may be able to work better with other websites’ NLIs, so NLI vendors may have an incentive to provide price discounts to early adopters of their NLI systems. This is something like what firms are doing when they give away beta versions of their product. Vendors can potentially use similar discounts to internalize some of the network externalities among users of their systems.

## 4. How is NLP technology feasible?

This section now turns to the technological challenges faced by NLIs versus simpler interfaces. Since natural languages are so complicated, it may seem impossible to develop viable NLP technologies. The set of possible sentences may seem too vast to handle.

What makes NLP potentially feasible is that natural languages use their rules recursively. That is, they use a limited set of rules over and over to generate an unlimited set of sentences. We can illustrate this by considering a different natural language, which computers can handle very well, i.e., mathematics. Suppose, e.g., that one wants to determine the present value of a project with 3 years of income, $Y _ { 1 } , Y _ { 2 } ,$ and $Y _ { 3 } ,$ and initial outlay C. Then one must calculate

$$
\frac {Y _ {1}}{1 + r} + \frac {Y _ {2}}{(1 + r) ^ {2}} + \frac {Y _ {3}}{(1 + r) ^ {3}} - C.
$$

Performing a calculation like this on a menu-based system would be very difficult. However, people use programming languages and spreadsheets to work with formulas like this all the time. The key is that the user and the computer share the language of mathematics. Computers can work with mathematics because mathematics is a recursive language which uses simple components to build up more complicated structures. For example, the formula above is a combination of the operations of addition, subtraction, multiplication, and division.

Of course, ordinary natural languages are much more complicated than mathematics [4]. Nevertheless, natural languages have a recursive structure, known as phrase structure [6,7]. Linguists represent this structure using parse trees. For example, the question ‘‘Who teaches the students in the class’’ has a (simplified) parse tree

$$
\begin{array}{l} \text {s(noun("who"),verb\_pp("teaches",noun\_p} \\ \text {("the","students"), pp("in",noun\_p("the",} \\ \text {class"))))} \end{array}
$$

This indicates that the main verb of the sentence is ‘‘teaches’’. Also, the subject of the verb is ‘‘who’’ and the object of the verb is ‘‘the students’’. Finally, the prepositional phrase (pp) indicates that the teaching is occurring ‘‘in the class’’. This structure is known as a parse tree because it can also be represented as a tree structure.

The recursive nature of English allows the system to use the same grammatical rules over and over. Thus, the noun phrase rule is applied here to both the noun phrase ‘‘the students’’ and the noun phrase ‘‘the class’’. This reusability is analogous to the reusability of arithmetic operations, exploited in programming languages and spreadsheets. Just as a program can combine a limited set of operations to generate an unlimited set of formulas, a parser uses a limited set of grammatical rules to interpret an unlimited set of English sentences.

Thus, NLIs derive a benefit over menu or formbased interfaces, because NLIs are able to exploit the recursive structure of natural languages such as English to process a wider range of user needs. Moreover, an NLI can draw on a much wider vocabulary that a menu or form-based interface can. This vocabulary will generally be stored in a lexicon [9], for the system’s use, and is an additional advantage of an NLI over a simpler interface type.

## 5. A prototype NLI system

The system at the University of Mississippi uses the programming language Prolog to analyze English sentences and translate these sentences into SQL. The application domain we focus on is a very simple version of a university database. The following describes the different components of this system: the parser, the lexicon, the knowledge base, and the SQL generator.

## 5.1. The parser

As discussed above, the parser breaks complicated sentences into small parts with their grammatical roles, e.g., parts of speech, indicated [10,45]. An example is given in Section 4. Our parser also moves ‘‘WHwords’’ (such as ‘‘who’’, ‘‘which’’, ‘‘when’’, ‘‘where’’, etc.) to the appropriate position in the sentence to allow the SQL generator to determine what the user really wants to ask. For example, the sentence

‘‘What did bob teach in H110’’

is parsed as:

$$
\begin{array}{l} \text {s(noun("bob"),verb\_pp("teach",noun("what"),} \\ \text {pp("in",noun("H110"))))} \end{array}
$$

This indicates that ‘‘what’’ is asking for the object of the verb ‘‘taught’’. Again, the fact that such movement rules can be combined with phrase structure rules in an unlimited number of ways enhances the flexibility of an NLI. Our parser builds on the approach in Ref. [10].

The parser, then, is the heart of the typical NLP system and should be fairly independent of application area. That is, the parser should not be organization-specific. For more on parsers, see Refs. [4,10,11]. For references on the syntactic theory underlying parsers, including movement, see Refs. [6,7].

## 5.2. The lexicon

Our lexicon contains the system’s vocabulary and indicates the part of speech for each word. This vocabulary includes both the words in the database, and the words that the users might employ. Some sample entries in the lexicon are:

<table><tr><td>wh(“who”).</td><td>wh(“which”).</td><td>wh(“where”).</td></tr><tr><td>do(“do”).</td><td>do(“did”).</td><td>do(“does”).</td></tr><tr><td>d(“the”).</td><td>d(“a”).</td><td>d(“an”).</td></tr><tr><td>n(“mis409”).</td><td>n(“class”).</td><td>n(“computer”).</td></tr><tr><td>v(“is”).</td><td>v(“teach”).</td><td>v(“take”).</td></tr><tr><td>aj(“red”).</td><td>aj(“higher”).</td><td>aj(“small”).</td></tr><tr><td>p(“in”).</td><td>p(“on”).</td><td>p(“under”).</td></tr></table>

Thus, ‘‘who’’ is a wh-word, ‘‘does’’ is a conjugation of the important auxiliary verb ‘‘do’’, ‘‘the’’ is a determiner, ‘‘computer’’ is a noun, ‘‘teach’’ is a verb, ‘‘red’’ is an adjective, and ‘‘in’’ is a preposition. The parser uses this classification to determine the recursive structure of sentences.

The size of the lexicon can be fruitfully contrasted with the size of a typical menu base. The effective language of a menu base is limited by the number of options offered at a typical level, raised to the number of levels in the menu base. For example, a menu base with 8 options per level and three levels will offer roughly $8 ^ { \hat { 3 } } = 5 1 2$ options, giving a vocabulary of about 512 choices. Any reasonably large lexicon will therefore dwarf most menu bases. Again, this underscores the increased flexibility of an NLI as compared to a menu base. Note, however, that if each menu item yields a flexible form-based interface, such as a query by example interface, this may increase the menu base’s flexibility. Section 6 compares NLIs to more sophisticated user interfaces, such as attribute (or column) selection form or report wizards.

Finally, lexicons should be fairly ‘‘transportable’’ from one organization to another, particularly within application area [17,19,26]. This suggests that markets could develop for lexicons in different application areas. This would allow an organization to purchase the underlying NLI system and the lexicon separately, though the organization may also want to be able to modify the lexicon in various ways. Area-specific lexicons are useful because, even if a word has several meanings in general, only a few of these meanings may apply to a given area. This may significantly reduce ambiguity.

## 5.3. The knowledge base

The knowledge base allows the computer to relate the words in a user’s query to the terms in the database. The following are some sample entries in our system’s knowledge base.

isa(‘‘professor’’, ‘‘rank’’). isa(‘‘mis’’, ‘‘major’’). isa(‘‘classes’’, ‘‘table<sup>\_</sup>name’’). v<sup>\_</sup>obj(‘‘take’’, ‘‘c<sup>\_</sup>title’’). actor(‘‘takes’’, ‘‘stuname’’). in<sup>\_</sup>table(‘‘course<sup>\_</sup>no’’, ‘‘classes’’). in<sup>\_</sup>table(‘‘rank’’, ‘‘faculty’’).

isa(‘‘mis’’, ‘‘c<sup>\_</sup>title’’). isa(‘‘art’’, ‘‘department’’). isa(‘‘computer’’, ‘‘tool’’). v<sup>\_</sup>obj(‘‘taught’’, ‘‘c<sup>\_</sup>title’’). actor(‘‘teaches’’, ‘‘facname’’). in<sup>\_</sup>table(‘‘dept’’, ‘‘faculty’’). in<sup>\_</sup>table(‘‘credits’’, ‘‘student’’).

This part of the system is needed to interpret the words in a user’s query in terms of the attribute names, etc., in the database. Thus, if the user’s query includes the word ‘‘professor’’, the system will know that ‘‘professor’’ is a ‘‘rank’’, and will know to look for the ‘‘rank’’ attribute in the Faculty table. The attribute names in the database provide the ultimate meanings of the key words in a user’s query. The knowledge base provides a bridge between the words employed by the user and these ultimate meanings given by the database.

Since these ultimate meanings are given by the application (in this case, the database), the organization employing the NLI must custom-build much of the knowledge base for the specific application. This may often be a major part of the cost to the organization of adopting an NLI. Breaking off this information into a separate knowledge-base component should make this customization easier. However, certain sophisticated commercial NLIs can already do much of this customization automatically. See the discussion of ELF’s Analyzer in Section 8.1 below.

Also, much of the knowledge in a knowledge base will not be organization specific. For example, the entry isa(‘‘faculty’’, ‘‘employee’’) would apply across universities. Such entries are called ‘‘lexical semantic relations’’ [3,42], and a great deal of work has been done building large sets of these relations. For example, WordNet [18,29,30] is a large collection of lexical semantic relations built at Princeton University. Word-Net builds on six major lexical semantic relations: synonyms, hypernyms (X is a kind of Y), hyponyms (Y is a kind of X), holonyms (X is a part of Y), meronyms (Y is a part of X), and familiarity. WordNet contains lexical semantic relations between 95,600 different word forms. Ultimately, markets may develop for area-specific versions of such pre-developed knowledge bases.

## 5.4. The SQL generator

The SQL generator takes sentence structures in the form of parse trees, and combines them with information from the lexicon and knowledge base to generate commands that database systems can understand (SQL in the case of our system). The generated SQL statements are then executed by database management systems (DBMS) to produce answers for the users. For example, the question:

‘‘Who teaches mis in H110 at 12:00’’

is parsed as

$$
\begin{array}{l} \text {s(noun("who"),verb\_pp("teaches",n("mis"),} \\ \text {pp("in",noun("H110")),pp("at",noun("12:00))))} \end{array}
$$

(the version of Prolog we use-PDC Prolog-has difficulty handling colons-as in ‘‘12:00’’-but we ignore this in the discussion here and below). The SQL generator then converts this parse tree into an SQL statement as:

<table><tr><td>SELECT</td><td>facname</td></tr><tr><td>FROM</td><td>faculty, classes</td></tr><tr><td>WHERE</td><td>c_title = ‘mis’</td></tr><tr><td>and</td><td>room = ‘H110’</td></tr><tr><td>and</td><td>sched = ‘12:00’</td></tr><tr><td>and</td><td>faculty.facid = classes.facid</td></tr></table>

Since the SQL generator is a separate component, the system can be more easily transported between different DBMS’s. In a transportable version of the system, the database administrator would need to indicate which DBMS the interface will be used with, so the SQL generator generates the appropriate dialect of SQL [17,19,26].

## 6. When is a problem domain ‘‘well structured but not too well structured?’’

We now use the general structure of our NLI to consider how well structured an application domain should be in order for an NLI to be the appropriate form of interface. We focus on applications, which require a reasonably flexible interface, for example, a mid-level executive’s task of extracting data from a database to prepare an ad hoc report.

To assess the flexibility of an NLI, we compare an NLI to an attribute-selection (i.e., column-selection) system, such as Oracle Developer’s Data Block Wizard [31]. Such systems allow users to custombuild forms by selecting from lists of attributes, and so, gives users considerable flexibility, without requiring them to know SQL. Thus, we ask whether it makes more sense for an organization to customize an NLI for their particular application domain, or expect users to work through an attribute-selection process to build a form or report. In the process, we consider the demands placed on the language understanding system and on the organization-specific knowledge base, which would have to be developed for a typical application. Throughout we use the University of Mississippi NLI as the representative system, though we occasionally refer to more sophisticated commercial systems.

We proceed in five stages. First, we consider a query that requests information from attributes (i.e., columns) of a single table. Second, we consider constraints on individual attributes in a single table, for example, listing employees with salaries greater than US \$40,000. Third, we allow for cross-attribute constraints (e.g., within-major GPA greater than overall GPA). Fourth, we consider queries requiring joins. Finally, we consider performing various computations on attributes, given various own and cross-attribute constraints. For example, what is the average salary of employees with at least 5 years experience with the firm?

For each of these tasks, we consider the relative difficulty of handling the task with an NLI versus a sophisticated non-NLI interface, such as Oracle/ Developer’s Data Block Wizard. How convenient is an NLI versus such an attribute-selection system in handling each task and how does this convenience vary with, e.g., the number of attributes in the database? This will allow us to determine which tasks, if any, may be sufficiently simple that they can be handled by an NLI, but too complicated to handle by even a sophisticated menu-based system.

## 6.1. Selecting attributes of a single table

First consider a query such as

‘‘What are the salaries of all faculty?’’

This query is parsed as

$$
s (n o u n (“ w h a t ”), v e r b \_ p h r a s e (“ a r e ”, d \_ n 1 \_ p p
$$

( ‘‘ t h e ’’ , ‘‘ s a l a r i e s ’’ , p p ( ‘‘ o f ’’ , a v <sup>\_</sup> n ( ‘‘ a l l ’’ , ‘‘faculty’’))))).

The SQL generator then converts this parse tree into the SQL statement

<table><tr><td>SELECT</td><td>facname, salaries</td></tr><tr><td>FROM</td><td>faculty</td></tr></table>

What does the NLI need to do to make this conversion? First, it needs to recognize that ‘‘what’’ refers to ‘‘salaries’’. This follows because ‘‘what’’ is the subject and ‘‘salaries’’ is the object of the verb ‘‘is’’. This does not involve any organization-specific knowledge, and so can be incorporated into the base system. This is therefore a fixed cost of developing an NLI, so it should not be costly to the organization in the long run [40]. The organization-specific knowledge the system needs in the knowledge base for this query includes:

(1) ‘‘Salaries’’ is an attribute name in the Faculty table. This is represented by the rule in<sup>\_</sup>table (‘‘salary’’,‘‘faculty’’) in the knowledge base.

(2) The attribute ‘‘facname’’ in the Faculty table is specified as a special naming attribute for the Faculty table. Thus, whenever the system presents any information from the Faculty table, it also presents the corresponding element in the ‘‘facname’’ attribute. This is done for the convenience of the user in interpreting the answer.

Note that a different organization might list all employees’ salaries in a large Employee table, for example, so ‘‘salaries of the faculty’’ might be obtained by selecting the ‘‘salaries’’ attribute from the Employee table, where ‘‘employee<sup>\_</sup>category’’ equals ‘‘faculty’’. Thus, since different organizations use different database structures, each organization must indicate where it locates data in its database. Significant organization-specific customization must therefore go into a successful NLI application. On the other hand, some NLI systems do a lot of this customization automatically. See the discussion of the ELF NLI in Section 8.1 below.

By contrast, consider what a user has to do to perform this query through an attribute-selection system, such as Oracle/Developer’s Data Block Wizard and Layout Wizard [31] or Microsoft Access’s Form Wizard and Report Wizard [2]. Using the Oracle/Developer system, for example, the user first selects a table, say, the Faculty table, and selects the ‘‘facname’’ and ‘‘salary’’ attributes, using the Data Block Wizard. She then uses the Layout Wizard to display the information using either a Form or tabular format.

This attribute-selection process is not completely trivial, but it is not prohibitively difficult for a user with a moderate amount of training. On the other hand, if it is difficult to provide even a small amount of training, as in B2C and B2B applications (see Section 2), then the attribute-selection process may be infeasible, increasing the relative benefit of an NLI.

The convenience of an NLI versus an attributeselection system also depends on the size of the database. As the number of attributes in the database grows, an NLI might save the user the effort of scrolling down long lists of attributes. The typical database for a medium sized company contains about 200 tables, and about 30 attributes per table, yielding as many as 6000 attributes that the user must look through. This may become prohibitively time consuming. On the other hand, a database with a large number of attributes may yield frequent ambiguities for the NLI. For example, the word ‘‘price’’ could refer to the price of an input purchased by the organization, or the price of a product or service sold by the firm.

Finally, it may be possible to combine natural language processing capabilities with an attributeselection or menu-based system. For example, the system could ask the user to provide keywords to indicate which issues she is interested in, and the system could return a more limited list of attributes related to those keywords (this approach was suggested by a referee). That is, the system could function something like an information retrieval system. The user would then select attributes from this shorter, more focused list to create a form or report, as above. The system could even incorporate a thesaurus or knowledge base, to expand the list of attributes retrieved. This may provide an interface which is easier to build than an NLI, but easier to use than an unaided attribute-selection system.

## 6.2. Restrictions on individual attributes

Next, consider the query

‘‘What does Smith teach in H110 at 10:00?’’

This query is parsed as

s(noun(‘‘smith’’),verb<sup>\_</sup>pp2(‘‘teach’’,noun(‘‘what’’), pp(‘‘in’’,noun(‘‘H110’’)),pp(‘‘at’’,noun(‘‘10:00’’))))

The SQL generator then ultimately converts this into the SQL statement:

<table><tr><td>SELECT</td><td>facname, course_no, c_title</td></tr><tr><td>FROM</td><td>faculty, classes</td></tr><tr><td>WHERE</td><td>facname = ‘Smith’</td></tr><tr><td>and</td><td>room = ‘H110’</td></tr><tr><td>and</td><td>ched = ‘10:00’</td></tr><tr><td>and</td><td>faculty.facid = classes.facid</td></tr></table>

Ignore the last line for the moment.

What does the system need to know in order to handle this query? In terms of the knowledge base, the system uses the following rules:

(1) The wh-word ‘‘what’’ appears in the object position of the verb ‘‘teach’’. This triggers the rule v<sup>\_</sup>obj(‘‘teach’’,‘‘c<sup>\_</sup>title’’), and so, indicates that the question may be asking for an entry from the attribute ‘‘c<sup>\_</sup>title’’, which contains course titles. Note, incidentally, that this builds on the movement facility of our parser, which moved the wh-word ‘‘what’’ from the subject position in the original question to the object position in the parse tree.

(2) The rule isa(‘‘smith’’,‘‘facname’’) indicates that one restriction on the ‘‘facname’’ attribute will be facname = ‘smith’.

(3) The rule isa(‘‘H110’’,‘‘room’’) indicates that a restriction on the ‘‘room’’ attribute will be room = ‘H110’.

(4) The rule isa(‘‘10:00’’,‘‘sched’’) indicates that a restriction on the ‘‘sched’’ attribute will be sched = ‘10:00’.

Thus, building a knowledge base capable of handling this query would again require a considerable amount of organization-specific work, though much of it could be done with a sophisticated install procedure.

How would this compare to processing by an attribute-selection system such as Oracle/Developer’s Data Block and Layout Wizards? First, the user would select the five attributes ‘‘facname’’, ‘‘course<sup>\_</sup>no’’, ‘‘c<sup>\_</sup>title’’, ‘‘room’’, and ‘‘sched’’, as above (ignore for the moment the fact that the attributes actually come from two different tables). If the user chooses the tabular format, she would then use a query by example (QBE) approach to specify query constraints by typing ‘smith’ for the ‘‘facname’’ attribute, ‘H110’ for the ‘‘room’’ attribute, and ‘10:00’ for the ‘‘sched’’ attribute.

This procedure would require somewhat more knowledge of the Oracle/Developer Wizard facility. However, with a moderate amount of training, an employee of the firm, say, could easily use such a system unless the number of attributes was prohibitively large. Thus, in this case, an attribute-selection approach might be as flexible as an NLI, and easier to build.

On the other hand, the number of attributes accessed will tend to be larger if the user wants to put restrictions on attributes. For example, in the above query, only the ‘‘facname’’, ‘‘course<sup>\_</sup>no’’, and ‘‘c<sup>\_</sup>title’’ attributes are wanted, but the ‘‘room’’ and ‘‘sched’’ attributes are used to impose restrictions (ignoring, for the moment, the joining condition in the last line of the SQL statement). Thus, in this case, the user would need to locate five attributes, even though only three are ultimately desired. Therefore, if the number of attributes in the database is large, then an attribute-selection system will tend to become somewhat more difficult to use.

## 6.3. Restrictions across attributes

Next, consider the following query, which involves a comparison between two attributes:

‘‘Which students have overall GPA less than major GPA?’’

This query is parsed as

```prolog
S(noun(“Which”, “students”), verb_pp(“have”, compp(np_adj(adj(“overall”), n(“GPA”)), comp(“less”, “than”), np_adj(adj(“major”), n(“GPA”))))).
```

The SQL generator then converts this into the SQL statement:

<table><tr><td>SELECT</td><td>stuname</td></tr><tr><td>FROM</td><td>student</td></tr><tr><td>WHERE</td><td>overall_gpa &lt; major_gpa</td></tr></table>

The new element, here, is the comparison of two attributes, ‘‘overall<sup>\_</sup>gpa’’ and ‘‘major<sup>\_</sup>gpa’’. This requires more of the parser, i.e., a comparison construction (compp and comp). Also, organization-specific elements in the knowledge base are necessary to allow the system to find ‘‘overall GPA’’ and ‘‘major GPA’’ in the database, though this is needed even setting aside cross-attribute restrictions. Beyond that, the SQL generator needs to recognize ‘‘less than’’ as ‘‘ < ’’ in SQL, but again, this can be prespecified in the SQL generator. Thus, cross-attribute restrictions seem to create few extra difficulties for an NLI.

By contrast, imposing this cross-attribute restriction in an attribute-selection system such as Oracle/ Developer’s Data Block and Layout Wizard is nontrivial. In the Oracle system, the user must first create the basic form structure, as above. She must then select the ‘‘property palette’’, and type the crossattribute restriction Major<sup>\_</sup>GPA>Overall<sup>\_</sup>GPA into the ‘‘where clause’’ row. This requires considerable sophistication of the user. Such problems may therefore be so poorly structured that an NLI would be preferred to an attribute-selection approach. The comparative advantage of NLIs may therefore increase at this point. On the other hand, it is not clear how often users want to use such cross-attribute restrictions in practice.

## 6.4. Joining tables

The joining of two tables is obtained by forming the Cartesian product of two tables and imposing a crossattribute restriction. The major new element is that the system must know which Attribute<sup>\_</sup>X = Attribute<sup>\_</sup>Y restrictions are needed to perform the join. This will be trivial for both types of system if each table has at most one foreign key pointing to any other table. Sometimes this may not be the case. For example, a film industry database may have foreign keys in the Movie table for both ‘‘lead actor’’ and ‘‘supporting actor’’, pointing to the same Actor table. In this case, the problem of joining would become nontrivial. This difficulty, however, would be common to both systems. Note that the query in Section 6.2 above involved joining two tables, and so, required the cross-attribute restriction faculty.facid = classes.facid.

If we move beyond flat files to multi-table databases, the number of attributes can explode, as mentioned above. Using an attribute-selection interface can therefore become very time consuming, especially for people who are not familiar with the database. The user would have to look at many tables, and many attributes per table. The system will then only be able to provide the correct answer if it is clear what joining conditions to use to join the tables.

## 6.5. Performing computations on attributes

Consider the query

‘‘What is the average GPA of MIS majors?’’

After parsing, the system generates the SQL commands

<table><tr><td>SELECT</td><td>Avg(overall_gpa)</td></tr><tr><td>FROM</td><td>student</td></tr><tr><td>WHERE</td><td>major = ‘mis’</td></tr></table>

Here, the knowledge base needs to know that there is no attribute such as average<sup>\_</sup>gpa in which ‘‘average GPA’’ could be found, but that, instead, ‘‘average GPA’’ would request that the Avg function be applied to the ‘‘overall<sup>\_</sup>gpa’’ attribute, after applying the major = ‘mis’ restriction. Likewise, in an attributeselection system, the user can restrict the field in the ‘‘major’’ attribute to be ‘mis’, and then specify that an average of the ‘‘overall<sup>\_</sup>gpa’’ attribute is desired. There does not seem to be any special advantage to an NLI in this case.

## 6.6. Other types of queries

More sophisticated NLIs can understand question structures more complicated than those handled by the University of Mississippi system. For example, the commercial NLI, ELF [15, SQL Server 7.0 link] can handle questions such as ‘‘Which customers have ordered both Konbu and Filo Mix?’’ This question, referring to Microsoft’s Northwind database, requires the system to select customers based on having ‘‘Konbu’’ in one row of that customer’s product attribute, and ‘‘Filo Mix’’ in another row of that same customer’s product attribute. Similarly, the query ‘‘Show company names of the suppliers that have more than 3 products’’, requires ELF to select suppliers whose supplier IDs appear in more than three rows of the Product table of the Northwind database. These queries would be very difficult to handle using an attribute-selection system, but can be handled by sophisticated NLIs such as ELF. Thus, NLIs like ELF have a significant comparative advantage over attribute-selection-based systems for questions like this.

## 7. Customization issues

As mentioned above, current natural language processing technology is still very limited, so NLIs in the near future will depend heavily on careful application-specific and organization-specific customization, especially for the systems’ knowledge bases and lexicons. This customization represents the major component of the variable cost of extending NLIs to new users. A central question then becomes how to economize on these customization costs.

Part of the solution is the development of sophisticated installation systems, like ELF’s Analyzer, which can perform part of this customization automatically (see Section 8.1). A second way to economize on customization costs is to transform these costs, as much as possible, from variable organization-specific costs into fixed costs, which can be spread over many organizations. This can be done by customizing in two stages: first, build partly customized industry-specific or application-specific systems. This would involve refining the lexicon, knowledge base, and SQL generator for specific application areas. For example, in the related area of voice recognition, the company Kurzweil sells different versions of its product, with vocabularies appropriate for different areas, such as law, medicine, etc. [37, pp. 59 –60].

However, to the extent that the knowledge base and SQL generator interprets words in terms of an organization’s specific database attributes and fields, detailed knowledge of the organization’s database needs to be built into the knowledge base. The above partly customized systems would therefore have to be further customized for specific organizations within an industry. While sophisticated install systems like the ELF Analyzer can help with this, NLIs will nevertheless remain somewhat expensive to adapt by individual organizations.

This, in turn, suggests standardizing organizations’ database structures as well as their knowledge bases and lexicons. This is actually being done by the software companies mentioned in Section 8.1 below. For example, the company MD Computer Consultants was already marketing a software product for doctors offices, which included a carefully designed database structure. Since they have already designed this standardized database structure for their application area, it is much easier for them to customize the commercial NLI, ELF as an interface to their databases. They can then sell the interface, jointly with the database structure, to many customers. This allows their customers to trade off some flexibility in terms of database design, in exchange for a cheaper and more accurate NLI. A similar strategy is used by the human resource software company, also discussed in Section 8.1. The existence of these firms suggests that an ‘‘NLI infrastructure’’ is developing, of firms which build customized NLI-database systems for specific application areas.

The major role for organization-specific customization also suggests that the growth of NLI systems will require a labor market to develop, of people with skill in customizing knowledge bases and lexicons. Just as MIS programs currently turn out graduates who can handle sophisticated DBMS packages such as Oracle, Informix, and DB2, in the same way, future MIS programs may turn out graduates who know how to identify needed elements to include in an NLIs customized knowledge base or lexicon.

This suggests that a network externality may exist in the spread of NLI technology [37,38 Chapter 10,39]. NLI technology may depend upon professionals with skills in customizing NLI systems, but professionals will not develop these skills until NLI technologies become popular. This network externality has implications similar to those of the network externalities mentioned in Section 2.2 and the fixed-cost element in NLP systems mentioned in Section 3. Adoption will initially be slow but, as NLI use achieves a critical mass, the area may begin to grow more rapidly, as professionals develop the skills to customize NLIs, and organizations adopt systems which draw upon these skills.

NLI vendors can internalize some of these externalities by providing customer support, to help organizations customize their NLI. Both ELF and EasyAsk do this (Section 8). Oracle used a similar strategy in the early stages of the relational database market. Then, as the number of MIS personnel familiar with relational databases increased, Oracle was able to reduce the amount of direct customer support needed for users to successfully adapt their software [34].

## 8. Commercially available NLIs

A handful of major commercial NLIs have been developed in the past 20 years or so. The following briefly describes some NLIs, which are either currently available, or have been available in the past. Two commercially available systems, English Language Frontend (ELF), and EasyAsk, are then described in greater detail. Given the state of flux of the NLI field, the following discussion does not attempt to be exhaustive.

One of the first NLI products was Q&A, developed by Symantec. Symantec sold Q&A from 1982 to 1998, but has since discontinued Q&A, and turned to products related to Internet security, etc. Recently, Lantica Software LLC has announced plans to develop a Q&A-compatible database interface, though it is not clear what its NLI capabilities will be.

A second major commercial NLI, Intellect, was developed for mainframes in the early 1980s, by Larry Harris, a former professor of Computer Science at Dartmouth. Harris went on to develop English Wizard, for PCs, in the mid-1990s, and EasyAsk for search of e-commerce sites and other enterprise databases (see Ref. [12] and below). A third NLI, LanguageAccess, was briefly distributed by IBM in the early 1990s [5,24], and a fourth, English Query, has been introduced by Microsoft, for use with

Microsoft’s SQL Server [28]. Finally, the NLI ELF (English Language Frontend) was introduced by the ELF Software in 1995. The same company previously introduced ELLIE, an NLI for dBase, in 1989 (see Ref. [14] and below).

To get some sense of the commercial implications of NLIs, we interviewed people at two commercial NLI companies, the ELF Software Company, and EasyAsk. We also interviewed three ELF customers, to get a user’s perspective on the product. Unfortunately, it is beyond the scope of this paper to do a more systematic survey of NLI users.

## 8.1. The ELF NLI

The founder and CEO of ELF Software is computational linguist Jon Greenblatt. Greenblatt developed the basic interface in the mid 1980’s, using transformational grammar modeled after Chomsky’s Aspects model [8]. This part of the system involves about a thousand linguistic rules. Unlike the simple prototype discussed in Section 5 of the current paper, Greenblatt’s system is not written in Prolog, but in Delphi, since Delphi allows greater control over the detailed workings of the computer. At this point, ELF has been marketed primarily for smaller databases, with a single-user edition costing only US\$139 and a deluxe developer’s edition costing US\$499, [16]. Technically, the system is designed to work with larger and more complicated databases, as well.

The ELF system is much more sophisticated than the system in Section 5. It thus gives some sense of the advantages of sophisticated NLIs over their closest non-NLI competitors such as attribute-selection systems. For example, ELF Software presents a demonstration application on their website [15, SQL Server 7.0 link], interfacing with Microsoft’s Northwind sample database. They illustrate ELF with queries such as ‘‘Which customers have ordered both Konbu and Filo Mix’’, as mentioned above. As argued above, an attribute-selection system would have difficulty answering a query like this. ELF, on the other hand, generates an extremely complicated SQL statement in response to this query, which gives back the correct answer. The fact that ELF can handle this query suggests how sophisticated some commercial NLIs are.

The ELF demo provides drop-down menus illustrating about 40 queries. It also allows visitors to type in other queries over the web. For example it was able to handle typed-in questions such as ‘‘Which customers ordered tofu but not konbu?’’ and ‘‘Which customers ordered products with unit price greater than \$40?’’ The ELF demo is not perfect, however. For example, in response to the query ‘‘What is the price of tofu?’’ it gives shipping freight, not price. However, the response table clearly labels the shipping freight attribute as ‘‘Freight’’, so there is little danger of user confusion. Also, in response to ‘‘What is the unit price of tofu?’’ (emphasis added), the demo returns the correct answer. Finally, ELF is designed so that a system administrator can easily fix problems like this, though Greenblatt says that he did very little customization with the Northwind demo. In summary, the ELF system, while not perfect, is able to handle a remarkable range of linguistic input and SQL output.

An aspect of ELF that Greenblatt takes special pride in is the install feature, called the Analyzer. ELF is designed to analyze the structure of a user’s database automatically, to determine which attributes and tables different concepts will refer to. For example, in the Employees table of the Northwind database, the ELF Analyzer identifies attribute names such as ‘‘Home Phone’’ as concepts that a user might ask about. Thus, ELF is able to do a considerable amount of customization automatically. However, the system administrator will generally also have to do some additional customization, such as defining synonyms for the different database concepts, to broaden ELF’s vocabulary.

To get a user’s perspective on ELF, we interviewed three ELF customers, Taha Kass-Hout, Penda Tomlinson, and Steve Hyde. Kass-Hout adopted ELF for an application at a public health institution, while Tomlinson and Hyde are incorporating ELF as an NLI into software products, which their companies are selling.

Taha Kass-Hout adopted ELF to help 14 people he was supervising, who had responsibility for inputting data and answering ad hoc questions concerning a relational database about medical information. These users had highschool degrees and a little beyond. A few had some experience with computers, and ‘‘knew how they thought’’, according to Kass-Hout.

Installing and running the ELF Analyzer took Kass-Hout about an hour. Building the additional vocabulary then took a few hours. Kass-Hout also developed a set of 40 or 50 sample questions, whose structure the users could follow. This took Kass-Hout 5 or 6 days on and off, with users helping by telling him the things they wanted to ask. Most of the users were not sufficiently confident to experiment with different kinds of questions, and so, stayed close to Kass-Hout’s original list of sample question structures.

A few of the users, however, began exploring the full range of what they could ask through ELF, using trial and error. They would try a question, and ELF would either indicate that it did not understand the question, or respond with something the user did not understand. For the first few weeks of this experimentation period, they would ask Kass-Hout about almost every new question. Eventually, however, they became confident with the system, and only called occasionally for reassurance. It helped, however, that, since the users had entered the data themselves, they were familiar with the structure of the database, so they could recognize when ELF gave an incorrect answer. In the end, Kass-Hout felt that the users who had gone through this exploratory process were ‘‘extremely happy with the results of ELF as an NLI’’.

Perhaps the most interesting thing about Kass-Hout’s experience is the effectiveness of trial and error as a training tool. This suggests that a similar trial and error process might be an important step in users becoming comfortable with other NLIs, as argued in Section 2.2 above.

The other two customers we interviewed were incorporating ELF into systems for resale. Penda Tomlinson works for a company which supplies software systems to support the human resource function, and is incorporating ELF into these systems as a database interface tool. Their system currently has a complex report writer, and Tomlinson is hoping that ELF will allow users to create reports without knowing any SQL. Their target users are human resource professionals: administrators and staff, with a focus on users at the executive level. The number of users per organization ranges from 1 to 30. The basic database structure Tomlinson’s firm supplies involves about eight tables. One table has about 100 attributes, and the others have about 30 attributes each. Customers can also ask for additional attributes.

The fact that the firm designs the database gives these databases a lot of common, standardized, structure. This makes it easier to adapt the NLI to this structure, as argued in Section 7 above. However, ambiguity remains a problem, according to Tomlinson. The database’s vocabulary is large, and different attributes often have similar names, such as ‘‘contracted hours per day’’ versus ‘‘contracted hours per week’’. A major challenge in customizing ELF for their database product is to handle these ambiguities. One approach they are using is to give the user extra information in case of ambiguity. For example, if the user asks a question about something ‘‘contractual’’ the system may return everything with ‘‘contractual’’ in it, and let the user sort it out.

Tomlinson initially tried his system out in-house (on colleagues in his firm). His sense is that, at the present time, when a user first starts using the system, without any sample questions for guidance, their queries have a success rate of about 50%. If given sample questions to illustrate the system, and one to one and a half hours of practice, their success rate rises to 70– 80%. Some users are very passive, and accept whatever answer the system gives. Others, however, are more active, changing the wording of a question to see how the system responds. ‘‘We’ve had users randomly cut words out to see what happens’’ according to Tomlinson. ‘‘Once people feel like they can joke about it and feel comfortable with the system, then it’s successful’’.

Tomlinson’s firm has just begun trying the system on focus groups. Queries asked by members of the focus groups include ‘‘Show telephone number of male employees aged over 18 with salaries over 25,000’’, ‘‘how many UK european employees are located at head office?’’ and ‘‘how many employees are in each department of each sex?’’ Note that these queries are very complicated, and presumably depend upon the full natural language understanding capabilities of a sophisticated NLI like ELF, and also on the customization done by Tomlinson’s firm. On the other hand, it is not clear how the queries will change as the system moves from focus groups to actual applications.

The third ELF customer we interviewed was Steve Hyde, at MD Computer Consultants, a supplier of software solutions for medical office applications. They are incorporating ELF as a database interface into Medical Office Mate, a scheduling and billing system for doctors’ offices. The database component of Medical Office Mate has about 36 tables, with about 520 attributes that they want ELF to handle. This database contains information about patients, appointments, insurance companies, services delivered, payments received, and so on.

Hyde believes that the ELF NLI is very ‘‘robust’’. He also feels that the Analyzer is very convenient, and does a lot of the customization work. Nevertheless, his company is doing a lot of additional customization to incorporate ELF into Medical Office Mate. Hyde feels that, since his company has designed the underlying standardized database structure, it is a lot easier for them to customize ELF to work well with that structure. This is again consistent with the argument in Section 7 above. He also maintains that careful normalization of the database reduces the problem of ambiguity. Rather than having a lot of attributes with similar information in them, a well normalized database has less redundancy, and instead has foreign keys pointing to the location of the relevant data elsewhere in the database. He also feels that splitting the database into views will reduce the ambiguities that ELF will have to deal with, though this will be less necessary if the database is designed well. Hyde has a very high standard for what he hopes ELF will do, once incorporated into his product. He disagreed with the suggestion that users should be willing to experiment with the system in order to learn how to work around its limitations. He felt that his users will ‘‘just want the data so they can go home. They’re not going to want to play around with it. . . . A successful NLI should save you work. It’s not a toy’’. Nevertheless, he felt that beta testing is an important part of the development process. They plan to give the beta version, free, to ‘‘certain doctors with very knowledgeable staff’’. These first few customers would presumably have a lot of complaints about the system. Then, as the system is refined in response to their complaints, he expects to have ‘‘a pretty good system’’. Once the final version is ready for sale, the company will also give the new version to the beta users for free. Hyde felt that a reasonably accurate NLI would be significantly easier to use than an attribute-selection wizard/QBE system.

## 8.2. The EasyAsk NLI

EasyAsk serves two major types of applications: NLIs for on-line retail web catalogues, and enterprise applications for searching heterogeneous internal databases. EasyAsk’s e-commerce customers include Lands’ End, Coldwater Creak, Bombay, Blair, and Talbots.

From the user’s point of view, these NLIs operate a lot like information retrieval (IR) systems. Users type in a request, and the system returns a list of catalogue items, much like a standard search engine returns a list of web pages. Internally, however, the system operates as a standard NLI, parsing the request and connecting its elements with the different database concepts. This makes the system more intelligent than a standard IR system. For example, the system can handle a request such as ‘‘cotton sweaters between \$50 and \$60’’. This question involves the prepositional phrase ‘‘between \$50 and \$60’’, and requires the system to determine that the numbers refer to the ‘‘price’’ attribute in the database, even though the word ‘‘price’’ does not appear in the request. Typical questions for EasyAsk’s commercial sites range from ‘‘golfwear’’ to ‘‘petite red cotton polo shirt for less than \$30’’. Note that this second request requires recursive application of the adjectives ‘‘cotton’’, ‘‘red’’, and ‘‘petite’’ to the compound noun ‘‘polo shirt’’, before appending the prepositional phrase ‘‘for less than \$30’’.

According to Richard Wood, vice president of development, the original installation of EasyAsk usually takes ‘‘a couple of weeks to a month’’. The system then goes on line. For the first few months after the system goes live, EasyAsk is actively involved in reviewing the site and refining the site-specific lexicon. Ultimately, however, EasyAsk expects a system administrator on the customer’s side to take responsibil ity for the lexicon. The system keeps a log of users requests, with how the system translated the requests, and whether the system returned any answers. There is also an EasyAsk NLI to the log file, which allows the system administrator to ask questions such as ‘‘which requests most often failed to return answers’’. The monetary cost of the 3-year site license is ‘‘low six figures and up’’, according to Wood, with daily consulting fees for the installation and a maintenance fee of 18%.

EasyAsk also builds enterprise applications, for search of internal databases. These applications generally involve multiple databases, and unstructured data such as documents. They are therefore more complicated, because the system must initially determine which databases should be queried, and then must integrate the returned information into a coherent response. These systems must therefore combine standard IR techniques with NLI techniques. At this point, EasyAsk’s commercial sales are primarily in e-commerce, with some enterprise applications, but they hope to expand the enterprise side of their business in the future.

## 9. Conclusion

We are now in a position to compare NLIs with simpler interfaces. First, we can see that an NLI depends on sophisticated processing components such as the parser. This is a disadvantage, because it is extremely difficult to build systems that can handle a very wide range of sentences. However, this represents a fixed cost, which should, in the long run, have little effect on the prices of such systems. However, with existing systems, there is always a risk that a parser will fail to parse a sentence, or come up with the wrong interpretation.

In addition, since NLI technology is still limited, organizations must carefully customize the lexicon and knowledge base for their application domain. However, sophisticated install features can help with this customization, and ‘‘NLI infrastructure’’ firms are beginning to market standardized NLI-database systems to different types of users. Finally, since NLIs are still highly imperfect, users may have to learn through trial and error how to work around the limitations of existing NLI systems.

In this paper, we have primarily considered NLIs and other types of user-friendly interfaces as competitors. However, it is possible to combine these two types of interfaces. For example, as discussed in Section 6.1, a natural-language-based information retrieval capability might be combined with an attributeselection procedure to help the user search through long lists of attributes in creating a form or report. Other ways to combine NLIs with menu bases also suggest themselves. For example, if a database is very big, one could break the database up into different views, and build different NLIs customized for those different views. These different views, in turn, could then be accessed through a menu. This may reduce the level of ambiguity each of these NLIs must deal with, and so, make these NLIs more accurate and easier to develop. Alternatively, if an NLI has trouble disambiguating a query, it may present a menu of answers appropriate to different interpretations of the query, and let the user choose between them. This is something like what the Ask Jeeves search engine does in a different context.

While the current paper has focused only on database applications, the relative advantage of NLIs may grow as we moved to more sophisticated systems, such as model bases or expert systems. Of course, with such sophisticated applications, the adaptation of the NLI may be even more complicated. It may therefore turn out that applications, such as information retrieval, requiring less robust natural language processing, may be more appropriate [20,36]. An example of this might be Ask Jeeves. A third set of applications involves voice recognition systems. With voice recognition systems, the most natural language for a user to use is, unsurprisingly, a natural language. While point and click technologies favor menus, voice recognition systems favor ordinary human language. Thus, as voice recognition systems progress, the value of systems, which are able to interpret ordinary natural language sentences will increase. NLP technology is even used in voice recognition technology itself, since a lexicon is needed to translate a string of sounds into words, and parsing helps to disambiguate between various possible strings of words all of which approximate the sounds picked up by the system. Finally, graphic user interface (GUI) systems are being developed which draw on voice recognition, NLP, and point and click technologies (we thank Martha Evens and William Woods for bringing these systems to our attention) These systems allow users to give commands like ‘‘I would like to add that [click] and that [click]’’, to facilitate extremely natural and flexible modes of communication to control computers.

## Acknowledgements

The authors wish to thank Martha Evens, Jon Greenblatt, Steve Hyde, Taha A. Kass-Hout, Penda Tomlinson, Richard Wood, and William Woods for very helpful discussions. An anonymous referee also made extremely valuable suggestions, in particular, encouraging us to interview commercial NLI developers and customers. Sumali Conlon would also like to acknowledge support from the University of Mississippi Faculty Small Grant Program, the Hearin Foundation, and the Office of Naval Research. John Conlon would like to acknowledge support from NSF grant #0215631. Any remaining errors are, of course, ours.

## References

[1] N.R. Adam, A. Gangopadhyay, J. Clifford, A form-based approach to natural language query processing, Journal of Management Information Systems 11 (2) (1994 Autumn) 109– 135.

[2] J.J. Adamski, K.T. Finnegan, C. Hommell, Microsoft Access 2000, Course Technology, Cambridge, MA, 2000.

[3] T.E. Ahlswede, M. Evens, Generating a relational lexicon from a machine readable dictionary, International Journal of Lexicography 1 (3) (1988 Sept.) 214–237.

[4] J. Allen, Natural Language Understanding, 2nd ed., Benjamin/ Cummings, Menlo Park, CA, 1995.

[5] I. Androutsopoulos, G.D. Ritchie, P. Thanisch, Natural language interfaces to databases-an introduction, Journal of Natural Language Engineering 1 (1) (1995) 29 – 81.

[6] C.L. Baker, English Syntax, 2nd ed., MIT Press, Cambridge, MA, 1995.

[7] N. Chomsky, Syntactic Structures, The Hague, Mouton, 1957.

[8] N. Chomsky, Aspects of the Theory of Syntax, MIT Press, Cambridge, MA, 1965.

[9] S. Conlon, M. Evens, T. Ahlswede, R. Strutz, Developing a large lexical database for information retrieval, parsing, and text generation systems, Information Processing and Management 29 (4) (1993) 415 – 431.

[10] M.A. Covington, Natural Language Processing for Prolog Programmers, Prentice Hall, Englewood Cliffs, NJ, 1994.

[11] M.A. Covington, D. Nute, A. Vellino, Prolog Programming in Depth, Scott, Foresman and Company, Glenview, IL, 1988.

[12] EasyAsk, Company Overview and Management Team (www.easyask.com, last viewed, May 7, 2003).

[13] P. Ein-Dor, I. Spiegler, Natural language access to multiple databases: a model and a prototype, Journal of Management Information Systems 12 (1) (1995 Summer) 171 – 197.

[14] ELF, About Us (www.elf-software.com/about.htm, last viewed, May 7, 2003).

[15] ELF, Demos (www.elf-software.com/demos.htm, last viewed, May 7, 2003).

[16] ELF, Store (www.elf-software.com/store.htm, last viewed, May 7, 2003).

[17] S.S. Epstein, Transportable natural language processing through simplicity-the PRE system, ACM Transactions on Office Information Systems 3 (2) (1985 April) 107– 120.

[18] C. Fellbaum, WordNet: An Electronic Lexical Database, MIT Press, Cambridge, MA, 1998.

[19] B.J. Grosz, D. Applet, P. Martin, F. Pereira, TEAM: an experiment in the design of transportable natural-language interfaces, Artificial Intelligence 32 (2) (1987) 173 – 244.

[20] P.S. Jacobs (Ed.), Text-Based Intelligent Systems: Current Research and Practice in Information Extraction and Retrieval, Lawrence Erlbaum, Hillsdale, NJ, 1992.

[21] S. Jagpal, Marketing Strategy and Uncertainty, Oxford Univ. Press, Oxford, 1999.

[22] B. Klein, R. Crawford, A. Alchian, Vertical integration, appropriable rents, and the competitive contracting process, Journal of Law and Economics 21 (2) (1978 Oct.) 297–326.

[23] D.M. Kreps, J.A. Scheinkman, Quantity precommitment and bertrand competition yield cournot outcomes, Bell Journal of Economics 14 (2) (1983 Autumn) 326 – 337.

[24] Language Industry Monitor, TM/2: Tip of the Iceberg? (www.lim.nl/monitor/ibm-tm2-2.html, 1993, last viewed, May 7, 2003).

[25] S. Liebowitz, Re-thinking the Network Economy, AMACOM, New York, 2002.

[26] P. Martin, D. Appelt, F. Pereira, Transportability and Generality in a Natural-Language Interface System, Proceedings of the Eighth International Joint Conference on Artificial Intellegence, Karlsruhe, West Germany, William Kaufmann, Los Altos, 1983.

[27] E. Maskin, J. Riley, Monopoly with incomplete information, Rand Journal of Economics 15 (2) (1984 Summer) 171– 196.

[28] Microsoft, English Query (www.microsoft.com/sql/evaluation/ features/english.asp, last viewed, May 7, 2003).

[29] G.A. Miller, WordNet: an on-line lexical database, International Journal of Lexicography 3 (4) (1990 Dec.) 235–312.

[30] G.A. Miller, WordNet: a lexical database for English, Communications of the ACM 38 (11) (1995 Nov.) 39– 41.

[31] J. Morrison, M. Morrison, Enhanced Guide to Oracle8i, Course Technology, Cambridge, MA, 2002.

[32] S. Nanduri, S. Rugaber, Requirements validation via automated natural language processing, Journal of Management Information Systems 12 (3) (1996 Winter) 9 – 19.

[33] W.Y. Oi, A Disneyland Dilemma: two part tariffs for a Mickey Mouse monopoly, Quarterly Journal of Economics 85 (1) (1971 Feb.) 77–90.

[34] S. Read, The Oracle Edge: How Oracle Corporation’s Take No Prisoners Strategy Has Created an \$8 Billion Software Powerhouse, Adams Media, Holbrook, MA, 2000.

[35] S. Russell, P. Norvig, Artificial Intelligence: A Modern Approach, Prentice Hall, Upper Saddle River, NJ, 1995.

[36] G. Salton, Automatic Text Processing: The Transformation, Analysis, and Retrieval of Information by Computer, Addi son-Wesley, Reading, MA, 1989.

[37] C. Shapiro, H.R. Varian, Information Rules: A Strategic Guide

to the Network Economy, Harvard Business School Press, Boston, MA, 1999.

[38] O. Shy, Industrial Organization, Theory and Practice, MIT Press, Cambridge, MA, 1995.

[39] O. Shy, The Economics of Network Industries, Cambridge Univ. Press, Cambridge, UK, 2001.

[40] J. Tirole, The Theory of Industrial Organization, MIT Press, Cambridge, MA, 1988.

[41] D.L. Waltz, An english language question answering system for a large relational database, Communication of the ACM 21 (7) (1978 July) 526 – 539.

[42] Y.C. Wang, J. Vanderdorpe, M. Evens, Relational thesauri in information retrieval, Journal of the American Society for Information Science 36 (1) (1985 Jan.) 15 – 27.

[43] R. Wilensky, Y. Arens, D. Chin, Talking to UNIX in english: an overview of UC, Communications of the ACM 27 (6) (1984 June) 574 – 593.

[44] O.E. Williamson, The modern corporation: origins, evolution, attributes, Journal of Economic Literature 19 (4) (1981 Dec.) 1537– 1568.

[45] W.A. Woods, Transition network grammars for natural language analysis, Communications of the ACM 13 (10) (1970 Oct.) 591–602.

[46] W.A. Woods, Semantics and quantification in natural language question answering, in: M. Yovits (Ed.), Advances in Computers, vol. 17, Academic Press, New York, 1978.

![](/api/attachments/DETNBKY5/fulltext/images/ea563eee0146afb592880d5cf7ef7fbdaa3b7c89414e664148db37642e75e972.jpg)

Dr. Sumali Conlon is an Associate Professor of Management Information Systems at the University of Mississippi. She received her PhD in Computer Science from the Illinois Institute of Technology in 1990. Her teaching and research interests include Database Systems, Information Retrieval, Knowledge Management, E-Commerce, Web Mining, and Natural Language Processing. Her work has appeared in the Journal of the American Society for Infor-

mation Science, Information Processing & Management, Omega, and Decision Support Systems, among others.

![](/api/attachments/DETNBKY5/fulltext/images/7ef38bc034333467f61dd76f1d0d4fe30056d90026bc6a4639de7ccf85d9894e.jpg)

Dr. John Conlon is an Associate Professor of Economics at the University of Mississippi. He received his PhD from the University of Chicago in 1988. His teaching and research interests include Game Theory, Information Economics, and the Economics of High-Tech Industries. His work has appeared in the Journal of Economic Theory, the International Economic Review, the Journal of Economic Dynamics and Control, and Decision Support Systems, among others.

Dr. Tabitha James is an Assistant Professor of Business Information Technology in the Pamplin College of Business at Virginia Polytechnic Institute and State University. She received her PhD from the University of Mississippi in 2002.
