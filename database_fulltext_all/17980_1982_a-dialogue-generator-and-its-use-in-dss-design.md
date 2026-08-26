---
otero_id: 17980
otero_key: "KNM94VVC"
title: "A dialogue generator and its use in DSS design"
authors: "Izak Benbasat; Yair Wand"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90004-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Dialogue Generator and Its Use in DSS Design

Izak Benbasat and Yair Wand \*

Faculty of Commerce and Business Administration, The University of British Columbia, Vancouver, Canada V6T 1Y8

This paper describes a conceptual model and the experimental implementation of a Decision Support System (DSS) dialogue generator. The dialogue generator is a tool for the DSS builder to develop the human/computer interface efficiently and expeditiously. It enables the DSS builder to speed up the initial implementation, provides flexible interfaces, makes it easier to adapt to changing needs, and offers the ability to experiment with prototypes, all of which are factors that contribute to a successful DSS implementation. The paper also provides examples of how the dialogue generator was useful in implementing two experimental systems.

Keywords: Decision Support System, Dialogue Generator, Human-Computer Interface, Interactive Systems, Prototyping.

## 1. Introduction

The term Decision Support System (DSS) refers to an interactive system with access to the analytic power, models, and active data base of the computer. The main goal of a DSS is to help decision makers solve semi-structured problems.

A good human/computer interface is a prerequisite for success of an interactive computerized system. This is especially important for a DSS, since the semi-structured nature of the decision-making process requires (preferably) that the user

![](/api/attachments/KNM94VVC/fulltext/images/0d314f63d55da7c1b6bae8065f88fdbdaf0b1293e779cafb8e333139de94c6cc.jpg)

of Systems, Man, and Cybernetics and the Journal of Accounting Research, among others.

![](/api/attachments/KNM94VVC/fulltext/images/3f8ec23a391ae69b3535813f1e559dbae33e923bc39e0e2fe1a8bd913be08231.jpg)  
sent research interests are in Information Requirements Analysis, Decision Support Systems, and Quantitative Modelling in Information Systems.

and the system interact in a conversational mode to supplement the judgement of the user with the analytical power of the computer. Furthermore, since the managerial users of a DSS are not technical specialists, the interface should not impose any structure with which the user would feel uncomfortable.

Another aspect of DSS development is its justification. Due to its use for decision support and the evolutionary nature of development, it is extremely difficult to make any cost/benefit analysis for DSS. It has been recently suggested that prototyping may be a viable approach to justify a DSS [4.7].

This paper presents a conceptual model and the implementation principles of a DSS dialogue generator designed to facilitate the development of conversational DSS for nontechnical users. A DSS generator is a package of related hardware and software that provides a set of capabilities to build a specific DSS. The dialogue generator is a tool for the DSS builder to implement the human/computer interface of a DSS efficiently and expeditiously and to develop a prototype quickly. The dialogue generator described in the paper has been implemented and used in the design of two simple DSS.

## 2. The Need for a Flexible Interface

It is often suggested that a user wants a DSS that is easy to use. Unfortunately, “ease of use” is a difficult concept to define: it comprises several dimensions. Some authors [3,13] have suggested lists of goals to guide the design of interactive systems. However, it has been pointed out that these lists tend to contain contradictory recommendations [9]. For example, one would expect that there are some dimensions, such as the capability to abbreviate a command, which are desirable for all types of users. On the other hand, the choice of a dimension such as dialogue type (user vs. computer-guided) might depend on the user's experience level [12].

Keen [5] and Carlson [1] emphasize the idea of differing user needs by stating that any computer support must be flexible and allow for personalized use. For example, a novice user would prefer a dialogue type that guides him, giving explanations and exploratory questions. An experienced user would more likely want to use a powerful and concise command language with few keywords. Furthermore, for a given user, one would expect a gradual change from being a novice to becoming experienced, sometimes only after a few hours of interactive computer use [8].

