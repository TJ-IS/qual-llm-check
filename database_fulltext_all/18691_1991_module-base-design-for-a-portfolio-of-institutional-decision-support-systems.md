---
otero_id: 18691
otero_key: "7BBHXB8F"
title: "Module base design for a portfolio of institutional decision support systems"
authors: "Ramakrishnan Pakath; H.Raghav Rao"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90019-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Module base design for a portfolio of institutional decision support systems

Ramakrishnan Pakath

Department of Decision Science and Information Systems, College of Business and Economics, University of Kentucky, Lexington, KY 40506, USA

H. Raghav Rao

Department of Management Science and Systems, School of Management, State University of New York at Buffalo, Buffalo, NY 14260, USA

Recently, there has been a trend toward utilizing artificial intelligence techniques in decision support systems (DSSs) to enhance system capabilities and support. This paper focuses on using one such technique (productions or rules) for enhancing module representation, access, execution and maintenance flexibility in a class of systems called institutional DSSs. In the approach we propose, an organization maintains a portfolio of such DSSs. An individual system contains, in its knowledge base, only the “structural”, “invocational” and “presentation” knowledge of the modules used by that system. Executable representations of all of the modules in the portfolio and the associated “procedural” knowledge are generated and stored in an external organizational model base (OMB). We discuss representation schemes for the three types of module-related knowledge in each DSS as well as the architecture for the system-user interface.

Keywords: Institutional DSS, Production systems, OPS5, Knowledge representation, Knowledge manipulation.

## 1. Introduction

Decision Support Systems (DSSs) are at the frontier of the continually evolving field of computer-based support systems for decision making. In recent times, various researchers have proposed the integration of artificial intelligence (AI) techniques with conventional DSS technology to enhance the capabilities of and the quality of support provided by a DSS. While such integration could lead to systems that can be truly regarded as “intelligent” systems (e.g., see Turban [7]), integration has other benefits such as, improved problem processing capabilities, better knowledge representation schemes, and more flexible system-user interfaces.

We focus on some of the benefits of utilizing AI techniques in conventional DSSs for enhanced systems-support in building and solving mathematical models of complex decision problems. Traditionally, a DSS provides support for model building and solution by storing what are called “modeling” and “procedural” knowledge in its knowledge base. Modeling knowledge consists of “modules”, or building blocks, that can be aggregated to form a larger “model”. Modules themselves are relatively simple models (e.g., present value, economic order quantity) that address specific facets of many complex, real-world problems. Typically, such modules are aggregated into “module banks”. Each bank contains the set of modules that relate to a specific type of problem (e.g., an inventory control bank, a production scheduling bank). Associated with each module is the procedural knowledge that enables one to execute (or solve) the module.

With regard to modeling and procedural knowledge, the incorporation of AI capabilities in a DSS has the following potential benefits:

(a) The system could be endowed with sophisticated module representation schemes as well as heuristic search and solution techniques borrowed from AI research.

(b) The system could ease the task of problem solving by providing enhanced support in module selection, module chaining, and module execution.

(c) The system could further embellish the benefits cited in (b) above by providing a non-procedural system-user interface.

Here, we describe the application of a particular technique called “productions” (or, more generally, “rules”) for module representation and manipulation in a class of systems called “institutional” DSSs in order to achieve the benefits in (b) and (c). An institutional DSS is a system specifically designed for support of a family of closely related decision problems of a recurring nature in an organization.

Although the field of AI has been contributing substantially to the design of highly intelligent systems, our focus is only on using AI techniques to enhance traditional support. With regard to (c) for example, rather than providing a “natural language” interface, our approach is to create, relatively easily, an interface that avoids a high degree of procedurality. This emphasis is deliberate. We only seek to demonstrate the significant gains that may be realized with even simple concepts borrowed from AI and modest systems design efforts.

In this approach, the organization builds and maintains an external library of frequently-used modules and a portfolio of institutional DSSs that access this library. The module library generates and stores “executable module representations” and also contains the associated procedural knowledge for module solution. Therefore, the module-related knowledge contained in the knowledge bases of the individual DSSs in the portfolio is limited to knowledge on (i) providing a user with the generic mathematical structure of any module (i.e., “structural knowledge”), (ii) how selected modules can be invoked for solution (i.e., “invocational knowledge”), and (iii) presenting the solution to the user (i.e., “presentation knowledge”).

