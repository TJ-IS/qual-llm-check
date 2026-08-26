---
otero_id: 23298
otero_key: "YPTR8SWG"
title: "Declarative Languages for Advanced Information Technologies"
authors: "Anthony Kosky"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.20"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Declarative Languages for Advanced Information Technologies

Anthony Kosky, Department of Computing, Imperial College

Abstract: In recent times there has been a great increase in interest in declarative programming languages, which are based on sound mathematical formalisms, independent of the machinery on which they are implemented. Such languages are easier to understand and debug, and have advantages with regard to program transformation and verification, and parallel implementation over conventional, imperative languages. In this essay I will discuss the various paradigms available for declarative programming, and also the object orientated programming paradigm, and put forward various ideas that I feel are of particular interest.

## Introduction

In recent times there has been a great increase in interest in what are known as ‘declarative programming languages’. These languages are conceptually very different from conventional ‘imperative’ languages such as Pascal and C. Imperative languages are closely linked with the computational mechanism on which they are implemented. Declarative languages, in contrast, are based on sound mathematical formalisms completely independent of the underlying structure of the machinery on which they are running.

As a result programming in declarative languages should no longer be a matter of constructing a series of instructions manipulating the internal state of a machine, but, instead, is reduced to a matter of expressing the problem to be solved in terms of the given mathematical formalism.

In addition, the mathematical well-foundedness of these languages makes program transformation and manipulation possible, as well as formal verification. Also their independence of the von-Neumann model of computation lends them naturally to parallel evaluation.

These and other advantages mean that the next generation of computer systems will almost certainly be based upon declarative languages.

There are currently two main approaches to declarative languages: 'functional programming languages', such as Hope and Miranda, which derive their semantics from the lambda calculus, and 'logic' or 'relational' programming languages, such as Prolog, which are based on first order Horn-clause logic interpreted in a procedural manner. In this essay I will give a comparison of these two paradigms and try to suggest ways in which they might be improved and the advantages of one might be incorporated into the other. I will assume a basic knowledge of the concepts of the two paradigms. In addition, I will discuss the 'object-oriented programming' paradigm which, while not inherently declarative, incorporates many interesting ideas which could usefully be included in future declarative languages. I will not attempt to give a complete, or even balanced, overview of the subjects covered, but merely to put forward various ideas and points of view that I feel are of particular interest.

## A comparison of the logic and functional programming paradigms

## Notation

There is an immediately noticeable syntactic difference between the two paradigms in that functional programs have their outputs defined implicitly as the right-hand side of the equations defining the program, while logic programs have them named explicitly as an extra variable in the head of the defining clauses. For example, a program, in Hope, to append two lists could be written:

dec append: list(alpha) # list(alpha) -> list(alpha);

-- - append([ ], 1) <= 1;

-- - append (x::11, 12) <= x::append(11, 12);

The first line of this program 'declares' the function append and states that it takes a pair of lists with elements of some type alpha and returns a list with elements of the same type alpha. Here alpha is a type variable: it is instantiated to some actual type each time the function is called. A statement of the form '- - - LEFT <= RIGHT,' means 'replace any expression of the form LEFT by one of the form RIGHT'. So the second line means 'replace a list 1 appended to an empty list by the list 1' ([] is used to represent the empty list). The notation 'x::1' means the list with first element x and the elements of the list 1 as the rest of the list. So the last line means 'the list 12 applied to the list x::11 (the list consisting of the element x added on to the beginning of the list 11) should be replaced by the element x added on to the front of the list formed by appending the list 12 to the list 11'.

Hence if the function append is called with a pair of lists, 11 and 12 say, then if the first list, 11, is empty then it returns the second list, 12. If, on the other hand, 11 is not empty then it removes the first element of 11, applies append to the remaining list and the list 12, and then adds the first element of 11 on to the front of the resultant list.

In Prolog an equivalent program would be:

```prolog
append([], L, L).
append([X|L1], L2, [X|L3]): - append(L1, L2, L3). L3).
```

Here the notation '[X:L]' is used instead of 'X::L' to represent a list with first element X and L as the rest of the elements. Also capital letters are used, instead of small letters, for variables (both these differences are purely syntactic and can safely be ignored). The notation ': - ' means 'if' or 'is implied by'.