The DSS builder therefore faces the task of designing a system to suite the needs of a variety of users who have evolving knowledge levels, requirements, thought processes, and task environments. Thus a DSS cannot be based on a static set of “user-friendly” interface characteristics. Rather, the DSS builder needs an adaptive tool that would make iterative design possible. This tool should provide for a design architecture which is modular, flexible, responsive, communicative, and easily modified [5].

## 3. Desired Features of a DSS Dialogue Generator

The dialogue generator described in this paper was designed with the following requirements: 1) it must be possible to change the interface features quickly and efficiently, 2) it must provide the ability to conduct modular design and implementation, and 3) it must allow the user to participate actively in the design of the human/computer interface:

1) Desired Interface Features. The following is a non-exhaustive list of interface alternatives of the dialogue generator:

a) Providing various prompts and dialogue types (user vs. computer-guided);

b) Adding help and explanation facilities;

c) Generation of error diagnostics;

d) Defaulting of input;

e) Providing abbreviation capabilities;

f) Stacking of more than one command or data input in a given dialogue line;

g) Echoing or confirming user entries;

h) Renaming of commands;

i) Modifying the type of actions the system takes; for example, redefining the error check logic or the series of steps to be performed by a given command.

For some of the capabilities listed above (for example a, b, and c), the dialogue generator should enable the DSS builder to provide a continuum of options from verbose to terse, depending on the user. For some others, such as abbreviation and stacking, the system could provide unlimited abbreviation and stacking capabilities, thereby allowing the user to decide how much to use these options. In addition, the users can dynamically change the style of response they receive. For example, after users understand the reasons for an erroneous entry, they may instruct the system to provide the short version of the error diagnostics in the future. Similarly, users may instruct the dialogue generator to switch from a system-guided to a user-guided dialogue.

2) Prototyping and Modular Design. The proposed dialogue generator allows users or DSS builders to concentrate initially on those parts of the DSS they deem to be important. Since the dialogue generator contains modular prompting, error-checking actions, and similar facilities, a system could be built quickly without one or more of these modules present. For example, since input error-check facilities often take up one third of a program's processing steps, the designer may skip that portion at first, and implement an initial system quickly and cheaply. While the user is experimenting with the particular DSS, the DSS builder could be developing the error checking facilities. Moreover, modularity, coupled with the flexible interface features, allows the DSS builder to expand and modify the system easily in response to the user's new experiences with the system.

3) User-led Design. The proposed dialogue generator is organized so the user can specify, either with the help of the DSS builder or else alone (if the user is experienced) the flow and contents of the dialogue. By allowing the user to build a large portion of the interactive component of the DSS, user involvement and the chances of successful implementation are improved.

## 4. Elements of an Interactive Dialogue

From a DSS builder's viewpoint the DSS is composed of three major components: database management software, model base management software, and dialogue generation and management software for handling the interface between the user and the system [2,10]. A recent study by Sutton and Sprague [11] indicated that, even with the use of generalized dialogue generator software, the display generation and management functions account for more than 60% of the contents of an interactive program.

The dialogue generator/manager provides prompting and receives from the user data and instructions (commands) on which parts of the system should be activated. The user who interacts with the DSS only 'sees' these parts of the system. Hence, the degree to which the system is user-oriented depends mostly on the interactive elements (commands, prompts, outputs) rather than the operating components (a model or data base). For example, the same computerized model may be viewed by the user differently if it is activated differently. This is similar to systems in which output reports with different formats are based on the same data but appear to be generated by different systems.

In order to design a generalized and effective dialogue generator, the following questions were examined:

1. Are there enough common generic elements in the human/computer dialogue to justify the development of a generalized dialogue generator to control the interface in interactive systems?

If such modularization is possible, then the interactive front-end of the system may be more easily modified than systems where the interaction is intermixed with the processing.

2. What is an effective way to separate the interactive parts of a DSS from the processing parts; namely, models, data management, and reporting?

