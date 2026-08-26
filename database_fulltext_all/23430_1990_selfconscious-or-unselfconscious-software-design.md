---
otero_id: 23430
otero_key: "D5ZGFF22"
title: "Selfconscious or unselfconscious software design?"
authors: "Martin Loomes"
year: "1990"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1990.6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Selfconscious or unselfconscious software design?

MARTIN LOOMES

Hatfield Polytechnic, College Lane, Hatfield, Herts AL10 9AB

Abstract: Anyone who is involved in computer science education will be used to engaging in passionate debates over questions such as 'What programming language should we be teaching'? Moreover, if these debates take place in front of colleagues from other disciplines, for example when joint schemes are being developed, then concern is often expressed about the inability of computer scientists to come to any generally accepted conclusions.

In this paper the view is proposed that the key questions of computer science education are really manifestations of a much deeper issue in computing which has been alluded to in various publications, but never discussed to a generally accepted conclusion by the computer science community at large.

## Two paradigms

Thomas Kuhn, writing in the context of the philosophy of science, has suggested that scientific communities can operate in two modes (Kuhn, 1970). The first is the stable situation of normal science, where scientists accept some underlying principles of theory, method, application, etc. and work within these to resolve the unanswered questions of the day. Disagreements that arise between two scientists can usually be resolved by appeal to these collectively held principles.

The second mode is that of scientific revolution, where conflicting groups of underlying principles are held by two or more scientific communities. In this mode normal science can still take place within each community, but normal scientific progress involving scientists from more than one community cannot take place, because there is no generally accepted body of principles available to resolve the open questions. Kuhn suggests that when such divisions of a discipline occur the progress of normal science is impaired until one of the communities can persuade the rest to adopt their body of principles, or ‘paradigm’.

If two such conflicting paradigms exist in computing, then many of the passionate debates we currently observe might be explained. Moreover, if we could identify the two paradigms and divert some of the energy currently spent on inter-paradigm discussion of detail into resolving the revolutionary phase, then perhaps normal science could be resumed. Educationalists should be ideally placed to do this. The rational discussion that should accompany curriculum design, for example, should necessitate the identification of the paradigm. Unfortunately, most teachers of computing seem to have been beguiled, or trapped, into discussing the manifestations of the various paradigms without questioning the paradigms themselves. They have become bewitched by the issues of specification and implementation (the what and how) without the explication (why), and it is only in the 'why' that the principles of the paradigm are called into question explicitly.

This problem is exacerbated by the naive adoption of a producer-consumer model of education, that casts industry in the role of consumer. The adoption of this model allows industry to influence (or even to dictate) the 'what', leaving education to decide on the 'how'. The 'why' is subsumed under the adoption of the model, and never called into question. One of the major motives behind this paper is to react against this model, and to put the 'why' back into educational practice.

A number of possible candidates for existing paradigms within current software engineering practice can be detected. Hirschheim and Klein (1989), for example, discuss four such paradigms that may be considered to pervade current information systems development. The paradigms being considered in this paper are rather more basic than those of Hirschheim and Klein, and call into question some of the premises that implicitly underpin the latter.

## Selfconscious or unselfconscious design?

In his famous work on architecture, Alexander (1964) discusses the distinctions between selfconscious and unselfconscious design. It is far from obvious that we are entitled to treat these as two distinct paradigms in the sense (or the one of many senses) of Kuhn, but a number of insights may be gained by trying to do so.

## Unselfconscious design

In unselfconscious design a designer does not think about the process of design itself. There are right ways and wrong ways of doing things, but these are passed on within the culture rather than being based on explicit principles known to each designer. Because the designer does not stand back from the process there is no possibility of experimentation with the process. Changes to working habits are made as a result of immediate feedback through failure. This process of evolution only really works if the designer is able to appreciate the failure first hand and so react to the feedback immediately. Unselfconscious design is passed on from generation to generation by exposure to the design process and imitation.

## Selfconscious design

Alexander states that selfconscious design is required when the artifacts being produced reach a level of complexity that can no longer be understood by a single individual. The design process itself then has to be subjected to analysis to enable work to be divided. Furthermore, reacting to feedback through failure may become unrealistic: constructing numerous versions of an artifact which evolve into a good fit with the environment to satisfy some need is not usually an economic way of proceeding. The designer has to find ways of dividing the problem into manageable size chunks through analysis. In short, the designer needs to utilize abstraction, both to subdivide the problem and also to allow experimentation with aspects of the artifact without having to build it completely.

