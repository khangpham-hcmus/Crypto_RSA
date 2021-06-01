import random
from KeyGen_Generation import*
from EncryptionFunction import Encryption
from DecryptionFunction import Decryption
from  powerMod_function import power_mod
from tool_test_autoRSA import testTool


#Kiểm tra bằng tay
def RSA_method(number_of_bits_integer):

    n, e, d, p, q = KeyGen(number_of_bits_integer, DEBUG=True)
    message_original=int(input("Input the message originally (integer):"))
    c = Encryption(n, e, message_original)
    print("The original message:",message_original)
    print("\nPuclic key:");
    print("n=",n)
    print("e=",e)
    print("\nCiphertext after encrypted: ",c);

    print("\nPersonal Key:")
    print("n=",n)
    print("d=",d);

    print("\nDecryption process is beginning:")
    cipher_key=int(input("Input the ciphertext:"))
    print("Input personal key:")
    n_=int(input("n="))
    d_=int(input("d="))
    message_is_decrypted=Decryption(n_,d_,cipher_key)
    print("\nThe message after decypted is: ",message_is_decrypted)
    if(message_is_decrypted==message_original):
        print("Decryption is succeeded.\n")
    else:
        print("Decryption is failed.\n")

