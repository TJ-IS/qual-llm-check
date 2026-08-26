---
otero_id: 18244
otero_key: "HGBJD4JB"
title: "Information - organization - decision: Some strange loops"
authors: "Jean-Louis Le Moigne; Edgar H. Sibley"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90044-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information – Organization – Decision: Some Strange Loops

Jean-Louis Le Moigne

GRASCE, Faculté d'Economie Appliquée de Droit, d'Economie et des Sciences d'Aix-Marseille, 3 Avenue R. Schuman, 13100 Aix-en-Provence, France

and

Edgar H. Sibley

George Mason University, Dept. Comp. and Inform. Science, 4400 University Drive, Fairfax, VA 22030, USA

Acceptance of the theoretical foundations of Management Information Systems (MIS) has remained surprisingly high in the past twenty years, whereas information processing technologies have been improving at an incredible rate. This stability appears to be because the MIS model is based on the cybernetic model of organizations. We see, however, a conceptual crisis due in the development of more and more complex information systems and increased questioning of the deficiencies of organizational models based on cybernetic theory. This is particularly highlighted by the problems encountered in introducing the “bounded rationality paradigm” of H.A. Simon into the model.

In this paper, we propose a new model that should be better adapted to contemporary technology. This model allows both order and disorder to be included, while incorporating the concept of “organizational memory,” to improve the representation of a complex organizational information system with an action and process aspect.

Keywords: Management Information Systems, Organizational Information Systems, Organizational theory, Intelligent Systems, Conceptual modeling, Cybernetics, Complex systems, Science of Design.

![](/api/attachments/HGBJD4JB/fulltext/images/07dc3849b583831d1600c6453a8dd2271259cb7572235497c62f3c7055b9ec6f.jpg)

Jean-Louis Le Moigne, Professor of Systems Sciences at the University of Aix-Marseille III, France, cofounder of the “Groupe de Recherche en Analyse de Système et Calcul Economique” (GRASCE, CNRS 940), Director of the program of “Méthodes Informatiques Appliquées à la Gestion” (Aix-Marseille). Born in 1931, graduate as engineer (Ecole Centrale de Paris), then, after 13 years in a large French industrial group as a management and computer scientist (ITP Harvard Business School and MIT Sloan School). Author of eight books on Information Systems, Decision Systems, self-organizing enterprises, intelligent systems, complex systems, and of fifty articles on those topics and related epistemological discussions. His main area of research and teaching lies in the cross-fertilization of the Sciences of Design and the social sciences, the new sciences of Organization.

![](/api/attachments/HGBJD4JB/fulltext/images/83fc21aa7702367d11b2eb8631b91d277d6f9b699eab4f7d2294c507cca7fc6d.jpg)

Dr. Edgard H. Sibley, who has been the Chairman of the Board of Editors of Information & Management since its inception, is now University Professor at George Mason University. Other activities include Chair of the Computing Practices Panel of Communications of the ACM and membership of other editorial boards. He has been associated with many conferences and made major presentations in most of the world. His consulting has primarily involved large scale information systems implementations with dictionary, quality, and embedded aspects. Over 80 of his articles have been published.

He has served on many professional groups, including the NASA Computer Science Advisory Panel, the KITIA (to review the development of the KAPSE-Kernel ADA Processing Environment), a group to study the needs for a Software Technology Initiative, the CODASYL Systems Committee, the ANSI/SPARC ad hoc task groups on Database Management Systems and Database Systems, their committee on Operating Systems Control Languages, and ANSI X3H1.

He was U.S. Delegate to IAG (user group of IFIP) for the American Federation (AFIPS) and has been consultant and technical advisor to the United Nations (in UNIDO, UNDP, ILO, and UNESCO). He has also consulted with many corporations and several agencies of the US Government; he is an internal consultant to the US General Accounting Office.

## 1. Introduction

It is a strange paradox that while information technologies have been changing for twenty years at an impressive rate, we are continuously questioning the limit of man's and society's ability to adapt. The models of social organizations during the insertion of these technologies seems to have remained surprisingly constant; the MIS concept, created in the United States of America about 1965, had reached a kind of reassuring plateau by 1975, and since then it has hardly changed, at least conceptually.