Traditional ways of doing things are not to be dismissed lightly, for they may well provide insights into methods that work for particular classes of problem. The responsibility for selecting the method, however, rests with the designer. Tradition itself does not relieve the designer of this responsibility. Alexander refers to this as the 'loss of innocence'. He makes the point that the designer may still decide to accept the traditional ways of doing things, or even decide to design purely by intuition, but that such decisions must take place.

## Software engineering design

Over the years there have been a number of publications suggesting that software engineering needs to become more scientific (Gries, 1981) or 'rigorous' (Jones, 1980), and less like a 'craft' especially 'witchcraft' (Hoare, 1984). These seem very similar to the suggestion that the discipline should become more selfconscious. Indeed, one might take selfconsciousness as a prerequisite for these other suggestions.

If, as is being suggested here, this move to self-consciousness constitutes a paradigm shift, then it is obvious why many topics of discussion have produced stormy debates, very often leading nowhere (DeMillo et al., 1977, Dijkstra, 1978). The different communities will try to interpret the topics in their own paradigms and the resulting debate will not be grounded in shared principles.

Furthermore, Alexander suggests that there are two standard responses made by unselfconscious designers to protect themselves against the loss of innocence.

\- The designer takes refuge in terms such as 'flair', where the ability to design is seen as an innate characteristic which cannot be questioned. Indeed, the mere act of seeking to analyse it may destroy it.

\- The designer takes refuge in schools or established styles, where like-minded colleagues provide a degree of support.

Both of these responses can be observed in software engineering design. The former is now largely discredited by terms such as 'hacking'. The latter, however, can be seen to be going strong. Object oriented design, methods such as SSADM and, ironically, formal methods can all be viewed as styles within which designers seek refuge from the loss of innocence (Mills, 1980). This should not be taken as a criticism of styles, of course, only as a warning that such styles may act as places of refuge regardless of the intentions of the initial proponents of the style.

## Illustrations

In this section we will examine a few current topics of debate amongst teachers of software engineering, and show how they can be viewed in this light. In particular, note how in each case the conflicting paradigms fuel the debate, but how no amount of debate can resolve the discussion until the paradigms themselves are questioned.

## Formal methods

'How, why and where should we teach formal methods'? To the teacher of selfconscious design these questions amount to issues such as:

\- Do we teach formal methods because they are directly useful, or because they are fundamental in some sense?

\- How do we teach students to appreciate the role of formal methods, so they are able to select appropriate techniques for particular occasions?

\- How do formal methods fit into the whole area of design?

\- How do we prepare the student to learn these techniques when they are required?

\- Upon what principles are formal methods based?

\- What impact will formal methods have upon the students' perception of other courses? Will they be able to apply these techniques to material learned in courses such as Computer Systems and Networks?

To a teacher of unselfconscious design a difficult set of issues will be raised.

\- Are the methods widely used in industry, so that 'schools' exist for the student to join? If so, which school should we elect to join (Z or VDM, CCS or CSP, ...)?

\- How can the methods be reduced to procedures that the student can learn to replicate?

\- Are the steps involved well-defined so that they can be taught?

\- Are there tasks to be done in other courses that can be used to provide practice for the students in the techniques covered?

Notice that the substance of any discussion between the two may not make apparent these differences. Both might ask whether a method is being used in industry, and how, but the motivation for the question is different, and the value systems being used for deciding action based upon the answers will also be different. For one, the widespread use of a technique may be sufficient reason to consider teaching it, for the other, the very rejection of a method by industry may render it important. Similarly, both may seek the widespread use of these methods in other courses, but for very different reasons.

## Proprietary methods

The question of whether we should teach methods such as JSD, SSADM or Mascot will also be treated rather differently. The teacher of unselfconscious design is likely to want to teach such methods because they are directly useful. The teacher of selfconscious design might want to teach them because they call into question fundamental issues of design, or because the student might benefit from an analytical study of proposed methods in order to provide insights into how things might be done. Equally likely, however, the latter may want to avoid them because they carry the inherent temptation for the student to view them as ways of avoiding the loss of innocence.

Teaching methods will differ too. The teacher of unselfconscious design will want to make the student proficient in the use of a method, including any rules of a meta-method governing the selection of method. The teacher of selfconscious design will want to teach the principles on which such methods are based, or to discuss the dangers of utilising methods which are not based on sound principles.

## Theory and practice

It is likely that these terms will be used differently within the two paradigms. Unselfconscious design has no real role for theories, although it may have a role for procedural rules that have been distilled from them. In this paradigm, theory is likely to be viewed as largely irrelevant, which might be allowed into isolated courses to placate colleagues from the opposing paradigm. These courses are likely to be delayed until the final stages of a scheme of study, and made optional. The term ‘theory’ is attributed a meaning approaching idle speculation for its own sake. ‘Practice’ will be used to describe the activity of actually designing in an unselfconscious way.

