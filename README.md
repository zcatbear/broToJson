# broToJson

This will convert a given bro log file to json with parameters if you have such needs.
This is to be run with switches, for which argparse is used  
They are as follows:  
- `-p/--printout` This prints out the output to the screen and forgoes the output file option
- `-i/--inputFile` This is the file to be ingested (this is required)
- `-o/--outputFile` This is the file to be output after being converted. Note, this doesn't check to see if you already have a file by that name, so it will overwrite what exists here already if there is something with the same name. Default is broToJsonOut.json


