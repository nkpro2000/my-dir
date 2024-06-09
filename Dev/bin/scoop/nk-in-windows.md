# ~/nk

## clone
* ~/nk/.git/config
* ~/nk/.git/info/sparse-checkout
* ~/nk/.git/info/exclude
```console
naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ git config -l
core.symlinks=false
core.autocrlf=true
core.fscache=true
color.interactive=true
color.ui=auto
help.format=html
diff.astextplain.textconv=astextplain
rebase.autosquash=true
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
credential.helper=helper-selector
credential.helperselector.selected=<no helper>
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
core.protectntfs=false
core.sparsecheckout=true
remote.origin.url=https://github.com/nkpro2000/my-dir
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ git sparse-checkout list
/*
!/Dev/bin/<any_code_editor>
!/.assets/NK.ico
!/.assets/NK.png

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ git ls-files | diff - <(git ls-files | git sparse-checkout check-rules)
3,4d2
< .assets/NK.ico
< .assets/NK.png
8,9d5
< .assets/nk.ico
< .assets/nk.png
22,23d17
< Dev/bin/<any_code_editor>/bin/.gitkeep
< Dev/bin/<any_code_editor>/data

```
`$ git checkout`

## icons
```console
naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ ls -a
.  ..  .assets  .git  .gitignore  .secrets  .unsat  Dev
Notes  Setup  desktop.ini  nk.py  setup-nk.py  todo.md

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ bat desktop.ini
───────┬───────────────────────────────────────────────────────────────────────
       │ File: desktop.ini
───────┼───────────────────────────────────────────────────────────────────────
   1   │ [.ShellClassInfo]
   2   │ IconResource=C:\Users\naveen.s.r\nk\.assets\NewK.ico,0
   3   │ [ViewState]
   4   │ Mode=
   5   │ Vid=
   6   │ FolderType=Generic
───────┴───────────────────────────────────────────────────────────────────────

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ ls -a Dev
.  ..  Envs  bin  code  desktop.ini  jupyter  lobby  oaks  tex

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ bat Dev/desktop.ini
───────┬───────────────────────────────────────────────────────────────────────
       │ File: Dev/desktop.ini
───────┼───────────────────────────────────────────────────────────────────────
   1   │ [.ShellClassInfo]
   2   │ IconResource=C:\Users\naveen.s.r\nk\.assets\Dev.ico,0
   3   │ [ViewState]
   4   │ Mode=
   5   │ Vid=
   6   │ FolderType=Generic
───────┴───────────────────────────────────────────────────────────────────────

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ ls -a Notes
.  ..  .gitkeep  desktop.ini

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ bat Notes/desktop.ini
───────┬───────────────────────────────────────────────────────────────────────
       │ File: Notes/desktop.ini
───────┼───────────────────────────────────────────────────────────────────────
   1   │ [.ShellClassInfo]
   2   │ IconResource=C:\Users\naveen.s.r\nk\.assets\Notes.ico,0
   3   │ [ViewState]
   4   │ Mode=
   5   │ Vid=
   6   │ FolderType=Generic
───────┴───────────────────────────────────────────────────────────────────────

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ ls -a Setup
.  ..  Dolphin  Panel  Sh  Tty  desktop.ini

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ bat Setup/desktop.ini
───────┬───────────────────────────────────────────────────────────────────────
       │ File: Setup/desktop.ini
───────┼───────────────────────────────────────────────────────────────────────
   1   │ [.ShellClassInfo]
   2   │ IconResource=C:\Users\naveen.s.r\nk\.assets\nk_.ico,0
   3   │ [ViewState]
   4   │ Mode=
   5   │ Vid=
   6   │ FolderType=Generic
───────┴───────────────────────────────────────────────────────────────────────

naveen.s.r@CDC2-L-FR80F63 MINGW64 ~/nk (master|SPARSE)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

You are in a sparse checkout with 90% of tracked files present.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Dev/bin/scoop/
        todo.md

no changes added to commit (use "git add" and/or "git commit -a")

```

