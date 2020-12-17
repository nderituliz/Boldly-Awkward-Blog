# Boldly-Awkward-Blog
An app that displays our quotes
## By [Elizabeth Nderitu](https://github.com/nderituliz)


## User Stories
Users can do the following with the app:
* View the different blogs.
* See the blogs other people have posted.
* Comment on the different blogs and leave feedback.
* Submit a blog in any category.
* Vote on the blog they liked and give it a delete or close.

## BDD
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Various Blogs  | N/A | Various blogs  |
|Display Blogs | **Click** on a Category| A page with a list of blogs |
|Add new blog | **Click** New post | User Should register/sign in to add new blog |
|View Blogs | **Click** on a post | View a blog and comments |
|Comment on a blog | **Click** Comment | Registered User displays a form where a user can comment on a certain blog |


## Technologies used
* Python3.8
* Flask framework
* HTML & CSS
* postgresql

## Setup/Installation Requirements
* internet access
* $ git clone 
* $ cd boldly-awkward (project-name)
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt ( to install all the dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh
* The app runs and you can make changes.


# Support and Contacts

In case You have any query, kindly reach out via [nderituliz@gmail.com]


## Known Bugs
User image avartar does not function properly.


### License


## LICENSE
* Copyright (c) || 2020 [Elizabeth Nderitu](https://github.com/nderituliz)
* MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
