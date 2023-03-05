# ChosenOne Extras
Scripts for the project [ChosenOne](https://github.com/moonstorage/ChosenOne).

## Setup
1. Run the commands below to install the libraries:
   > `pip install firebase_admin`
   > `pip install instaloader`
2. Replace `credential.json` with your own Firebase Admin Service Account Secret.
3. Go inside `register.py` and replace `databaseURL` with your own Firebase Admin Database URL.

## Instructions
### register.py
> Pass user's instagram username as the first argument and optionally pass "yes" as the second argument if you want the user to be displayed as **verified**.

**Example:**
> `py register.py someone` (Unverified user)
> `py register.py someone yes` (Verified user)