From a user's viewpoint a 'run' consists of a series of requests for input at which the system awaits some response from the user. As a result of this input ('data' or 'instructions') the system takes some action (processing) which may result in information being displayed. Such a request and the response to it are defined as an interaction event. This is the basic notion in the dialogue implementation, and the dialogue generator is based on subdividing an interaction even into a specified set of common phases or a 'cycle'. The following basic phases are always present in an interaction event:

1. Prompt - Indicate to the user that the system expects an input.

2. Input - The user provides an input.

3. Action - The system takes an action based on the input.

An action may be as involved as activating a simulator or as simple as storing a value for later use.

The basic set of steps above is, of course, overly simplistic; e.g., it does not provide for input checks. Also, in many interactive systems the user may optionally request more explanations regarding the input (a 'help' feature). In addition there may be a default value to be substituted for the input if the user gives no response. Another useful option is for the user to 'escape' a request for input that was unintentionally invoked.

Finally, a mechanism is needed to control the dynamic flow: the sequence of events, which determines the order of processing. This implies that after each event a pointer should be set to the next event to be executed (at times, the same event). To accomplish this the event cycle should include a 'set next event' phase. The complete interaction event cycle is now:

1. Prompt

2. Input

3. Escape: if Input == 'escape', change next event indicator, end event cycle.

4. Help: if Input = 'help', display additional information, and event cycle.

5. Check: apply input checks; if errors, report errors, end event cycle.

6. Next: set 'next event' indicator.

7. Action

Each event is given a unique identification code in order to identify the 'next event'. An interaction event may be described, therefore, in terms of the information necessary to carry out the seven phases, and the full description of an event is:

ID Prompt; Default; Escape; Help; Check; Next: Action)

The full dialogue description consists of the set of interaction event descriptions. The events in this set may be invoked in various sequences. The sequence of events may be fully prescribed, partially user-controlled or fully user-controlled.

The following example may serve to clarify this. A decision maker is asked to use a simulator to find the [price, quantity] combination that maximizes the profit for a given product. Hence, the task involves selecting a [price, quantity] combination and requesting a simulator to provide the resulting profit figure. The decision maker could request tabular and graphical reports, which display the inputs [price, quantity] and corresponding profit figures for the previous trials, to assist in solving the problem.

Figures 1 and 2 show two possible dialogue types that could be designed for this task. The system-guided dialogue version (Fig. 1) is highly structured and leads the user through the problem solving task by looping through a set of five questions. The user-guided dialogue version (Fig. 2) is rather flexible. The user controls the dialogue by entering the appropriate command.

Assume that the user and the DSS builder wish to implement the system-guided dialogue as shown in Figure 1. The first step would be to identify the interaction events; they are: set price, set quantity,

![](/api/attachments/KNM94VVC/fulltext/images/3599496686d7bdbeed48ed0541d3c40d4cf5bd7d54699d157217a6c8fcb92d1d.jpg)  
Fig. 1. A "System-Guided Dialogue" Version Interaction. (Note: The human operator entries are underlined. The instructions given to the users specified that the figures in parentheses indicate valid input ranges; the figures in brackets are default values.)

<table><tr><td colspan="4">1) COMMAND: PRICE</td></tr><tr><td colspan="4">Enter desired price level (1-30) [10]: 15</td></tr><tr><td colspan="4">COMMAND: QUANTITY</td></tr><tr><td colspan="4">Enter desired quantity produced (1-70) [25]: _</td></tr><tr><td colspan="4">COMMAND: SIMULATE</td></tr><tr><td colspan="4">Period 1 has been simulated</td></tr><tr><td colspan="4">With PRICE = 15 and QUANTITY = 25 your profit was $35.</td></tr><tr><td colspan="4">2) COMMAND: PRICE 10 Q 35 SIMULATE</td></tr><tr><td colspan="4">Period 2 has been simulated</td></tr><tr><td colspan="4">With PRICE = 10 and QUANTITY = 35 your profit was $45.</td></tr><tr><td colspan="4">3) COMMAND: P 20 S</td></tr><tr><td colspan="4">Period 3 has been simulated</td></tr><tr><td colspan="4">With PRICE = 20 and QUANTITY = 35 your profit was $12.</td></tr><tr><td colspan="4">4) COMMAND: TABULAR</td></tr><tr><td>PERIOD</td><td>PRICE</td><td>QTY</td><td>PROFIT</td></tr><tr><td>1</td><td>15</td><td>25</td><td>35</td></tr><tr><td>2</td><td>10</td><td>35</td><td>45</td></tr><tr><td>3</td><td>20</td><td>35</td><td>12</td></tr></table>

