# Torrent video names
The Torrent videos renamer is a command-line tool that helps you convert file names from dot-separated format to space-separated format and exclude unnecessary file information, including only the file name like the following:
```
The.House.I.Live.In.1945.DSR.x264.mp4 -> The House I Live In.mp4
```
This tool is designed only for media files with common video extensions.

## Usage
To run the program, use the following command-line format:
```<python>
python rename.py [-f FILE] [-d DIRECTORY] [--dryrun]
```
## Parameters
* -f, --file: Specifies the input file to be renamed.
* -d, --dir: Specifies the input directory containing files to be renamed. If this option is provided, the program will process all <u>video</u>files within the directory.
* --dryrun: Optional flag that enables the dry run mode. When provided, it only prints the changes without actually renaming the files.


## Contributing
Contributions to the File Renamer project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the GitHub repository.
