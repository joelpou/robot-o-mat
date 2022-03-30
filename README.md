# BOT-O-MAT
You have been asked to create an application where you can create robots that can complete different tasks. Each of the available tasks has a completion time for which the robots have to wait for before completing it.

## How to run
1. Only requirement is setup of python3 interpreter
2. To run script, on terminal run:

    ``` python3 bot-o-mat.py```

## Bot-O-Mat CLI Instructions:
* There are 5 options on CLI:
1. Create Bot 
2. Create Task
3. Do Tasks
4. Bot Info
5. Exit

* To do any of the options 2 - 4 you need to create at least one Bot first.
* After you create a Bot you can create tasks which will be automatically assigned sequentially to Bots that have space.
* After at least one tasks is assigned to Bot then you can select option 3 and do tasks.
* After do tasks completes a log file called "do_tasks_log.txt" will be created that contains timestamps of Bot performing tasks and completion time.
* Note that if more than one Bot is created, tasks will only be assigned to second Bot if first Bot tasks are filled.
* Also note that do tasks will perform all tasks of all Bots concurrently.

## Requirements
1. Create an interface (CLI or GUI), where users can create new robots tasks that get assigned automatically.
2. Assign the Robot a set of five random tasks.
3. Define methods to complete each task.
4. Store completion time per robot, per task. 

## Robot
- The Robot must complete each task within the given duration (specified in milliseconds).
- When a task is completed, it should be removed from the list of asigned tasks. 

## Tasks
Tasks have a description and an estimated time to complete.
```
[
  {
    description: 'do the dishes',
    eta: 1000,
  },{
    description: 'sweep the house',
    eta: 3000,
  },{
    description: 'do the laundry',
    eta: 10000,
  },{
    description: 'take out the recycling',
    eta: 4000,
  },{
    description: 'make a sammich',
    eta: 7000,
  },{
    description: 'mow the lawn',
    eta: 20000,
  },{
    description: 'rake the leaves',
    eta: 18000,
  },{
    description: 'give the dog a bath',
    eta: 14500,
  },{
    description: 'bake some cookies',
    eta: 8000,
  },{
    description: 'wash the car',
    eta: 20000,
  },
]
```
## Robot Types
```
{ 
  UNIPEDAL: 'Unipedal',
  BIPEDAL: 'Bipedal',
  QUADRUPEDAL: 'Quadrupedal',
  ARACHNID: 'Arachnid',
  RADIAL: 'Radial',
  AERONAUTICAL: 'Aeronautical'
}
```
## Bonus Features
***note: be creative and have fun! Use this list or create your own. Do as much or as little as you want.***
- Allow users to create multiple robots at one time
- Allow users to manually asigne tasks to a robot
- Create a leaderboard for tasks completed by each Robot
- Incorporate a failure rate per robot type and come up with a retry logic for failed tasks
- Can you find clever ways to notify when a robot complete a tasks?
- Create tasks specific for each robot type, this could work in conjunction with the leaderboard. For e.g. robots that are assigned tasks that their type can't perform won't get "credit" for finishing the task.
- Add persistance for tasks, bots and leaderboard stats
