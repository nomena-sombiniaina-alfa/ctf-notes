# History
## get history
```ps1
Get-Content (Get-PSReadLineOption).HistorySavePath # persistent
Get-History # current shell
```

## clean history
```ps1
Clear-History
Remove-Item (Get-PSReadLineOption).HistorySavePath -Force
```