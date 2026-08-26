---
otero_id: 25920
otero_key: "YVNUXFUH"
title: "Fact‐oriented modelling for data analysis"
authors: "TA Halpin; ME Orlowska"
year: "1992"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1992.tb00070.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fact-oriented modelling for data analysis

TA Halpin and ME Orlowska

Key Centre for Software Technology, Department of Computer Science, University of Queensland, Australia 4072

Abstract. Although entity-relationship modelling is the most popular means of specifying the conceptual schema for the data perspective of an information system, an alternative design approach known as fact-oriented modelling appears to offer advantages. This paper provides an overview of fact-oriented modelling, including some recent revisions and an evaluation of how the method has coped with large-scale practical applications. One distinguishing feature of the approach is its emphasis on natural verbalization of information examples in terms of elementary facts. This notion of elementarity is clarified to cater for a problematic case involving compositely identified object types. Finally, the algorithm for mapping a conceptual to a relational schema is revised to cater for lazy object types.

Keywords: conceptual schema, data analysis, information systems.

## INTRODUCTION

For reasons such as correctness, clarity, adaptability and productivity, information systems are best specified first at the conceptual level (ISO, 1982). The conceptual design of an information system may include data, process and behavioural perspectives (Olle et al., 1988), and the implementation depends on features of the target system, such as the underlying data model (relational, hierarchic, network, object-oriented etc.) and the location mode (centralized, distributed etc.). For this paper, we restrict our attention to the data perspective, and assume the implementation target is a relational database system.