The first line of the program means 'a list L appended to the empty list is the first list L'. The second line means 'if the list L2 appended to the list L1 is the list L3 then the list L2 appended to the list [X';L1] is the list [X';L3]).

The extra parameter is necessary in order for the multiple use of clauses (see later). However it does make it necessary to think of an extra variable name (which is a pain) and it makes programs less readable.

## Typing

Logic programming languages are generally untyped (there are typed versions of Prolog but these are not much use and are frowned upon by the logic programming community). Most modern functional languages, on the other hand, are strongly typed and support polymorphism (in the examples of Hope programs given here the 'dec' line at the beginning of each function definition defines the 'type' of the function in terms of the types of its parameters and the type of the parameter it returns). Members of the functional programming fraternity claim that strong typing makes programs less prone to errors and easier to understand, and that having to define types makes the programmer think about what the program is actually doing. As a result, they say, type checking greatly improves programmer productivity. Logic programmers, however, are not convinced that type checking is either necessary or worth while.

## Higher order

Most modern functional languages are 'higher order'.

This means that functions are themselves 'first class objects' which can be passed as parameters and returned as values. For example, in Hope, one can write a function map which applies a given function to each element of a list as follows:

dec map: list(alpha) # (alpha -> beta) -> list(beta);

Here the first line says that the function map takes a list of elements of some type alpha and a function mapping elements of type alpha on to elements of some type beta as parameters and returns a list of elements of type beta (here beta is another type variable). The second line says that map applied to an empty list and any function, f, returns an empty list. The last line means that map applied to a list, x::1, and a function, f, applies map to the list 1 (x::1 with the first element removed) and the function f, and then adds the element f(x) (the element formed by applying the function f to the element x) to the front of the resultant list. Hence map (1, f) goes through the elements of 1 recursively applying the function f to them, and forms a new list containing the results.

Such functions can then be put to various uses. For example, we could write a function to take a list of integers and return a list of factorials of those integers as:

```rust
dec fact : num -> num;
-- -- fact(0) <= 1;
-- -- fact(succ(n)) <= succ(n) * fact(n);
dec fact_list : list(num) -> list(num);
-- -- fact_list(1) <= map(1, fact);
```

So fact is a function from natural numbers to natural numbers such that fact applied to 0 is 1, and fact applied to the successor of some number n (ie the number $n + 1$ , and, therefore, a non-zero number) is the number succ(n) (the number to which the function was originally applied) multiplied by the number formed by applying fact to n.

The function fact\_list calls on map to apply the function fact to each element of a list 1.

Alternatively, one could write a function to return the first element of each list in a list of lists:

dec head : list(alpha) -> alpha;

```txt
-- - head(x::1) <= x;
```

dec head\_list: list(list(alpha)) -> list(alpha);

```txt
-- - head_list(1) <= map(1, head);
```

Clearly the function head applied to a list of elements of type alpha returns the first element of the list. The function head list uses map to apply head to each list in a list of lists of elements of type alpha and so returns a list of elements of type alpha.

In general, one can express many similar algorithms as instances of one generic function, which leads to more concise and readable programs. Logic programming languages do not have this capability.

## Multiple mode use of relations

Logic programs allow relations to be used in various 'modes'. For example, the append program defined earlier can be used in its normal mode to concatenate two given lists, as in append ([1, 2], [3, 4], L)? which would unify L with the list [1, 2, 3, 4]. Alternatively, it could be used to find a pair of lists which, when one was appended to the other, would make a given list, as in append (L1, L2, [1, 2, 3, 4])?, which would yield the solutions:

$$
\begin{array}{c} \mathrm{L1} = [ ], \mathrm{L2} = [ 1, 2, 3, 4 ], \\ \text {and L1} = [ 1 ], \mathrm{L2} = [ 2, 3, 4 ], \\ \text {and L1} = [ 1, 2 ], \mathrm{L2} = [ 3, 4 ], \\ \text {and L1} = [ 1, 2, 3 ], \mathrm{L2} = [ 4 ], \\ \text {and L1} = [ 1, 2, 3, 4 ], \mathrm{L2} = [ ], \end{array}
$$

(Note: This also demonstrates the non-deterministic nature of logic programming of which more later), or it could be used to give the difference between two lists, as in append ([1, 2], L, [1, 2, 3, 4])?. It can even be used with all its parameters instantiated simply to check that one list is the concatenation of two other lists, as in append([1, 2], [3, 4], [1, 2, 3, 4])?.

This capability makes logic programs more expressive than their functional counterparts in that one logic program can do the job of several functional programs.

However, there are problems: in Prolog many predicates will work when used in one mode but will go into an infinite loop when one attempts to use them in some other mode. For example, consider a program to reverse the order of the elements of a list defined by:

$$
\begin{array}{l} \text { reverse } ([ X ^ {\prime} X s ], R s): - \text { reverse } (x s, R s 1), \\ \text { append } (R s l, X, R s). \\ \text { reverse } ([ ], [ ]). \end{array}
$$

This goes through a list, taking an element off the front, reversing the rest of the list, and then adding the element on to the end of the reversed list.

It will work fine when called as, say, reverse ([1, 2, 3], R)?, instantiating R to [3, 2, 1], but if it is called with the first element uninstantiated, as in reverse (R, [1, 2, 3]), it will not terminate.

RESULT: Programmers using Prolog have to give consideration to how predicates are likely to be called in a program and which parameters will be instantiated. This is, to say the least, a little at odds with the idea of declarative programming. What's more it tends to cause bugs in programs (and, worse still, it usually causes bugs which are very difficult to spot).

As a further example of the non-declarative nature of Prolog let us look at an example of a problem caused by a combination of the above problem and the fact that Prolog tries to solve sub-clauses in sequential order. Consider a program to concatenate three lists defined by:

$$
\begin{array}{l} \text {append3 (Xs, Ys, Zs, Ls) : - append (XYs, Zs, Ls),} \\ \text {append (Xs, Ys,} \\ \text {XYs).} \end{array}
$$

If called with the first three arguments instantiated and the last argument uninstantiated then this program would go into an infinite loop without returning a solution. However, if the program were changed to:

$$
\begin{array}{l} \text {append3 (Xs, Ys, Zs, Ls): - append (Xs, Ys, XYs),} \\ \text {append (XYs, Zs, Ls).} \end{array}
$$

then it would work perfectly, even though, logically, both clauses have exactly the same meaning (this problem could be cured by the use of suspensions as described later).

Unfortunately, this non-declarativeness is not particular to Prolog but is common to all attempts to implement logic programming languages that I know of. It is possible to avoid the problems noted above by introducing other non-declarative features. Alternatively, one can adopt a search strategy which finds all possible solutions to a problem before going off into an infinite loop. However this is not a terribly satisfactory solution and, also, would be computationally very expensive. It is, perhaps, one of the most convincing arguments in favour of functional programming languages that they are fairly easy to implement, while one can, at best, only implement a rather poor approximation to a logic programming language which isn't even declarative.

There is a further problem with multiple mode use of predicates in that a clause is usually written with one particular mode of use in mind, and often does not work efficiently in other modes of use. In such cases one would be better off writing a separate function corresponding to each way in which the predicate would be used.

## Non-ground variables

Logic programming, unlike functional programming, allows programs to return results containing uninstantiated variables (in logic programming jargon terms which are not 'ground'). For example, consider a clause to return the first element of a list:

$$
\text { head } ([ \mathrm{X} | \mathrm{L} ], \mathrm{X}).
$$

Clearly, if this were called in a query such as head ([1, 2, 3], X)?, it would instantiate X to 1, but what would happen if it were called as head(X, 1)?. The answer is that it would return a list of the form [1;L] where L is an uninstantiated variable. Terms generated in this manner can be used as templates for other clauses. For example, one could write a program, front\_up\_to, which checks to see if an element, X, is in a list, L, and if it is then returns the front of the list up to the element X, as:

$$
\begin{array}{l} \text { front\_up\_to } (L, X, L 1): - \text { head } (L 2, X), \text { append } \\ (L 1, L 2, L). \end{array}
$$

Functional languages do not have this capability and are, in this respect, less expressive than logic languages.

## Non-determinism

Functional languages are deterministic, that is a function admits only one possible solution for each possible set of inputs. This deterministic nature of functional languages, together with various mathematical properties, means that it is unnecessary to incorporate search strategies (mechanisms to search all possible ways of solving a problem) in implementations of the languages. This yields a substantial improvement in efficiency and speed of execution when compared to logic languages.

Logic programs, on the other hand, are non-deterministic: a logic program can give several possible answers to a query, each one corresponding to a different way of proving the goal (for an example of this see the append example given earlier). This is very useful for expressing and solving problems which are inherently non-deterministic, eg problems which, at some stage, require the program to choose between several possible solutions of a sub-problem.

It is worth while pointing out again that Prolog is not 'complete', that is it does not necessarily find all possible solutions to a problem. If one adopts a breadth-first, rather than depth-first, search technique then one will find all possible solutions. However, this would be very expensive in terms of the memory required to implement it.

## Unification v pattern matching

If one looks for the origins of the differences between functional and logic languages one finds that most of the important ones are caused by the differences between the methods used for matching variables to clauses and function definitions in programs. Functional languages use ‘pattern matching’ while logic programming languages use the more powerful and general method of ‘unification’.

In unification, when a goal is matched to a clause head, in fact the clause head is matched to a term by means of an 'input substitution' and the goal is matched to the same term by means of an 'output substitution'. For example, unifying the query append ([1, 2], [3, 4], L)? with the clause

$$
\text { append } ([ X | X s ], Y s, [ X | Z s ]): - \text {   append } (X s, Y s, Z s)
$$

yields the input substitution $\{X \to 1, Xs \to [2], Ys \to [3, 4]\}$ and the output substitution $\{L \to [X|Zs]\}$ .

It is the seemingly innocuous output substitution that is missing from pattern matching and that can be said to be responsible for all the important differences between functional and logic programming. (Those differences that it does not cause can be shown to be either merely syntactic or additional restrictions and constructs that have been tacked on to the underlying paradigm and could equally well be added to the other paradigm. Either way, they are of no real consequence.)

## Object-oriented programming

An ‘object’ is some entity which has an internal state and which can perform various acts on its state when it receives ‘messages’ from other objects. Each object has a selection of ‘methods’ available to it, each of which can be activated when it receives a message from another object. After it has completed a method it will send an object, often itself, to the object which sent it the message. An object-oriented programming system is itself made up of objects. Virtually all the basic data types are objects, and the programming constructs are methods defined on those objects. One does not so much write a program ‘in’ the language as extend the language with new objects which define the program.

In most object-oriented programming systems each object has a 'class' of which it is an 'instance'. The class (which is itself an object) defines what memory the object has allocated to it and how it is arranged, and also what methods it has available to it. One of the most powerful features of such systems is that classes are arranged in a hierarchy with 'inheritance'. This means that an object which is an instance of one class can use messages defined in its 'superclass' (the next class up in the hierarchy). When an object receives a message it first checks its own class definition for a corresponding method and then, if it does not find one there, it starts working its way up the hierarchy, until it finds a suitable method (or gets to the top, in which case it fails). This means that one can write very general methods which cover a large range of classes and leave the more specific details to other classes lower down the hierarchy. For example, if one were writing a function which would be applied to both real numbers and integers one would write it as a method for the class Number of which Real and Integer would be subclasses. The operators, plus, multiply and so on, would be defined differently for the two classes and, if the function called on them it would go back to the starting class in order to try to find them.

The object-oriented approach leads to very modular and structured programs. Also it makes it extremely easy-to-reuse code. In order to use a previously defined object one need not know anything about its internal workings or how it is implemented, only how it behaves to the outside world. Equally, one can completely rewrite an object, for example to make one of its methods more efficient, without affecting the overall behaviour of any of the objects that use it, providing one doesn't alter the way it appears to behave to other objects. These are goals that people have tried very hard to achieve with various 'structured' languages with only limited success.

## Applicability of the paradigms to parallel processing

It seems likely that the next generation of computer systems will be based on parallel architectures. After all, one of the main aims of current research is to simulate the human brain which is itself a parallel system. Also it is becoming increasingly difficult to make faster and more powerful machines based on the now-ageing von-Neumann architecture which must, by now, have taken us almost as far as it can go. As a result, the importance of a programming paradigm to AIT and the next generation of computers may well be dependent on how well it can be made to work on parallel machines.

In order to decide how applicable a programming paradigm is to parallel evaluation one must look at it from two points of view.

First, one must consider to what extent one can take advantage of parallelism in an implementation of the language, that is by what methods one can make use of parallelism when evaluating a program written in the language, and how easy it would be to incorporate the methods into a system implementing the language. This is looking at things from a purely technical point of view.

The second way of looking at things is from a more programming-oriented point of view: in order for it to be worth while to implement a language on a parallel architecture, the language should help the programmer to think about problems in a parallel way and write algorithms that take advantage of parallelism in solving a problem.

## The applicability of object-oriented programming

If one first looks at object-oriented programming systems one finds that they score very highly from the second, programming, point of view. An object can be thought of as a little processor, with its own lump of memory (instance variables) and its own set of programs (methods), which communicates with other processors (objects) by sending messages backwards and forwards, and executes programs depending on the messages it receives. In this way object-oriented programming systems mirror the structure of a parallel computer. They force the programmer to think in terms of lots of little processes running concurrently and communicating with each other, and hence help him or her to write programs which work well in this way. Also they take some work off the hands of the computer by not making it have to decide on how to split processes up.

## Applicability of functional programming languages

Unfortunately functional programming languages make poor languages for parallel machines for the same reasons that object-oriented languages make good ones. Functional languages are excellent at mirroring the structure of sequential processes. A computer program (and indeed a computer) can be thought of as a black box: one puts the inputs in at one end and gets an output out at the other. Functions preserve this structure as one looks at programs at greater levels of detail (in other words, they split the program into a sequence of little black boxes). This tends to lead to a sequential way of thinking about programs.

This does not mean that one can't make use of parallelism in evaluating functional programs. Graph reduction techniques, as used in the Alice machine being developed at Imperial College, makes maximal use of parallelism in evaluating functional expressions. However, this is making use of parallelism on a micro, rather than a macro, scale: programs are split up into as small pieces as possible and these pieces are then evaluated as they are shown to be necessary, rather than splitting the program up into smallish chunks and then evaluating each chunk sequentially. This approach means that the computer puts more effort into linking and organizing the various pieces of the program than it does into actually evaluating them, and wastes a great deal of computational effort.

## The applicability of logic programming languages

Initially logic programming as a paradigm seems to fit in very well with the ideas of parallel processing since there is nothing inherently sequential about Horn clause logic (on which the languages are based). However, in real programs the order in which an interpreter tries to solve the goals of a query can make a vast difference to the efficiency of a program. For example, consider a clause which finds members of a list of integers that are less than 1000:

$$
\text { member\_1\_t\_1000 } (X, L): - \text { member } (X, L), X <   1 0 0 0.
$$

Suppose that member 1\_t\_1000 is called with a fairly short list L. If the interpreter decided to solve the goal member (X, L) first then it would go through all the elements of L checking to see if they were less than 1000, which would be quite an efficient solution. If, on the other hand, it were to try to solve the goal X < 1000 first then it would generate each integer less than 1000 and test it to see if it was a member of L, which would be extremely inefficient, especially if all solutions were required.

These problems can be alleviated by incorporating constructs such as ‘suspensions’ and ‘read only variables’ in a language in order to tell the interpreter to wait for certain variables to be instantiated before it evaluates a particular clause. However, this would make it necessary for the programmer to think about how the interpreter actually works, and, once again, is somewhat at odds with the ideas of declarative programming.

## Some ways of improving functional programming languages

## Set abstraction

One of the main reasons for using logic programming rather than functional programming languages is in order to handle non-deterministic problems. However, using a non-deterministic interpreter where it is not necessary is very inefficient, so it would be nice to be able to only use non-determinism when it is needed and not the rest of the time.

One way to simulate non-determinism in functional language is to use 'set abstraction'. A set is a collection of elements without repetition (that is, no element occurs more than once). We could denote such a set in a functional language by a list of elements enclosed in curly brackets, for example $\{1, 2, 3, 4, 5\}$ . Unlike lists, however, two sets are equal if they have the same elements, regardless of the order in which the elements are arranged, so, for example, $\{1, 2, 3\} = \{2, 3, 1\}$ . In order to make sets useful we also need a 'such that' construct. We could denote this by a construct of the form $\{X|p(X)\}$ , which would mean the set of all elements X such that $p(X)$ is true. For example, in Hope extended with these constructs, a program to find all the pairs of lists which, when one is appended to the other, make a given list would be:

dec split : list(alpha) -> set(list(alpha) # list(alpha));

-- - split(1) <= (11, 12) | append(11, 12) = 1 .

(This is equivalent to the Prolog append function given earlier used in the second mode of use described.)

In addition, in order to make use of sets, we would need operators member\_set and empty\_set with the obvious meanings. More complicated set operations could easily be built from these basic operators, for example set union:

dec union : set(alpha) # set(alpha) -> set(alpha);

-- - union(s1, s2) <= {x | member\_set(x, s1) or member\_set(x, s2).

## Type hierarchies and inheritance

When writing programs it is useful to be able to restrict the parameters accepted and values returned by a function to as small a class of different types as possible. For example, if one were to write a function which is only supposed to be applied to natural numbers, it would be useful to be able to define it as a function on the natural numbers, rather than on the integers or even the real numbers.

There are two main reasons why this would be desirable: first, it would help the interpreter spot any errors which involved applying a function to the wrong kind of data, and, secondly, it would make the programmer think about what kind of parameters a function will be used for and, also, would provide more information about how the program worked to anyone reading or maintaining it at a later stage.

However, if one had a data type of integers and were to define one of natural numbers then one would still want to be able to apply any functions on integers to natural numbers (but not the other way round).

One way of organizing this would be to incorporate 'type hierarchies' and 'inheritance', as used in object-oriented languages, into a language. This would mean that we could declare certain types to be 'subtypes' of other more general types (natural numbers would be a subtype of integers, capital letters a subtype of characters, and so on). If one type was a subtype of some other type this would mean that everything of that type would also be of the other type (natural numbers are also integers, capital letters are characters, and so on) and could be used by any function requiring a parameter of the second type.

However, we would not want to specify every subtype relation: we would only want to give certain, basic, subtype relations and would want the interpreter to deduce all the others. For example, if we defined capital letters to be a subtype of letters and letters to be a subtype of characters, we would want the interpreter to deduce that capital letters are also a subtype of characters. Furthermore, a list of capital letters is also a list of characters so the interpreter should deduce a subtype relation between these two types of lists. Similarly, a function mapping integers on to capital letters is also a function mapping natural numbers on to characters, and we would want another subtype relation to express this.

These relations could be deduced from the given, basic subtype relations by means of a set of 'inference rules' which could be built into the type-checking mechanism of our interpreter.

For some functions it would be useful to be able to define the function for some type, T, and then give a more specific definition for some subtype of T. For example, integers are also real numbers and so we would like a type integer to be a subtype of reals. However we would not want to use the same definition of the basic arithmetic operators for both integers and reals. We could cope with such situations by arranging for the interpreter to always use the most specific version of the function possible (however this would preclude multiple inheritance, ie we could not define a type to be a subtype of two different types because this might cause non-determinism).

## Some ways of improving logic programming languages

## Conditional equalities

There are cases, in logic programming, where functional notation would be preferable to relational notation. For example, many logic programs are intended to be used in a functional rather than a relational manner (ie certain parameters are intended only to be used as inputs and certain parameters are intended as outputs). Consider, for example, a program length (L, N), the intended meaning of which is 'the length of the list L is N', given by the Prolog program:

```prolog
length([X|Xs], N) : - length(Xs, N1), N is succ(N1).
length([], 0).
```

The actual, logical meaning of this program is 'a list L and an integer N are in the length relation if the number of elements of L is N'. This is particularly misleading because, in this case, the program would go into an infinite loop if it were called with the first variable uninstantiated. Also the first clause of the program contains a sequence of the form:

```txt
... pred( ..., N1, ...),
... N1 is ex(N), ...
```

Such sequences are common in Prolog, and in most languages would be written:

```txt
... pred(...,ex(N),...). ...
```

which is a much more elegant notation and gets rid of an extra, unnecessary, variable. A more functional notation for the program would be:

```javascript
length([X|Xs]) = succ(N) : - length(Xs) = N.
length([]) = 0.
```

This is more concise and elegant, and makes the meaning of the program clearer.

So what we would like is a way of incorporating such functional notations into a logic language. One way of doing this would be to extend the logic language to include 'conditional equalities'. A conditional equality is an expression of the form:

```txt
t1 = t2 : - C.
```

Such a clause would read 'the term t1 can be replaced by the term t2 if the condition C holds'.

There are two ways that one can handle such expressions. The first is to use a pre-compiler that converts programs containing such expressions into regular logic programs. For every pair of clauses in the source program of the form

```txt
head ( . . . ,11, . . . ): - conds.
t1 = t2 : - C.
```

it would add a clause

```txt
head( . . . ,12, . . . ): - conds.C.
```

to the output program. Similarly, for a pair of clauses of the form:

```txt
head: - ... ,pred( ..., t1, ..., ) , ...
t1 = t2 : - C.
```

it would add a clause

```txt
head: ... pred(...,12,...). C...
```

Alternatively, one could extend the interpreter to interpret the expressions at run time. In this case when the interpreter came across a term, pred( . . . , t1, . . . ), and there was a matching clause, t1 = t2 : - C, it would try to solve the goal C and, if it succeeded, it would rewrite the term to pred( . . . , t2, . . . ) and carry on. This method would allow for recursive use of the conditional equalities, but would have much more complicated denotional semantics.

## Suspensions and read-only variables

Another useful extension to Logic programming languages would be the use of 'suspensions'. This would involve marking certain parameters to show that the term in which they occur should not be used until they are instantiated. One possible notation would be to append certain symbols to parameters. We would need two kinds of symbols for appending to parameters in clause heads, say '&' and '+'. '&' would mean 'this clause cannot be used without this parameter instantiated'. For example, consider the reverse program rewritten as:

```prolog
reverse([|&, |]). reverse([X|Xs|&, Rs): - reverse(Xs, Rs1), append(Rs1, [X], Rs).
```

This would only work to return the reverse of the first parameter or to check that the second parameter is its reverse.

The ‘+’ could be followed by an optional label (there could be several such labels in a single clause head and each one would be local to that clause head). ‘+ (label)’ would mean ‘this or one of the other parameters followed by + (label) must be instantiated in order to use this clause’. For example, the append program could be rewritten:

```prolog
append([X|L1|+, L2, |X|L3|+): - append(L1, L2, L3).
```

append( $||+$ , L, L+).

This would mean that append could not be used without either the first or the last variable instantiated (if it were allowed to be called in this manner then it would go into an infinite loop anyway). (Note: ‘+’ followed by a unique label could be used instead of ‘&’, ‘&’ is suggested only to make programs more readable.)

These constructs would also allow us to have several different definitions of a single predicate so that the interpreter could decide which one to use depending on which variables were instantiated.

We would also need a symbol, say '?' to put after parameters in the terms of a clause body. '?' would mean 'do not attempt to solve this goal until this parameter is instantiated'. The interpreter would suspend a call if the correct parameters were not instantiated, and go on to try to solve the rest of the goals in the clause and see whether the necessary variables became instantiated. If so then it would try to do the call again, otherwise it would fail. For example, we could rewrite our member\_1\_t\_1000 program as:

member\_1\_t\_1000(X, L): - member(X, L), X? < 1000.

## Hierarchies of databases

Large programs written in logic programming languages become very difficult to read and understand (and consequently very difficult to debug). Also errors and side-effects are caused by unintentionally overlapping definitions or by accidentally using the same identifier twice. It is, therefore, very necessary to find a way of structuring logic programs and making them modular. It seems natural to use some of the ideas from object-oriented programming and to adopt a hierarchical system of databases.

Each database in the hierarchy would inherit all the statements and clauses from its parent databases and supplement them with its own. For example, the append and member clauses would be put quite high up in the hierarchy so that they would be available to all the databases lower down.

The non-deterministic nature of logic programming would make multiple inheritance possible (ie a database could have several parent databases and inherit from all of them). If a database called a clause which was defined in several different databases to which there were paths for it in the hierarchy, then each one would count as a different solution and would be handled in the normal way. A system of flags could be used to prevent a database being used more than once for the same call. For example, a call to append would give only one solution rather than the same solution once for every path in the hierarchy to the database in which it is defined.

Each database would have a label and would be defined by its label followed by its list of clauses and statements. The inheritance rules would be listed separately by a sequence of 'is\_a' statements. Databases could send queries to other databases by calling their label followed by the goal to be solved.

## Yet another problem with logic programming

There is another problem with logic programming languages which I have not yet pointed out, and which, oddly enough, is due mainly to its name. Many people (including many logicians who should know better) seem to think that logic is something natural and intrinsically correct. They think that it is a formal expression of the processes that we, as human beings, use to reason with. In fact it is simply a language of symbols together with a set of postulates, which happens, for some very simple examples, to give a fairly poor approximation of the way we reason about things. This does, of course, create a great deal of confusion.

Furthermore, people tend to think that Prolog (and other so-called logic programming languages) really are logic programming, while in fact they are only very poor approximations of it. As I demonstrated earlier, one can have perfectly good logic programs that don't work as Prolog programs, and other logically identical programs which do.

This generally causes a lot of errors and also makes them very difficult to spot. One can have programs which are clearly 'reasonable', and indeed seem 'logical', but which fail inexplicably when one tries to run them.

In my opinion, all references in books or articles to 'logic programming' should be changed to read 'relational programming'. What's more, all references to 'classical logic' should be changed to something like, say, 'relational calculus', and, of course, Prolog should be given a completely new name and new documentation that doesn't mention even relational programming.

## Conclusion

Clearly, declarative programming languages have a great deal to offer for future generations of computer systems. However, while both the functional and the logic programming paradigms do have major strengths, both paradigms still leave a great deal to be desired. What is necessary is either an extension of one or the other of the languages to include the good points of the other, or, better still, an entirely new paradigm based on some different mathematical formalism which avoids the pitfalls of existing declarative languages while retaining their strengths. It would probably be better to develop an entirely new mathematical formalism for the specific purpose of providing a basis for a programming language, rather than trying to adapt some existing mathematical system which was originally conceived for some other reason.

Object-oriented programming languages, while not in themselves declarative, do incorporate many good ideas which we would do well to incorporate in future declarative languages.

## References

Cardelli, L. (1984) A semantics of multiple inheritance. Semantics of Data Types, International Symposium, Lecture Notes in Computer Science 173. Springer Verlag.

Darlington, J., Field, A. J. and Pull, H. (1985) The unification of functional and logic programming languages. Imperial College internal paper.

Goldberg, A. and Robson, D. (1983) Smalltalk-80. The Language and its Implementation. Addison-Wesley.

Harrison, P. G. and Reeve, M. J. (1987) The parallel graph reduction machine, Alice. Graph Reduction, Lecture Notes in Computer Science 279. Springer Verlag.

Shapiro, E. Y. and Takeuchi, A. (1983) Object orientated programming in concurrent prolog. In New Generation Computing, Vol 1 (T. Mota-oka, ed.). Springer Verlag, Berlin.

Zaniolo, C. (1984) Object-orientated Programming in Prolog. Proceedings of the International Symposium on Logic Programming, Atlantic City, NJ. IEEE Computer Society Press, New York.

## Biographical notes

![](/api/attachments/YPTR8SWG/fulltext/images/e563c66f51ba239d83554e0008b0889b7a5b7fb27bd02b365c692a92ecd5d971.jpg)

Anthony Kosky studied for a BSc (Hons) in Mathematics at the University of Kent at Canterbury, where he was awarded the 1987 Rotary and I.M.A. prizes. He is currently studying 'Foundations in Advanced Information Technology' at Imperial College, London.

Address for correspondence: Department of Computing, Imperial College, London SW7 2BT.
