# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget

import iconosBlancos_rc
import _icons_rc
import imagenesGeneral_rc
import iconosNegros_rc
import imagenesGeneral_rc

class Ui_ventanaPrincipal(object):
    def setupUi(self, ventanaPrincipal):
        if not ventanaPrincipal.objectName():
            ventanaPrincipal.setObjectName(u"ventanaPrincipal")
        ventanaPrincipal.resize(1161, 828)
        ventanaPrincipal.setStyleSheet(u"*{\n"
"	border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"	padding: 0;\n"
"	margin:  0;\n"
"	color: #000000;\n"
"}\n"
"\n"
"#centralContenedor{\n"
"	background-color: #e0dcd5;\n"
"}\n"
"\n"
"#subMenuContenedorIzquierdo{\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"#subMenuContenedorIzquierdo, QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px, 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"#menuSubCentroContenedor,#subMenuDerecho{\n"
"	background-color: #d3cec3;\n"
"}\n"
"\n"
"#frame_5, #frame_9, #emergenteNotificacionSubContenedor, #emergente2{\n"
"	background-color: #ffffff;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#cabeceraContenedor, #pieContenedor{\n"
"	background-color: #d3cec3\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: #ffffff;\n"
"	padding: 5px 10px;\n"
"	margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#actualizarBoton{\n"
"	background-color: #f00;\n"
"	padding: 10px, 10px;\n"
"	border-radius: 10px;\n"
""
                        "}\n"
"\n"
"#editarBoton, #eliminarBoton{\n"
"	background-color: #f00;\n"
"	padding: 10px, 10px;\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.centralContenedor = QWidget(ventanaPrincipal)
        self.centralContenedor.setObjectName(u"centralContenedor")
        self.horizontalLayout = QHBoxLayout(self.centralContenedor)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuContenedorIzquierdo = QCustomSlideMenu(self.centralContenedor)
        self.menuContenedorIzquierdo.setObjectName(u"menuContenedorIzquierdo")
        self.menuContenedorIzquierdo.setMaximumSize(QSize(42, 16777215))
        self.verticalLayout = QVBoxLayout(self.menuContenedorIzquierdo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.subMenuContenedorIzquierdo = QWidget(self.menuContenedorIzquierdo)
        self.subMenuContenedorIzquierdo.setObjectName(u"subMenuContenedorIzquierdo")
        self.verticalLayout_2 = QVBoxLayout(self.subMenuContenedorIzquierdo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.subMenuContenedorIzquierdo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 8, 0, 0)
        self.menuBoton = QPushButton(self.frame)
        self.menuBoton.setObjectName(u"menuBoton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBoton.sizePolicy().hasHeightForWidth())
        self.menuBoton.setSizePolicy(sizePolicy)
        self.menuBoton.setMinimumSize(QSize(0, 0))
        self.menuBoton.setContextMenuPolicy(Qt.NoContextMenu)
        self.menuBoton.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/blackIcons/Black/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBoton.setIcon(icon)
        self.menuBoton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.menuBoton)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.subMenuContenedorIzquierdo)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 10, 0, 10)
        self.inicioBoton = QPushButton(self.frame_2)
        self.inicioBoton.setObjectName(u"inicioBoton")
        sizePolicy.setHeightForWidth(self.inicioBoton.sizePolicy().hasHeightForWidth())
        self.inicioBoton.setSizePolicy(sizePolicy)
        self.inicioBoton.setLayoutDirection(Qt.LeftToRight)
        self.inicioBoton.setAutoFillBackground(False)
        self.inicioBoton.setStyleSheet(u"background-color: #e0dcd5;")
        icon1 = QIcon()
        icon1.addFile(u":/blackIcons/Black/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inicioBoton.setIcon(icon1)
        self.inicioBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.inicioBoton)

        self.estudianteBoton = QPushButton(self.frame_2)
        self.estudianteBoton.setObjectName(u"estudianteBoton")
        icon2 = QIcon()
        icon2.addFile(u":/blackIcons/Black/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.estudianteBoton.setIcon(icon2)
        self.estudianteBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.estudianteBoton)

        self.materiaBoton = QPushButton(self.frame_2)
        self.materiaBoton.setObjectName(u"materiaBoton")
        icon3 = QIcon()
        icon3.addFile(u":/blackIcons/Black/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.materiaBoton.setIcon(icon3)
        self.materiaBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.materiaBoton)

        self.profesorBoton = QPushButton(self.frame_2)
        self.profesorBoton.setObjectName(u"profesorBoton")
        icon4 = QIcon()
        icon4.addFile(u":/blackIcons/Black/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profesorBoton.setIcon(icon4)
        self.profesorBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.profesorBoton)

        self.notaBoton = QPushButton(self.frame_2)
        self.notaBoton.setObjectName(u"notaBoton")
        icon5 = QIcon()
        icon5.addFile(u":/blackIcons/Black/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notaBoton.setIcon(icon5)
        self.notaBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.notaBoton)

        self.documentoBoton = QPushButton(self.frame_2)
        self.documentoBoton.setObjectName(u"documentoBoton")
        icon6 = QIcon()
        icon6.addFile(u":/blackIcons/Black/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.documentoBoton.setIcon(icon6)
        self.documentoBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.documentoBoton)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.subMenuContenedorIzquierdo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 10, 0, 10)
        self.gradosBoton = QPushButton(self.frame_3)
        self.gradosBoton.setObjectName(u"gradosBoton")
        icon7 = QIcon()
        icon7.addFile(u":/blackIcons/Black/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gradosBoton.setIcon(icon7)
        self.gradosBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.gradosBoton)

        self.ajustesBoton = QPushButton(self.frame_3)
        self.ajustesBoton.setObjectName(u"ajustesBoton")
        icon8 = QIcon()
        icon8.addFile(u":/blackIcons/Black/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ajustesBoton.setIcon(icon8)
        self.ajustesBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.ajustesBoton)

        self.acercaDeBoton = QPushButton(self.frame_3)
        self.acercaDeBoton.setObjectName(u"acercaDeBoton")
        icon9 = QIcon()
        icon9.addFile(u":/blackIcons/Black/alert-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.acercaDeBoton.setIcon(icon9)
        self.acercaDeBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.acercaDeBoton)

        self.ayudaBoton = QPushButton(self.frame_3)
        self.ayudaBoton.setObjectName(u"ayudaBoton")
        icon10 = QIcon()
        icon10.addFile(u":/blackIcons/Black/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ayudaBoton.setIcon(icon10)
        self.ayudaBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.ayudaBoton)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.subMenuContenedorIzquierdo)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 10, 0, 10)
        self.cerrarSesionBoton = QPushButton(self.frame_4)
        self.cerrarSesionBoton.setObjectName(u"cerrarSesionBoton")
        icon11 = QIcon()
        icon11.addFile(u":/blackIcons/Black/lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarSesionBoton.setIcon(icon11)
        self.cerrarSesionBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.cerrarSesionBoton)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.subMenuContenedorIzquierdo)


        self.horizontalLayout.addWidget(self.menuContenedorIzquierdo, 0, Qt.AlignLeft)

        self.menuCentroContenedor = QCustomSlideMenu(self.centralContenedor)
        self.menuCentroContenedor.setObjectName(u"menuCentroContenedor")
        self.verticalLayout_7 = QVBoxLayout(self.menuCentroContenedor)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.menuSubCentroContenedor = QWidget(self.menuCentroContenedor)
        self.menuSubCentroContenedor.setObjectName(u"menuSubCentroContenedor")
        self.menuSubCentroContenedor.setMinimumSize(QSize(280, 0))
        self.verticalLayout_8 = QVBoxLayout(self.menuSubCentroContenedor)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 0)
        self.frame_5 = QFrame(self.menuSubCentroContenedor)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.cerrarMenuCentro = QPushButton(self.frame_5)
        self.cerrarMenuCentro.setObjectName(u"cerrarMenuCentro")
        icon12 = QIcon()
        icon12.addFile(u":/blackIcons/Black/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarMenuCentro.setIcon(icon12)
        self.cerrarMenuCentro.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.cerrarMenuCentro, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.centroPaginas = QCustomQStackedWidget(self.menuSubCentroContenedor)
        self.centroPaginas.setObjectName(u"centroPaginas")
        self.ajustePagina = QWidget()
        self.ajustePagina.setObjectName(u"ajustePagina")
        self.verticalLayout_9 = QVBoxLayout(self.ajustePagina)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.ajustePagina)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)

        self.centroPaginas.addWidget(self.ajustePagina)
        self.acercaDePagina = QWidget()
        self.acercaDePagina.setObjectName(u"acercaDePagina")
        self.verticalLayout_10 = QVBoxLayout(self.acercaDePagina)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.acercaDePagina)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.centroPaginas.addWidget(self.acercaDePagina)
        self.ayudaPagina = QWidget()
        self.ayudaPagina.setObjectName(u"ayudaPagina")
        self.verticalLayout_11 = QVBoxLayout(self.ayudaPagina)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.ayudaPagina)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_4)

        self.centroPaginas.addWidget(self.ayudaPagina)

        self.verticalLayout_8.addWidget(self.centroPaginas)


        self.verticalLayout_7.addWidget(self.menuSubCentroContenedor, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.menuCentroContenedor)

        self.principalCuerpoContenedor = QWidget(self.centralContenedor)
        self.principalCuerpoContenedor.setObjectName(u"principalCuerpoContenedor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.principalCuerpoContenedor.sizePolicy().hasHeightForWidth())
        self.principalCuerpoContenedor.setSizePolicy(sizePolicy2)
        self.principalCuerpoContenedor.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.principalCuerpoContenedor)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.cabeceraContenedor = QWidget(self.principalCuerpoContenedor)
        self.cabeceraContenedor.setObjectName(u"cabeceraContenedor")
        self.horizontalLayout_4 = QHBoxLayout(self.cabeceraContenedor)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_6 = QFrame(self.cabeceraContenedor)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setPixmap(QPixmap(u":/imagenes/Imagenes/Logo/2.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.cabeceraContenedor)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.notificacionBoton = QPushButton(self.frame_7)
        self.notificacionBoton.setObjectName(u"notificacionBoton")
        icon13 = QIcon()
        icon13.addFile(u":/font_awesome_regular/icons/font_awesome/regular/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notificacionBoton.setIcon(icon13)
        self.notificacionBoton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.notificacionBoton)

        self.masBoton = QPushButton(self.frame_7)
        self.masBoton.setObjectName(u"masBoton")
        icon14 = QIcon()
        icon14.addFile(u":/blackIcons/Black/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.masBoton.setIcon(icon14)
        self.masBoton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.masBoton)

        self.perfilBoton = QPushButton(self.frame_7)
        self.perfilBoton.setObjectName(u"perfilBoton")
        icon15 = QIcon()
        icon15.addFile(u":/font_awesome_regular/icons/font_awesome/regular/circle-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfilBoton.setIcon(icon15)
        self.perfilBoton.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.perfilBoton)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_14 = QFrame(self.cabeceraContenedor)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.botonMenuEliminar = QPushButton(self.frame_14)
        self.botonMenuEliminar.setObjectName(u"botonMenuEliminar")
        icon16 = QIcon()
        icon16.addFile(u":/blackIcons/Black/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.botonMenuEliminar.setIcon(icon16)
        self.botonMenuEliminar.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.botonMenuEliminar, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_14)

        self.frame_8 = QFrame(self.cabeceraContenedor)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.minimizarBoton = QPushButton(self.frame_8)
        self.minimizarBoton.setObjectName(u"minimizarBoton")
        icon17 = QIcon()
        icon17.addFile(u":/blackIcons/Black/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizarBoton.setIcon(icon17)

        self.horizontalLayout_3.addWidget(self.minimizarBoton)

        self.restaurarBoton = QPushButton(self.frame_8)
        self.restaurarBoton.setObjectName(u"restaurarBoton")
        icon18 = QIcon()
        icon18.addFile(u":/blackIcons/Black/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restaurarBoton.setIcon(icon18)

        self.horizontalLayout_3.addWidget(self.restaurarBoton)

        self.cerrarBoton = QPushButton(self.frame_8)
        self.cerrarBoton.setObjectName(u"cerrarBoton")
        icon19 = QIcon()
        icon19.addFile(u":/blackIcons/Black/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarBoton.setIcon(icon19)

        self.horizontalLayout_3.addWidget(self.cerrarBoton)


        self.horizontalLayout_4.addWidget(self.frame_8, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.cabeceraContenedor)

        self.principalCuerpoContenido = QWidget(self.principalCuerpoContenedor)
        self.principalCuerpoContenido.setObjectName(u"principalCuerpoContenido")
        sizePolicy1.setHeightForWidth(self.principalCuerpoContenido.sizePolicy().hasHeightForWidth())
        self.principalCuerpoContenido.setSizePolicy(sizePolicy1)
        self.principalCuerpoContenido.setMinimumSize(QSize(839, 520))
        self.horizontalLayout_7 = QHBoxLayout(self.principalCuerpoContenido)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 6)
        self.principalContenidosContenedor = QWidget(self.principalCuerpoContenido)
        self.principalContenidosContenedor.setObjectName(u"principalContenidosContenedor")
        self.horizontalLayout_13 = QHBoxLayout(self.principalContenidosContenedor)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.principalPaginas = QCustomQStackedWidget(self.principalContenidosContenedor)
        self.principalPaginas.setObjectName(u"principalPaginas")
        self.inicioPagina = QWidget()
        self.inicioPagina.setObjectName(u"inicioPagina")
        self.verticalLayout_18 = QVBoxLayout(self.inicioPagina)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_2 = QWidget(self.inicioPagina)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_28 = QVBoxLayout(self.widget_2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(9)
        self.tableWidget.setFont(font2)

        self.verticalLayout_28.addWidget(self.tableWidget)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_10.setFont(font3)

        self.verticalLayout_28.addWidget(self.label_10)


        self.verticalLayout_18.addWidget(self.widget_2)

        self.principalPaginas.addWidget(self.inicioPagina)
        self.estudiantesPagina = QWidget()
        self.estudiantesPagina.setObjectName(u"estudiantesPagina")
        self.horizontalLayout_14 = QHBoxLayout(self.estudiantesPagina)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_11 = QLabel(self.estudiantesPagina)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_11)

        self.principalPaginas.addWidget(self.estudiantesPagina)
        self.materiasPagina = QWidget()
        self.materiasPagina.setObjectName(u"materiasPagina")
        self.verticalLayout_20 = QVBoxLayout(self.materiasPagina)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_12 = QLabel(self.materiasPagina)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_12)

        self.principalPaginas.addWidget(self.materiasPagina)
        self.profesoresPagina = QWidget()
        self.profesoresPagina.setObjectName(u"profesoresPagina")
        self.verticalLayout_21 = QVBoxLayout(self.profesoresPagina)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_13 = QLabel(self.profesoresPagina)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_13)

        self.principalPaginas.addWidget(self.profesoresPagina)
        self.notasPagina = QWidget()
        self.notasPagina.setObjectName(u"notasPagina")
        self.verticalLayout_22 = QVBoxLayout(self.notasPagina)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_14 = QLabel(self.notasPagina)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_14)

        self.principalPaginas.addWidget(self.notasPagina)
        self.documentosPagina = QWidget()
        self.documentosPagina.setObjectName(u"documentosPagina")
        self.verticalLayout_23 = QVBoxLayout(self.documentosPagina)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_15 = QLabel(self.documentosPagina)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_15)

        self.principalPaginas.addWidget(self.documentosPagina)
        self.gradosPagina = QWidget()
        self.gradosPagina.setObjectName(u"gradosPagina")
        self.verticalLayout_26 = QVBoxLayout(self.gradosPagina)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_19 = QLabel(self.gradosPagina)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_19)

        self.principalPaginas.addWidget(self.gradosPagina)

        self.horizontalLayout_13.addWidget(self.principalPaginas)


        self.horizontalLayout_7.addWidget(self.principalContenidosContenedor)

        self.menuContenedorDerecho = QCustomSlideMenu(self.principalCuerpoContenido)
        self.menuContenedorDerecho.setObjectName(u"menuContenedorDerecho")
        self.menuContenedorDerecho.setMinimumSize(QSize(250, 0))
        self.menuContenedorDerecho.setMaximumSize(QSize(200, 502))
        self.verticalLayout_13 = QVBoxLayout(self.menuContenedorDerecho)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.subMenuDerecho = QWidget(self.menuContenedorDerecho)
        self.subMenuDerecho.setObjectName(u"subMenuDerecho")
        self.subMenuDerecho.setMinimumSize(QSize(0, 0))
        self.gridLayout_3 = QGridLayout(self.subMenuDerecho)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 0, 0, 0)
        self.frame_9 = QFrame(self.subMenuDerecho)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.cerrarMenuDerecho = QPushButton(self.frame_9)
        self.cerrarMenuDerecho.setObjectName(u"cerrarMenuDerecho")
        self.cerrarMenuDerecho.setIcon(icon12)
        self.cerrarMenuDerecho.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.cerrarMenuDerecho, 0, Qt.AlignRight)


        self.gridLayout_3.addWidget(self.frame_9, 0, 0, 1, 1)

        self.derechoPaginas = QCustomQStackedWidget(self.subMenuDerecho)
        self.derechoPaginas.setObjectName(u"derechoPaginas")
        self.perfilPagina = QWidget()
        self.perfilPagina.setObjectName(u"perfilPagina")
        self.verticalLayout_15 = QVBoxLayout(self.perfilPagina)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget = QWidget(self.perfilPagina)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(224, 308))
        self.verticalLayout_27 = QVBoxLayout(self.widget)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 50))
        self.label_25.setMaximumSize(QSize(50, 50))
        self.label_25.setPixmap(QPixmap(u":/blackIcons/Black/edit.svg"))
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_27.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.widget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setLayoutDirection(Qt.LeftToRight)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.correo = QLineEdit(self.frame_11)
        self.correo.setObjectName(u"correo")
        self.correo.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.correo, 9, 0, 1, 1)

        self.label_33 = QLabel(self.frame_11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(200, 20))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_33.setFont(font5)

        self.gridLayout_5.addWidget(self.label_33, 0, 0, 1, 1)

        self.apellido = QLineEdit(self.frame_11)
        self.apellido.setObjectName(u"apellido")
        self.apellido.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.apellido, 5, 0, 1, 1)

        self.label_23 = QLabel(self.frame_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(200, 20))
        self.label_23.setFont(font5)

        self.gridLayout_5.addWidget(self.label_23, 6, 0, 1, 1)

        self.nombre = QLineEdit(self.frame_11)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.nombre, 3, 0, 1, 1)

        self.cedula = QLineEdit(self.frame_11)
        self.cedula.setObjectName(u"cedula")
        self.cedula.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.cedula, 1, 0, 1, 1)

        self.telefono = QLineEdit(self.frame_11)
        self.telefono.setObjectName(u"telefono")
        self.telefono.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.telefono, 7, 0, 1, 1)

        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(100, 20))
        self.label_20.setFont(font5)
        self.label_20.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_5.addWidget(self.label_20, 2, 0, 1, 1)

        self.label_21 = QLabel(self.frame_11)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(100, 20))
        self.label_21.setFont(font5)
        self.label_21.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_5.addWidget(self.label_21, 4, 0, 1, 1)

        self.label_32 = QLabel(self.frame_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(150, 20))
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_32, 8, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.frame_11)


        self.verticalLayout_15.addWidget(self.widget)

        self.actualizarBoton = QPushButton(self.perfilPagina)
        self.actualizarBoton.setObjectName(u"actualizarBoton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.actualizarBoton.sizePolicy().hasHeightForWidth())
        self.actualizarBoton.setSizePolicy(sizePolicy4)
        self.actualizarBoton.setMinimumSize(QSize(140, 40))
        self.actualizarBoton.setMaximumSize(QSize(140, 40))
        self.actualizarBoton.setFont(font5)
        self.actualizarBoton.setLayoutDirection(Qt.LeftToRight)
        icon20 = QIcon()
        icon20.addFile(u":/blackIcons/Black/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actualizarBoton.setIcon(icon20)
        self.actualizarBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_15.addWidget(self.actualizarBoton, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.perfilPagina)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_8)

        self.derechoPaginas.addWidget(self.perfilPagina)
        self.masPagina = QWidget()
        self.masPagina.setObjectName(u"masPagina")
        self.verticalLayout_16 = QVBoxLayout(self.masPagina)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.masPagina)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_9)

        self.derechoPaginas.addWidget(self.masPagina)
        self.eliminarPagina = QWidget()
        self.eliminarPagina.setObjectName(u"eliminarPagina")
        self.gridLayout = QGridLayout(self.eliminarPagina)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_22 = QLabel(self.eliminarPagina)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 7, 0, 1, 1)

        self.label_24 = QLabel(self.eliminarPagina)
        self.label_24.setObjectName(u"label_24")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(50)
        sizePolicy5.setVerticalStretch(50)
        sizePolicy5.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy5)
        self.label_24.setMinimumSize(QSize(50, 50))
        self.label_24.setPixmap(QPixmap(u":/blackIcons/Black/trash-2.svg"))
        self.label_24.setScaledContents(True)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setWordWrap(False)

        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.eliminarPagina)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(227, 224))
        self.widget_3.setMaximumSize(QSize(227, 16777215))
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.widget_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setContentsMargins(9, 0, 0, 2)
        self.label_28 = QLabel(self.frame_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font5)

        self.gridLayout_2.addWidget(self.label_28, 2, 0, 1, 1)

        self.nombreActualizar = QLineEdit(self.frame_13)
        self.nombreActualizar.setObjectName(u"nombreActualizar")

        self.gridLayout_2.addWidget(self.nombreActualizar, 3, 0, 1, 1)

        self.cedulaEliminar = QLineEdit(self.frame_13)
        self.cedulaEliminar.setObjectName(u"cedulaEliminar")
        self.cedulaEliminar.setMinimumSize(QSize(0, 0))
        self.cedulaEliminar.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.cedulaEliminar, 1, 0, 1, 1)

        self.label_29 = QLabel(self.frame_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font5)

        self.gridLayout_2.addWidget(self.label_29, 4, 0, 1, 1)

        self.label_27 = QLabel(self.frame_13)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)

        self.gridLayout_2.addWidget(self.label_27, 0, 0, 1, 1)

        self.correoActualizar = QLineEdit(self.frame_13)
        self.correoActualizar.setObjectName(u"correoActualizar")

        self.gridLayout_2.addWidget(self.correoActualizar, 9, 0, 1, 1)

        self.telefonoActualizar = QLineEdit(self.frame_13)
        self.telefonoActualizar.setObjectName(u"telefonoActualizar")

        self.gridLayout_2.addWidget(self.telefonoActualizar, 7, 0, 1, 1)

        self.apellidoActualizar = QLineEdit(self.frame_13)
        self.apellidoActualizar.setObjectName(u"apellidoActualizar")

        self.gridLayout_2.addWidget(self.apellidoActualizar, 5, 0, 1, 1)

        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)

        self.gridLayout_2.addWidget(self.label_30, 6, 0, 1, 1)

        self.label_31 = QLabel(self.frame_13)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font5)

        self.gridLayout_2.addWidget(self.label_31, 8, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_13, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)

        self.eliminarBoton = QPushButton(self.eliminarPagina)
        self.eliminarBoton.setObjectName(u"eliminarBoton")
        self.eliminarBoton.setMinimumSize(QSize(0, 10))
        self.eliminarBoton.setFont(font5)
        icon21 = QIcon()
        icon21.addFile(u":/blackIcons/Black/alert-triangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminarBoton.setIcon(icon21)
        self.eliminarBoton.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.eliminarBoton, 6, 0, 1, 1, Qt.AlignHCenter)

        self.editarBoton = QPushButton(self.eliminarPagina)
        self.editarBoton.setObjectName(u"editarBoton")
        self.editarBoton.setMinimumSize(QSize(0, 10))
        self.editarBoton.setFont(font5)
        icon22 = QIcon()
        icon22.addFile(u":/blackIcons/Black/refresh-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editarBoton.setIcon(icon22)
        self.editarBoton.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.editarBoton, 2, 0, 1, 1, Qt.AlignHCenter)

        self.derechoPaginas.addWidget(self.eliminarPagina)

        self.gridLayout_3.addWidget(self.derechoPaginas, 1, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.subMenuDerecho)


        self.horizontalLayout_7.addWidget(self.menuContenedorDerecho)

        self.menuContenedorDerecho.raise_()
        self.principalContenidosContenedor.raise_()

        self.verticalLayout_12.addWidget(self.principalCuerpoContenido)

        self.emergenteNotificacionContenedor = QCustomSlideMenu(self.principalCuerpoContenedor)
        self.emergenteNotificacionContenedor.setObjectName(u"emergenteNotificacionContenedor")
        self.verticalLayout_24 = QVBoxLayout(self.emergenteNotificacionContenedor)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.emergenteNotificacionSubContenedor = QWidget(self.emergenteNotificacionContenedor)
        self.emergenteNotificacionSubContenedor.setObjectName(u"emergenteNotificacionSubContenedor")
        self.verticalLayout_25 = QVBoxLayout(self.emergenteNotificacionSubContenedor)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_17 = QLabel(self.emergenteNotificacionSubContenedor)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)

        self.verticalLayout_25.addWidget(self.label_17)

        self.frame_10 = QFrame(self.emergenteNotificacionSubContenedor)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.cerrarNotificacion = QPushButton(self.frame_10)
        self.cerrarNotificacion.setObjectName(u"cerrarNotificacion")
        self.cerrarNotificacion.setIcon(icon12)
        self.cerrarNotificacion.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.cerrarNotificacion, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_10)


        self.verticalLayout_24.addWidget(self.emergenteNotificacionSubContenedor)


        self.verticalLayout_12.addWidget(self.emergenteNotificacionContenedor)

        self.pieContenedor = QWidget(self.principalCuerpoContenedor)
        self.pieContenedor.setObjectName(u"pieContenedor")
        self.horizontalLayout_10 = QHBoxLayout(self.pieContenedor)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.pieContenedor)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label_18)


        self.horizontalLayout_10.addWidget(self.frame_12)

        self.dimensionBarra = QFrame(self.pieContenedor)
        self.dimensionBarra.setObjectName(u"dimensionBarra")
        self.dimensionBarra.setMinimumSize(QSize(10, 10))
        self.dimensionBarra.setMaximumSize(QSize(10, 10))
        self.dimensionBarra.setFrameShape(QFrame.StyledPanel)
        self.dimensionBarra.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.dimensionBarra, 0, Qt.AlignBottom)


        self.verticalLayout_12.addWidget(self.pieContenedor)


        self.horizontalLayout.addWidget(self.principalCuerpoContenedor)

        ventanaPrincipal.setCentralWidget(self.centralContenedor)

        self.retranslateUi(ventanaPrincipal)

        self.principalPaginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ventanaPrincipal)
    # setupUi

    def retranslateUi(self, ventanaPrincipal):
        ventanaPrincipal.setWindowTitle(QCoreApplication.translate("ventanaPrincipal", u"Sistema Gestion Estudiantil Andres Bello", None))
