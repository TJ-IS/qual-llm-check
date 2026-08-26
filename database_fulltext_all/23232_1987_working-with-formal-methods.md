---
otero_id: 23232
otero_key: "8UYVT4PA"
title: "Working with Formal Methods"
authors: "John Nicholls"
year: "1987"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1987.13"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Working with Formal Methods

John Nicholls, IBM United Kingdom Laboratories, Hursley

## Introduction

My experience in working with formal methods began around 1963. Since then I have been involved, with colleagues at Hursley and elsewhere, in a number of projects for developing mathematically-based notations, methods and tools for systems software.

Our work has necessarily been based on an engineering, rather than a scientific approach to programming, emphasizing the creation of products rather than theories. For us, the use of formal methods is not a topic for theoretical research or a means of founding a general theory of computing; it is simply one of the set of available tools for making better software. A question asked of any new method is: 'Does it work?' In particular, we need to say: 'Does it work in our environment, with our products, our people, and our tools?'.

As I will indicate, we are finding that, in appropriate conditions, the use of formal methods does indeed 'work' and is becoming an established part of our development method.

## The case for formal methods

The case for using formal methods can be presented in two ways:

The analogy with engineering This argument can be presented as follows. If we look at established branches of engineering, we see the widespread use of mathematics to support those who design aircraft, electronic circuits or bridges. Many people would like to use mathematics in a similar way to help in the design of programming structures. Wouldn't it be good, they say, if we could calculate the effect of a program, in the same way we can calculate the effect of a design change in a bridge, or an electronic circuit? Hence the ideas for a programming calculus, one of the names for work in this direction of research. Of course, the idea of calculating with programs is attractive, although this dream is made somewhat unreal by the peculiarities of current programming languages.

Relationship to the development process This form of argument is based on the observation that all software development involves some form of symbol processing. There is often a long cycle of development between the first idea for a new piece of software and its delivery as a product. (In our experience, this interval can extend to four years or even longer). Over such periods of time, the documentation for a project becomes critically important, since it represents an accumulation of work in progress. It may be the most stable element of the project, as technology, environment and staff change over time. Given this situation, it is natural that the management of a project will want to capture, at as early a stage as possible, the precise meaning of the symbols in such documentation.

Of the two arguments, the first may be more profound and far-reaching. It has found expression in work by McCarthy, Backus, Hoare and others, and provides a long-term goal for a science of programming.

The second argument provides a basis for much of the current interest in formal methods in industry. Formal methods provide a groundwork for the systematic transformation of the symbols in a specification to the symbols in a final program.

## Limitations and reservations

The fact that the practical application of formal methods in industry has made such little progress, in spite of considerable encouragement and exhortation, may be partly due to the conservatism and inertia of the software industry. However, it also reflects some of the difficulties faced by those who are otherwise in favour of such methods. Some of the issues to be faced before planning their introduction are as follows:

Project management Before deciding to use formal methods, any project should first consider its current methods. Introducing formal methods is not a way of providing control for an otherwise uncontrolled activity. At the very least, the development group should have identified the stages in their process and documented what is to be produced at each stage.

Support Any project starting to use formal methods needs to have support in the form of education and technical consulting in its early stages. Even more importantly, management should provide moral support and encouragement. They need to learn to keep their nerve, especially during early phases of the project. This is because the pattern of work will differ from what they are used to; progress is likely to be much slower at first, though if all goes well there will be compensation as the project reaches later stages.

The scope of formal methods Finally, the use of formal methods can deal only with those topics that lend themselves to mathematical treatment. However strongly a system is formalized, there is still a need for informal descriptions of the system environment and descriptions of how it relates to the world outside the computer system. There are some topics, like the design of user interfaces, which are essentially empirical, and it should be recognized as an established part of the process to produce prototypes for such activities.

## History of the introduction of formal methods

Formal methods have come into their present use in two stages:

\- early use in the description of computer languages; and

\- the introduction of formal methods of development.

I next give some background to our experiences in these two activities.

## The formalization of programming languages

Our first experiences in using formal methods were for the description of computer languages, where they have traditionally had their most consistent and lasting successes. Objectives for this work include providing a greater understanding of computer languages, greater precision in their descriptions and the creation of language standards.

It is interesting to contrast our experience with the formalization of syntax and semantics.

## Syntax

The most successful application of formal notation has been in the precise description of the syntax of computer languages. The BNF notation originally used for the description of Algol 60 remains the most enduring standard for work of this kind. The reasons for its success include the following:

