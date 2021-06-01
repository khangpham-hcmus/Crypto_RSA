import random
from KeyGen_Generation import*
from EncryptionFunction import Encryption
from DecryptionFunction import Decryption
from  powerMod_function import power_mod
from tool_test_autoRSA import testTool

#Encrypt the line simple
def Encypt_Line_Simple_RSA(message_original,n,e):
    #Convert the message to list of number :
    num_list=[]
    for i in message_original:
        num_list.append(ord(i))
    #Tìm kích thước danh sách số vừa sinh ra
    len_of_num_list=len(num_list)
    # Create a ciphertext_list to storage the ciphertext in interger style

    ciphertext_list=[]
    j=0
    while(j<len_of_num_list):
        c = Encryption(n, e,num_list[j])
        ciphertext_list.append(c)
        j=j+1
    return ciphertext_list

#Decrypt the text
def Decrypt_Line_Simple_RSA(n,d,ciphertext_list):
    plaintext_list=[]
    len_of_ciphertext_list=len(ciphertext_list)
    i=0
    while(i<len_of_ciphertext_list):
        message_is_decrypted=Decryption(n,d,ciphertext_list[i])
        plaintext_list.append(message_is_decrypted)
        i += 1
    result=""
    len_of_plaintext_list=len(plaintext_list)
    j=0
    while(j<len_of_plaintext_list):
        temp=chr(plaintext_list[j])
        result=result+temp
        j=j+1
    return result