Fig. 2. A "Use-Guided Dialogue" Version Interaction. (Note: The human operator entries are underlined. The instructions given to the users specified that the figures in parentheses indicated valid input ranges; the figures in brackets are default values).

simulate, request tabular report, request graphical report. The second step is to build the dialogue; this involves developing the full description of the given interaction events by specifying each of the phases. Table 1 shows a representation of the dialogue shown in Figure 1. Note that this is a descriptive definition as outlined by the user to the DSS builder.

## 5. Implementation of the Dialogue Generator

## 5.1. Event Descriptions

The two crucial implementation decisions are: 1. How to represent the information about events (text, action, etc.).

2. How to organize this information.

The technique used is to represent each interaction event as a line in a table (the 'event description table'). Each column in the table contains a reference to the information about one phase (e.g. prompt, check, action). The information itself is contained in other tables. We now demonstrate this approach through an example and then explain its advantages.

Consider the event table of Table 1; this is a descriptive definition of a dialogue that a user would outline to a DSS builder. The next step is for the DSS builder to implement the event table in a form which can be inputted to the dialogue generator. Table 2 is such an implementation of Table 1 (to conserve space only line numbers 1 and 6 are shown). As an example, Table 2 has an entry: TEXT PROMPT - PRICE; here TEXT refers to a table name (see Table 3) and PROMPT - PRICE to a line (identifier) in this table. PROMPT - PRICE identifies some information, which is the text on its right, namely

Table 1
Descriptive Interaction Event Table for System-Guided Dialogue Shown in Figure 1

<table><tr><td>NO</td><td>ID</td><td>PROMPT</td><td>DEFAULT</td><td>ESCAPE</td><td>HELP</td><td>CHECK</td><td>NEXT</td><td>ACTION</td></tr><tr><td>1</td><td>PRICE</td><td>Enter desired price level (1-30)</td><td>Previous value</td><td>EXIT</td><td>Price should be GE 1 and LE 30</td><td> $1 \leq \text{PRICE} \leq 30$ </td><td>QUANTITY</td><td>store value</td></tr><tr><td>2</td><td>QUANTITY</td><td>Enter desired quantity produced (1-70)</td><td>Previous value</td><td>EXIT</td><td>Quantity should be GE 1 and LE 70</td><td> $1 \leq \text{QUANTITY} \leq 70$ </td><td>SIMULATE</td><td>store value</td></tr><tr><td>3</td><td>SIMULATE</td><td>-</td><td>--</td><td>EXIT</td><td>-</td><td>--</td><td>TABULAR</td><td>simulate</td></tr><tr><td>4</td><td>TABULAR</td><td>Want to see a tabular report (YES or NO)</td><td>“NO”</td><td>EXIT</td><td>Enter “YES” if you want to see a report with price, quantity and corresponding profit</td><td>“YES” or “NO”</td><td>GRAPHIC</td><td>generate report</td></tr><tr><td>5</td><td>GRAPHIC</td><td>Want to see a graphical report (YES or NO)</td><td>“NO”</td><td>EXIT</td><td>Enter “YES” if you want to see a graph of profit plotted against price and quantity</td><td>“YES” or “NO”</td><td>CONTINUE</td><td>generate report</td></tr><tr><td>6</td><td>CONTINUE</td><td>Do you want to stop (YES or NO)</td><td>“NO”</td><td>EXIT</td><td>Enter “NO” if you want to try more price, quantity combinations</td><td>“YES” or “NO”</td><td>-</td><td>select value of NEXT as PRICE or EXIT</td></tr><tr><td>7</td><td>EXIT</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>stop</td></tr></table>

