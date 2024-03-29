const Discord = require("discord.js");
const client = new Discord.Client();
const fs = require('fs');

client.login("token");

client.setMaxListeners(2); // Change as you wish

client.on("message", msg => {
    if (!msg.content.startsWith("!")) return;

    if (msg.author.id == client.user.id) {
        return;
    }

    const args = msg.content.slice(1).split(' ');
    const command = args.shift().toLowerCase();

    switch (command) {
        case "play":
            var files = fs.readdirSync('./test-images');
            console.log(files.length);

            sendImage(0);

            function sendImage(f) {
                var file = files[f];
                var code = file.substr(0, 4);

                msg.channel.send("", {
                    files: ['C:/path/to//antiminjubot/test-images/' + file]
                }).then(function () {
                    console.log('Sent ' + file);
                }).catch(function (e) {
                    console.log(e);
                });

                client.addListener('message', function (response) {
                    if (response.author.id != client.user.id && response.content == '!claim ' + code) {
                        console.log('Correct ' + file);

                        var newRand = Math.floor(Math.random() * 132);

                        console.log(newRand);
                        return sendImage(newRand);
                    } else {
                        console.log('Wrong ' + file);
                    }
                });
            }

            break;
        case "start":
            var files = fs.readdirSync('./test-images');
            console.log(files.length);

            sendImage(0);

            function sendImage(f) {
                var file = files[f];
                var code = file.substr(0, 4);

                msg.channel.send("", {
                    files: ['C:/path/to/antiminjubot/test-images/' + file]
                }).then(function () {
                    console.log('Sent');
                }).catch(function (e) {
                    console.log(e);
                });

                client.addListener('message', function (response) {
                    if (response.author.id != client.user.id && response.content == '!claim ' + code) {
                        console.log('Correct');
                        return sendImage(f + 1);
                    } else {
                        console.log('Wrong');
                    }
                });
            }

            break;
    }
});
