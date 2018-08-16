## Prerequisites
* [Juypiter Notebook]()
* [Docker]() 
* a GitHub [account]()
*  scripts requires a personal [http://data.world](https://data.world) account
* a github url to the clean-data folder (aka, GH_URL)
* a data.world user name (aka, DW_USER)
* a data.world url to dataset path (aka, DW_DB_URL)
* a data.world authorization token (aka, DW_AUTH_TOKEN)
Note: Developers setup personal accounts for development.   

## Installation
```
git clone https://github.com/citizenlabsgr/data.world
# environment variables are script specific
# create environment variable file .env
cd data.world/scripts/ source-path-goes-here
# GH_URL is the folder where clean data is stored
echo GH_URL= https:// >> .env
echo DW_USER=AAAA >> .env
echo DW_DB_URL=<> >> .env
echo DW_AUTH_TOKEN=<data-world-token> >> .env
```

At this point you should be good to start jamming on issues [here](https://github.com/citizenlabsgr/adopt-a-drain/issues).

## Docker

To setup a local development environment with
[Docker](https://docs.docker.com/engine/installation/).

```
# Override database settings as the docker host:
echo DB_HOST=db > .env
echo DB_USER=postgres >> .env

# Enable google maps with your developer google map api key 
echo GOOGLE_MAPS_JAVASCRIPT_API_KEY=<get-google-map-api-key> >> .env

# Setup your docker based postgres database:
docker-compose run --rm web bundle exec rake db:setup

# Load data:
docker-compose run --rm web bundle exec rake data:load_things
# OR: don't load all that data, and load the seed data:
# docker-compose run --rm web bundle exec rake db:seed

# Start the web server:
docker-compose up

# Visit your website http://localhost:3000 (or the IP of your docker-machine)
```

## Usage
rails server

## Seed Data
bundle exec rake data:load_drains



## Submitting a Pull Request
1. [Fork the repository.][fork]
2. [Create a topic branch.][branch]
3. Add specs for your unimplemented feature or bug fix.
4. Run `bundle exec rake test`. If your specs pass, return to step 3.
5. Implement your feature or bug fix.
6. Run `bundle exec rake test`. If your specs fail, return to step 5.
7. Run `open coverage/index.html`. If your changes are not completely covered
by your tests, return to step 3.
8. Add, commit, and push your changes.
9. [Submit a pull request.][pr]

[fork]: http://help.github.com/fork-a-repo/
[branch]: https://guides.github.com/introduction/flow/
[pr]: http://help.github.com/send-pull-requests/


