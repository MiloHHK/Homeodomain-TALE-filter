
import os
import shutil
import subprocess


def copy_and_trim_fasta(input_file, output_folder,editprogram):
    """Input: Path of a FASTA file containing homeodomain sequences, output folder path, name of a text writing program.
    Output: a file (file)_edited in the output folder that only includes homeodomain sequences with the TALE loop in the proper place(),
    and a file (file)_removed with the removed sequences.
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("directory made at" + output_folder)

    # Extracting file name and extension
    file_name, file_ext = os.path.splitext(os.path.basename(input_file))
    output_file = os.path.join(output_folder, f"{file_name}_filtered{file_ext}")
    output_removed = os.path.join(output_folder, f"{file_name}_removed{file_ext}")
    
    try:
        #Make a output file to copy the input file.
        shutil.copy2(input_file, output_file)
        print(f"File copied to '{output_file}'")


        # Oepn the copied file for editing
        subprocess.Popen([editprogram,output_file])

        # Read the file's lines
        with open(output_file, 'r') as file:
            lines = file.readlines()

                                    
        hitlist = []
        print("trimming...")
        for i in range(len(lines)):
            line = lines[i]
            if ">" in line and i+1 < len(lines) and i != 0: 
                if "-" in lines[i+1][23:27]: #lines[present line][line contents], if there, flags for deletion. Tinker if you need!
                    #swap "-" for "---" if your interested in a complete breakage...
                    #the triple dash will include a few more genes then a single one will, it is less restrictive.

                    #I may add a version here to alter based on length, another way to define the tale loop.
                    #or some iteration of an H or sumn before and a PYP or sub part of it after.

                    i2 = i+1
                    for DentCheck in lines[i+1:]: #searches thru each line to see if there's a next > dent.
                        if ">" in DentCheck:
                            DentCheck = True 
                            break
                        else:
                            i2 = i2+1

                    #add coordinates to the hitlist
                    if DentCheck == True:
                        hitlist.append([i,i2]) 
                    else:                       
                        #you've reached the end! that means you can nuke the rest.
                        hitlist.append([i,None])
        removed_lines = []
        #pop provides a reverse order(to not mess w lengths) and timer by cutting.
        while len(hitlist) != 0:
            reverse = hitlist.pop() 
            hit_lines = (lines[reverse[0]:reverse[1]]) #this is a list with all 3 of the lines in it.
            for x in range(len(hit_lines)): #this should be the len of the list... for us thats 3 lines.
                hit_lines[x] = str(hit_lines[x].strip("/n")) 
            removed_lines = hit_lines + removed_lines #adds it so most recent will go first (reversing direction yet again to be normal)
            del lines[reverse[0]:reverse[1]]

        
        # Write the modified content back to the file
        with open(output_file, 'w') as file:
            file.writelines(lines)
        subprocess.Popen([editprogram,output_removed]) #i did this here to not have to have two subs at once. Idk if that does anything.
        with open(output_removed, 'w') as file:
            file.writelines(removed_lines)
        

    except Exception as e:
        print(f"An error occurred: {str(e)}")

        # The below is for the future: rn this totally overwrites any file there with the same name.
        #in the future, i may have it change output file to be like (1) or (2) etc. That way it won't overwrite previous runs.
        #when that happens, if a run fails itll be annoying to have it take up space for an unedited doc.
        #I bracketed this because rn, it serves no purpouse. a overwritten unedited file or a deleted one dosent really matter.
        
        #os.remove(output_file)
        #print("file deleted from"+str(output_file))
        #any exceptions automatically delete the created file.

if __name__ == "__main__":
    # Input file path
    print("welcome to Homeodomain TALE filter.")
    print("")
    #eventually, ill create custom trims i think.
    print("Enter the path to the input alignment file: ")
    input_file_path = input("")
    input_file_path = input_file_path.strip()
    input_file_path = input_file_path.strip("'")
    input_file_path = input_file_path.strip('"')
    input_file_path = input_file_path.strip()
    print("Enter the path to the output folder. (press enter to send to the default output folder)")
    output_folder_path = input("")
    if output_folder_path == "":
        from pathlib import Path #takes your current working directory.
        #print(Path.cwd())
        output_folder_path = str(str(Path.cwd()) + "/outputs")
        #print(output_folder_path)
        #output_folder_path 
        #a = input ("thats your current workin' directory.")
    output_folder_path = output_folder_path.strip()
    output_folder_path = output_folder_path.strip("'")
    output_folder_path = output_folder_path.strip('"')
    output_folder_path = output_folder_path.strip()

    print("Input name of a system-default text editor Program.")
    print("For windows, this is notepad, apple TextEdit, and most linux has vim built in.")
    print("Shortcuts: enter for notepad, 't' texteditor, 'v' vim")
    editprogram = input("") 
    if editprogram == "":
        editprogram = "notepad"
    elif editprogram == "t":
        editprogram = "TextEdit" #need an apple person to test this
    elif editprogram == "v": #need a vimhead to test this. dont think windows has.
        editprogram = "vim"


    copy_and_trim_fasta(input_file_path, output_folder_path,editprogram)
    print("Process complete.")
    #maybe in the futre ill give you the option to rename your 2 files here before you leave, or just hit enter to leave.
    a = input("Press enter to exit.")
