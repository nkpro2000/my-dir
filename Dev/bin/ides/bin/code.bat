@echo off
echo $^> call "%UserProfile%\nk\Dev\bin\ides\code\bin\code.cmd" --user-data-dir "%UserProfile%\nk\Dev\code\ides\code\data\user" --extensions-dir "%UserProfile%\nk\Dev\code\ides\code\data\exts" %*
call "%UserProfile%\nk\Dev\bin\ides\code\bin\code.cmd" --user-data-dir "%UserProfile%\nk\Dev\code\ides\code\data\user" --extensions-dir "%UserProfile%\nk\Dev\code\ides\code\data\exts" %*