# Scoop
```md
# Dev/bin
.path  
.generate_path  
code -> <any_code_editor> './code/bin'  
<any_code_editor>/  
## scoop
.install-si/              https://github.com/ScoopInstaller/Install  
dir/                      './scoop/dir/shims'x `SCOOP`x  
persist-in-windows/       to hardlink other files
 (has: home-dir/ and other script to MKLINK [[/D] | [/H] | [/J]])  
nk-in-windows.md          to doc changes  
```
```console
$ scoop list
Installed apps:

Name Version Source Updated             Info
---- ------- ------ -------             ----
7zip 23.01   main   2024-01-20 12:05:14
nano 7.2-22.1 main   2024-01-21 16:39:25
bat  0.24.0  main   2024-01-20 12:02:53
git  2.43.0  main   2024-01-20 12:13:04
pwsh 7.4.1   main   2024-01-20 12:44:05
```
```pwsh
> $env:PATH = 'C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\shims' + $env:PATH
> $env:GIT_INSTALL_ROOT = 'C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\git\current'
```
> added automatically by Scoop while installing, its just a syntatical description.

# Oaks (Java, Maven)
```md
# Dev/oaks
## bin
mvn.bat
## java
jdk\\->  `JAVA_HOME`x
## maven
mvn\\->  `MAVEN_HOME`x  
localRepo                 for localRepository in v  
settings.xml              User-level Profile  
toolchains.xml            User-level ToolChain  
> https://maven.apache.org/guides/introduction/introduction-to-profiles.html
```
```console
PS C:\Users\naveen.s.r> mvn -v
I> JAVA_HOME = "C:\Users\naveen.s.r\nk\Dev\oaks\java\jdk"
$> call "C:\Users\naveen.s.r\nk\Dev\oaks\maven\mvn\bin\mvn.cmd" --settings "C:\Users\naveen.s.r\nk\Dev\oaks\maven\settings.xml" -v
Apache Maven 3.9.6 (bc0240f3c744dd6b6ec2920b3cd08dcc295161ae)
Maven home: C:\Users\naveen.s.r\nk\Dev\oaks\maven\mvn
Java version: 21.0.1, vendor: Oracle Corporation, runtime: C:\Users\naveen.s.r\nk\Dev\oaks\java\jdk
Default locale: en_US, platform encoding: UTF-8
OS name: "windows 11", version: "10.0", arch: "amd64", family: "windows"
```
added `%UserProfile%\nk\Dev\oaks\bin` to PATH

# IDEs
## Idea (jetBrains)
```md
# Dev/bin
code/bin/
## ides
idea\\->  `IDEA_HOME`x
### bin
idea.bat  
idew.bat  
# Dev/code
data <- ../bin/code/data
## ides
### idea
data-idea.properties  
data/{config,system,plugins}  
work-idea.properties  
work/{config,system,plugins}  
```
```console
PS C:\Users\naveen.s.r> where.exe git
C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\shims\git.exe
PS C:\Users\naveen.s.r> where.exe mvn
C:\Users\naveen.s.r\nk\Dev\oaks\bin\mvn.bat
PS C:\Users\naveen.s.r> where.exe idea
C:\Users\naveen.s.r\nk\Dev\bin\ides\bin\idea.bat
PS C:\Users\naveen.s.r> idea --version
I> IDEA_PROPERTIES = "C:\Users\naveen.s.r\nk\Dev\code\ides\idea\data-idea.properties"
$> call "C:\Users\naveen.s.r\nk\Dev\bin\ides\idea\bin\idea.bat" --version
CompileCommand: exclude com/intellij/openapi/vfs/impl/FilePartNodeRoot.trieDescend bool exclude = true
IntelliJ IDEA 2023.3.2 (Community Edition)
Build #IC-233.13135.103
```
added `%UserProfile%\nk\Dev\bin\ides\bin` to PATH