A brief examination of books and magazines confirms this, not only because of its theoretical justification, but also because of the known savings in real applications. Here we attempt to understand the reasons for this paradox; it leads us to conjecture about the necessity for a revolution: the general model that most public or private, large or small organizations have been using is becoming perverted.

Herbert Simon proposed that managers tend to satisfy rather than optimize, unless some alternatives are provided to them. Thus incorrect or non-optimal solutions abound. We predict, in the evolution of theory and practice, the emergence of a new model capable of providing a framework within which social organizations can develop their own information systems that are better adapted to complexity and evolution.

## 2. Classical Information Systems Concepts

The complete and least questioned presentation of the modern MIS is found in Gordon Davis' book [1]. There he attempted to provide a unifying theory of MIS: the classical paradigm, in the sense of T.S. Kuhn [2]. This work is devoted to a conceptual presentation of MIS without reference to the implementation technology, and it certainly accounts for the stability of it as a conceptual foundation. Some of the salient points are now reviewed.

## MIS is dedicated to management

MIS is organized according to managerial functions as defined in the cybernetic model of the organization: "The MIS is an integrated manmachine system which provides the data, supporting procedures, management and decision-making in a social organization” [1].

The cybernetic model of the organization is the conceptual framework of the MIS

The cybernetic model of the firm was (and still is) the glue which binds the two rival schools of organizational theory:

1. The organization-Machine is heir to the Scientific Management School of F. Taylor and H. Fayol.

2. The Organization-Organism stemming from the work of E. Mayo and N.N. Roetlishberger in the Human Relations School.

By defining cybernetics as the study of “control and communication in natural and artificial systems”, Norbert Wiener [3] proposed an attractive synthesis model. This is simple to present but unfortunately it is liable to be complicated by three factors: the imposition of levels, strata and layers; the definition of a set of actions, (including short-term procedures, medium-term tactics, and long-term strategy); and the statement of a field of action (goods, markets, and regions) [4,5].

## An MIS requires feedback

The general model of an organization may be split into two subsystems: the Controlled System and the Control System. These provide the classic paradigm of the MIS as shown in Figure 1. To be effective, the cybernetic model must clarify the modes of production and transmission of the inputs; i.e., the information, which, by its acquisition, use, retention, and transmission, allows proper interaction between the control system and its environment. Feedback is vital for temporal regulation, and appears in all branches of science, e.g., homeostatic regulation as identified by physiologists (such as M. Cannon).

![](/api/attachments/HGBJD4JB/fulltext/images/37f3b1857265e96a6c919eb13636bfcc7c238b675ed7e3e5667c77c38912f0d4.jpg)  
Fig. 1. The Cybernetic (Feedback) Model of an Organization (for on MIS Model).

An MIS involves computation and transmission of data

Although he obviously perceived this fact, Norbert Wiener did not really develop it. R.A. Fisher's work related to use of data for decision making, while Claud Shannon's work dealt with the coding and transmission of information [6]; indeed, these two are almost contemporary. But neither they nor their successors, who were concerned with statistics in decision making (nor John von Neuman) were able to provide the theoretical foundation to link management and computer science. They defined no conceptual basis for the production and retention of information. Of course, Herbert Simon was starting to develop his famous thesis on administrative behaviour [7], but few were listening to him then. Also Human Problem Solving [8], as developed by him with Newell, had started to monopolize much of his attention, thereby slowing the other development.

## MIS is the Computation and proper feedback of information

Cybernetics provided a theoretical structure, though incomplete, that linked the control system (including its conceptual and instrumental part) with the controlled constituent of the entire organization. The functional identification of the many feedback mechanisms and selection of the “right” one (by use of operations research techniques) is the major factor during the conception and development of the MIS, using the resources of the information processing system.

## MIS is a vague systems approach rather than an effective methodology

An MIS requires both a theoretical basis of communication and organization (marketing, production, logistics, finance, management, staff, and data processing). These have classically been divided into “three layers” of decision levels: operational, tactical, and strategic. Although often quoted by MIS writers, L. von Bertalanffy's general systems paradigm does not provide a better or more effective conceptual foundation than cybernetics.

Conclusion: There are deficiencies in the MIS approach

