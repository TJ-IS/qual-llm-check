---
otero_id: 23359
otero_key: "3YZMCA9N"
title: "An Empirical Analysis of Spreadsheet Usage: A solution storing up problems?"
authors: "David Mason"
year: "1989"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1989.20"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Empirical Analysis of Spreadsheet Usage: A solution storing up problems?

David Mason

One of the most striking features of today's business environment is the extent to which the spreadsheet has penetrated business computing and the speed with which it was adopted. Spreadsheets are probably the most widespread business tool in use today. Virtually every computer installation and every PC user has a spreadsheet. Certainly few businesses are without one.

There are four main reasons for this outstanding success.

(i) Ease of Use. The majority of first time users are immediately impressed with how easy the tool is to use.

(ii) Ease of Application. You need very little instruction to get going and they are so flexible that you can do almost anything with them.

(iii) Natural Approach. The spreadsheet is laid out in rows and columns which coincides with the way managers have been trained to tackle business problems.

(iv) No Programming. Spreadsheet packages are so well designed in that even using the advanced facilities doesn't seem like programming.

These advantages have made the spreadsheet the single most important management tool in use today. End users relish their freedom from the data processing department. And at the same time DP professionals welcome spreadsheets as a product which allows users to get on with their own problems, and frees them from endless small programming requests. On the face of it spreadsheets benefit everyone. However, this is not entirely true. This research has revealed that in practice the spreadsheet applications in many companies are a source of endless troubles. Just because a problem can be solved with a spreadsheet, it does not follow that it should.

## Spreadsheeting

For the majority of users a spreadsheet is their only decision support tool. The research established several reasons for this. Sometimes it was because spreadsheeting formed the manager's introduction to computing (Davis and Olson, 1985). Often it was the only formal training ever received in computing techniques. In addition, large numbers of users have never had any formal training at all: they are entirely self taught. For this type of manager using a spreadsheet is normal and natural, and done without further thought. When presented with any kind of problem the first thing they reach for is the spreadsheet. It is applied to anything and everything, a kind of electronic whitewash.

Given this background it should be no surprise that the majority of spreadsheet users look no further for a tool to solve their computing needs. During the research it became apparent that spreadsheets have taken a firm hold in corporate computing. Users now actively resist any suggestion that they should change.

## Resistance to change

There are five reasons commonly advanced for this.

(1) 'Why should I?' Many users won't even consider looking beyond the spreadsheet. And why should they? The spreadsheet is so flexible they think it can solve almost any problem. Most managers have no interest in computing technology itself and want to spend as little time as possible learning new software packages.

(2) Time Invested. After spending the initial time learning the commands and concepts, users will insist on getting as much value as possible from their time investment.

(3) No Alternatives. Spreadsheet users are normally not DP professionals and have no reason to examine alternative software packages. And in most organisations although the information centre or data processing departments regularly carry out software evaluations, they do so only for their own purposes. They only advise users if specifically requested.

(4) 'Leave well alone'. The great majority of spreadsheet applications are very simple models, designed by the user for the user. Just a few rows and columns. They are perfectly happy as they are: If it ain't broke, don't fix it.

(5) Too Busy. To be fair, many spreadsheeters do recognise when a spreadsheet has reached the critical point where it should be replaced. But even when users are aware of shortcomings they are often just too busy. Business pressures mean that few users are willing (or have the time) to scrap their overstretched spreadsheet and start over.

## The serpent in the spreadsheet

These arguments for continuing with spreadsheets as currently used arise because users are not aware of the potential problems. Problems really only arise when spreadsheets grow too large. The normal pattern is for a user to build a small model and use it for a while. Then the spreadsheeter is tempted to tag bits on here and there. The flexibility of a spreadsheet makes this easy to do, at least in the beginning. But as the solution being modelled becomes more complex, changes and enhancements become more and more difficult to implement. In the end what was once a simple management aid turns into something unmanageable.

This is largely a function of the friendly and forgiving interface of the spreadsheet. It insulates users from the realisation that they are actually using a powerful programming tool. Inexperienced spread-sheeters are not only unaware of the penalties of breaking design rules, they often don't even realise that there are rules.

