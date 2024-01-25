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
