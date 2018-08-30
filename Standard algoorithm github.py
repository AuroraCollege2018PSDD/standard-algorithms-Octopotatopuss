
BEGIN MAINPROGRAM




	numArray = []


	continue = True


	WHILE continue:


		choice = Get input "Do you want to (L)oad numbers, (P)rint the Array, (S)um the array, find the ma(X) of the array, find the mi(N) of the array or (Q)uit"


		CASEWHERE choice is


			L: loadArray(numArray)


			P: printArray(numArray)


			S: sumArray(numArray)


			X: maxArray(numArray)


			N: minArray(numArray)


			Q: continue = False


		ENDCASE


	END WHILE


END MAINPROGRAM






BEGIN loadArray(thisArray)


	runSubroutine = true


	WHILE runSubroutine:


		inputNum = get input("Enter the number you wish to add or Q to return to main program")


		IF inputNum == Q:


			runSubroutine = False


		ELSE:


			IF inputNum is a number


				append inputNum to thisArray


			END IF


		ENDIF


	END WHILE	


END loadArray










BEGIN printArray(thisArray)


	let i = 0


	REPEAT


		print thisArray(i)


		i = i +1


	UNTIL i >= size of thisArray


END printArray


BEGIN loadArray 

BEGIN LoadArray

    Let i = 1
   
Read DataValue

WHILE DataValue < > "xxx"

  Let Element (i) = DataValue
   
   i = i + 1
   
    Read DataValue

ENDWHILE

      Let NumElements = i
   
Display " There are" NumElements " items loaded into the array"

END LoadArray

BEGIN SumArray 

Total = 0

    i = 1
   
   Let total = i + Total
   
If i <= Total

       Display “The sum of all elements in the array is 0”
   
If i > Total

Display “The sum of all elements in the array is: “ + Total
   
END SumArray 


BEGIN MaxArray 

Set max to 1

     Let [ i ] Array = 0
   
        If i > 1 THEN 
      
  Set i to Max

If i < 1

Set i to Min 

Display “The highest value is” Max 

END MaxArray 

BEGIN MinArray

    Set min to 1
   
     Let i = 2 
      
       If i < 1 
         
Set i to Min

Display “The lowest value is” Min 

END MinArray




