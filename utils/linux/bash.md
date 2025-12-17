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

## method 1 - SSH using ssh-agent (recommended)
> Add every key to ssh-agent and it will automatically assign to the right server
```bash
eval "$(ssh-agent -s)"
ssh-add ~/priv_a
ssh-add ~/priv_b
ssh-add ~/priv_c
ssh -J userA@10.10.10.10,userB@10.10.100.11 userc@10.10.110.11
```

## method 2 - using config file
```bash
cat << 'ENDL' > ~/.ssh/config
Host A
  HostName 10.10.10.10
  User userA
  IdentityFile ~/priv_a

Host B
  HostName 10.10.100.11
  User userB
  IdentityFile ~/priv_b
  ProxyJump A

Host C
  HostName 10.10.110.11
  User userc
  IdentityFile ~/priv_c
  ProxyJump B
ENDL
ssh C
```