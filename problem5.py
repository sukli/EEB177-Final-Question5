#! /usr/bin/python

def read_csv_file_to_dic(filename):
    f = open(filename, "r")
    lines = f.read().splitlines()
    dic = {}
    for line in lines:
        split = line.split(",")
        dic[split[0]] = split[1]
    return dic 

def main():
    dic = read_csv_file_to_dic("richness_fishbase_family.csv")

if __name__ == '__main__':
    main()