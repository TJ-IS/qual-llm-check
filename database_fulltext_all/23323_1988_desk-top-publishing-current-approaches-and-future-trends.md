---
otero_id: 23323
otero_key: "C6CEMGQK"
title: "Desk-Top Publishing: Current Approaches and Future Trends"
authors: "George Black"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.42"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Desk-Top Publishing: Current Approaches and Future Trends

George Black, IBM UK Ltd

Abstract: In order to assess future trends in desk-top publishing (DTP), it is necessary to understand the problems encountered in today's solutions.

The environment addressed by this paper is the single-user interactive workstation for a business, technical or publishing professional. A local or shared low-cost printer is assumed. High-quality and high-volume printing is treated as a remote or an external function to which a document can be transferred in machine-readable form.

## Key problem areas

## Function distribution

Assuming that an application or device driver creates a page description, where can page generation best be accomplished:

1. in the system unit?

2. in the printer adapter?

3. in the printer itself?

## System Unit-Based (Figure 1)

Advantages: Shares system CPU, memory, disk etc., and therefore provides a low-cost solution. The adapter is merely a data transport mechanism and therefore low-cost, and the printer can be unbuffered and driven at video rate, again low-cost.

![](/api/attachments/C6CEMGQK/fulltext/images/1099a596e8b1b08d153745b45448469445eb46e7609bb8bc0819e0d521608f1b.jpg)  
Figure 1. System-based solution

Disadvantages: impacts system performance by using CPU and memory for page generation; demands adequate system performance for required printer throughput.

## Adapter-based (Figure 2)

Advantages: acts as co-processor to off-load page generation from system processor/memory; gives high speed bus access to system memory or disk; can also use a video link to drive a simple unbuffered printer (low cost). The printer could be shared across multiple adapters of this type.

![](/api/attachments/C6CEMGQK/fulltext/images/b5c9c7938c121ba5f3138e7f5aefa4777f879a9fd67a1812ff48d1e8d7e699b7.jpg)  
Figure 2. Adapter-based solution

Disadvantages: adapter contains processor and memory for all aspects of page generation: PDL interpreter code, page buffers, character outlines/ bitmaps etc. Hence it is a more expensive adapter than the simple video driver in a system unit-based generation.

## Printer-based (Figure 3)

Advantages: completely independent printer; off-loads system unit as in an adapter-based generation;

can have multiple system adapters or network links; uses standard built-in system printer adapters.

![](/api/attachments/C6CEMGQK/fulltext/images/bcf0ff9365bd36116a4cffd3f940477a59ad454bd70d96614390282732eaa8b4.jpg)  
Figure 3. Printer-based solution

Disadvantages: standard system printer adapters are typically low speed and output only. Consequently access to system resources may be limited by this type of adapter. The printer contains processor and memory for all aspects of page generation, PDL interpreter code, page buffers, character outlines/bitmaps – therefore higher cost as for an adapter-based generation.

## Data volume

## Data stream lengths

Page description languages (PDLs) produce large data streams, containing images, graphics and unformatted text, all with many presentation attributes. Therefore there is a large volume of data to be moved from the application to the PDL processor. A typical text page can be 6k bytes or more and pages with complex graphics and/or large images can be 30k — 1 megabyte! Even a typical 4 column newsletter A4 page, containing just text in a single typeface, can be 30k.

If such amounts of PDL data are transmitted from the system unit, it can take several seconds (0.1–10 s) per page, depending on the adapter link performance and page complexity:

Serial approx 1k bytes/s
Parallel approx 20k bytes/s
Non-standard approx 500k bytes/s

Page Buffer Sizes

<table><tr><td rowspan="2">Printer resolution</td><td colspan="2">Paper size</td></tr><tr><td>Letter/A4</td><td>Legal</td></tr><tr><td>300 dpi</td><td>1 megabyte</td><td>1.2 megabytes</td></tr><tr><td>600 dpi</td><td>4 megabytes</td><td>4.8 megabytes</td></tr><tr><td>1200 dpi</td><td>16 megabytes</td><td>19.2 megabytes</td></tr><tr><td>2400 dpi</td><td>64 megabytes</td><td>76.8 megabytes</td></tr></table>

