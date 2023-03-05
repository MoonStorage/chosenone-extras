import firebase_admin
import instaloader
from firebase_admin import credentials, db
from instaloader import Profile

# Initialize Admin
cred = credentials.Certificate("credential.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "[YOUR-DATABASE-URL]" #TODO: Replace with your own Database URL
})

# Collect Data
while True:
    # Default values
    username = ""
    verified_t = ""
    verified = False

    command = input("Command: ")
    command = command.strip()

    if " " in command:
        username = command.split(" ")[0]
        verified_t = command.split(" ")[1]
    else:
        username = command

    if verified_t == "yes":
        verified = True

    # Instaloader
    loader = instaloader.Instaloader()
    profile = Profile.from_username(loader.context, username)

    # Again
    followers = profile.followers
    bio = profile.biography
    picture = profile.profile_pic_url

    db.reference(f"users/{username.replace('.', ':')}").set({
        "bio": bio,
        "username": username,
        "picture": picture,
        "verified": verified,
        "followers": followers
    })

    print()

    print("\033[92m" + "\033[1m" + "Username: " + "\033[0m" + str(username))
    print("\033[92m" + "\033[1m" + "Followers: " + "\033[0m" + str(followers))
    print("\033[92m" + "\033[1m" + "Biography: " + "\033[0m" + str(bio))
    print("\033[92m" + "\033[1m" + "Picture: " + "\033[0m" + str(picture))
    print()

    if verified:
        print("\033[92m" + "\033[1m" + "VERIFIED" + "\033[0m")
    else:
        print("\033[91m" + "\033[1m" + "NOT VERIFIED" + "\033[0m")

    print()
    print()
    print()
