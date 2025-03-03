# encoding: UTF-8

from objectmaphelper import *

settings_OCC_SettingsDialog = {"name": "Settings", "type": "OCC::SettingsDialog", "visible": 1}
owncloudWizard_OCC_OwncloudWizard = {"name": "owncloudWizard", "type": "OCC::OwncloudWizard", "visible": 1}
owncloudWizard_qt_passive_wizardbutton1_QPushButton = {"name": "__qt__passive_wizardbutton1", "type": "QPushButton", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
owncloudWizard_lLocal_QLabel = {"name": "lLocal", "type": "QLabel", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
pbSelectLocalFolder_QPushButton = {"buddy": owncloudWizard_lLocal_QLabel, "name": "pbSelectLocalFolder", "type": "QPushButton", "visible": 1}
qFileDialog_QFileDialog = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
qFileDialog_splitter_QSplitter = {"name": "splitter", "type": "QSplitter", "visible": 1, "window": qFileDialog_QFileDialog}
splitter_frame_QFrame = {"container": qFileDialog_splitter_QSplitter, "name": "frame", "type": "QFrame", "visible": 1}
frame_stackedWidget_QStackedWidget = {"container": splitter_frame_QFrame, "name": "stackedWidget", "type": "QStackedWidget", "visible": 1}
stackedWidget_treeView_QTreeView = {"container": frame_stackedWidget_QStackedWidget, "name": "treeView", "type": "QTreeView", "visible": 1}
qFileDialog_newFolderButton_QToolButton = {"name": "newFolderButton", "type": "QToolButton", "visible": 1, "window": qFileDialog_QFileDialog}
treeView_QExpandingLineEdit = {"columnIndex": 0, "container": stackedWidget_treeView_QTreeView, "rowIndex": 2, "type": "QExpandingLineEdit", "unnamed": 1, "visible": 1}
qFileDialog_Choose_QPushButton = {"text": "Choose", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": qFileDialog_QFileDialog}
enter_Password_QInputDialog = {"type": "QInputDialog", "unnamed": 1, "visible": 1, "windowTitle": "Enter Password"}
enter_Password_Cancel_QPushButton = {"text": "Cancel", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": enter_Password_QInputDialog}
settings_settingsdialog_toolbutton_admin_localhost_QToolButton = {"name": "settingsdialog_toolbutton_admin@localhost", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
settings_stack_QStackedWidget = {"name": "stack", "type": "QStackedWidget", "visible": 1, "window": settings_OCC_SettingsDialog}
stack_accountToolbox_QToolButton = {"container": settings_stack_QStackedWidget, "name": "_accountToolbox", "type": "QToolButton", "visible": 1}
settings_QMenu = {"type": "QMenu", "unnamed": 1, "visible": 1, "window": settings_OCC_SettingsDialog}
owncloudWizard_usernameLabel_QLabel = {"name": "usernameLabel", "type": "QLabel", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
owncloudWizard_passwordLabel_QLabel = {"name": "passwordLabel", "type": "QLabel", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
qFileDialog_fileNameLabel_QLabel = {"name": "fileNameLabel", "type": "QLabel", "visible": 1, "window": qFileDialog_QFileDialog}
leUsername_QLineEdit = {"buddy": owncloudWizard_usernameLabel_QLabel, "name": "leUsername", "type": "QLineEdit", "visible": 1}
owncloudWizard_cbSyncFromScratch_QRadioButton = {"name": "cbSyncFromScratch", "type": "QRadioButton", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
lePassword_QLineEdit = {"buddy": owncloudWizard_passwordLabel_QLabel, "name": "lePassword", "type": "QLineEdit", "visible": 1}
fileNameEdit_QLineEdit = {"buddy": qFileDialog_fileNameLabel_QLabel, "name": "fileNameEdit", "type": "QLineEdit", "visible": 1}
settings_settingsdialog_toolbutton_artur_jankaritech_ocloud_de_QToolButton = {"name": "settingsdialog_toolbutton_artur@jankaritech.ocloud.de", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
stack_folderList_QTreeView = {"container": settings_stack_QStackedWidget, "name": "_folderList", "type": "QTreeView", "visible": 1}
sharingDialog_OCC_ShareDialog = {"name": "SharingDialog", "type": "OCC::ShareDialog", "visible": 1}
sharingDialog_qt_tabwidget_stackedwidget_QStackedWidget = {"name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1, "window": sharingDialog_OCC_ShareDialog}
qt_tabwidget_stackedwidget_SharingDialogUG_OCC_ShareUserGroupWidget = {"container": sharingDialog_qt_tabwidget_stackedwidget_QStackedWidget, "name": "SharingDialogUG", "type": "OCC::ShareUserGroupWidget", "visible": 1}
sharingDialogUG_scrollArea_QScrollArea = {"container": qt_tabwidget_stackedwidget_SharingDialogUG_OCC_ShareUserGroupWidget, "name": "scrollArea", "type": "QScrollArea", "visible": 1}
scrollArea_deleteShareButton_QToolButton = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "deleteShareButton", "type": "QToolButton", "visible": 1}
settings_settingsdialog_toolbutton_Quit_ownCloud_QToolButton = {"name": "settingsdialog_toolbutton_Quit ownCloud", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
quit_ownCloud_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Quit ownCloud"}
quit_ownCloud_Yes_QPushButton = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": quit_ownCloud_QMessageBox}
qFileDialog_lookInCombo_QComboBox = {"name": "lookInCombo", "type": "QComboBox", "visible": 1, "window": qFileDialog_QFileDialog}
splitter_sidebar_QSidebar = {"container": qFileDialog_splitter_QSplitter, "name": "sidebar", "type": "QSidebar", "visible": 1}
settings_settingsdialog_toolbutton_Settings_QToolButton = {"name": "settingsdialog_toolbutton_Settings", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
stack_scrollArea_QScrollArea = {"container": settings_stack_QStackedWidget, "name": "scrollArea", "type": "QScrollArea", "visible": 1}
scrollArea_QScrollBar = {"container": stack_scrollArea_QScrollArea, "type": "QScrollBar", "unnamed": 1, "visible": 1}
scrollArea_groupBox_QGroupBox = {"container": stack_scrollArea_QScrollArea, "name": "groupBox", "type": "QGroupBox", "visible": 1}
groupBox_proxyGroupBox_QGroupBox = {"container": scrollArea_groupBox_QGroupBox, "name": "proxyGroupBox", "type": "QGroupBox", "visible": 1}
proxyGroupBox_manualProxyRadioButton_QRadioButton = {"container": groupBox_proxyGroupBox_QGroupBox, "name": "manualProxyRadioButton", "type": "QRadioButton", "visible": 1}
proxyGroupBox_hostLineEdit_QLineEdit = {"container": groupBox_proxyGroupBox_QGroupBox, "name": "hostLineEdit", "type": "QLineEdit", "visible": 1}
proxyGroupBox_authRequiredcheckBox_QCheckBox = {"container": groupBox_proxyGroupBox_QGroupBox, "name": "authRequiredcheckBox", "type": "QCheckBox", "visible": 1}
proxyGroupBox_labelLocalhost_QLabel = {"container": groupBox_proxyGroupBox_QGroupBox, "name": "labelLocalhost", "type": "QLabel", "visible": 1}
groupBox_uploadBox_QGroupBox = {"container": scrollArea_groupBox_QGroupBox, "name": "uploadBox", "type": "QGroupBox", "visible": 1}
uploadBox_autoUploadLimitRadioButton_QRadioButton = {"container": groupBox_uploadBox_QGroupBox, "name": "autoUploadLimitRadioButton", "type": "QRadioButton", "visible": 1}
stack_qt_tabwidget_stackedwidget_QStackedWidget = {"container": settings_stack_QStackedWidget, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
qt_tabwidget_stackedwidget_OCC_ActivityWidget_OCC_ActivityWidget = {"container": stack_qt_tabwidget_stackedwidget_QStackedWidget, "name": "OCC__ActivityWidget", "type": "OCC::ActivityWidget", "visible": 1}
oCC_ActivityWidget_activityList_QListView = {"container": qt_tabwidget_stackedwidget_OCC_ActivityWidget_OCC_ActivityWidget, "name": "_activityList", "type": "QListView", "visible": 1}
o_activityList_QScrollBar = {"container": oCC_ActivityWidget_activityList_QListView, "type": "QScrollBar", "unnamed": 1, "visible": 1}
oCC_ActivityWidget_notifyScroll_QScrollArea = {"container": qt_tabwidget_stackedwidget_OCC_ActivityWidget_OCC_ActivityWidget, "name": "_notifyScroll", "type": "QScrollArea", "visible": 1}
o_notifyScroll_QScrollBar = {"container": oCC_ActivityWidget_notifyScroll_QScrollArea, "type": "QScrollBar", "unnamed": 1, "visible": 1}
o_notifyScroll_Accept_QPushButton = {"container": oCC_ActivityWidget_notifyScroll_QScrollArea, "text": "Accept", "type": "QPushButton", "unnamed": 1, "visible": 1}
o_notifyScroll_timeLabel_QLabel = {"container": oCC_ActivityWidget_notifyScroll_QScrollArea, "name": "_timeLabel", "type": "QLabel", "visible": 1}
o_notifyScroll_subjectLabel_QLabel = {"container": oCC_ActivityWidget_notifyScroll_QScrollArea, "name": "_subjectLabel", "type": "QLabel", "visible": 1}
scrollArea_OCC_ShareUserLine_OCC_ShareUserLine = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "OCC__ShareUserLine", "type": "OCC::ShareUserLine", "visible": 1}
o_folderList_QModelIndex = {"column": 0, "container": stack_folderList_QTreeView, "text": "", "type": "QModelIndex"}
qt_tabwidget_stackedwidget_OCC_IssuesWidget_OCC_IssuesWidget = {"container": stack_qt_tabwidget_stackedwidget_QStackedWidget, "name": "OCC__IssuesWidget", "type": "OCC::IssuesWidget", "visible": 1}
oCC_IssuesWidget_treeWidget_QTreeWidget = {"container": qt_tabwidget_stackedwidget_OCC_IssuesWidget_OCC_IssuesWidget, "name": "_treeWidget", "type": "QTreeWidget", "visible": 1}
o_treeWidget_lorem_conflicted_copy_2020_12_14_133239_txt_QModelIndex = {"column": 1, "container": oCC_IssuesWidget_treeWidget_QTreeWidget, "text": RegularExpression("lorem (conflicted copy 2020-12-14 133239).txt"), "type": "QModelIndex"}
scrollArea_sharedWith_QLabel = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "sharedWith", "type": "QLabel", "visible": 1}
scrollArea_permissionsEdit_QCheckBox = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "permissionsEdit", "type": "QCheckBox", "visible": 1}
scrollArea_permissionShare_QCheckBox = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "permissionShare", "type": "QCheckBox", "visible": 1}
stack_qt_tabwidget_tabbar_QTabBar = {"container": settings_stack_QStackedWidget, "name": "qt_tabwidget_tabbar", "type": "QTabBar", "visible": 1}
o_treeWidget_Conflict_Server_version_downloaded_local_copy_renamed_and_not_uploaded_QModelIndex = {"column": 3, "container": oCC_IssuesWidget_treeWidget_QTreeWidget, "text": "Conflict: Server version downloaded, local copy renamed and not uploaded.", "type": "QModelIndex"}
qt_tabwidget_stackedwidget_OCC_ProtocolWidget_OCC_ProtocolWidget = {"container": stack_qt_tabwidget_stackedwidget_QStackedWidget, "name": "OCC__ProtocolWidget", "type": "OCC::ProtocolWidget", "visible": 1}
oCC_ProtocolWidget_treeWidget_QTreeWidget = {"container": qt_tabwidget_stackedwidget_OCC_ProtocolWidget_OCC_ProtocolWidget, "name": "_treeWidget", "type": "QTreeWidget", "visible": 1}
o_treeWidget_lorem_txt_QModelIndex = {"column": 1, "container": oCC_ProtocolWidget_treeWidget_QTreeWidget, "text": "lorem.txt", "type": "QModelIndex"}
sharingDialog_qt_tabwidget_tabbar_QTabBar = {"name": "qt_tabwidget_tabbar", "type": "QTabBar", "visible": 1, "window": sharingDialog_OCC_ShareDialog}
qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget = {"container": sharingDialog_qt_tabwidget_stackedwidget_QStackedWidget, "name": "OCC__ShareLinkWidget", "type": "OCC::ShareLinkWidget", "visible": 1}
oCC_ShareLinkWidget_checkBox_password_QCheckBox = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "checkBox_password", "type": "QCheckBox", "visible": 1}
oCC_ShareLinkWidget_widget_editing_QWidget = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "widget_editing", "type": "QWidget", "visible": 1}
oCC_ShareLinkWidget_checkBox_password_QProgressIndicator = {"aboveWidget": oCC_ShareLinkWidget_widget_editing_QWidget, "container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "leftWidget": oCC_ShareLinkWidget_checkBox_password_QCheckBox, "type": "QProgressIndicator", "unnamed": 1, "visible": 1}
sharingDialog_label_name_QLabel = {"name": "label_name", "type": "QLabel", "visible": 1, "window": sharingDialog_OCC_ShareDialog}
oCC_ShareLinkWidget_linkShares_QTableWidget = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "linkShares", "type": "QTableWidget", "visible": 1}
linkShares_QToolButton = {"container": oCC_ShareLinkWidget_linkShares_QTableWidget, "text": "...", "type": "QToolButton", "unnamed": 1, "visible": 1}
oCC_ShareLinkWidget_lineEdit_password_QLineEdit = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "lineEdit_password", "type": "QLineEdit", "visible": 1}
oCC_ShareLinkWidget_calendar_QDateEdit = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "calendar", "type": "QDateEdit", "visible": 1}
oCC_ShareLinkWidget_qt_calendar_prevmonth_QPrevNextCalButton = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "qt_calendar_prevmonth", "type": "QPrevNextCalButton", "visible": 1}
oCC_ShareLinkWidget_qt_calendar_calendarview_QCalendarView = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "qt_calendar_calendarview", "type": "QCalendarView", "visible": 1}
oCC_ShareLinkWidget_qt_spinbox_lineedit_QLineEdit = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "qt_spinbox_lineedit", "type": "QLineEdit", "visible": 1}
linkShares_0_0_QModelIndex = {"column": 0, "container": oCC_ShareLinkWidget_linkShares_QTableWidget, "row": 0, "type": "QModelIndex"}
oCC_ShareLinkWidget_radio_readOnly_QRadioButton = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "radio_readOnly", "type": "QRadioButton", "visible": 1}
oCC_ShareLinkWidget_radio_readWrite_QRadioButton = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "radio_readWrite", "type": "QRadioButton", "visible": 1}
oCC_ShareLinkWidget_radio_uploadOnly_QRadioButton = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "radio_uploadOnly", "type": "QRadioButton", "visible": 1}
oCC_ShareLinkWidget_checkBox_expire_QCheckBox = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "checkBox_expire", "type": "QCheckBox", "visible": 1}
oCC_ShareLinkWidget_checkBox_expire_QProgressIndicator = {"aboveWidget": oCC_ShareLinkWidget_lineEdit_password_QLineEdit, "container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "leftWidget": oCC_ShareLinkWidget_checkBox_expire_QCheckBox, "type": "QProgressIndicator", "unnamed": 1, "visible": 1}
oCC_IssuesWidget_tableView_QTableView = {"container": qt_tabwidget_stackedwidget_OCC_IssuesWidget_OCC_IssuesWidget, "name": "_tableView", "type": "QTableView", "visible": 1}
o_tableView_0_1_QModelIndex = {"column": 1, "container": oCC_IssuesWidget_tableView_QTableView, "row": 0, "type": "QModelIndex"}
settings_settingsdialog_toolbutton_Add_account_QToolButton = {"name": "settingsdialog_toolbutton_Add account", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
settings_settingsdialog_toolbutton_Activity_QToolButton = {"name": "settingsdialog_toolbutton_Activity", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
sharingDialog_Close_QPushButton = {"text": "Close", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": sharingDialog_OCC_ShareDialog}
stack_Enable_experimental_placeholder_mode_QPushButton = {"container": settings_stack_QStackedWidget, "text": "Enable experimental placeholder mode", "type": "QPushButton", "unnamed": 1, "visible": 1}
disable_virtual_file_support_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Disable virtual file support?"}
disable_virtual_file_support_Disable_support_QPushButton = {"text": "Disable support", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": disable_virtual_file_support_QMessageBox}
error_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Error"}
owncloudWizard_urlLabel_QLabel = {"name": "urlLabel", "type": "QLabel", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
choose_What_to_Sync_OCC_SelectiveSyncDialog = {"type": "OCC::SelectiveSyncDialog", "unnamed": 1, "visible": 1, "windowTitle": "Choose What to Sync"}
choose_What_to_Sync_Deselect_remote_folders_you_do_not_wish_to_synchronize_QLabel = {"text": "Deselect remote folders you do not wish to synchronize.", "type": "QLabel", "unnamed": 1, "visible": 1, "window": choose_What_to_Sync_OCC_SelectiveSyncDialog}
choose_What_To_Synchronize_QTreeWidget = {"aboveWidget": choose_What_to_Sync_Deselect_remote_folders_you_do_not_wish_to_synchronize_QLabel, "type": "QTreeWidget", "unnamed": 1, "visible": 1, "window": choose_What_to_Sync_OCC_SelectiveSyncDialog}
deselect_remote_folders_you_do_not_wish_to_synchronize_QHeaderView = {"container": choose_What_To_Synchronize_QTreeWidget, "orientation": 1, "type": "QHeaderView", "unnamed": 1, "visible": 1}
linkShares_QToolButton_2 = {"container": oCC_ShareLinkWidget_linkShares_QTableWidget, "occurrence": 2, "type": "QToolButton", "unnamed": 1, "visible": 1}
oCC_ShareLinkWidget_Delete_QPushButton = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "text": "Delete", "type": "QPushButton", "unnamed": 1, "visible": 1}
oCC_ShareLinkWidget_pushButton_setPassword_QPushButton = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "pushButton_setPassword", "type": "QPushButton", "visible": 1}
remove_All_Files_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Remove All Files?"}
setupWizardWindow_OCC_Wizard_SetupWizardWindow = {"name": "SetupWizardWindow", "type": "OCC::Wizard::SetupWizardWindow", "visible": 1}
setupWizardWindow_contentWidget_QStackedWidget = {"name": "contentWidget", "type": "QStackedWidget", "visible": 1, "window": setupWizardWindow_OCC_Wizard_SetupWizardWindow}
contentWidget_urlLineEdit_QLineEdit = {"container": setupWizardWindow_contentWidget_QStackedWidget, "name": "urlLineEdit", "type": "QLineEdit", "visible": 1}
setupWizardWindow_nextButton_QPushButton = {"name": "nextButton", "type": "QPushButton", "visible": 1, "window": setupWizardWindow_OCC_Wizard_SetupWizardWindow}
insecure_connection_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Insecure connection"}
insecure_connection_Confirm_QPushButton = {"text": "Confirm", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": insecure_connection_QMessageBox}
contentWidget_usernameLineEdit_QLineEdit = {"container": setupWizardWindow_contentWidget_QStackedWidget, "name": "usernameLineEdit", "type": "QLineEdit", "visible": 1}
contentWidget_passwordLineEdit_QLineEdit = {"container": setupWizardWindow_contentWidget_QStackedWidget, "name": "passwordLineEdit", "type": "QLineEdit", "visible": 1}
contentWidget_advancedConfigGroupBox_QGroupBox = {"container": setupWizardWindow_contentWidget_QStackedWidget, "name": "advancedConfigGroupBox", "type": "QGroupBox", "visible": 1}
advancedConfigGroupBox_localDirectoryGroupBox_QGroupBox = {"container": contentWidget_advancedConfigGroupBox_QGroupBox, "name": "localDirectoryGroupBox", "type": "QGroupBox", "visible": 1}
localDirectoryGroupBox_localDirectoryLineEdit_QLineEdit = {"container": advancedConfigGroupBox_localDirectoryGroupBox_QGroupBox, "name": "localDirectoryLineEdit", "type": "QLineEdit", "visible": 1}
localDirectoryGroupBox_chooseLocalDirectoryButton_QToolButton = {"container": advancedConfigGroupBox_localDirectoryGroupBox_QGroupBox, "name": "chooseLocalDirectoryButton", "type": "QToolButton", "visible": 1}
oCC_TlsErrorDialog_OCC_TlsErrorDialog = {"name": "OCC__TlsErrorDialog", "type": "OCC::TlsErrorDialog", "visible": 1}
oCC_TlsErrorDialog_Yes_QPushButton = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": oCC_TlsErrorDialog_OCC_TlsErrorDialog}
advancedConfigGroupBox_syncModeGroupBox_QGroupBox = {"container": contentWidget_advancedConfigGroupBox_QGroupBox, "name": "syncModeGroupBox", "type": "QGroupBox", "visible": 1}
syncModeGroupBox_configureSyncManuallyRadioButton_QRadioButton = {"container": advancedConfigGroupBox_syncModeGroupBox_QGroupBox, "name": "configureSyncManuallyRadioButton", "type": "QRadioButton", "visible": 1}
add_Folder_Sync_Connection_OCC_FolderWizard = {"type": "OCC::FolderWizard", "unnamed": 1, "visible": 1, "windowTitle": "Add Folder Sync Connection"}
add_Folder_Sync_Connection_qt_passive_wizardbutton1_QPushButton = {"name": "__qt__passive_wizardbutton1", "type": "QPushButton", "visible": 1, "window": add_Folder_Sync_Connection_OCC_FolderWizard}
add_Folder_Sync_Connection_groupBox_QGroupBox = {"name": "groupBox", "type": "QGroupBox", "visible": 1, "window": add_Folder_Sync_Connection_OCC_FolderWizard}
groupBox_folderTreeWidget_QTreeWidget = {"container": add_Folder_Sync_Connection_groupBox_QGroupBox, "name": "folderTreeWidget", "type": "QTreeWidget", "visible": 1}
add_Folder_Sync_Connection_FolderWizardSourcePage_OCC_FolderWizardLocalPath = {"name": "FolderWizardSourcePage", "type": "OCC::FolderWizardLocalPath", "visible": 1, "window": add_Folder_Sync_Connection_OCC_FolderWizard}
add_Folder_Sync_Connection_Deselect_remote_folders_you_do_not_wish_to_synchronize_QLabel = {"text": "Deselect remote folders you do not wish to synchronize.", "type": "QLabel", "unnamed": 1, "visible": 1, "window": add_Folder_Sync_Connection_OCC_FolderWizard}
add_Folder_Sync_Connection_Deselect_remote_folders_you_do_not_wish_to_synchronize_QTreeWidget = {"aboveWidget": add_Folder_Sync_Connection_Deselect_remote_folders_you_do_not_wish_to_synchronize_QLabel, "type": "QTreeWidget", "unnamed": 1, "visible": 1, "window": add_Folder_Sync_Connection_OCC_FolderWizard}
deselect_remote_folders_you_do_not_wish_to_synchronize_ownCloud_QModelIndex = {"column": 0, "container": add_Folder_Sync_Connection_Deselect_remote_folders_you_do_not_wish_to_synchronize_QTreeWidget, "text": "ownCloud", "type": "QModelIndex"}
syncModeGroupBox_useVfsRadioButton_QRadioButton = {"container": advancedConfigGroupBox_syncModeGroupBox_QGroupBox, "name": "useVfsRadioButton", "type": "QRadioButton", "visible": 1}
contentWidget_Enable_experimental_placeholder_mode_QPushButton = {"container": setupWizardWindow_contentWidget_QStackedWidget, "text": "Enable experimental placeholder mode", "type": "QPushButton", "unnamed": 1, "visible": 1}
contentWidget_Stay_safe_QPushButton = {"container": setupWizardWindow_contentWidget_QStackedWidget, "text": "Stay safe", "type": "QPushButton", "unnamed": 1, "visible": 1}