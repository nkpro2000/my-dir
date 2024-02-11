# pwsh.exe (in WindowsOS)
# This script link files/dirs (mostly config) of apps to here.
# This script only make files/dirs if neccessary, for trees in Paths(param).
# Then links them with targets in tree, so persist even after rm s on default location.
# Will be run by user like `pwsh -NoLogo -NoProfile .\do_links.ps1` from shell.

#Requires -PSEdition Core

Param (
    [Parameter(
        Position = 0, ValueFromRemainingArguments = $true, Mandatory=$false,
        HelpMessage = "do on subset of home-dir. (Default:'.')" )]
    [String[]]$Paths = ".",

    [Parameter(Mandatory=$false, HelpMessage = "do Hard Links (Default:`$true)")]
    [Switch]$Hl = $true,
    [Parameter(Mandatory=$false, HelpMessage = "do Junctions")]
    [Switch]$Jn = $false,
    [Parameter(Mandatory=$false, HelpMessage = "do Symbolic Links")]
    [Switch]$Sl = $false,

    [Parameter(Mandatory=$false, HelpMessage = "Verbose")]
    [Switch]$v = $false
)
Set-Location "${Env:UserProfile}\nk\Dev\bin\scoop\persist-in-windows\home-dir\"
If($v){ Write-Host "|> Current Working Dir : $(Get-Location)" }


Function do_on ($p) {
If($v){ Write-Host "|> doing links on $p (Rel.toCWD)" }
foreach($i in (Get-ChildItem -Path "$p"|%{$_.Name})) { Try{
# Core-Logic{

If (Test-Path -Path "$p\$i" -PathType 'Leaf') {
If ($Hl -And -Not (Get-Item -Path "$p\$i").LinkType) {
## File !Link {

echo "Yet2Do F!L $p\$i"

}ElseIf ($Hl -And (Get-Item -Path "$p\$i").LinkType -eq "HardLink") {
## HardLink File {

Write-Host "I> Already HardLinked $p\$i" -NoNewline
If($v){ Write-Host "`n|> ``-> $(fsutil hardlink list "$p\$i")" }
Else{ Write-Host " ($((fsutil hardlink list "$p\$i").Count))"}

}ElseIf ($Sl -And (Get-Item -Path "$p\$i").LinkType -eq "SymbolicLink") {
## SymLink File {

Write-Host "I> Just SymLk $p\$i"

}}

ElseIf (Test-Path -Path "$p\$i" -PathType 'Container') {
If (-Not (Get-Item -Path "$p\$i").LinkType) {
If("$i" -notmatch "\.nkJn$"){ do_on("$p\$i") }ElseIf($Jn){
## Folder !Link {

echo "Yet2Do D!L $p\$i"

}}ElseIf ($Jn -And (Get-Item -Path "$p\$i").LinkType -eq "Junction") {
## Junction

Write-Host "I> IDKwhat2do $p\$i"

}ElseIf ($Sl -And (Get-Item -Path "$p\$i").LinkType -eq "SymbolicLink") {
## SymLinkD

Write-Host "I> Just SymLD $p\$i"

}}

# Core-Logic}
}Catch{
    Write-Host "?> Errored at $p\$i"
    If($v){
        Write-Host "|> ``-> $_"
        Write-Host "|> ``-> $($_.CategoryInfo)"
        Write-Host "|> ``-> $($_.ScriptStackTrace|ForEach{$_.Replace("`n","`n|> ``-> ")})"
}}}}


ForEach($p in $Paths) {
    #If($v){ Write-Host "|> doing links on $p (Rel.toCWD)" }
    do_on($p)
}