<table><tr><td colspan="9">Table 2Example of an Event Description Table</td></tr><tr><td>NO</td><td>ID</td><td>PROMPT</td><td>DEFAULT</td><td>ESCAPE</td><td>HELP</td><td>CHECK</td><td>NEXT</td><td>ACTION</td></tr><tr><td>1</td><td>PRICE</td><td>TEXT PROMPT-PRICE</td><td>PRICE</td><td>EXIT</td><td>TEXT HELP-PRICE</td><td>CHECK PRICE</td><td>QUANTITY</td><td>ACTION PRICE</td></tr><tr><td>6</td><td>CONTINUE</td><td>TEXT PROMPT-CONTINUE</td><td>“NO”</td><td>EXIT</td><td>TEXT HELP-CONTINUE</td><td>CHECK CONTINUE</td><td>-</td><td>ACTION SELECT</td></tr></table>

Table 3  
Example of TEXT table

<table><tr><td>Identifier</td><td>Information</td></tr><tr><td>PROMPT - PRICE</td><td>Enter desired price level (1-30)</td></tr><tr><td>HELP - PRICE</td><td>Price should be GE 1 and LE 30</td></tr><tr><td>PROMPT - CONTINUE</td><td>Do you want to stop (YES or NO)</td></tr><tr><td>HELP - CONTINUE</td><td>Enter “NO” if you want to try more price, quantity combinations</td></tr><tr><td>ERROR - CONTINUE</td><td>Your response should be ‘YES’ or ‘NO’; please re-enter</td></tr></table>

"Enter desired price level (1-30)"

Note that the HELP column in Table 2 is organized in the same way. The entries refer to the TEXT table and the specific identifier, such as HELP - PRICE, in that table. The CHECK column similarly refers to the CHECK table (Table 4) and an entry in that table. However, unlike the TEXT table, which only carries text to be displayed, the CHECK table consists of the pair <logical check, error message>. The error message is a reference to a table (TEXT) and the identifier of the message to be displayed (e.g. HELP - PRICE) if the logical check indicates an error condition (such as price greater than 30).

The logical checks described could involve testing for the range of a given value, such as RE-

Table 4  
Example of a CHECK Table

<table><tr><td>Identifier</td><td>Logical Check</td><td>Error Message</td></tr><tr><td>PRICE</td><td>RESPONSE ≤ 30</td><td>TEXTHELP - PRICE</td></tr><tr><td>PRICE</td><td>RESPONSE ≥ 1</td><td>TEXTHELP - PRICE</td></tr><tr><td>CONTINUE</td><td>RESPONSE IN LIST</td><td>TEXTERROR - CONTINUE</td></tr></table>

Table 5  
Example of an ACTION Table

<table><tr><td>Identifier</td><td>Action</td></tr><tr><td>PRICE</td><td>PRICE = NUMERIC (RESPONSE)</td></tr><tr><td>SELECT</td><td>SETNEXT RESPONSE</td></tr></table>

SPONSE ≤ 30 and RESPONSE ≥ 1. It could also involve checking against a list of valid entries. The logical check shown on the second line of Table 4 indicates that a table labelled LIST contains the acceptable answers. Recall that the check is being conducted for the response to the question:

"Do you want to stop?"

Therefore, the table LIST should at least contain the words YES and NO. However, if the user wants to add more entries later, such as GO, STOP, Y, N, OK, etc., this is done very simply by using a text editor (part of the system package) to make additional entries. Such an addition only requires that the DSS builder change the table LIST.

Table 5 is an example of an ACTION table. The action relating to PRICE (assuming PRICE was in the valid range of 1 - 30) is to make the value of the variable "PRICE" equal to the user response to the prompt for PRICE. The action for SELECT is to invoke a function SETNEXT that will set the value of the "next event ID" to

