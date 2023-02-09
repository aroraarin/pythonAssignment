class Valid:
    #validator to check whether input row is valid or not
    def validator(self, str):
        for i in str:
            if  i != " " and i!='X'and i!='O':
                return False
        return True        
