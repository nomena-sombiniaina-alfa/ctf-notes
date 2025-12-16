# Linux CLI
## Basic CLI
* `echo`, `ls`, `ls -la`, `cat`, `cd`
* Hidden files start with `.`

## Log Analysis
* Navigate to `/var/log`
* `grep "Failed password" auth.log` to spot failed logins

## Artifact Discovery
* `find /home/socmas -name *egg*`
* File found: `eggstrike.sh`

## Script Review
* `cat | sort | uniq` for data processing
* `>`, `>>`, `|`, `&&` used for redirects and chaining
* File deletion and replacement via `rm`, `mv`

## Privilege & History
* `sudo su` to switch to root
* `history` / `.bash_history` shows attacker activity


## side quest : 
content : 
``` raw
root@tbfc-web01:/home/mcskidy/Documents$ cat read-me-please.txt 
From: mcskidy
To: whoever finds this

I had a short second when no one was watching. I used it.

I've managed to plant a few clues around the account.
If you can get into the user below and look carefully,
those three little "easter eggs" will combine into a passcode
that unlocks a further message that I encrypted in the
/home/eddi_knapp/Documents/ directory.
I didn't want the wrong eyes to see it.

Access the user account:
username: eddi_knapp
password: S0mething1Sc0ming

There are three hidden easter eggs.
They combine to form the passcode to open my encrypted vault.

Clues (one for each egg):

1)
I ride with your session, not with your chest of files.
Open the little bag your shell carries when you arrive.

2)
The tree shows today; the rings remember yesterday.
Read the ledger’s older pages.

3)
When pixels sleep, their tails sometimes whisper plain words.
Listen to the tail.

Find the fragments, join them in order, and use the resulting passcode
to decrypt the message I left. Be careful — I had to be quick,
and I left only enough to get help.

~ McSkidy

```