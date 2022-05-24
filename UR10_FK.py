import numpy as np

def DH(a_n, d_n, theta_n, alpha_n):
  H=np.array([[np.cos(theta_n), -np.sin(theta_n)*np.cos(alpha_n), np.sin(theta_n)*np.sin(alpha_n), a_n*np.cos(theta_n)], [np.sin(theta_n), np.cos(theta_n)*np.cos(alpha_n), -np.cos(theta_n)*np.sin(alpha_n), a_n*np.sin(theta_n)], [0, np.sin(alpha_n), np.cos(alpha_n), d_n], [0, 0, 0, 1]])
  return H
H1 = DH(0,0.089,np.pi/2,np.pi/2)
H2 = DH(-0.425,0,0,0)
H3 = DH(-0.392,0,0,0)
H4 = DH(0,0.109,np.pi/2,np.pi/2)
H5 = DH(0,0.094,-np.pi/2,-np.pi/2)
H6 = DH(0,0.082,0,0)
V = np.dot(np.dot(H1,H2),H3)
N = np.dot(np.dot(V,H4),H5)
H = np.dot(N,H6)
print(H)
