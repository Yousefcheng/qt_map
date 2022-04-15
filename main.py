from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
from folium import CustomIcon
import folium
import time

# from PyQt5.QtWebChannel import QWebChannel

'''
class Map_Display:
    # 初始化地图
    def __init__(self, center_locattion=[34.2634, 109.0432]) -> None:

        # 谷歌地图 https://mt.google.com/vt/lyrs=h&x={x}&y={y}&z={z}
        # 调用高德地图http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}
        self.map = folium.Map(
            
            location=center_locattion,   # 例：location=[34.2634, 109.0432],
            zoom_start=16,
            control_scale=True,
            
            tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',  # 高德地图
            attr='default'
        )
        # 显示鼠标点击点经纬度
        self.map.add_child(folium.LatLngPopup())

        self.map.add_child(folium.ClickForMarker(
            popup='Waypoint'
            )
        )  # 将鼠标点击点添加到地图上

    # 生成线
    def make_line(self, locations=[[34.2634, 109.0432], [36.2688, 109.0432], [37.2699, 109.0432], [38.2777, 109.0432]]):

        line = folium.PolyLine(
            # 例：locations=[[34.2634, 109.0432], [36.2688, 109.0432], [37.2699, 109.0432], [38.2777, 109.0432]],
            locations=locations,
            color='blue'
        )
        line.add_to(self.map)

    # 标记点图标更改+坐标标记
    def makeIcon(self, icon_image_url="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F00%2F94%2F03%2F2956f2b5da690d2.jpg%21rw400&refer=http%3A%2F%2Fbpic.588ku.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1638535529&t=46e106bf37a49b24a4acc772bd5951ba", 
                        shadow_image_url="https://profile.csdnimg.cn/9/7/A/3_zhangphil", 
                        location=[34.2634, 109.0432]):
        url = '{}'.format
        # icon_image = url("https://img-blog.csdnimg.cn/20190511223909598.png")   # 图标图片
        # shadow_image = url("https://profile.csdnimg.cn/9/7/A/3_zhangphil")   #  图标的影子图片
        icon_image = url(icon_image_url)
        shadow_image = url(shadow_image_url)

        # 图标样式
        icon = CustomIcon(
            icon_image,
            icon_size=(38, 95),
            icon_anchor=(22, 94),
            shadow_image=shadow_image,
            shadow_size=(50, 64),
            shadow_anchor=(4, 62),
            popup_anchor=(-3, -76),
        )

        marker = folium.Marker(
            # location=[34.2634, 109.0432],
            location=location,
            icon=icon,
            # tooltip 是悬浮弹出的描述
            popup="zhang\nphil"              # popup 是marker的名字
        )

        marker.add_to(self.map)
    # 标记点辐射范围

    def makeCircle(self, location=[34.2634, 109.0432]):
        # 随着地图变化而变化
        circle = folium.Circle(

            # location=[34.2634, 109.0432],
            location=location,
            radius=50,
            popup='Laurelhurst Park',  # marker的名字
            color='#3186cc',
            fill=False,
            fill_color='#3186cc'
        )
        circle.add_to(self.map)

        # 固定不动的一个圆
        circle_marker = folium.CircleMarker(

            # location=[34.2634, 109.0432],
            location=location,
            radius=1,
            popup='popup',
            color='#DC143C',      # 圈的颜色
            fill=True,
            fill_color='#6495E'  # 填充颜色
        )
        circle_marker.add_to(self.map)

    # 保存html
    def saveHtml(self):
        self.map.save("save_map.html")
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('地图显示')
        self.resize(1000, 640)
        # 新建一个QWebEngineView()对象
        self.qwebengine = QWebEngineView(self)
        # 设置网页在窗口中显示的位置和大小
        self.qwebengine.setGeometry(20, 20, 960, 600)

        #传值
        # channel = QWebChannel()
        # channel.registerObject("obj", factorial)
        # 将channel传递给html中的JS
        # self.browser.page().setWebChannel(channel)
        # 在QWebEngineView中加载网址
        path = "./map.html"
        path = os.path.abspath(path)
        path = path.replace('\\', '/')

        # 加载地图
        self.qwebengine.load(QUrl(path))


if __name__ == '__main__':
    # map=Map_Display()
    # map.make_line()
    # map.makeCircle()
    # map.makeIcon()
    # map.saveHtml()
    app = QApplication(sys.argv)
    win = MainWindow()
    # while():
        # map.makeIcon(icon_image_url="https://profile.csdnimg.cn/9/7/A/3_zhangphil")
    win.show()


    sys.exit(app.exec_())
    map.makeIcon(icon_image_url="https://profile.csdnimg.cn/9/7/A/3_zhangphil")
    
    map.saveHtml()
    win = MainWindow()

    # time.sleep(5)
    
    
    # map.saveHtml()
