def ask ( *parameters ):
    '''


    :param parameters: commands in the form of strings e.g:  ask("a" "b" "z")
    :return: particular commands to be returned
    '''
    #take all ask commands like pd ,fd in form of strings or numbers if they're numbers
    l = list(*parameters)
    print l
    #predefined functions like pd, fd, etc
    dict={"a": "alphabet" , "abc": "string" , '1' : "number" , "others" : "others"}
    #functions requested
    dict_agent={}
    for x in l:
        if x in dict:
            dict_agent[x] = dict[x] #if functions predefined add it to list of functions demanded
        else:
            t = str(l)
            dict_agent[x] = t  #if not predefined functions , create a function by looking up in the program for such functions
    return dict_agent #return demanded functions to agent


#function to make agent_set and ask work together

def ask_turtles (agent_name , dct ):
    '''

    :param agent_name: list of agent id's those who will execute the commands
    :param dct: functions that are supposed to be executed
    :return: actions in the form of print statements
    '''
    for y in agent_name:
        for key,value in dct.iteritems(): #make agent do demanded work
            print (str(y)+ " is doing "+str(value)+" for "+str(key))

#function to create agents

def agent_name(number_of_agents):

    '''

    :param number_of_agents: number of agents that you want to create
    :return: list of agents
    '''

    l=list()
    for x in range(0,number_of_agents):
        l.append(x)
    return l

#to create multiple turtles
#create only one if you want to work with only one turtle i.e. input number_of_agents 1
#agent_name(5)


#commands that the turtle is supposed to execute
#ask("a" "b" "z")

#the binding function to bind turtle and ask
ask_turtles(agent_name(5), ask("a" "b" "z"))