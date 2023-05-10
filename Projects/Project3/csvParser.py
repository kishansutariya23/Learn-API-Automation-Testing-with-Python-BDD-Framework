import csv


# read mode
with open('C:\Consistency\Python testing\API testing\Projects\Project3\color_srgb.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)  # object
    # print(list(csvReader)) # data in list


    name = []
    hex = []
    for row in csvReader:
        # print(row[0])
        name.append(row[0])
        hex.append(row[1])
print(name)
print(hex)

# ==========
index = name.index('Red')
hex_code_red=hex[index]
print('Hex code of red is ',hex_code_red)




# write mode
# if we use 'w' then it will erase existing data so try to used 'a' so we can append to existing data
with open('C:\Consistency\Python testing\API testing\Projects\Project3\color_srgb.csv','a') as wfile:
    write = csv.writer(wfile)
    write.writerow(['ki','#000000','rgb(0,0,0)'])
