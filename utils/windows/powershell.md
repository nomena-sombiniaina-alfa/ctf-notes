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

---

# SSH
## ssh jump
| Me :            | Machine A :             | Machine B :             | Machine C :      |
| --------------- | ------------            | ------------            | ------------     |
|                 | user : userA            | user : userB            | user : userc     |
|                 | key : ~/priv_a          | key : ~/priv_b          | key : ~/priv_c   |
| ip : 10.10.10.1 | ip : 10.10.10.10        |                         |                  |
|                 | ip : 10.10.100.10       | ip : 10.10.100.11       |                  |
|                 |                         | ip : 10.10.110.10       | ip : 10.10.110.11|
#### Flux :
`Me → Machine A → Machine B → Machine C`

###### Using config file
```ps1
@"Host A
  HostName <IP-A>
  User <USER-A>
  IdentityFile <PATH-TO-A-PRIVKEY>

Host B
  HostName <B-IP-ACCESSIBLE-FROM-A>
  User <USER-B>
  IdentityFile <PATH-TO-B-PRIVKEY>
  ProxyJump A

Host C
  HostName <C-IP-ACCESSIBLE-FROM-B>
  User <USER-C>
  IdentityFile <PATH-TO-C-PRIVKEY>
  ProxyJump B
"@ | Out-File -Encoding UTF8 C:\users\<username>\.ssh\config
ssh C
```

---
