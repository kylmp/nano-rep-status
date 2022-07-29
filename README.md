# Nano Representative Status Page

### About
Status page for nano representatives. Shows online status, balances, voting weight and more.

Created by kylmp

![Picture](https://raw.githubusercontent.com/qcryptic/nano-rep-status/master/pic.png)

### Installation 

**Prerequisite:** Your nano node should already be running and accessible via RPC from the system this status page is running on.

**Install Dependencies (Debian/Ubuntu):**
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip install Flask
sudo pip install nano-python
```

**Clone Repo:**
```
cd ~
git clone https://github.com/qcryptic/nano-rep-status.git
```

**Run It:**

*First you should edit the config variables in nanoRepStatus.py as needed*
```
cd ~/nano-rep-status
python3 nanoRepStatus.py
```

Alternatively, run it in the background with no output (can safely close the terminal now):
```
nohup python3 nanoRepStatus.py &
```

A lot of the design is based on the design from https://github.com/dbachm123/nanoNodeMonitor
