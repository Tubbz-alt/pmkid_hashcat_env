# PMKID Hashcat Environment

A container environment holding the dependencies for a pmkid wpa2 password cracking attack.

## Dependencies

- It is necessary to have `docker` and `docker-compose` installed.
- You are supposed to have GPUs.

## Setup & Run

```
git clone git@github.com:busykoala/pmkid_hashcat_env.git
cd pmkid_hashcat_env
docker-compose up
```

## Usage

An application is planned to be shipped with this repo to have a straightforward
way to do a pmkid hashcat attack for wpa2 password cracking.

The attack planned to be implemented will more or less follow [this tutorial](https://null-byte.wonderhowto.com/how-to/hack-wi-fi-cracking-wpa2-passwords-using-new-pmkid-hashcat-attack-0189379/).

There will be the steps:
- choose a wlan interface to be used
- choose a wlan access point to crack

With the info above it should then be possible to run the attack and print the
matching password in the end (if found in a given password list).
