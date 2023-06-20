Name:          kylin-photo-viewer
Version:       1.2.0
Release:       3
Summary:       kylin-photo-viewer
License:       BSL-1.0 and Libpng and zlib and GPL-2.0-or-later
URL:           https://github.com/UbuntuKylin/kylin-photo-viewer
Source0:       %{name}-%{version}.tar.gz
Patch01:       0001-fix-compile-error-of-kylin-photo-viewer.patch
Patch02:       0002-fix-clang.patch

BuildRequires: qt5-qtbase-devel
BuildRequires: qtchooser
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: opencv
BuildRequires: qt5-qtsvg-devel
BuildRequires: stb-devel
BuildRequires: giflib-devel
BuildRequires: libpng-devel
BuildRequires: freeimage-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: gsettings-qt-devel
BuildRequires: ukui-interface
BuildRequires: glib2-devel
BuildRequires: peony libpeony-dev

%description
Photo viewer, support to view, zoom and rotate images of various formats

%prep
%autosetup -p1

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%if "%toolchain" == "clang"
%{qmake_qt5} -spec linux-clang ..
%else 
%{qmake_qt5} ..
%endif
%{make_build}
popd 

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 

mkdir -p %{buildroot}/usr/share/kylin-user-guide/data/guide

cp -r %{_builddir}/%{name}-%{version}/data/pictures %{buildroot}/usr/share/kylin-user-guide/data/guide/

%post
glib-compile-schemas /usr/share/glib-2.0/schemas &> /dev/null ||:

%files
%{_bindir}/kylin-photo-viewer
%{_includedir}/kylin_image_codec/kylinimagecodec.h
%{_includedir}/kylin_image_codec/kylinimagecodec_global.h
%{_includedir}/kylin_image_codec/loadmovie.h
%{_includedir}/kylin_image_codec/savemovie.h
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
%{_datadir}/kylin-photo-viewer/translations/kylin-photo-viewer_bo_CN.qm
%{_datadir}/pixmaps/kyview_logo.png
%{_datadir}/kylin-user-guide/data/guide/

%changelog
* Tue Jun 20 2023 yoo <sunyuechi@iscas.ac.cn> - 1.2.0-3
- fix clang build error

* Wed Feb 1 2023 peijiankang <peijiankang@kylinos.cn> - 1.2.0-2
- add build debuginfo and debugsource

* Mon Oct 24 2022 tanyulong <tanyulong@kylinos.cn> - 1.2.0-1
- update upstream version 1.2.0

* Thu Jun 9 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.2-4
- add kylin-user-guide file

* Thu Jun 9 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.2-3
- Fix the version of kylin-photo-viewer

* Thu May 26 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.2-2
- remove {%if 0 and %endif}

* Fri May 20 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.2-1
- Init kylin-photo-viewer package for openEuler
