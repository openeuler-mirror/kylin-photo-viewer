%define debug_package %{nil}
Name:           kylin-photo-viewer
Version:        1.0.2
Release:        1
Summary:        kylin-photo-viewer
License:        GPL-3.0-or-later
URL:            https://github.com/UbuntuKylin/kylin-photo-viewer
Source0:        %{name}-%{version}.tar.gz

%if 0
BuildRequires: qt5-qtbase-devel
BuildRequires: qtchooser
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-linguist
BuildRequires: opencv
BuildRequires: qt5-qtsvg-devel
BuildRequires: giflib-devel
BuildRequires: libpng-devel
BuildRequires: freeimage-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: gsettings-qt-devel
BuildRequires: ukui-interface
BuildRequires: glib2-devel
BuildRequires: libpeony-dev
%endif

%description
Photo viewer, support to view, zoom and rotate images of various formats

%prep
%setup -q

%build
%if 0
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd 

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 
%endif
%files
%if 0
%{_bindir}/kylin-photo-viewer
%{_includedir}/kylin_image_codec/kylinimagecodec.h
%{_includedir}/kylin_image_codec/kylinimagecodec_global.h
%{_includedir}/kylin_image_codec/loadmovie.h
%{_includedir}/kylin_image_codec/savemovie.h
%{_includedir}/kylin_image_codec/stb_image.h
%{_includedir}/kylin_image_codec/stb_image_write.h
%{_prefix}/lib/libkylinimagecodec.so
%{_prefix}/lib/libkylinimagecodec.so.1
%{_prefix}/lib/libkylinimagecodec.so.1.0
%{_prefix}/lib/libkylinimagecodec.so.1.0.0
%{_libdir}/cmake/Qt5Gui/Qt5Gui_ApngImagePlugin.cmake
%{_libdir}/qt5/plugins/imageformats/libqapng.so
%{_datadir}/applications/kylin-photo-viewer.desktop
%{_datadir}/glib-2.0/schemas/org.kylin.photo.viewer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.log4qt.kylin-photo-viewer.gschema.xml
%{_datadir}/kylin-photo-viewer/translations/kylin-photo-viewer_zh_CN.qm
%{_datadir}/pixmaps/kyview_logo.png
%endif

%changelog
* Fri May 20 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.2-1
- Init kylin-photo-viewer package for openEuler
