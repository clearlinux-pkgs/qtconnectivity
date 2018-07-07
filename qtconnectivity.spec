#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtconnectivity
Version  : 5.11.1
Release  : 7
URL      : http://download.qt.io/official_releases/qt/5.11/5.11.1/submodules/qtconnectivity-everywhere-src-5.11.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.11/5.11.1/submodules/qtconnectivity-everywhere-src-5.11.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtconnectivity-lib
Requires: qtconnectivity-license
Requires: qtconnectivity-bin
BuildRequires : bluez-dev
BuildRequires : cmake
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras

%description
This application is a graphical test application for Bluetooth.
It is able to invoke close to all API features offered by the QtBluetooth API.
It includes features like:

%package bin
Summary: bin components for the qtconnectivity package.
Group: Binaries
Requires: qtconnectivity-license

%description bin
bin components for the qtconnectivity package.


%package dev
Summary: dev components for the qtconnectivity package.
Group: Development
Requires: qtconnectivity-lib
Requires: qtconnectivity-bin
Provides: qtconnectivity-devel

%description dev
dev components for the qtconnectivity package.


%package lib
Summary: lib components for the qtconnectivity package.
Group: Libraries
Requires: qtconnectivity-license

%description lib
lib components for the qtconnectivity package.


%package license
Summary: license components for the qtconnectivity package.
Group: Default

%description license
license components for the qtconnectivity package.


