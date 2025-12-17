# Local port forwarding
```
A ==> B
B ==> C
A =x=> C
```
>I open a port on A to allow A to access a service on C through B 
```cmd
netsh interface portproxy add v4tov4 listenport=<B_PORT> listenaddress=<B_IP> connectport=<C_PORT> connectaddress=<C_IP> # on B
nc -nv <B_INTERFACE_HOST> <B_PORT> # To access <C_IP>:<C_PORT> from A
```


# SSH jump

| Me :            | Machine A :             | Machine B :             | Machine C :      |
| --------------- | ------------            | ------------            | ------------     |
|                 | user : userA            | user : userB            | user : userc     |
|                 | key : ~/priv_a          | key : ~/priv_b          | key : ~/priv_c   |
| ip : 10.10.10.1 | ip : 10.10.10.10        |                         |                  |
|                 | ip : 10.10.100.10       | ip : 10.10.100.11       |                  |
|                 |                         | ip : 10.10.110.10       | ip : 10.10.110.11|

Flux :
Me → Machine A → Machine B → Machine C

## Using config file
```cmd
(echo "Host A"
echo "  HostName <IP-A>"
echo "  User <USER-A>"
echo "  IdentityFile <PATH-TO-A-PRIVKEY>"
echo ""
echo "Host B"
echo "  HostName <B-IP-ACCESSIBLE-FROM-A>"
echo "  User <USER-B>"
echo "  IdentityFile <PATH-TO-B-PRIVKEY>"
echo "  ProxyJump A"
echo ""
echo "Host C"
echo "  HostName <C-IP-ACCESSIBLE-FROM-B>"
echo "  User <USER-C>"
echo "  IdentityFile <PATH-TO-C-PRIVKEY>"
echo "  ProxyJump B"
) > C:\users\<username>\.ssh\config
ssh C
```