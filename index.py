import numpy as np
import math

T1 = 3180e-6
T2 = 318e-6
T3 = 75e-6
T4 = 7959e-6

overral_db_gain_bias = 20

def get_attenuation(f, iec=True):
  p1 = np.log10( 1 + (1/(4*np.square(np.pi)*np.square(f)*np.square(T2))))
  p2 = np.log10( 1 + (1/(4*np.square(np.pi)*np.square(f)*np.square(T1))))
  p3 = np.log10( 1 + (1/(4*np.square(np.pi)*np.square(f)*np.square(T4))))
  p4 = np.log10( 1 + (4*np.square(np.pi)*np.square(f)*np.square(T3)))
  if iec:
    raw_frequency = (p1-p2-p3-p4)*-10
  else:
    raw_frequency = (p1-p2-p4)*-10
  return round(raw_frequency-overral_db_gain_bias,2)

frequencies = [1,2,3,5,11,12,13,15,16,19,20,22,25,28,31.5,35,40,44,50,55,63,70,80,89,100,110,125,140,1,19,20,24,25,31,3,38,40,43,48,50,54,61,63,68,76,80,85,95,100,11,12,12,13,15,16,1,19,2,21,24,25,27,30,31,34,38,40,43,48,50,5,61,63,68,760,800,85,950,1000,1100,1200,1250,1300,1500,1600,1700,1900,2000,21000]

result = "GraphicEQ: "
for frequency in frequencies:
  result = result + str(frequency)+" "+str(get_attenuation(frequency, False))+"; "

result = result[:len(result)-2]
print(result)