## Trade-Offs

If the printer cannot be stopped once the page is in motion (typically for a laser printer), then a ram page buffer is required, otherwise the disk to ram to printer bandwidth must match the print engine paper rate, between frame sync and end frame, for each page. This is typically 1.8 to 2.3 megabits per second for a 300 dpi print engine.

If a stop-start (re-registerable) printer is used (ink jet), then the picture can be generated in swathes with a reasonable size swathe buffer of say 4k-5k bytes. The PDL interpreter must clip the source PDL for each page against each swathe on the page (Figure 4).

![](/api/attachments/C6CEMGQK/fulltext/images/2e137d17a608c3ed673794373fe1a4d0c22fe2e6bd8d02246a1d2d67c50adb7a.jpg)  
Figure 4. Swathe clipping

This would obviously reduce page memory requirements greatly but at the expense of processing time and hence printing performance. However, a source PDL buffer is required to retain the page definition while multiple clips are performed, and for a full page image this can approach page buffer size. The alternative is to re-transmit the source PDL as needed, again with a performance impact.

## Colour and greyscale

Depending on the printer technology, colour or greyscale may require either multiple passes of the page and/or multiple bits per dot in the page buffer. Some colour printers require four passes — cyan, magenta, yellow and black — requiring the PDL interpreter to generate the colour separations (four page buffers), one at a time for each colour pass. Some thermal transfer printers require a colour value per printed dot, ie 4 bits for 16 colours, etc, in order to select the correct ink for a single pass process. This obviously increases buffer size and normally requires a start/stop (re-registerable) paper transport, as a non-stop transport would require an unacceptably large buffer or very high bandwidth disk to paper path, both of which are expensive.

## Rip Performance

Rastering graphics primitives, clipping and transforming objects (including text character outlines) and image processing, such as half-tone generation or non-linear scaling up or down, requires very high speed general purpose processors or special graphics-assist chips in order to create page buffer content at a rate which matches the rated print speed, or paper throughput, of the printer.

Special hardware is also often used simply to move, or copy, previously rastered images from one memory address (byte + bit offset) to another. Such assists take the form of simple barrel shifters through to special bit array manipulators which coupled with Or-ing memory give high speed Boolean functions within the read/modify/write cycles (Figure 5).

![](/api/attachments/C6CEMGQK/fulltext/images/080e0aff2e0fa4e6da3fea4d3a5104750af32621bc3aff7b26ef0aba6f8e85c8.jpg)  
Figure 5. Bit block transfer

## Font definitions

Two types are used, a vector outline form and character images or bit maps.

## Outline definitions

These are more concise but require rastering to the required size in bit-mapped form (Figure 6).

The outline definitions may contain scaling tips and the rasterization follows grid-fitting rules.

![](/api/attachments/C6CEMGQK/fulltext/images/c90f8e3580b718e1d0da8031f407fb97cccec858ba0d532b0e5361b17d9a5051.jpg)  
Figure 6. Outline character

## Bit-mapped definitions

These are ready to print and only need positioning. However, a unique representation is needed for each size and face (Figure 7). A 300 dpi 72 point 'H' would require about 10k bytes in memory unless some form of compression is used, coupled with a special decompress, translate and store chip.

![](/api/attachments/C6CEMGQK/fulltext/images/dbf37ba08258c47aeb6b60f8f0dfad34d8819540ec2f299d789b67343e3d222a.jpg)  
Figure 7. Bit-mapped character

## Font storage requirements

Whether stored on disk, in ram or in rom, fonts are large. A 192-character bit-mapped typeface is:

for 9 point, approximately 25k bytes  
for 12 point, approximately 45k bytes  
for 16 point, approximately 80k bytes

Outline forms are 10k-30k bytes, depending on the complexity of the outlines, eg Helvetica is simpler than Gothic. Because of the size of bit-mapped fonts at high resolution, and high point sizes, it becomes necessary to use outlines which are more concise and allow more functionality, in that they can be scaled, rotated and sheered before being rastered into the bit mapped form.

