# -*- coding: utf-8 -*-

from Librarys.matplotlib_lib import *
from self_functions.functions import *
from Librarys.sklearn_lib import *
from self_Dialogs.Dialogs import *
import ctypes
import tensorflow as tf
from collections import Counter
import os
import copy
import time
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    filepath = ""
    loaded_data = []
    hasPCA = False

    def __init__(self):

        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        self.setWindowIcon(QtGui.QIcon('beau/BrainSort.png'))
        self.feature_name = ['Precentral_L',
                             'Precentral_R',
                             'Frontal_Sup_L',
                             'Frontal_Sup_R',
                             'Frontal_Sup_Orb_L',
                             'Frontal_Sup_Orb_R',
                             'Frontal_Mid_L',
                             'Frontal_Mid_R',
                             'Frontal_Mid_Orb_L',
                             'Frontal_Mid_Orb_R',
                             'Frontal_Inf_Oper_L',
                             'Frontal_Inf_Oper_R',
                             'Frontal_Inf_Tri_L',
                             'Frontal_Inf_Tri_R',
                             'Frontal_Inf_Orb_L',
                             'Frontal_Inf_Orb_R',
                             'Rolandic_Oper_L',
                             'Rolandic_Oper_R',
                             'Supp_Motor_Area_L',
                             'Supp_Motor_Area_R',
                             'Olfactory_L',
                             'Olfactory_R',
                             'Frontal_Sup_Medial_L',
                             'Frontal_Sup_Medial_R',
                             'Frontal_Mid_Orb_L',
                             'Frontal_Mid_Orb_R',
                             'Rectus_L',
                             'Rectus_R',
                             'Insula_L',
                             'Insula_R',
                             'Cingulum_Ant_L',
                             'Cingulum_Ant_R',
                             'Cingulum_Mid_L',
                             'Cingulum_Mid_R',
                             'Cingulum_Post_L',
                             'Cingulum_Post_R',
                             'Hippocampus_L',
                             'Hippocampus_R',
                             'ParaHippocampal_L',
                             'ParaHippocampal_R',
                             'Amygdala_L',
                             'Amygdala_R',
                             'Calcarine_L',
                             'Calcarine_R',
                             'Cuneus_L',
                             'Cuneus_R',
                             'Lingual_L',
                             'Lingual_R',
                             'Occipital_Sup_L',
                             'Occipital_Sup_R',
                             'Occipital_Mid_L',
                             'Occipital_Mid_R',
                             'Occipital_Inf_L',
                             'Occipital_Inf_R',
                             'Fusiform_L',
                             'Fusiform_R',
                             'Postcentral_L',
                             'Postcentral_R',
                             'Parietal_Sup_L',
                             'Parietal_Sup_R',
                             'Parietal_Inf_L',
                             'Parietal_Inf_R',
                             'SupraMarginal_L',
                             'SupraMarginal_R',
                             'Angular_L',
                             'Angular_R',
                             'Precuneus_L',
                             'Precuneus_R',
                             'Paracentral_Lobule_L',
                             'Paracentral_Lobule_R',
                             'Caudate_L',
                             'Caudate_R',
                             'Putamen_L',
                             'Putamen_R',
                             'Pallidum_L',
                             'Pallidum_R',
                             'Thalamus_L',
                             'Thalamus_R',
                             'Heschl_L',
                             'Heschl_R',
                             'Temporal_Sup_L',
                             'Temporal_Sup_R',
                             'Temporal_Pole_Sup_L',
                             'Temporal_Pole_Sup_R',
                             'Temporal_Mid_L',
                             'Temporal_Mid_R',
                             'Temporal_Pole_Mid_L',
                             'Temporal_Pole_Mid_R',
                             'Temporal_Inf_L',
                             'Temporal_Inf_R',
                             ]

        self.tri = np.loadtxt(r'source\\tri8.txt')
        print('tri', self.tri.shape)
        self.coord = np.loadtxt(r'source\\coord8.txt')
        print('coord', self.coord.shape)

        self.x = np.loadtxt(r'source\x.txt')
        self.y = np.loadtxt(r'source\y.txt')
        self.z = np.loadtxt(r'source\z.txt')
        print('x,y,z', np.shape(self.x))

        # 如果电脑不存在D盘则会报错
        if not os.path.exists(r'D:\BrainSort_workspace'):
            os.makedirs(r'D:\BrainSort_workspace')

        if not os.path.exists(r'D:\BrainSort_features'):
            os.makedirs(r'D:\BrainSort_features')

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 618)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 618))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 618))
        self.setWindowTitle(str("Brain Sort"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # 字体设置
        font_M = QtGui.QFont()
        font_M.setFamily('MicrosoftYaHei')

        font_A = QtGui.QFont()
        font_A.setFamily('AvenirNext-Regular')

        font_H = QtGui.QFont()
        font_H.setFamily('Helvetica')

        # 绘图区域的设置
        self.plot_widget = QtGui.QWidget(self.centralwidget)
        self.plot_widget.setGeometry(QtCore.QRect(0, 0, 651, 451))
        self.plot_widget.setObjectName(_fromUtf8("plot_widget"))

        # 绘图
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.plot_widget.figure = plt.figure()
        self.ax = self.plot_widget.figure.add_subplot(111)
        self.plot_widget.canvas = FigureCanvas(self.plot_widget.figure)
        self.plot_widget.toolbar = NavigationToolbar(self.plot_widget.canvas, self.plot_widget)

        self.plot_action = QtGui.QAction(MainWindow)
        self.plot_action.triggered.connect(self.plot)

        self.ROC_action = QtGui.QAction(MainWindow)
        self.ROC_action.triggered.connect(self.plot_ROC)

        self.plot_brain_action = QtGui.QAction(MainWindow)
        self.plot_brain_action.triggered.connect(self.plot_brain)

        plot_layout = QtGui.QVBoxLayout()
        plot_layout.addWidget(self.plot_widget.canvas)
        plot_layout.addWidget(self.plot_widget.toolbar)
        self.plot_widget.setLayout(plot_layout)

        # 运行状态显示区域的设置
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(651, 8, 351, 361))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setStyleSheet('font-family:Helvetica;font-size:14px;color:#697B8C;line-height:22px;')

        # 字体颜色设置

        self.label_accuracy = QtGui.QLabel(self.centralwidget)
        self.label_accuracy.setGeometry(QtCore.QRect(653, 372, 80, 16))
        self.label_accuracy.setObjectName(_fromUtf8("label_accuracy"))
        self.label_accuracy.setFont(font_A)
        self.label_accuracy.setStyleSheet('font-family:MicrosoftYaHei;font-size:14px;')

        self.lineEdit_accuracy = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_accuracy.setGeometry(QtCore.QRect(750, 372, 133, 20))
        self.lineEdit_accuracy.setReadOnly(True)
        self.lineEdit_accuracy.setObjectName(_fromUtf8("lineEdit_accuracy"))
        self.lineEdit_accuracy.setStyleSheet(
            'opacity:0.4;font-family:MicrosoftYaHei;font-size:14px;color:#697B8C;text-align:left;')

        self.label_sensitivity = QtGui.QLabel(self.centralwidget)
        self.label_sensitivity.setGeometry(QtCore.QRect(653, 400, 80, 16))
        self.label_sensitivity.setObjectName(_fromUtf8("label_sensitivity"))
        self.label_sensitivity.setFont(font_A)
        self.label_sensitivity.setStyleSheet('font-family:MicrosoftYaHei;font-size:14px')

        self.lineEdit_sensitivity = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_sensitivity.setGeometry(QtCore.QRect(750, 400, 133, 20))
        self.lineEdit_sensitivity.setReadOnly(True)
        self.lineEdit_sensitivity.setObjectName(_fromUtf8("lineEdit_sensitivity"))
        self.lineEdit_sensitivity.setStyleSheet(
            'opacity:0.4;font-family:MicrosoftYaHei;font-size:14px;color:#697B8C;text-align:left;')

        self.label_specificity = QtGui.QLabel(self.centralwidget)
        self.label_specificity.setGeometry(QtCore.QRect(653, 428, 80, 16))
        self.label_specificity.setObjectName(_fromUtf8("label_specificity"))
        self.label_specificity.setFont(font_A)
        self.label_specificity.setStyleSheet('font-family:MicrosoftYaHei;font-size:14px;')

        self.lineEdit_specificity = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_specificity.setGeometry(QtCore.QRect(750, 428, 133, 20))
        self.lineEdit_specificity.setReadOnly(True)
        self.lineEdit_specificity.setObjectName(_fromUtf8("lineEdit_specificity"))
        self.lineEdit_specificity.setStyleSheet(
            'opacity:0.4;font-family:MicrosoftYaHei;font-size:14px;color:#697B8C;text-align:left;')

        # 前面的那些部件构造时都选取了 centralwidget 作为父部件，此处将其设为主窗口的中心部件
        MainWindow.setCentralWidget(self.centralwidget)

        # 菜单栏和菜单项的设置
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.File = QtGui.QMenu(self.menubar)
        self.File.setObjectName(_fromUtf8("File"))
        self.File.setFont(font_M)

        self.Load = QtGui.QMenu(self.File)
        self.Load.setObjectName(_fromUtf8("Load"))
        self.Load.setFont(font_A)

        self.about_predict = QtGui.QMenu(self.File)

        self.ALG = QtGui.QMenu(self.menubar)
        self.ALG.setObjectName(_fromUtf8("ALG"))
        self.ALG.setFont(font_M)

        self.SVM = QtGui.QMenu(self.ALG)
        self.SVM.setObjectName(_fromUtf8("SVM"))
        self.SVM.setFont(font_A)

        self.Pre_Process = QtGui.QMenu(self.menubar)
        self.Pre_Process.setFont(font_M)

        self.Feature_select = QtGui.QMenu(self.menubar)
        self.Feature_select.setObjectName(_fromUtf8("Feature_Select"))
        self.Feature_select.setFont(font_M)

        self.Visualization = QtGui.QMenu(self.menubar)
        self.Visualization.setFont(font_M)

        self.HELP = QtGui.QMenu(self.menubar)
        self.HELP.setObjectName(_fromUtf8("HELP"))
        self.HELP.setFont(font_M)

        # 将配置好的menubar添加到主窗口中
        MainWindow.setMenuBar(self.menubar)
        self.menubar.setStyleSheet('font-family:MicrosoftYaHei;font-size:14px;')
        # 构建了一个状态栏
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        # 构造一个工具栏，
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # 下面是构建了许多action，并将action与执行的函数连接在一起
        # 没有连接的就是等待写执行函数的
        self.open_with_label = QtGui.QAction(MainWindow)
        self.open_with_label.setObjectName(_fromUtf8("with_label"))
        self.open_with_label.triggered.connect(self.open_withlabel)
        self.open_with_label.setFont(font_A)

        self.open_with_desc = QtGui.QAction(MainWindow)
        self.open_with_desc.setObjectName(_fromUtf8("with_desc"))
        self.open_with_desc.triggered.connect(self.open_withdesc)
        self.open_with_desc.setFont(font_A)

        self.open_mat = QtGui.QAction(MainWindow)
        self.open_mat.setObjectName(_fromUtf8("with_label"))
        self.open_mat.triggered.connect(self.openmat)
        self.open_mat.setFont(font_A)

        self.open_with_features = QtGui.QAction(MainWindow)
        self.open_with_features.setObjectName(_fromUtf8("with_desc"))
        self.open_with_features.triggered.connect(self.open_features)
        self.open_with_features.setFont(font_A)

        self.save_action = QtGui.QAction(MainWindow)
        self.save_action.setObjectName(_fromUtf8("save_action"))
        self.save_action.triggered.connect(self.savemodel)
        self.save_action.setFont(font_A)


        self.linear = QtGui.QAction(MainWindow)
        self.linear.setObjectName(_fromUtf8("linear"))
        self.linear.triggered.connect(self.linear_D)
        self.linear.setFont(font_A)

        self.rbf = QtGui.QAction(MainWindow)
        self.rbf.setObjectName(_fromUtf8("rbf"))
        self.rbf.triggered.connect(self.rbf_D)
        self.rbf.setFont(font_A)

        self.knn = QtGui.QAction(MainWindow)
        self.knn.setObjectName(_fromUtf8("knn"))
        self.knn.triggered.connect(self.knn_D)
        self.knn.setFont(font_A)

        self.cnn = QtGui.QAction(MainWindow)
        self.cnn.setObjectName(_fromUtf8("knn"))
        self.cnn.triggered.connect(self.cnn_D)
        self.cnn.setFont(font_A)

        self.elastic = QtGui.QAction(MainWindow)
        self.elastic.setObjectName(_fromUtf8("elastic"))
        self.elastic.triggered.connect(self.elastic_D)
        self.elastic.setFont(font_A)

        self.ttest_action = QtGui.QAction(MainWindow)
        self.ttest_action.setObjectName(_fromUtf8("TTest"))
        self.ttest_action.triggered.connect(self.run_ttest)
        self.ttest_action.setFont(font_A)

        self.lasso_action = QtGui.QAction(MainWindow)
        self.lasso_action.setObjectName(_fromUtf8("Lasso"))
        self.lasso_action.triggered.connect(self.run_lasso)
        self.lasso_action.setFont(font_A)

        self.rf_model = QtGui.QAction(MainWindow)
        self.rf_model.setObjectName(_fromUtf8("Lasso"))
        self.rf_model.triggered.connect(self.run_rf_model)
        self.rf_model.setFont(font_A)

        self.Fisher_score = QtGui.QAction(MainWindow)
        self.Fisher_score.setObjectName(_fromUtf8("Fisher_score"))
        self.Fisher_score.triggered.connect(self.run_Fisher_score)
        self.Fisher_score.setFont(font_A)

        self.norm_action = QtGui.QAction(MainWindow)
        self.norm_action.setObjectName(_fromUtf8("Norm"))
        self.norm_action.triggered.connect(self.run_norm)
        self.norm_action.setFont(font_A)

        self.min_max_action = QtGui.QAction(MainWindow)
        self.min_max_action.setObjectName(_fromUtf8("Norm"))
        self.min_max_action.triggered.connect(self.run_min_max)
        self.min_max_action.setFont(font_A)

        self.replace_nan = QtGui.QAction(MainWindow)
        self.replace_nan.setObjectName(_fromUtf8("replace_nan"))
        self.replace_nan.triggered.connect(self.run_replace_nan)
        self.replace_nan.setFont(font_A)

        self.pca_action = QtGui.QAction(MainWindow)
        self.pca_action.setObjectName(_fromUtf8("PCA"))
        self.pca_action.triggered.connect(self.run_pca)
        self.pca_action.setFont(font_A)

        self.about_software = QtGui.QAction(MainWindow)
        self.about_software.setObjectName(_fromUtf8("about_software"))
        self.about_software.setFont(font_A)

        self.about_ALG = QtGui.QAction(MainWindow)
        self.about_ALG.setObjectName(_fromUtf8("about_ALG"))
        self.about_ALG.setFont(font_A)

        self.run = QtGui.QAction(MainWindow)
        self.run.setObjectName(_fromUtf8("run"))
        self.run.triggered.connect(self.defaultRun)
        self.run.setFont(font_A)
        self.run.setIcon(QtGui.QIcon('beau/train1.png'))

        self.predict = QtGui.QAction(MainWindow)
        self.predict.setObjectName(_fromUtf8("predict"))
        self.predict.triggered.connect(self.run_predict)
        self.predict.setFont(font_A)
        self.predict.setIcon(QtGui.QIcon('beau/train2.png'))

        self.read_model = QtGui.QAction(MainWindow)
        self.read_model.setObjectName(_fromUtf8("read_model"))
        self.read_model.triggered.connect(self.readmodel)
        self.read_model.setFont(font_A)

        self.clear_history = QtGui.QAction(MainWindow)
        self.clear_history.setObjectName(_fromUtf8("clear"))
        self.clear_history.triggered.connect(self.textBrowser.clear)
        self.clear_history.setFont(font_A)
        self.clear_history.setIcon(QtGui.QIcon('beau/clear1.png'))

        self.Load.addAction(self.open_with_label)
        self.Load.addAction(self.open_with_desc)
        self.Load.addAction(self.open_mat)

        self.about_predict.addAction(self.open_with_features)
        self.about_predict.addAction(self.read_model)

        self.File.addAction(self.Load.menuAction())
        self.File.addAction(self.about_predict.menuAction())
        self.File.addAction(self.save_action)

        self.SVM.addAction(self.linear)
        self.SVM.addAction(self.rbf)

        self.ALG.addAction(self.SVM.menuAction())
        self.ALG.addAction(self.knn)
        self.ALG.addAction(self.cnn)

        self.Feature_select.addAction(self.ttest_action)
        self.Feature_select.addAction(self.pca_action)
        self.Feature_select.addAction(self.elastic)
        self.Feature_select.addAction(self.Fisher_score)
        self.Feature_select.addAction(self.rf_model)
        self.Feature_select.addAction(self.lasso_action)

        self.Pre_Process.addAction(self.replace_nan)
        self.Pre_Process.addAction(self.norm_action)
        self.Pre_Process.addAction((self.min_max_action))

        self.Visualization.addAction(self.plot_action)
        self.Visualization.addAction(self.ROC_action)
        self.Visualization.addAction(self.plot_brain_action)

        # ToDo
        self.HELP.addAction(self.about_software)
        self.HELP.addAction(self.about_ALG)

        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Pre_Process.menuAction())
        self.menubar.addAction(self.Feature_select.menuAction())
        self.menubar.addAction(self.ALG.menuAction())
        self.menubar.addAction(self.Visualization.menuAction())
        self.menubar.addAction(self.HELP.menuAction())

        # 将上面写好的action添加到工具栏中
        self.toolBar.addAction(self.run)
        self.toolBar.addAction(self.predict)
        self.toolBar.addAction(self.clear_history)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textBrowser.append('Welcome to BrainSort！\n')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BrainSort", None))

        self.label_accuracy.setText(_translate("MainWindow", "Accuracy", None))
        self.label_sensitivity.setText(_translate("MainWindow", "Sensitivity", None))
        self.label_specificity.setText(_translate("MainWindow", "Specificity", None))

        self.File.setTitle(_translate("MainWindow", "File", None))
        self.ALG.setTitle(_translate("MainWindow", "Algorithm", None))
        self.about_predict.setTitle('Predict')
        self.Feature_select.setTitle(_translate("MainWindow", "Features", None))
        self.Pre_Process.setTitle(_translate("MainWindow", "Preprocess", None))
        self.Visualization.setTitle(_translate("MainWindow", "Visualization", None))
        self.Load.setTitle(_translate("MainWindow", "Load", None))
        self.SVM.setTitle(_translate("MainWindow", "SVM", None))
        self.HELP.setTitle(_translate("MainWindow", "Help", None))

        self.toolBar.setWindowTitle(_translate("MainWindow", "ToolBar", None))

        self.open_with_label.setText(_translate("MainWindow", "with label", None))
        self.open_with_desc.setText(_translate("MainWindow", "with desc", None))
        self.open_mat.setText(_translate("MainWindow", "mat data", None))
        self.open_with_features.setText(_translate("MainWindow", "only feature", None))
        self.save_action.setText(_translate("MainWindow", "Save", None))

        self.knn.setText(_translate("MainWindow", "KNN", None))
        self.cnn.setText(_translate("MainWindow", "CNN", None))
        self.linear.setText(_translate("MainWindow", "Linear", None))
        self.rbf.setText(_translate("MainWindow", "RBF", None))

        self.ttest_action.setText(_translate("MainWindow", "TTest", None))
        self.lasso_action.setText(_translate("MainWindow", "Lasso", None))
        self.rf_model.setText(_translate("MainWindow", "Random Forest", None))
        self.Fisher_score.setText(_translate("MainWindow", "Fisher score", None))
        self.elastic.setText(_translate("MainWindow", "Elastic Network", None))
        self.norm_action.setText(_translate("MainWindow", "Normalize", None))
        self.min_max_action.setText(_translate("MainWindow", "Min-Max Scaler", None))

        self.replace_nan.setText(_translate("MainWindow", "Missing Value", None))
        self.pca_action.setText(_translate("MainWindow", "PCA", None))

        self.about_software.setText(_translate("MainWindow", "About Software", None))
        self.about_ALG.setText(_translate("MainWindow", "About Creator", None))

        self.run.setText(_translate("MainWindow", "train", None))
        self.predict.setText(_translate("MainWindow", "predict", None))
        self.read_model.setText(_translate("MainWindow", "load model", None))
        self.clear_history.setText(_translate("MainWindow", "clear", None))
        self.plot_action.setText((_translate("MainWwindow", "Top K", None)))
        self.ROC_action.setText((_translate("MainWwindow", "ROC", None)))
        self.plot_brain_action.setText((_translate("MainWwindow", "3D Brain", None)))

    # -------------------------------------------------------------------------------
    # 数据读取
    def openmat(self):
        self.hasPCA = False
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Load Data', '/home')
        self.filepath = str(filename)

        self.nw_data, self.nw_label = load_mat(str(filename))
        sample, height, width, channels = np.shape(self.nw_data)

        # 读取数据时默认选择了所有列作为特征
        self.textBrowser.append(str("Load Successfully."))
        self.textBrowser.append(str("Data size：%s samples, Feature shape: %s × %s × %s " %(sample, height, width, channels)))

    def open_withdesc(self):
        self.hasPCA = False
        self.k_desc = Ui_Dialog_k_desc()
        if self.k_desc.exec():
            try:
                k = int(self.k_desc.lineEdit.text())
            except:
                self.textBrowser.append('Wrong Format!\n')
                return

        filename = QtGui.QFileDialog.getOpenFileName(self, 'Load Data', '/home')
        self.filepath = str(filename)

        data = load_txt(str(filename))
        row, col = np.shape(data)

        labels_1 = [1] * k
        labels_2 = [-1] * (row - k)
        labels_1.extend(labels_2)
        labels = np.array(labels_1).reshape((row, -1))

        self.loaded_data = np.hstack((labels, data))
        self.index = [i + 1 for i in range(col)]
        # 读取数据时默认选择了所有列作为特征

        row, col = self.loaded_data.shape

        self.textBrowser.append(str("Load Successfully."))
        self.textBrowser.append(str("Data size: " + str(row) + " rows, " + str(col) + " columns"))
        self.textBrowser.append(str("Note：The first column is label information.\n"))
        del data

    def open_withlabel(self):
        self.hasPCA = False
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Load Data', '/home')
        self.filepath = str(filename)

        data = load_txt(str(filename))
        row, col = np.shape(data)

        # 深度拷贝
        self.origin_data = copy.deepcopy(data)
        self.loaded_data = copy.deepcopy(data)

        self.index = [i + 1 for i in range(col - 1)]
        # 读取数据时默认选择了所有列作为特征
        self.textBrowser.append(str("Load Successfully."))
        self.textBrowser.append(str("Data size: " + str(row) + " Rows, " + str(col) + " Columns"))
        self.textBrowser.append(str("Note：The first column is label information(+1 and -1).\n"))
        del data

    def open_features(self):

        filename = QtGui.QFileDialog.getOpenFileName(self, 'Load Features', 'D:\BrainSort_features')
        filepath = str(filename)
        print(filepath)
        data = load_txt(filepath)
        row, col = np.shape(data)

        self.feature_mat = data

        # 读取数据时默认选择了所有列作为特征
        self.textBrowser.append(str("Load Successfully."))
        self.textBrowser.append(str("It's feature matrix with " + str(row) + " rows and " + str(col) + " columns.\n"))

        filepath = filepath.split('/')
        filename = filepath.pop()
        self.predict_label_path = '/'.join(filepath)
        print(self.predict_label_path)

        name = filename.split('.')
        houzhui = name.pop()
        name = ''.join(name)
        self.predict_label_filename = name+'_predict_label'+'.'+houzhui

        del data

    # -------------------------------------------------------------------------------
    # 模型保存与读取
    def savemodel(self):
        if not hasattr(self, 'clf'):
            self.textBrowser.append(str("There is no model now!\n"))
            return
        file_path = QtGui.QFileDialog.getSaveFileName(self, "Save Algorithm Model ", r"D:\BrainSort_workspace",
                                                      "model(*.model)")
        file_path = file_path.split('.')
        file_path.pop()
        r = '/'.join(file_path)
        print(r)

        if not os.path.exists(r):
            os.makedirs(r)
        else:
            self.textBrowser.append('The folder already exists!\n')
            return

        r = r.split('/')
        file_name = r[-1] + '.model'
        print(file_name)
        r = '/'.join(r)
        file_path = r + '/' + file_name
        # 绝对路径

        try:
            joblib.dump(self.clf, str(file_path))
            self.textBrowser.append(str("Save Algorithm Model Successfully!\n"))
        except:
            self.textBrowser.append(str("Save Algorithm Model Failed!\n"))

        feature_index = [(i - 1) for i in self.index]

        # 保存列坐标时，由于之前特征挑选方法得到的都是在第一列是label时的下标，故在此统一减1
        np.savetxt(r + '/' + 'feature_index.txt', feature_index, fmt='%d')
        np.savetxt(r + '/' + 'raw_data.txt', self.origin_data[:, feature_index])
        # 注意：之前保存的index都是带标签列坐标，但是在读取的时候是不带类别标签的特征矩阵
        # 所以要将index转化为特征矩阵中的列坐标

        if not self.hasPCA:
            return

        file_path = r + '/' + 'PCA.model'
        try:
            joblib.dump(self.pca_model, str(file_path))
            self.textBrowser.append(str("Save PCA Model Successfully.\n"))
        except:
            self.textBrowser.append(str("Save PCA Model Failed.\n"))

    def readmodel(self):
        if hasattr(self,'for_predict_pca_model'):
            # 连续读取模型时，若不加判断会 Fault
            del self.for_predict_pca_model

        elif hasattr(self,'for_predict_clf'):
            del self.for_predict_clf

        filename = QtGui.QFileDialog.getOpenFileName(self, 'Load Algorithm Model', 'D:\BrainSort_workspace')
        filepath = str(filename)
        print(filepath)
        self.for_predict_clf = joblib.load(filepath)
        self.textBrowser.append(str('Load Algorithm Model Successfully!\n'))

        filepath = filepath.split('/')
        filepath.pop()
        r = '/'.join(filepath)
        print(r)

        feature_index_path = r + '/feature_index.txt'
        raw_data_path = r + '/raw_data.txt'
        pca_model_path = r + '/PCA.model'

        if os.path.exists(pca_model_path):
            self.for_predict_pca_model = joblib.load(pca_model_path)
            self.textBrowser.append('Load pca model successfully!\n')
        elif os.path.exists(feature_index_path):
            index = np.loadtxt(fname=feature_index_path)

            self.for_predict_index = [int(i) for i in list(index)]

            self.textBrowser.append('Load index successfully.\n')
            print(type(self.for_predict_index), self.for_predict_index)

        if os.path.exists(raw_data_path):
            self.for_predict_raw_data = np.loadtxt(fname=raw_data_path)
            # 注意这里的就是选中的那些特征矩阵，不需要任何变换
            self.textBrowser.append('load raw_data successfully.')

    # -------------------------------------------------------------------------------
    def defaultRun(self):
        if self.filepath == "":
            self.textBrowser.append(str('No Data Now!\n'))
        else:
            self.textBrowser.append(str('No Algorithm Now!\n'))
    # -------------------------------------------------------------------------------
    # 预处理函数

    def run_norm(self):
        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
            return
        self.loaded_data = Norm(self.loaded_data)
        self.textBrowser.append(str('Normalized.\n'))

    def run_min_max(self):
        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
            return
        self.loaded_data = Min_Max(self.loaded_data)
        self.textBrowser.append(str('Min-Max Normalized.\n'))

    def run_replace_nan(self):
        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
            return
        self.loaded_data = replace_nan(self.loaded_data)
        self.textBrowser.append(str('Replace Nan and Inf with the mean of that column.\n'))
    # -------------------------------------------------------------------------------
    # 特征选择函数
    # 这几种是直接在处理函数中启动参数接受窗口,获取参数后调用self_functions文件夹下的自定义函数

    def run_ttest(self):
        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
            return

        self.TTest_D = Ui_Dialog_TTest()

        if self.TTest_D.exec_():
            print('Click OK')

            try:
                temp = float(self.TTest_D.lineEdit.text())
                print(temp)
                self.loaded_data, self.index = TTest(self.loaded_data, temp)
                self.textBrowser.append(str("Threshold=" + str(self.TTest_D.lineEdit.text())))
                self.textBrowser.append(str('There are ' + str(len(self.index)) + ' columns choosed:'))

            except:
                self.textBrowser.append(str("Wrong Format，Threshold = 0.01"))
                self.loaded_data = TTest(self.loaded_data, 0.01)
                self.loaded_data, self.index = TTest(self.loaded_data)
                self.textBrowser.append(str('There are ' + str(len(self.index)) + ' columns choosed:'))

            finally:

                result = ''
                for item in self.index:
                    result += str(item)
                    result += ' '
                self.textBrowser.append(str(result))
                self.textBrowser.append(str('Note：The column is label information.\n'))
                return
        else:
            print('Click cancel')
            self.textBrowser.append(str("You have exited the parameter settings interface.\n"))

    def run_rf_model(self):
        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
            return

        self.rf_D = Ui_Dialog_rf()

        if self.rf_D.exec_():
            print('Click OK')

            try:
                n_trees = int(self.rf_D.lineEdit_n_estimators.text())
                min_split = int(self.rf_D.lineEdit_min_samples_split.text())
                k_save = int(self.rf_D.lineEdit_k_save.text())
                print(n_trees, min_split, k_save)

            except:
                self.textBrowser.append(str("Wrong Fomat,Use default parameter now!"))
                n_trees = 10
                min_split = 3
                k_save = int(0.6 * np.shape(self.loaded_data)[1])
                self.textBrowser.append('n_trees:10')
                self.textBrowser.append('min_split:3')
                self.textBrowser.append('k_save:'+str(k_save))

            finally:
                self.loaded_data, self.index = rf_select(self.loaded_data, n_trees=n_trees, min_split=min_split,
                                                         k_save=k_save)
                self.textBrowser.append(str('Choosed Columns are :' + str(len(self.index)) + ''))
                result = ''
                for item in self.index:
                    result += str(item)
                    result += ' '
                self.textBrowser.append(str(result))
                return

    def run_Fisher_score(self):
        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
            return

        self.Fisher_score_D = Ui_Dialog_Fisher_score()

        if self.Fisher_score_D.exec_():
            print('Click OK')

            try:
                temp = float(self.Fisher_score_D.lineEdit.text())
                print(temp)
                self.loaded_data, self.index = Fisher_score(self.loaded_data, temp)
                self.textBrowser.append(str("Threshold=" + str(self.Fisher_score_D.lineEdit.text())))
                self.textBrowser.append(str('There are ' + str(len(self.index)) + ' columns choosed:'))

            except:
                self.textBrowser.append(str("Wrong Format，p=0.1"))
                self.loaded_data, self.index = Fisher_score(self.loaded_data, p=0.1)
                self.textBrowser.append(str('There are ' + str(len(self.index)) + ' columns choosed:'))

            finally:

                result = ''
                for item in self.index:
                    result += str(item)
                    result += ' '
                self.textBrowser.append(str(result))
                self.textBrowser.append(str('Note：The 1th column is label.\n'))
                return

    def run_lasso(self):
        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
            return

        self.lasso_D = Ui_Dialog_lasso()

        if self.lasso_D.exec_():
            print('Click OK')

            try:
                alpha = float(self.lasso_D.lineEdit_alpha.text())
                print(alpha)

                loop_num = int(self.lasso_D.lineEdit_loop_num.text())
                print(loop_num)

                self.loaded_data, self.index = lasso(self.loaded_data, alpha, loop_num)
                self.textBrowser.append(str("alpha = " + str(alpha)))
                self.textBrowser.append(str("loop = " + str(loop_num)))
                self.textBrowser.append(str('There are ' + str(len(self.index)) + ' columns choosed:'))

            except:
                self.textBrowser.append(str("Wrong Format，alpha=0.01, loop=50"))
                self.loaded_data, self.index = lasso(self.loaded_data, 0.01, 50)
                self.textBrowser.append(str('There are ' + str(len(self.index)) + ' columns choosed:'))

            finally:

                result = ''
                for item in self.index:
                    result += str(item)
                    result += ' '
                self.textBrowser.append(str(result))
                self.textBrowser.append(str('Note：The 1th column is label.\n'))
                return

    def run_pca(self):

        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
        else:

            features, labels = div_label_feature(self.loaded_data)

            pca = PCA(n_components=0.9, copy=False, whiten=False, svd_solver='full')
            features = pca.fit_transform(X=features)

            self.pca_model = pca
            self.loaded_data = np.hstack((np.reshape(a=labels, newshape=(len(labels), 1)), features))

            self.textBrowser.append(str("The numbes of features turn to %s \n" % str(np.shape(self.loaded_data)[1]-1)))
            self.hasPCA = True


    def run_predict(self):
        if hasattr(self, 'for_predict_clf') and hasattr(self, 'feature_mat'):

            model = self.for_predict_clf
            raw_data = replace_nan(self.for_predict_raw_data)
            row_raw, col_raw = raw_data.shape
            self.feature_mat = replace_nan(self.feature_mat)

            if hasattr(self, 'for_predict_pca_model'):
                # 如果是含有pca降维方法的
                together_data = np.vstack((raw_data, self.feature_mat))
                res = Norm_features(together_data)
                feature_mat = res[row_raw:, :]

                pca = self.for_predict_pca_model
                predict_data = pca.transform(feature_mat)
                print('predict_data', predict_data.shape)
                labels = model.predict(predict_data)
            else:
                # 如果没有PCA降维
                # print(type(raw_data))
                predict_data = self.feature_mat[:, self.for_predict_index]
                together_data = np.vstack((raw_data, predict_data))
                res = Norm_features(together_data)
                feature_mat = res[row_raw:, :]
                labels = model.predict(feature_mat)

            print('predict_data', predict_data.shape)
            labels = [int(i) for i in labels]

            name = self.predict_label_filename.split('.')
            name = name[0]
            np.savetxt(self.predict_label_path + '/' +name+'_'+time.strftime('%H%M%S',time.localtime())+'.txt', labels,fmt='%d')
            labels = [str(i) for i in labels]
            self.textBrowser.append('Predict label are:')
            result = ' '.join(labels)
            self.textBrowser.append(result)
            self.textBrowser.append('Save labels successfully.\n')
        else:
            self.textBrowser.append('Load model and feature mat first!\n')

    def linear_svm_selectC(self):
        print('Grid Searching···')
        C = range(1, 1000, 10)
        parameter = {'C': C}
        svc = svm.LinearSVC()
        features, labels = div_label_feature(self.loaded_data)
        clf = GridSearchCV(svc, parameter)
        clf.fit(features, labels)
        self.textBrowser.append(str("Best Value is " + str(clf.best_params_)))

    # -------------------------------------------------------------------------------
    def plot(self):

        if hasattr(self, 'origin_coef'):
            weight = self.sorted_weight_percentage
            name = self.sorted_brain_name
            index = self.brain_weight_index
            print('index', index)
        else:
            self.textBrowser.append(str("No Weights Now!\n"))
            return

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x(), 1.03 * height, "%.3f" % float(height))

        self.plot_D = Ui_Dialog_plot()
        if self.plot_D.exec_():
            print('Click OK')
            try:
                k_save = int(self.plot_D.lineEdit_k.text())
                if k_save >= 20 or k_save == 0:
                    k_save = 20
                weight = weight[:k_save]
                name = name[:k_save]
                index = index[:k_save]
                # 这种截取的方式是深复制
            except:
                self.textBrowser.append('Wrong!\n')
                return
        else:
            return
        total = sum(weight)
        print('total',total)
        weight = [item / total for item in weight]
        print('weight',weight)
        self.ax = self.plot_widget.figure.add_subplot(111)
        self.ax.hold(False)

        rect = self.ax.bar(left=list(range(len(weight))), height=weight, align='center', width=0.8, yerr=0.001,color='#14C9FA')
        autolabel(rect)
        plt.title('Top Brain Regions')
        plt.xlabel('Brain Region Index')
        plt.ylabel('Contribution')
        index = [i+1 for i in index]
        plt.xticks(list(range(len(index))), index)

        self.plot_widget.canvas.draw()
        self.textBrowser.append(str("Draw successfully\n"))

    def plot_ROC(self):

        if hasattr(self, 'true_label'):
            self.ax = self.plot_widget.figure.add_subplot(111)
            self.ax.hold(False)
            false_positive_rate, true_positive_rate, thresholds = roc_curve(self.true_label, self.predict_prob)
            roc_auc = auc(false_positive_rate, true_positive_rate)
            plt.title('ROC Curve')
            plt.plot(false_positive_rate, true_positive_rate, '#1EACF6', label='AUC = %0.2f' % roc_auc)
            plt.legend(loc='lower right')
            self.ax.hold(True)
            plt.plot([0, 1], [0, 1],'--',color = '#ff5722')
            plt.xlim([-0.01, 1.01])
            plt.ylim([-0.01, 1.01])
            plt.ylabel('True Positive Rate')
            plt.xlabel('False Positive Rate')
            self.plot_widget.canvas.draw()
        else:
            self.textBrowser.append(str("Can't Draw!\n"))

    def plot_brain(self):

        triangular_mesh(self.coord[0, :], self.coord[1, :], self.coord[2, :], self.tri, opacity=0.7,
                        color=(0.6, 0.6, 0.6))

        if hasattr(self, 'brain_weight'):
            print('Plot processing')
            max_contribution = max(self.brain_weight)
            k = 10 / max_contribution
            print('k', k)
            self.sizes = np.array([item * k for item in self.brain_weight])
            print('sizes', self.sizes)
            points3d(self.x, self.y, self.z, self.sizes)

        show()

    # -------------------------------------------------------------------------------
    # 这几种是先启动窗口获取参数再调用对应的处理函数
    def linear_D(self):
        if self.filepath == "":
            self.textBrowser.append(str("No Data Now!\n"))
            return

        self.linear_D = Ui_Dialog()
        self.run.triggered.disconnect()

        if self.linear_D.exec_():
            print('Click OK')

            if self.linear_D.lineEdit.text() == 'auto':
                self.textBrowser.append(str("Use Parameter Grid Search.\n"))
                self.run.triggered.connect(self.linear_svm_selectC)
                return

            try:
                c = float(self.linear_D.lineEdit.text())
                k = int(self.linear_D.lineEdit_p.text())
                self.run.triggered.connect(lambda: self.run_svm(C=c, k=k))
                self.textBrowser.append(str("C=" + str(c)))
                self.textBrowser.append(str("K=" + str(k)+'\n'))
                return

            except:
                self.textBrowser.append(str("Wrong Format,Use default parameter."))
                self.run.triggered.connect(lambda: self.run_svm())
                return
        else:
            print('Click cancel')
            self.textBrowser.append(str("Re-select Algorithm.\n"))
            self.run.triggered.connect(self.defaultRun)

    def run_svm(self, C=1.0, k=3):
        accuracy_all, true_p_all, true_n_all, false_p_all, false_n_all = (0, 0, 0, 0, 0)

        features, labels = div_label_feature(self.loaded_data)
        coef_all = np.zeros((k, features.shape[1]))
        coef_index = 0
        kf = KFold(n_splits=k, shuffle=True)
        max_accuracy = 0
        for train_index, test_index in kf.split(features):

            train_data = features[train_index]
            train_label = labels[train_index]
            test_data = features[test_index]
            test_label = labels[test_index]

            clf = svm.LinearSVC(C=C)

            clf.fit(X=train_data, y=train_label)
            self.clf = clf

            predict_label = clf.predict(test_data)
            predict_prob = clf.decision_function(X=test_data)
            print('predict_prob', predict_prob)
            accuracy, true_p, true_n, false_p, false_n = get_result(test_label, predict_label)

            if accuracy > max_accuracy:
                self.true_label = test_label
                self.predict_prob = predict_prob

            accuracy_all += accuracy
            true_p_all += true_p
            true_n_all += true_n
            false_p_all += false_p
            false_n_all += false_n

            coef_all[coef_index, :] = clf.coef_[0]
            coef_index += 1

        self.origin_coef = sum(coef_all) / k
        # 选中的列的系数

        if self.hasPCA == True:
            print('PCA processing')
            self.origin_coef = self.pca_model.inverse_transform(self.origin_coef)

        self.abs_coef = [abs(i) for i in list(self.origin_coef)]
        print(len(self.abs_coef))
        # 绝对值化
        self.brain_weight = [0] * 90
        # 用于存放每个脑区的总贡献

        coef_index = 0
        for i in self.index:
            self.brain_weight[(i % 90) -1] += self.abs_coef[coef_index]
            coef_index += 1
        # 注意，这里的index是从1开始的，而特征1应该放在brain——weight中的下标0位置
        # 现在得到的brain_weight是对应脑区的abs(系数）累加，下面对其进行归一化
        total = sum(self.brain_weight)
        self.brain_weight = [item / total for item in self.brain_weight]

        # 以上得到了90个脑区的贡献度
        self.brain_weight_index = list(np.argsort(self.brain_weight))
        self.brain_weight_index.reverse()
        # 这个index范围为0~89,0对应脑区1
        # print('self.brain_weight_index',self.brain_weight_index)

        self.sorted_brain_weight = [self.brain_weight[i] for i in self.brain_weight_index]

        total = sum(self.sorted_brain_weight)
        self.sorted_weight_percentage = [round(item / total, 4) for item in self.sorted_brain_weight]

        self.sorted_brain_name = [self.feature_name[i] for i in self.brain_weight_index]

        for i in range(len(self.brain_weight)):
            if self.brain_weight_index[i]+1<10:
                temp = '%-3s %-20s'%(str('0'+str(self.brain_weight_index[i]+1)),str(self.sorted_brain_name[i]))
                res = temp
                self.textBrowser.append(res)
                self.textBrowser.append('score : '+str(self.sorted_weight_percentage[i])+'\n')

            else:
                temp = '%-3s %-20s'%(str(self.brain_weight_index[i]+1),str(self.sorted_brain_name[i]))
                res = temp
                self.textBrowser.append(res)
                self.textBrowser.append('score : '+str(self.sorted_weight_percentage[i])+'\n')


        self.textBrowser.append('\nGet result!\n')

        self.clf = svm.LinearSVC(C=C).fit(features, labels)

        self.lineEdit_accuracy.setText(str(round(accuracy_all / k,3)))
        self.lineEdit_specificity.setText(str( round(float(true_p_all) / (false_n_all + true_p_all),3)) )
        self.lineEdit_sensitivity.setText(str( round(float(true_n_all) / (true_n_all + false_p_all),3)) )

    def knn_D(self):
        if self.filepath == "":
            self.textBrowser.append(str("No Data Now!\n"))
            return

        self.knn_D = Ui_Dialog_KNN()
        self.run.triggered.disconnect()

        if self.knn_D.exec_():
            print('Click OK')

            try:
                k = int(self.knn_D.lineEdit.text())
            except:
                k = 5
            try:
                p = int(self.knn_D.lineEdit_p.text())
            except:
                p = 2

            w = str(self.knn_D.lineEdit_w.text())
            if w not in ['uniform', 'distance']:
                w = 'uniform'

            try:
                kf = int(self.knn_D.lineEdit_kf.text())
            except:
                kf = 3
            self.run.triggered.connect(lambda: self.run_knn(k=k, p=p, w=w, kf=kf))
            self.textBrowser.append(str("k=" + str(k)))
            self.textBrowser.append(str("p=" + str(p)))
            self.textBrowser.append(str("w=" + w))
            self.textBrowser.append(str("k_fold=" + str(kf)))

        else:
            print('Click cancel')
            self.textBrowser.append(str("Re-select Algorithm.\n"))
            self.run.triggered.connect(self.defaultRun)

    def run_knn(self, k=3, p=2, w='uniform', kf=3):
        accuracy_all, true_p_all, true_n_all, false_p_all, false_n_all = (0, 0, 0, 0, 0)

        features, labels = div_label_feature(self.loaded_data)
        kfold = KFold(n_splits=kf, shuffle=True)
        max_accuracy = 0
        for train_index, test_index in kfold.split(features):

            train_data = features[train_index]
            train_label = labels[train_index]
            test_data = features[test_index]
            test_label = labels[test_index]

            clf = KNeighborsClassifier(n_neighbors=k, p=p, weights=w)
            clf.fit(X=train_data, y=train_label)
            self.clf = clf

            predict_label = clf.predict(test_data)

            accuracy, true_p, true_n, false_p, false_n = get_result(test_label, predict_label)
            if accuracy > max_accuracy:
                self.true_label = test_label
                self.predict_prob = predict_label
            accuracy_all += accuracy
            true_p_all += true_p
            true_n_all += true_n
            false_p_all += false_p
            false_n_all += false_n

        self.clf = KNeighborsClassifier(n_neighbors=k, p=p, weights=w).fit(features, labels)
        self.lineEdit_accuracy.setText(str(round(accuracy_all / kf, 3)))
        self.lineEdit_specificity.setText(str( round( float(true_p_all) / (false_n_all + true_p_all), 3)))
        self.lineEdit_sensitivity.setText(str( round( float(true_n_all) / (true_n_all + false_p_all), 3)))

        self.textBrowser.append(str("This training has been completed.\n"))

    def cnn_D(self):
        if self.filepath == "":
            self.textBrowser.append(str("No Data Now!\n"))
            return

        self.cnn_D = Ui_Dialog_CNN()
        self.run.triggered.disconnect()

        if self.cnn_D.exec_():
            print('Click OK')
            args = {'kfold': 3,
                    'batch_size': 10,
                    'epoch': 1,
                    'learning_rate': 0.01,
                    'cov1': [5, 5, 64, 1, 1],
                    'pool1': [3, 3, 2, 2],
                    'cov2': [5, 5, 64, 1, 1],
                    'pool2': [3, 3, 2, 2],
                    'fc1_num': 128,
                    'fc2_num': 32,
                    }
            try:
                kfold = int(self.cnn_D.kfold.text())
                args['kfold'] = kfold
            except:
                print('kfold Fault')

            try:
                batch_size = int(self.cnn_D.batch.text())
                args['batch_size'] = batch_size
            except:
                print('batch_size Fault')

            try:
                epoch = int(self.cnn_D.epoch.text())
                args['epoch'] = epoch
            except:
                print('epoch Fault')

            try:
                learning_rate = float(self.cnn_D.learning_rate.text())
                args['learning_rate'] = learning_rate
            except:
                print('learning_rate Fault')

            try:
                fc1_num = int(self.cnn_D.fc1.text())
                args['fc1_num'] = fc1_num
            except:
                print('fc1_num Fault')

            try:
                fc2_num = int(self.cnn_D.fc2.text())
                args['fc2_num'] = fc2_num
            except:
                print('fc2_num Fault')

            try:
                cov1 = self.cnn_D.cov1.text().strip().split(' ')
                cov1 = [int(item) for item in cov1]
                args['cov1'] = cov1
            except:
                print('cov1 Fault')

            try:
                cov2 = self.cnn_D.cov2.text().strip().split(' ')
                cov2 = [int(item) for item in cov2]
                args['cov2'] = cov2
            except:
                print('cov2 Fault')

            try:
                pool1 = self.cnn_D.pool1.text().strip().split(' ')
                pool1 = [int(item) for item in pool1]
                args['pool1'] = pool1
            except:
                print('pool1 Fault')

            try:
                pool2 = self.cnn_D.pool1.text().strip().split(' ')
                pool2 = [int(item) for item in pool2]
                args['pool2'] = pool2
            except:
                print('pool2 Fault')

            self.run.triggered.connect(lambda: self.run_cnn(args=args))
            print(args)
            self.textBrowser.append(str("CNN para confirmed.\n"))
            self.textBrowser.append(str("K Fold = %s.\n" % args['kfold']))
            self.textBrowser.append(str("Epoch = %s.\n" % args['epoch']))
            self.textBrowser.append(str("Batch = %s.\n" % args['batch_size']))
            self.textBrowser.append(str("Learning rate = %s.\n" % args['learning_rate']))
            self.textBrowser.append(str("Model training....\n"))

        else:
            print('Click cancel')
            self.textBrowser.append(str("Select algorithm option.\n"))
            self.run.triggered.connect(self.defaultRun)

    def run_cnn(self, args):
        print(args)
        kfold = args['kfold']
        batch_size = args['batch_size']
        epoch = args['epoch']
        learning_rate = args['learning_rate']

        conv1 = args['cov1']
        cvl1_k = conv1[0:3]  # 5 5 64
        cvl1_s = conv1[3:]  # 1 1

        pool1 = args['pool1']
        pool1_shape = pool1[0:2] # 3 3
        pool1_stride = pool1[2:]  # 2 2

        conv2 = args['cov2']
        cvl2_k = conv1[0:3]  # 5 5 64
        cvl2_s = conv1[3:]  # 1 1

        pool2 = args['pool2']
        pool2_shape = pool1[0:2] # 3 3
        pool2_stride = pool1[2:]  # 2 2

        fc1_num = args['fc1_num']
        fc2_num = args['fc2_num']

        accuracy_all, true_p_all, true_n_all, false_p_all, false_n_all = (0, 0, 0, 0, 0)

        features, labels = self.nw_data, self.nw_label
        print('feature', features.shape, 'label', labels.shape)

        kfold_model = KFold(n_splits=kfold, shuffle=True)

        max_accuracy = 0
        for train_index, test_index in kfold_model.split(features):

            train_data = features[train_index]
            train_label = labels[train_index]
            test_data = features[test_index]
            test_label = labels[test_index]

            # 下面搭建模型和训练模型
            with tf.Graph().as_default():
                sess = tf.InteractiveSession()  # 创建默认的Interactive Session
                max_steps = int(train_data.shape[0] / batch_size)

                def variable_with_weight_loss(shape, stddev, wl):  # 权重及初始化-截断的正态分布
                    var = tf.Variable(tf.truncated_normal(shape, stddev=stddev))
                    if wl is not None:
                        weight_loss = tf.multiply(tf.nn.l2_loss(var), wl, name='weight_loss')  # l2正则化项
                        tf.add_to_collection('losses', weight_loss)
                    return var

                def loss(logits, labels):
                    #      """Add L2Loss to all the trainable variables.
                    #      Add summary for "Loss" and "Loss/avg".
                    #      Args:
                    #        logits: Logits from inference().
                    #        labels: Labels from distorted_inputs or inputs(). 1-D tensor
                    #                of shape [batch_size]
                    #      Returns:
                    #        Loss tensor of type float.
                    #      """
                    #      # Calculate the average cross entropy loss across the batch.
                    labels = tf.cast(labels, tf.int64)
                    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
                        logits=logits, labels=labels, name='cross_entropy_per_example')
                    cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy')
                    tf.add_to_collection('losses', cross_entropy_mean)

                    # The total loss is defined as the cross entropy loss plus all of the weight
                    # decay terms (L2 loss).

                    return tf.add_n(tf.get_collection('losses'), name='total_loss')

                sample_count, channels1, channels2, band_num = train_data.shape
                image_holder = tf.placeholder(tf.float32, [batch_size, channels1, channels2, band_num])
                label_holder = tf.placeholder(tf.int32, [batch_size])

                # 卷积层
                weight1 = variable_with_weight_loss(shape=[cvl1_k[0], cvl1_k[1], band_num, cvl1_k[2]], stddev=5e-2, wl=0.0)
                kernel1 = tf.nn.conv2d(image_holder, weight1, [1, cvl1_s[0], cvl1_s[1], 1], padding='SAME')
                bias1 = tf.Variable(tf.constant(0.0, shape=[cvl1_k[2]]))
                conv1 = tf.nn.relu(tf.nn.bias_add(kernel1, bias1))

                # 池化层
                pool1 = tf.nn.max_pool(conv1, ksize=[1, pool1_shape[1], pool1_shape[1], 1], strides=[1, pool1_stride[0], pool1_stride[1], 1],
                                       padding='SAME')
                # LRN层
                norm1 = tf.nn.lrn(pool1, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75)

                # 卷积层
                weight2 = variable_with_weight_loss(shape=[cvl2_k[0], cvl2_k[1], cvl1_k[2], cvl2_k[2]], stddev=5e-2, wl=0.0)
                kernel2 = tf.nn.conv2d(norm1, weight2, [1, cvl2_s[0], cvl2_s[1], 1], padding='SAME')
                bias2 = tf.Variable(tf.constant(0.1, shape=[cvl2_k[2]]))
                conv2 = tf.nn.relu(tf.nn.bias_add(kernel2, bias2))

                # LRN层
                norm2 = tf.nn.lrn(conv2, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75)

                # 池化层
                pool2 = tf.nn.max_pool(norm2, ksize=[1, pool2_shape[0], pool2_shape[1], 1], strides=[1, pool2_stride[0], pool2_stride[1], 1],
                                       padding='SAME')

                # Reshape层
                reshape = tf.reshape(pool2, [batch_size, -1])  # flatten

                dim = reshape.get_shape()[1].value  # 获得数据长度

                # 全连接层
                weight3 = variable_with_weight_loss(shape=[dim, fc1_num], stddev=0.04, wl=0.004)  # 全连接层节点数
                bias3 = tf.Variable(tf.constant(0.1, shape=[fc1_num]))
                local3 = tf.nn.relu(tf.matmul(reshape, weight3) + bias3)

                # 全连接层
                weight4 = variable_with_weight_loss(shape=[fc1_num, fc2_num], stddev=0.04, wl=0.004)  # 全连接层
                bias4 = tf.Variable(tf.constant(0.1, shape=[fc2_num]))  # 全连接层节点数
                local4 = tf.nn.relu(tf.matmul(local3, weight4) + bias4)

                # 全连接层
                weight5 = variable_with_weight_loss(shape=[fc2_num, 2], stddev=1 / 192.0, wl=0.0)
                bias5 = tf.Variable(tf.constant(0.0, shape=[2]))
                logits = tf.add(tf.matmul(local4, weight5), bias5)

                loss = loss(logits, label_holder)

                train_op = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)  #优化器

                top_k_op = tf.nn.in_top_k(logits, label_holder, 1)  # 输出分类最高的准确率

                tf.global_variables_initializer().run()

                tf.train.start_queue_runners()  # 使用线程来进行加速
                #  以上搭建好了模型，接下来准备模型迭代训练
                ####################################################################################################
                true_count = 0
                flag = 0
                flag_l = 0
                loss_mat = np.zeros(int(max_steps + 1))
                for epoch_index in range(epoch):
                    for step in range(max_steps):
                        print('step=', step, 'max_step', max_steps)
                        start_time = time.time()
                        offset = (step * batch_size)  
                        batch_data = train_data[offset:(offset + batch_size)]
                        batch_label = train_label[offset:(offset + batch_size)]
                        if batch_data.shape[0] != batch_size:
                            continue
                        _, loss_value = sess.run([train_op, loss], feed_dict={image_holder: batch_data,
                                                                              label_holder: batch_label})


                        loss_mat[flag_l] = loss_value
                        flag_l += 1
                        duration = time.time() - start_time

                        if step % 2 == 0:
                            examples_per_sec = batch_size / duration
                            sec_per_batch = float(duration)

                            predictions, predict_logits = sess.run([top_k_op, logits], feed_dict={image_holder: batch_data,
                                                                                                  label_holder: batch_label})
                            true_count = np.sum(predictions)
                            precision = true_count / batch_size


                            format_str = (
                                'step %d, loss = %.2f (%.1f examples/sec; %.3f sec/batch), train_precision = %.3f')
                            print(format_str % (step, loss_value, examples_per_sec, sec_per_batch, precision))

            print('模型训练结束，开始预测')
            # 下面用训练好的模型进行预测
            num_iter = int(test_label.shape[0] / batch_size)
            print('num_iter', num_iter)

            true_count = 0
            total_sample_count = num_iter * batch_size
            step = 0
            print('test_data.shape', test_data.shape)

            true_label, predict_label = [], []

            while step <= num_iter - 1:
                print('true_count', true_count)
                offset = (step * batch_size)  
                batch_data = test_data[offset:(offset + batch_size)]
                batch_label = test_label[offset:(offset + batch_size)]

                print(batch_data.shape, batch_label.shape)
                # 获得真实标签
                if batch_data.shape[0] != batch_size:
                    continue


                true_label.extend(batch_label)

                predictions = sess.run([top_k_op], feed_dict={image_holder: batch_data,
                                                              label_holder: batch_label})
                print(predictions)
                predictions = predictions[0]
                # 获得模型的预测标签
                temp_predict_label = []
                for temp_index in range(predictions.shape[0]):
                    if predictions[temp_index]:
                        temp_predict_label.append(batch_label[temp_index])
                    else:
                        temp_predict_label.append(abs(1-batch_label[temp_index]))
                predict_label.extend(temp_predict_label)

                true_count += np.sum(predictions)
                step += 1

            precision_t = true_count / total_sample_count
            print('precision = %.3f' % precision_t)

            accuracy, true_p, true_n, false_p, false_n = get_result(test_label, predict_label, negative=0)

            if accuracy > max_accuracy:
                self.true_label = test_label
                self.predict_prob = predict_label

            accuracy_all += accuracy
            true_p_all += true_p
            true_n_all += true_n
            false_p_all += false_p
            false_n_all += false_n

        self.lineEdit_accuracy.setText(str(round(accuracy_all / kfold, 3)))
        self.lineEdit_specificity.setText(str(round(float(true_p_all) / (false_n_all + true_p_all), 3)))
        self.lineEdit_sensitivity.setText(str(round(float(true_n_all) / (true_n_all + false_p_all), 3)))

        self.textBrowser.append(str("This training has been completed.\n"))

    def rbf_D(self):
        if self.filepath == "":
            self.textBrowser.append("No Data Now!\n")
            return

        self.rbf_D = Ui_Dialog_rbf()
        self.run.triggered.disconnect()

        if self.rbf_D.exec_():
            print('Click OK')

            try:
                temp = float(self.rbf_D.lineEdit.text())
                k = int(self.rbf_D.lineEdit_p.text())
                self.run.triggered.connect(lambda: self.run_rbf(C=temp, k=k))
                self.textBrowser.append("C=" + str(temp))
                self.textBrowser.append("K=" + str(k))
                return

            except:
                self.textBrowser.append("Wrong Format,Use Default Parameter.\n")
                self.run.triggered.connect(lambda: self.run_rbf(C=1, k=3))
                return
        else:
            print('Click cancel')
            self.textBrowser.append("Re-select Algorithm.\n")
            self.run.triggered.connect(self.defaultRun)

    def run_rbf(self, C=1.0, k=3):
        accuracy_all, true_p_all, true_n_all, false_p_all, false_n_all = (0, 0, 0, 0, 0)
        accuracy_all, specificity_all, sensitivity_all = (0, 0, 0)

        features, labels = div_label_feature(self.loaded_data)

        coef_all = np.zeros((k, features.shape[1]))
        coef_index = 0
        kf = KFold(n_splits=k, shuffle=True)
        max_accuracy = 0
        for train_index, test_index in kf.split(features):

            train_data = features[train_index]
            train_label = labels[train_index]
            test_data = features[test_index]
            test_label = labels[test_index]

            clf = svm.SVC(C=C, kernel='rbf')
            clf.fit(X=train_data, y=train_label)

            predict_label = clf.predict(test_data)
            predict_prob = clf.decision_function(test_data)
            accuracy, true_p, true_n, false_p, false_n = get_result(test_label, predict_label)
            if accuracy > max_accuracy:
                self.true_label = test_label
                self.predict_prob = predict_prob
            accuracy_all += accuracy
            true_p_all += true_p
            true_n_all += true_n
            false_p_all += false_p
            false_n_all += false_n

        self.clf = svm.SVC(C=C, kernel='rbf').fit(features, labels)

        self.lineEdit_accuracy.setText( str( round(accuracy_all / k,3) ) )
        self.lineEdit_specificity.setText(str(round(  float(true_p_all) / (false_n_all + true_p_all),3)))
        self.lineEdit_sensitivity.setText(str( round( float(true_n_all) / (true_n_all + false_p_all),3 )))

        self.textBrowser.append(str("This training has been completed.\n"))

    def elastic_D(self):
        if self.filepath == "":
            self.textBrowser.append(str("No Data Now!"))
            return

        self.elastic_D = Ui_Dialog_elastic_network()

        if self.elastic_D.exec_():
            print('Click OK')

            try:
                alpha = float(self.elastic_D.lineEdit_alpha.text())
            except:
                alpha = 1.0
            try:
                l1_ratio = float(self.elastic_D.lineEdit_l1_ratio.text())
            except:
                l1_ratio = 0.5

            try:
                max_iter = int(self.elastic_D.lineEdit_max_iter.text())
            except:
                max_iter = 100

            try:
                tol = float(self.elastic_D.lineEdit_tol.text())
            except:
                tol = 0.1
            self.textBrowser.append(str("alpha=" + str(alpha)))
            self.textBrowser.append(str("l1_ratio=" + str(l1_ratio)))
            self.textBrowser.append(str("max_iter=" + str(max_iter)))
            self.textBrowser.append(str("tol=" + str(tol)+'\n'))
            self.run_elastic(alpha=alpha,l1_ratio=l1_ratio,max_iter=max_iter,tol=tol)

        else:
            print('Click cancel')
            self.textBrowser.append(str("Re-select Algorithm."))
            self.run.triggered.connect(self.defaultRun)

    def run_elastic(self, alpha, l1_ratio, max_iter, tol):
        if self.loaded_data == []:
            self.textBrowser.append(str('No Data Now!\n'))
            return
        ela = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, max_iter=max_iter, tol=tol)
        features, labels = div_label_feature(data=self.loaded_data)
        ela.fit(X=features, y=labels)
        self.index = [0]
        i = 1
        for item in ela.coef_:
            if item != 0:
                self.index.append(i)
            i += 1

        result = ''
        for item in self.index:
            if item != 0:
                result += str(item)
                result += ' '
        self.textBrowser.append('The Selected columns are:：' + result)
        self.textBrowser.append('There are ' + str((len(self.index)) - 1) + ' features\n')
        self.loaded_data = self.loaded_data[:, self.index]
        self.index.remove(0)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.setAutoFillBackground(True)

    win.show()
    sys.exit(app.exec_())
