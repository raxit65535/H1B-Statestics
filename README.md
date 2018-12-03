# H1B-Statestics
coding challange for Insight global


# Implementation System
- Ubuntu 18.04 OS, Python3 - ipython
- I have used Jupyter notebook to code entire project, latter I downloaded the .py file from Jupyter ipython.
- ipython notebook is in the "src" folder. 

# Project Structure

- The directory structure for your repo should look like this:

      ├── README.md 
      ├── run.sh
      ├── src
      │   └──InsightGlobal-DataEngineering.py
      ├── input
      │   └──h1b_input.csv
      ├── output
          └── top_10_occupations.txt
          └── top_10_states.txt
    
- input folder contains the dataset which we want to analyze on given measures in the problem statement
 
- Once the .py file successfuly runs, it will create two output files, top_10_occupations.txt and top_10_states.txt
 

# run.sh for running the code
- As specified in the requirement section, created run.sh file which include bash command to run the .py file by passing the
   data set as a command line argument.
- Here both the output files (top_10_occupations.txt & top_10_states.txt) will be generated in "output" folder, so need need to give       output file path as command line argument. We will only provide the path of dataset as command line argument as shown below. (here my   dataset is inside input folder, hence I am giving path ./input/"dataset-name")
- $> python3 ./src/InsightGlobal-DataEngineering.py ./input/h1b_input.csv
  
- I have tested the code on the three csv datasets H1B_FY_2014.csv, H1B_FY_2015.csv, H1B_FY_2016.csv share on parent repository.
   [link](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing)
 
- I have also tested the code on H1B_2018.xlsx dataset given on the official site, just to double check the analysis is congruent 
   to the ready made report provided.
 
-  note: in all three dataset, single SOC_CODE has multiple JOB_TITLE, hence, I tried to run the dataset of year 2018, 
   for which we have the analysis available. Using SOC_CODE, I got almost same results as 2018 reports. 
   I am not sure how the JOB_TITLE should be matched with SOC_CODE optimistically, but here in my implementation, 
   I took the first JOB_TITLE occurance in dataset, which is associated with SOC_CODE. I have provided detail comments to explain 
   each step.
 

   
###### note: I was working on different repository at first, but I tried to push the dataset of more than 100 MB on that repository and by mistake commit the transaction. Since, then I was not able to push anything, so I made this new repo from scratch after the development was over.
