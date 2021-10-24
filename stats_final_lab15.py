# -*- coding: utf-8 -*-
"""stats_final_lab15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13JIW7sGR5vda_YRN79ZkVfbIZKEfFgRt

**อย่าลืม Save a copy in drive ก่อนนะคะ**

จงเขียนโปรแกรมเพื่อหาค่าที่โจทย์ต้องการและแสดงผลลัพธ์ออกทางหน้าจอ

1. 	นักจิตวิทยาสนใจที่จะทราบความแปรผันของเวลาที่ผู้ขับรถยนต์มีต่อสิ่งเร้าที่เห็น จึงสุ่มตัวอย่างผู้ขับรถยนต์ เพื่อทดลองจำนวน 16 คน ดังนี้ 0.6,0.14,0.08,0.14,0.034,0.045,0.112,0.205,0.008,0.36,0.05,0.12,0.28,0.114,0.36,0.056 หน่วยเป็นวินาที
 

  1.1 จงหาค่าความแปรปรวนของเวลาที่ผู้ขับรถยนต์มีต่อสิ่งเร้าที่เห็น 

  1.2 
  จงหาค่าส่วนเบี่ยงเบนมาตรฐานของเวลาที่ผู้ขับรถยนต์มีต่อสิ่งเร้าที่เห็น 
  

  1.3 จงหาช่วงความเชื่อมั่น 95% ของเวลาที่ผู้ขับรถยนต์มีต่อสิ่งเร้าที่เห็น

  1.4 นักจิตวิทยายืนยันว่าเวลาที่คนขับมีปฏิกิริยาต่อสิ่งเร้าสม่ำเสมอมีค่าความแปรปรวนน้อยกว่า 0.85 วินาที$^2$ จงทดสอบว่าคำยืนยันของนักจิตวิทยาเกี่ยวกับค่าความแปรปรวน เชื่อถือได้หรือไม่ ที่ระดับนัยสำคัญ 0.1  

  1.5 นักจิตวิทยานี้เชื่อว่าเวลาที่คนขับมีปฏิกิริยาต่อสิ่งเร้าสม่ำเสมอเท่ากับ 0.16 วินาที จงทดสอบว่าความเชื่อของนักจิตวิทยาเป็นจริงหรือไม่ ที่ระดับนัยสำคัญ 0.05



2. นักลงทุนเชื่อว่าหุ้นของบริษัท A มีความเสี่ยงมากกว่าหุ้นของบริษัท B ความเสี่ยงนี้วัด
จากราคาหุ้นที่ผันแปรไปในแต่ละวัน จึงมีการทดสอบความเชื่อข้างต้นโดยสุ่มราคาหุ้นบริษัท A มา
21 วัน ดังนี้ 43.25, 44.50, 40.75, 42.00, 42.50, 41.25, 53.00, 52.50, 51.75, 50.00, 48.75, 49.00, 46.25, 48.00, 47.25, 47.50, 46.00, 46.00, 47.25, 45.75, 42.50
และราคาหุ้นบริษัท B มา 24 วัน ดังนี้  0.83, 0.82, 0.81, 0.78, 0.75, 0.74, 0.76, 0.81, 0.87, 0.96, 0.94, 1.04, 0.99, 0.97, 0.91, 0.95, 0.97, 1.00, 1.02, 1.18, 1.06, 1.04,0.99,0.96

2.1 จงประมาณอัตราส่วนความแปรปรวนของหุ้นบริษัท A และ หุ้นบริษัท B พร้อมทั้งอธิบายความหมาย

2.2 จงหาช่วงความเชื่อมั่น 90% ของอัตราส่วนความแปรปรวนของราคาหุ้นบริษัท A และ หุ้นบริษัท B พร้อมทั้งอธิบายความหมาย

2.3 จงทดสอบว่าราคาหุ้นของบริษัท
A มีความแปรปรวนเท่ากับราคาหุ้นของบริษัท B จริงหรือไม่ ที่ระดับนัยสำคัญ 0.1

2.4 จงทดสอบว่าหุ้นของบริษัท
A มีความเสี่ยงมากกว่าหุ้นของบริษัท B จริงหรือไม่ ที่ระดับนัยสำคัญ 0.05
"""

