#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const completedTask = body.filter((task) => task.completed);
    const userTaskCount = {};
    completedTask.forEach(task => {
      const userId = task.userId;
      userTaskCount[userId] = (userTaskCount[userId] || 0) + 1;
    });
    console.log(userTaskCount);
  }
});
