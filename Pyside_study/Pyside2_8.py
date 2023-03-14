def drawRenderingAPI(self,device):
        painter = QPainter(device)
        painter.setRenderHint(QPainter.Antialiasing,True)

        painter.setPen(QPen(Qt.black,2,Qt.SolidLine,Qt.RoundCap))
        painter.setBrush(QBrush(Qt.darkGreen,Qt.SolidPattern))
        painter.setFont(QFont("Arial",12))

        rect = QRect(10,20,180,120)
        rectText = QRect(0,140,200,40)
        rects = [QRect(10,20,100,80),QRect(80,60,100,80)]
        points = [QPoint(20,120),QPoint(40,20),QPoint(140,60),QPoint(180,120)]

        path = QPainterPath()
        path.moveTo(40,120)
        path.lineTo(40,60)
        path.cubicTo(180,0,100,100,180,120)

        startAngle = 90*16
        arcLength = 120*16

        # point
        painter.translate(10,10)
        painter.drawPoint(rect.center())
        painter.drawText(rectText,Qt.AlignCenter,"drawPoint()")

        # points
        painter.translate(200,0)
        painter.drawPoints(points)
        painter.drawText(rectText,Qt.AlignCenter,"drawPoints()")

        # line
        painter.translate(200,0)
        painter.drawLine(rect.topLeft(),rect.bottomRight())
        painter.drawText(rectText,Qt.AlignCenter,"drawLine()")

        # lines
        painter.translate(200,0)
        painter.drawLines(points)
        painter.drawText(rectText,Qt.AlignCenter,"drawLines()")

        # rectangle
        painter.translate(200, 0)
        painter.drawRect(rect)
        painter.drawText(rectText, Qt.AlignCenter, "drawRect()")

        # rectangles
        painter.translate(200, 0)
        painter.drawRects(rects)
        painter.drawText(rectText, Qt.AlignCenter, "drawRects()")

        # rounded rect
        painter.translate(-1000,200)
        painter.drawRoundedRect(rect,25,25,Qt.RelativeSize)
        painter.drawText(rectText,Qt.AlignCenter,"drawRoundRect()")

        # ellipse
        painter.translate(200,0)
        painter.drawEllipse(rect)
        painter.drawText(rectText,Qt.AlignCenter,"drawEllipse()")

        # polyLine
        painter.translate(200,0)
        painter.drawPolyline(points)
        painter.drawText(rectText,Qt.AlignCenter,"drawPolyline()")

        # polygon
        painter.translate(200,0)
        painter.drawPolygon(points)
        painter.drawText(rectText,Qt.AlignCenter,"drawPolygon()")

        # convex polygon
        painter.translate(200,0)
        painter.drawConvexPolygon(points)
        painter.drawText(rectText,Qt.AlignCenter,"drawConvexPolygon()")

        # arc
        painter.translate(200,0)
        painter.drawArc(rect,startAngle,arcLength)
        painter.drawText(rectText,Qt.AlignCenter,"drawArc()")

        # chord
        painter.translate(-1000,200)
        painter.drawChord(rect,startAngle,arcLength)
        painter.drawText(rectText,Qt.AlignCenter,"drawChord()")

        # pie
        painter.translate(200,0)
        painter.drawPie(rect,startAngle,arcLength)
        painter.drawText(rectText,Qt.AlignCenter,"drawPie()")

        # path
        painter.translate(200,0)
        painter.drawPath(path)
        painter.drawText(rectText,Qt.AlignCenter,"drawPath()")

        # text
        painter.translate(200,0)
        painter.drawText(rect,Qt.AlignCenter,"Hello Qt")
        painter.drawText(rectText,Qt.AlignCenter,"drawText()")

        # pixmap
        painter.translate(200,0)
        painter.drawPixmap(40,40,self.pixmapLogo)
        painter.drawText(rectText,Qt.AlignCenter,"drawPixmap()")

        # fillRect
        linGradient = QLinearGradient(rect.bottomRight(),rect.topLeft())
        linGradient.setColorAt(0,Qt.darkGreen)
        linGradient.setColorAt(0.5,Qt.green)
        linGradient.setColorAt(1.0,Qt.white)
        brush = QBrush(linGradient)

        painter.translate(200,0)
        painter.fillRect(rect,brush)
        painter.drawText(rectText,Qt.AlignCenter,"fillRect()")