\- The notation is simple and elegant. It says exactly what needs to be said, without forcing attention on unnecessary detail.

\- It helps the reader to understand the structure of a language. An extension to the original notation can be made by introducing the concept of an abstract syntax; this formed a central part of our PL/I language design work at Hursley.

\- It leads to improved and automatic ways of writing parsers.

As we were to discover in later work, the acceptance of formal methods by designers and programmers is critical to their successful use. An important reason for the success of BNF was that users of the notation -- language designers and compiler writers -- had reasons to welcome its introduction.

## Semantics

Following the establishment of a formal notation for syntax, it was natural to work on the formalization of language semantics. As might have been expected, this has proven to be a much more difficult problem. We first used methods of formal semantic definition in producing the formal definition of PL/I. A significant part of the early work on this was begun in the PL/I Language Definition group in Hursley, where we produced formal concrete and abstract syntaxes, informal descriptions of the translator linking them, and an abstract interpreter.

Before work on the PL/I definition was started, several methods were considered, including those based on ideas of McCarthy, Landin, Elgot and others. The method finally chosen was based on what is now called operational semantics, involving the definition of an abstract machine executing an idealized version of a PL/I program. After preliminary work together, responsibility for the work of completing the fully formal definition of PL/I was taken over by the IBM Vienna Laboratory, who had an established reputation in this field. The definition was to be written in the mathematical notation Vienna Definition Language (VDL).

In contrast with our previous experience with BNF, we found the VDL notation and method to be complex and difficult. We spent considerable time educating the users (language designers and compiler writers) in the notation and the method of definition. Although the ULD (Universal Language Definition) documents provided some insight for language designers, the general structure of the language was often obscured by detail. In contrast with our experiences with syntax definitions, the formal semantics of PL/I did not seem to provide significant help to compiler writers.

The PL/I formal specification based on VDL, called the ULD, remains the most thorough and complete work on the formalization of a programming language during its development. It was a tour de force in the use of formal methods, but did not ultimately lead to the widespread use of this style of definition for other languages or systems. The change to a denotational technique of definition and the emergence of the notation and technique known as Vienna Definition Method (VDM) have replaced the VDL work, and provide a direction which has much in common with the Z notation.

## Formal methods of development

Over the past five or six years, we in Hursley, together with other IBM development laboratories, have been introducing formal methods in software development. To support this, there is an extensive education programme and associated tool support. A primary objective is to help in the development of high quality software. Formal notation is used to record first the specification, and then the design of software components. Systematic techniques of refinement are used to ensure that a specification is satisfied by the corresponding design, and similarly that the final code satisfies the design.

One of the formal development projects we have at Hursley is the work using the Z notation in the development of part of the transaction processing system, CICS. (An outline of this project will be described in a paper by Collins, Nicholls and Sorensen, In Press.) I should stress that this is not the only Hursley development project using formal methods of specification and design, although it has special interest in having a stronger emphasis on the specification stage of development.

Two aspects of this work are now discussed, the contribution of the notation, and the effect on the development process.

## Notation

Table 1 contains an evaluation of the Z notation, produced as part of an internal review of the project. These comments are specific to Z, but describe the properties we will look for in any notation to be used at the specification stage of the project.

Much of the Z notation, perhaps about 80 per cent, consists of concepts and notations from standard set theory and logic. These concepts are now familiar to many of our programmers from the education courses they all attend, including the Software Engineering Workshops. The part that is specific to Z, the schema notation, is a simple but powerful extension to standard mathematics that helps in handling the kind of mathematical text encountered in the description of systems software. Independence from a specific programming language has been helpful, since the code of the final product may be written in one of several languages.

Perhaps the most telling point in the list is the final one – the acceptance of the notation by its users, the system programmers working on the project. For the first time, at least in my experience, programmers on this project welcomed the use of formal methods as a help for their work. This means that not only is management encouraging the adoption of formal methods, but the programmers are themselves seeking to use them.

## Process

Table 2 shows some comments made by the manager of the project in which the work is being done:

<table><tr><td>Effects of Z on the process (a development manager&#x27;s view):</td></tr><tr><td>Specification and design concerns can be kept separate– inspections are more productive</td></tr><tr><td>Complete specifications are produced at an early stage– unambiguous– difficult areas cannot be fudged</td></tr><tr><td>Z notation is a tool for ideas– greater confidence at an earlier stage– it has become possible to assess the effect of changes</td></tr><tr><td>Product documentation is more precise, more complete</td></tr><tr><td>It has become easier to move pieces of development between people</td></tr><tr><td>There is a conviction that product quality will be much improved</td></tr></table>

## Table 2. The effects of Z on the development process

You may notice a different emphasis in these comments. Instead of the previous remarks about the precision and mathematical rigour of the notation, a project manager is naturally more concerned about the effect of a new method on the development process.

Throughout this work, we have observed that the introduction of a formal development stage (instead of our previous use of English, or loosely-defined 'pseduo-code') has meant that more work gets done at earlier stages. The balance of work in the project changes, so that inspections of early development stages become more difficult, more time-consuming, but (the crucial point) more productive. This is one of the effects we are seeking from the introduction of formal methods, since we know that early recognition and prevention of design errors is highly effective in improving the process.

## Introducing formal methods

The following notes detail some of our experiences of the Customer Information Control System (CICS) project. These are factors that need to be considered in any project of its kind in commercial software development.

Environment Two aspects are important, the scale of the project and the motivation for using formal methods. Our experience with the CICS project and other similar projects has been limited to groups of 20 or more programmers. It is relatively easy to justify the need for education, consulting support, and tool development for projects of this size.

Motivation for the use of formal methods must come partly from the management, based on the importance and criticality of the software product. It should also come from programmers working on the project, who must wish to work in a professional and dedicated way.

Training and education Although the notation we use appears to be abstract, we have not found difficulties in introducing Z to people with a wide range of educational background, provided there is adequate training for the notation and method. We have found it necessary to provide support in early stages of the project with experienced consultants. It is very helpful to have examples of work using the notation, based on the terminology and techniques used in the product. The provision of case studies (1) was an important step in introducing Z for CICS programmers.

Establishing a project Our first step in introducing the formal methods is to set up a pilot project with about two or three people, providing a nucleus of skill and experience in the particular project we are concerned with. They must be supported by the management and by training consultants mentioned above. We set out to measure the effect of the new methods to provide a basis for later decisions on their use.

Technology needs Notation itself provides the most effective tool but needs to be supported by at least some simple tools for editing, displaying and printing the formal text. It must also be recognized that a new structure for the development process may be needed, reflecting the change in the balance of work done during the long period that a software product is developed and maintained.

## Working with formal methods

I should finally like to indicate what I would regard as effectively 'working with formal methods'. If you read some of the more idealistic descriptions of theoretical computer scientists, you would think that formal methods take programmers into a new kind of world, in which the grime of the software factory is replaced by the clinical atmosphere of the laboratory, the crudities of poring over hex dumps by the scalpel-like precision of mathematical theorems. Such a vision can hardly be sustained as long as we have to work with present staff, on current software. Hence a practical approach to this mode of working might include the following:

```txt
- the establishment of a well-defined and managed development process in which the work to be done at each stage is specified and agreed in advance.
- The use of a mathematical notation to represent the system at each stage.
- A means of validating (verifying, proving) that the results after each stage satisfy the requirements of the previous stage.
- The application of this process throughout the life cycle of the product.
```  
Table 3. Working with formal methods

This may be less ambitious than ardent formalists would like, and may disappoint those who would prefer us to believe that fully formal methods, involving the use of theorem-provers and knowledge-based libraries of designs are just around the corner. However I submit that even this modest step forward would be a worthwhile advance for many groups, bringing the benefits of working with formal methods to many now working in software development.

## Reference

1. Hayes, I. (1986) (ed) Specification case studies. London, Prentice-Hall International.

Biographical notes

![](/api/attachments/8UYVT4PA/fulltext/images/6682524bb3d871a77ff84918ff10e759718be6972435ce97d1c83e2b20b37790.jpg)

John Nicholls is Manager of Software Engineering and Process Technology at IBM United Kingdom Laboratories, Hursley Park, where his group is responsible for the introduction and support of new programming methods. His current work includes the development of formal techniques for developing systems software. His previous experiences with IBM include responsibility for programming language design, and research into the design of user interfaces. In addition to working at Hursley, he has carried out research and development at IBM Research Yorktown Heights, Austin Texas, and ESRI, La Hulpe.

Address for correspondence: IBM United Kingdom Laboratories Limited, Hursley Park, Winchester, Hampshire SO21 2JN.