Selfconscious design, however, is likely to be founded on theories. Far from being isolated, these theories will be integrated into the subject from the beginning. Delaying theoretical topics until the end of a course does not make sense: students would have to be taught outside of the paradigm in the beginning. The term ‘theory’ is now being used to describe that which has an important role in determining action: practice is the manifestation of the application of theory. The two terms are no longer in opposition, but are tightly coupled by the nature of the paradigm.

## The interface between school and higher education

A thorny problem for many departments teaching computing has been how to react to computing as taught in schools and colleges. There is little doubt that pupils in schools are presented with an unself-conscious paradigm. There is virtually no discussion on what it means to design a program, but pupils learn 'how' to write programs via examples and rules.

This presents a major problem for students and staff alike when such pupils enter those higher educational establishments which teach according to a self-conscious design paradigm. Students are frequently being told that their ways of solving problems are not satisfactory, but they receive the feedback from the artifact itself that it works. Within their paradigm this is the final arbiter. They view themselves as competent designers, and often react to the risk of losing their innocence by extrovert acts of hacking to demonstrate their flair. The problem is how to persuade such students to reject their existing paradigm and start again in a new one.

Teachers of unselfconscious design may well see the situation differently. For them, the problem is one of mixed ability teaching. The students with considerable experience of computing will be seen as well advanced in the correct paradigm. The challenge is to teach these students alongside those who have no previous experience.

## Programming languages

The debate on programming languages will follow a similar course to that on design methods. The teacher of unselfconscious design will want languages that the student can be taught to program proficiently in, and preferably languages that are being used in existing styles within industry. The teacher of selfconscious design will want languages that facilitate the discussion of principles upon which design decisions must be made.

Both of these approaches may have the overt aim of 'teaching programming', but the term means widely differing things within the two paradigms, and in particular, the metrics that will be used to measure success will be very different. Within the unself-conscious paradigm, a working program will be seen as a dominant indicator of success. Within the self-conscious paradigm the student's ability to explain the working, or non-working, of a program will be seen as paramount (of course, it will be hoped that if a student can explain why the program does not work then appropriate remedial action can be taken).

## Conclusions

This paper has not sought to give any answers, but to raise questions. It has also attempted to suggest a possible framework for structuring the resulting discussions, although no attempt has been made to justify this framework.

There is one problem of regression, however, which has been ignored: proponents of the unselfconscious paradigm are likely to carry this paradigm over to the design of software engineering curricula. In this case, much of this paper will be viewed as threatening, as it calls for a loss of innocence in the area of education. Individuals who view curriculum design in this fashion are likely to follow tradition, tinker as a result of feedback, or hack with 'flair'.

This paper has taken an intentionally polarized view. In reality, of course, most teachers will not fit exactly into one paradigm or the other, but are struggling to find any tenable paradigm in the light of the pressures they face. The major tenet of this paper is that until the level of discussion can be lowered from addressing the symptoms of conflicting paradigms to identifying the paradigms themselves, software engineering will never manage to become a coherent discipline. It is hoped that by putting forward two deliberately extreme paradigms such debate may be fostered.

## References

Alexander, C. (1984) Notes on the Synthesis of Form, Harvard University Press.

Dijkstra, E.W. (1978) On a political pamphlet from the middle ages, ACM Software Engineering Notes, 3, 2, 14–16.

DeMillo, A. Lipton, J. and Perlis, J. (1977) Social processes and proofs of theorems and programs. In Proceedings of the Fourth ACM Symposium on Principles of Programming Languages, 206–14.

Gries, D. (1981) The Science of Programming, Springer-Verlag.

Hirschheim, R., and Klein, H.K. (1989) Four paradigms of information systems development, Communications of the ACM, 32, 10, 5–16.

Hoare, C.A.R. (1984) Programming: Sorcery or science. IEEE Software, 5–16.

Jones, C.B. (1980) Software Development: A Rigorous Approach, Prentice Hall.

Kuhn, T.S. (1980) The Structure of Scientific Revolutions (enlarged edition), University of Chicago Press.

Mills, H.D. (1980) Software engineering education. Proceedings of the IEEE, 68, 9, 1158–62.

## Biographical notes

Martin Loomes is a senior lecturer in the Department of Computer Science, Hatfield Polytechnic.

Address for correspondence: Department of Computer Science Hatfield Polytechnic, College Lane, Hatfield, Herts AL10 9AB, UK.
