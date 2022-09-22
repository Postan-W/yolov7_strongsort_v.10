import cv2
import numpy as np

def draw_area(image,area):
    '''
    :param image: numpy.ndarray a picture loaded by cv2
    :param area: list. like [[[275,753],[847,1019],[1509,281],[1203,153],[275,753]]]
    :return:
    '''
    area = np.array(area, np.int32)
    thickness = round(0.002 * (image.shape[0] + image.shape[1]) / 2) + 1
    cv2.polylines(image, area, isClosed=True, color=(0, 255, 0), thickness=thickness, lineType=cv2.LINE_AA)

def in_area_or_not(bbox,area):
    '''
    :param bbox: list. like [x1,y1,x2,y2]即框的左上右下角坐标whwh
    :param area: list. like [[[275,753],[847,1019],[1509,281],[1203,153],[275,753]]]
    :return: True or False
    '''
    object_x1 = int(bbox[0])
    object_y1 = int(bbox[1])
    object_x2 = int(bbox[2])
    object_y2 = int(bbox[3])
    object_w = object_x2 - object_x1
    object_h = object_y2 - object_y1
    object_cx = object_x1 + (object_w / 2)#中心点w
    object_cy = object_y1 + (object_h / 2)#中心点h
    """
        判断点是否在多边形内部的 pnpoly 算法，从一个目标点引出一条射线(任意一条射线)，统计这条射线与对变形的交点个数。如果有奇数个交点，则说明目标点在多边形内，
        若为偶数(0也算)个交点，则在外。
        本代码实现的算法是目标点向右引出的一条射线。
        :param pt: 点坐标 [x,y]
        :param poly: 点多边形坐标 [[[x1,y1],[x2,y2],...],[[x1,y1],[x2,y2],...]...]
        :return: 点是否在多边形之内
        """
    # 注意，这里是多个多边形区域
    res_list = []
    for poly in area:
        nvert = len(poly)
        vertx = []
        verty = []
        testx = object_cx
        testy = object_cy
        for item in poly:
            vertx.append(item[0])
            verty.append(item[1])
        j = nvert - 1  # 下面的for语句，第一次循环1选择最后一个点作为比较点
        res = False
        for i in range(nvert):  # 遍历n-1个点
            # 第一次for循环使用最后一个点
            if (verty[j] - verty[i]) == 0:
                j = i
                continue
            # 通过画图可以很容易明白，下面公式即得到从(testx,testy)向右引出的水平射线和两点连线的交点的x坐标值
            x = (vertx[j] - vertx[i]) * (testy - verty[i]) / (verty[j] - verty[i]) + vertx[i]
            if ((verty[i] > testy) != (verty[j] > testy)) and (testx < x):
                res = not res  # 奇数次为True，偶数次为False
            j = i  # 下次循环时形成下一条边
        res_list.append(res)
    return True in res_list  # 有一个区域中包含该点即可

def calc_time(interval,fps):
    pass