In practice the research turned up spreadsheets in amazing variety. They were used as a records manager, as a word processor, for budgeting and forecasting, as a desk calculator, as a management accounting tool, as an accounting entry package, as a programming language, even advocated as an expert system vehicle (Leigh and Doherty, 1986).

The real problems arise when a spreadsheet turns into a database. Every model has to hold some data, and to that extent a spreadsheet must incorporate a database function (Ariav and Ginzbergh, 1985). However, users tend to expand their spreadsheets indefinitely. This research project uncovered PC spreadsheets with fifty of more columns and thousands of rows. By any definition that is a database.

This uncontrolled growth causes serious problems: data redundancy, slow access, inconsistency, uncertainty, vulnerability, and data exchange problems.

Data redundancy. One fundamental problem with spreadsheets is that they are limited to a single table. Every piece of data you want to use in the spreadsheet is held in one data structure. Effectively this means that all your processing is limited to a single file. This is exactly the situation which prevailed before the introduction of disk storage. To that extent spreadsheets are actually a step backwards.

The problem of course is that business applications involve multiple files (Howe, 1983). Combining several logically distinct files into one inevitably brings update, deletion and amendment difficulties (Vasta, 1989).

For example, suppose a manager wanted to hold details of all orders received, as part of a sales application and to serve as a database. This might be structured in columns as Sale Number, Customer Details, Products Ordered, Supplier Details. Printing out details in any particular order would pose no problems. Finding which sales relate to a given customer would be a simple query. However adding a potential new customer would mean creating a dummy order. Changing any of the customer details means a search of the whole spreadsheet since you don't know which sales were for a given customer. Eventually the spreadsheet would get over-large and some entries would have to be deleted. If it so happened that a deleted order was the only one from a particular customer then all details of that customer would disappear. Similarly, if that deleted order contained that last remaining reference to a product then all knowledge of that product would also be lost. If one customer has many orders then the customer details are stored many times, or blank cells allocated and storage space is wasted.

This class of problem is well known and is easily avoided. Relational data theory was developed to eliminate precisely this class of problem and the solution of data redundancy, data normalisation, lies at the heart of today's relational databases (Martin, 1984).

Slow access. Quite apart from the theoretical aspects, over-stretching a spreadsheet is bad practice because the model becomes cumbersome to use. When using large models moving from left side to right side and back again repeatedly is slow and clumsy. Moving vertically from top to bottom to see a result and then moving back up to change the critical variable often means wading through multiple disk accesses.

There can also be a loss of intuitive 'feel' for the model. Spreadsheets support 'What if.' investigations by showing the effect of changing a single variable directly and dynamically. This encourages managers to explore relationships and to investigate more complex associations (Thierauf, 1988). The advantage is clearest where all the elements affected can be seen on screen simulataneously. Direct interactive feedback makes spreadsheeting an invaluable learning tool for decision makers. With a model wider than the screen only a few variables and the outcome can be viewed simultaneously so this advantage is greatly diminished.

Inconsistency. Managers recognise how clumsy overlarge spreadsheets are and the usual response is to find some way to split it into submodels (Sprague and Carlson, 1982), perhaps dividing it by sales divisions, or storing current and previous year data separately. This however, only shifts the problem, it doesn't eliminate it. Updating multiple models with the same data item is tedious and error prone, and there is no simple foolproof way of ensuring that all the submodels reflect the current position at all times.

Uncertainty. Increased size usually brings increased complexity. It is easy to build a large model. But in a large model with many variables there is the constant danger that the syntax is correct but the logic is not. There is in principle no reason why I couldn't build a model of the entire firm in a spreadsheet, or of the entire nation's economy for that matter. I would probably have reservations about accepting the economy model's predictions for inflation or unemployment. But how many companies are running on the basis of data from a spreadsheet incorporating the same degree of underlying uncertainty, without recognising the dangers of hidden assumptions or untested relationships?

There is unfortunately no simple reliable way of ensuring the integrity and accuracy of a model. The more complex the model the harder it is to test. Professional modellers recognise that fact. Amateurs are more likely to accept the model as long as the results support their expectations.

Vulnerability: security problems. Few spreadsheets offer more than rudimentary security. Data integrity is usually poorly served and a cell's contents can easily be accidentally altered. To combat this some spreadsheets offer data typing and will not allow say, a decimal point in an invoice number cell if that is declared as integer only. Some will allow columns or cells to be locked so they cannot be updated. But how many offer extensive validation checks? Or can verify the existence of an entered value by checking data held in another file?

