
def control():
    while True:
        command = input()
        if command == "exit()":
            #interrupt code here


List1 = ['a', 'b' , 'c', 'd', 'e', 'f']

List2 = ['1', '2', '3', '4', '5', '6']

List3 = []

List3.append("99999AAAABBBBCCCC111")
List3.append("99999AAAABBBBCCCC222")
List3.append("99999AAAABBBBCCCC333")
List3.append("99999AAAABBBBCCCC444")
List3.append("99999AAAABBBBCCCC555")
List3.append("99999AAAABBBBCCCC666")
#List3.append("99999AAAABBBBCCCC777")

#minimum 1
a = 1
res = locals()['List3']

switch = True
while True:
    try:
        while switch == True:
            for i in List1:
                #print(i)
                switch = False
                break
    
        for k in range(len(res)):
            print('Element found', locals()['List3'][k])

        while switch == False:
            for i in List2:
                #print(i)
                switch = True
                break
    except KeyboardInterrupt:
        program = 'for k in range(len(res)):\n\tprint("Element found", locals()["List3"][k],".", end="", flush=True)'
        exec(program, globals(), locals())


#DISCONNECT_MESSAGE = "!DISCONNECT" from helper.py
#while True:
#    con,ip = Server.accept()
#    _thread.start_new_thread(control,(con,))
#    print(str(ip) + " Connected")
#
#    try:
#        cmd = str(con.recv(1024).decode())  #<-- interrupt this line
#    except Exception:
#        print("Error")

