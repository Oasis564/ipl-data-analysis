# read all the content from IPL_2018.csv

# with open("IPL_2018.csv", 'r') as f:
#     content = f.read()
#     print(content)
    
# read the entire file and print each row

# with open("IPL_2018.csv", 'r') as f:
#     content = f.readlines()
#     for i in range(0, len(content)):
#         # By putting square brackets then i inside of the print next to content we are actually starting from the first line till line 144(all the lines in the file).
#         print(content[i])
        
# read the entire file and print each row using the CSV module

# import csv

# with open("IPL_2018.csv", 'r') as f:
#     content = csv.reader(f)
#     for row in content:
#         print(row)

# read the entire file and print each row using the CSV module and ',' as the delimeter

# import csv

# with open("IPL_2018.csv", 'r') as f:
#     content = csv.reader(f,delimiter=",")
#     for row in content:
#         print(row)

# read the entire file and print each row using the CSV module and convert th content into a list before printing
  
# import csv

# with open("IPL_2018.csv", 'r') as f:
#     content = csv.reader(f)
#     content_list = list(content)
#     for i in range(0, len(content_list)):
#         print(content_list[i])
        
# Total runs scored by Aaron Finch in IPL2018 are 134

import csv

with open("IPL_2018.csv", 'r') as f:
     content = csv.reader(f)
     content_list = list(content)
     for i in range(0, len(content_list)):
        print(f"Total runs scored by {content_list[i][0]} in IPL2018 are {content_list[i][4]}")