Some have password protection. This will prevent unauthorised accesss. But what about restricting the access rights of authorised users? How many spreadsheets can restrict the view of a legitimate user to only a few of the columns of the model? A sales manager, for example, might want to make product stockholding data available to customers, but not want them to see the column holding the cost figure. The uncoordinated use of spreadsheets may increase accessibility of information for unauthorised users (Young, 1984).

Data interchange problems. An overlarge spreadsheet brings problems when it serves only a single user. The situation is even worse when its data has to be accessed by others. The sheer size of some spreadsheets makes sharing open information awkward. What happens when a user with say thirty columns 'in his model wants to import the data from a colleague's model with fifty columns?

Using the actual terminal of another manager is usually an impractical way of sharing data, so file copying is inevitable. But if files are to be copied preserving the security of the model is a problem. In applications where a manager wants to share columns but not others, the only solution is to copy out the permitted columns and issue copies of those sub sets only. But once again there is the problem of ensuring that updates to the master sheet are reflected in all the subsidiary sheets. This means extra work for the 'data owner'. A clear finding of this research is that users of 'personal' databases are very lax when it comes to supplying data to downstream users. Such work has low priority in their eyes, and with no particular incentive to supply updates on time the common result is time shifted data values in use throughout the organisation.

The situation is worse when several users are trying to use the same data in common. This happens when a second user wants to update some of the cells and transfer them back to the original person, but leaving other cells untouched. And in the meantime the first user has updated other cells on his own machine. The result is often pure chaos.

## Controlling the chaos

These problems, data redundancy, model validity, security, loss of integrity, stem basically from an attempt to make a personal productivity tool into an all-purpose programming environment. The solution lies in first ensuring that the right tool is being used, and then imposing company wide controls on the creation and use of spreadsheets.

Why do people still use the wrong tool for the job? The great majority of spreadsheets are used on microcomputers. End users are managers and executives, not DP professionals. Managers tend to adopt a personal and limited view of information system requirements, and seldom consider the wider aspects. Those who do recognise the impli-cations often prefer to ignore them. Individual justifications for this ranged from apathy, through ‘not my responsibility’, to misplaced ideas of individual freedom. Central IS departments too often allow spreadsheeting to go uncontrolled and uncoordinated since they regard it as just ‘users playing around’ – and therefore ignore the potential problems and costs to the organisation.

How do you know if you are using the wrong tool? It is impossible to lay down hard and fast rules about when to use a spreadsheet and when not. However, the experience of this research project suggests that the following ten questions will eliminate the obvious offenders.

## Ten tests for spreadsheet applications

(1) Do you have more than five models which are closely linked, or which share the same data, or have to be updated simultaneously?

(2) Does the spreadsheet hold large volumes of data? Are you really running a database in disguise?

(3) How many dimensions are involved in the problem? A spreadsheet is a general purpose modelling tool. If you have a large and complex application consider using specialist modelling software.

(4) Does the application involve several distinct entities? Does the model reflect the true entity relationships or does it model only one aspect of a multifaceted situation?

(5) Is the data regularly needed by more than one user? Many users implies the need for many different access paths to the data not just the single view used by the original builder. Do you need to see the same data in many different report formats?

(6) Are the systems purely for personal decision support or are there third parties involved? Do your results or reports go to other departments? Maybe they could use the raw data themselves. Do others have to re-key the figures from your reports?

(7) Who is the end user? Would it be better just to supply summary information and omit most details? Is there a need for 'Black boxing' the solution?

(8) Does the data have to conform to legal requirements? Not just the data protection legislation, but also the various requirements of taxation authorities, licensing bodies and the organisation's own auditors?

(9) Does the application have security needs?

(10) Do you usually wish the screen was bigger?

## Data model administration

In large organisations an uncoordinated increase in spreadsheet use can only lead to more problems. Companies need to create the equivalent of a database administrator to oversee the use of spreadsheets.

The initial tasks of the Data Model Administrator would be as follows:

Registration. Record the current users and uses of spreadsheets. This would ensure that corporate effort is not being duplicated where different departments build essentially identical models.

