# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Instance(object):
    def setupUi(self, Instance):
        Instance.setObjectName("Instance")
        Instance.resize(1054, 519)
        self.gridLayout_4 = QtWidgets.QGridLayout(Instance)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gb_coins = QtWidgets.QGroupBox(Instance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gb_coins.sizePolicy().hasHeightForWidth())
        self.gb_coins.setSizePolicy(sizePolicy)
        self.gb_coins.setObjectName("gb_coins")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gb_coins)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tree_coins = QtWidgets.QTreeWidget(self.gb_coins)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_coins.sizePolicy().hasHeightForWidth())
        self.tree_coins.setSizePolicy(sizePolicy)
        self.tree_coins.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tree_coins.setFont(font)
        self.tree_coins.setMidLineWidth(0)
        self.tree_coins.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tree_coins.setAlternatingRowColors(False)
        self.tree_coins.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tree_coins.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tree_coins.setIndentation(5)
        self.tree_coins.setColumnCount(4)
        self.tree_coins.setObjectName("tree_coins")
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_coins)
        self.tree_coins.header().setMinimumSectionSize(19)
        self.gridLayout_2.addWidget(self.tree_coins, 0, 0, 1, 5)
        self.lbl_utxos = QtWidgets.QLabel(self.gb_coins)
        self.lbl_utxos.setIndent(5)
        self.lbl_utxos.setObjectName("lbl_utxos")
        self.gridLayout_2.addWidget(self.lbl_utxos, 1, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.bt_donate_selected = QtWidgets.QPushButton(self.gb_coins)
        self.bt_donate_selected.setObjectName("bt_donate_selected")
        self.gridLayout_2.addWidget(self.bt_donate_selected, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)
        self.bt_donate_all = QtWidgets.QPushButton(self.gb_coins)
        self.bt_donate_all.setObjectName("bt_donate_all")
        self.gridLayout_2.addWidget(self.bt_donate_all, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 4, 1, 1)
        self.gridLayout_4.addWidget(self.gb_coins, 3, 1, 1, 1)
        self.gb_charities = QtWidgets.QGroupBox(Instance)
        self.gb_charities.setObjectName("gb_charities")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gb_charities)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tree_charities = QtWidgets.QTreeWidget(self.gb_charities)
        self.tree_charities.setAlternatingRowColors(True)
        self.tree_charities.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tree_charities.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tree_charities.setIndentation(20)
        self.tree_charities.setRootIsDecorated(True)
        self.tree_charities.setWordWrap(False)
        self.tree_charities.setHeaderHidden(False)
        self.tree_charities.setColumnCount(4)
        self.tree_charities.setObjectName("tree_charities")
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_charities)
        self.tree_charities.header().setVisible(True)
        self.tree_charities.header().setCascadingSectionResizes(False)
        self.tree_charities.header().setMinimumSectionSize(10)
        self.tree_charities.header().setSortIndicatorShown(True)
        self.gridLayout_3.addWidget(self.tree_charities, 0, 0, 1, 4)
        self.lbl_bad_address = QtWidgets.QLabel(self.gb_charities)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_bad_address.setFont(font)
        self.lbl_bad_address.setIndent(5)
        self.lbl_bad_address.setObjectName("lbl_bad_address")
        self.gridLayout_3.addWidget(self.lbl_bad_address, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(224, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 1, 1, 1)
        self.tb_minus = QtWidgets.QToolButton(self.gb_charities)
        self.tb_minus.setEnabled(False)
        self.tb_minus.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tb_minus.setAutoRaise(True)
        self.tb_minus.setObjectName("tb_minus")
        self.gridLayout_3.addWidget(self.tb_minus, 1, 2, 1, 1)
        self.tb_plus = QtWidgets.QToolButton(self.gb_charities)
        self.tb_plus.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tb_plus.setAutoRaise(True)
        self.tb_plus.setObjectName("tb_plus")
        self.gridLayout_3.addWidget(self.tb_plus, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.gb_charities, 2, 0, 2, 1)
        self.fr_title = QtWidgets.QFrame(Instance)
        self.fr_title.setMinimumSize(QtCore.QSize(0, 100))
        self.fr_title.setMaximumSize(QtCore.QSize(16777215, 150))
        self.fr_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_title.setLineWidth(1)
        self.fr_title.setObjectName("fr_title")
        self.gridLayout = QtWidgets.QGridLayout(self.fr_title)
        self.gridLayout.setContentsMargins(10, 10, 10, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_icon = QtWidgets.QLabel(self.fr_title)
        self.lbl_icon.setText("")
        self.lbl_icon.setPixmap(QtGui.QPixmap(":/DonateSpareChange/resources/icon64.png"))
        self.lbl_icon.setObjectName("lbl_icon")
        self.gridLayout.addWidget(self.lbl_icon, 0, 0, 2, 1)
        self.lbl_byline = QtWidgets.QLabel(self.fr_title)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_byline.setFont(font)
        self.lbl_byline.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_byline.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_byline.setOpenExternalLinks(True)
        self.lbl_byline.setObjectName("lbl_byline")
        self.gridLayout.addWidget(self.lbl_byline, 0, 2, 1, 1)
        self.lbl_title = QtWidgets.QLabel(self.fr_title)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 1, 1, 1)
        self.lbl_blurb = QtWidgets.QLabel(self.fr_title)
        self.lbl_blurb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_blurb.setWordWrap(True)
        self.lbl_blurb.setObjectName("lbl_blurb")
        self.gridLayout.addWidget(self.lbl_blurb, 1, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 3, 1, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout_4.addWidget(self.fr_title, 0, 0, 2, 1)
        self.gb_criteria = QtWidgets.QGroupBox(Instance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_criteria.sizePolicy().hasHeightForWidth())
        self.gb_criteria.setSizePolicy(sizePolicy)
        self.gb_criteria.setMinimumSize(QtCore.QSize(0, 0))
        self.gb_criteria.setMaximumSize(QtCore.QSize(16777215, 200))
        self.gb_criteria.setObjectName("gb_criteria")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gb_criteria)
        self.gridLayout_5.setVerticalSpacing(4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lbl_amount = QtWidgets.QLabel(self.gb_criteria)
        self.lbl_amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_amount.setObjectName("lbl_amount")
        self.gridLayout_5.addWidget(self.lbl_amount, 0, 0, 1, 1)
        self.fr_amount = QtWidgets.QFrame(self.gb_criteria)
        self.fr_amount.setMinimumSize(QtCore.QSize(0, 30))
        self.fr_amount.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fr_amount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_amount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_amount.setObjectName("fr_amount")
        self.gridLayout_5.addWidget(self.fr_amount, 0, 1, 1, 2)
        self.lbl_age = QtWidgets.QLabel(self.gb_criteria)
        self.lbl_age.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_age.setObjectName("lbl_age")
        self.gridLayout_5.addWidget(self.lbl_age, 1, 0, 1, 1)
        self.sb_age = QtWidgets.QSpinBox(self.gb_criteria)
        self.sb_age.setMaximum(9999)
        self.sb_age.setObjectName("sb_age")
        self.gridLayout_5.addWidget(self.sb_age, 1, 1, 1, 1)
        self.cb_age = QtWidgets.QComboBox(self.gb_criteria)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_age.sizePolicy().hasHeightForWidth())
        self.cb_age.setSizePolicy(sizePolicy)
        self.cb_age.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_age.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_age.setBaseSize(QtCore.QSize(0, 0))
        self.cb_age.setObjectName("cb_age")
        self.cb_age.addItem("")
        self.cb_age.addItem("")
        self.cb_age.addItem("")
        self.cb_age.addItem("")
        self.gridLayout_5.addWidget(self.cb_age, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem6, 2, 0, 1, 1)
        self.chk_autodonate = QtWidgets.QCheckBox(self.gb_criteria)
        self.chk_autodonate.setObjectName("chk_autodonate")
        self.gridLayout_5.addWidget(self.chk_autodonate, 3, 0, 1, 1)
        self.chk_1tx = QtWidgets.QCheckBox(self.gb_criteria)
        self.chk_1tx.setObjectName("chk_1tx")
        self.gridLayout_5.addWidget(self.chk_1tx, 3, 1, 1, 2)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_4.addWidget(self.gb_criteria, 0, 1, 3, 1)

        self.retranslateUi(Instance)
        QtCore.QMetaObject.connectSlotsByName(Instance)

    def retranslateUi(self, Instance):
        _translate = QtCore.QCoreApplication.translate
        Instance.setWindowTitle(_translate("Instance", "Form"))
        self.gb_coins.setTitle(_translate("Instance", "Coins (UTXOs)"))
        self.tree_coins.setToolTip(_translate("Instance", "<html><head/><body><p>The set of all coins (UTXOs) in your wallet are displayed here.</p><p>Coins that meet the criteria for donation that you specified are marked as <span style=\" font-weight:600;\">eligible</span>.</p></body></html>"))
        self.tree_coins.headerItem().setText(0, _translate("Instance", "Amount"))
        self.tree_coins.headerItem().setText(1, _translate("Instance", "Address"))
        self.tree_coins.headerItem().setText(2, _translate("Instance", "Age"))
        self.tree_coins.headerItem().setText(3, _translate("Instance", "Status"))
        __sortingEnabled = self.tree_coins.isSortingEnabled()
        self.tree_coins.setSortingEnabled(False)
        self.tree_coins.topLevelItem(0).setText(0, _translate("Instance", "0.001 mBCH"))
        self.tree_coins.topLevelItem(0).setText(1, _translate("Instance", "qqashdaishdaskudhaskuh837"))
        self.tree_coins.topLevelItem(0).setText(2, _translate("Instance", "120 blk"))
        self.tree_coins.topLevelItem(0).setText(3, _translate("Instance", "123 blocks old, eligible for donation"))
        self.tree_coins.setSortingEnabled(__sortingEnabled)
        self.lbl_utxos.setText(_translate("Instance", "2/16 coins meet specified criteria"))
        self.bt_donate_selected.setToolTip(_translate("Instance", "<html><head/><body><p>Create a new transaction for all the coins you selected that are <span style=\" font-weight:600;\">eligible</span>.</p><p>Recipients will be selected in a round-robin fashion from the set of all recipients.</p></body></html>"))
        self.bt_donate_selected.setText(_translate("Instance", "Donate Selected"))
        self.bt_donate_all.setToolTip(_translate("Instance", "<html><head/><body><p>Create a new transaction for all the coins in your wallet that are <span style=\" font-weight:600;\">eligible</span>.</p><p>Recipients will be selected in a round-robin fashion from the set of all recipients.</p></body></html>"))
        self.bt_donate_all.setText(_translate("Instance", "Donate All Eligible"))
        self.gb_charities.setToolTip(_translate("Instance", "<html><head/><body><p>Specify a list of recipients to receive your spare change.</p><p>Donations will be made in a round-robin fashion from the set of enabled recipients with a valid address specified.</p></body></html>"))
        self.gb_charities.setTitle(_translate("Instance", "Charities / Donation Destinations"))
        self.tree_charities.headerItem().setText(0, _translate("Instance", "Enabled"))
        self.tree_charities.headerItem().setText(1, _translate("Instance", "Donated (mBCH)"))
        self.tree_charities.headerItem().setText(2, _translate("Instance", "Recipient Name"))
        self.tree_charities.headerItem().setText(3, _translate("Instance", "Recipient Address"))
        __sortingEnabled = self.tree_charities.isSortingEnabled()
        self.tree_charities.setSortingEnabled(False)
        self.tree_charities.topLevelItem(0).setText(1, _translate("Instance", "1.2345678"))
        self.tree_charities.topLevelItem(0).setText(2, _translate("Instance", "EatBCH"))
        self.tree_charities.topLevelItem(0).setText(3, _translate("Instance", "qqakdjalkdjlsidqwilasldihdadhalskdhadulaskdhaskud"))
        self.tree_charities.setSortingEnabled(__sortingEnabled)
        self.lbl_bad_address.setToolTip(_translate("Instance", "One or more addresses are invalid"))
        self.lbl_bad_address.setText(_translate("Instance", "<html><head/><body><p><font color=#BC1E1E><i>One or more addresses are invalid</i></font></p></body></html>"))
        self.tb_minus.setToolTip(_translate("Instance", "<html><head/><body><p>Delete selected recipients</p></body></html>"))
        self.tb_minus.setText(_translate("Instance", "➖"))
        self.tb_plus.setToolTip(_translate("Instance", "<html><head/><body><p>Add a new recipient</p></body></html>"))
        self.tb_plus.setText(_translate("Instance", "➕"))
        self.lbl_byline.setToolTip(_translate("Instance", "<html><head/><body><p><pre>https://github.com/cculianu/DonateSpareChange</pre></p></body></html>"))
        self.lbl_byline.setText(_translate("Instance", "<html><head/><body><p>by <a href=\"https://github.com/cculianu/DonateSpareChange\">Calin Culianu</a><br/></p></body></html>"))
        self.lbl_title.setText(_translate("Instance", "Donate Spare Change 1.6"))
        self.lbl_blurb.setText(_translate("Instance", "<html><head/><body><p><span style=\" font-size:12pt;\">Automatically donate your spare change to the destinations of your choice.</span></p></body></html>"))
        self.gb_criteria.setTitle(_translate("Instance", "Specify Criteria for Donation"))
        self.lbl_amount.setToolTip(_translate("Instance", "<html><head/><body><p>In order to accommodate a wide variety of wallet configurations, this plugin donates from both &quot;change&quot; addresses as well as &quot;receiving&quot; addresses. As such, it needs to decide what is <span style=\" font-weight:600;\">spare change</span> and what is not.</p><p>So here is where you specify what amount for a coin (UTXO) you consider to be <span style=\" font-weight:600;\">spare change. </span></p><p>If a coin is below this threshold, it\'s considered spare change and is <span style=\" font-weight:600;\">eligible</span> for donation to one of the charities specified.</p><p><span style=\" font-style:italic;\">Do not specify significant amounts here unless you are rich!</span></p><p>(0.001 BCH aka 1 mBCH is a good threshold if you aren\'t sure)</p></body></html>"))
        self.lbl_amount.setText(_translate("Instance", "\"Change\" amount threshold below:"))
        self.fr_amount.setToolTip(_translate("Instance", "<html><head/><body><p>In order to accommodate a wide variety of wallet configurations, this plugin donates from both &quot;change&quot; addresses as well as &quot;receiving&quot; addresses. As such, it needs to decide what is <span style=\" font-weight:600;\">spare change</span> and what is not.</p><p>So here is where you specify what amount for a coin (UTXO) you consider to be <span style=\" font-weight:600;\">spare change. </span></p><p>If a coin is below this threshold, it\'s considered spare change and is <span style=\" font-weight:600;\">eligible</span> for donation to one of the charities specified.</p><p><span style=\" font-style:italic;\">Do not specify significant amounts here unless you are rich!</span></p><p>(0.001 BCH aka 1 mBCH is a good threshold if you aren\'t sure)</p></body></html>"))
        self.lbl_age.setToolTip(_translate("Instance", "<html><head/><body><p>Specify how many confirmations a coin needs to have before it is sent to a charity.</p><p><span style=\" font-weight:600;\">0 blocks</span> indicates unconfirmed outputs are ok to be spent</p><p><span style=\" font-weight:600;\">1 block</span> indicates at least 1 confirmation is required before you donate the coin</p><p>(and so on)</p></body></html>"))
        self.lbl_age.setText(_translate("Instance", "Donation minimum coin age:"))
        self.sb_age.setToolTip(_translate("Instance", "<html><head/><body><p>Specify how many confirmations a coin needs to have before it is sent to a charity.</p><p><span style=\" font-weight:600;\">0 blocks</span> indicates unconfirmed outputs are ok to be spent</p><p><span style=\" font-weight:600;\">1 block</span> indicates at least 1 confirmation is required before you donate the coin</p><p>(and so on)</p></body></html>"))
        self.sb_age.setSuffix(_translate("Instance", " blocks"))
        self.cb_age.setItemText(0, _translate("Instance", "Blocks"))
        self.cb_age.setItemText(1, _translate("Instance", "Hours"))
        self.cb_age.setItemText(2, _translate("Instance", "Days"))
        self.cb_age.setItemText(3, _translate("Instance", "Weeks"))
        self.chk_autodonate.setToolTip(_translate("Instance", "<html><head/><body><p>Auto-donate coins <span style=\" font-weight:600;\">in the background</span> (without prompting) as they become eligible. </p><p>This feature requires that your wallet not be password-protected.</p></body></html>"))
        self.chk_autodonate.setText(_translate("Instance", "Auto-donate change"))
        self.chk_1tx.setToolTip(_translate("Instance", "<html><head/><body><p>When this is <span style=\" font-weight:600;\">enabled</span>, all coins that meet the specified criteria are batched together in 1 single sending transaction.</p><p>For the cost minded: This has the advantage of conserving on <span style=\" font-weight:600;\">fees</span>.</p><p>For the privacy minded: It becomes easier to associate your receiving addresses with each other if you turn this option on. So if <span style=\" font-weight:600;\">privacy</span> is your concern, leave this option <span style=\" font-weight:600;\">disabled</span>.</p><p><span style=\" font-style:italic;\">Note: This option only appies to </span><span style=\" font-weight:600; font-style:italic;\">auto-donation mode</span><span style=\" font-style:italic;\">. </span>To control batching in manual mode, select single or multiple items from the table below.</p></body></html>"))
        self.chk_1tx.setText(_translate("Instance", "Batch all sends as a single transacton"))

from . import resources
