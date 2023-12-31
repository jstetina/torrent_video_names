#! /bin/python3
import argparse
import os

from torrent_video_names.functions import rename

def rename_file(file_path:str, dryrun=False) -> str:
    prev_file = os.path.abspath(file_path)

    if not (os.path.exists(prev_file) or dryrun):
        return False

    if (new_file := rename(prev_file)) is False:
        return False
    
    if not dryrun:
        os.rename(prev_file, new_file)
    else:
        print("OLD:", os.path.basename(prev_file))
        print("NEW:", os.path.basename(new_file))

    return new_file

def rename_dir_files(dir_path:str, dryrun=False):
    files = [dir_path + path for path in os.listdir(os.path.abspath(dir_path))]
    for file in files:
        prev_file = os.path.abspath(file)
        rename_file(prev_file, dryrun)        

if __name__ == "__main__":

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Argument parsing
    parser = argparse.ArgumentParser(
                    prog = "Torrent names", 
                    description = "Rename torrent video files"
            )

    group = parser.add_mutually_exclusive_group(required=True)
      
    group.add_argument(
            "-f","--file", 
            type=str, 
            action="store",
            dest="input_file_name",
            help="Name of input file"
        )

    group.add_argument(
            "-d","--dir", 
            type=str, 
            action="store",
            dest="input_dir",
            help="Name of input directory"
        )

    parser.add_argument(
            "--dryrun", 
            required=False,
            action="store_true",
            dest="dryrun",
            help="Prints file name(s) on screen, without renaming"
        )

    args = parser.parse_args()

    if args.input_file_name:
        rename_file(args.input_file_name, args.dryrun)

    elif args.input_dir:
        rename_dir_files(args.input_dir, args.dryrun)




