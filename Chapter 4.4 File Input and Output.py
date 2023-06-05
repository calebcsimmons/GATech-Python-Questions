 #? Chapter 4.4 File Input and Output
 
def average_file(filename):  ## Average of a File
    output_file = open(filename, "r")
    allLines = output_file.readlines()
    numList = []
    try:
        for line in allLines:
            numList.append(int(line))
        average = sum(numList) / len(numList)
        return average
    except:
        return "Error reading file!"
    finally:
        output_file.close()
 
def st_dev(filename):  ## Standard Deviation of a File
    file = open(filename, "r")
    allLines = file.readlines()
    allLines = [int(x) for x in allLines]
    meanDiff = []
    mean = sum(allLines) / len(allLines)
    for line in allLines:
        value = (line - mean)**2
        meanDiff.append(value)
    sumDiff = sum(meanDiff)
    StDev = (sumDiff/len(allLines))**0.5
    return StDev
    
def find_net_force_from_file(filename): ## Net Force From File
    from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt
    fileOpened = open(filename, "r")
    allLines = fileOpened.readlines()
    force_list = [item.strip() for item in allLines]
    force_list = [tuple(map(int, item.split())) for item in force_list]
    fileOpened.close()
    all_hor_forces = []
    all_vert_forces = []
    
    for tup in force_list:
        magnitude, angle = tup
        hor_force = magnitude*cos(radians(angle))
        vert_force = magnitude*sin(radians(angle))
        
        all_hor_forces.append(hor_force)
        all_vert_forces.append(vert_force)
        
    total_hor_force = sum(all_hor_forces)
    total_vert_force = sum(all_vert_forces)
    total_mag = round((((total_hor_force**2) + (total_vert_force**2))**0.5),1)
    total_angle = round((degrees((atan2(total_vert_force, total_hor_force)))),1)
    return total_mag, total_angle

def write_weird_file(filename, target_list, mode = "w", sort_first = False, reverse_first = False): ## Write to File
    
    
    Output_file = open(filename, mode)
    if sort_first:
        target_list.sort()
    if reverse_first:
        target_list.reverse()
    
    for item in target_list:
        
        print(item, file = Output_file)
    Output_file.close()

def multiply_file_by_index(outputFile, inputFile): ## Read then Write to File
    read_file = open(inputFile, "r")
    input_list = read_file.readlines()
    input_list = [line.strip() for line in input_list]
    input_list = [int(line) for line in input_list]
    read_file.close()
    count = 1
    mult_list = []
    for i in input_list:
        mult = i * count
        mult_list.append(mult)
        count += 1
    write_file = open(outputFile, "w")
    for i in mult_list:
        print (i, file = write_file)
    write_file.close()
    
def name_fixer(output_file, input_file): ## Name Fixer (first,second,last) from File
    read_file = open(input_file, "r")
    names = read_file.readlines()
    names = [line.strip() for line in names]
    fixed_list = []

    for name in names:
        if "," in name:
            wholeName = name.split()
            fixedName = wholeName[1] + " " + wholeName[2] + " " + wholeName[0]
            fixedName = fixedName.replace(",", "")
            fixed_list.append(fixedName)
        else:
            fixed_list.append(name)
    read_file.close()
    
    write_file = open(output_file, "w")
    for name in fixed_list:
        print(name, file = write_file)
    write_file.close()

def name_refixer(output_file, input_file): ## Name Fixer (last,first,second) from File
    read_file = open(input_file, "r")
    names = read_file.readlines()
    names = [line.strip() for line in names]
    fixed_list = []

    for name in names:
        if "," in name:
            fixed_list.append(name)
            
        else:
            wholeName = name.split()
            fixedName = wholeName[2] + ", " + wholeName[0] + " " + wholeName[1]
            fixed_list.append(fixedName)
            
    read_file.close()
    
    write_file = open(output_file, "w")
    for name in fixed_list:
        print(name, file = write_file)
    write_file.close()
    
def format_checker(filename): ## File Format Checker for new File Type
    checkfile = open(filename, "r")
    allLines = checkfile.readlines()
    allLines = [lines.strip("\n") for lines in allLines]
    checkfile.close()
    sumFifth = 0
    try:
        for lines in allLines:
            elements = lines.split()
            if len(elements) != 5:  #Checks if every line has 5 elements
                return False
            intCheck = int(elements[0]) + int(elements[2]) + int(elements[3]) # Checks if integers or not
            sumFifth += float(elements[4]) 
            if float(elements[4]) >= 1: #Checks if fifth element is a decimal number
                return False
        if sumFifth != 1:   #Checks if all 5th elements sum to 1.0
            return False
    except:
        return False
    answer = True
    return answer

def reader(filename): ## Returning List of Tuples
    checkfile = open(filename, "r")
    allLines = checkfile.readlines()
    allLines = [lines.strip("\n") for lines in allLines]
    checkfile.close()
    listoftups = []
    
    for lines in allLines:
        elements = lines.split()
        line1, line2, line3, line4, line5 = elements
        tup = (int(line1), line2, int(line3), int(line4), float(line5))
        listoftups.append(tup)
    return listoftups

def write_1301(filename, tupleList): ## Write List of Tuples to File
    writeFile = open(filename, "w")
    for tup in tupleList:
        f1, f2, f3, f4, f5 = tup
        inLine = "{f1} {f2} {f3} {f4} {f5}".format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)
        print(inLine, file= writeFile)
        
