#Inverse Kinematic
import numpy as np 
x = 4
y = 2
# Calculate the angle of the second joint
theta_2 = np.arctan2(y,x)
print(theta_2)
# The 3x3 rotation matrix of frame 6 relative to frame 0
rot_mat_0_6 = np.array([[-1, 0, 0],
                        [0, -1, 0],
                        [0, 0, 1]])
# The 3x3 rotation matrix of frame 3 relative to frame 0
rot_mat_0_3 = np.array([[-np.sin(theta_2), 0, np.cos(theta_2)],
                        [np.cos(theta_2), 0, np.sin(theta_2)],
                        [0, 1, 0]])
# Calculate the inverse rotation matrix
inv_rot_mat_0_3 = np.linalg.inv(rot_mat_0_3)
 
# Calculate the 3x3 rotation matrix of frame 6 relative to frame 3
rot_mat_3_6 = (inv_rot_mat_0_3).dot(rot_mat_0_6)
print(rot_mat_3_6)
# Calculate the value for theta_5
theta_5 = np.arccos(rot_mat_3_6[2, 2])
print(theta_5)
 
# Calculate the value for theta_6
# -sin(theta_5)cos(theta_6) = rot_mat_3_6[2,0]
# Solving for theta_6...
# rot_mat_3_6[2,0]/-sin(theta_5) = cos(theta_6)
# arccosine(rot_mat_3_6[2,0]/-sin(theta_5)) = theta_6
theta_6 = np.arccos(rot_mat_3_6[2, 0] / -np.sin(theta_5))
print(theta_6)

# Calculate the value for theta_4 using one of the other
# cells in rot_mat_3_6. We'll use the second row, third column.
# cos(theta_4)sin(theta_5) = rot_mat_3_6[1,2]
# cos(theta_4) = rot_mat_3_6[1,2] / sin(theta_5)
# theta_4 = arccosine(rot_mat_3_6[1,2] / sin(theta_5))
theta_4 = np.arccos(rot_mat_3_6[1,2] / np.sin(theta_5))
print(theta_4)


r11 = -np.sin(theta_4) * np.cos(theta_5) * np.cos(theta_6) - np.cos(theta_4) * np.sin(theta_6)
r12 = np.sin(theta_4) * np.cos(theta_5) * np.sin(theta_6) - np.cos(theta_4) * np.cos(theta_6)
r13 = -np.sin(theta_4) * np.sin(theta_5)
r21 = np.cos(theta_4) * np.cos(theta_5) * np.cos(theta_6) - np.sin(theta_4) * np.sin(theta_6)
r22 = -np.cos(theta_4) * np.cos(theta_5) * np.sin(theta_6) - np.sin(theta_4) * np.cos(theta_6)
r23 = np.cos(theta_4) * np.sin(theta_5)
r31 = -np.sin(theta_5) * np.cos(theta_6)
r32 = np.sin(theta_5) * np.sin(theta_6)
r33 = np.cos(theta_5)
 
rot_mat_3_6 = np.array([[r11, r12, r13],
                        [r21, r22, r23],
                        [r31, r32, r33]])

print(rot_mat_3_6)
 

