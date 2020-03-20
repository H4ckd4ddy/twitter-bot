# Twitter bot

Generic docker image for twitter bots

##### With docker :
```
docker run \
--env CONSUMER_API=my_consumer \
--env CONSUMER_API_SECRET=my_consumer_secret \
--env ACCES_TOKEN=my_token \
--env ACCES_TOKEN_SECRET=my_token_secret \
--env TRIGGERS="keywords;to;detect;seperated;by;semicolons"
--env BLACKLIST="tweets;containing;any;of;these;words;are;ignored"
--env RESPONSES="random;responses"

-d hackdaddy/twitter-bot
```

##### With docker-compose :
```
version: '3.7'
services:
  bot:
    image: hackdaddy/twitter-bot
    container_name: Bot
    environment:
      CONSUMER_API:
      CONSUMER_API_SECRET:
      ACCES_TOKEN:
      ACCES_TOKEN_SECRET:
      TRIGGERS: "keywords;to;detect;seperated;by;semicolons"
      BLACKLIST: "tweets;containing;any;of;these;words;are;ignored"
      RESPONSES: "random;responses"
```
