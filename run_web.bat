@echo off
echo ========================================================
echo  Launching Online Quiz Management Web Application
echo ========================================================

rem Check if compiled
if not exist bin\com\ait\quiz\web\QuizWebServer.class (
    echo Compiling web server and classes...
    call compile.bat
)

echo Starting embedded Java Web Server on port 8080...
start "" "http://localhost:8080"
java -cp bin com.ait.quiz.web.QuizWebServer 8080

pause