#if QT_CONFIG(tooltip)
        self.menuBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBoton.setText("")
#if QT_CONFIG(tooltip)
        self.inicioBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Inicio", None))
#endif // QT_CONFIG(tooltip)
        self.inicioBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"INICIO", None))
#if QT_CONFIG(tooltip)
        self.estudianteBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Estudiantes", None))
#endif // QT_CONFIG(tooltip)
        self.estudianteBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ESTUDIANTES", None))
#if QT_CONFIG(tooltip)
        self.materiaBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Materias", None))
#endif // QT_CONFIG(tooltip)
        self.materiaBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"MATERIAS", None))
#if QT_CONFIG(tooltip)
        self.profesorBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Profesores", None))
#endif // QT_CONFIG(tooltip)
        self.profesorBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"PROFESORES", None))
#if QT_CONFIG(tooltip)
        self.notaBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Notas", None))
#endif // QT_CONFIG(tooltip)
        self.notaBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"NOTAS", None))
#if QT_CONFIG(tooltip)
        self.documentoBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Documentos", None))
#endif // QT_CONFIG(tooltip)
        self.documentoBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"DOCUMENTOS", None))
#if QT_CONFIG(tooltip)
        self.gradosBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Grados", None))
#endif // QT_CONFIG(tooltip)
        self.gradosBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"GRADOS", None))
