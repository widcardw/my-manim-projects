import numpy as np
import math

'''
该模块持续更新中......

命名规则：
点A在上，点B左下，点C右下；(如果输入者不知道相对位置的话，以后再说)
a,b,c为对边长度；
点D在a上，点E在b上，点F在c上；（即三线与三边的交点）
'''

################工具区#########################

def translation(P, x_or_y):
    '''
    param P: 点的np坐标
    x_or_y: 1:取x坐标；2:取y坐标
    return: 返回np坐标的x或y
    '''
    if x_or_y == 1: #选取x坐标
        return P[0]
    elif x_or_y == 2:   #选取y坐标
        return P[1]
    else:           #否则啥也不返回
        return

def get_line_long(P1, P2):
    '''
    param P1: 第一个点np坐标
    param P2: 第二个点np坐标
    return: 返回两点之间的距离
    '''
    x1 = translation(P1, 1)
    y1 = translation(P1, 2)
    x2 = translation(P2, 1)
    y2 = translation(P2, 2)

    temp1 = (x2 - x1) * (x2 - x1)
    temp2 = (y2 - y1) * (y2 - y1)
    return np.sqrt(temp1 + temp2)

def get_line_middle_point(P1, P2):
    '''
    param P1: 第一个点np坐标
    param P2: 第二个点np坐标
    return: 返回两点之间的中点
    '''
    x1 = translation(P1, 1)
    y1 = translation(P1, 2)
    x2 = translation(P2, 1)
    y2 = translation(P2, 2)

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return np.array([x, y, 0])

def get_circumference(triangle):
    '''
    param triangle: MyTriangle对象
    return: 返回该三角形的周长
    '''
    return triangle.a + triangle.b + triangle.c

def get_area(triangle):
    '''
    param triangle: MyTriangle对象
    return: 返回该三角形的面积
    '''
    p = get_circumference(triangle) / 2
    return np.sqrt(p * (p - triangle.a) * (p - triangle.b) * (p - triangle.c))

def two_determinant(two_list):
    '''
    param two_list: 2*2数表（二维数组）
    return: 行列式
    '''
    a = two_list[0][0]
    b = two_list[0][1]
    c = two_list[1][0]
    d = two_list[1][1]
    return a * d - b * c

def three_determinant(three_list):
    '''
        param two_list: 3*3数表（二维数组）
        return: 行列式
    '''
    a = three_list[0][0]
    b = three_list[0][1]
    c = three_list[0][2]
    d = three_list[1][0]
    e = three_list[1][1]
    f = three_list[1][2]
    g = three_list[2][0]
    h = three_list[2][1]
    i = three_list[2][2]
    return a * two_determinant([[e,f],[h,i]]) - b * two_determinant([[d,f],[g,i]]) + c * two_determinant([[d,e],[g,h]])

def get_two_points_line(P1, P2):
    '''
    两点式化斜截式
    param P1: 第一个点的坐标P1(x1,y1)
    param P2: 第二个点的坐标P2(x2,y2)
    return: [k, b]
    '''
    x1,y1,x2,y2 = translation(P1, 1), translation(P1, 2), translation(P2, 1), translation(P2, 2)
    k = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * (y2 - y1) / (x2 - x1)
    return [k, b]

def two_lines_intersection(k1, b1, k2, b2):
    '''
    两条斜截式直线交点
    param k1: 第一条直线斜率
    param b1: 第一条直线截距
    param k2: 第二条直线斜率
    param b2: 第二条直线截距
    return: [x, y]交点np坐标
    '''
    x = -(b1 - b2)/(k1 - k2)
    y = (k2 * b1 - k1 * b2) / (k2 - k1)
    return np.array([x, y, 0])

class MyTriangle():

################战前信息########################

    def __init__(self, A, B, C):
        '''
        (基本属性)
        param A: A点np坐标
        param B: B点np坐标
        param C: C点np坐标
        '''

        self.A = A  #A的np坐标
        self.B = B  #B的np坐标
        self.C = C  #C的np坐标
        self.x1 = translation(A, 1)
        self.y1 = translation(A, 2)
        self.x2 = translation(B, 1)
        self.y2 = translation(B, 2)
        self.x3 = translation(C, 1)
        self.y3 = translation(C, 2)
        self.a = get_line_long(B, C)   #线段BC,即a的长度
        self.b = get_line_long(A, C)   #线段AC,即b的长度
        self.c = get_line_long(A, B)   #线段AB,即c的长度

