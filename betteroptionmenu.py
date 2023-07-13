import tkinter

class BetterOptionMenu(tkinter.OptionMenu):
    """
    An implementation of the tkinter OptionMenu, which inherets tkinter.OptionMenu.
    It gives you the ability to add / remove items from the Option List,
    Get Options from the List,
    Get the Number of Options in the list
    Return the selected Option Value and selected Option Index
   
    Methods
    -------
    SelectOption(Index)
        Selects an Option in the OptionMenu specified by the Index integer
    AddOptions(LstOptions)
        Adds options to the OptionMenu speciefied by lstOptions list
    AddOption(Option)
        Adds the option to the OptionMenu specified by Option string
    DeleteOption(Index)
        Deletes an option from the OptionMenu specified by the Index integer
    DeleteOptions()
        Deletes all options from the OptionMenu
    GetOption(Index)
        Returns the option as a string specified by the Index integer
    GetOptions()
        Returns all the options contained in the OptionMenu as a list of strings
    GetNumberOrOptions()
        Returns the total number of Options contained in the OptionMenu
    RenameOption(Index, Option)
        Renames an Option to match the Option string specified by the Index integer
    """
    
    def __init__(self, parent, StrVar=None, IntVar=None, LstOptions=None, DefaultValue="", command=None):
        """
        Parameters
        ----------
        parent : tkinter.TK
            the parent container of the OptionMenu
        StrVar : tkinter.StringVar()
            the tkinter string variable used to get / set the selected Option's value
        IntVar : tkinter.IntVar()
            the tkinter integer variable used to get / set the selected Option's index
        LstOptions : list
            the List of strings used to display the Options in the OptionMenu
        DefaultValue : str
            the string used to display a default value in the Option Menu if nothing is selected
            this can happen if the object initializes with no selected value
            this can happen if the selected option is deleted
            this can happen if an index is selected that does not exist
        command : function(Option, Index)
            the function to be called with the parameters Option and Index.
            This function is called when an Option is selected and the selected Option Value and Option Index is returned through the functoin
        """
        if (StrVar is None):
            self.__StrVar = tkinter.StringVar()
        else:
            self.__StrVar = StrVar

        if (IntVar is None):
            self.__IntVar = tkinter.IntVar()
        else:
            self.__IntVar = IntVar


        self.__IntVar.trace("w", self.__evtIntVarSet__)

        self.__StrVar.set(DefaultValue)
        self.__DefaultValue = DefaultValue
        
        super().__init__(parent, value="",variable=StrVar)
        self.__command = command
        self.__lstOptions = LstOptions
           
        self.__menu = self["menu"]      #Get the Menu Object from the OptionMenu Object
        self.__menu.delete(0, "end")    #Delete all of the Objects contained inside the OptionMenu Object

        #Loop through each of the values contained in the list and generate buttons on the menu
        #Assign the Button Label and Command function to return the value and the index
        for index, value in enumerate(LstOptions):
            self.__MenuAdd__(value, index)


    def __MenuAdd__(self, value, index):
        """__Internal Function__ that Adds a Menu Command to the Option Menu
        This function assigns the Menu Button Label text,
        and command that assigns the selected value and index to the tkinter
        String and Intiger values.  Also combine the callback command function specified

        Parameters
        ----------
        value : str
            The value used to display the Option Command Label string
            Also used for the command callback function specified to indicate which Option was selected
        index : int
            The index used to for the command callback function specified to indicate which Option was selected by index
        """
        self.__menu.add_command(label=value,
                                command=lambda value=value, index=index: [self.__StrVar.set(value),
                                                                          self.__IntVar.set(index)])

    def __MenuEdit__(self, value, index):
        """__Internal Function__ that Modifies a Menu Command in the Option Menu
        This function assigns the Menu Button Label text,
        and command that assigns the selected value and index to the tkinter
        String and Intiger values.  Also combine the callback command function specified

        Parameters
        ----------
        value : str
            The value used to display the Option Command Label string
            Also used for the command callback function specified to indicate which Option was selected
        index : int
            The index used to for the command callback function specified to indicate which Option was selected by index
        """
        self.__menu.entryconfigure(index,
                                   label=value,
                                   command=lambda value=value, index=index: [self.__StrVar.set(value),
                                                                             self.__IntVar.set(index)])

    def __evtIntVarSet__(self, var, index, mode):
        """__Internal Function__ that executes when the IntVar changes
        This function assigns StrVar value based on the Option specified by the Index specified by IntVar
        It is used so that the selected option can be set by index
        """
        self.SelectOption(self.__IntVar.get())

    def SelectOption(self, Index):
        """Selects the Option in the Option Menu based on the Index integer
           If the Index is out of range the DefaultValue string is applied

        Parameters
        ----------
        index : int
            The index used to select the Option in the Option Menu
        """
        if self.GetNumberOfOptions() >= Index >= 0:
            self.__StrVar.set(self.GetOption(Index))
        else:
            self.__StrVar.set(self.__DefaultValue)


    def AddOptions(self, LstOptions):
        """Adds Options to the OptionMenu

        Parameters
        ----------
        LstOptions : list
            A list of strings to be added as Options to the OptionMenu
        """
        for Option in LstOptions:
            self.AddOption(Option)

    def AddOption(self, Option):
        """Adds a Option to the OptionMenu

        Parameters
        ----------
        Option : str
            An Option to be added to the OptionMenu
        """
        index = len(self.__lstOptions)   #Get the index value to return (The length of the list of Options)
        self.__lstOptions.append(Option)
        self.__MenuAdd__(Option, index)

    def DeleteOption(self, Index):
        """Deletes an Option from the OptionMenu by the Index Position

        Parameters
        ----------
        Index : int
            The position of the Option to be deleted from the OptionMenu
        """
        del self.__lstOptions[Index]    #Delete the Option from the Option List with the specified Index
        self.__menu.delete(Index)       #Delete the Object from the Option List with the specified Index

        if Index == self.__IntVar.get():  #This means the selected Option is being deleted
            self.__StrVar.set(self.__DefaultValue) #Assign the default value
        else:
            if Index > self.__IntVar.get(): #If the Index is greater than the selected index 
                self.__IntVar.set(Index -1) #This means that the selected index is decremented by one.

        #Need to loop through the remainder to update the indexes
        for i, value in enumerate(self.__lstOptions):
            if i >= Index:
                self.__MenuEdit__(value, i)

    def DeleteOptions(self):
        """Deletes all Options of the OptionMenu
        """
        self.__lstOptions = []          #Clear the Options List
        self.__menu.delete(0, "end")    #Delete all of the Objects contained inside the OptionMenu Object
        self.__StrVar.set(self.__DefaultValue)  #The Option is deleted set the Default Value in the OptionMenu

    def GetOption(self, Index):
        """Returns a Option Label Value of the Specified Index

        Parameters
        ----------
        Index : int
            The position of the Option to have the Label Value returned from the OptionMenu

        Returns
        -------
        str
            The Option Label Value of the specified by the Index
        """
        return self.__lstOptions[Index]

    def GetOptions(self):
        """Returns a list of Option Label Value

        Returns
        -------
        list
            A List of Strings of the Option Label Values
        """
        return self.__lstOptions

    def GetNumberOfOptions(self):
        """Returns the total number of Options contained in the OptionMenu

        Returns
        -------
        int
            The total number of Options contained in the OptionMenu
        """
        return len(self.__lstOptions)

    def RenameOption(self, Index, Option):
        """Renames an Option Label Value of the Specified Index

        Parameters
        ----------
        Value : str
            The value used to display the Option Command Label string
            Also used for the command callback function specified to indicate which Option was selected
        Index : int
            The position of the Option to have the Label Value renamed
        """
        self.__lstOptions[Index] = Option   #Change the Option at the index
        self.__MenuEdit__(Option, Index)
        self.SelectOption(self.__IntVar.get()) #Update the Selected Option based on the current IntVar.  This is incase the selected Option is Renam