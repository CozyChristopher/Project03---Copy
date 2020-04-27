# CS 1XA3 Project03 - <ganc4>
## Usage
- Install Anaconda by going to https://docs.anaconda.com/anaconda/install/
- Activate djangoenv on your system with the following command
  ``` bash
  conda activate djangoenv
  ```
- Run locally with: python manage.py runserver localhost:8000
- Run on mac1xa3.ca with: python manage.py runserver localhost:10030
- In order to access the User database, one must make migrations first with authenticate
following commands
```bash
    python manage.py makemigrations

    python manage.py migrate
```
Log in with test1, password: r74qz9e8rN2VmVL
...

## Objective 01: Signup
Description:
- This feature is displayed in signup.djhtml which is rendered by signup_view
- It makes a POST Request from the UserCreationForm to /e/ganc4/signup
which is handled by signup_view
Exceptions:
- If the password does not meet the requirements it will prompt to the user to
create a different password
## Objective 02: Adding Profile and Interest
Description:
- This feature is displayed by social_base.djhtml which is rendered by
messages_view
- It shows the current users employment, location, birthday, and interests
## Objective 03: Editing Profile
Description:
- This feature is displayed by account.djhtml which is rendered by account_view
- It makes two POST Requests from the PasswordChangeForm and the UserInfoForm
to /e/ganc4/social/account/ which is handled by account_view
## Objective 04: Randoms list
Description:
- This feature is displayed by people.djhtml which is rendered by people_view
- It starts by displaying one person and proceeds to display 2 more people who
are not friends with the currently signed in user when a POST request is made
- It make a POST Request from people.js and it is handed by more_ppl_view
## Objective 05: Sending Friend requests
Description:
- This feature is displayed by people.djhtml and rendered by people_view
- It makes a POST request from people.js and it is handled by
friend_request_view
