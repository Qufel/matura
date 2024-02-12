import math
import time

f = open("liczby.txt", "r+")

DANE = []
for num in f.readlines():
    DANE.append(int(num.strip()))

f.close()

def first(nums):
    
    res = []
    
    for num in nums:
        num_str = str(num)
        if num_str[0] == num_str[-1]:
           res.append(num)
           
    return "{} {}".format(len(res), res[0])

print(first(DANE))

def second(nums):
    
    res = []
    
    for num in nums:
        
        copy_n = num
        divs = []
        
        k = 2
        while copy_n != 1:
            while copy_n % k == 0:
                copy_n /= k
                divs.append(k)
            k += 1
        
        res.append([num, divs])
    
    divisors_count = []
    divisiors_unique = []
    
    for r in res:
        divs = r[1]
        divisors_count.append(len(divs))
        
        c = 1
        m = divs[0]
        for d in divs:
            if d != m:
                c += 1
                m = d
                
        divisiors_unique.append(c)
    
    divisors_max_id = divisors_count.index(max(divisors_count))
    divisiors_unique_max_id = divisiors_unique.index(max(divisiors_unique))
    
    return "{} {} {} {}".format(nums[divisors_max_id], divisors_count[divisors_max_id], nums[divisiors_unique_max_id], divisiors_unique[divisiors_unique_max_id])
    
print(second(DANE))    

def thirds(nums):

    res = []
    
    for x in nums:
        for y in nums:
            for z in nums:
                if(z % y == 0 and y % x == 0):
                    if (x != y and x != z and y != z):
                        res.append("{} {} {}\n".format(x, y, z))
                    
    return res

t = thirds(DANE)

f_t = open("trojki.txt", "w+")

f_t.writelines(t)

f_t.close()

def fives(nums):
    
    res = []
    
    for u in nums:
        for w in nums:
            if(u != w and w % u == 0):
                for x in nums:
                    if(u != x and w != x and x % w == 0):
                        for y in nums:
                            if(u != y and w != y and x != y and y % x == 0):
                                for z in nums:
                                    if(u != z and w != z and x != z and y != z and z % y == 0):
                                        res.append("{} {} {} {} {}\n".format(u, w, x, y, z))
    
    return len(res)

print(fives(DANE))

print("Czas:", time.process_time())