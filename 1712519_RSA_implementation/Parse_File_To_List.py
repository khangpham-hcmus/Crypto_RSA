# Reading a data.txt file
def parse_file(name_file):#tách file thành từng dòng rồi lưu về list
    file = open(name_file, 'r', encoding='utf8')
    list_line=[]
    if (file == None):
        return list_line
    list_line = file.readlines()
    return list_line    # trả về 1 list gồm những dòng của file được phân tích