Thus the generation and production of information, and its “memorization” (organizational retention or discarding) within the organization is virtually ignored in the classical MIS paradigm. Possibly this is due to a lack of appropriate foundations in the literature.

## 3. The Crisis of the Classical Model of MIS

The apparent shortcomings of the MIS classical model has not stopped universities from teaching it, nor practitioners from using it. The reason for this strange stability must be examined. Some factors are:

## The classical functions are to compute and transmit

The relevance of the MIS model in information processing has certainly been a stable platform. For 30 years, the computer industry, and consequently computer science, has favoured hardware performance improvement (speed, capacity, and cost). The production and retention of information was seen as a nontechnical part, arising from individual or group “users” of computer systems, supposedly not responsible for the economical consequences of the technology. On the other hand, storage systems are regarded as technological devices; but until the development of mass memory with random access, particularly hard and floppy disks, its cost was such that the user had to regard it as a rare resource. It was therefore not necessary in the early days to produce a theory for uneconomical parts of a large system; moreover, the early memory devices were sequential and tended to be slow.

## "The Computer is first a Memory" (H.A. Simon)

Memory technology has changed incredibly over the years. But though it is now cheap, organizations still seem unable to adjust to it and use it effectively. Some of the major discussions centre on the centralization or decentralization issue, which is of less and less of importance. Questions like: “Which part of the database should be stored where?” become moot when the cost of inexpensive duplicates and good communication exist (except in the few systems where immediate updates are essential or concurrency problems are truly a design necessity).

## The Crisis of the Cybernetic Model

The fact that the classical model is founded on functional management may bring it into ultimate disrepute. We believe that the theory must diversify, adding complexity and being revitalized. The three-level model linking operational, tactical, and strategic management systems through information channels seems only to be workable at the lowest (operational) levels of the organization. Modern views and the consequent changes in the theory of organizations today (such as the Japanese model, Theory Z, and the prize for excellence) should form a part of the new paradigm that replaces the classical MIS model.

## Simon's Models of Bounded Rationality

The strength of the cybernetic model was its extreme simplicity. In it, a thousand theories may be incorporated and coexist without apparent violation of the overall concept. Thus it is reassuring to hear of natural reason. Just as wise men may assert that it is normal to have both rich and poor people, one may agree that there must be a sub-control-system (the managers), presumably sufficiently intelligent to make the right decision that induces the right behaviour of the sub-controlled-system (the rest of the organization at that level). Simon demonstrated the shortcomings, dangers, and perversity of this model in 1947, by introducing the concept of bounded rationality. His argument is often merely considered as an isolated case; most authors who cite this work act as if it will not invalidate the cybernetic model of the organization, and thus the MIS paradigm. Davis, for instance, questions the appropriateness of the organizational model of decision making and considers the individual model (intelligence, design, and choice). However, this model, without bounded rationality (or rent-seeking in economic terms), is not compatible with the cybernetic model.

## What if the users were intelligent?

These theoretical contradictions do not affect the development of an MIS provided that they do not directly affect the cognitive freedom of the individual managers; i.e., as long as they are willing to accept the results of the model (management controls) and act without questioning it. However, our knowledge of the complexity of social organizations causes us to reject this overly simplistic model. But it was through such models that theorists attempt to explain organizational behaviour. The more the MIS paradigm relies on the cybernetic model, the more it weakens its own legitimacy. If an executive notices that 70% of the cost of the information system is allocated to maintenance of old programs, he ends up by asking questions that should have been asked long ago: "Is our Information System built on sand?"

## 4. A New Paradigm: From MIS to OIS

Another reason for questioning the classical model is in the conceptual independence of the Organizational Information System (OIS) from the underlying technology of Information Processing. Even if we take into account the exceptional performance permitted by newer memory technology, it is important to assess also the effect of the theories of organization within a general theory. A complex system is likely to be operating upon and thus translating itself. It may be organized, informed and informing, etc. We must move from the cybernetic model of the organization to a systemic or tectologic one.

According to Ackoff, the revolution was not really possible until 1975, though by then some pioneers had made inroads into the conceptual framework. The systemic theory of the French epistemologist E. Morin [9] merges those of H. Atlan [10] and I. Prigogine [11] to show a model consistent with the works of von Foerster and Varela. Of course, the science of Organization had almost disappeared for a century, perhaps due to the influence of the Cartesian Positivism of Auguste Comte, but it is now reemerging in the Sciences of Information, Decision Making, Education, Cognition, and those others that Simon terms the Sciences of the Artificial [12].

