#!/usr/bin/env python
# coding: utf-8

# # This is Coding Challange for InsightGlobal Data Engineering

# In[148]:


#importing the necessary Libraries for processing the CSV files
import csv as csv
import math
import re as re
import sys as sys


# #### Data Analysis of data set at any given year

# In[147]:


# total time complexity for processing the entire dataset is O(n + nlogn + nlogn) - O(nlogn)
#specifying two dictionaries in python for saving key:value pair of topten occupation and top tep states for 
# certified visa applications

# dictionary to store key: SOC_CODE, and incremental value
topten_occupation = dict()

# dictionary to store key: EMPLOYER_STATE and incremental value
topten_states = dict()

# dictionary to map SOC_CODE to JOB_TITLE. 
# note: in the dataset, single SOC_CODE has multiple JOB_TITLE, I tried to run the dataset of year 2018, 
# for which we have the analysis available. Using SOC_CODE, I got almost same results as 2018 reports. 
# I am not sure how the JOB_TITLE is matched with SOC_CODE, here in my implementation, I took the first JOB_TITLE
# occurance in dataset, which is associated with SOC_CODE.
soc_jobtitle = dict()

# variable for saving the index of CASE_SATUS attribute in tokens (or in row)
case_status = int()

# for saving index of SOC_CODE
soc_code = int()

# for saving index of JOB_TITLE
job_title = int()

# for saving index of EMPLOYER_STATE
state = int()
    
# giving the filename using commnad line argument
filename = sys.argv[-1]

# opening the .csv file from input folder
with open(filename) as csv_file:
        
  
    # saving the tokenized attributes from the "first line" of csv into a variable
    attributes = csv_file.readline().split(';')

    # creating regular expression for identifying the required attribute from the dataset
    regexp_certified = re.compile(r'STATUS')
    regexp_soc = re.compile(r'SOC_CODE')
    regexp_job_title = re.compile(r'JOB_TITLE')
    regexp_state = re.compile(r'EMPLOYER_STATE')
    
    # the loop iteration will get us the indexes of the attribute we need in the dataset at each row
    for i,j in enumerate(attributes,0):
        
        # printing the attributes just to get insights of data
        print(i,j)
        
        if(regexp_certified.search(attributes[i])):
            case_status = i
        elif(regexp_soc.search(attributes[i])):
            soc_code = i
        elif(regexp_job_title.search(attributes[i])):
            job_title = i
        elif(regexp_state.search(attributes[i])):
            state = i
            
    
    # line count will keep the total count of number of certified case status into the dataset
    line_count = 0
    
    # sequential processing of csv file using for loop - O (n)
    for row in csv_file:
        
        # tokenizing the line by ';'
        tokens = row.split(';')
        
        #key1 is for topten_occupation() dictionary & key2 is for topten_states() dictionary
        key1 = tokens[soc_code]
        key2 = tokens[state]

        #processing only those cases which has status certified
        if(tokens[case_status] == "CERTIFIED"):
            
            # logic to implement key:value pair in dict (search complexity is O(1))
            if(key1 in topten_occupation):
                topten_occupation[key1] += 1
                
            else:
                # time complexity for insert is O(n)  
                topten_occupation[key1] = 1
                soc_jobtitle[key1] = tokens[job_title]
                
            if(key2 in topten_states):
                topten_states[key2] += 1
            else:
                topten_states[key2] = 1
            
            # keeping track of number of certified cases    
            line_count = line_count +1
    
    
# sorting the dict - time complexity according to timesort algorithm - O(nlogn)    
final_occupation = sorted(topten_occupation.items(), key=lambda kv: kv[1], reverse=True)[:10]
final_states = sorted(topten_states.items(), key=lambda kv: kv[1], reverse=True)[:10]

# just to get insight of total number of CERTIFIED cases, printing the counter
print("\n\n Number of Lines in CSV file:\t", line_count)


# In[144]:


print("Top-10 Certified Occupations of year 2014: \n\n")

# now have the all the data in the dictionaries, its time to export the o/p in .txt file
with open("./output/Top_10_occupations.txt",'w') as myoccupations:
    for x,y in final_occupation:
        # we had maintain the toal number of certified case count, (line_count), which we can use to calculate %
        # latter the percentage is rounded off using round() method
        percentage = (y * 100)/line_count
        
        # printing the data on interactive ipython
        print(soc_jobtitle[x],y,percentage)
        
        # preparing string to insert into the .txt file
        line = str(soc_jobtitle[x]) +";" +str(y)+ ";" + str(round(percentage))+"%" +"\n"
        myoccupations.write(line)


# In[145]:


print("Top-10 Certified states of year 2014: \n\n")
with open("./output/Top_10_states.txt",'w') as mystates:
    
    for x,y in final_states:
        percentage = (y * 100)/line_count
        print(x,y,percentage)
        line = str(x) +";" +str(y)+ ";" + str(round(percentage))+"%" +"\n"
        mystates.write(line)