# 1.1จงหาค่าความแปรปรวนของเวลาที่ผู้ขับรถยนต์มีต่อสิ่งเร้าที่เห็น
import numpy as np
data = np.array([0.6,0.14,0.08,0.14,0.034,0.045,0.112,0.205,0.008,0.36,0.05,0.12,0.28,0.114,0.36,0.056])
s = np.var(data)
print(round(s,7))

#1.2 จงหาค่าส่วนเบี่ยงเบนมาตรฐานของเวลาที่ผู้ขับรถยนต์มีต่อสิ่งเร้าที่เห็น

s1 = np.std(data)
print(round(s1,7))

#1.3 จงหาช่วงความเชื่อมั่น 95% ของเวลาที่ผู้ขับรถยนต์มีต่อสิ่งเร้าที่เห็น
from scipy.stats import chi2
alpha = 0.05
n = len(data)
df = n-1
s2 = np.var(data,ddof=1)
x_l = chi2.ppf(1-alpha/2,df)
x_u = chi2.ppf(alpha/2,df)

lower = np.sqrt(((n-1)*s2)/x_l)
upper = np.sqrt(((n-1)*s2)/x_u)
print('L = ',lower)
print('U = ',upper)

#1.4 นักจิตวิทยายืนยันว่าเวลาที่คนขับมีปฏิกิริยาต่อสิ่งเร้าสม่ำเสมอมีค่าความแปรปรวนน้อยกว่า 0.85 วินาที 2  จงทดสอบว่าคำยืนยันของนักจิตวิทยาเกี่ยวกับค่าความแปรปรวน เชื่อถือได้หรือไม่ ที่ระดับนัยสำคัญ 0.1
''' H0 <= 0.85
    H1 >  0.85 '''

from scipy.stats import chi2
import numpy as np

def var_test(x,var0,alternative,alpha):
  n = len(x)
  stat = (n-1) * np.var(x,ddof=1) / var0
  print('stats = %.7f'%(stat))

  if alternative == "smaller":
    critical_value = chi2.ppf(alpha,n-1)
    print('critical value = %.7f'%(critical_value))
    if stat <= critical_value:
      return " H_0 reject"
    else:
      return "H_1 accept"
  elif alternative == "larger":
    critical_value = chi2.ppf(1-alpha,n-1)
    print('critical value = %.7f' %(critical_value))
    if stat <= critical_value:
      return " H_0 reject"
    else:
      return "H_1 accept"
  else:
    critical_value1 = chi2.ppf(alpha / 2, n - 1)
    critical_value2 = chi2.ppf(1 - (alpha / 2), n - 1)
    print('critical value1 = %.7f, critical value2 = %.7f'%(critical_value1,critical_value2))
    if stat <= critical_value1 or stat >= critical_value2:
      return "H_0 rejected"
    else:
      return "H_0 accepted"

data = np.array([0.6,0.14,0.08,0.14,0.034,0.045,0.112,0.205,0.008,0.36,0.05,0.12,0.28,0.114,0.36,0.056])
alpha_ = 0.1
null_hypothesis = 0.85
var_test(data,var0=null_hypothesis,alternative="smaller",alpha=alpha_)

#1.5 นักจิตวิทยานี้เชื่อว่าเวลาที่คนขับมีปฏิกิริยาต่อสิ่งเร้าสม่ำเสมอเท่ากับ 0.16 วินาที จงทดสอบว่าความเชื่อของนักจิตวิทยาเป็นจริงหรือไม่ ที่ระดับนัยสำคัญ 0.05
null_hypothesis = 0.16**2
alpha_=0.05
var_test(data,var0=null_hypothesis,alternative="two-sided",alpha=alpha_)

#2.1 จงประมาณอัตราส่วนความแปรปรวนของหุ้นบริษัท A และ หุ้นบริษัท B พร้อมทั้งอธิบายความหมาย ex 6 
from scipy.stats import f
import numpy as np
data1 = np.array([43.25, 44.50, 40.75, 42.00, 42.50, 
                  41.25, 53.00, 52.50, 51.75, 50.00, 48.75, 49.00, 46.25, 48.00, 47.25, 47.50, 46.00, 46.00, 47.25, 45.75, 42.50])
data2 = np.array([0.83, 0.82, 0.81, 0.78, 0.75, 0.74, 0.76, 0.81, 0.87, 0.96, 0.94, 
                  1.04, 0.99, 0.97, 0.91, 0.95, 0.97, 1.00, 1.02, 1.18, 1.06, 1.04,0.99,0.96])

