import random
from powerMod_function import *
#==========================================================================================
#Xây dựng hàm kiểm tra nguyên số cho số nhỏ: <=32 bit
def prime_test_small_Int(n):
  # Nếu n<2 : false
  if n < 2:
    return False
  # N là số nguyên tố khi và chỉ khi duyệt từ 2 đến sqrt(n): không tìm thấy ước => true
  i = 2
  while i*i <= n:
    if n % i == 0:
      return False
    i += 1
  return True

#============================================================================================
#Xây dựng hàm kiểm tra nguyên tố cho số lớn: >32 bit
#Sử dụng thuật toán Miller (còn gọi là phép thử Miller)
def TestPrime_By_Miller_Rabin(n, b = None):
  # Gọi n là số được kiểm tra nguyên tố
  # Nếu n<2 : false
  if n < 2:
    return False
  # If n == 2 or n == 3 :True
  if n < 4:
    return True
  # If n chẵn và n >2: false
  if n  % 2 == 0:
    return False
  # If a == None thì chọn ngẫu nhiên  b = rand()
  if not b:
    b = random.randrange(2, n - 1) #Chọn ngẫu nhiên b trong khoảng từ 2 tới n-1
  # Thử bằng Miller
  r = 0
  m = n - 1
  #Tìm r và m sao cho n-1 = m*(2**r) , m là số lẻ,r là số nguyên >0
  while m % 2 == 0:
    r += 1
    m //= 2
  # Ta có:  n - 1 = m*(2^r)  với m là số lẻ
  x = power_mod(b, m, n)
  # x = b^m (mod n)
  # Nếu x=1 mod n hoặc x == -1 mod n =>> x^(2**r) ==  1 mod n =>Vượt qua kiểm thử
  #Sử dụng tính chất: nếu a=b modular n thì a-b=0 modular n
  if ((x - 1) % n == 0) or ((x + 1) % n == 0):  # x=1 mod n thì (x-1) chia hết cho n (tương tự x=-1)
    return True
  #Nếu kiểm tra tới đây thì x^2 !=1 modular n =>> n không là nguyên tố
  return False

#=====================================================================================
#Tìm phần tử khả nghịch d biết e.d = 1 (mod phi_n)
#Sử dụng thuật toán Euclid mở rộng ax+by=GCD(a,b)
#trong đó e nguyên tố cùng nhau với phi_n
#nên ta xét: ax+phi_n*y = GCD(a,phi_n) = 1        mod phi_n
#=>          ax=1 mod phi_n (do phi_n*y=0 mod phi_n)
#Suy ra x là phần tử khả nghịch của a mod phi_n (a=e)
#Hàm tìm phần tử khả nghịch bằng Extended Euclid

def get_Inverse(e, phi_n):
  #e và phi_n luôn nguyên tố cùng nhau vì đã được cài đặt trong hàm khác để e thỏa (e,phi_n)=1
  #ax+by=1

#   x1*y1 +x2*y2 = x3*y3
#=>  ex+phi_n*y = GCD(e,phi_n)
  x1 = e
  x2 = phi_n
  x3 = e % phi_n
  y1 = 1
  y2 = 0
  y3 = 1
  while x3 != 0: #Chia Euclid ~~ (dùng Bezout tìm cặp (x,y) trong ax+by=GCD(a,b))
    x1 = x2
    x2 = x3
    x3 = x1 % x2
    y1 = y2
    y2 = y3
    y3 = y1 - y2 * (x1 // x2)
  # Lúc này ta có: e * y2 = x2 (mod phi_n)
  # If y2 < 0 thì  y2 := y2 - y2 * phi_n (mod phi_n)
  #Vì thông thường thì ta sẽ lấy y2 là số dương nhở nhất
  if y2 < 0:
    y2= y2 * (1-phi_n)
    y2 = y2 % phi_n
    return y2
  return y2


  #======================================================================
#GCD(a,b):Hàm tìm ước chung lớn nhất
def GCD(a,b):
  if(a<b):
    c=a
    a=b
    b=c
  while(b!=0):
    r=a%b
    a=b
    b=r
  return a
#===========================================================================================
def get_ed(phi_n):
  while True:
    #sử dụng kiến thức : xét phương trình Ax=B mod m
    # Với A khác 0 thuộc vành Zm thì phương trình trên có nghiệm duy nhất

    e = random.randrange(2, phi_n) #Sinh ngẫu nhiên e trong Vành Zphi_n
    #Mục đích là sinh e thỏa (e,phi_n)=1
    while(GCD(e,phi_n)!=1): # nếu e nguyên tố cùng nhau với phi_n thì thoát vòng lặp
      e = random.randrange(2, phi_n)
    d = get_Inverse(e, phi_n) # tìm phần tử khả nghịch của e để ed=1 mod phi_n
    if d:
      return e, d

#===========================================================================================
def KeyGen(key_size, DEBUG=False):
  prime_size = key_size // 2

  # Sinh số nguyên tố p ngẫu nhiên
  p = None
  while True:
    #Phát sinh ngẫu nhiên p rồi kiểm tra tính nguyên tố
    p = random.randrange(2**(prime_size - 1), 2**prime_size)
    #Nếu số nhỏ thì không dùng Miller (<=32 bit)
    if prime_size <= 32:
      if prime_test_small_Int(p):
        break
    # Dùng phép thử Miller nếu là số lớn >32 bit
    else:
      if TestPrime_By_Miller_Rabin(p, 2) and  \
         TestPrime_By_Miller_Rabin(p, 3) and  \
         TestPrime_By_Miller_Rabin(p, 5) and  \
         TestPrime_By_Miller_Rabin(p, 7) and  \
         TestPrime_By_Miller_Rabin(p, 11) and \
         TestPrime_By_Miller_Rabin(p, 13) and \
         TestPrime_By_Miller_Rabin(p, 17) and \
         TestPrime_By_Miller_Rabin(p, 19) and \
         TestPrime_By_Miller_Rabin(p,23):
        break

  # Sinh số nguyên tố q ngẫu nhiên
  q = None
  while True:
    #Sinh số ngẫu nhiên q và kiểm tra tính nguyên tố
    q = random.randrange(2**(prime_size - 1), 2**prime_size)
    # Dùng phép thử Miller nếu là số lớn >32 bit
    if prime_size <= 32:
      if prime_test_small_Int(q):
        break
    else:
      if TestPrime_By_Miller_Rabin(q, 2) and  \
         TestPrime_By_Miller_Rabin(q, 3) and  \
         TestPrime_By_Miller_Rabin(q, 5) and  \
         TestPrime_By_Miller_Rabin(q, 7) and  \
         TestPrime_By_Miller_Rabin(q, 11) and \
         TestPrime_By_Miller_Rabin(q, 13) and \
         TestPrime_By_Miller_Rabin(q, 17) and \
         TestPrime_By_Miller_Rabin(q, 19) and\
         TestPrime_By_Miller_Rabin(q,23):
        break

  #Tính n
  n = p * q
  #Tính phi_n: đếm số nguyên tố cùng nhau với n và nhỏ hơn n
  phi_n = (p - 1) * (q - 1)
  #Sinh khóa công khai e (public key) và khóa cá nhân d (personal key)
  e, d = get_ed(phi_n)
  #Trả về kết quả
  if DEBUG:
    return n, e, d, p, q
  return n, e, d, None, None



