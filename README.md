# PMKID Hashcat Environment

A container environment holding the dependencies for a pmkid wpa2 password cracking attack.

The attack planned to be implemented will more or less follow [this tutorial](https://null-byte.wonderhowto.com/how-to/hack-wi-fi-cracking-wpa2-passwords-using-new-pmkid-hashcat-attack-0189379/).

## Dependencies

- It is necessary to have `docker` and `docker-compose` installed.
- You are supposed to have GPUs.

## Setup & Run

```
git clone git@github.com:busykoala/pmkid_hashcat_env.git
cd pmkid_hashcat_env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ./runme.py
```

## Test

Because there is no real production mode planned in the near future the test
dependencies are also in `requirements.txt` and therefore installed when setup.

```
source venv/bin/activate
pytest
```

## Future Plans

Since the python script `runme.py` is not yet doing anything there is still work to do.

It is planned to crack wlan passwords with these user interaction steps:
- choose a wlan interface to be used
- choose a wlan access point to crack
- choose a password list to use
