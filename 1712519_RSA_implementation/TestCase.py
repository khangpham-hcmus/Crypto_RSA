import random
from KeyGen_Generation import  KeyGen
from EncryptionFunction import Encryption
from DecryptionFunction import Decryption
from  powerMod_function import power_mod


def testTool(number_of_bits_integer,i):


    n, e, d, p, q = KeyGen(number_of_bits_integer, DEBUG=True)
    m = random.randrange(2**(number_of_bits_integer // 2 - 1))

    c = Encryption(n, e, m)

    m_ = Decryption(n, d, c)
    print('Test #%d:' % i)

    if m == m_:#original message is the same the message decrypted
      print("Decryption is successful:")

      print('  p = ' ,p)
      print('  q = %d' % q)
      print('  n = %d' % n)
      print('  puclic key: e = %d' % e)
      print('  personal key: d = %d' % d)
      print('  message original = %d' % m)
      print('  message decrypted = %d' %m_)
      print('  c = %d' % c)
    else:
        print("Decryption is failed.\n")

