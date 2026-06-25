# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_codigo = QLabel(self.centralwidget)
        self.lbl_codigo.setObjectName(u"lbl_codigo")
        self.lbl_codigo.setGeometry(QRect(20, 10, 71, 31))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(14)
        self.lbl_codigo.setFont(font)
        self.lbl_codigo.setTabletTracking(True)
        self.lbl_servicio_nombre = QLabel(self.centralwidget)
        self.lbl_servicio_nombre.setObjectName(u"lbl_servicio_nombre")
        self.lbl_servicio_nombre.setGeometry(QRect(320, 0, 191, 41))
        self.lbl_servicio_nombre.setFont(font)
        self.lbl_costo_base = QLabel(self.centralwidget)
        self.lbl_costo_base.setObjectName(u"lbl_costo_base")
        self.lbl_costo_base.setGeometry(QRect(320, 50, 121, 31))
        self.lbl_costo_base.setFont(font)
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(20, 110, 91, 31))
        self.lbl_nombre.setFont(font)
        self.txt_codigo = QLineEdit(self.centralwidget)
        self.txt_codigo.setObjectName(u"txt_codigo")
        self.txt_codigo.setGeometry(QRect(90, 10, 161, 31))
        font1 = QFont()
        font1.setFamilies([u"Palatino Linotype"])
        font1.setPointSize(12)
        self.txt_codigo.setFont(font1)
        self.txt_codigo.setMaxLength(5)
        self.txt_servicio_nombre = QLineEdit(self.centralwidget)
        self.txt_servicio_nombre.setObjectName(u"txt_servicio_nombre")
        self.txt_servicio_nombre.setGeometry(QRect(500, 10, 281, 31))
        self.txt_servicio_nombre.setFont(font1)
        self.txt_servicio_nombre.setMaxLength(30)
        self.txt_costo_base = QLineEdit(self.centralwidget)
        self.txt_costo_base.setObjectName(u"txt_costo_base")
        self.txt_costo_base.setGeometry(QRect(500, 50, 121, 31))
        self.txt_costo_base.setFont(font1)
        self.txt_costo_base.setMaxLength(4)
        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(100, 110, 341, 31))
        self.txt_nombre.setFont(font1)
        self.txt_nombre.setMaxLength(60)
        self.btn_registrar = QPushButton(self.centralwidget)
        self.btn_registrar.setObjectName(u"btn_registrar")
        self.btn_registrar.setGeometry(QRect(60, 270, 101, 61))
        self.btn_registrar.setFont(font)
        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(620, 270, 91, 61))
        self.btn_limpiar.setFont(font)
        self.btn_mostrar_informacion = QPushButton(self.centralwidget)
        self.btn_mostrar_informacion.setObjectName(u"btn_mostrar_informacion")
        self.btn_mostrar_informacion.setGeometry(QRect(290, 270, 201, 61))
        self.btn_mostrar_informacion.setFont(font)
        self.lbl_mostrar_datos = QLabel(self.centralwidget)
        self.lbl_mostrar_datos.setObjectName(u"lbl_mostrar_datos")
        self.lbl_mostrar_datos.setGeometry(QRect(20, 440, 121, 41))
        self.lbl_mostrar_datos.setFont(font)
        self.txt_resultado = QTextEdit(self.centralwidget)
        self.txt_resultado.setObjectName(u"txt_resultado")
        self.txt_resultado.setGeometry(QRect(160, 360, 461, 191))
        self.txt_resultado.setFont(font1)
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(20, 150, 81, 31))
        self.lbl_apellido.setFont(font)
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(20, 200, 71, 21))
        self.lbl_email.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 71, 21))
        self.label.setFont(font)
        self.txt_cedula_2 = QLineEdit(self.centralwidget)
        self.txt_cedula_2.setObjectName(u"txt_cedula_2")
        self.txt_cedula_2.setGeometry(QRect(90, 50, 171, 31))
        self.txt_cedula_2.setFont(font1)
        self.txt_apellido_2 = QLineEdit(self.centralwidget)
        self.txt_apellido_2.setObjectName(u"txt_apellido_2")
        self.txt_apellido_2.setGeometry(QRect(100, 150, 341, 31))
        self.txt_apellido_2.setFont(font1)
        self.txt_email_2 = QLineEdit(self.centralwidget)
        self.txt_email_2.setObjectName(u"txt_email_2")
        self.txt_email_2.setGeometry(QRect(80, 200, 361, 31))
        self.txt_email_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 812, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.lbl_servicio_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre del servicio:", None))
        self.lbl_costo_base.setText(QCoreApplication.translate("MainWindow", u"Costo base:", None))
        self.lbl_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.btn_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btn_mostrar_informacion.setText(QCoreApplication.translate("MainWindow", u"Mostrar informaci\u00f3n", None))
        self.lbl_mostrar_datos.setText(QCoreApplication.translate("MainWindow", u"Mostrar datos", None))
        self.lbl_apellido.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.lbl_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"C\u00e9dula:", None))
    # retranslateUi