## Font cartridges

The number of different typefaces and or sizes which can be used on a single page is limited by the number of cartridges which can be inserted into the printer at any one time. For soft fonts (bit mapped or outlines), the number is limited by the available memory in printer. For total flexibility, access to disk-based fonts is necessary, whether bit mapped or outline representation is being used.

## Font cache

For performance reasons, most PDL interpreters which use outline font definitions maintain a cache of the most recently used (ready-rastered) bit maps, on the assumption that most documents don't use too many face and size combinations. At the start of day some printers can be told to generate a cache made up of certain face and size combinations, prior to printing.

Other printers are loaded with a ready-built cache containing system-defined or user-requested faces and sizes.

## Print engine types

Lasers: non-stop (so far); fast, cheap and reliable; good quality; typically 300 dpi.

Ink-jet: start/stop (re-registerable); or thermal slow but cheaper.

Transfer: recently up to 300 dpi; same good quality.

Dot matrix: start/stop; very slow; very cheap; lower resolution draft quality only.

Typical laser printer paper, feed and print options

Sizes: B5, A5, A4, A3 + envelopes.

Choice: single or multiple feed trays.

Copies: simplex (typical); duplex (a few; expensive).

## Rated print speed

Typically laser printers are rated at 6, 8, 12 or 20 pages per minute. This is the speed of the paper path. The actual page rate is content-dependent. Typically simple text will print at about rated speed, as will multiple copies of a single page. Mixed text, graphics and image pages print significantly slower than the rated speed.

## PDL interpretation

Today there are two types of laser printer support; one for printers that do not have a full page image buffer and another for those that do. The former is limited to supporting data stream objects which can be processed completely to laser scan lines at or faster than the paper speed in left to right, top to bottom order. This typically means bit-mapped text plus images restricted to a built-in buffer size. The process works as follows (Figure 8):

![](/api/attachments/C6CEMGQK/fulltext/images/d8f69866dfc446e9eeda31f4f44a85b8f8c2babb5c64618c5d7598b87d201e02.jpg)  
Figure 8. PDL processing without a page buffer

The latter can process a data stream containing any text image or graphics object, together with its attributes and transformations; and 'paint' the page buffer prior to starting the paper along its path (Figure 9).

Postscript printers work in this manner and the IBM Personal Pageprinter is one such example.

![](/api/attachments/C6CEMGQK/fulltext/images/18727456ec894dc68722e944192c3fe8392dbfae3e0f9e297d9c489c8d82ca10.jpg)  
Figure 9. PDL processing with a page buffer

## PDL syntax design

Given that transmission time is a significant portion of page processing time, it is important that the PDL should be concise, from the data stream length point of view.

## PDL generation

It is even more important that applications which generate PDL should produce efficient PDL. Some of the first generation applications could be improved dramatically in this respect. It is not uncommon to see the graphics state saved and restored around each application object, as well as per page. This is very wasteful in terms of processing time and a more global optimization of the scope of attributes and transformations should repay the programming effort many fold.

## Sharing laser printers

## Sharing boxes

A sharing box allocates the printer to one user at a time for the duration of a document (Figure 10). The other printers are given a 'busy' signal.

![](/api/attachments/C6CEMGQK/fulltext/images/cb23d2c80ce66c2cd31b7af9ae42aad5a661903a2c9e588ff17557231e401700.jpg)  
Figure 10. Printer sharing box

## Networked

(a) Networked PCs with a Lan Print Server containing a spool queue and the printer drivers (Figure 11)

![](/api/attachments/C6CEMGQK/fulltext/images/b99f40854998aeb275a6e75def0c27f4d19fa2b6a120763980e16acc52f285d0.jpg)  
Figure 11. Lan print server solution

(b) The Lan adapter and protocol support is in the printer. Workstations on the network bid for the printer and handle their own print spooling (Figure 12).

