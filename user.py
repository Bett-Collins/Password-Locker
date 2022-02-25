class User:
    """
    Class that generates new instances of users.
    """
    user_list = [] #empty details list

    def __init__(self,user_name,user_password,user_email):
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email    

    def save_user(self):

        '''
        save_details method saves details objects into details_list
        '''

        User.user_list.append(self)    


    def delete_user(self):

        '''
        delete_details method deletes a saved details from the details_list
        '''

        User.user_list.remove(self)   


    @classmethod
    def find_user_by_name(cls,name):
        for details in cls.user_list:
            if User.user_name == name:
                return User 


    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a details exists from the details list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the details exists
        '''
        for User in cls.user_list:
            if User.user_password == user_name:
                    return User

        return False      


    @classmethod
    def display_user(cls):  #check this line later
        '''
        method that returns the details list
        '''
        return cls.user_list
        