#if QT_CONFIG(tooltip)
        self.ajustesBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Ajustes", None))
#endif // QT_CONFIG(tooltip)
        self.ajustesBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"AJUSTES", None))
#if QT_CONFIG(tooltip)
        self.acercaDeBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Acerca de", None))
#endif // QT_CONFIG(tooltip)
        self.acercaDeBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ACERCA DE", None))
#if QT_CONFIG(tooltip)
        self.ayudaBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Ayuda", None))
#endif // QT_CONFIG(tooltip)
        self.ayudaBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"AYUDA", None))
#if QT_CONFIG(tooltip)
        self.cerrarSesionBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Sesion", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarSesionBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"CERRAR SESION", None))
        self.label.setText(QCoreApplication.translate("ventanaPrincipal", u"Mas cositas", None))
#if QT_CONFIG(tooltip)
        self.cerrarMenuCentro.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Menu", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarMenuCentro.setText("")
        self.label_2.setText(QCoreApplication.translate("ventanaPrincipal", u"AJUSTES", None))
        self.label_3.setText(QCoreApplication.translate("ventanaPrincipal", u"ACERCA DE", None))
        self.label_4.setText(QCoreApplication.translate("ventanaPrincipal", u"AYUDA", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("ventanaPrincipal", u"Complejo Educativo Andres Bello", None))
        self.notificacionBoton.setText("")
#if QT_CONFIG(tooltip)
        self.masBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Mas", None))
#endif // QT_CONFIG(tooltip)
        self.masBoton.setText("")
#if QT_CONFIG(tooltip)
        self.perfilBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Perfil", None))
#endif // QT_CONFIG(tooltip)
        self.perfilBoton.setText("")
        self.botonMenuEliminar.setText("")
#if QT_CONFIG(tooltip)
        self.minimizarBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Minimizar Ventana", None))
#endif // QT_CONFIG(tooltip)
        self.minimizarBoton.setText("")
#if QT_CONFIG(tooltip)
        self.restaurarBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Restaurar Ventana", None))
#endif // QT_CONFIG(tooltip)
        self.restaurarBoton.setText("")
#if QT_CONFIG(tooltip)
        self.cerrarBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Ventana", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarBoton.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ventanaPrincipal", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ventanaPrincipal", u"Cedula", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ventanaPrincipal", u"Nombre", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ventanaPrincipal", u"Apellido", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ventanaPrincipal", u"Telefono", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ventanaPrincipal", u"Correo", None));
        self.label_10.setText(QCoreApplication.translate("ventanaPrincipal", u"INFORMACION", None))
        self.label_11.setText(QCoreApplication.translate("ventanaPrincipal", u"ESTUDIANTES", None))
        self.label_12.setText(QCoreApplication.translate("ventanaPrincipal", u"MATERIAS", None))
        self.label_13.setText(QCoreApplication.translate("ventanaPrincipal", u"PROFESORES", None))
        self.label_14.setText(QCoreApplication.translate("ventanaPrincipal", u"NOTAS", None))
        self.label_15.setText(QCoreApplication.translate("ventanaPrincipal", u"DOCUMENTOS", None))
        self.label_19.setText(QCoreApplication.translate("ventanaPrincipal", u"GRADOS", None))
        self.label_7.setText(QCoreApplication.translate("ventanaPrincipal", u"Informacion Detallada", None))
#if QT_CONFIG(tooltip)
        self.cerrarMenuDerecho.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Menu", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarMenuDerecho.setText("")
        self.label_25.setText("")
        self.correo.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Correo Electronico", None))
        self.label_33.setText(QCoreApplication.translate("ventanaPrincipal", u"Cedula de Identidad", None))
        self.apellido.setText("")
        self.apellido.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Apellido", None))
        self.label_23.setText(QCoreApplication.translate("ventanaPrincipal", u"Telefono", None))
        self.nombre.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Nombre", None))
        self.cedula.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Nro. de Cedula", None))
        self.telefono.setText("")
        self.telefono.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Telefono", None))
        self.label_20.setText(QCoreApplication.translate("ventanaPrincipal", u"Nombre", None))
        self.label_21.setText(QCoreApplication.translate("ventanaPrincipal", u"Apellido", None))
        self.label_32.setText(QCoreApplication.translate("ventanaPrincipal", u"Correo Electronico", None))
        self.actualizarBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ACTUALIZAR", None))
        self.label_8.setText(QCoreApplication.translate("ventanaPrincipal", u"PERFIL", None))
        self.label_9.setText(QCoreApplication.translate("ventanaPrincipal", u"MAS...", None))
        self.label_22.setText(QCoreApplication.translate("ventanaPrincipal", u"CUIDADO", None))
        self.label_24.setText("")
        self.label_28.setText(QCoreApplication.translate("ventanaPrincipal", u"Nombre", None))
        self.label_29.setText(QCoreApplication.translate("ventanaPrincipal", u"Apellido", None))
        self.label_27.setText(QCoreApplication.translate("ventanaPrincipal", u"Cedula", None))
        self.label_30.setText(QCoreApplication.translate("ventanaPrincipal", u"Telefono", None))
        self.label_31.setText(QCoreApplication.translate("ventanaPrincipal", u"Correo", None))
        self.eliminarBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ELIMINAR", None))
        self.editarBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ACTUALIZAR", None))
        self.label_17.setText(QCoreApplication.translate("ventanaPrincipal", u"Notificacion", None))
        self.label_16.setText(QCoreApplication.translate("ventanaPrincipal", u"Notificacion Mensaje", None))
#if QT_CONFIG(tooltip)
        self.cerrarNotificacion.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Notificacion", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarNotificacion.setText("")
        self.label_18.setText(QCoreApplication.translate("ventanaPrincipal", u"Creado por: Yoel Rivero UBV", None))
    # retranslateUi