# Hardlink, Junctions, Symlinks and Symlink directories
> https://superuser.com/questions/343074/directory-junction-vs-directory-symbolic-link
```bash
find ./nk \
-type l -exec ls -ld {} \; \
-o \
-type f -links +1 -exec ls -ld {} \; \
-exec sh -c 'cmd //c fsutil hardlink list "$1" | grep -vF "$(echo "$1"|tr / \\\\|sed "s/^.//")" | sed "s/^/ hardlinked => /"' shell {} \;
```
> https://stackoverflow.com/questions/8513133/how-do-i-find-all-of-the-symlinks-in-a-directory-tree  
> https://superuser.com/questions/366739/how-can-i-find-hard-links-on-windows  
> https://superuser.com/questions/1413103/execute-cmd-command-with-shell  
```console
lrwxrwxrwx 1 naveen.s.r 1049089 18 Jan 25 18:05 ./nk/Dev/bin/code -> VSCodium-win32-x64
lrwxrwxrwx 1 naveen.s.r 1049089 16 Jan 25 15:32 ./nk/Dev/bin/ides/code -> VSCode-win32-x64
lrwxrwxrwx 1 naveen.s.r 1049089 17 Jan 20 21:09 ./nk/Dev/bin/ides/idea -> ./ideaIC-2023.3.2
lrwxrwxrwx 1 naveen.s.r 1049089 60 Jan 20 12:05 ./nk/Dev/bin/scoop/dir/apps/7zip/23.01/Codecs -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/persist/7zip/Codecs
lrwxrwxrwx 1 naveen.s.r 1049089 61 Jan 20 12:05 ./nk/Dev/bin/scoop/dir/apps/7zip/23.01/Formats -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/persist/7zip/Formats
lrwxrwxrwx 1 naveen.s.r 1049089 56 Jan 20 12:05 ./nk/Dev/bin/scoop/dir/apps/7zip/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/7zip/23.01
lrwxrwxrwx 1 naveen.s.r 1049089 56 Jan 20 12:02 ./nk/Dev/bin/scoop/dir/apps/bat/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/bat/0.24.0
-rw-r--r-- 2 naveen.s.r 1049089 8059 Jan 25 21:11 ./nk/Dev/bin/scoop/dir/apps/btop/1.0.4/btop.conf
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\btop\btop.conf
lrwxrwxrwx 1 naveen.s.r 1049089 60 Jan 25 21:02 ./nk/Dev/bin/scoop/dir/apps/btop/1.0.4/themes -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/persist/btop/themes
lrwxrwxrwx 1 naveen.s.r 1049089 56 Jan 25 21:02 ./nk/Dev/bin/scoop/dir/apps/btop/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/btop/1.0.4
lrwxrwxrwx 1 naveen.s.r 1049089 66 Jan 25 21:01 ./nk/Dev/bin/scoop/dir/apps/cheat/4.4.2/cheatsheets -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/persist/cheat/cheatsheets
-rw-r--r-- 2 naveen.s.r 1049089 3746 Jan 25 21:01 ./nk/Dev/bin/scoop/dir/apps/cheat/4.4.2/conf.yml
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\cheat\conf.yml
lrwxrwxrwx 1 naveen.s.r 1049089 57 Jan 25 21:01 ./nk/Dev/bin/scoop/dir/apps/cheat/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/cheat/4.4.2
lrwxrwxrwx 1 naveen.s.r 1049089 55 Jan 25 21:00 ./nk/Dev/bin/scoop/dir/apps/file/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/file/5.45
lrwxrwxrwx 1 naveen.s.r 1049089 61 Jan 25 21:00 ./nk/Dev/bin/scoop/dir/apps/findutils/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/findutils/4.4.2
lrwxrwxrwx 1 naveen.s.r 1049089 1 Jan 20 12:13 ./nk/Dev/bin/scoop/dir/apps/git/current -> /
lrwxrwxrwx 1 naveen.s.r 1049089 55 Jan 25 21:01 ./nk/Dev/bin/scoop/dir/apps/grep/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/grep/3.11
lrwxrwxrwx 1 naveen.s.r 1049089 59 Jan 21 16:39 ./nk/Dev/bin/scoop/dir/apps/nano/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/nano/7.2-22.1
lrwxrwxrwx 1 naveen.s.r 1049089 64 Jan 25 21:02 ./nk/Dev/bin/scoop/dir/apps/powersession/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/powersession/1.4.7
-rw-r--r-- 2 naveen.s.r 1049089 0 Jan 20 12:44 ./nk/Dev/bin/scoop/dir/apps/pwsh/7.4.1/Microsoft.PowerShell_profile.ps1
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\pwsh\Microsoft.PowerShell_profile.ps1
-rw-r--r-- 2 naveen.s.r 1049089 0 Jan 20 12:44 ./nk/Dev/bin/scoop/dir/apps/pwsh/7.4.1/Microsoft.VSCode_profile.ps1
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\pwsh\Microsoft.VSCode_profile.ps1
-rw-r--r-- 2 naveen.s.r 1049089 0 Jan 20 12:44 ./nk/Dev/bin/scoop/dir/apps/pwsh/7.4.1/profile.ps1
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\pwsh\profile.ps1
lrwxrwxrwx 1 naveen.s.r 1049089 56 Jan 20 12:44 ./nk/Dev/bin/scoop/dir/apps/pwsh/current -> /c/Users/naveen.s.r/nk/Dev/bin/scoop/dir/apps/pwsh/7.4.1
-rw-r--r-- 2 naveen.s.r 1049089 8059 Jan 25 21:11 ./nk/Dev/bin/scoop/dir/persist/btop/btop.conf
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop\1.0.4\btop.conf
-rw-r--r-- 2 naveen.s.r 1049089 3746 Jan 25 21:01 ./nk/Dev/bin/scoop/dir/persist/cheat/conf.yml
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat\4.4.2\conf.yml
-rw-r--r-- 2 naveen.s.r 1049089 0 Jan 20 12:44 ./nk/Dev/bin/scoop/dir/persist/pwsh/Microsoft.PowerShell_profile.ps1
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\pwsh\7.4.1\Microsoft.PowerShell_profile.ps1
-rw-r--r-- 2 naveen.s.r 1049089 0 Jan 20 12:44 ./nk/Dev/bin/scoop/dir/persist/pwsh/Microsoft.VSCode_profile.ps1
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\pwsh\7.4.1\Microsoft.VSCode_profile.ps1
-rw-r--r-- 2 naveen.s.r 1049089 0 Jan 20 12:44 ./nk/Dev/bin/scoop/dir/persist/pwsh/profile.ps1
 hardlinked => \Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\pwsh\7.4.1\profile.ps1
lrwxrwxrwx 1 naveen.s.r 1049089 15 Jan 25 15:35 ./nk/Dev/bin/VSCodium-win32-x64/data -> ../../code/data
lrwxrwxrwx 1 naveen.s.r 1049089 12 Jan 20 14:36 ./nk/Dev/oaks/java/jdk -> ./jdk-21.0.1
lrwxrwxrwx 1 naveen.s.r 1049089 20 Jan 20 14:48 ./nk/Dev/oaks/maven/mvn -> ./apache-maven-3.9.6
```
> https://superuser.com/questions/823959/how-to-view-all-the-symbolic-links-junction-points-hard-links-in-a-folder-usin
```console
PS C:\Users\naveen.s.r> cmd /c dir /al /s nk
 Volume in drive C is Windows
 Volume Serial Number is 568D-155F

 Directory of C:\Users\naveen.s.r\nk\Dev\bin

01/25/2024  06:05 PM    <SYMLINKD>     code [VSCodium-win32-x64]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\code

01/25/2024  03:35 PM    <SYMLINKD>     data [..\..\code\data]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\ides

01/25/2024  03:32 PM    <SYMLINKD>     code [VSCode-win32-x64]
01/20/2024  09:09 PM    <SYMLINKD>     idea [.\ideaIC-2023.3.2]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip

01/20/2024  12:05 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\23.01]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\23.01

01/20/2024  12:05 PM    <JUNCTION>     Codecs [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\7zip\Codecs]
01/20/2024  12:05 PM    <JUNCTION>     Formats [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\7zip\Formats]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\current

01/20/2024  12:05 PM    <JUNCTION>     Codecs [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\7zip\Codecs]
01/20/2024  12:05 PM    <JUNCTION>     Formats [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\7zip\Formats]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\bat

01/20/2024  12:02 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\bat\0.24.0]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop

01/25/2024  09:02 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop\1.0.4]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop\1.0.4

01/25/2024  09:02 PM    <JUNCTION>     themes [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\btop\themes]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop\current

01/25/2024  09:02 PM    <JUNCTION>     themes [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\btop\themes]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat

01/25/2024  09:01 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat\4.4.2]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat\4.4.2

01/25/2024  09:01 PM    <JUNCTION>     cheatsheets [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\cheat\cheatsheets]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat\current

01/25/2024  09:01 PM    <JUNCTION>     cheatsheets [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\cheat\cheatsheets]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\file

01/25/2024  09:00 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\file\5.45]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\findutils

01/25/2024  09:00 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\findutils\4.4.2]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\git

01/20/2024  12:13 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\git\2.43.0]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\grep

01/25/2024  09:01 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\grep\3.11]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\nano

01/21/2024  04:39 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\nano\7.2-22.1]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\powersession

01/25/2024  09:02 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\powersession\1.4.7]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\pwsh

01/20/2024  12:44 PM    <JUNCTION>     current [\??\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\pwsh\7.4.1]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\bin\VSCodium-win32-x64

01/25/2024  03:35 PM    <SYMLINKD>     data [..\..\code\data]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\oaks\java

01/20/2024  02:36 PM    <SYMLINKD>     jdk [.\jdk-21.0.1]
               0 File(s)              0 bytes

 Directory of C:\Users\naveen.s.r\nk\Dev\oaks\maven

01/20/2024  02:48 PM    <SYMLINKD>     mvn [.\apache-maven-3.9.6]
               0 File(s)              0 bytes

     Total Files Listed:
               0 File(s)              0 bytes
              26 Dir(s)  79,635,062,784 bytes free
PS C:\Users\naveen.s.r>
```
> https://learn.microsoft.com/en-us/sysinternals/downloads/junction
```console
PS C:\Users\naveen.s.r> .\nk\Lobby\junction.exe -s nk

Junction v1.07 - Creates and lists directory links
Copyright (C) 2005-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

.\\?\C:\Users\naveen.s.r\nk\Dev\bin\code: SYMBOLIC LINK
   Print Name     : VSCodium-win32-x64
   Substitute Name: VSCodium-win32-x64

\\?\C:\Users\naveen.s.r\nk\Dev\bin\code\data: SYMBOLIC LINK
   Print Name     : ..\..\code\data
   Substitute Name: ..\..\code\data

...\\?\C:\Users\naveen.s.r\nk\Dev\bin\ides\code: SYMBOLIC LINK
   Print Name     : VSCode-win32-x64
   Substitute Name: VSCode-win32-x64

\\?\C:\Users\naveen.s.r\nk\Dev\bin\ides\idea: SYMBOLIC LINK
   Print Name     : .\ideaIC-2023.3.2
   Substitute Name: .\ideaIC-2023.3.2

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\23.01

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\23.01\Codecs: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\7zip\Codecs

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\23.01\Formats: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\7zip\Formats

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\current\Codecs: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\7zip\Codecs

.\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\7zip\current\Formats: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\7zip\Formats

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\bat\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\bat\0.24.0

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop\1.0.4

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop\1.0.4\themes: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\btop\themes

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\btop\current\themes: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\btop\themes

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat\4.4.2

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat\4.4.2\cheatsheets: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\cheat\cheatsheets

.\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\cheat\current\cheatsheets: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\persist\cheat\cheatsheets

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\file\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\file\5.45

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\findutils\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\findutils\4.4.2

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\git\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\git\2.43.0

...\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\grep\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\grep\3.11

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\nano\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\nano\7.2-22.1

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\powersession\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\powersession\1.4.7

\\?\C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\pwsh\current: JUNCTION
   Substitute Name: C:\Users\naveen.s.r\nk\Dev\bin\scoop\dir\apps\pwsh\7.4.1

...\\?\C:\Users\naveen.s.r\nk\Dev\bin\VSCodium-win32-x64\data: SYMBOLIC LINK
   Print Name     : ..\..\code\data
   Substitute Name: ..\..\code\data

..\\?\C:\Users\naveen.s.r\nk\Dev\oaks\java\jdk: SYMBOLIC LINK
   Print Name     : .\jdk-21.0.1
   Substitute Name: .\jdk-21.0.1

\\?\C:\Users\naveen.s.r\nk\Dev\oaks\maven\mvn: SYMBOLIC LINK
   Print Name     : .\apache-maven-3.9.6
   Substitute Name: .\apache-maven-3.9.6

..
PS C:\Users\naveen.s.r>
```