PRICE if the user response is NO

(user does not want to stop)

or

## EXIT if the user response is YES

(user wants to stop).

Function SETNEXT actually refers to a table to determine the next event ID's corresponding to YES and NO. A detailed explanation of a similar approach is given later.

The main advantage of this arrangement is that the interaction event descriptions (Table 2) which may be viewed as the 'logic', are separated from the actual text, action reference, check reference, etc. (e.g., Tables 3, 4, and 5), which may be viewed as the 'data' processed by this 'logic'. This separation allows the text, checks, actions, etc.. to be developed separately from the system flow. In turn, this allows a quick skeletal development that may be augmented later (for example by adding checks and help). Moreover, the same flow may be implemented with various versions of the text (prompt and help), thereby providing flexibility.

The DSS dialogue description also becomes 'homogeneous': all the components are stored in similar tables. Therefore, the same definition procedures may be employed to describe the various elements, and the same software tools may be employed to build and modify the various components.

## 5.2. Software

The software developed to "drive" the events in Table 2 consists of several processors: a prompt processor, a check processor, a help processor, etc. For example, when the user enters the command PRICE (dialogue in Fig. 2), the prompt processor takes as input the entry TEXT PROMPT - PRICE (Table 2). It then retrieves from the reference table TEXT (Table 3) the screen corresponding to PROMPT - PRICE and displays it. Similarly, if the user responds to the PRICE prompt with HELP, the help processor will retrieve information corresponding to HELP - PRICE from the reference table TEXT and display it (Tables 2 and 3).

A set of common utilities is used by all processors to decode an entry in the interaction event description and to locate the information in the relevant table. Thus, the homogeneous representation of the dialogue components permits a structured and relatively simple implementation of the dialogue generator.

## 5.3. User-Guided Dialogue

User-guided dialogue is a mode of interaction where the user decides on the next step by selecting from the set of possible options (Fig. 2). An interactive DSS typically may contain a combination of system-guided and user-guided dialogues. The more user-guided the system, the more flexible it is, but the user must be more experienced.

The technique for implementing a user-guided dialogue is based on the use of special SELECT action and table. The table has two entries ('columns') – a code entry and an event identification entry (see the example below). The select routine accepts a code and a table name and searches for the code in the first entry of the table. When the code is found, the 'next event' indicator is set to the contents of the event identification entry.

This mechanism allows for: 1. multiple command names, 2. easy change of command names, 3. easy addition of options at any (unstructured) interaction event. Also, the 'select' table may be used to display a 'menu' and to check the input (for non-existing or ambiguous commands). Table 6 gives an example SELECT table.

The initial line of the event description table for the user-guided dialogue version starts by prompting the user to enter a command (the ID of this line is defined as COMMAND). The 'action' to be taken after the command (user input) is received (for example, PRICE) is to search for PRICE in the Code column of the SELECT table. As an outcome of this search, the 'next event' is set to PRICE. Thus, the next action the system will take is to access the line identified by PRICE in the event description table (that is, line No. 1 in Table 2). The system will then display the prompt "Enter Desired Price Level (1-30)" (see example 1 in Figure 2). If the user enters a valid price, such as 25, the system will take the appropriate action; that is, set the value of variable "PRICE" to 25 (see Table 5). The NEXT event ID in the user-guided dialogue version is then set to COMMAND, which again prompts the user.

Table 6
Example of a SELECT table

<table><tr><td>CODE</td><td>Event ID</td></tr><tr><td>PRICE</td><td>PRICE</td></tr><tr><td>P</td><td>PRICE</td></tr><tr><td>QUANTITY</td><td>QUANTITY</td></tr><tr><td>VOLUME</td><td>QUANTITY</td></tr><tr><td>GRAPHICAL</td><td>GRAPHICAL</td></tr><tr><td>EXIT</td><td>EXIT</td></tr><tr><td>STOP</td><td>EXIT</td></tr></table>

