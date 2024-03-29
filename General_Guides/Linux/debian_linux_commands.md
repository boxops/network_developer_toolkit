# Configure permanent IP on Ubuntu

### Reference: https://netplan.io/examples

## Add the following to the file (modify to needs)
```
sudo nano /etc/netplan/01-network-manager-all.yaml
```
```
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enp3s0:
      addresses:
        - 192.168.1.1
      nameservers:
        search: [mydomain, otherdomain]
        addresses: [8.8.8.8, 1.1.1.1]
      routes:
        - to: default # or 0.0.0.0/0
          via: 192.168.1.254
        - to: 192.168.1.99
          via: 192.168.1.254
```

## Press Ctrl+S and Ctrl+X to save and exit

## Test and validate the config
```
sudo netplan try
```
## Apply the config
```
sudo netplan apply
```

## Look up the changes
```
ip a
```
```
ip r
```
