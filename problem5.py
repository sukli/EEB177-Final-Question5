#! /usr/bin/python

# read the csv file into a dictionary data structure
def read_csv_file_to_dic(filename):
    # open file and split into lines
    f = open(filename, "r")
    lines = f.read().splitlines()
    dic = {}
    # iterate over lines, skipping over the first ('family,count')
    for line in lines[1:]:
        # split by comma and insert as k,v pair
        split = line.split(",")
        dic[split[0]] = int(split[1])
    return dic

def print_families(dic, species_threshold):
    max_species_num = max(dic.values())
    # prints all families if there exists at least one family with more species than species_threshold
    if (species_threshold < max_species_num):
        for key in sorted(dic):
            print "Family %s contains %d species" % (key, dic[key])
    # prints if there does not exist at least one family with more species than species_threshold
    elif (species_threshold > max_species_num):
        print "No families have more than %d species" % species_threshold

# print families with 1 species
def print_families_1(dic):
    # iterate through the keys in sorted order
    for key in sorted(dic):
        # check if species number is 1
        if (dic[key] == 1):
            print key

def main():
    dic = read_csv_file_to_dic("richness_fishbase_family.csv")

if __name__ == '__main__':
    main()