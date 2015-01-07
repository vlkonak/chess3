__author__ = 'Vladimir Konak'

from math import sin, cos, radians

from PyQt4.QtCore import QPointF, QRect, Qt, SIGNAL
from PyQt4.QtGui import QColor, QAbstractButton,\
                QApplication,QPolygonF, QPainter

black = QColor(0,0,0)
white = QColor(255,255,255)

class Square(QAbstractButton):
    def __init__(self):
        self.figure = None
        self.isSelected = False
        self.color = QColor()
        self.isHighlighted = False
        self.highlightColor = QColor(0,255,0)

    def createButton(self, central_widget):
        super(Square, self).__init__(central_widget)

    def setGeometry(self, rect):
        super(Square, self).setGeometry(rect)

    def enterEvent(self, *args, **kwargs):
        if not self.isEmpty() or self.isHighlighted:
            QApplication.setOverrideCursor(Qt.PointingHandCursor)

    def leaveEvent(self, *args, **kwargs):
        if not self.isEmpty() or self.isHighlighted:
            QApplication.restoreOverrideCursor()

    def paintEvent(self, e):
        pass


    def setup(self, a, b, c):
        #a  = (0..2)
        #b  = (0..3)
        #c  = (0..7)
        d_alpha = 30./4
        square_size = r = 50
        db = 5 - b
        dc = c - 4
        k = 1.16
        self.coords = [
                    QPointF(dc*r,r*(db-(2-abs(dc))*sin(radians(b*d_alpha)))*k),
                    QPointF((dc+1)*r,r*(db-(2-abs(dc+1))*sin(radians(b*d_alpha)))*k),
                    QPointF((dc+1)*r,r*(db-1-(2-abs(dc+1))*sin(radians(b*d_alpha+d_alpha)))*k),
                    QPointF(dc*r,r*(db-1-(2-abs(dc))*sin(radians(b*d_alpha+d_alpha)))*k)
                         ]
        if (b+c)%2: self.color = black
        else: self.color = white

        def rotate(self,theta):
            theta = radians(theta)
            for point in self.coords :
                x = point.x()
                y = point.y()
                point.setX(x*cos(theta) - y*sin(theta))
                point.setY(y*cos(theta) + x*sin(theta))

        def translate(self, dx, dy):
            for point in self.coords :
                point.setX(point.x()+dx)
                point.setY(point.y()+dy)

        rotate(self,a*120.)
        translate(self, 400,400)
        button_geometry = QPolygonF(self.coords).boundingRect()
        self.setGeometry(button_geometry.toRect())
        self.show()


    def isEmpty(self):
        if self.figure == None : return True
        else: return False

    #def __repr__(self):
        #return str(self.color.red())