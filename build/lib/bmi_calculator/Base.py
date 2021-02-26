import os, sys

sys.path.append(os.path.abspath("."))


class Base:
    
    """
    @TYPE   :   Class
    @DESC   :   Blue print of Data Structure
    @AUTHOR :   Aniket Basu
    @EMAIL  :   aniketbasu7@gmail.com
    """

    _DATA = None
    
    def get_data(self) -> None:

        """
        @TYPE   :   Method
        @DESC   :   get output
        @AUTHOR :   Aniket Basu
        @EMAIL  :   aniketbasu7@gmail.com
        """
        
        return {
            "DATAFRAME" : self._DATA
        }