Order and Disorder: the Organization and its Complexity

Owing to its intricacy and consequent unpredictability, the systemic model of the organization is not developed here. It is best characterized through the change in the representation of the organization, which is no longer regarded as a state but a process. Thus though the cybernetic model may be complicated, the new model is complex and cannot be reduced to a unique form. This therefore shows the concurrent need for many different views and theories; e.g., the dynamic conjunction of order and disorder cannot be explained by a structured theory. The concept of the process model is illustrated in Figure 2.

## The organization is more a process than a result

It is still possible to define a highly structured control system of an organization where the actors try to save some room to manoeuvre by taking some potential space or rent [13]. However, we must attempt to define an organized social construct that allows a radical changes to the control structure. Thus the organization is no longer the answer to a well structured problem, but a partial answer to a badly-structured one. This makes it difficult, if not impossible, to analyse; it becomes a set of actions designed to provide satisfactory results to a set of problems.

## Information informs the organization

A change of the frame of reference obviously affects the model of an information system. The focus of the organizational process changes from representation of the behavioural or decision process to the representation of the information process. Behaviour is no longer decided a priori according to the rational norm (that a subsystem must support the system in an optimal way), but that it is the outcome of self representation processes (such as the power plays of managers) within the organization. The organization is organized through its information processes; thus the organization produces the information system and vice versa. Identification of the information process within the organization may conflict with the cybernetic model (which then possesses “the means of acquisition, use, retention and transmission of information” [3]), but this would ignore the conditions under which the information was acquired or produced while the organization is being developed.

![](/api/attachments/HGBJD4JB/fulltext/images/8ad031b9a5a699de31c2edc301294c19efc415e0a85fe4631f8731d1bcf9e758.jpg)  
Fig. 2. The Organization as a Process.

## Self-representation of the activity of the organization

An action involving several actors results in the production of information appropriated and stored by the group. The control of this endogenous information process (in the sense of controlling the collection, production, and use of the data) is the essence of the Organizational Information System (OIS) model (see Fig. 3). It must allow the organization to represent itself and define its data, its behaviour, and its transformations with the means of controlling them. Then the OIS is little more complex in its representation than that of the cybernetic model.

![](/api/attachments/HGBJD4JB/fulltext/images/2431564aff7c29ef12c56dd4cd1dab521a8ffe34fa6ca4e0dd3547a4557afe24.jpg)  
Fig. 3. The Systemic Model of the Organization and the OIS

## Two Aspects of the Systemic Model

The systemic model has the great advantage of allowing two different viewpoints of organizations and information.

1. The Production of Information (a Synchronous View)

