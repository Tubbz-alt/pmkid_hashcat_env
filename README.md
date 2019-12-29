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
