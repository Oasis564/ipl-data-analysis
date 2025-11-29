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

# import csv

# with open("IPL_2018.csv", 'r') as f:
#      content = csv.reader(f)
#      content_list = list(content)
#      for i in range(0, len(content_list)):
#         print(f"Total runs scored by {content_list[i][0]} in IPL2018 are {content_list[i][4]}")
        
# get all the values inside the X6s column inside a list variable

# import csv

# with open("IPL_2018.csv", 'r') as f:
#    content = csv.reader(f)
#    content_list = list(content)
#    sixers = []
#    # in this for loop, for every row there is in content_list(aside from the first) we append sixers and put row which we convert to an integer and then specify which row we want exactly which is the X6s so that is 12.
#    for row in content_list[1:]:
#       sixers.append(int(row[12]))
#    print(sixers)
#    print(sum(sixers))
   
# import csv

# with open("IPL_2018.csv", 'r') as f:
#    content = csv.reader(f)
#    content_list = list(content)
#    wickets = []
#    # in this for loop, for every row there is in content_list(aside from the first) we append sixers and put row which we convert to an integer and then specify which row we want exactly which is the X6s so that is 12.
#    for row in content_list[1:]:
#       wickets.append(int(row[17]))
#    print(wickets)
#    print(sum(wickets))

import csv

with open("New.csv", 'w') as f:
   # The csv_writer will act as a pen to write inside a csv file
   csv_writer = csv.writer(f)
   # below will be the header for our csv file
   header = ("Name", "Class", "City")
   # below will be the data inside the csv
   data = (
      ("Cameron", "3D1", "Edinburgh"),
      ("Matti", "3B1", "Edinburgh"),
      ("Milosz", "4B1", "Edinburgh"),
      ("Damo", "3A1", "Edinburgh")
   )
   
   # below will be used to create the header inside the csv file
   csv_writer.writerow(header)
   # below code will be used to write the data inside the csv file
   for row in data:
      csv_writer.writerow(row)