Many conceptual modelling methods exist (see Jardine & Reuber, 1984; Brachman, 1988; Olle et al., 1988; Sowa 1988). One popular way to design relational data structures is to use entity relationship modelling (ER) to specify the conceptual schema, map this onto a relational schema, and then refine the table structure using normalization (Chen & Dogac, 1983; Teorey et al., 1986). Although similar to ER modelling in some respects, fact-oriented modelling, as exemplified by NIAM (Nijssen's information analysis method), arguably provides a simpler and stronger approach.

Natural verbalization of examples in terms of elementary facts is the foundation of NIAM's design procedure. Its conceptual schema diagrams use only one data structure (the fact type), allow a wide variety of constraints to be expressed, and are easily populated for validation purposes.

Papers by Falkenberg (1976), Verheijen & Van Bekkum (1982), and Vermeir (1983) discuss an early form of NIAM which adopted the Binary Relationship Model. To provide a more natural and direct connection with human conceptualization, relationships of any arity are now allowed. For historical background on the binary-relationship model, as well as an argument for retaining the binary-only restriction, see Mark (1987). Halpin (1989a) provided a logical formalization, and introduced many enhancements. Orlowska & Zhang (1989) and Zhang & Orlowska (1990a) established various connections with normalization theory. A NIAM-based model for a unified architecture of information systems has been proposed by Nijssen (1989). A recent text (Nijssen & Halpin, 1989) provides a detailed introduction to the method.

This paper illustrates the main features of a current version of fact-oriented modelling, and discusses some issues arising from its use in practice. Recent changes to the method are examined, including a new check for derived fact types, and a revised treatment of compositely identified object types. The algorithm for mapping to a relational database system is clarified and extended.

## THE CONCEPTUAL SCHEMA DESIGN PROCEDURE

Most conceptual modelling methods provide a graphical language for the high level specification of conceptual schemas. Of these graphical notations, the conceptual schema diagram language of NIAM is perhaps the most intuitive and expressive. However, as pointed out by Levesque (1984), there is a fundamental trade off between expressibility and tractability. The more expressive a language becomes, the greater the computational complexity of procedures for checking logical results (e.g. constraint implication, or schema equivalence). Partly to keep the problem manageable, most research in database design has restricted the set of constraints to functional and multi-valued dependencies (see Beeri & Kifer, 1986). Nevertheless, in practical database applications the additional constraint categories depicted on NIAM diagrams often occur, and hence should not be ignored.

Though it includes some mechanisms for specifying information flows (information flow diagrams) and modelling an application's behaviour, the emphasis of NIAM is on the design of information structures. In particular, it provides a conceptual schema design procedure (CSDP) for specifying information structures at the conceptual level, as well as an algorithm (the ONF or 'Optimal normal form' algorithm) for mapping these conceptual structures onto normalized relational schemas for implementation in relational database systems.

The conceptual schema design procedure currently comprises nine steps (see Table 1). As a refinement to the procedure presented in Nijssen & Halpin (1989), we include a further derivation check within Step 5. The rest of this section illustrates the basic working of this design procedure by means of a simple example.

Step 1 is the most important stage of the CSDP. Examples of the kinds of information required from the system are verbalized in natural language. Such examples are usually available in the form of output reports or input forms, perhaps from a current manual version of the required system. To avoid misinterpretation, it is usually necessary to have a UoD (Universe of Discourse) expert (a person familiar with the application) perform or at least check the verbalization. As an aid to this process, the speaker imagines he/she has to convey the information contained in the examples to a friend over the telephone.

Table 1. The conceptual schema design procedure (CSDP)

<table><tr><td>1. Transform familiar information examples into elementary facts, and apply quality checks.</td></tr><tr><td>2. Draw a first draft of the conceptual schema diagram, and apply a population check.</td></tr><tr><td>3. Eliminate surplus entity types and common roles, and check for derived fact types.</td></tr><tr><td>4. Add uniqueness constraints for each fact type.</td></tr><tr><td>5. Check arity and logical derivation of fact types.</td></tr><tr><td>6. Add object type, mandatory role, subtype and occurrence frequency constraints.</td></tr><tr><td>7. Check that each entity can be identified.</td></tr><tr><td>8. Add equality, exclusion, subset and other constraints.</td></tr><tr><td>9. Check that the conceptual schema is consistent with the original examples, has no redundancy, and is complete.</td></tr></table>

To begin with, suppose the information system needs to maintain an academic staff directory for a university, as exemplified by the report extract shown in Table 2. The terms 'emp#' and 'ext#' abbreviate 'employee number' and 'extension number'. The information contained in this Table is to be stated in terms of elementary facts. Basically, an elementary fact asserts that a particular object has a property, or that one or more objects participate in a relationship. For the moment, let us agree that a fact is elementary if it cannot be expressed as a conjunction of simpler facts (by 'simpler' we mean the arity of the predicate is smaller than that of the original).

Table 2. Extract from a directory of academic staff

<table><tr><td>emp#</td><td>name</td><td>dept</td><td>ext#</td><td>room</td></tr><tr><td>15</td><td>Cantor G</td><td>Maths</td><td>1900</td><td>55</td></tr><tr><td>20</td><td>Locke J</td><td>Philosophy</td><td>1234</td><td>90</td></tr><tr><td>39</td><td>Russell B</td><td>Philosophy</td><td>1234</td><td>90</td></tr><tr><td>43</td><td>Codd EF</td><td>Computer Science</td><td>2911</td><td>59</td></tr><tr><td>50</td><td>Wirth N</td><td>Computer Science</td><td>2888</td><td>67</td></tr><tr><td>65</td><td>Hagar TA</td><td>Computer Science</td><td>2200</td><td>40</td></tr><tr><td>77</td><td>Cantor G</td><td>Computer Science</td><td>2744</td><td>40</td></tr><tr><td>etc.</td><td></td><td></td><td></td><td></td></tr></table>

As a first attempt, one might read off the information in the first row of Table 2 as the four elementary facts F1–4. Each of these is a binary relationship. Here each binary predicate is shown in bold between the noun phrases which identify the two participating objects.

F1 The Academic with emp# 15 has name 'Cantor G'.

F2 The Academic with emp# 15 works in the Department named 'Maths'.

F3 The Academic with emp#15 uses the Phone with ext# '1900'.

F4 The Academic with emp# 15 occupies the Room with room# '55'.

As a quality check at Step 1, one ensures that objects are well identified. Basic objects are either values or entities. Values are either character strings or numbers: they are identified by constants (e.g. 'Cantor G', 15). Entities are 'real world' objects which are identified by a definite description (e.g. the person with emp# 15). Typically, such a description indicates the entity type (e.g. Academic), a value (e.g. 15) and a reference mode (e.g. emp#). A reference mode is the manner in which the value refers to the entity. In the facts F1–4, the object types are italicized. More complex naming conventions are possible (see Nijssen & Halpin, 1989).

In setting out facts F1–F4, the emp# is unquoted while both ext# and room# are quoted. This indicates the designer treated emp# as a number, but considered ext# and room# as character strings. However, unless arithmetic operations are required for emp# it could have been quoted. Unless ext# and room# must permit non-digits (e.g. hyphens or letters), or string operations are needed for them, they could have been unquoted.

If desired, value types may be explicitly named. For example, F1 could have been expressed as F1': The Academic with emp# 15 has Name 'Cantor G'. Here the value type Name is used, and the predicate is abbreviated to 'has'. It is understood that 'has' predicates are distinguished by expansion (by appending the value type name). For example, the implicit predicate name in F1 is still 'has name.'

As a second quality check at Step 1, the arities of the predicates are inspected to see if some facts should be split or recombined. For example, suppose facts F1 and F2 were verbalized as the single fact F5.

F5 The Academic with emp#15 and name 'Cantor G' works in the Department named 'Maths'.

The presence of the word 'and' suggests that F5 may be split without information loss. The repetition of 'Cantor G' on rows 1 and 7 shows that academics cannot be identified just by their name. However, the uniqueness of emp# in the sample population suggests that this might suffice for reference. As the 'and-test' is solely heuristic, and sometimes a composite naming scheme is required for identification, the UoD expert needs to be consulted to verify that emp# by itself is sufficient for identification. With this assurance obtained, F5 is now split into F1 and F2.

Step 2 of the CSDP is to draw a first draft of the conceptual schema diagram and apply a population check (see Figure 1). Entity types are depicted as named ellipses, and predicates are shown as named box-sequences with the predicate name written in or beside the first role box. Value types are displayed as broken ellipses, usually named. Line segments connect entity types to the roles they play. Reference modes are written in parenthesis. In this example there are four fact types. As a check, each has been populated with one fact, shown as an adjacent row of entries. Facts F1–F4 may be read off this figure.

![](/api/attachments/YVNUXFUH/fulltext/images/0921b4a6ecd1aeecda9a70a357016403aec10146032e342be955d76d16d53de7.jpg)  
Figure 1. Draft conceptual schema for Table 2 with sample population.

The parenthesisization of reference modes is an abbreviation for the explicit portrayal of reference types. For example, the notation 'Academic (emp#)' indicates an injection (1:1-into mapping) from the entity type Academic to the value type Emp#. The astute reader will realize that there is a problem with the fact type for room occupancy: we return to this issue later.

To help illustrate other aspects of the CSDP we now widen our example. Suppose the information system is also required to produce departmental handbooks. Figure 2 shows an extract from one such report. To save space, details are shown here for only four of the 22 academics in that department.

In verbalizing a report, at least one instance of each fact type should be stated. We do not restate that these academics work for the Computer Science Department as F2 is already an instance of this type. Let us suppose that the designer suggests the fact set F6–14. There are problems here. However, to illustrate later checks in the CSDP, we deliberately make some mistakes in the early steps.

F6 The Department named 'Computer Science' has Fax# '3710783'.

F7 The Department named 'Computer Science' has professors in Quantity 5.

F8 The Professor named 'Codd EF' holds the Chair named 'Databases'.

F9 The Professor named 'Codd EF' was awarded the Degree with code 'BSc' at the University with code 'UQ' in the Year 1960 AD.

F10 The Professor named 'Codd EF' heads the Department named 'Computer Science'.

F11 The Department named 'Computer Science' has senior lecturers in Quantity 9.

F12 The Senior Lecturer named 'Cantor G' was awarded the Degree with code 'MA' at the University with code 'ANU' in the Year 1955 AD.

![](/api/attachments/YVNUXFUH/fulltext/images/32b1cd1bc109e1c4f8133f10c78bfab0df23cf8b2bb64433441875d770a6066d.jpg)  
Figure 2. Extract from Handbook of Computer Science Department.

F13 The Department named 'Computer Science' has lecturers in Quantity 8.

F14 The Lecturer named 'Hagar TA' was awarded the Degree with code 'BinfTech' at the University with code 'ANU' in the Year 1986 AD.

As a quality check for Step 1 we again consider whether entities are well identified. It appears from the handbook example that within a single department academics may be identified by their name. Let us assume this is verified by the UoD expert. However, it is required to handle all departments in the one system, and integrate this application with the directory application considered earlier. Because of this it is clear we must replace the academic naming convention used for facts F6–14 by the global scheme used earlier (i.e. emp#). Suppose that we can't see anything else wrong with facts F6–14, and proceed to expand the draft schema diagram to include this new information (this is left as an exercise for the reader).

This leads us to Step 3 of the CSDP: eliminate surplus entity types and common roles, and check for derived fact types. The first part of this step prompts us to look carefully at the fact types for F9, F12 and F14. Currently these are handled as three quaternary fact types, one for Professors, one for Senior Lecturers and one for Lecturers. The common predicate suggests that the entity types Professor, Senior Lecturer and Lecturer should be collapsed to the single entity type Academic, with this predicate now shown only once, as shown in Figure 3. The superscript '+' on the reference mode '(AD)' indicates injection to a numeric type (e.g. years can be subtracted).

![](/api/attachments/YVNUXFUH/fulltext/images/9951849e295260ae0ad299cdc6cbd3c329ce42205e3f6f15bc74cdf9fa1fae78.jpg)  
... was awarded ... at...in...

Figure 3. The three kinds of academics are grouped together.

The second aspect of Step 3 is to see if some fact types can be derived from others. It should be obvious that so long as all the academics are listed, the number of professors, senior lecturers and lecturers can be derived simply by counting. So facts like F7, F11 and F13 are derivable. Derived fact types are specified by derivation rules. If included on the schema diagram they are asterisked. For convenience we transform the three binaries into a single ternary as shown in Figure 4. For a detailed treatment of schema transformations see Halpin (1989b, 1990b, 1991a, b).

![](/api/attachments/YVNUXFUH/fulltext/images/b1c78753fe69af49357fe0062a863ae8e84da6a22568267d425c8d56538ae4a0.jpg)  
... employs academics of ... in...  
Figure 4. A derived fact type.

The superscript '+' on Quantity specifies that this is a numeric value type. In this portrayal, we include the concept of Quantity as a dimensionless count within the concept of Number. If desired, Quantity could be treated as an entity type instead of as a value type.

Step 4 of the CSDP is to add uniqueness constraints to each fact type. A bar across n roles of a fact type ( $n \geq 1$ ) indicates that each corresponding n-tuple in the associated fact table is unique (no duplicates are allowed for that column combination). Arrow tips at the ends of the bar are needed if the roles are non-contiguous (otherwise arrow tips are optional). A uniqueness constraint spanning roles of different predicates is indicated by a circled 'u': this specifies that in the natural join of the predicates, the combination of connected roles is unique.

For example, a fragment of the conceptual schema under consideration is displayed in Figure 5. While these constraints are suggested by the original population, the UoD expert should normally be consulted to verify them. It is sometimes helpful to construct a test population for each fact type in this regard, though simple questions are usually more efficient.

![](/api/attachments/YVNUXFUH/fulltext/images/00c0fa77b0e5d854cfcf0316e5888b52d3d4b0935e5710519f7f2b50e42f905c.jpg)  
Figure 5. Uniqueness constraints added to a subschema.

The intra-predicate uniqueness constraints on the binary fact types assert that each academic uses at most one phone, occupies at most one room, has at most one name, and works for at most one department. The inter-predicate uniqueness constraint stipulates that each name, department combination applies to at most one academic (i.e. within the same department, academics have distinct names). The constraint on the quaternary says that for each (academic, degree) pair the award was made by at most one university in at most one year.

Step 5 provides a more thorough check on the arity and logical derivability of fact types. A sufficient but not necessary condition for splittability of an n-ary fact type is that it has a uniqueness constraint which spans fewer than n-1 roles. Clearly the quaternary in Figure 5 satisfies this condition. Splitting takes place on the key. The quaternary may be split into two ternaries: Academic was awarded Degree at University; Academic was awarded Degree in Year. Alternatively, a nested approach may be adopted (see later). Rarely, a fact type may be splittable without the previous condition: if in doubt, one checks for FDs (functional dependencies) other than the uniqueness constraints; if such an FD is found the fact type is split on the source of the FD.

With practice, the designer typically detects splittability at Step 1 simply by applying 'common sense' or the sense of the UoD expert to verify whether information loss occurs when candidate splits are made. Formally, a projection-join test may be made (Nijssen & Halpin, 1989), but this is usually impractical as it relies on significant populations.

As a refinement to Step 5, we add a check for logical derivability. Derivability of an arithmetic nature (e.g. academic staff count) is fairly common and obvious. Logical derivability can be harder to spot, especially if some important facts were missed at Step 1 (e.g. see Zhang & Orlowska, 1989). We now ask ourselves whether there are any additional relationships between object types, especially any which involve simple keys. With our example, we at last spot that we have missed stating the fact type: Phone is In Room. Suppose we confirm that each phone extension (which is what we mean by 'Phone' here) is in only one room (this is not true in some UoDs). We now add this to our schema. The next phase of the checking procedure is to look for patterns of uniqueness constraints which suggest derivability. The simplest case is transitive implication: a candidate for this occurs in the subschema shown in Figure 6.

Even a novice designer would suspect that one of these binaries is derivable from the other two. As a default design guideline, we usually demand that, if a fact type is derivable, its constraint(s) must also be derivable. It is easy to see, using counterexamples, that the only uniqueness constraint that could be derivable is the one on the fact type: Academic occupies Room. One could also easily deduce this from FD theory. We now ask the UoD expert whether the following derivation rule is true:

## Academic occupies Room iff Academic uses Phone and Phone is in Room.

The answer could be No, but suppose it is Yes. We may now use this rule to derive the fact type: Academic occupies Room. We might leave it on the schema with an asterisk beside it, or simply remove it from the diagram, but at any rate the rule is entered in the textual part of the schema. Notice the use of 'iff' rather than 'if'; unless the rule is a biconditional, it is only partly derivable (for more on this issue, see Halpin, 1989a, 1990a).

To perform this step thoroughly with our example, one needs to also check whether there is a functional relationship from either Phone or Room to Dept. For example, if each room is used, b y only one department we could use this together with the uses and is in fact types to derive the works in fact type (including its uniqueness constraint). However, in developing our example further let us suppose that the UoD expert informs us that no such functional relationship exists (e.g. a joint research laboratory might be occupied by academics from more than one department). Our sample population was not significant in this regard (a common occurrence in practice!). So we do not alter the schema further at this step. Even if such additional functional relationships did exist, other design criteria would typically override the default guideline in deciding which fact type(s) to make derivable (of course the additional functional constraints would still need to be specified and enforced).

![](/api/attachments/YVNUXFUH/fulltext/images/3160891835994a697f0e61cbdcb4c7cbe549fd30f1fc94b7ac35a86ae8d601c3.jpg)  
Figure 6. A pattern suggesting derivability.

As a further example, suppose a novice designer proposes the schema of Figure 7 for a UoD in which technical reports record failures exhibited by computers within an organization. Each computer is identified by its serial number, and the kind of failure is specified by a code. The nested predicate in the right-hand section objectifies computer failure: the top-right binary is transitively derivable from the bottom-right and top-left binaries. Moreover, the nested predicate and its lower binary are probably derivable from the three lower binaries on the left. To check this, the UoD expert is asked whether the dates and times of computer failures match the dates and times recorded on the reports. Let us suppose the answer is Yes: the whole right-hand section of this schema may now be deleted as it is redundant.

This example was actually developed from a functional dependency rather than a factor- oriented approach: it is unlikely that a designer who performed Step 1 would verbalize the redundant section from a sample report, except perhaps to capture the constraint already captured by the inter-predicate uniqueness constraint. Detection of derived fact types is one area where CASE tools can be of assistance (Zhang & Orlowska, 1990b). A formal treatment of the general problem of derivability detection is currently in preparation for a separate technical paper.

![](/api/attachments/YVNUXFUH/fulltext/images/5da605ba27adade11b72d75b868f03652f2b62b24a38cd3f1cd777d39d111b63.jpg)  
Figure 7. Another pattern suggesting derivability.

![](/api/attachments/YVNUXFUH/fulltext/images/ffe89d179d3f8470bbed7e307951dc0e49f5705142b5df0b70978c02f8fc6c97.jpg)  
Figure 8. Mandatory and optional roles on a subschema.

Step 6 of the CSDP is to add object type, mandatory role, subtype and occurrence frequency constraints. Object type constraints specify a list of possible values to which the object type bijects. These usually take the form of an enumeration or range. For example, the academic status is restricted to Professor, Senior Lecturer and Lecturer: this is shown by enclosing the status codes 'P', 'SL' and 'L' in braces (see Figure 8).

A role is mandatory (or total) for an object type if and only if every object of that type which is referenced in the database must be known to play that role. This is explicitly shown by means of a mandatory role dot where the role arc(s) connect with object type ellipse. For example, the dots in Figure 8 indicate that all academics have a status and work for a department, and that each department is worked in by academics. However, the absence of dots on the other roles played by Academic and Dept indicates that these roles are optional: some academics might not hold chairs and some departments might not have fax numbers. Note the 1:1 nature of the optional binaries.

As the inclusion of mandatory role constraints facilitates the detection of derived fact types, the designer may wish to postpone the check for logical derivability until after this has been done. At any rate, now that mandatory roles are specified, subtyping may be determined. Each optional role is inspected: if the role is played only by some well-defined subtype, a subtype node is introduced with this role attached. Subtype definitions are written below the diagram and subtype links are shown as directed line segments from subtypes to supertypes. Consider the two optional roles in Figure 8. There is no rule to define which departments have fax numbers, so the fax# fact type remains as is. However, an academic chair can be held only by a professor, so we must introduce Professor as a subtype for this role. Moreover, each professor must hold a chair, so this role is mandatory for that subtype. This leads to the subschema of Figure 9.

![](/api/attachments/YVNUXFUH/fulltext/images/c2411aa629db9b7f637313acf1a6f818f20bf0aaa65658ba157c4f04cba06f3b.jpg)  
Figure 9. The result of applying subtyping to Figure 8.

While this conveys the main idea of subtyping, our example is a trivial one. Subtyping in NIAM is very flexible. The visual separation of the subtype nodes from their parent node(s) allows directed acyclic graphs of any complexity to be diagrammed. It is understood that subtypes inherit the roles of their supertypes. Multiple inheritance is allowed. Matrix methods enable computation of the subtype graphs from a significant population. For further details on subtyping see Nijssen & Halpin (1989).

The last stage of Step 6 is to add occurrence frequencies. If each object that plays a given role must do so n times, this is an occurrence frequency of n, and is depicted by writing the number next to the role. A uniqueness constraint is an occurrence frequency of 1, and has a special notation of its own as discussed. With our example, no occurrence frequencies need to be added. But were each room to have exactly two phones, then a 2 would be placed next to the role played by Room in the fact Phone-is-in-Room (see Figure 6).

Step 7 of the CSDP considers more complex identification schemes. For example, a BankAccount might be identified by its relationship to a value (its local account number) combined with its relationship to an entity (its Branch, which in turn is identified by its branch number). Some typical examples are given in Nijssen & Halpin (1989, Ch. 7), and some nastier cases are discussed in Halpin & Ritson (1990).

Step 8 adds equality, exclusion, subset and other constraints. As an example, consider the pair-subset constraint shown by the dotted arrow in the subschema of Figure 10. This indicates that if an academic heads a department he or she must work for the same department. Formally, the set of (Academic,Dept) pairs instantiating the heads predicate must be a subset of the set of (Academic,Dept) pairs instantiating the works in predicate. Equality between sets is indicated by a dotted line with arrow heads at both ends, and exclusion between sets is shown by a dotted line with an 'X' mark. For more examples see Nifssen & Halpin (1989, Ch. 8).

![](/api/attachments/YVNUXFUH/fulltext/images/5bdee1895f11f5b09d9beceaf49cea2de22510e73323f5e9f9f174c52dbff0d9.jpg)  
Figure 10. A pair-subset constraint.

The head of department role in Figure 10 is optional. We do not subtype here as we assume that any academic (even an ordinary lecturer) may be head of department. The complete conceptual schema is set out in Figure 11. For simplicity, the derived fact types are omitted from the diagram, though derivation rules are supplied underneath. Notice that the awarding of degrees is handled by using a pair type (Degree, Academic) depicted by framing the objectified relationship (which must be many:many). This nested approach is better than using two ternaries: apart from a simpler picture, this results in fewer tables when passed to the ONF algorithm (see later). For further discussion of such conceptual schema optimization see Halpin (1990b, 1991a, b).

The final step of the CSDP, Step 9, checks that the schema is consistent with the original examples, avoids redundancy, and is complete. No changes are needed for our example. There is a minor derived redundancy, as if someone heads a department, we know from the subset constraint that this person works for that department; but this is innocuous. Other schematizations are possible (e.g. we can define works in and heads to be pair-exclusive, or use a unary is head instead of the binary heads) but we ignore these alternatives here.

## THE ONF MAPPING ALGORITHM

Once the conceptual schema has been specified, a simple algorithm is used to group these fact types into relation types in 'optimal normal form' (ONF). If the conceptual fact types are elementary (as they should be), then ONF is a fully normalized design for which an attempt has been made to minimize the number of tables (for a formal treatment of related issues, see Zhang & Orlowska, 1991). Before discussing the mapping, we define a few terms. A simple key may be thought of as a uniqueness constraint spanning exactly one role; a composite key is a uniqueness constraint spanning more than one role. A compidot (compositely identified object Type) is either a pair type, e.g. (Degree, Academic), or an object type whose primary reference scheme is based on an inter-predicate uniqueness constraint (e.g. if employee numbers were not used, then Academic would be defined by a composite of both Name and Dept). The

![](/api/attachments/YVNUXFUH/fulltext/images/4d03b8406ae8f2f89c0b49559aa96ace60d4fb1d89ac3eb1c9d3829ac88df94b.jpg)

Professor = \_df Academic having Status 'P'

Academic occupies Room iff Academic uses Room and Phone is in Room

Dept employs academics of Status in Quantity iff Quantity =

(select count (\*) from Works\_in

where Academic has Status

and Academic works in Dept)

Figure 11. The complete conceptual schema.

Bank-Account example cited earlier is a compidot whose identification scheme maps to the attribute pair: (branch#, localaccount#). The basic stages on the ONF algorithm are as follows.

1 Initially treat each compidot as an atomic 'black box' by mentally erasing any predicates used in its identification scheme, and absorb subtypes into their super-type.

2 Map each fact type with a composite key into a separate table, basing the primary key on this key.

3 Group fact types with simple keys attached to a common object type into the same table, basing the primary key on the identifier of this object type.

4 Map each remaining fact type to a separate table, basing the primary key on (one of) its keys.

5 Unpack each mapped compidot into its component attributes.

With stage 3, a choice may arise with 1:1 binaries. If one role is optional and the other mandatory then the fact type is grouped with the object type on the mandatory side. For example, the head-of-department fact type is grouped into the department Table. Other refinements to the ONF algorithm have been developed (e.g. other options for 1:1 cases and subtyping, certain derived fact type cases, and partially null keys) but we do not consider these here.

As well as fact types, the conceptual constraints and derivation rules are mapped down. An exhaustive formal treatment of the general mapping procedure is beyond the scope of this paper. A generic notation (partly graphical) is used to specify the Tables and constraints of the resulting relational schema, and the derivation rules are expressed as SQL views. Keys are underlined. f alternate keys exist, the primary key is double-underlined. A mandatory role is captured by naking its corresponding attribute mandatory in its Table (MA is assumed by default), by marking as optional (OP) all optional roles for the same object type which map to the same Table, and by running an equality/subset constraint from those mandatory/optional roles which map to another Table.

Most conceptual constraint notations map down with little change. Constraints on lists of ole-lists (e.g. subset, equality, exclusion) map to corresponding constraints on the attributes to which they map. Equality constraints may be shown without arrowheads. Subtype constraints are typically stated as qualifications to OP marks. Conceptual object types are semantic domains: as current relational systems do not support this feature, domain names are usually omitted. Syntactic domains (data types) may be specified next to the column names if desired: 'the reference mode has a '+', the default data type is numeric, or else the default is character string; the designer typically chooses more specific data subtypes as appropriate.

The conceptual schema under discussion maps to the relational schema shown in Figure 2. The $<2,1>$ in the pair-subset constraint indicates the source pair should be reversed before the comparison: the textual version of this is 'Department[heademp#, deptname] Academic[emp#, deptname]. Derived Tables are shown below the base Tables. The notation $I = _{df}$ is short for 'create view V as'. As with conceptual schemas, relational schemas may be isplayed with various stages of information hiding (e.g. for a brief overview some or all of the constraint layers may be suppressed).

The notion of mapping from a conceptual to a relational schema as a high level alternative, mere normalization has been adopted by several researchers. However, mapping algorithms ased on entity relationship modelling tend to be more complex in their grouping aspect and less comprehensive in their constraint mapping (see Teorey et al., 1986, p. 220; Elmasri & lavathe, 1989, p. 143, 329–334, 427–430).

![](/api/attachments/YVNUXFUH/fulltext/images/54727574af12d96e5fc1399548c09d17c15e3d6e9d21995fcd866e0eb2d0591e.jpg)

'null iff status <> 'p'

Occupies (emp#, room) = df select emp#, room

from Academic Join Phone

Employs (deptname, status, quantity) = df select deptname, status, count (\*)
from Academic
group by deptname, status

Figure 12. The relational schema mapped for Figure 11.

## FACT-ORIENTED MODELLING IN PRACTICE

Though nowhere near as widespread as ER modelling, fact-oriented modelling does have a substantial user base. In this section we provide a brief evaluation of its use in education and industry, based largely on feedback from practitioners in Australia.

At the upper secondary level, a pilot computer science program involving thousands of students has demonstrated that the basics of NIAM can be successfully taught in high school. At the tertiary level, larger numbers of students have been taught the method from first year onwards, and few have had trouble achieving proficiency. There is ample evidence to show that the hardest aspect to master is Step 1, where the information is verbalized in natural language in terms of elementary facts, especially when the information is presented in a novel way. Further experience at the graduate level indicates that even intelligent students with a background in the method find the following topics particularly challenging: metaschemas; complex schema transformation and optimization; and exhaustive constraint mapping. These findings suggest areas of support which ought to be addressed by CASE tools.

Feedback from NIAM users in industry has, perhaps not surprisingly, been very positive. Those who previously used ER modelling found the NIAM notation richer and more intuitive, and felt that being able to populate a schema diagram with sample facts was very useful for checking purposes and communication with the client. The lack of a need to treat attributes in a special way at the early part of the design process was seen to offer two main advantages: stability (e.g. Phone or DeptHead cannot change from an attribute to an entity type as the schema evolves); and natural verbalization revealing all the semantic domains (e.g. 'Person was born in Year'; 'Person died in Year' vs 'Person has Birth Year'; 'Person has Death Year').

Step 1 of the design procedure was considered vital. By focusing on simple facts, expressed one at a time in natural language, the chance of making an error in interpretation was seen to be reduced. It was found that it was safer to use the terms verbalized by the client rather than the terms invented by the designer, who could sometimes be 'a little too creative'.

The ability of a NIAM diagram to depict so much information in the one place was seen as an important safety mechanism for completeness and consistency in the early stages of the design (this also helps with schema transformations, Halpin, 1989a). Later it was useful to be able to hide information in various ways, to prevent information overload when one wanted to focus on different aspects of the schema. Though not yet officially part of NIAM, various ways of information-hiding were used in practice, including sparse-schemas, schema segmentation, and constraint hiding.

One analyst stated that a major feature of NIAM was its extensibility. He had found it easy to add his own extensions to the method to deal with aspects such as dynamic constraints and temporal issues. While this comment may be encouraging, it does point out that standard NIAM is not a complete information system development method. Its emphasis is on the static data perspective. Unlike some other approaches, such as RUBRIC (Loucopolos & Layzell, 1989), it has little to say about dynamic rules and evolution of business policies. Although NIAM includes information flow diagrams, it has yet to integrate data, process and behaviour in a mature, formal way. Various research efforts are under way to address such deficiencies.

Research by Avison & Wood-Harper (1991) suggests that no single method can be appropriate to all situations. They propose a framework called Multiview which can be used to synthesize existing methods to provide a more comprehensive approach to information systems development. The use of this framework to combine NIAM with other methods is an avenue worth exploring.

In spite of the weaknesses just mentioned, NIAM has been used successfully to develop many large applications. Of the applications surveyed, the largest is a forestry management information system known as FORMIS. This application has 20 000 function points, and its conceptual schema includes over 1700 object types and 1500 fact types. Its implementation in a relational database system uses over 600 base Tables and 150 working Tables. Several other applications had conceptual schemas with over 500 fact types.

In spite of their size, these applications were successfully developed using NIAM without the assistance of CASE tools. One reason for this is the small number of NIAM CASE tools in existence (e.g. Intellibase's RIDL\* and Control Data's IAST). This situation is about to change, as commercial companies such as Information Technology International (Brisbane, Australia) and ServerWare (Bellevue, Washington State, USA) are soon to release workbenches to support as commercial companies such as Information Technology International (Brisbane, Australia) and ServerWare (Bellevue, Washington State, USA) are soon to release workbenches to support fact-oriented modelling. In addition, research prototypes are being developed which offer very advanced support for this modelling approach (e.g. see Halpin, 1991c).

## ELEMENTARY FACTS, COMPIDOTS AND LAZY ENTITIES

For reasons such as simplicity, flexibility and non-redundancy, NIAM requires all conceptual fact types to be elementary. In this section we clarify the notion of elementarity for cases involving compidots, and discuss a refinement to the ONF algorithm for 'lazy entities'.

To illustrate the issues, consider a UoD in which academics are primarily identified by their name and department (employee numbers are not used), subjects are identified by subject codes (e.g. CS112), and each subject is taught by exactly one academic. To begin with, let us also assume each academic must teach at least one subject. Figure 13 shows four ways in which a designer may have tried to schematize this UoD.

The ternary in Figure 13(a) has two roles uncovered by a uniqueness constraint. Hence it is compound rather than elementary, and must be split into the two elementary binaries shown in Figure 13(b). Now consider schemas (c) and (d) from Figure 13. These are simple examples of a general case that we wish to clarify, namely a predicate attached to a compidot has a uniqueness constraint spanning all its roles except the role played by the compidot. Is such a predicate elementary? We wish to answer 'Yes', and now argue briefly for this position.

As the splitting of a composite fact type into elementary fact types is an equivalence transformation (Halpin, 1989a, b), splitting must preserve the object types. Unlike Figure 13(b), Figure 13(c) includes the information that the UoD contains the object type Academic which is identified by the academic's Name and Department. So Figure 13(c) should be thought of as elementary, rather than as splittable into the binaries of Figure 13(b).

Figure 13(d) is less straightforward (and less natural). Using the nesting formalization of Halpin (1989a), it is possible to set up a contextual equivalence between it and Figures 13(a) and 13(b). However, an alternative formalization by Halpin based on named, objectified relationship types enables Figures 13(c) and (d) to be contextually matched. Pragmatically, a uniform treatment of compidots for this rare case is easier for the designer.

For such reasons, we permit both Figures 13(c) and 13(d). By demanding that splitting must preserve object types, including explicit pair types, each of 13(c) and 13(d) may be regarded as an elementary fact type; each is a binary fact type (not a ternary), one of which object types is compositely identified. Figure 13(b) is also legal. Indeed, Figures 13(b), (c), (d) all have the same ONF map: Subject (subjcode, lecturer\_name, dept).

Now consider the situation where some academics may teach no subjects. The teaching role played by the compidot in Figures 13(c) and 13(d) is now optional rather than mandatory (visually, the relevant dot is removed). If academics play no other roles, then the compidot is lazy. The notion of laziness was introduced to NIAM by Halpin (1989a) to allow one to record the mere existence of an entity; he later extended this notion to pair-types, but not subtypes or

(a)

![](/api/attachments/YVNUXFUH/fulltext/images/2329b638d78ee50abc2897867fd81b3db3e0f076f865cd49f784cd5651faca66.jpg)

(b)  
![](/api/attachments/YVNUXFUH/fulltext/images/9dcbf888d807781292795127c24ae8e37019583c9225b8114212c6350cded1a4.jpg)

(c)

![](/api/attachments/YVNUXFUH/fulltext/images/3d75a6c11758bd4bffa38f38f431790f1e41773926f35917046a04e9c1490158.jpg)

(d)

![](/api/attachments/YVNUXFUH/fulltext/images/ec7df822f840652638205d1b88804cee59850a7f87ec86ff6a0e74bbfc665fad.jpg)  
Figure 13. Four different attempts at schematization.

(a)  
![](/api/attachments/YVNUXFUH/fulltext/images/4ad43a80439ae1876f4e0d9a8ff7da10364a580e15d3479ec8c473f2db9e9089.jpg)

(b)  
![](/api/attachments/YVNUXFUH/fulltext/images/bdb23eb1cef73cc07b7ae87b0381ef6b353576890f3045ffd13ba5090030f9ef.jpg)  
Figure. 14. In both cases, Academic is a lazy entity type.

value types. A primitive entity type or a pair-type is lazy if and only if the disjunction of its non-referential roles is optional. The referential roles of an object type are those in its identification scheme.

An exclamation mark ‘!’ is appended to the name of a lazy entity type. Figure 14 shows two examples where Academic is lazy: in (a) academics are identified by the combination of their name and department; in (b) by their employee number. The reference scheme in (b) could have been parenthesized. The role played by Subject is implicitly mandatory if the schema is global.

If a role played by an object type is uniquely constrained then it is a functional role of that object type. The ONF algorithm stated earlier causes problems for lazy object types with non-functional roles. For example, Figure 14(a) maps to a single Table: Subject\_academic (subjcode OP, lecturer\_name, dept). Here the primary key may be null, to allow us to record that a lecturer exists although the lecturer may teach no subjects. But wholly null primary keys are a source of potential confusion and inconsistency. To avoid such problems, Stage 3 of the mapping algorithm is amended as follows.

3' Group fact types having simple keys attached to a common object type into the same table, basing the primary key on the identifier of this object type. Each lazy object type with zero or more functional roles maps to a separate Table with its identifier as the mandatory key and its other attributes (if any) optional.

Applying the revised algorithm, Figure 14(a) now maps to two Tables as shown in Figure 15. A pairwise subset constraint between the (name, dept) pairs ensures that only existing academics lecture a subject. For a related discussion of entity integrity and entity identification, see Halpin & Ritson (1990). A comprehensive constraint mapping algorithm will appear in a separate paper.

![](/api/attachments/YVNUXFUH/fulltext/images/ffc168a17b0caf040a1c5f9f6bf51fec3a59111a54e50f1799dcf617c79891e6.jpg)  
Figure 15. The map now obtained from Figure 14(a).

## CONCLUSION

This paper presented an up-to-date review and a practical evaluation of fact-oriented modelling. Although the examples were trivial, most of the main features of this approach were covered, including some recent refinements (e.g. a further check for logical derivation, and a treatment of certain cases involving compositely identified objects and lazy objects). In comparison with Entity Relationship modelling, fact-oriented modelling offers the advantages of simplicity (the fact type is the only data structure), stability (e.g. no changing of attributes like Managers into entities), role-oriented notation (making diagrams populatable), a rich and intuitive notation for constraints, a comprehensive mapping algorithm, and a clear procedure for design based on verbalization in natural language. For completeness the method needs to be either extended (e.g. to formally capture dynamic rules) or combined with other methods. For exposition purposes, the mathematical content of the paper was kept to a minimum. A formal treatment of most of the issues may be found in the references.

## REFERENCES

Avison, D.E. & Wood-Harper, A.T. (1991) Information systems development research: an exploration of ideas in practice. The Computer Journal, 34, 98–112.

Beeri, C. & Kifer, M. (1986) An integrated approach to logical design of relational database schemes. ACM Transactions on Database Systems, 11, 134–158.

Brachman, R.J. (1988) The basics of knowledge representation and reasoning. AT&T Technical Journal, 67, 7–24. Chen, P.P. (1976) The entity-relationship model—toward a unified view of data. ACM Transactions on Database Systems, 1, 9–36.

Chen, P.P. & Dogac, A. (1983) Entity-Relationship Model in the ANSI/SPARC Framework, Entity-Relationship Ap

proach to Information Modelling and Analysis, Chen, P.P. (ed.). Elsevier Science Publishers, B.V., North Holland.

Elmasri, R. & Navathe, S.B. (1989) Fundamentals of Database Systems. Benjamin Cummings, Redwood City CA.

Falkenberg, E.D. (1976) Concepts for information modelling. In: Modelling in Data Base Management Systems, Nijssen, G.M. (ed.). North-Holland, Amsterdam.

Halpin, T.A. (1986) Conceptual schemala and predicate logic. Proceedings of the First Australian Al Congress, Melbourne.

Halpin, T.A. (1989a) A Logical Analysis of Information Systems: static aspects of the data-oriented perspective. PhD dissertation, University of Queensland.

Halpin, T.A. (1989b) Contextual equivalence of conceptual schemas. In: Proceedings of the Advanced Database Systems Symposium, pp. 47–54. Information Processing Society of Japan, Kyoto.

Halpin, T.A. (1990a) Conceptual schemas and relational databases. Australian Database Research Conference Proceedings, Srinivasan, B. and Zeleznikov, J. (eds), pp. 29–8. Monash University, Melbourne.

Halpin, T.A. (1990b) Conceptual schema optimization. Proceedings of 13th Australian Computer Science Conference, Monash University, Melbourne.

Halpin, T.A. (1991a) Optimizing global conceptual schemas. Proceedings of the Australian Database and Information Systems Conference, Sydney.

Halpin, T.A. (1991b) A fact-oriented approach to schema transformation. Proceedings of the MFDBS-91, Roslock (Springer-Verlag).

Halpin, T.A. (1991c) WISE: a workbench for information system engineering. Proceedings of the 1991 Conference on Next Generation of CASE Tools, Trondheim.

Halpin, T.A. & Ritson, P.R. (1990) Entity integrity: a closer look. Technical Report 196. Department of Computer Science. The University of Queensland.

ISO (1982) Concepts and Terminology for the Conceptual Schema and the Information Base, van Griethuysen, J.J. (ed). ISO TC97/SC5/WG3, Eindhoven.

Jardine, D.A. & Reuber, A.R. (1984) Information semantics and the conceptual schema. Information Systems, 9, 147–56.

Levesque, H.J. (1984) A fundamental tradeoff in knowledge representation and reasoning. Proceedings CSCI-84, pp. 141–52. London, Ontario.

Loucopoulos, P. & Layzell, P.J. (1989) Improving information system development and evolution using a rule-based paradigm. Software Engineering Journal, Sept. 259–267.

Mark, L. (1987) The binary relationship model — 10th anniversary. Proceedings of the VIM-47 EMDA Conference. Minneapolis, Nov.

Nifssen, G.M. & Halpin, T.A. (1989) Conceptual Schema and Relational Database Design Prentice Hall, Sydney.

Nijssen, G.M. (1989) An axiom and architecture for information systems. In: Information Systems Concepts: an in-depth analysis, Falkenberg, E.D. and Lindgren, P. (eds), pp. 157–75. North-Holland Publ., Amsterdam.

Olle, T.W., Hagelslein, J., Macdonald, I.G., Rolland, C., Sol, H.G., Van Assche, F.J.M. & Verrijn-Stuart, A.A. (1988) Information Systems Methodologies — A Framework for Understanding, Addison-Wesley, Wokingham, England.

Orlowska, M.E. & Zhang, Y. (1989) Relational database schema design: a comparison between the NIAM and Synthesis approaches. Proceedings of the Second

International Symposium on Systems Research Informatics and Cybernetics, August 1989, Baden-Baden, West Germany.

Sowa, J.F. (1988) Knowledge representation in database, expert systems, and natural language. Proceedings of the IFIP WG2.6/WG2/8 Working Conference on the Role of AI in Database and Information Systems, Kung, C.H. and Meersman, R.A. (eds). North Holland, Amsterdam.

Teorey, T.J., Yang, D. & Fry, J.P. (1986) A logical design methodology for relational databases using the extended entity-relationship model. ACM Computing Surveys, 18, 197–222.

Verheijen, G.M.A. & Van Bakkum, J. (1982) NIAM: An information analysis method. In: Information Systems Design Methodologies: a comparative review, Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds). IFIP, North Holland, Amsterdam.

Vermeir, D. (1983) Semantic Hierarchies and Abstractions in Conceptual Schemata. Information Systems, 8, 117–124.

Zhang, Y. & Orlowska, M.E. (1989) Analysing a NIAM conceptual schema and its transformation into an EKNF relational database schema. Technical Report no. 119, Department of Computer Science, University of Queensland, May 1989.

Zhang, U. & Orlowska, M.E. (1990a) Transforming a NIAM conceptual schema into an EKNF relational database schema. Proceedings of the International Conference on Databases, Parallel Architectures and their Applications, IEEE Computer Science Press, March 1990.

Zhang, Y. & Orlowska, M.E. (1990b) Designing relational databases from NIAM conceptual schemas. Proceedings of the International Conference on System Management, June 1990, Institute of Management Consultants, Hong Kong, pp. 261–265.

Zhang, Y. & Orlowska, M.E. (1991) A new polynomial time algorithm for BCNF relational database design. Information Systems, 16, (in press)

## Further reading

Kent, W. (1978) Data and Reality, North-Holland, Amsterdam.

Kent, W. (1982) Choices in practical data design. Proceedings of the Eighth International Conference on Very Large Data Bases, pp. 165–180. VLDB.

Kent, W. (1986) The realities of data: basic properties of data reconsidered. In: Database Semantics, Steel Jr, T.B. and Meersman, R.A. (eds). Elseviers Science Publishers B.V., North Holland.

Kobayashi, I. (1986) Losslessness and semantic correct-

Kobayashi, I. (1986) Losslessness and semantic correctness of database schema transformation: another look at schema equivalence. Information Systems, 11, 41–59.

## Biographies

Terry Halpin is a senior lecturer in computer science at The University of Queensland, with degrees in science, arts, education, in philosophy, and a doctorate in computer science. His PhD work provided a rigorous formal theory for schema transformations in fact-oriented modelling, and his current research interests focus on conceptual modelling and CASE tools. He has published several research papers, and co-authored two books on logic and one book (with Prof. Nijssen) on conceptual schema and relational database design.

Maria Orlowska is a professor in information systems at the Department of Computer Science at The University of Queensland. She holds MSc (1974) and DSc (1979) degrees in Computer Science from Warsaw University, Poland. Her research interests are: Database Theory, Information Systems Design Methodologies and Analysis of Algorithms. She has published over 70 research papers and reports as a result of research conducted in Poland, Japan, South Africa, USA and Australia.
