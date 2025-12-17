# Port forwarding
## Local port forwarding
```
A ==> B
B ==> C
A =x=> C
```
>I open a port on A to allow A to access a service on C through B 
```bash
ssh -fNL [A_INTERFACE_HOST:]<A_PORT>:<C_IP>:<C_PORT> <B_USER>@<B_IP> # on A
nc -nv <A_INTERFACE_HOST> <A_PORT> # To access <C_IP>:<C_PORT> from A
```

## Remote port forwarding
```
B ==> A
C ==> B
C =x=> A
```
>I open a port on B to allow C to access a service on A through B
```bash
ssh -fNR [B_INTERFACE_HOST:]<B_PORT>:<A_IP>:<A_PORT> <B_USER>@<B_IP> # on A
nc -nv <B_INTERFACE_HOST> <B_PORT> # To access <A_IP>:<A_PORT> from C
```
