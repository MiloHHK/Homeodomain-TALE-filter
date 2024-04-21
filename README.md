# Homeodomain-TALE-filter
Given a fasta alignment file containing the homeodomains of homeobox protiens, it will filter out those without a TALE loop in the proper location(except the first gene as an outgroup). Should save the user a few hours of boring manual filtration.


How to use--------------------------------------------------------

Run the file with python, and your command line will open it up.

Upon opening, it will request you to enter the path of an input file. 
Copy the path of where your desired file is located, for example: "C:\Users\You\Folder_Location\TALEifier\Homeodomain_TALE_Filter_V1.0.py" on a windows computer. 
Quotation marks around the path is acceptable so if using windows you can use the copy as path command without having to trim them. The inputted file should be an alignment file in FASTA format with each gene being a protien of a single homeodomain. The program uses the ">" starts for genes that are characteristic for fasta files to search, so make sure your document in question works with this.

Next, it will request you to enter the path of an output folder, which can be done in hthe same way as the previous. If you press enter, it will default to the outputs folder within this program. If you want to set a different folder as the default, i reccomend tinkering with the code to do so, or having a shortcut to outputs in your desired folder.

Third, it will request you to enter the name of a system-default text editor program.
This is distinct from just any text-editor program: to work with your computer, the editor in question has to be one that has commands built into the OS. To make a non-default program possible, it would have to call it as a path, something that is probably uneccessary. I included shortcuts to common text editors: hitting enter will set the program as notepad, the defualt for windows. Typing "t" will enter TextEdit, the default for mac, and "v" will run vim, a default for most linux distributions. As of now, it has only been tested on windows, so I cannot promise that the other two will work on thier appropriate OS's.

#ooh maybe ill make a rename file option at the very end. like after its complete you can do it or just press enter to exit.

With this information entered, the program will read through the file input, and it will remove any genes that lack a characteristic TALE motif. The filtered set of genes will be placed in the output folder as (File name)_filtered.filetype,
and the removed genes will be placed there as (File name)_removed.filetype. The first gene in a file will be assumed to be the outgroup and will not be removed by the filter.

Eventually i may add a optional input at the end to rename the file but as of now that is not a feature.

Details and Issues--------------------------------------------------------

Becasue TALE genes can be variable in the content of thier loops and it is hard to reliably find a specific 3 acid sequence.The way it determines what a Three amino acid loop extension is by searching for where it should be, in the 23rd to 25th acid. If the alignment has a "-" acid in that space, it is assumed to be lacking the Loop extension, and is removed. If the alignment does not have enough TALE genes in it for it to treat any non-TALE genes as lacking a group there (thus treating the loop as an extension rather than a deficiency) it will not work.

This method does not work perfectly: Running the sample file through and checking through the filtered genes, some of those removed have the characteristic PYP motif that is usually nearby the TALE loop, but happen to have an acid or two listed as missing. Additionally, a gene that is clearly broken or unfit can pass through the filter if the alignment happens to treat it as having codons in this area. As homeobox genes are well known for being highly conserved and with the same number of sequences, these are not huge issues, but must be known. Searching through the removed document for potential errors is advised.

Obviously, this program requires a modern version of the Python language installed.

--------------------------------------------------------
I included two copies of the python file, one that is stripped down and one with my annotations for those looking to tinker with the files.

This project is not in any way professional nor something i expect to return to. Hopefully it works for your OS and for your project, but I make no promises to return to this and expand it's useability as it was for personal use. 
