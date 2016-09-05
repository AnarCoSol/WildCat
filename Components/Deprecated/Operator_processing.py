class Operator_processing():
    def __init__(self):
        pass
    
    def processing(self,code_appender = list(), role = str()):
        for code in code_appender:
                tokens =  code.Subject.split(" ")
                #print tokens
                if tokens[0] == "" or tokens[0] == "node" or tokens[0] == platform.uname()[1]:
                        i = 0
                        code.Subject = str()
                        for tok in tokens:
                                if i != 0:
                                        code.Subject += tok
                                        code.Subject += " "
                                i += 1
                        #clean string removing the last space char
                        code.Subject = code.Subject[:len(code.Subject)-1]
                else:
                        continue

                if code.Subject == "exviemshse":
                    pass
                
                if len(code.Subject) >= 12:
                        if code.Subject[:12] == "run body as ": #not tested 17/1/16
                                if code.Subject[12:] == "python":
                                    pass
                                        
                        elif code.Subject[:13] == "save body as ": #not tested 17/1/16
                            pass
                                
                if code.Subject == "run body": #not tested 17/1/16
                    pass
                
                if code.Subject[- len("body as args"):] == "body as args": #not tested 09/05/16
                    pass

                else:
                    pass
                        
        return "continue" 