alpha = 0.05
n1 = len(data1)
n2 = len(data2)
df1 = n1-1
df2 = n2-1
s1 = np.var(data1)
s1 = np.var(data1,ddof=1)
s2 = np.var(data2,ddof=1)
print('Var Before = ',s1)
print('Var after = ',s2)
print('R of Var = ',s1/s2)

#2.2 จงหาช่วงความเชื่อมั่น 90% ของอัตราส่วนความแปรปรวนของราคาหุ้นบริษัท A และ หุ้นบริษัท B พร้อมทั้งอธิบายความหมาย ex7
from scipy.stats import f
import numpy as np
data1 = np.array([43.25, 44.50, 40.75, 42.00, 42.50, 
                  41.25, 53.00, 52.50, 51.75, 50.00, 48.75, 49.00, 46.25, 48.00, 47.25, 47.50, 46.00, 46.00, 47.25, 45.75, 42.50])
data2 = np.array([0.83, 0.82, 0.81, 0.78, 0.75, 0.74, 0.76, 0.81, 0.87, 0.96, 0.94, 
                  1.04, 0.99, 0.97, 0.91, 0.95, 0.97, 1.00, 1.02, 1.18, 1.06, 1.04,0.99,0.96])

alpha = 0.1
n = len(data1)
df1 = n-1
m = len(data2)
df2 = m-1

s1_2 = np.var(data1,ddof=1)
s2_2 = np.var(data2,ddof=1)
f_l = f.ppf(1-alpha/2,df1,df2)
f_u = f.ppf(alpha/2,df1,df2)
lower = (s1_2/s2_2)/f_l
upper = (s1_2/s2_2)/f_u
print('L =',lower)
print('U =',upper)

#2.3 จงทดสอบว่าราคาหุ้นของบริษัท A มีความแปรปรวนเท่ากับราคาหุ้นของบริษัท B จริงหรือไม่ ที่ระดับนัยสำคัญ 0.1 ex 9

def var_ratio_test(x1,x2, var0, alternative, alpha):
  n = len(x1)
  m = len(x2)
  stat = (np.var(x1,ddof=1)/np.var(x2,ddof=1))/var0
  print('stat = %.7f' %(stat))
  if alternative == "smaller":
    critical_value = f.ppf(alpha, n - 1,m - 1)
    print('critical value = %.7f' %(critical_value))
    if stat <= critical_value:
      return "H_0 rejected"
    else:
      return "H_0 accepted"
  elif alternative == "larger":
    critical_value = f.ppf(1 - alpha, n - 1,m - 1)
    print('critical value = %.7f' %(critical_value))
    if stat >= critical_value:
      return "H_0 rejected"
    else:
      return "H_0 accepted"
  else:
    critical_value1 = f.ppf(alpha / 2, n - 1,m - 1)
    critical_value2 = f.ppf(1 - (alpha / 2), n - 1,m - 1)
    print('critical value1 = %.7f, critical value2 = %.7f'%(critical_value1,critical_value2))
    if stat <= critical_value1 or stat >= critical_value2:
      return "H_0 rejected"
    else:
      return "H_0 accepted"

null_hypothesis = 1
significance = 0.1
var_ratio_test(data1,data2, var0 = null_hypothesis,alternative = "two-sided",alpha = significance)

#2.4จงทดสอบว่าหุ้นของบริษัท A มีความเสี่ยงมากกว่าหุ้นของบริษัท B จริงหรือไม่ ที่ระดับนัยสำคัญ 0.05
data1 = np.array([43.25, 44.50, 40.75, 42.00, 42.50, 
                  41.25, 53.00, 52.50, 51.75, 50.00, 48.75, 49.00, 46.25, 48.00, 47.25, 47.50, 46.00, 46.00, 47.25, 45.75, 42.50])
data2 = np.array([0.83, 0.82, 0.81, 0.78, 0.75, 0.74, 0.76, 0.81, 0.87, 0.96, 0.94, 
                  1.04, 0.99, 0.97, 0.91, 0.95, 0.97, 1.00, 1.02, 1.18, 1.06, 1.04,0.99,0.96])
null_hypothesis = 1
alpha_ = 0.05
var_ratio_test(data1,data2, var0 = null_hypothesis,alternative = "larger",alpha = alpha_)