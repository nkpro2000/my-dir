@echo off
setlocal
  REM set "JAVA_HOME=%UserProfile%\nk\Dev\oaks\java\jdk"
  REM echo I^ JAVA_HOME = "%JAVA_HOME%"
  set "IDEA_PROPERTIES=%UserProfile%\nk\Dev\code\ides\idea\work-idea.properties"
  echo I^> IDEA_PROPERTIES = "%IDEA_PROPERTIES%"
  echo $^> call "%UserProfile%\nk\Dev\bin\ides\idea\bin\idea.bat" nosplash %*
  call "%UserProfile%\nk\Dev\bin\ides\idea\bin\idea.bat" nosplash %*
endlocal
@REM https://intellij-support.jetbrains.com/hc/en-us/articles/207240985-Changing-IDE-default-directories-used-for-config-plugins-and-caches-storage
