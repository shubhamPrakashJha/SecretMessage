import os
def rename_file():
    #take all file name in directory
    file_list = os.listdir(r"C:\Users\Shubham Prakash\Desktop\udacity\prank")
    #print(file_list)

    #rename all those file name
    os.chdir(r"C:\Users\Shubham Prakash\Desktop\udacity\prank")
    for file_name in file_list:
        print("old name = "+file_name)
        print("new name = "+ file_name.strip('0123456789'))
        print("=========================================")
        os.rename(file_name,file_name.strip('0123456789'))
rename_file()