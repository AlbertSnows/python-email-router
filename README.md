# Simple Email Router

This is a simple repo that adds an endpoint to route valid email requests

## FAQ

### How to install your app

There's a bunch of ways to run this app.

Most simply, `docker-compose up` will spin up a docker

 container to play with. You should be able to access

 it via localhost. You'll need to have docker stuff installed.

Or, you can also just run the Dockerfile directly

`docker build -t email_router:latest`

`docker run -p 80:8080 email_router:latest`

Orr, you can run `Waitress` directly, which is the prod server the app is hosted on via the .sh script

`./spin.sh`

Orrr, you can run the flask server

`flask --app flaskr run`

For each of thes you'll need to have the correct package

installed, such as `waitress` or `flask` on the CLI.

Those will all spin up the server. These should all be accessible by either `localhost`

or `127.0.0.1`

There are a few toy endpoints, the main one for the email stuff is at `/email`

### Which language, framework, and libraries you chose and why

Language: Python

Framework: Flask

Why: I haven't worked with Python in a while so it was a good opportunity to revist the

language. Flask seemed like a solid choice becuase we're effectively making the smallest

conceivable API and Flask is well suited for micro-frameworks.

Note, you need to have an api key with sendgrid in order for the emails to be sent.

Put your api key in the .env and then pass your json to the endpoint. You can use

either a curl or an API tool like Insomnia or Postman to run the command.

Libraries:

 pyrsistent -> because persistent data structures

 jsonschema -> for pleasant endpoint validation

 dotenv -> for easy env variable setup

 requests -> *the* choice for sending http requests as far as I can tell

 beautifulsoup -> has a robust html->plaintext parser


### Tradeoffs

No notable tradeoffs. The implementation ended up being remarkably small, which are

points in its favor.

### How much time you spent on the exercise

About two days, most of which was spent learning about Python and Flask antics.

### Anything else you wish to include

Normally I always include tests but Python has a fairly mature set of libraries

to solve problems like this. 90% of the code is just asking libraries to do things

for me which means there's not a lot of headway to get out of testing.

Also Python has a lot of cool functional libraries I didn't get to try. RIP.