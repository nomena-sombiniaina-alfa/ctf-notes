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
