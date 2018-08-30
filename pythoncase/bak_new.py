import os
import sys

def bak_file(path_s, path_d):
    file_list = os.listdir(path_s)
    for file_name in file_list:
        file_s_path = os.path.join(path_s, file_name)    
        file_d_path = os.path.join(path_d, file_name)    
        if os.path.isdir(file_s_path):
            if not os.path.isdir(file_d_path):
                create_dir = "mkdir -p %s" % (file_d_path)
                if os.system(create_dir) == 0:
                    print create_dir
                else:
                    print "mkdir %s failure" % (file_d_path)
                    os._exit(0)
            bak_file(file_s_path, file_d_path)
        else:
            if os.path.isfile(file_d_path):
                file_s_stat = os.stat(file_s_path)
                file_d_stat = os.stat(file_d_path)
                if file_s_stat.st_mtime <= file_d_stat.st_mtime:
                    continue
            cp_com = "cp %s %s" % (file_s_path, file_d_path)
#��Ҫ�ж�path_s��path_d �Ƿ�ΪĿ¼#

            if os.system(cp_com) == 0 :
                print cp_com
            else:
                print "cp file failure"
                os._exit(0)
if __name__ == "__main__":
    path_s = raw_input("please input the source directory path:")
    path_d = raw_input("please input the destination directory path:")
    bak_file(path_s, path_d)
