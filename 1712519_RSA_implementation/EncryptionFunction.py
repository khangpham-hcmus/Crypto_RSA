#Phần 1: mã hóa dữ liệu
# Input: (n,e,m) trong đó: e là số nguyên tố,m là thông điệp(số nguyên): 0<= m < n
#Output: ciphertext c=m^e mod n

from  powerMod_function import power_mod
def Encryption(n, e, m):
  return power_mod(m, e, n)
