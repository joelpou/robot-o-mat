import time
import json
import threading

bots = []
exitFlag = 0  # internal threading variable
cli_opts = ("Create Bot", "Create Task", "Do Tasks", "Bot Info", "Exit")

class Bot(threading.Thread):
    max_tasks = 5
    types = ("Unipedal", "Bipedal", "Quadrupedal", "Arachnid", "Radial", "Aeronautical")
    statuses = ("Free", "Ready", "Busy")

    def __init__(self, name, type, tasks):
        threading.Thread.__init__(self)
        self.name = name
        self.type = type
        self.tasks = tasks
        if len(tasks) > 0:
            self.status = Bot.statuses[1]
        else:
            self.status = Bot.statuses[0]

    def run(self):
        start = time.time()
        self.status = Bot.statuses[2]
        do_tasks(self)
        self.tasks.clear()
        self.status = Bot.statuses[0]
        end = time.time()
        completion_time = end - start

        log = "{} completed tasks in {:.2f} seconds and is {} to do tasks.".format(
            self.name, completion_time, self.status.lower()
        )
        log_tasks(log)
        print(log)

    def __str__(self) -> str:
        bot = {
            "name": self.name,
            "type": self.type,
            "tasks": self.tasks,
            "status": self.status,
        }
        return json.dumps(bot, sort_keys=True, indent=4)


def do_tasks(bot):
    for task in bot.tasks:
        time.sleep(task["eta"] / 1000)
        log = "{} is {} working on {} | {}".format(
            bot.name,
            bot.status.lower(),
            task["description"],
            time.ctime(time.time()),
        )
        log_tasks(log)
        print(log)
        task.clear()
    if exitFlag:
        bot.name.exit()


def create_bot(name, type, tasks):
    if not name:
        print("Please provide bot name...")
        return
    if type not in Bot.types:
        print("Please provide valid bot type: {}".format(Bot.types))
        return
    # TODO validate tasks structure
    bot = Bot(name=name, type=type, tasks=tasks)
    return bot


def create_task(ntask, duration):
    if not ntask or not duration:
        print("Error! Please provide a new task and task duration...")
        return
    new_task = ""
    for bot in bots:
        if len(bot.tasks) == 0:
            new_task = {"description": ntask, "eta": duration}
            bot.tasks.append(new_task)
            bot.status = Bot.statuses[1]
            print("\nSuccess! New task {} created for {}.".format(new_task, bot.name))
            return
        else:
            # Check if task already exists (must be unique in list of bots)
            for task in bot.tasks:
                if task["description"] == ntask:
                    print("\nError! Task {} already assigned.".format(ntask))
                    return  # task already assigned to this bot
                elif len(bot.tasks) == Bot.max_tasks:
                    break  # bot has max number of tasks assigned
                else:
                    new_task = {"description": ntask, "eta": duration}
                    bot.tasks.append(new_task)
                    print("\nSuccess! New task {} created for {}.".format(new_task, bot.name))
                    return
    if not new_task:
        print(
            "\nError! Could not add {}, you may need to create new bot first...\n.".format(
                ntask
            )
        )
    
def log_tasks(log):   
    log_tasks = open("do_tasks_log.txt", "a")
    log_tasks.write(log + '\n')
    log_tasks.close()

def handle_options(opt):
    if opt == cli_opts.index(cli_opts[0]):
        name = input("\nPlease provide your Bot's name: ")
        while True:
            print(
                "\nPlease provide {}'s type by choosing one from the following options: ".format(
                    name
                )
            )
            for i, type in enumerate(Bot.types):
                print("{}. {}".format(i + 1, type))
            try:
                type_num = int(input("Selected number option: "))
            except:
                print("\nError! Invalid Bot type chosen, please try again...\n")
            else:
                if 0 < type_num < len(Bot.types) + 1:
                    break
                else:
                    print(
                        "\nError! Please select valid number in range 1 to {}...\n".format(
                            len(Bot.types)
                        )
                    )

        type = Bot.types[type_num - 1]
        new_bot = create_bot(name, type, [])
        bots.append(new_bot)
        print("\nBot named {} successfully created!".format(name))
        print(str(new_bot) + "\n\n")

    elif opt == cli_opts.index(cli_opts[1]):
        if len(bots) == 0:
            print("\nError! Please create new Bot before creating new task...\n")
            return
        task = input("\nPlease provide a new task: ")
        while True:
            try:
                duration = int(
                    input(
                        "\nPlease provide an estimated duration in milliseconds for {}: ".format(
                            task
                        )
                    )
                )
                break
            except:
                print("\nError! Please provide a number in milliseconds...")
        create_task(task, duration)

    elif opt == cli_opts.index(cli_opts[2]):
        if len(bots) == 0:
            print("\nError! Please add new Bots to do tasks...")
            return
        temp = []
        for bot in bots:
            if bot.tasks > 0:
                bot.start()
            # recreate Bot to recreate new instance of Thread TODO improve this logic
            # threads can't be reused
            bot = create_bot(bot.name, bot.type, [])
            temp.append(bot)
        
        for bot in bots:
            if bot.tasks > 0:
                bot.join()
            
        bots.clear()
        for bot in temp:
            bots.append(bot)            

    elif opt == cli_opts.index(cli_opts[3]):
        if len(bots) == 0:
            print("\nError! Please add new Bots to see info...")
            return
        for bot in bots:
            print(str(bot))


def main():
    while True:
        print("\n///Bot-O-Mat CLI///")
        print("\nPlease select one of the following options: ")
        for i, opt in enumerate(cli_opts):
            print("{}. {}".format(i + 1, opt))
        try:
            cli_opt = int(input("Selected option number: "))
        except:
            print("\nError! Invalid option chosen, please try again...\n")
        else:
            if cli_opt == cli_opts.index(cli_opts[4]) + 1:
                break
            elif 0 < cli_opt < len(cli_opts):
                handle_options(cli_opt - 1)
            else:
                print(
                    "\nPlease select valid number in range 1 to {}...\n".format(
                        len(cli_opts)
                    )
                )

    print("\nHasta la vista baby!")


if __name__ == "__main__":
    main()