Several such institutional DSSs can be constructed, as needed, with significantly less effort than if each system were to maintain its own structural, invocational, presentation and procedural knowledge, and executable representation schemes. Thus, while it is generally desirable to keep the individual DSS databases separate from the organizational database and from one another (e.g., see Sprague and Carlson [5]), it would be both viable and economical to maintain an “organizational model base” (OMB) with individual DSSs in the portfolio having their knowledge bases linked to the OMB.

Our discussions are based on a prototype institutional DSS developed by the authors (along with Drs. K.Y. Tam and Y. Yang) and described in Tam and Rao [6]. Our paper focuses on feasible enhancements to the prototype that became evident during the course of prototyping and further analysis of the implementation.

The rest of the paper is organized as follows. Section 2 describes OPS5, the primary AI-based software tool used for prototype implementation. Section 3 describes the knowledge representation and manipulation capabilities (pertaining to decision models) that are possible using our approach. Section 4 contains some concluding remarks.

## 2. An Overview of OPS5

We base our discussions on a prototype system implemented using OPS5 within a LISP shell on a VAX 11/780 that runs UNIX. OPS5 belongs to a class of programming languages called “production systems”. We provide a brief discussion on the OPS5 architecture, features of each structural component of the architecture, and the control mechanism for the entire system. For detailed discussions see Forgy [1].

## 2.1. System architecture

OPS5 consists of three components: the “production memory”, the “working memory”, and the “control system”. In traditional DSS terminology, the production memory together with the working memory constitute the “knowledge base” and the control system constitutes the “problem processor”.

## 2.1.1. The working memory component

This component consists of a finite set of ordered pairs, $\langle$ time tag, working memory element $\rangle$ . An “element” is an instance of a data item in working memory. OPS5 permits two data item types: a scalar (or atomic) data type and a structured data type. The latter consists of a named “class” and a finite set of named “attributes” that describe the class. An instantiation of a structured data type corresponds to an instantiation for each of its attributes. Attributes must be of the atomic type. Atomic type data items can take on numeric (i.e., fixed- or floating-point numeric) or symbolic (i.e., character string) values.

For a given structured data item with a specific class name, one can “create” multiple instances of the data item that coexist in working memory. Each subsequent “update” to an existing element would result in a new instance being created and stored. Each such instance corresponds to one working memory element.

The second member of an ordered pair contained in working memory is a time tag. A time tag is a unique, numerical identifier (integer) supplied by the OPS5 interpreter. This tag indicates when the associated working memory element was created or last modified. Time tags are used by the control system component in conflict resolution.

## 2.1.2. The production memory component

This consists of a finite set of named conditional statements called “productions” (hence the term “production system”).

A production is very similar to the IF–THEN statement found in conventional programming languages. The IF part consists of a finite set of conditions (or patterns), $C_{1}, C_{2}, \ldots, C_{n}$ . The THEN part consists of a finite set of actions, $A_{1}, A_{2}, \ldots, A_{m}$ . The interpretation of a production is that when the contents of the working memory component are such that each of the n conditions $C_{1}, \ldots, C_{n}$ is satisfied, each of the m actions $A_{1}, \ldots, A_{m}$ , can be executed.

A condition or pattern is an expression that describes some element that could exist in the working memory component. The extent of abstraction of this description can vary. For instance, a pattern may contain fewer attributes and associated values than the working memory element the pattern describes. Such a pattern will match any element that contains the information in the pattern (though the element may also contain other information).

A pattern is satisfied if its description matches that of at least one element. The IF portion of a production is satisfied if all of its patterns are satisfied. This satisfaction implies that the actions in the THEN portion can be executed. Action execution may result in changes (i.e., additions, deletions, modifications) to working memory contents.

Actions can also be performed without any associated conditions. Thus, it is common to find statements in the production memory component that correspond to performing certain actions with no attempt at pattern matching. Such unconditional actions are typically utilized for initialization.

## 2.1.3. The control system component

This component executes the productions contained in production memory by performing an iterative sequence of operations called the “Recognize-Act Cycle”. The steps in this cycle are as follows:

1. Conflict resolution: Select one production with a satisfied IF portion from a set of such satisfied productions. If no such production exists, return control to the system user.

2. Act: Execute the actions specified in the THEN portion of the selected production.

3. Match: Evaluate all productions to determine which are satisfied, given the current contents of the working memory.

4. Flow control: If a “program halt” was performed, return control to the user. Otherwise go to step 1.

The output of the match process forms the input to the conflict resolution process. Essentially, this output/input is a set of productions with satisfied IF portions called the “conflict set”. During conflict resolution, the interpreter examines the conflict set to find a single production from a dominating set of productions in the conflict set. Choice of a single, dominant production is based on a “conflict resolution strategy”. OPS5 provides two such strategies called the LEX strategy and the MEA strategy that possess the following general features:

