git status
write-host "Would you like to continue the workflow?"
$Readhost = Read-Host " ( y / n ) "
Switch ($Readhost){
  Y {Write-host "Yes, continue the workflow process"; git add $args[0]; git commit -m $args[1] $args[0]; git push}
  N {Write-host "No, do not continue the workflow process"; $gitWorkflow = $false}
  Default {Write-host "Default, do not continue the workflow process"; $gitWorkflow = $false}
}
