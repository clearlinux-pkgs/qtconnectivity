#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtconnectivity
Version  : 5.15.2
Release  : 28
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtconnectivity-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtconnectivity-everywhere-src-5.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtconnectivity-bin = %{version}-%{release}
Requires: qtconnectivity-lib = %{version}-%{release}
Requires: qtconnectivity-license = %{version}-%{release}
BuildRequires : bluez-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
Patch1: qtconnectivity-stable-branch.patch

%description
# HeartRateGame #
Demonstrates how to check a Bluetooth-connection, discover LE-devices, connect
to devices, discover services and finally connect to a heartrate-service.
The purpose of the game is increase the heartrate so much as possible in 60s.
Relax before starting the game. Don't be too nervous, it increases the heartrate!

%package bin
Summary: bin components for the qtconnectivity package.
Group: Binaries
Requires: qtconnectivity-license = %{version}-%{release}

%description bin
bin components for the qtconnectivity package.


%package dev
Summary: dev components for the qtconnectivity package.
Group: Development
Requires: qtconnectivity-lib = %{version}-%{release}
Requires: qtconnectivity-bin = %{version}-%{release}
Provides: qtconnectivity-devel = %{version}-%{release}
Requires: qtconnectivity = %{version}-%{release}

%description dev
dev components for the qtconnectivity package.


%package examples
Summary: examples components for the qtconnectivity package.
Group: Default
Requires: qtconnectivity-dev = %{version}-%{release}

%description examples
examples components for the qtconnectivity package.


%package lib
Summary: lib components for the qtconnectivity package.
Group: Libraries
Requires: qtconnectivity-license = %{version}-%{release}

%description lib
lib components for the qtconnectivity package.


%package license
Summary: license components for the qtconnectivity package.
Group: Default

%description license
license components for the qtconnectivity package.


