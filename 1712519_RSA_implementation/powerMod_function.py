#Input x,y,p với x^y mod p
#Output là kết quả của x^y mod p
#Ý tưởng:x^y mod n = (x^(y/2))^2 nếu y chẵn
#           x^y mod n = x* (x^(y-1)) = x* ((x^2)^(y-1))

def power_mod(x, y, p):
    # Tạo biến kết quả
    result_mod = 1;
    # Nếu x>=p thì x <-- x mod p
    x = x % p
    while (y > 0):

        # nếu y  lẻ
        if (y & 1):
            result_mod = (result_mod * x) % p;# Lúc này : y <-- y-1

        # Tại đây y chẵn =>> dịch bit sang phải 1 lần (tức là chia nguyên cho 2)
        y = y >> 1;  # y = y//2
        x = (x * x) % p;
    return result_mod

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
