@echo off
echo $^> call "%UserProfile%\nk\Dev\bin\ides\code\bin\code.cmd" --user-data-dir "%UserProfile%\nk\Dev\code\ides\code\work\user" --extensions-dir "%UserProfile%\nk\Dev\code\ides\code\work\exts" %*
call "%UserProfile%\nk\Dev\bin\ides\code\bin\code.cmd" --user-data-dir "%UserProfile%\nk\Dev\code\ides\code\work\user" --extensions-dir "%UserProfile%\nk\Dev\code\ides\code\work\exts" %*
