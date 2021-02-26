import os, sys
sys.path.append(os.path.abspath("."))


from .Base import *


class BMI(Base):

    """
    @TYPE   :   Class
    @DESC   :   Class will help to calculate the BMI
    @PARENT :   Base
    @AUTHOR :   Aniket Basu
    @EMAIL  :   aniketbasu7@gmail.com
    """
    
    def __init__(self, data: dict) -> None:
        
        self._DATA = data
        
        
    def _preprocess_data(self) -> None:

        """
        @TYPE   :   Method
        @SCOPE  :   Private
        @DESC   :   convert height from Cm to M
        @AUTHOR :   Aniket Basu
        @EMAIL  :   aniketbasu7@gmail.com
        """
        
        try:
            self._DATA["HeightM"] = self._DATA["HeightCm"] / 100
        
        except TypeError:
            print("HeightCm should be float type.")
        
        
    def _calculate_bmi(self) -> None:

        """
        @TYPE   :   Method
        @SCOPE  :   Private
        @DESC   :   calculate BMI from WeightKg & HeightM
        @AUTHOR :   Aniket Basu
        @EMAIL  :   aniketbasu7@gmail.com
        """
    
        try:
            self._DATA["BMI"] = self._DATA["WeightKg"] / self._DATA["HeightM"] ** 2

        except TypeError:
            print("WeightKg & HeightM should be float type.")


    def _analysis(self) -> None:
        
        """
        @TYPE   :   Method
        @SCOPE  :   Private
        @DESC   :   labeled the data from BMI
        @AUTHOR :   Aniket Basu
        @EMAIL  :   aniketbasu7@gmail.com
        """

        if self._DATA["BMI"] < 18.5: self._DATA["Class"] = "Under Weight"
        elif self._DATA["BMI"] < 25 and self._DATA["BMI"] >= 18.5: self._DATA["Class"] = "Normal Weight"
        elif self._DATA["BMI"] < 30 and self._DATA["BMI"] >= 25: self._DATA["Class"] = "Over Weight"
        elif self._DATA["BMI"] < 35 and self._DATA["BMI"] >= 30: self._DATA["Class"] = "Moderately Obese"
        elif self._DATA["BMI"] < 40 and self._DATA["BMI"] >= 35: self._DATA["Class"] = "Severely Obese"
        else: self._DATA["Class"] = "Severely Obese"

    
    def run(self) -> None:

        """
        @TYPE   :   Method
        @SCOPE  :   Public
        @DESC   :   call all function in batch
        @AUTHOR :   Aniket Basu
        @EMAIL  :   aniketbasu7@gmail.com
        """
        self._preprocess_data()
        self._calculate_bmi()
        self._analysis()