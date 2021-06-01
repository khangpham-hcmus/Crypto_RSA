from tool_test_autoRSA import testTool
from RSA_Crypto_Method import *
import RSA_Text_FILE
from Parse_File_To_List import *
import time
from RSA_Text_FILE import *
#==============================================================

if __name__ == '__main__':

    filename = "data.txt"
    # Thực hiện quá trình mã hóa file
    start_encrypt = time.time()  # Bắt đầu do thời gian
    # Phân tích file thành từng dòng
    Lines_List = parse_file(filename)
    # Sinh n,e,d
    n, e, d, p, q = KeyGen(1024)
    line_simple = ""
    CipherText_from_File = []
    for line_simple in Lines_List:
        c=Encypt_Line_Simple_RSA(line_simple,n,e)
        CipherText_from_File.append(c)
    end_encrypt = time.time()  # Bắt đầu dừng

    #Thực hiện quá trình giải mã file
    start_decrypt=time.time()#Bắt đầu đo thời gian giải mã
    Plaintext_Is_Decrypted=[]#Mỗi phần tử là 1 dòng sau khi giải mã
    for c in CipherText_from_File:
        message_is_decrypted=Decrypt_Line_Simple_RSA(n,d,c)#Giải mã từng dòng
        Plaintext_Is_Decrypted.append(message_is_decrypted)
    end_decrypt=time.time()#Dừng thời gian giải mã

    #Print ra màn hình
    print("The message original:\n",Lines_List)

    if(Lines_List==Plaintext_Is_Decrypted):
        print("The message original is the same the message decrypted.\n")
    else:
        print("\nThey are different.\n")
    print("The time to encrept: ",end_encrypt-start_encrypt)
    print("The time to decrypt: ",end_decrypt-start_decrypt)
    output=open("output.txt","w",encoding='utf-8')
    for i in Plaintext_Is_Decrypted:
        output.write(i)










