#Phần 2: Giải mã:
#Khôi phục thông điệp m với m=c^d mod n

from KeyGen_Generation import get_Inverse
from  powerMod_function import power_mod

#decryption for RSA with n,ciphertext and pesonal key
def Decryption(n, d, c):
  return power_mod(c, d, n)


#Kiến thức áp dụng: Nếu n lớn hớn 2,n là hợp số thì n chắc chắn có 1 ươc nguyên tố <căn bậc 2 n
# Khi đó đặt n1= n//2 =>tiếp tục áp dụng phân tích n1 thì ra các snt

#Hàm lấy số nguyên x lớn nhất sao cho x^2<=n
def isqrt(n):
  if n < 2:
    return n
  small_index = isqrt(n >> 2) << 1  # Lấy căn bặc 2 của số lớn theo bit nhị phân
  large_index = small_index + 1
  if large_index * large_index > n: # nếu bình phương lên lớn n thì trả về số đó trừ 1
    return small_index
  return large_index

#Hàm phân tích ra các thừa số nguyên tố
def Factor_Prime(n):
  if n<2:
    return 2
  i = isqrt(n)+1
  while i >= 2:
    if n % i == 0:
      return i, n // i
    i -= 1

#Hàm giải mã mà không có personal key
#Input là public key n,e, và bản mã ciphertext c đi cùng
#Output là message được ẩn trong bản mã
def Decryp_None_PersonalKey(n, e, c):
  p = None
  q = None
  p, q = Factor_Prime(n)
  phi_n = (p - 1) * (q - 1)
  d = get_Inverse(e, phi_n)
  return pow(c, d, n)