# Notes
## cloning procedure
```console
PS C:\Users\naveen.s.r\Videos\Lobby> git clone https://github.com/nkpro2000/my-dir.git
Cloning into 'my-dir'...
remote: Enumerating objects: 483, done.
remote: Counting objects: 100% (483/483), done.
remote: Compressing objects: 100% (299/299), done.
remote: Total 483 (delta 238), reused 375 (delta 147), pack-reused 0
Receiving objects: 100% (483/483), 1.85 MiB | 24.96 MiB/s, done.
Resolving deltas: 100% (238/238), done.
error: invalid path 'Dev/bin/<any_code_editor>/bin/.gitkeep'
fatal: unable to checkout working tree
warning: Clone succeeded, but checkout failed.
You can inspect what was checked out with 'git status'
and retry with 'git restore --source=HEAD :/'

PS C:\Users\naveen.s.r\Videos\Lobby> cd .\my-dir\
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> ls
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> bat .\.git\*
───────┬───────────────────────────────────────────────────────────────────────────────
       │ File: .git\HEAD
───────┼───────────────────────────────────────────────────────────────────────────────
   1   │ ref: refs/heads/master
───────┴───────────────────────────────────────────────────────────────────────────────
───────┬───────────────────────────────────────────────────────────────────────────────
       │ File: .git\config
───────┼───────────────────────────────────────────────────────────────────────────────
   1   │ [core]
   2   │     repositoryformatversion = 0
   3   │     filemode = false
   4   │     bare = false
   5   │     logallrefupdates = true
   6   │     symlinks = false
   7   │     ignorecase = true
   8   │ [remote "origin"]
   9   │     url = https://github.com/nkpro2000/my-dir.git
  10   │     fetch = +refs/heads/*:refs/remotes/origin/*
  11   │ [branch "master"]
  12   │     remote = origin
  13   │     merge = refs/heads/master
───────┴───────────────────────────────────────────────────────────────────────────────
───────┬───────────────────────────────────────────────────────────────────────────────
       │ File: .git\description
───────┼───────────────────────────────────────────────────────────────────────────────
   1   │ Unnamed repository; edit this file 'description' to name the repository.
───────┴───────────────────────────────────────────────────────────────────────────────
[bat error]: '.git\hooks': Access is denied. (os error 5)
[bat error]: '.git\info': Access is denied. (os error 5)
[bat error]: '.git\logs': Access is denied. (os error 5)
[bat error]: '.git\objects': Access is denied. (os error 5)
───────┬───────────────────────────────────────────────────────────────────────────────
       │ File: .git\packed-refs
───────┼───────────────────────────────────────────────────────────────────────────────
   1   │ # pack-refs with: peeled fully-peeled sorted
   2   │ 1402d4840b71489f04d69a2d41a9c8e1b4518d1e refs/remotes/origin/master
───────┴───────────────────────────────────────────────────────────────────────────────
[bat error]: '.git\refs': Access is denied. (os error 5)
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> bat .\.git\info\*
───────┬───────────────────────────────────────────────────────────────────────────────
       │ File: .git\info\exclude
───────┼───────────────────────────────────────────────────────────────────────────────
   1   │ # git ls-files --others --exclude-from=.git/info/exclude
   2   │ # Lines that start with '#' are comments.
   3   │ # For a project mostly in C, the following would be a good set of
   4   │ # exclude patterns (uncomment them if you want to use them):
   5   │ # *.[oa]
   6   │ # *~
───────┴───────────────────────────────────────────────────────────────────────────────
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> cp ..\..\..\nk\.git\info\sparse-checkout .\.git\info\
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> bat .\.git\info\sparse-checkout
───────┬───────────────────────────────────────────────────────────────────────────────
       │ File: .\.git\info\sparse-checkout
───────┼───────────────────────────────────────────────────────────────────────────────
   1   │ /*
   2   │ !/Dev/bin/<any_code_editor>
   3   │ !/.assets/NK.ico
   4   │ !/.assets/NK.png
───────┴───────────────────────────────────────────────────────────────────────────────
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> git config core.protectNTFS false
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> git config core.sparseCheckout true
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> git checkout
Your branch is up to date with 'origin/master'.
PS C:\Users\naveen.s.r\Videos\Lobby\my-dir> tree /F /A
Folder PATH listing for volume Windows
Volume serial number is 568D-155F
C:.
|   .gitignore
|   .unsat
|   nk.py
|   setup-nk.py
|
+---.assets
|       Dev.ico
|       Dev.png
|       NewK.ico
|       nk_.ico
|       nk_.png
|       Notes.ico
|       Notes.png
|
+---.secrets
|       .gen
|       secret5.py
|       secret5.sh
|
+---Dev
|   +---bin
|   |   |   .generate_path
|   |   |   .path
|   |   |   code
|   |   |
|   |   +---ides
|   |   |   |   code
|   |   |   |   idea
|   |   |   |
|   |   |   \---bin
|   |   |           code.bat
|   |   |           codejs.bat
|   |   |           idea.bat
|   |   |           idew.bat
|   |   |
|   |   \---scoop
|   |       |   nk-in-windows.md
|   |       |
|   |       \---persist-in-windows
|   |               yet2do.scripts
|   |
|   +---code
|   |   +---data
|   |   |       .gitkeep
|   |   |
|   |   \---ides
|   |       +---code
|   |       |       .gitkeep
|   |       |
|   |       \---idea
|   |               data-idea.properties
|   |               work-idea.properties
|   |
|   +---Envs
|   |       Github.sh
|   |       Python.sh
|   |       Shell.sh
|   |
|   +---jupyter
|   |   +---.pyvenv
|   |   |       pyvenv.cfg
|   |   |
|   |   +---bin
|   |   |       jupy
|   |   |       saju
|   |   |
|   |   \---py
|   |       +---jupyter-data
|   |       |   \---kernels
|   |       |       \---python3-venv
|   |       |               kernel.json
|   |       |               logo-svg.svg
|   |       |
|   |       \---venv
|   |               pyvenv.cfg
|   |
|   +---lobby
|   |       .gitkeep
|   |
|   +---oaks
|   |   +---bin
|   |   |       mvn.bat
|   |   |
|   |   +---java
|   |   |       jdk
|   |   |
|   |   \---maven
|   |       |   mvn
|   |       |   settings.xml
|   |       |   toolchains.xml
|   |       |
|   |       \---localRepo
|   |               .gitkeep
|   |
|   \---tex
|       +---bin
|       |       teks
|       |
|       +---live
|       |   \---.install-tl
|       |           install.sh
|       |
|       \---repo
|           \---ctan-archive
|                   get-all.sh
|
+---Notes
|       .gitkeep
|
\---Setup
    +---Dolphin
    |       dirs-info.toml
    |
    +---Panel
    |   \---Scripts
    |           .gitkeep
    |
    +---Sh
    |   |   Envs.sh
    |   |   nk-profile.sh
    |   |   nk-profile.sh_notes
    |   |   nk-profile.sh_notes2
    |   |   nk-rcfile.sh
    |   |   zm_nk-profile.sh
    |   |
    |   \---Envs
    |           LANGsByGoogle.sh
    |           PYTHON.sh
    |
    \---Tty
        |   setup-nk_kbd.py
        |
        +---docs
        |       dumpkeys-l_notes
        |       dumpkeys-_notes
        |       dumpkeys_notes
        |       loadkeys_notes.md
        |
        \---keymaps
                nk_kbd-header.inc
                nk_kbd-shctlr.map
                nk_kbd-us-alpnum.map
                nk_kbd-us-splchr.map
                nk_kbd-us.map_notes
```

