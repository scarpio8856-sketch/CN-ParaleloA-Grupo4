# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1220, 780)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutMain = QHBoxLayout(self.centralwidget)
        self.horizontalLayoutMain.setObjectName(u"horizontalLayoutMain")
        self.grpEntrada = QGroupBox(self.centralwidget)
        self.grpEntrada.setObjectName(u"grpEntrada")
        self.verticalLayoutEntrada = QVBoxLayout(self.grpEntrada)
        self.verticalLayoutEntrada.setObjectName(u"verticalLayoutEntrada")
        self.formLayoutParametros = QFormLayout()
        self.formLayoutParametros.setObjectName(u"formLayoutParametros")
        self.lblEjemplos = QLabel(self.grpEntrada)
        self.lblEjemplos.setObjectName(u"lblEjemplos")

        self.formLayoutParametros.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblEjemplos)

        self.cmbEjemplos = QComboBox(self.grpEntrada)
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.setObjectName(u"cmbEjemplos")

        self.formLayoutParametros.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbEjemplos)

        self.lblFuncion = QLabel(self.grpEntrada)
        self.lblFuncion.setObjectName(u"lblFuncion")

        self.formLayoutParametros.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFuncion)

        self.txtFuncion = QLineEdit(self.grpEntrada)
        self.txtFuncion.setObjectName(u"txtFuncion")

        self.formLayoutParametros.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtFuncion)

        self.lblXl = QLabel(self.grpEntrada)
        self.lblXl.setObjectName(u"lblXl")

        self.formLayoutParametros.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblXl)

        self.spnXl = QDoubleSpinBox(self.grpEntrada)
        self.spnXl.setObjectName(u"spnXl")
        self.spnXl.setDecimals(6)
        self.spnXl.setMinimum(-100000.000000000000000)
        self.spnXl.setMaximum(100000.000000000000000)
        self.spnXl.setSingleStep(0.100000000000000)

        self.formLayoutParametros.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spnXl)

        self.lblXu = QLabel(self.grpEntrada)
        self.lblXu.setObjectName(u"lblXu")

        self.formLayoutParametros.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblXu)

        self.spnXu = QDoubleSpinBox(self.grpEntrada)
        self.spnXu.setObjectName(u"spnXu")
        self.spnXu.setDecimals(6)
        self.spnXu.setMinimum(-100000.000000000000000)
        self.spnXu.setMaximum(100000.000000000000000)
        self.spnXu.setSingleStep(0.100000000000000)
        self.spnXu.setValue(1.000000000000000)

        self.formLayoutParametros.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spnXu)

        self.lblEs = QLabel(self.grpEntrada)
        self.lblEs.setObjectName(u"lblEs")

        self.formLayoutParametros.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblEs)

        self.spnEs = QDoubleSpinBox(self.grpEntrada)
        self.spnEs.setObjectName(u"spnEs")
        self.spnEs.setDecimals(6)
        self.spnEs.setMinimum(0.000001000000000)
        self.spnEs.setMaximum(100.000000000000000)
        self.spnEs.setSingleStep(0.010000000000000)
        self.spnEs.setValue(0.010000000000000)

        self.formLayoutParametros.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spnEs)

        self.lblMaxIter = QLabel(self.grpEntrada)
        self.lblMaxIter.setObjectName(u"lblMaxIter")

        self.formLayoutParametros.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblMaxIter)

        self.spnMaxIter = QSpinBox(self.grpEntrada)
        self.spnMaxIter.setObjectName(u"spnMaxIter")
        self.spnMaxIter.setMinimum(1)
        self.spnMaxIter.setMaximum(1000)
        self.spnMaxIter.setValue(100)

        self.formLayoutParametros.setWidget(5, QFormLayout.ItemRole.FieldRole, self.spnMaxIter)

        self.lblValorVerdadero = QLabel(self.grpEntrada)
        self.lblValorVerdadero.setObjectName(u"lblValorVerdadero")

        self.formLayoutParametros.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblValorVerdadero)

        self.txtValorVerdadero = QLineEdit(self.grpEntrada)
        self.txtValorVerdadero.setObjectName(u"txtValorVerdadero")

        self.formLayoutParametros.setWidget(6, QFormLayout.ItemRole.FieldRole, self.txtValorVerdadero)

        self.lblUnidades = QLabel(self.grpEntrada)
        self.lblUnidades.setObjectName(u"lblUnidades")

        self.formLayoutParametros.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblUnidades)

        self.txtUnidades = QLineEdit(self.grpEntrada)
        self.txtUnidades.setObjectName(u"txtUnidades")

        self.formLayoutParametros.setWidget(7, QFormLayout.ItemRole.FieldRole, self.txtUnidades)

        self.lblPasoDx = QLabel(self.grpEntrada)
        self.lblPasoDx.setObjectName(u"lblPasoDx")

        self.formLayoutParametros.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lblPasoDx)

        self.spnPasoDx = QDoubleSpinBox(self.grpEntrada)
        self.spnPasoDx.setObjectName(u"spnPasoDx")
        self.spnPasoDx.setDecimals(4)
        self.spnPasoDx.setMinimum(0.000100000000000)
        self.spnPasoDx.setMaximum(1000.000000000000000)
        self.spnPasoDx.setSingleStep(0.050000000000000)
        self.spnPasoDx.setValue(0.100000000000000)

        self.formLayoutParametros.setWidget(8, QFormLayout.ItemRole.FieldRole, self.spnPasoDx)


        self.verticalLayoutEntrada.addLayout(self.formLayoutParametros)

        self.gridLayoutBotones = QGridLayout()
        self.gridLayoutBotones.setObjectName(u"gridLayoutBotones")
        self.btnCalcular = QPushButton(self.grpEntrada)
        self.btnCalcular.setObjectName(u"btnCalcular")

        self.gridLayoutBotones.addWidget(self.btnCalcular, 0, 0, 1, 1)

        self.btnBuscarIntervalos = QPushButton(self.grpEntrada)
        self.btnBuscarIntervalos.setObjectName(u"btnBuscarIntervalos")

        self.gridLayoutBotones.addWidget(self.btnBuscarIntervalos, 0, 1, 1, 1)

        self.btnLimpiar = QPushButton(self.grpEntrada)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.gridLayoutBotones.addWidget(self.btnLimpiar, 1, 0, 1, 1)

        self.btnExportar = QPushButton(self.grpEntrada)
        self.btnExportar.setObjectName(u"btnExportar")

        self.gridLayoutBotones.addWidget(self.btnExportar, 1, 1, 1, 1)


        self.verticalLayoutEntrada.addLayout(self.gridLayoutBotones)

        self.verticalSpacerEntrada = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutEntrada.addItem(self.verticalSpacerEntrada)


        self.horizontalLayoutMain.addWidget(self.grpEntrada)

        self.grpResultados = QGroupBox(self.centralwidget)
        self.grpResultados.setObjectName(u"grpResultados")
        self.verticalLayoutResultados = QVBoxLayout(self.grpResultados)
        self.verticalLayoutResultados.setObjectName(u"verticalLayoutResultados")
        self.tabGraficas = QTabWidget(self.grpResultados)
        self.tabGraficas.setObjectName(u"tabGraficas")
        self.tabFuncion = QWidget()
        self.tabFuncion.setObjectName(u"tabFuncion")
        self.layoutTabFunc = QVBoxLayout(self.tabFuncion)
        self.layoutTabFunc.setObjectName(u"layoutTabFunc")
        self.widgetGraficaFuncion = QWidget(self.tabFuncion)
        self.widgetGraficaFuncion.setObjectName(u"widgetGraficaFuncion")

        self.layoutTabFunc.addWidget(self.widgetGraficaFuncion)

        self.tabGraficas.addTab(self.tabFuncion, "")
        self.tabError = QWidget()
        self.tabError.setObjectName(u"tabError")
        self.layoutTabError = QVBoxLayout(self.tabError)
        self.layoutTabError.setObjectName(u"layoutTabError")
        self.widgetGraficaError = QWidget(self.tabError)
        self.widgetGraficaError.setObjectName(u"widgetGraficaError")

        self.layoutTabError.addWidget(self.widgetGraficaError)

        self.tabGraficas.addTab(self.tabError, "")
        self.tabAcercaDe = QWidget()
        self.tabAcercaDe.setObjectName(u"tabAcercaDe")
        self.layoutTabAcerca = QVBoxLayout(self.tabAcercaDe)
        self.layoutTabAcerca.setObjectName(u"layoutTabAcerca")
        self.lblAcercaDe = QLabel(self.tabAcercaDe)
        self.lblAcercaDe.setObjectName(u"lblAcercaDe")
        self.lblAcercaDe.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lblAcercaDe.setWordWrap(True)

        self.layoutTabAcerca.addWidget(self.lblAcercaDe)

        self.tabGraficas.addTab(self.tabAcercaDe, "")

        self.verticalLayoutResultados.addWidget(self.tabGraficas)

        self.tablaResultados = QTableWidget(self.grpResultados)
        self.tablaResultados.setObjectName(u"tablaResultados")

        self.verticalLayoutResultados.addWidget(self.tablaResultados)

        self.txtResultado = QTextEdit(self.grpResultados)
        self.txtResultado.setObjectName(u"txtResultado")
        self.txtResultado.setMaximumSize(QSize(16777215, 140))
        self.txtResultado.setReadOnly(True)

        self.verticalLayoutResultados.addWidget(self.txtResultado)

        self.verticalLayoutResultados.setStretch(0, 3)
        self.verticalLayoutResultados.setStretch(1, 2)
        self.verticalLayoutResultados.setStretch(2, 1)

        self.horizontalLayoutMain.addWidget(self.grpResultados)

        self.horizontalLayoutMain.setStretch(0, 1)
        self.horizontalLayoutMain.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabGraficas.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"C\u00e1lculo Num\u00e9rico - M\u00e9todo de Bisecci\u00f3n (Grupo 4: Diodo)", None))
        self.grpEntrada.setTitle(QCoreApplication.translate("MainWindow", u"Par\u00e1metros de entrada", None))
        self.lblEjemplos.setText(QCoreApplication.translate("MainWindow", u"Caso / Ejemplo:", None))
        self.cmbEjemplos.setItemText(0, QCoreApplication.translate("MainWindow", u"Caso Grupo 4: Punto de operaci\u00f3n de un diodo", None))
        self.cmbEjemplos.setItemText(1, QCoreApplication.translate("MainWindow", u"Ejemplo libro (Chapra): Paracaidista", None))
        self.cmbEjemplos.setItemText(2, QCoreApplication.translate("MainWindow", u"Ejemplo libro: exp(-x) - x", None))

        self.lblFuncion.setText(QCoreApplication.translate("MainWindow", u"Funci\u00f3n f(x):", None))
        self.txtFuncion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: exp(-x) - x", None))
        self.lblXl.setText(QCoreApplication.translate("MainWindow", u"L\u00edmite inferior (xl):", None))
        self.lblXu.setText(QCoreApplication.translate("MainWindow", u"L\u00edmite superior (xu):", None))
        self.lblEs.setText(QCoreApplication.translate("MainWindow", u"Tolerancia \u03b5s (%):", None))
        self.lblMaxIter.setText(QCoreApplication.translate("MainWindow", u"M\u00e1x. iteraciones:", None))
        self.lblValorVerdadero.setText(QCoreApplication.translate("MainWindow", u"Valor verdadero (opc.):", None))
        self.txtValorVerdadero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcional para calcular \u03b5t (%)", None))
        self.lblUnidades.setText(QCoreApplication.translate("MainWindow", u"Unidades f\u00edsicas:", None))
        self.txtUnidades.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lblPasoDx.setText(QCoreApplication.translate("MainWindow", u"Paso b\u00fasqueda \u0394x:", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.btnBuscarIntervalos.setText(QCoreApplication.translate("MainWindow", u"Buscar intervalos (\u0394x)", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnExportar.setText(QCoreApplication.translate("MainWindow", u"Exportar CSV", None))
        self.grpResultados.setTitle(QCoreApplication.translate("MainWindow", u"Resultados, Tabla y Gr\u00e1ficas", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabFuncion), QCoreApplication.translate("MainWindow", u"Gr\u00e1fica f(x)", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabError), QCoreApplication.translate("MainWindow", u"Convergencia \u03b5a", None))
        self.lblAcercaDe.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Proyecto de Aula: M\u00e9todo de Bisecci\u00f3n (Proyecto B - Grupo 4)</span></h3><p><span style=\" font-weight:700;\">Asignatura:</span> C\u00e1lculo Num\u00e9rico (MECATR24) \u2014 Quinto Nivel, Ingenier\u00eda Mecatr\u00f3nica</p><p><span style=\" font-weight:700;\">Caso de aplicaci\u00f3n obligatorio:</span> Punto de operaci\u00f3n de un diodo semiconductor (Vs = 5 V, R = 1 k\u03a9, Is = 1\u00d710\u207b\u00b9\u00b2 A, VT = 25.85 mV)</p><p><span style=\" font-weight:700;\">Paralelo:</span> A</p><p><span style=\" font-weight:700;\">Integrantes del Equipo (4):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Integrante 1 (L\u00f3g"
                        "ica num\u00e9rica): JOS\u00c9 STEVEN NAVARRETE RIVAS</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Integrante 2 (Interfaz Qt Designer): JUNIOR ALEXANDER HERRERA CH\u00c1VEZ</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Integrante 3 (Controlador y gr\u00e1ficas): STEVEN JOSU\u00c9 CARPIO FRANCO</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Integrante 4 (Pruebas y documentaci\u00f3n): ALAN FLAUBERT FIERRO YANZA</li></ul></body></html>", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabAcercaDe), QCoreApplication.translate("MainWindow", u"Acerca de", None))
    # retranslateUi