################四线交三边战区######################

    #高线
    def get_drop_feet(self):
        points = []
        A, B, C, O = self.A, self.B, self.C, self.get_orthocenter()
        points.append(two_lines_intersection(*get_two_points_line(A, O), *get_two_points_line(B, C)))
        points.append(two_lines_intersection(*get_two_points_line(B, O), *get_two_points_line(C, A)))
        points.append(two_lines_intersection(*get_two_points_line(C, O), *get_two_points_line(A, B)))
        return points

    #中线
    def get_middle_points(self):
        points = []
        A, B, C, O = self.A, self.B, self.C, self.get_centroid()
        points.append(two_lines_intersection(*get_two_points_line(A, O), *get_two_points_line(B, C)))
        points.append(two_lines_intersection(*get_two_points_line(B, O), *get_two_points_line(C, A)))
        points.append(two_lines_intersection(*get_two_points_line(C, O), *get_two_points_line(A, B)))
        return points

    #角平分线
    def get_angle_bisector_intersection(self):
        points = []
        A, B, C, O = self.A, self.B, self.C, self.get_incenter()
        points.append(two_lines_intersection(*get_two_points_line(A, O), *get_two_points_line(B, C)))
        points.append(two_lines_intersection(*get_two_points_line(B, O), *get_two_points_line(C, A)))
        points.append(two_lines_intersection(*get_two_points_line(C, O), *get_two_points_line(A, B)))
        return points

    #垂直平分线
    def get_vertical_bisector_intersection(self):
        points = []
        A, B, C = self.A, self.B, self.C
        points.append(get_line_middle_point(B, C))
        points.append(get_line_middle_point(C, A))
        points.append(get_line_middle_point(A, B))
        return points

#################五心战区##########################

    #垂心
    def get_orthocenter(self):
        #链接：https://zh.wikipedia.org/wiki/%E9%AB%98%E7%BA%BF
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3

        X1_list = [
            [x2 * x3 + y2 * y3, 1, y1],
            [x3 * x1 + y3 * y1, 1, y2],
            [x1 * x2 + y1 * y2, 1, y3]
        ]
        X2_list = [
            [x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1]
        ]
        Y1_list = [
            [x2 * x3 + y2 * y3, x1, 1],
            [x3 * x1 + y3 * y1, x2, 1],
            [x1 * x2 + y1 * y2, x3, 1]
        ]
        Y2_list = [
            [x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1]
        ]
        X1 = three_determinant(X1_list)
        X2 = three_determinant(X2_list)
        Y1 = three_determinant(Y1_list)
        Y2 = three_determinant(Y2_list)
        x = X1 / X2
        y = Y1 / Y2
        return np.array([x, y, 0])

    #重心
    def get_centroid(self):
        #链接：https://zh.wikipedia.org/wiki/%E5%87%A0%E4%BD%95%E4%B8%AD%E5%BF%83
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3

        x = (x1 + x2 + x3) / 3
        y = (y1 + y2 + y3) / 3
        return np.array([x, y, 0])

    #外心
    def get_circumcenter(self):
        #链接：https://zh.wikipedia.org/wiki/%E5%A4%96%E6%8E%A5%E5%9C%93
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3

        X1_list = [
            [x1 * x1 + y1 * y1, y1, 1],
            [x2 * x2 + y2 * y2, y2, 1],
            [x3 * x3 + y3 * y3, y3, 1]
        ]
        X2_list = [
            [x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1]
        ]
        Y1_list = [
            [x1, x1 * x1 + y1 * y1, 1],
            [x2, x2 * x2 + y2 * y2, 1],
            [x3, x3 * x3 + y3 * y3, 1]
        ]
        Y2_list = [
            [x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1]
        ]
        X1 = three_determinant(X1_list)
        X2 = 2 * three_determinant(X2_list)
        Y1 = three_determinant(Y1_list)
        Y2 = 2 * three_determinant(Y2_list)
        x = X1 / X2
        y = Y1 / Y2
        return np.array([x, y, 0])

    #内心
    def get_incenter(self):
        #链接：https://zh.wikipedia.org/wiki/%E5%86%85%E5%88%87%E5%9C%86
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3
        a, b, c = self.a, self.b, self.c

        x = (a * x1 + b * x2 + c * x3) / (a + b + c)
        y = (a * y1 + b * y2 + c * y3) / (a + b + c)
        return np.array([x, y, 0])

    #旁心(三个)
    def get_excenter(self):
        #链接：https://zh.wikipedia.org/wiki/%E6%97%81%E5%88%87%E5%9C%93
        x1, x2, x3, y1, y2, y3 = self.x1, self.x2, self.x3, self.y1, self.y2, self.y3
        a, b, c = self.a, self.b, self.c

        Ja_x = (-a * x1 + b * x2 + c * x3) / (-a + b + c)
        Ja_y = (-a * y1 + b * y2 + c * y3) / (-a + b + c)
        Jb_x = (a * x1 - b * x2 + c * x3) / (a - b + c)
        Jb_y = (a * y1 - b * y2 + c * y3) / (a - b + c)
        Jc_x = (a * x1 + b * x2 - c * x3) / (a + b - c)
        Jc_y = (a * y1 + b * y2 - c * y3) / (a + b - c)

        return [np.array([Ja_x, Ja_y, 0]), np.array([Jb_x, Jb_y, 0]), np.array([Jc_x, Jc_y, 0])]

##################示例区#################################
if __name__ == "__main__":
    A = np.array([-1, 3, 0])
    B = np.array([-4, -2, 0])
    C = np.array([4, -2, 0])
    triangle = MyTriangle(A, B, C)