%prep
%setup -q -n qtconnectivity-everywhere-src-5.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1530977666
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/qtconnectivity
cp LICENSE.LGPL3 %{buildroot}/usr/share/doc/qtconnectivity/LICENSE.LGPL3
cp LICENSE.FDL %{buildroot}/usr/share/doc/qtconnectivity/LICENSE.FDL
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/doc/qtconnectivity/LICENSE.GPL3-EXCEPT
cp LICENSE.GPL2 %{buildroot}/usr/share/doc/qtconnectivity/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/doc/qtconnectivity/LICENSE.GPL3
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sdpscanner

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/adapter1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/adapter_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/agent_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/androidbroadcastreceiver_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/bluetoothmanagement_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/bluez5_helper_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/bluez_data_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/device1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/device_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/devicediscoverybroadcastreceiver_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/dummy_helper_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/gattchar1_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/gattdesc1_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/gattservice1_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/hcimanager_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/inputstreamthread_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/jni_android_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/lecmaccalculator_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/localdevicebroadcastreceiver_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/lowenergynotificationhub_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/manager_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/obex_agent_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/obex_client1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/obex_client_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/obex_manager_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/obex_objectpush1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/obex_transfer1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/obex_transfer_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/objectmanager_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbluetooth_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtcentralmanager_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtchanneldelegate_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtconnectionmonitor_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtdeviceinquiry_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtdevicepair_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtgcdtimer_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtl2capchannel_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtledeviceinquiry_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtnotifier_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtobexsession_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtperipheralmanager_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtrfcommchannel_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtsdpinquiry_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtservicerecord_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtsocketlistener_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/osxbtutility_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/profile1_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/properties_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothaddress_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothdevicediscoveryagent_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothdeviceinfo_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothhostinfo_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothlocaldevice_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothserver_osx_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothserver_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothservicediscoveryagent_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothserviceinfo_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothsocket_osx_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothsocket_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothtransferreply_bluez_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothtransferreply_osx_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothtransferreply_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qbluetoothtransferrequest_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qleadvertiser_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qlowenergycontroller_android_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qlowenergycontroller_bluez_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qlowenergycontroller_bluezdbus_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qlowenergycontroller_osx_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qlowenergycontroller_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qlowenergycontroller_winrt_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qlowenergycontrollerbase_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qlowenergyserviceprivate_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qprivatelinearbuffer_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qtbluetooth-config_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/qtbluetoothglobal_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/remotedevicemanager_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/serveracceptancethread_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/service_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/servicediscoverybroadcastreceiver_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/servicemap_p.h
/usr/include/qt5/QtBluetooth/5.11.1/QtBluetooth/private/uistrings_p.h
/usr/include/qt5/QtBluetooth/QBluetoothAddress
/usr/include/qt5/QtBluetooth/QBluetoothDeviceDiscoveryAgent
/usr/include/qt5/QtBluetooth/QBluetoothDeviceInfo
/usr/include/qt5/QtBluetooth/QBluetoothHostInfo
/usr/include/qt5/QtBluetooth/QBluetoothLocalDevice
/usr/include/qt5/QtBluetooth/QBluetoothServer
/usr/include/qt5/QtBluetooth/QBluetoothServiceDiscoveryAgent
/usr/include/qt5/QtBluetooth/QBluetoothServiceInfo
/usr/include/qt5/QtBluetooth/QBluetoothSocket
/usr/include/qt5/QtBluetooth/QBluetoothTransferManager
/usr/include/qt5/QtBluetooth/QBluetoothTransferReply
/usr/include/qt5/QtBluetooth/QBluetoothTransferRequest
/usr/include/qt5/QtBluetooth/QBluetoothUuid
/usr/include/qt5/QtBluetooth/QLowEnergyAdvertisingData
/usr/include/qt5/QtBluetooth/QLowEnergyAdvertisingParameters
/usr/include/qt5/QtBluetooth/QLowEnergyCharacteristic
/usr/include/qt5/QtBluetooth/QLowEnergyCharacteristicData
/usr/include/qt5/QtBluetooth/QLowEnergyConnectionParameters
/usr/include/qt5/QtBluetooth/QLowEnergyController
/usr/include/qt5/QtBluetooth/QLowEnergyDescriptor
/usr/include/qt5/QtBluetooth/QLowEnergyDescriptorData
/usr/include/qt5/QtBluetooth/QLowEnergyHandle
/usr/include/qt5/QtBluetooth/QLowEnergyService
/usr/include/qt5/QtBluetooth/QLowEnergyServiceData
/usr/include/qt5/QtBluetooth/QtBluetooth
/usr/include/qt5/QtBluetooth/QtBluetoothDepends
/usr/include/qt5/QtBluetooth/QtBluetoothVersion
/usr/include/qt5/QtBluetooth/qbluetooth.h
/usr/include/qt5/QtBluetooth/qbluetoothaddress.h
/usr/include/qt5/QtBluetooth/qbluetoothdevicediscoveryagent.h
/usr/include/qt5/QtBluetooth/qbluetoothdeviceinfo.h
/usr/include/qt5/QtBluetooth/qbluetoothglobal.h
/usr/include/qt5/QtBluetooth/qbluetoothhostinfo.h
/usr/include/qt5/QtBluetooth/qbluetoothlocaldevice.h
/usr/include/qt5/QtBluetooth/qbluetoothserver.h
/usr/include/qt5/QtBluetooth/qbluetoothservicediscoveryagent.h
/usr/include/qt5/QtBluetooth/qbluetoothserviceinfo.h
/usr/include/qt5/QtBluetooth/qbluetoothsocket.h
/usr/include/qt5/QtBluetooth/qbluetoothtransfermanager.h
/usr/include/qt5/QtBluetooth/qbluetoothtransferreply.h
/usr/include/qt5/QtBluetooth/qbluetoothtransferrequest.h
/usr/include/qt5/QtBluetooth/qbluetoothuuid.h
/usr/include/qt5/QtBluetooth/qlowenergyadvertisingdata.h
/usr/include/qt5/QtBluetooth/qlowenergyadvertisingparameters.h
/usr/include/qt5/QtBluetooth/qlowenergycharacteristic.h
/usr/include/qt5/QtBluetooth/qlowenergycharacteristicdata.h
/usr/include/qt5/QtBluetooth/qlowenergyconnectionparameters.h
/usr/include/qt5/QtBluetooth/qlowenergycontroller.h
/usr/include/qt5/QtBluetooth/qlowenergydescriptor.h
/usr/include/qt5/QtBluetooth/qlowenergydescriptordata.h
/usr/include/qt5/QtBluetooth/qlowenergyservice.h
/usr/include/qt5/QtBluetooth/qlowenergyservicedata.h
/usr/include/qt5/QtBluetooth/qtbluetooth-config.h
/usr/include/qt5/QtBluetooth/qtbluetoothglobal.h
/usr/include/qt5/QtBluetooth/qtbluetoothversion.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/adapter_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/agent_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/androidjninfc_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/androidmainnewintentlistener_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/dbusobjectmanager_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/dbusproperties_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/manager_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/neard_helper_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qllcpserver_android_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qllcpserver_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qllcpserver_p_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qllcpsocket_android_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qllcpsocket_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qllcpsocket_p_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qndefnfcsmartposterrecord_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qndefrecord_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldmanager_android_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldmanager_emulator_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldmanager_neard_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldmanager_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldmanagerimpl_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldmanagervirtualbase_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldsharemanager_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldsharemanagerimpl_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldsharetarget_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldsharetargetimpl_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldtagtype1_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldtagtype2_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldtagtype3_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldtagtype4_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldtarget_android_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldtarget_emulator_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldtarget_neard_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qnearfieldtarget_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qtlv_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/qtnfcglobal_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/tag_p.h
/usr/include/qt5/QtNfc/5.11.1/QtNfc/private/targetemulator_p.h
/usr/include/qt5/QtNfc/QNdefFilter
/usr/include/qt5/QtNfc/QNdefMessage
/usr/include/qt5/QtNfc/QNdefNfcIconRecord
/usr/include/qt5/QtNfc/QNdefNfcSmartPosterRecord
/usr/include/qt5/QtNfc/QNdefNfcTextRecord
/usr/include/qt5/QtNfc/QNdefNfcUriRecord
/usr/include/qt5/QtNfc/QNdefRecord
/usr/include/qt5/QtNfc/QNearFieldManager
/usr/include/qt5/QtNfc/QNearFieldShareManager
/usr/include/qt5/QtNfc/QNearFieldShareTarget
/usr/include/qt5/QtNfc/QNearFieldTarget
/usr/include/qt5/QtNfc/QQmlNdefRecord
/usr/include/qt5/QtNfc/QtNfc
/usr/include/qt5/QtNfc/QtNfcDepends
/usr/include/qt5/QtNfc/QtNfcVersion
/usr/include/qt5/QtNfc/qndeffilter.h
/usr/include/qt5/QtNfc/qndefmessage.h
/usr/include/qt5/QtNfc/qndefnfcsmartposterrecord.h
/usr/include/qt5/QtNfc/qndefnfctextrecord.h
/usr/include/qt5/QtNfc/qndefnfcurirecord.h
/usr/include/qt5/QtNfc/qndefrecord.h
/usr/include/qt5/QtNfc/qnearfieldmanager.h
/usr/include/qt5/QtNfc/qnearfieldsharemanager.h
/usr/include/qt5/QtNfc/qnearfieldsharetarget.h
/usr/include/qt5/QtNfc/qnearfieldtarget.h
/usr/include/qt5/QtNfc/qnfcglobal.h
/usr/include/qt5/QtNfc/qqmlndefrecord.h
/usr/include/qt5/QtNfc/qtnfcglobal.h
/usr/include/qt5/QtNfc/qtnfcversion.h
/usr/lib64/cmake/Qt5Bluetooth/Qt5BluetoothConfig.cmake
/usr/lib64/cmake/Qt5Bluetooth/Qt5BluetoothConfigVersion.cmake
/usr/lib64/cmake/Qt5Nfc/Qt5NfcConfig.cmake
/usr/lib64/cmake/Qt5Nfc/Qt5NfcConfigVersion.cmake
/usr/lib64/libQt5Bluetooth.prl
/usr/lib64/libQt5Bluetooth.so
/usr/lib64/libQt5Nfc.prl
/usr/lib64/libQt5Nfc.so
/usr/lib64/pkgconfig/Qt5Bluetooth.pc
/usr/lib64/pkgconfig/Qt5Nfc.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_bluetooth.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_bluetooth_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_nfc.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_nfc_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Bluetooth.so.5
/usr/lib64/libQt5Bluetooth.so.5.11
/usr/lib64/libQt5Bluetooth.so.5.11.1
/usr/lib64/libQt5Nfc.so.5
/usr/lib64/libQt5Nfc.so.5.11
/usr/lib64/libQt5Nfc.so.5.11.1
/usr/lib64/qt5/qml/QtBluetooth/libdeclarative_bluetooth.so
/usr/lib64/qt5/qml/QtBluetooth/plugins.qmltypes
/usr/lib64/qt5/qml/QtBluetooth/qmldir
/usr/lib64/qt5/qml/QtNfc/libdeclarative_nfc.so
/usr/lib64/qt5/qml/QtNfc/plugins.qmltypes
/usr/lib64/qt5/qml/QtNfc/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/qtconnectivity/LICENSE.FDL
/usr/share/doc/qtconnectivity/LICENSE.GPL2
/usr/share/doc/qtconnectivity/LICENSE.GPL3
/usr/share/doc/qtconnectivity/LICENSE.GPL3-EXCEPT
/usr/share/doc/qtconnectivity/LICENSE.LGPL3