Note that in the select table, multiple command names (e.g. EXIT/STOP, PRICE/P, QUANTITY/VOLUME) lead to the same action. Similarly, command names can be easily changed by modifying the entries in the code column, but leaving the Event ID column the same.

## 5.4. Multi-Entry Input

As users become more experienced with the system, they may like to use multiple entry lines without waiting for explicit prompting (see part 2, Fig. 2).

This option is accomplished as follows: Each input line is broken down to its elements (such as PRICE 10, Q 35, SIMULATE) and the elements are placed in a queue. The routine that accepts the input examines the queue, and as long as the queue is non-empty, the prompt is suppressed. As soon as the queue becomes empty, the prompt is reactivated and the user can respond with a new line.

## 5.5. Capturing Users' Input

Analysis of users' input to a conversational system may be of value for both design and research. For example, the input may be examined in order to answer questions such as:

1. How do inexperienced users learn to use the system?

2. What is the degree of use of 'help' and 'escape'?

3. Under what conditions do users tend to make errors?

By defining the dialogue as a series of interaction events with a common structure, a well-defined way of capturing and identifying the input exists. Since the user response is provided in the input phase of the interaction event cycle (which is always processed by the same module), it is easy to capture this input. Also, the structure of an interaction event cycle means that an input always follows a prompt in one of the following ways:

1. At the beginning of the cycle.

2. After a 'help' request.

3. After an error message.

Hence, a given input line can be fully characterized in terms of:

1. The event ID.

2. The phase which preceded the prompt.

Following this idea, a generalized 'log' facility that captures and identifies each user's input is easily implemented.

## 5.6. The Use of APL

The dialogue generator was implemented in APL, which was found to be especially suited for two reasons:

1. It has extensive and effective matrix processing facilities. These were used in the table processing routines.

2. It has an 'execute' function which can execute a character string as an expression. Using this function, expressions for actions and checks were stored as entries in text tables and invoked when necessary. For example, a check for the range of input value stored in RESPONSE may be stored as the string RESPONSE ≤ 30, which is a valid APL expression (See Table 4).

## 6. An Example of the Use of the Dialogue Generator

The dialogue generator software was tested by implementing the dialogues of Figs. 1 and 2. Next, the dialogue generator was used to develop a DSS for inventory planning. The main purpose of this DSS was for use in a study to determine how decision makers interact with decision aids and how they function with computer-based support systems.

The model base (simulation model) part of the DSS was programmed and tested independently. The objective was to implement a flexible interface for the decision makers to interact with this model. One of the authors of this paper was assigned the role of the DSS user. His task was to outline the dialogue. This included defining the commands to be used in inputs to the model, simulation, sensitivity analysis, and reporting. This allowed for selective retrieval and sorting of the simulation results. The second author had the role of the DSS builder. A third member of the team was a research assistant, who acted as the “technical supporter”.

The DSS user started by defining the commands he wanted to be part of the dialogue and the prompts and the actions to be taken. He prepared a descriptive table, similar to that in Table 1. However, in the initial description of the table, columns for defaults, escape, help, and check were left blank. While developing this skeleton system, the DSS user sought the guidance of the DSS builder. For example, the user did not know how to describe the SORT command, which required specifying the fields to be sorted, and their sequence. After consulting with the DSS builder, it was decided to implement this command as two interaction events, one to prompt the user for the field(s) and the second for the sort order. Also, the availability of multi-entry input allows the user to respond in one or two input lines.

The next step was for the DSS builder to instruct the technical supporter on the creation of the action table (e.g., Table 5). This required technical knowledge of how to link the action table with the model base used. The DSS user was not involved at this stage, but worked on defining the kind of input checks required by the system.