(a) In both strategies, once a particular production is selected for execution in step 1 of the cycle, it is discarded from further consideration.

(b) Both strategies seek to select as dominant productions those productions that draw on the most recent data in working memory (based on the time tags of working memory elements).

(c) From the dominating set, both strategies seek to select for execution a production with less abstract patterns over those with more abstract patterns.

(d) The only (slight) difference between the two strategies is in their choice of a dominating set of productions.

![](/api/attachments/7BBHXB8F/fulltext/images/68d7da90bd2cc95f97eb422f9b8d578b229e4d70312619afd0fc57eb3eb57beb.jpg)

ER: Executable Representations

KS: Knowledge System

IK: Invocational Knowledge

PK: Presentation Knowledge

LS: Language System

PPS: Problem Processing System

RK: Procedural Knowledge

SK: Structural Knowledge

Fig. 1. System Architecture.

<table><tr><td>Module 1. The fundamental EOQ Model.</td></tr><tr><td>Module 2. The Model when replenish/deplete cycles are of unequal length.</td></tr><tr><td>Module 3. The Model when replenishment rate is finite.</td></tr><tr><td>Module 4. The Model when shortages are allowed.</td></tr><tr><td>Module 5. The Model when shortages are allowed and replenishment rate is finite.</td></tr></table>

## 3. The proposed AI-based approach

We now discuss the use of productions to implement the module banks in institutional DSSs for flexible support in module selection, execution and chaining. The approach has the advantage of greater ease of module bank maintenance compared to systems that utilize conventional programming languages and traditional knowledge representation and manipulation schemes.

The architecture for our approach is shown in Figure 1. Essentially, the knowledge base of any one of the several institutional DSSs in the portfolio only contains the structural, invocational and presentation knowledge of the modules accessed from the external module library by that DSS. The library itself generates and stores executable representations of modules (based on input parameter information passed to the library by the DSS) and contains procedural knowledge for solving the executable versions of modules.

Consider a situation where the following modules are contained in the “Inventory Control Module Bank” of the DSS:

## Inventory Control Module Bank

The knowledge base of the DSS could contain a variety of such module banks (for production scheduling, forecasting and regression analysis, etc.). The user first gains access to a desired bank, and thereafter to a single module or a set of modules within it.

## 3.1. Module representation

There are four issues concerning module representation. First, a user must be allowed to view a structural (mathematical) representation of a modrule in terms of the input parameters, the output parameters, and the relationships between the inputs and the outputs. Secondly, for an actual realization (i.e., a given set of parameter values) of a module, an executable representation and the associated procedural knowledge or access to these is also required. In essence, the knowledge base of each DSS must contain:

a. (i) structural knowledge, executable representations and procedural knowledge for each module or

(ii) structural knowledge and invocational knowledge for invoking the execution of externally generated and stored executable representations and

b. presentation knowledge that allows a user to view results in different ways (e.g., using symbols, numbers, graphs, charts).

The proposed approach utilizes the knowledge types mentioned in a (ii) and (b) above.

## 3.1.1. Structural knowledge

Knowledge concerning the structure of a module is captured and stored using a production as shown in Figure 2. Instructions for “page breaks” and “pause” can be embedded in a production like P10 to control screen display. Similarly, such a large production can be replaced by a set of several productions of smaller size.

P10 states that if there is a working memory element (of the structured type) named WAN-TM1S with its only attribute RESPONSE having a (symbolic) value of Y (i.e., the user has responded with a Yes when asked if he/she wants to view the structural representation of MODULE 1), then WRITE (i.e., display on screen) the appropriate module structure. The purpose of stating output expressions explicitly, is to save the user the trouble of deriving an explicit expression from a more aggregated expression. The user is quickly able to ascertain what inputs are necessary to generate a particular output. Further, in a particular decision context, if all of the outputs are not required for the user to continue with the decision making process, he/she can execute the model to yield precisely those outputs that are required. Knowledge of the inputs needed for these selected outputs, is therefore, essential.