%prep
%setup -q -n qtconnectivity-everywhere-src-5.15.2
cd %{_builddir}/qtconnectivity-everywhere-src-5.15.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1647100823
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtconnectivity
cp %{_builddir}/qtconnectivity-everywhere-src-5.15.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtconnectivity/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtconnectivity-everywhere-src-5.15.2/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtconnectivity/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtconnectivity-everywhere-src-5.15.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtconnectivity/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtconnectivity-everywhere-src-5.15.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtconnectivity/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtconnectivity-everywhere-src-5.15.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtconnectivity/f45ee1c765646813b442ca58de72e20a64a7ddba
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sdpscanner

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/adapter1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/adapter_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/agent_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/androidbroadcastreceiver_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/battery1_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/bluetoothmanagement_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/bluez5_helper_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/bluez_data_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/btdelegates_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/btraii_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/device1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/device_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/devicediscoverybroadcastreceiver_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/dummy_helper_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/gattchar1_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/gattdesc1_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/gattservice1_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/hcimanager_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/inputstreamthread_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/jni_android_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/lecmaccalculator_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/localdevicebroadcastreceiver_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/lowenergynotificationhub_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/manager_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/obex_agent_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/obex_client1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/obex_client_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/obex_manager_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/obex_objectpush1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/obex_transfer1_bluez5_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/obex_transfer_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/objectmanager_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbluetooth_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtcentralmanager_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtconnectionmonitor_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtdeviceinquiry_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtdevicepair_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtgcdtimer_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtl2capchannel_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtledeviceinquiry_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtnotifier_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtobexsession_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtperipheralmanager_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtrfcommchannel_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtsdpinquiry_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtservicerecord_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtsocketlistener_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/osxbtutility_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/profile1_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/profile1context_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/profilemanager1_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/properties_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothaddress_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothdevicediscoveryagent_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothdeviceinfo_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothhostinfo_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothlocaldevice_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothserver_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothservicediscoveryagent_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothserviceinfo_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothsocket_android_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothsocket_bluez_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothsocket_bluezdbus_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothsocket_dummy_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothsocket_osx_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothsocket_win_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothsocket_winrt_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothsocketbase_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothtransferreply_bluez_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothtransferreply_osx_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothtransferreply_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothtransferrequest_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qbluetoothutils_winrt_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qleadvertiser_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontroller_android_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontroller_bluez_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontroller_bluezdbus_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontroller_darwin_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontroller_dummy_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontroller_win_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontroller_winrt_new_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontroller_winrt_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergycontrollerbase_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qlowenergyserviceprivate_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qprivatelinearbuffer_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qtbluetooth-config_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qtbluetoothglobal_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/qwinlowenergybluetooth_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/remotedevicemanager_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/serveracceptancethread_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/service_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/servicediscoverybroadcastreceiver_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/servicemap_p.h
/usr/include/qt5/QtBluetooth/5.15.2/QtBluetooth/private/uistrings_p.h
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
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/adapter_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/agent_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/androidjninfc_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/androidmainnewintentlistener_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/dbusobjectmanager_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/dbusproperties_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/manager_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/neard_helper_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qllcpserver_android_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qllcpserver_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qllcpserver_p_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qllcpsocket_android_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qllcpsocket_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qllcpsocket_p_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qndefnfcsmartposterrecord_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qndefrecord_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldmanager_android_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldmanager_emulator_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldmanager_neard_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldmanager_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldmanagerimpl_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldmanagervirtualbase_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldsharemanager_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldsharemanagerimpl_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldsharetarget_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldsharetargetimpl_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldtagtype1_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldtagtype2_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldtagtype3_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldtagtype4_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldtarget_android_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldtarget_emulator_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldtarget_neard_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qnearfieldtarget_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qtlv_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/qtnfcglobal_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/tag_p.h
/usr/include/qt5/QtNfc/5.15.2/QtNfc/private/targetemulator_p.h
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

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/bluetooth/bluetooth.pro
/usr/share/qt5/examples/bluetooth/btchat/btchat.pro
/usr/share/qt5/examples/bluetooth/btchat/chat.cpp
/usr/share/qt5/examples/bluetooth/btchat/chat.h
/usr/share/qt5/examples/bluetooth/btchat/chat.ui
/usr/share/qt5/examples/bluetooth/btchat/chatclient.cpp
/usr/share/qt5/examples/bluetooth/btchat/chatclient.h
/usr/share/qt5/examples/bluetooth/btchat/chatserver.cpp
/usr/share/qt5/examples/bluetooth/btchat/chatserver.h
/usr/share/qt5/examples/bluetooth/btchat/main.cpp
/usr/share/qt5/examples/bluetooth/btchat/remoteselector.cpp
/usr/share/qt5/examples/bluetooth/btchat/remoteselector.h
/usr/share/qt5/examples/bluetooth/btchat/remoteselector.ui
/usr/share/qt5/examples/bluetooth/btfiletransfer/btfiletransfer.pro
/usr/share/qt5/examples/bluetooth/btfiletransfer/btfiletransfer.qrc
/usr/share/qt5/examples/bluetooth/btfiletransfer/busy.gif
/usr/share/qt5/examples/bluetooth/btfiletransfer/main.cpp
/usr/share/qt5/examples/bluetooth/btfiletransfer/pairing.gif
/usr/share/qt5/examples/bluetooth/btfiletransfer/pindisplay.cpp
/usr/share/qt5/examples/bluetooth/btfiletransfer/pindisplay.h
/usr/share/qt5/examples/bluetooth/btfiletransfer/pindisplay.ui
/usr/share/qt5/examples/bluetooth/btfiletransfer/progress.cpp
/usr/share/qt5/examples/bluetooth/btfiletransfer/progress.h
/usr/share/qt5/examples/bluetooth/btfiletransfer/progress.ui
/usr/share/qt5/examples/bluetooth/btfiletransfer/remoteselector.cpp
/usr/share/qt5/examples/bluetooth/btfiletransfer/remoteselector.h
/usr/share/qt5/examples/bluetooth/btfiletransfer/remoteselector.ui
/usr/share/qt5/examples/bluetooth/btscanner/btscanner.pro
/usr/share/qt5/examples/bluetooth/btscanner/device.cpp
/usr/share/qt5/examples/bluetooth/btscanner/device.h
/usr/share/qt5/examples/bluetooth/btscanner/device.ui
/usr/share/qt5/examples/bluetooth/btscanner/main.cpp
/usr/share/qt5/examples/bluetooth/btscanner/service.cpp
/usr/share/qt5/examples/bluetooth/btscanner/service.h
/usr/share/qt5/examples/bluetooth/btscanner/service.ui
/usr/share/qt5/examples/bluetooth/chat/Button.qml
/usr/share/qt5/examples/bluetooth/chat/InputBox.qml
/usr/share/qt5/examples/bluetooth/chat/Search.qml
/usr/share/qt5/examples/bluetooth/chat/chat.pro
/usr/share/qt5/examples/bluetooth/chat/chat.qml
/usr/share/qt5/examples/bluetooth/chat/chat.qrc
/usr/share/qt5/examples/bluetooth/chat/images/clear.png
/usr/share/qt5/examples/bluetooth/chat/images/default.png
/usr/share/qt5/examples/bluetooth/chat/images/lineedit-bg.png
/usr/share/qt5/examples/bluetooth/chat/qmlchat.cpp
/usr/share/qt5/examples/bluetooth/heartrate-game/bluetoothbaseclass.cpp
/usr/share/qt5/examples/bluetooth/heartrate-game/bluetoothbaseclass.h
/usr/share/qt5/examples/bluetooth/heartrate-game/connectionhandler.cpp
/usr/share/qt5/examples/bluetooth/heartrate-game/connectionhandler.h
/usr/share/qt5/examples/bluetooth/heartrate-game/devicefinder.cpp
/usr/share/qt5/examples/bluetooth/heartrate-game/devicefinder.h
/usr/share/qt5/examples/bluetooth/heartrate-game/devicehandler.cpp
/usr/share/qt5/examples/bluetooth/heartrate-game/devicehandler.h
/usr/share/qt5/examples/bluetooth/heartrate-game/deviceinfo.cpp
/usr/share/qt5/examples/bluetooth/heartrate-game/deviceinfo.h
/usr/share/qt5/examples/bluetooth/heartrate-game/heartrate-game.pro
/usr/share/qt5/examples/bluetooth/heartrate-game/heartrate-global.h
/usr/share/qt5/examples/bluetooth/heartrate-game/images.qrc
/usr/share/qt5/examples/bluetooth/heartrate-game/main.cpp
/usr/share/qt5/examples/bluetooth/heartrate-game/qml.qrc
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/App.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/BluetoothAlarmDialog.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/BottomLine.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/Connect.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/GameButton.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/GamePage.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/GameSettings.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/Measure.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/SplashScreen.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/Stats.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/StatsLabel.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/TitleBar.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/images/bt_off_to_on.png
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/images/heart.png
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/images/logo.png
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/main.qml
/usr/share/qt5/examples/bluetooth/heartrate-game/qml/qmldir
/usr/share/qt5/examples/bluetooth/heartrate-server/heartrate-server.pro
/usr/share/qt5/examples/bluetooth/heartrate-server/main.cpp
/usr/share/qt5/examples/bluetooth/lowenergyscanner/assets/Characteristics.qml
/usr/share/qt5/examples/bluetooth/lowenergyscanner/assets/Dialog.qml
/usr/share/qt5/examples/bluetooth/lowenergyscanner/assets/Header.qml
/usr/share/qt5/examples/bluetooth/lowenergyscanner/assets/Label.qml
/usr/share/qt5/examples/bluetooth/lowenergyscanner/assets/Menu.qml
/usr/share/qt5/examples/bluetooth/lowenergyscanner/assets/Services.qml
/usr/share/qt5/examples/bluetooth/lowenergyscanner/assets/busy_dark.png
/usr/share/qt5/examples/bluetooth/lowenergyscanner/assets/main.qml
/usr/share/qt5/examples/bluetooth/lowenergyscanner/characteristicinfo.cpp
/usr/share/qt5/examples/bluetooth/lowenergyscanner/characteristicinfo.h
/usr/share/qt5/examples/bluetooth/lowenergyscanner/device.cpp
/usr/share/qt5/examples/bluetooth/lowenergyscanner/device.h
/usr/share/qt5/examples/bluetooth/lowenergyscanner/deviceinfo.cpp
/usr/share/qt5/examples/bluetooth/lowenergyscanner/deviceinfo.h
/usr/share/qt5/examples/bluetooth/lowenergyscanner/lowenergyscanner.pro
/usr/share/qt5/examples/bluetooth/lowenergyscanner/main.cpp
/usr/share/qt5/examples/bluetooth/lowenergyscanner/resources.qrc
/usr/share/qt5/examples/bluetooth/lowenergyscanner/serviceinfo.cpp
/usr/share/qt5/examples/bluetooth/lowenergyscanner/serviceinfo.h
/usr/share/qt5/examples/bluetooth/picturetransfer/Button.qml
/usr/share/qt5/examples/bluetooth/picturetransfer/DeviceDiscovery.qml
/usr/share/qt5/examples/bluetooth/picturetransfer/FileSending.qml
/usr/share/qt5/examples/bluetooth/picturetransfer/PictureSelector.qml
/usr/share/qt5/examples/bluetooth/picturetransfer/background.png
/usr/share/qt5/examples/bluetooth/picturetransfer/bttransfer.qml
/usr/share/qt5/examples/bluetooth/picturetransfer/filetransfer.cpp
/usr/share/qt5/examples/bluetooth/picturetransfer/filetransfer.h
/usr/share/qt5/examples/bluetooth/picturetransfer/icon.png
/usr/share/qt5/examples/bluetooth/picturetransfer/main.cpp
/usr/share/qt5/examples/bluetooth/picturetransfer/picturetransfer.pro
/usr/share/qt5/examples/bluetooth/picturetransfer/qmltransfer.qrc
/usr/share/qt5/examples/bluetooth/pingpong/assets/Board.qml
/usr/share/qt5/examples/bluetooth/pingpong/assets/Dialog.qml
/usr/share/qt5/examples/bluetooth/pingpong/assets/Menu.qml
/usr/share/qt5/examples/bluetooth/pingpong/assets/main.qml
/usr/share/qt5/examples/bluetooth/pingpong/main.cpp
/usr/share/qt5/examples/bluetooth/pingpong/pingpong.cpp
/usr/share/qt5/examples/bluetooth/pingpong/pingpong.h
/usr/share/qt5/examples/bluetooth/pingpong/pingpong.pro
/usr/share/qt5/examples/bluetooth/pingpong/resource.qrc
/usr/share/qt5/examples/bluetooth/scanner/Button.qml
/usr/share/qt5/examples/bluetooth/scanner/default.png
/usr/share/qt5/examples/bluetooth/scanner/qmlscanner.cpp
/usr/share/qt5/examples/bluetooth/scanner/scanner.pro
/usr/share/qt5/examples/bluetooth/scanner/scanner.qml
/usr/share/qt5/examples/bluetooth/scanner/scanner.qrc
/usr/share/qt5/examples/nfc/annotatedurl/annotatedurl.cpp
/usr/share/qt5/examples/nfc/annotatedurl/annotatedurl.h
/usr/share/qt5/examples/nfc/annotatedurl/annotatedurl.pro
/usr/share/qt5/examples/nfc/annotatedurl/main.cpp
/usr/share/qt5/examples/nfc/annotatedurl/mainwindow.cpp
/usr/share/qt5/examples/nfc/annotatedurl/mainwindow.h
/usr/share/qt5/examples/nfc/annotatedurl/mainwindow.ui
/usr/share/qt5/examples/nfc/corkboard/Mode.qml
/usr/share/qt5/examples/nfc/corkboard/NfcFlag.png
/usr/share/qt5/examples/nfc/corkboard/android/AndroidManifest.xml
/usr/share/qt5/examples/nfc/corkboard/cork.jpg
/usr/share/qt5/examples/nfc/corkboard/corkboard.pro
/usr/share/qt5/examples/nfc/corkboard/corkboard.qrc
/usr/share/qt5/examples/nfc/corkboard/corkboards.qml
/usr/share/qt5/examples/nfc/corkboard/icon.png
/usr/share/qt5/examples/nfc/corkboard/main.cpp
/usr/share/qt5/examples/nfc/corkboard/note-yellow.png
/usr/share/qt5/examples/nfc/corkboard/tack.png
/usr/share/qt5/examples/nfc/ndefeditor/main.cpp
/usr/share/qt5/examples/nfc/ndefeditor/mainwindow.cpp
/usr/share/qt5/examples/nfc/ndefeditor/mainwindow.h
/usr/share/qt5/examples/nfc/ndefeditor/mainwindow.ui
/usr/share/qt5/examples/nfc/ndefeditor/mimeimagerecordeditor.cpp
/usr/share/qt5/examples/nfc/ndefeditor/mimeimagerecordeditor.h
/usr/share/qt5/examples/nfc/ndefeditor/mimeimagerecordeditor.ui
/usr/share/qt5/examples/nfc/ndefeditor/ndefeditor.pro
/usr/share/qt5/examples/nfc/ndefeditor/textrecordeditor.cpp
/usr/share/qt5/examples/nfc/ndefeditor/textrecordeditor.h
/usr/share/qt5/examples/nfc/ndefeditor/textrecordeditor.ui
/usr/share/qt5/examples/nfc/ndefeditor/urirecordeditor.cpp
/usr/share/qt5/examples/nfc/ndefeditor/urirecordeditor.h
/usr/share/qt5/examples/nfc/ndefeditor/urirecordeditor.ui
/usr/share/qt5/examples/nfc/nfc.pro
/usr/share/qt5/examples/nfc/poster/poster.pro
/usr/share/qt5/examples/nfc/poster/poster.qml
/usr/share/qt5/examples/nfc/poster/poster.qrc
/usr/share/qt5/examples/nfc/poster/qmlposter.cpp

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Bluetooth.so.5
/usr/lib64/libQt5Bluetooth.so.5.15
/usr/lib64/libQt5Bluetooth.so.5.15.2
/usr/lib64/libQt5Nfc.so.5
/usr/lib64/libQt5Nfc.so.5.15
/usr/lib64/libQt5Nfc.so.5.15.2
/usr/lib64/qt5/qml/QtBluetooth/libdeclarative_bluetooth.so
/usr/lib64/qt5/qml/QtBluetooth/plugins.qmltypes
/usr/lib64/qt5/qml/QtBluetooth/qmldir
/usr/lib64/qt5/qml/QtNfc/libdeclarative_nfc.so
/usr/lib64/qt5/qml/QtNfc/plugins.qmltypes
/usr/lib64/qt5/qml/QtNfc/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtconnectivity/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtconnectivity/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtconnectivity/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtconnectivity/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtconnectivity/f45ee1c765646813b442ca58de72e20a64a7ddba