The system was then tested with the prompts and actions only. This showed that the interface between the dialogue generator and the model base was working properly; i.e., the DSS user could now use the simulator through the new commands he had defined. Following this initial test, the DSS builder and the technical supporter implemented the check table (e.g., Table 4) based on the descriptions provided by the user. Next, the user and the technical supporter completed the error messages for the check table and the explanatory messages for the help table. The technical supporter keyed the messages into the tables using a CRT and text editor while the user was describing them.

After the test of the full system, minor modifications were made to the various output messages by using the text editor. Multiple names were entered for the same actions, such as SORT/ORDER and STOP/EXIT/QUIT, by adding new lines to the table.

Our experience with the use of the dialogue generator has confirmed its value. In summary:

a) the dialogue generator provides DSS users with a structured method of defining the elements of the dialogue, thereby allowing them to lead the design of the interface with the DSS;

b) by virtue of its modularity it provides an easy mechanism for developing a prototype quickly and efficiently; and

c) the dialogue generator makes it possible for users (other than those who developed the initial description) to make changes easily to suit their style of interacting with the system.

## 7. Concluding Comments

This paper described a conceptual model for dialogue generation, its implementation in a dialogue generator, and the experimental use of the latter in DSS design. Dialogue-centered design philosophy matches an observation made by Keen and Gambino [6]. Based on their experience in developing a DSS, they suggest that the first rule of thumb in building such a system should be to design first the dialogue; i.e., what the user says and sees. Since dialogue development usually consumes a large part of the development effort, use of a dialogue generator may substantially decrease development time.

Our particular implementation provides for modular implementation. Hence, it supports the idea of prototyping where a DSS should be first implemented as a simple version and evolve during use.

Finally, the approach provides for a well-defined recording of user input. Analysis of such input may provide information on how the system is used and how to improve the dialogue.

## References

[1] Eric D. Carlson, "An Approach for Designing Decision Support Systems", DATA BASE, 10, 3 (Winter, 1979) 3–15.

[2] Eric D. Carlson, and Wolfgang Metz, "Integrating Dialogue Management and Data Base Management", in: S.H. Lavington ed., Information Processing 80 (North-Holland Publishing Company, Amsterdam, 1980) 463–468.

[3] Wilfried J. Hansen, "User Engineering Principles For Interactive Systems," IFIPS Fall Joint Conference Proceedings, 39 (1971) 523-532.

[4] Peter Keen, "Value Analysis: Justifying Decision Support Systems", Management Information Systems Quarterly, 5, 1 (March, 1981) 1–15.

[5] Peter Keen, "Adaptive Design for Decision Support Systems", DATA BASE, 12, 1 and 2 (Fall, 1980) 15–25.

[6] Peter Keen and Thomas J. Gambino, "Building a Decision Support System: The Mythical Man-Month Revisited", Center for Information Systems Research, MIT, Sloan WP NO. 1132–80 (May, 1980).

[7] Barbara C. McNurlin, "Developing Systems By Prototyping", EDP Analyzer, 19, 9 (September, 1981).

[8] Jacob Palme, "Interactive Software for Humans", Management Dutamatics, 5, 4 (August, 1976) 139–154.

[9] Ben Shneiderman, "Human Factors Experiments in Designing Interactive Systems", IEEE Computer, (December, 1979) 9-19.

[10] Ralph H. Sprague Jr., "A Framework for the Development of Decision Support Systems", Management Information Systems Quarterly, 4, 4 (December, 1980) 1–26.

[11] J.A. Sutton and R.H. Sprague Jr., "A Study of Display Generation and Management in Interactive Business Applications", IBM Research Report RJ2392, IBM Research Division, San Jose (November, 1978).

[12] George H. Walther and Harold F. O'Neill Jr., "On-Line User-Computer Interface: The Effects of Interface Flexibility, Terminal Type, and Experience on Performance", AFiPS National Computer Conference Proceedings, 43 (1974) 379–384.

[13] Anthony I. Wasserman, "The Design of Idiot Proof Interactive Programs, AFIPS National Computer Conference Proceedings, 42 (1973) M34-M38.