Finally, some of the outputs (such as reorder level, L\*, and backorder quantity, Q\*) are irrelevant to MODULE 1, given the specific environmental requirements for applicability.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(PP10
(WANTM1S
^RESPONSE Y)
====&gt;
(WRITE
MODULE 1 STRUCTURE:
SPECIFIC ENVIRONMENTAL CONDITIONS:
NATURE OF REPLENISHMENT : INSTANTANEOUS.
NATURE OF CYCLE LENGTH : FIXED.
SHORTAGES : NOT ALLOWED.
MODULE INPUTS:
INVENTORY DEPLETION RATE : D UNITS/UNIT TIME.
ORDERING COST : $C_o$/ORDER.
HOLDING COST : $C_h$/UNIT/UNIT TIME.
MODULE OUTPUTS:
OPTIMUM ORDER QUANTITY, Q$^*$:
Q$^*$ = [(2C$_o$D)/C$_h$]$^{1/2}$ UNITS/CYCLE.
OPTIMUM CYCLE LENGTH, T$^*$:
T$^*$ = [(2C$_o$)/C$_h$D)]$^{1/2}$ TIME UNITS/CYCLE.
OPTIMUM NUMBER OF CYCLES, N$^*$:
N$^*$ = [(C$_h$D)/(2C$_o$)]$^{1/2}$ CYCLES.
OPTIMUM TOTAL COST, C$^*$:
C$^*$ = [2C$_o$C$_h$D]$^{1/2}$ DOLLARS.
OPTIMUM MAXIMUM INV. LEVEL, M$^*$:
M$^*$ = [(2C$_o$D)/C$_h$]$^{1/2}$ UNITS/CYCLE.
OPTIMUM BACKORDER QUANTITY, B$^*$:
B$^*$ = 0 UNITS/CYCLE.
OPTIMUM REORDER LEVEL, L$^*$:
L$^*$ = 0 UNITS/CYCLE.)
</div>

Fig. 2. Partial View of Structural Knowledge of a Module.

In summation, the structural knowledge possessed by the system permits the user to observe (a) the diverse interrelationships between the various module parameters, (b) the specific operating environment in which the module is applicable, and (c) the specific input parameter requirements for generating each of the outputs.

## 3.1.2. Invocational knowledge

Suppose that MODULE 1 is to be executed to find all possible output parameters described in P10. Yet another production, P20, (see Figure 3) facilitates module invocation and solution.

P20 contains three conditions. The first condition is that the user does want MODULE 1 executed (i.e., WANTM1E = Yes). The second condition requires that all of the Input Parameters (i.e., inventory depletion rate DRM1, ordering cost COM1, and holding cost CHM1) for Module 1 (i.e., IPM1) have known values (denoted by $\langle DRM1 \rangle$ , $\langle COM1 \rangle$ and $\langle CHM1 \rangle$ ). The third condition states that the user wants all possible outputs of the module evaluated (i.e., the user has responded with a sequence of Yes responses to a prior query concerning output requirements).