In order to operate actively within its environment, the organization performs operations that may be represented through various flows of information in the processing network. The interactions of the system with the environment and other processors (input and output) normally involved formatted data. The system needs to retain some memory of its transactions (such as its orders, invoices, deliveries, etc.). The organization has learned a somewhat arbitrary way of doing this, possibly through a filing system, and this becomes familiar for the wellbeing of the organization. The automated information system therefore needs to mimic this. Data generated by this behavior are called generic information by E. Morin, to distinguish them from the circulating information (Shannon's transmitted data). The generic information belongs to the organization that creates them. Their mode of construction (i.e., their data models, both conceptual and physical), arise from the OIS functions. Indeed, this may be the main function of the OIS, because the system and its database then become an inseparable unit.

Research on the representation of knowledge in the organization is a particularly rich sphere of activity. The sharing of information requires that it have a well defined and understood representation. Representing information through symbols allows its transmission (per Shannon), or it may provide a way to create new and meaningful or significant data (generic information) – a new semantic object. The signal (information) does not predefine a decision arising from its processing, as it would in the cybernetic model. Because decisions rely on previously created (or collected) and selected data, it is vital to identify beforehand, when and how all data is to be found and what types of processing is needed on it.

## 2. The "Memorization" of Information (a Diachronic View)

The classic example of the development of an organization is one of increasing complexity. The process is an active one which sees the emergence of a new function at the interface of both action and control; this allows the introduction of means to model both initiative and autonomy. Production of information demands a method for its storage (and thus its corporate memorization): the development of a system that is increasingly complex. Indeed, the modeling of the complex process of information storage is central to the definition and design of the OIS (its modelling of both generic and circulating information and their memorization).

It is strange that the organizational process of memorization is still misunderstood. It was only recently that the theory of organizations started to take account of this phenomenon, mainly in systemic models.

Can there be any real system or organization without a memory?

and

Can there be communication of a semantic nature without memory?

Organization and communication imply organizational memorization $[14]$ , but, as yet, we know very little about its functionality (conditions and modes). It is therefore not surprising that the impact of modern storage technologies on the OIS has been badly understood $[15]$ . Memorization is more than mere retention and storage; other functions include its addressing, indexing, classification, updating rules, etc. $[16]$ . Thus a database management system (DBMS) is merely a somewhat constrained aspect of the OIS.

## To control or to memorize: a cultural change

The evolution of the OIS from the MIS is not easy to accomplish. The addition of memory to the MIS model will be difficult to achieve. The incredible changes brought about by the microcomputer is one forcing factor. Indeed, as soon as the computer evolves and is no longer considered to be a rare resource, it can be distributed so that it allows easy access to the resources of memorization and communication. But such a technological modification would be difficult to provoke in the organization, which tends to favour computational functions. The cybernetic model cannot be used effectively in the estimation of economic factors associated with information technology; this problem should force acceptance of a systemic model.

## OIS or MIS? An Alternative

Our argument suggests that the classical paradigm is neither as universal nor as satisfying as some have believed. But any change will cause dissention: even though the new model is as well constructed as any previous one, and it proposes fair (correct) alternatives that were previously impossible. Two recent studies are worth considering here:

## 1. IS Design Methods

The profusion of methods for analysis and design of information systems (such as ISDOS, MERISE, etc.) have triggered a need to compare and contrast them $[17,18]$ under the aegis of IFIP: the CRIS studies show the difficulty in defining significant criteria for comparison, and this emphasizes the insufficiency and irrelevance of the reference model within which framework the method of analysis was developed. The organizational context is contradictory, complex, or inaccurate, and thus the theoretical basis vanishes and their vaunted benefits are not achieved (or difficult to justify).

## 2. Participative Methods in IS Development

The outstanding efforts in participative design reveal the ponderous effect of the conceptual constraints in the classical MIS model. Indeed it seems to inhibit and compromise rather than aid the process. The few successes reported seem to have involved a “conceptual anarchy”, though the conclusion of the researchers [e.g., 19,20] suggest a need to change to such a method for future success.

## Conceptual Foundations of an OIS and some Developments

It should be possible to develop a new paradigm using conceptual foundations of systems development based on the OIS; this would guarantee a solid basis for the future system, though it may take some time. Many of the basic epistemological problems are not yet sufficiently understood, though new concepts in the field have been discovered, e.g., in the science of design, self-referential and reflexive logic and the theory of organizational memorization (21). We may not have to wait for all the problems to be solved; indeed some may never be!

## Intelligent Information Systems

The future may replace the MIS with an Intelligent Information System. In 1968, the term intelligent MIS was introduced [22]. Perhaps, almost 20 years later, we can dimly see how and where it may affect the organization. We propose that it can only be achieved if we move soon from the MIS to the OIS as an intermediate step.

## References

[1] G.B. Davis, “Management Information Systems: Conceptual Foundations, Structure and Development”, 1974, Mac Graw Hill Book Co., New York.

[2] T.S. Kuhn, “The Structure of the Scientific Revolution”, the University of Chicago Press, 1962, seconde édition augmentée 1970, traduction française de la seconde édition: Flammarion, 1972.

[3] N. Wiener, “Cybernetics or Control and Communication in the Animal and in the Machine”, 1948, second edition 1961, the MIT Press, Cambridge, Mass.

[4] M.D. Mesarovic, D. Macko, Y. Takaharo, “Theory of Hierarchical, Multilevel Systems”, 1970, Academic Press, New York.

[5] R.N. Anthony, “Planning and Control Systems: A Framework for Analysis”, 1965, Harvard University Press, Boston.

[6] C.E. Shannon & W. Weaver, “The Mathematical Theory of Communication”, 1949, University of Illinois Press, Chicago.

[7] H.A. Simon, “Administrative Behavior. A study of Decision-Making Processes in Administrative Organizations”, 1947, 3e édition augmentée 1977, The Free Press, Mac Milan Pub., New York.

[8] A. Newell & H.A. Simon, “Human Problem Solving”, 1972, Prentice Hall Inc., Englewood-Cliff, N.J..

[9] Edgar Morin, “La Méthode”, tome I (La nature de la nature), 1977, tome II (La vie de la vie), 1980, éditions du Seuil, Paris.

[10] H. Atlan, “L'organisation biologique et la théorie de l'information, 1972, Ed. Hermann, Paris.

[11] I. Prigogine & I. Stengers, “La nouvelle alliance; métamorphose de la science”, 1979, éditions Gallimard, Paris.

[12] H.A. Simon, “The Sciences of the Artificial”, (2e édition), 1981, The MIT Press, Cambridge Mass.

[13] D.W. Winnicott, “Playing and Reality”, 1971, traduction française: “Jeu et réalité, l’espace potentiel”, 1975, éd. Gallimard, Paris.

[14] J.L. Le Moigne & D. Pascot (eds), ‘Les processes collectifs de mémorisation (mémoire et organisation), Actes du col-

loque d'Aix-en-Provence, CNRS, éditions de la Libraire de l'Université, Aix-en-Provence, 1980.

[15] J.L. Le Moigne, “Transmettre, Calculer, Communiquer?: co-mémoriser; quelques perspectives pour le développement de la télématique dans la société”, dans CITEL: “La Conception des systèmes télématiques”, AFCET/CITEL, Nice, 1981, pp. 3–13.

[16] J.L. Le Moigne, “Toward New Epistemological Foundations for information Systems”, dans “System Research”, 1985, Vol. 2, nb 3, pp. 247–252.

[17] T.W. Olle, H.G. Sol, C.J. Jully, “Information Systems Design Methodologies: a Feature Analysis”, 1983, North-Holland Publ. Co., Amsterdam.

[18] T.W. Olle, H.G. Sol, A.A. Verrijn-Stuart, “Information Systems Design Methodologies: a Comparative Review, 1982, North-Holland Publ. Co., Amsterdam.

[19] U. Briefs, C. Ciborra, L. Schneider, “Systems Design for, with and by the Users”, 1983, North-Holland Publ. Co., Amsterdam.

[20] U. Briefs, J. Kjaer, J.L. Rigal, “Computerization and Work: a Reader on Social Aspects of Computerization”, 1985, Springer Verlag, Berlin.

[21] J.L. Le Moigne, “Trois théorèmes de la théorie générale de l’organisation”, dans AFCET “Colloque Développement des Sciences et pratiques de l’organisation”, (AFCET, Paris, 1984), pp. 15–36.

[22] Z.S. Zannetos, “Toward Intelligent Management Information Systems”, dans “Industrial Management Review”, (depuis: Sloan Review), 1968, vol. 9, n° 3, pp. 21–38.

## Bibliography

(This bibliography provides various works which were not specifically referenced in the article, but belong to the foundation of the theory of Organizational Information Systems).

R.L. Ackoff, "Redesigning the Future", 1974, J. Wiley & S., New York.

H.I. Ansoff, "Corporate Strategy", 1965, Mc Graw Hill Books Cy, New York.

W.R. Ashby, "An Introduction to Cybernetics", 1956, Chapman & Hall, London.

Yves Barel, “Le Paradoxe et le système”, 1979, Presses Universitaires de Grenoble.

Gianluca Bocchi & Mauro Ceruti (eds), “La Sfida della Complessita”, 1985, Feltrinelli Editore, Milano.

A. Bogdanov, “Essays in Tektology”, (English translation by G. Gorelik), 1980, Intersystems Publication, Seaside Cal.

H. Brodie, J. Mylopoulos, J. Schmidt (eds), “On Conceptual Modeling”, 1984, Springer-Verlag, New York.

M.A. Costa-Martins, “Concepção duma base de dados”, 1984, RES-Editora, Porto (Portugal).

H. Crozier & E. Friedberg, “L'acteur et le système”, 1977, Editions du Seuil, Paris.

P. Dumouchel & J.P. Dupuy (eds), “L'auto-organisation: de la physique au politique”, 1983, éditions du Seuil, Paris.

G. Gorelik, “Bogdanov’s Tektology: its Basic Concepts and Relevance to Modern Generalizing Sciences”, in H.S.M. (Human System Management), 1980, vol. 1, nb. 4, pp. 327–337.

E. Grochla & N. Szyperski (eds), “Information Systems and Organizational Structure”, 1975, Walter de Gruyter, Berlin.

W.J.H. Kickert, "Organisation of Decision Making: A Systems

Theoretic Approach", 1980, North Holland Pub. Co., Amsterdam.

M. Landry & J.L. Le Moigne, "Toward a Theory of Organizational Information System: a General System Perspective", in Information Processing, IFIP 1977, B. Gilchrist Editor, North Holland Pub. Co., pp. 801–805.

J.L. Le Moigne, “Les systèmes d’information dans les organisations”, 1973. Presses Universitaires de France, PUF, Paris.

J.L. Le Moigne, “Les systèmes de décision dans les organisations”, 1974, Presses Universitaires de France, 1984.

J.L. Le Moigne, “Le vieillissement des organisations sociales”, dans “Communication”, n° 37, mars 1983, (éditions du Seuil, Paris), pp. 181–194.

J.L. Le Moigne & A. Demailly (eds), “Sciences de l’Intelligence, Sciences de l’Artificiel; avec H.A. Simon”, 1986, Presses Universitaires de Lyon.

F. Machlup & U. Mansfield, "The Study of Information: Interdisciplinary Messages", 1983, J. Wiley & Son, New York.

Piercalo Magiolini, “Costi e benefici di un sistema informativo”, 1981, Etas libri, Bompiani Souzogno.

R. Mattesich, “Industrial Reasoning and Systems Methodology”, 1978, D. Reidel Publ. Co., Boston.

J. Melese, “Approches systémiques des organisations. Vers l’entreprise à complexité humaine”, 1979, éditions Hommes et Techniques, Paris.

R. Nadeau & M. Landry, “L’aide à la décision, nature, instruments et perspectives d’avenir”, 1986, Presses de l’Université Laval, Québec.

Jean Piaget, “Biologie et connaissance”, 1967, Editions Gallimard, Paris.

Lucien Sfez, “Critique de la Décision,” 1974, 3e édition complétée 1981, Presses de la Fondation Nationale des Sciences Politiques.

H.A. Simon, “The New Science of Management Decision”, 1960, 3e édition complétée 1981, the MIT Press, Cambridge, Mass.

H.A. Simon, “The Structure of III-structured Problems”, dans “Artificial Intelligence”, 1973, vol. 4, pp. 181–201 (cf. aussi: Models of Discovery, 1977, p. 305).

H.A. Simon, "Models of Discovery", 1977, D. Reidel Publ. Co., Boston.

H.A. Simon, “Models of Bounded Rationality”, vol. 2: “Behavioral Economics and Business Organisation”, 1982, the MIT Press, Cambridge, Mass.

H. Tardieu, D. Nanci, D. Pascot, “Conception d’un système d’information: construction de la base de données”, 1979, Les Editions d’Organisation, Paris, et Gaëtan Morin éditeur, Québec.

H. Tardieu, A. Rochfeld, R. Coletti, “La méthode MERISE, Principles et Outils”, 1983, Les Editions d’Organisation, Paris.

U.N.U., “The Science and Praxis of Complexity”, 1985, The United Nation University Press, Tokyo.

F.J. Varela, “Principles of Biological Autonomy”, 1979, North-Holland Pub. Co., New York.

H. von Foerster, “Observing Systems”, 1981, seconde édition 1984, avec une introduction de F. Varela, Intersystems Publication, Seaside, Cal.

H. Zeleny, “Cybernetics and General Systems - a Unitary Science?” in Kybemetes, 1979, vol. 8, pp. 17–23.

H. Zeleny (ed), “Autopoiesis, a Theory of Living Organization”, 1981, North-Holland Publ. Co., New York.