Standardisation. Establish a data dictionary type environment for the whole organisation. Create a register of data types, column names and so on, to avoid needless duplication or incompatibility across user models. Structure.

Definition. Centralise control of the formulae held in individual spreadsheet models in the same way that all data elements are incorporated into a data dictionary to create a central repository of unique and tightly defined data. For example a formula for say, amortisation, developed in one part of the organisation can be tested, named and made available to all users to ensure consistency and prevent wasted effort.

Validation. Any model with the potential to be used by many others should be ‘walked through’ with a domain expert. So for instance a manager developing a stock valuation model would have to talk it through with the accountant before it could be released for general use.

Storage and distribution. Most models are of the 'quick and dirty' variety (Cragg et al., 1989), thrown away after use and therefore constantly reinvented. Data Model Administration offers the option of making copies of all in house models available for use as templates for new users or as shortcuts for ad hoc applications.

Report generation. Central administration can overcome one of the poor features common to spreadsheets – their limited reporting formats. Users who develop large models or amass large databases will want to display that data in many different ways. Few spreadsheets have anything like an adequate report formatter. Spreadsheet administration is done centrally then a good report designer can be purchased.

Coordination. Before a developer is allowed to start on a model it must be registered with the DMA to ensure that the data is not available on the system already.

Documentation. Every model must be adequately documented. Application programmers are not allowed to write programs without documenting them, there is no reason why modellers should be exempt.

Prioritisation. The DMA would be responsible for commissioning models, establishing priorities for modelling requests, coordinating with the overall organisation data management strategy, steering users towards upwardly compatible software packages and distributing externally purchased data.

## Conclusion

The data held in spreadsheets are now a major component of corporate information systems. They can no longer be left entirely in the hands of the end user. Centralised administration offers the ability to ensure that the data held in 'private' models is validated and has the potential to be integrated into the main organisational database. Otherwise if the situation is allowed to continue unchecked what the users are actually building is an underground, 'alternative' data organisation outside the formal information system.

## References

Ariay, G. and Ginzberg, M.G. (1985) DSS design: A systematic view of decision support. Communications of the ACM, 28, 10.

Cragg, P., Hunter, T. and Scott, J. (1989) Decision support systems – examples and issues. New Zealand Journal of Computing, 1, 1.

Date, C. (1986). An Introduction to Database Systems, Volume 1, 4th Edition. Addison-Wesley Publishing.

Davis, G. and Olson, M. (1985) Management Information Systems: Conceptual Foundations, Structure, and Development. 2nd Edition, McGraw Hill.

Howe, D. (1983) Data Analysis for Data Base Design. Edward Arnold Publishing Ltd., London.

Keen, P. and Scott Morton, M. (1978) Decision Support Systems: An Organisational Perspective. Addison-Wesley Publishing Company.

Leigh, W. and Doherty, M. (1986) Decision Support and Expert Systems. South West Publishing Co., Cincinnati, Ohio.

Martin, J. (1984) Managing The Database Environment. Prentice Hall, Englewood Cliffs, New Jersey.

Meador, L. and Mezger, R. (1984) Selecting an end user programming language for DSS development. MIS Quarterly, 8, 4, 267–281.

Sprague, R. and Carlson, E. (1982) Building Effective Decision Support Systems. Prentice Hall International.

Sprague, R. and Watson, H. (1986) Decision Support Systems: Putting Theory into Practice. Prentice Hall International.

Thierauf, R. (1988) User-Orientated Decision Support Systems: Accent on Problem Finding. Prentice Hall International.

Thierauf, R. (1982) Decision Support Systems for Effective Planning and Control: A Case Study Approach. Prentice Hall International.

Vasta, J. (1989) Understanding Database Management Systems. Wadsworth Publishing, Belmont, California.

Young, L. (1984) A corporate strategy for decision support systems. Journal of Information Systems Management, 1, 1.

## Biographical notes

David Mason is a Senior lecturer in the Information Systems Group at Victoria University of Wellington, New Zealand. He specialises in applied systems analysis with particular emphasis on automated design techniques and CASE tools.

Address for correspondence: David Mason, c/o Information Systems Group, PO Box 600, Victoria University of Wellington, Wellington, New Zealand.