<table><tr><td colspan="3">(P P20</td></tr><tr><td colspan="3">(WANTM1E</td></tr><tr><td></td><td colspan="2">^RESPONSE Y)</td></tr><tr><td colspan="3">(IPM1</td></tr><tr><td></td><td>^DRM1</td><td></td></tr><tr><td></td><td>^COM1</td><td></td></tr><tr><td></td><td>^CHM1</td><td></td></tr><tr><td colspan="3">(ORM1</td></tr><tr><td></td><td>^QM1</td><td>Y</td></tr><tr><td></td><td>^TM1</td><td>Y</td></tr><tr><td></td><td>^NM1</td><td>Y</td></tr><tr><td></td><td>^CM1</td><td>Y</td></tr><tr><td></td><td>^MM1</td><td>Y</td></tr><tr><td></td><td>^BM1</td><td>Y</td></tr><tr><td></td><td>^LM1</td><td>Y)</td></tr><tr><td colspan="3">===&gt;</td></tr><tr><td colspan="3">(CALL M1V1</td></tr><tr><td></td><td colspan="2">(MAKE OPM1</td></tr><tr><td></td><td>^QM1</td><td></td></tr><tr><td></td><td>^TM1</td><td></td></tr><tr><td></td><td>^NM1</td><td></td></tr><tr><td></td><td>^CM1</td><td></td></tr><tr><td></td><td>^MM1</td><td></td></tr><tr><td></td><td>^BM1</td><td></td></tr><tr><td></td><td>^LM1</td><td></td></tr></table>

Fig. 3. Invocational Knowledge of a Module.

The action part of P20 facilitates the execution of a version of MODULE 1, called M1V1, that is stored in the external module library and solves for all outputs. The production merely invokes module execution by referring to a module by its name. M1V1 is an external routine written in the LISP language in which OPS5 is implemented. The system passes on the required input parameter values (i.e., $\langle DRM1\rangle$ , $\langle COM1\rangle$ and $\langle CHM1\rangle$ ) to this routine and in turn accepts values for each of the seven output parameters from the LISP environment. The system builder may choose to implement interfaces for any other language (e.g., Fortran) if some of the required modules are not implemented in LISP.

After M1V1 is executed, the outputs of the execution (i.e., $\langle QM1\rangle$ , $\langle TM1\rangle$ , $\langle NM1\rangle$ etc.) are obtained from the external library and stored as attribute values for the element OPM1 (i.e., Output Parameters of Module 1) in working memory as created by the MAKE action in P20.

Different versions of the same module are created, differing from one another in terms of which output parameters are computed. An alternative would be to have a single executable version that solves for all possible outputs and have the system display only selected outputs. The choice is entirely context dependent. We make a tradeoff between the additional storage required to maintain the different versions of a module and the computational efforts required to solve a single, comprehensive version. Although the choice in the context of our simple example is not very critical, in general it must be based on careful consideration. In the context of institutional DSSs, we conjecture that maintaining alternative versions is desirable because:

(a) The time required to solve a more complex module for all possible outputs could be significantly greater than solving a relatively simpler module for a subset of the outputs.

(b) Given a portfolio of DSSs accessing the same external module library, two or more users may concurrently access and execute different versions of the same module.

Both (a) and (b) contribute toward quicker system turnaround. Further, the continually declining costs of storage devices make this approach feasible. This approach requires substantially less hardware and software resources when compared with the alternative where each DSS in the portfolio maintains its own module library.

## 3.1.3. Presentation knowledge

Figure 4 is an example depicting how presentation knowledge is contained in a production. This example presumes that (having solved for all possible outputs) the user wants a display of all of the computed outputs of Module 1. The IF portion of P30 determines whether all of the required inputs and outputs for the module have known values. Yet another condition verifies that the user wants all output parameter values displayed (Yes in the example). A WRITE action in P30 displays the required output parameter values and the inputs that generated these outputs.

```asm
(P P30
(WANTM1P
^RESPONSE Y)
(IPM1
^DRM1 <DRM1>
^COM1 <COM1>
^CHM1 <CHM1>)
(OPM1
^QM1 <QM1>
^TM1 <TM1>
^NM1 <NM1>
^CM1 <CM1>
^MM1 <MM1>
^BM1 <BM1>
^LM1 <LM1>)
(PRM1
^QM1 Y
^TM1 Y
^NM1 Y
^CM1 Y
^MM1 Y
^BM1 Y
^LM1 Y)
===>
(WRITE
MODULE INPUTS:
INVENTORY DEPLETION RATE : <DRM1> UNITS/UNIT TIME.
ORDERING COST : <COM1> $/ORDER.
HOLDING COST : <CHM1> $/UNIT/UNIT TIME.
MODULE OUTPUTS:
OPTIMUM ORDER QUANTITY, Q* : <QM1> UNITS/CYCLE.
OPTIMUM CYCLE LENGTH, T* : <TM1> TIME UNITS/CYCLE.
OPTIMUM NUMBER OF CYCLES, M* : <NM1> CYCLES.
OPTIMUM TOTAL COST, C* : <CM1> $. 
OPTIMUM MAXIMUM INVENTORY, M* : <MM1> UNITS/CYCLE.
OPTIMUM BACKORDER QUANTITY, B* : <BM1> UNITS/CYCLE.
OPTIMUM REORDER LEVEL, L* : <LM1> UNITS/CYCLE.
```  
Fig. 4. Example Presentation Knowledge for a Module.

Other forms of presentation include the use of graphs and charts: one could build an interface with a graphics package and include productions that enable one to view graphically displayed results.

In summation, structural knowledge of a module is contained in a WRITE action whereas invocational knowledge is contained in a CALL action. Presentation knowledge could involve both WRITE actions and CALL actions, depending on context. Also observe that fairly detailed structural representations are possible in the knowledge base of the individual DSSs in the portfolio due to the fact that considerable space savings result from maintaining executable module representations and procedural knowledge externally.

## 3.2. Module execution and chaining

An invocational representation of a version of a module is contained as an action in a production. This representation is merely in the form of a module name. When the conditions of the production are satisfied, the module is executed by performing the appropriate routine in the external library. The outputs generated by the routine are then obtained and stored as working memory elements for subsequent reference.

This approach has certain desirable features. First, it results in a more compact set of productions. Secondly, adding or deleting a module is as simple as adding or deleting a set of associated productions. Thus, modifying the DSS to adapt to changing environments/requirements becomes a relatively simple task as productions, unlike conventional programming language statements, are essentially independent units.

It is possible that some of the required inputs may not be available when a user requests a module's execution. Thus, production P20 will not fire unless all inputs are available and the system must therefore take steps to obtain all unknown parameter values. This may be achieved in one of three ways. The system offers the user a choice of either (i) supplying the unknown values, or (ii) obtaining the values from an existing DSS database (DSSDB), or (iii) possibly determining the required values by executing other modules (i.e., establishing a module chain). Thus, if the input parameter DRM1 (i.e., the inventory Depletion Rate for MODULE 1) is unknown, the DSS could execute another module in the Forecasting & Regression Analysis bank to obtain an estimate.

With reference to (ii) and (iii), within the set of productions for a particular module bank, we could include productions that alert the user about appropriate data base files and auxiliary module banks for generating unknown values. Provisions for interfacing with the DSSDB must be made in order to access data from this database. Again, this is possible using the LISP environment in which OPS5 operates.

## 3.3. System-user interface

The system-user interface facilitates flexible access and manipulation of (a) the module banks of the DSS, (b) the structural representations of modules in the module banks, (c) the executable representations in the external module library and (d) the presentation knowledge in the knowledge base. During the course of a dialog between the user and the system:

\- The DSS allows the user to select one or more module banks from its knowledge base.

\- The DSS informs the user about the various attributes (or parameters) that define a particular module and the environmental conditions under which the module is applicable.

\- The user is given the choice of either not specifying or flexiblyspecifying the set of existing environmental conditions on which module selection and execution must be based.

\- If the user desires, the system attempts to derive the necessary input parameter information from its knowledge base either through data retrieval or by executing yet another module (thus performing a module-chaining activity).

\- The user may terminate the dialog at any stage.

\- The user can override the system's recommendations at any stage.

The architecture of the system-user interface is depicted in Figure 5. The figure shows the considerable flexibility offered to the user in directing the dialog and manipulating the modules.

A WRITE action contained in a production displays the set of module banks available and allows the user to select a desired bank (see Figure 6). Once a bank is chosen (e.g., the Inventory

![](/api/attachments/7BBHXB8F/fulltext/images/e4c66aec1f2075a22f5fe6e030fd436af10f4dac66e09ef38392aad4339f297a.jpg)  
Fig. 5. Architecture for System-User Interface.

1. INVENTORY CONTROL.

2. PRODUCTION SCHEDULING.

3. PRODUCTION PLANNING.

4. MATERIALS REQUIREMENT PLANNING.

5. FORECASTING & REGRESSION ANALYSIS.

===> ENTER A NUMBER TO [1 THROUGH 5] TO SELECT A BANK, OR [E] TO EXIT MODEL BASE:

Fig. 6. Sample Listing of Available Module Banks.

Control Module Bank), yet another WRITE action displays the general environmental requirements (i.e., conditions required for applicability) for all of the modules in the chosen bank. For instance, for the five modules contained in the Inventory Control example, the general applicability requirements will include those shown in Figure 7.

In general, it is advisable to further decompose an aggregate module bank to insulate the user from unnecessary detail. For instance, we can decompose the Inventory Control Module Bank into those containing deterministic and stochastic modules.

Given the user's knowledge about the decision making environment, the choice of whether or not to continue with the current module bank is, again, left to the user.

## 3.3.1. Module selection

Once the user has accessed a particular module bank, access to one or more modules is achieved through a flexible question/answer session. An example of such a dialog is contained in Figure 8 (the display is compressed to conserve space). The user has wide latitude in controlling the conversation in terms of (a) backtracking and reiterating some of the earlier steps, (b) steering the dialog in a completely different direction, (c) overriding the system's recommendations, and (d) terminating the session.

<table><tr><td colspan="3">INVENTORY CONTROL MODULE BANK</td></tr><tr><td colspan="3">GENERAL ENVIRONMENTAL CONDITIONS REQUIRED FORAPPLICABILITY</td></tr><tr><td>1.</td><td>Number of Items:</td><td>One.</td></tr><tr><td>2.</td><td>Number of Stages:</td><td>One.</td></tr><tr><td>3.</td><td>Time Horizon of Analysis:</td><td>Infinite.</td></tr><tr><td>4.</td><td>Safety Stock:</td><td>None.</td></tr><tr><td>5.</td><td>Quantity Discounts:</td><td>None.</td></tr><tr><td>6.</td><td>Nature of Production Quantity:</td><td>Constant.</td></tr><tr><td>7.</td><td>Nature of Holding Cost:</td><td>Constant.</td></tr><tr><td>8.</td><td>Nature of Shortage Cost:</td><td>Constant.</td></tr><tr><td>9.</td><td>Nature of Setup Cost:</td><td>Constant.</td></tr><tr><td>10.</td><td>Nature of Demand:</td><td>Constant.</td></tr><tr><td>11.</td><td>Nature of Lead Time:</td><td>Zero.</td></tr><tr><td>===&gt;</td><td colspan="2">ENTER [M] TO SEE AVAILABLE MODULES, [B] TO VIEW MODULEBANK LISTING, OR [E] TO EXIT MODEL BASE:</td></tr></table>

Fig. 7. Example Display of Module Bank Applicability Conditions.

The user is provided with a listing of the specific modules in the selected bank. Among other things, the user may view the structure of and execute any of the modules. If necessary, the system guides the user to an appropriate module or set of modules. If the user requires guidance, the system asks for a specification of the nature of the specific environ-

## INVENTORY CONTROL MODULE BASE

<table><tr><td colspan="2">THE FOLLOWING MODULES ARE AVAILABLE</td></tr><tr><td colspan="2">MODULE 1. The fundamental EOQ Model.</td></tr><tr><td colspan="2">MODULE 2. The EOQ Model when replenish/deplete cycles are of unequal length.</td></tr><tr><td colspan="2">MODULE 3. The EOQ Model when replenishment rate is finite.</td></tr><tr><td colspan="2">MODULE 4. The EOQ Model when shortages are allowed.</td></tr><tr><td colspan="2">MODULE 5. The EOQ Model when shortages are allowed and replenishment rate is finite.</td></tr><tr><td>===&gt;</td><td>ENTER A NUMBER [1 THROUGH 5] TO PICK A MODULE, [S] TO SPECIFY A SPECIFIC ENVIRONMENTAL CONDITION, [G] TO VIEW GENERAL APPLICABILITY CONDITIONS, [B] TO VIEW MODULE BANK LISTING, OR [E] TO EXIT MODEL BASE :S</td></tr><tr><td>===&gt;</td><td>ENTER [R] TO SPECIFY NATURE OF REPLENISHMENT RATE, [C] TO SPECIFY NATURE OF CYCLE LENGTH, [H] TO SPECIFY NATURE OF SHORTAGES, [M] TO SEE AVAILABLE MODULES, A NUMBER [1 THROUGH 5] TO PICK A MODULE, [S] TO SPECIFY A SPECIFIC ENVIRONMENTAL CONDITION, [G] TO VIEW GENERAL APPLICABILITY CONDITIONS, [B] TO VIEW MODULE BANK LISTING, OR [E] TO EXIT MODEL BASE :R</td></tr><tr><td>===&gt;</td><td>ENTER [I] IF REPLENISHMENT RATE IS INSTANTANEOUS OR [F] IF FINITE, [C] TO SPECIFY NATURE OF CYCLE LENGTH, [H] TO SPECIFY NATURE OF SHORTAGES, [M] TO SEE AVAILABLE MODULES, A NUMBER [1 THROUGH 5] TO PICK A MODULE, [S] TO SPECIFY A SPECIFIC ENVIRONMENTAL CONDITION, [G] TO VIEW GENERAL APPLICABILITY CONDITIONS, [B] TO VIEW MODULE BANK LISTING, OR [E] TO EXIT MODEL BASE :I</td></tr><tr><td>===&gt;</td><td>MODULES 1, 2, AND 4 ARE APPLICABLE. ENTER [M] TO SEE AVAILABLE MODULES, A NUMBER [1 THROUGH 5] TO PICK A MODULE, [S] TO SPECIFY A SPECIFIC ENVIRONMENTAL CONDITION, [G] TO VIEW GENERAL APPLICABILITY CONDITIONS, [B] TO VIEW MODULE BANK LISTING, OR [E] TO EXIT MODEL BASE :1</td></tr><tr><td>===&gt;</td><td>ENTER [V] TO VIEW STRUCTURE OF MODULE 1, [X] TO ATTEMPT EXECUTION OF MODULE 1, [M] TO SEE AVAILABLE MODULES, A NUMBER [1 THROUGH 5] TO PICK A MODULE, [S] TO SPECIFY A SPECIFIC ENVIRONMENTAL CONDITION, [G] TO VIEW GENERAL APPLICABILITY CONDITIONS, [B] TO VIEW MODULE BANK LISTING, OR [E] TO EXIT MODEL BASE :S</td></tr></table>

Fig. 8. A Sample of the User–System Dialog.

mental conditions. This process results in the identification of a single module or a set of modules that are applicable given the user's environmental knowledge. At any stage, the user may pause to examine the modules to gain further insight. Having selected a set of modules, the user can proceed with module chaining and execution. Subsequently, other productions that contain presentation knowledge enable the user to view the results of module executions.

All of the features of the system-user interface discussed here and exemplified in Figures 6 through 8, can be implemented using productions and appropriate interfaces.

## 4. Concluding remarks

We have described one approach for utilizing AI techniques for effectively representing and processing modeling knowledge in the context of a portfolio of institutional DSSs.

We showed the distinction between various types of modeling knowledge (i.e., structural, invocational, and presentation) and how these may be captured and represented using productions in a language such as OPS5. Our methodology suggests that executable representations and procedural knowledge be maintained in a separate library, external to the portfolio. The knowledge bases of individual DSSs in the portfolio only contain structural, invocational and presentation knowledge of modules.

We stress the use of the approach in the context of institutional DSSs only because in many instances, builders of ad hoc DSSs tend to use more conventional tools (e.g., spreadsheet software) as (a) these permit rapid system development and (b) the builders may not have the time and other resources required for mastering a relatively unfamiliar AI tool and building the necessary external library interfaces. Maintaining such a library is of course feasible only if it is used on a recurring basis by several systems; ad hoc DSSs are standalone, “quick-hit” systems that are typically discarded after use.

With regard to the particular AI technique used here, there are several advantages of using productions instead of conventional programming languages. It permits (i) abstract representations of working memory contents in productions, (ii)

atomic and structural data types, and (iii) time tags to be associated with each instance of each element in working memory. The degree of abstraction, as well as the recency of elements, determines the flow of execution. Further, as control of execution lies outside of the program (in the control system) and not within the program as in conventional programming languages (for example, when using FOR, DO-WHILE or GOTO statements and subroutine calls), modifying the program is relatively simple.

On the other hand, building institutional DSSs along the suggested lines will also require creating and implementing interfaces between systems like OPS5 and existing DSSDBs and other software packages that facilitate presentation (e.g., graphics packages). Provisions will also have to be made for interfacing with existing mathematical and statistical subroutine libraries written in other high level languages.

Today, more powerful tools (e.g., GURU) that utilize the notions underlying OPS5 are available (Holsapple and Whinston [2]). These integrate various knowledge management techniques such as, spreadsheet, database, forms, text, graphics and rules. Tools (e.g., KEF) utilizing other AI-based techniques such as “frames” and “objects” are also available (Fikes and Kehler [4]). Further, many of these tools can also be effectively used in a micromputing environment. Such advanced tools will enable one to implement highly sophisticated and effective institutional DSSs.

## Acknowledgements

This research was funded in part by a Special Summer Faculty Research Fellowship from the President's Fund for Excellence, University of Kentucky, Lexington, KY, and a Summer Research Grant from the School of Management, State University of New York at Buffalo, NY. We gratefully acknowledge the use of the resources of the MIS Research Laboratory, DSIS Department, University of Kentucky, Lexington, KY.

The authors would also like to thank Dr. Andrew B. Whinston (Chair Professor of Management, University of Texas-Austin, Austin, TX) and the late Dr. King S. Fu (Goss Distinguished Professor of Engineering, Purdue University, West Lafayette, IN) for their inspiration and insights in developing the original prototype system. The contributions made by Drs. K.Y. Tam (University of Texas at Austin) and Dr. Y. Yang (University of Detroit) in implementing the prototype are also deeply appreciated.

## References

[1] Forgy, C., OPS5 User's Manual, CMU-CS-81-135, Department of Computer Science, Carnegie-Mellon University, Pittsburgh, PA, 1981.

[2] Holsapple, C.W., and Whinston, A.B., Business Expert Systems, Richard D. Irwin, Inc., Homewood, IL, 1987.

[3] Bonczek, R.H., Holsapple, C.W., and Whinston, A.B.,

Foundations of Decision Support Systems, Academic Press, Inc., New York, NY, 1981.

[4] Fikes, R., and Kehler, T., “The Role of Frame-based Representation in Reasoning”, Communications of the ACM, 28, 9, 1985, 906–920.

[5] Sprague, R.H., and Carlson, E.D., Building Effective Decision Support Systems, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1982.

[6] Tam, K.Y., and Rao, H.R., “Expert System for Inventory Models”, in Some Prototype Examples for Expert Systems, Fu, K.S., ed., TR-EE-85-1, School of Electrical Engineering, Purdue University, West Lafayette, IN, 1985.

[7] Turban, E., Decision Support and Expert Systems, Macmillan Publishing Company, New York, NY, 1988.

[8] Wilensky, R., LISPcraft, W.W. Norton and Company, New York, NY, 1984.
