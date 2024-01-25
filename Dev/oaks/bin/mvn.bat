@echo off
setlocal
  set "JAVA_HOME=%UserProfile%\nk\Dev\oaks\java\jdk"
  echo I^> JAVA_HOME = "%JAVA_HOME%"
  echo $^> call "%UserProfile%\nk\Dev\oaks\maven\mvn\bin\mvn.cmd" --settings "%UserProfile%\nk\Dev\oaks\maven\settings.xml" --toolchains "%UserProfile%\nk\Dev\oaks\maven\toolchains.xml" %*
  call "%UserProfile%\nk\Dev\oaks\maven\mvn\bin\mvn.cmd" --settings "%UserProfile%\nk\Dev\oaks\maven\settings.xml" --toolchains "%UserProfile%\nk\Dev\oaks\maven\toolchains.xml" %*
endlocal
@REM https://stackoverflow.com/questions/16649420/how-to-specify-an-alternate-location-for-the-m2-folder-or-settings-xml-permanen https://stackoverflow.com/a/27503199
@REM ../java/jdk & ../maven/mvn are /D(https://superuser.com/questions/343074/directory-junction-vs-directory-symbolic-link), so easly changed default versions.
