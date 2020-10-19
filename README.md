# Sonne - Dein Familienlotse <img src="https://github.com/tech4germany/rasa_familienlotse/blob/master/Sonne2.png" width="50" height="50">
Prototyp eines Chatbots, der zu Familienleistungen auf dem [Familienportal](https://familienportal.de/familienportal) des [Bundesfamilienministeriums für Familie, Senioren, Frauen und Jugend (BMFSFJ)](https://www.bmfsfj.de/) informiert und berät. 

Der Familienlotse Sonne soll als erste Ausbaustufe der Vision des BMFSFJ für einen Familienassistenten angesehen werden. Hierfür wurde Sonne mit einer Lotsenfunktionalität ausgestattet, die die Navigation auf der Seite unterstützen und erste Fragen beantworten kann.

Entstanden ist Sonne im Rahmen des [Tech4Germany Fellowships 2020](https://tech.4germany.org/fellowship-2020/) vom Team Chatbot ([Miriam Metz](https://www.linkedin.com/in/miriammetz/), [Benedikt Liebig](https://www.linkedin.com/in/beliebig/), [Johannes Heck](https://www.linkedin.com/in/johannescheck/) und [Anna Steinberg](https://www.linkedin.com/in/anna-steinberg-855329172/)) in Kooperation mit dem [Informationstechnikzentrum Bund(ITZBund)](https://www.itzbund.de/DE/Home/home_node.html) und dem [Bundesministerium des Inneren, für Bau und Heimat (BMI)](https://www.bmi.bund.de/DE/startseite/startseite-node.html).

Der Familienlotse basiert auf [Rasa Open Source](https://rasa.com/).
Dieses Repo umfasst Informationen zu
- [Installation und Starten von Rasa Open Source](#rasa-open-source)
- [Installation von Rasa X](#rasa-x)
    - [Set-Up eines Custom Action Servers für Rasa X](#custom-action-server)
    - [Nutzung von Rasa X](#manual-data-upload-to-rasa-x)
    - [Debugging Tipps](#debugging)
    - [Generelle Tipps](#tricks-for-using-rasa-x-container-installation-not-kubernetes)
- [Set-Up des Sonne Prototypen](#sonne---setup-prototyp)
    - [Anschluss an Telegram API](#rasa-telegram-api)
    - [Einbindung in ChatWidget](#rasa-webchat-ui)
- [Best Practices für NLU data](#11-best-practices-for-designing-nlu-training-data)

# Rasa Open Source

## Installation
Please check the [requirements](https://rasa.com/docs/rasa-x/installation-and-setup/install/docker-compose/#docker-compose-install-script) before installing rasa open source
```
pip3 install rasa --use-feature=2020-resolver
```

## cli commands
| command | meaning |
| ------ | ------ |
| rasa init | all necessary files are created in dir, basic bot is installed, be fastly test-ready |
| rasa interactive | load system in interactive learning session → interactive training with Y/N; possibility to export & quit to export new training data |
| rasa shell |load NLU model; ready to start a conversation|
|rasa shell nlu|load NLU model, then show NLU classification results on CLI|
|rasa visualize|visualize story-path in training data (graph.html)|
|rasa x|rasa x UI start up|

### start rasa server
```
rasa run -m models --enable-api --cors "*" debug
```

### start rasa action server
```
rasa run actions
```


# Rasa X
👉 Rasa X **can** and **should** be used to gather **_REAL_** training data<br>
👉 also use the in-built version control connecting rasa X to your rasa-repo of choice (preferably on github for full compatibility)

## Installation
```
1. Download
curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/0.32.2/install.sh
2. Install
sudo bash ./install.sh
3. Start
cd /etc/rasa
sudo docker-compose up -d
4. set your admin pw
cd /etc/rasa
sudo python3 rasa_x_commands.py create --update admin me <PASSWORD>
```
👉 now you should be able to reach `Rasa X` under hostname or IP. Login using newly created pw.

## Custom Action Server
To be able to use **rasa Custom Actions**, you'll need to specify a custom image for the rasa action server (docker image reference is "app", i.e. find app under `docker ps` overview). This workflow works with `GitHub` and `Docker Hub`!

### Register @ Docker-Hub for container registry
In order to be able to store an image in a container registry (so that other servers are able to pull this image from somewhere in the internet), you'll need to push the image using a GitHub-Action (see more in the next section) into a container registry. This is part of your CI/CD Pipeline.

### use github-actions for pipeline
Add .github/workflows to your rasa-repo (not rasa-x!) and add action_server.yml into this dir. This GitHub-action watches the `master`-branch on changes in the `actions/`-dir. If a push to master is executed and there have been changes in the `actions/`-dir, a GitHub Action gets triggered and stores the new custom action server-image in the docker hub.
Screenshot of `action_server.yml` file:
```
name: Continuous Integration for action server
on:
  push:
    branches:
    - master
    paths:
    - 'actions/**'

jobs:
  action_server_job:
    runs-on: ubuntu-latest
    name: Build Rasa Action Server image and upgrade Rasa X deployment
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
    - name: Set Build ID from run ID and number
      run: echo "BUILD_NUMBER=$GITHUB_RUN_NUMBER-$GITHUB_RUN_ID" >> $GITHUB_ENV
    - name: My action server image
      uses: RasaHQ/action-server-gha@master
      with: 
        rasa_sdk_version: 1.10.0
        docker_image_name: 't4grasafamilienlotse1/rasa_familienlotse_action_server'
        actions_directory: 'actions'
        docker_registry_login: ${{ secrets.DOCKER_HUB_LOGIN }}
        docker_registry_password: ${{ secrets.DOCKER_HUB_PASSWORD }}
        docker_image_tag: latest
        # docker_image_tag: ${{ env.BUILD_NUMBER }}
```
👉 Step 1 refers to a GitHub repository where GitHub Action logic is stored.<br>
👉 Step 2 adds an ID to the new image.<br>
👉 Step 3 builds the image as specified in current `actions.py` file located within `actions` directory.<br><br>

It's important to specify the right `rasa_sdk_version`. Setting `docker_image_tag` to `latest` spares the need to specify the exact hash of the image.

### adding github secrets
In your GitHub-repo: add secrets (only admins/maintainer) in settings
Under https://github.com/tech4germany/rasa_familienlotse/settings/secrets
you'll need to specify secrets for `DOCKER_HUB_LOGIN` (your Docker Hub Login/Username) and `DOCKER_HUB_PASSWORD` (your corresponding password)

### github action on github
Github-Actions tab in your repo: this is where the magic happens

### container registry
Check container registry in `Docker Hub` for successful image-built

### override docker-compose
Override your docker-compose.yml in order to pull the new action server image: 
👉 Create new file `docker-compose.override.yml` in the rasa installation folder (e.g. /etc/rasa/).<br>
Please reference the docker hub w/ corresponding repo and latest / image-hash
```
version: '3.4'
services:
  app: 
    image: "t4grasafamilienlotse1/rasa_familienlotse_action_server:latest"
```

### Restart the Rasa X docker container, pull the new image
```
docker-compose down && docker-compose pull && docker-compose up -d
```

## Manual data upload to Rasa X
👉 if git connection on Rasa X fails, you can manually upload all the necessary data

### step 1 - upload nlu data
👉 in the side menu under **Training **go to **NLU data** and upload the `nlu.md` from a local repo on your computer via the upload-box<br>

### step 2 - upload stories
👉 in the side menu under **Training **go to **Stories** and upload the `stories.md` from a local repo on your computer via the upload-box (if you have multiple stories spread across different files, **you need to paste them together into one file**)<br>

### step 3 - upload domain
👉 in the side menu under **Training **go to **domain** and upload the `domain.md` from a local repo on your computer via the upload-box (**along with domain come the responses, so no need to upload them specifically**)<br>

## Debugging

### access logs
```
cd /etc/rasa # go to rasa x container installation
docker ps # get all names of running containers
docker-compose logs -f rasa-x # get latest logs, -f for following
docker-compose logs -f rasa-worker # latest logs of worker
docker-compose logs -f app
docker-compose logs -f rasa-production
```

### check git connection
```
sudo docker exec -it rasa_rasa-x_1 bash

cd /app/git/1 ➡ make an ls -a in /git/ in order to determine current git-number
git remote -v
git status
git fetch -a
```
👉 enter container, enter app/git/ and check current-git connection

### check rasa x-endpoint
should return response as non-empty array
```
curl --request POST \
  --url http://<ipaddress>/webhooks/rest/webhook \
  --header 'content-type: application/json' \
  --data '{
  "sender": "Rasa",
  "message": "hi"
}'  
```
👉 should return response as non-empty array

### extract current model in use of Rasa X
```
curl --request GET \
  --url 'http://<ipaddress>/api/projects/default/models/tags/production?api_token=<token>' --output "model.tar.gz"
```
👉 `model.tar.gz` should show in your current dir
```
tar -C <some_local_dir/> -xvzf model.tar.gz 
```
👉 extract model, you should find `core` and `nlu`-model
```
{
  "config": "99914b932bd37a50b983c5e7c90ae93b",
  "core-config": "193ffaa6c10ee957125b907c64ff4545",
  "nlu-config": "dc1fe89d3d49bff74ec895f38d09b5a4",
  "domain": 484025307505654372,
  "nlg": "dd7cb5d72f2108f22da85c8ed5d9e34f",
  "messages": 405877826118901762,
  "stories": 419979385476559439,
  "trained_at": 1601476569.4479902,
  "version": "1.10.12"
}
```
👉 check fingerprint (above) for possible clash of versions<br>
👉 out of compatibility rasa open source must have the same version as is used by rasa x in the container (`1.10.12` in the example above


### check rasa open source version
```
rasa --version
```
### check Rasa X version
```
http://<your_ip>/api/version
```
### install the right rasa open source version
```
pip3 install rasa==<version_you_need> --use-feature=2020-resolver
```


## Tricks for using Rasa X container installation (not kubernetes!)

### do not use gitlab
🚨 full compatibility is only granted by using github.com 🚨

# Sonne - Setup Prototyp

## Rasa Telegram API
👉 _to demonstrate **rasa**'s messenger compatibility, we plugged rasa in the telegram API (WhatsApp's API makes having a business profile mandatory and thus is not that easy to play)_

### Fast-Track / Start telegram service if service is already setup
```
ngrok http 5005
rasa run -m models --enable-api --cors "*" debug
rasa run actions
```

### Telegram
for general installation advice, look at the [official rasa documentation](https://rasa.com/docs/rasa/connectors/telegram)

### register bot on telegram
How to get the Telegram credentials: You need to set up a Telegram bot.

To create the bot, go to [Bot Father](https://web.telegram.org/#/im?p=@BotFather), enter `/newbot` and follow the instructions. The URL that Telegram should send messages to will look like `http://<host>:<port>/webhooks/telegram/webhook`, replacing the `host` and `port` with the appropriate values from your running **Rasa X** or **Rasa Open Source server**.

At the end you should get your `access_token` and the `username` you set will be your verify.

If you want to use your bot in a group setting, it's advisable to turn on group privacy mode by entering /setprivacy. Then the bot will only listen when a user's message starts with /bot.

### start ngrok
```
ngrok http 5005
```
expose 5005 port
extract ngrok's **current https**-URL (lowest line in ngrok-output) and plug it into `credentials.yml`
Do not quit the ngrok window as with every restart a new URL is generated!

### enter credentials
in `credentials.yml`
```
telegram:
  access_token: <access_token_from_bot_father_in_telegramm"
  verify: "familienlotse_bot"
  webhook_url: "https://d3c9074d7745.ngrok.io/webhooks/telegram/webhook"
```

### start rasa server
```
rasa run -m models --enable-api --cors "*" debug
```

### start rasa action server
```
rasa run actions
```

## Rasa Webchat UI
👉 to simulate usage of rasa on a website, we need a [chat widget](https://github.com/botfront/rasa-webchat) which needs to be embedded in the `index.html` file, ports need to be set open and the website needs to be reachable. 

Important: This works only with **Rasa Open Source**.

### specify credentials
Specify credentials in `credentials.yml`
```
socketio:
  user_message_evt: user_uttered
  bot_message_evt: bot_uttered
  session_persistence: false
```

### start rasa with API enabled
```
rasa run -m models --enable-api --cors "*" --debug
```
`--cors` stands for [Cross-Origin Resource Sharing](https://developer.mozilla.org/de/docs/Web/HTTP/CORS)

### start rasa action server
```
rasa run actions
```

### add webchat script to index.html
add the following snippet to `<body/>` of `index.html`

```
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titel der Seite | Name der Website</title>
  </head>
  <body>
    <div id="webchat"></div>
    <script src="https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.min.js"></script>
    <script>
      WebChat.default.init({
        selector: "#webchat",
        initPayload: "/get_started",
        customData: {"language": "de"}, // arbitrary custom data. Stay minimal as this will be added to the socket
        socketUrl: "http://3.122.100.29:5005",
        socketPath: "/socket.io/",
        title: "Sonne - Dein Familienlotse",
        subtitle: "Subtitle",
        params: {"storage": "session"} // can be set to "local"  or "session". details in storage section.
      })
    </script>
  </body>
</html>
```

### start webserver
Webserver starts at `http://3.122.100.29:8000/`
```
start-html -> startet den server
stop-html -> stopt den server
restart-html -> restartet den server, nur wichtig wenn du was am server code änderts
```
The `html`-file is located in `~/html-server/index.html`
Do not `start-html` before having done `stop-html` since this `alias command` does not load the right ID.

### setting up webserver
👉 e.g. set up a nodejs webserver, here is an extract of the the commands (not an instruction!)
```
  962  sudo apt update
  963  sudo apt install nodejs
  964  node -v
  965  mkdir html-server
  966  cd html-server/
  967  npm init
  968  ll
  969  npm install express
  970  ll
  971  nano index.js
  972  nano index.html
  973  npm start
  974  nano package.json
  975  npm start
  976  nano package.json
  977  npm start
  978  nano index.js
  979  npm start
  980  nano index.html
  981  npm install -g forever
  982  sudo npm install -g forever
  983  ll
  984  forever index.js
  985  forever start index.js
  986  forever stop 0
  987  forever start ~/html-server/index.js
  988  forever status
  989  forever list
  990  forever start /home/ubuntu/html-server/index.js
  991  forever list
  992  forever stop 0
  993  forever stop 1
  994  cat /home/ubuntu/.forever/lbz4.log
  995  nano index.js
  996  forever start /home/ubuntu/html-server/index.js
  997  forever list
  998  nano index.html
  999  up
 1000  ll
 1001  cd ..//
 1002  forever list
 1003  forever stop 0
 1004  forever list
 1005  ll
 1006  nano .bashrc
 1007  source ~/.bashrc
 1008  stop-html
 1009  start-html
 1010  forever list
 1011  stop-html
 1012  forever list
 1013  start-html
 1014  restart-html
 1015  forever list
```
# 11 Best practices for Designing NLU Training Data

1. **autogenerated training data tends to overfitting**
→ build data set over time using examples from real conversations
→ things real users have said is the best predictor of what future users will say
2. **keep training examples distinct across intents**
→ provide_address, provide_email, provide_name are very similar in sorounding words (just other entities)
→ better: single inform intent and group all information
3. **Merge on intents, split on entities**
→ new and returning customer are similar (2.), so it's better to group them under a single intent; but how to continue from there?
→ save the extracted entity to a categorical slot, story depends on slot value ⇒ entity called `status`, 2 possible values `new` and `returning` → save info to slot `status`

```
## returning user
* greet
    - utter_ask_if_new
* inform
    - slot{"status": "returning"}
    - utter_welcome_back
```

and add to the training data: I'm `[new](status)` and `[Returning](status)`

4. **use synonyms wisely**
→ more entity mapping then entity extraction; 
→ hospital is mapped to `rbry-mqwu` 
→ map `truck`, `automobile`, `sedan` to `auto`
⇒ use synonyms when one consistent key is needed for the backend

5. **understand lookup tables and regexes**

→ methods for improving entity extraction
→ but work different from what you would think: lookup tables/regexes get featurized, are used to train NLU model
→ include a few values from lookup tables/regexes in training data

**6. leverage pre-trained entity extractors**

→ names, dates, places, email addresses (`SpaceEntityExtractor`)
→ amount of money, dates, email addresses, times, distances (`DucklingEntityExtractor`)
→ for spaCy or Duckling still add a few examples of sentences in training data, but no need to anotate them

**7. always include an out-of-scope intent**

→ catch-all for anything the user might say that is outside of the assistant's domain
→ "That sounds interesting, but that's not a skill I've learned yet. Here's what you can ask me..."
→ takes the pressure of the fallback policy to decide which user messages are in the scope (as addition; an out-of-scope intent allows you to better recover the conversation)

**8. handle misspelled words**

→ first line of defense against spelling erros should be your training data
→ don't just misspell any word, look into your training data
→ custom spell checker is also an option 

```
language: "en"

pipeline:
  - name: ConveRTTokenizer
  - name: ConveRTFeaturizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: "char_wb"
    min_ngram: 1
    max_ngram: 4
  - name: DIETClassifier
    epochs: 100
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100
```

**9. treat your data like code**

→ version control system and include data!

**10. Test your updates
→** Automated testing: ****[https://blog.rasa.com/rasa-automated-tests/](https://blog.rasa.com/rasa-automated-tests/)

[https://blog.rasa.com/10-best-practices-for-designing-nlu-training-data/](https://blog.rasa.com/10-best-practices-for-designing-nlu-training-data/)

**11. Class imbalance**
→ try to keep your intents balanced in your training data
→ `supervised_embeddings` pipeline uses balanced batching strategy
