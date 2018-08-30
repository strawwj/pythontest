import sys
def split_log(line):
    line_list = line.split(":")       
    return {'username':line_list[0],
            'homedir':line_list[5],
            'shell':line_list[6]}
def generate_report(con):
    for line in con:
        dict1 = split_log(line)
        yield dict1
        #print(line_list)
def main():
    try:
        with open(sys.argv[1]) as filepass:
            contents = filepass.readlines()
    except FileNotFoundError:
        print("the file {} is not found".format(sys.argv[1]))
    else:        
        log_report = generate_report(contents) 
        for i in log_report:
            print(i)   
if __name__ == '__main__':
    main()
