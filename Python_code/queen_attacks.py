#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#
def isDataExists(check,Data):
    for i in range(len(Data)):
        if(Data[i][0] == check[0] and Data[i][1] == check[1]):
            return True
    return False

def queensAttack(n, k, r_q, c_q, obstacles):
    # Initialize counts for each direction
    up = n - r_q
    down = r_q - 1
    right = n - c_q
    left = c_q - 1
    up_right = min(up, right)
    up_left = min(up, left)
    down_right = min(down, right)
    down_left = min(down, left)

    # Check obstacles and update counts
    for obstacle in obstacles:
        r, c = obstacle
        if r == r_q:
            if c > c_q:
                right = min(right, c - c_q - 1)
            else:
                left = min(left, c_q - c - 1)
        elif c == c_q:
            if r > r_q:
                up = min(up, r - r_q - 1)
            else:
                down = min(down, r_q - r - 1)
        elif abs(r - r_q) == abs(c - c_q):
            if r > r_q:
                if c > c_q:
                    up_right = min(up_right, r - r_q - 1)
                else:
                    up_left = min(up_left, r - r_q - 1)
            else:
                if c > c_q:
                    down_right = min(down_right, r_q - r - 1)
                else:
                    down_left = min(down_left, r_q - r - 1)

    # Return the sum of counts in all directions
    return up + down + right + left + up_right + up_left + down_right + down_left

def queensAttackx(n, k, r_q, c_q, obstacles):
    ret = 0
    hor_obs_down = 0
    hor_obs_up = n+1
    ver_obs_down = 0
    ver_obs_up = n+1
    for i in range(len(obstacles)):
        if(obstacles[i][0]==r_q):
            if(obstacles[i][1]<r_q):
                hor_obs_down = obstacles[i][1]
            if(obstacles[i][1]>r_q):
                hor_obs_up = obstacles[i][1]
        if(obstacles[i][1]==c_q):
            if(obstacles[i][0]<c_q):
                ver_obs_down = obstacles[i][0]
            if(obstacles[i][0]>c_q):
                ver_obs_up = obstacles[i][0]
    queen_path = []
    # print(hor_obs_down,hor_obs_up)
    # print(ver_obs_down,ver_obs_up)
    limit_down_diag_left = False
    limit_up_diag_left = False
    limit_down_diag_right = False
    limit_up_diag_right = False
    for i in range(1,n+1):
        #horizontal
        if(i != c_q ):
            if(i > ver_obs_down and i < ver_obs_up):
                # ret = ret + 1
                queen_path.append(str(r_q) + " " + str(i))
        #vertikal
        if(i != r_q):
            if(i > hor_obs_down and i < hor_obs_up):
                # ret = ret + 1
                queen_path.append(str(i) + " " + str(c_q))
        
        #diagonal kiri
        if(r_q-i >= 1 and c_q-i >= 1):
            if(not limit_down_diag_left):
                # ret = ret + 1
                queen_path.append(str(r_q-i) + " " + str(c_q-i))
                if(isDataExists([r_q-i,c_q-i],obstacles)):
                    limit_down_diag_left = True
            
        if(r_q+i <= n and c_q+i <=n):
            if(not limit_up_diag_left):
                # ret = ret + 1
                queen_path.append(str(r_q+i) + " " + str(c_q+i))
                if(isDataExists([r_q-i,c_q-i],obstacles)):
                    limit_up_diag_left = True
            
        #diagonal kanan
        if(r_q+i <= n and c_q-i >= 1):
            if(not limit_down_diag_right):
                # ret = ret + 1
                queen_path.append(str(r_q+i) + " " + str(c_q-i))
                if(isDataExists([r_q+i,c_q-i],obstacles)):
                    limit_down_diag_right = True
        if(r_q-i >= 1 and c_q+i <= n):
            if(not limit_up_diag_right):
                # ret = ret + 1
                queen_path.append(str(r_q-i) + " " + str(c_q+i))
                if(isDataExists([r_q-i,c_q+i],obstacles)):
                    limit_up_diag_right = True
        
        
    # queen_path.sort()
    # print(queen_path)
    # print(queen_path)
    for i in range(len(obstacles)):
        check = str(obstacles[i][0])+" "+str(obstacles[i][1])
        # print(type(check))
        try:
            queen_path.remove(check)
        except:
            pass
    # print(queen_path)
    return len(queen_path)
    # return ret
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
