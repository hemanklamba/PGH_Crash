# PGH_Crash
Crash Dataset Analysis related to SUDS Work Night 18th December

You can download the entire dataset at https://cmu.box.com/s/bxbuug2al6r8uzlpmytermeb6pbw1pw3
Make sure the dataset file ALL_Years_data.csv is in the same folder as the code.

Create a <b>variables</b> file (example:Variables_1.txt).
This file contains list of all the variables you are interested in.
Coding for the variables is available at: https://data.wprdc.org/dataset/3130f583-9499-472b-bb5a-f63a6ff6059a/resource/4df9a3c6-34c1-45a5-936e-80758f9f38a5/download/allegheny-county-crash-data-dictionary.pdf
Enter each variable in a separate line.

And then run the following command:

python get_dataset.py (Variable File) (Output File)
python get_dataset.py Variables_1.txt(Variable File) Variables_1_Data.csv(Output File)

