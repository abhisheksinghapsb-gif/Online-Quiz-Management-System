@echo off
echo ========================================================
echo  Compiling Online Quiz Management System (CIE-2)
echo ========================================================

if not exist bin mkdir bin

javac -d bin src\com\ait\quiz\exception\*.java src\com\ait\quiz\model\*.java src\com\ait\quiz\service\*.java src\com\ait\quiz\util\*.java src\com\ait\quiz\main\*.java src\com\ait\quiz\web\*.java

if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Compilation finished with 0 errors!
    echo Run 'run.bat' for Console mode.
    echo Run 'run_web.bat' for Web Browser mode.
) else (
    echo [ERROR] Compilation failed! Check error messages above.
)
