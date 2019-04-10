from task_1.database_handler import DatabaseHandler
from task_1.parser import Parser
from config import Config
from uuid import uuid4


class Console(object):

    def __init__(self):
        self.database_config = Config('db')
        self.host_config = Config('mk')
        self.database_handler = DatabaseHandler(self.database_config)
        self.parser = Parser(self.host_config, self.database_handler)

    def mainloop(self):

        is_running = True
        print("Welcome to the app console!")

        while is_running:
            print(">", end=" ")
            command = input().split()

            if command[0] in ('exit', 'close', 'quit'):
                is_running = False
            elif command[0] == 'create_student':
                student = (uuid4().hex, command[1], command[2], command[3])
                print('Student with id {} has been added.'.format(self.database_handler.add_student(student)))
            elif command[0] == 'download_articles':
                self.parser.download_articles()
            else:
                print("Command has not been recognized. Try again.")
        else:
            print("Thank you for using this app. Goodbye.")
