import time
Q = R = 0.5
P_0 = 2.65
C = 2
M = C**3
A = 1
G = 1
start_time = time.time()
for i in range(100):
    P_1 = A*P_0*A + Q
    R_1 = C*P_1*C + R
    P_2 = (1-G*M*C)*P_1 + G*M*R*M*G
    S = -G*M*R
    R_2 = (1-C*G*M)**2 * R_1
    K = (P_2*C+S)/R_2
    P_0 = P_2 - K*(P_2*C+S)
print('K la: {}\nP_0 la: {}'.format(K, P_0))
print('Calculated time: {}s'.format(time.time()-start_time))