![](/api/attachments/C6CEMGQK/fulltext/images/d14ebe4fc35c1ef5991f49a82c7a71207bbde7c653ede214c5a32688ebfa6df7.jpg)  
Figure 12. Lan attached printer

## Document type identification

Some printers can accept more than one type of input because they offer not only support for a PDL, but also emulation of other printers. When the spool queue can contain a mixture of files (documents) from various applications, perhaps in other workstations, some of which support PDL, while others support some form of ASC11, (eg Postscript + Diablo 650), then the print server has to tell the printer what to expect next. This requires architected document headers which define both the data stream type and in some cases the server resources required, eg paper size, fonts, etc. This allows either the print server or the printer itself to correctly interpret the data stream received.

In many systems today, this document type differentiation relies on simple convention such as 'If first character of file is % then treat as PDL, otherwise ASCII'. This is a less than perfect situation, as not all applications are developed with remote print servers in mind.

## The IBM approach

## IBM Personal Pageprinter 4216-20

This is an adapter card in system unit design, with a bi-directional, 2 bytes wide, extended parallel port interface which gives a data rate for transmission of PDL to the adapter-based RIP of around 200k + Bytes/s. The RIP is a Motorola 6800 processor with half a megabyte of write protectable program store, for the downloaded Postscript interpreter and Proprinter emulator, plus two megabytes of 120ns ram for page buffer, font cache and work space.

A barrel shifter with memory Or-ing on write cycles is used and there is an option to clear the page buffer on read cycles.

A FIFO buffer is used for video output of page data to the printer at 1.8–2.3 MHz. The printer is based on the six pages per minute RICOH Laser engine, which is a high quality, 300 dpi, write black device. The only switches on the printer are: POWER ON/OFF, ONLINE/OFFLINE and TEST. All other printer settings are under operator or application control through the PC.

There are 43 typefaces available with the printer, and many more additional typeface families are sold by Adobe Systems Inc. Times, Helvetica and Courier are always loaded and a further 25+ of those available can be downloaded for concurrent use. The adapter supports the Adobe Postscript page description language and also emulates the IBM Proprinter.

## Future trends

IBM is investigating most of the problems discussed above including: PC-based low cost solutions; adapter and printer-based high performance solutions; colour separation; colour printing; other print engines; use of other general and/or special purpose processors and VLSI logic; printer sharing via sharing boxes; networks and mainframe attached printers; integration of screen and printer support via common application interfaces; improved installation and ease of use; integrated scanner support, and improved font management.

When solutions are found which meet customer requirements in terms of cost, performance and function, then products will be brought to the marketplace.

The DTP industry in general is progressing towards the same goals, but my personal view is that we will see today's function and performance for less than £1000 before any major leaps forward at higher prices.

## Biographical notes

![](/api/attachments/C6CEMGQK/fulltext/images/809bb76ddd1d1e4e1e1da42bb447a17b5347762938b3166f3b38eb980aaddd45.jpg)

George Black is a development programmer at IBM UK Laboratories Ltd. at Hursley near Winchester, Hants. He was educated at Bolton School and Keele College North Staffs. Whilst working for the Atomic Energy Authority in Reactor Group Headquarters at Risley in the early sixties, he found he was more interested in the problems of computers than the application programming he was involved in. He joined IBM's Research and Development Laboratory, and in 1964 was just in time to work in a team on the development of the PL/I programming language and its first compiler. Through the late sixties and the early and mid-seventies he was involved in prototype design for the VSAM disk access method, design and development of the VTAM telecommunications access method and enhancement of the Customer Information Control System (CICS) which is a very successful trans-

action processing system. The late seventies and early eighties moved him into display graphics support, first with the mainframe Graphical Data Display Manager (GDDM) and the 3279 colour display terminal, then with PC based graphic workstations, the 3270 PC G, and GX. From 1986 he was part of the small team which planned, designed and developed the Personal Pageprinter. He is now in the Publishing Systems Advanced Development Group.

Address for correspondence: G. M. Black, Mail Point 094, IBM United Kingdom Laboratories Limited, Hursley Park, Winchester, Hampshire.
