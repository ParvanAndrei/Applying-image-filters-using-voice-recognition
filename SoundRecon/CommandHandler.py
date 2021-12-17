#!/usr/bin/env python3



class CommandHandler(object):
    command_dic = {}
    last_command = ''

    def __init__(self, list_of_commands):
        for command in list_of_commands:
            self.command_dic.update({command: 0})
            
    def update (self, command_string):
        for item in self.command_dic.items():
            if item[0] in command_string:
                self.command_dic.update({item[0]: 1})
            else:
                self.command_dic.update({item[0]: 0})
                
    def getLastCommand(self):
        for item in self.command_dic.items():
            if item[1] == 1:
                return item[0]
  