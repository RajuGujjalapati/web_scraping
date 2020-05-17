


@echo off

@rem unset these variables
@set WindowsSdkDir=
@set WindowsSDK_ExecutablePath_x64=
@set WindowsSDK_ExecutablePath_x86=
@set Framework40Version=
@set FrameworkDIR32=
@set FrameworkVersion32=
@set FSHARPINSTALLDIR=
@set VSINSTALLDIR=
@set VCINSTALLDIR=

@rem Add path to MSBuild Binaries
@if exist "%ProgramFiles%\MSBuild\14.0\bin" set PATH=%ProgramFiles%\MSBuild\14.0\bin;%PATH%
@if exist "%ProgramFiles(x86)%\MSBuild\14.0\bin" set PATH=%ProgramFiles(x86)%\MSBuild\14.0\bin;%PATH%

@goto end

:end
