
responseTimes = [100,200,150,300,]



def countResponseTimeRegressions(responseTimes):
    #Recorrer el arreglo skipeando el primero 
    #Si el numero es mayor al promedio delos numeros anteriores count +1 
    #regresar el contador al  final del loop 
    
    previus_array = []
    count =0
    for index,response in enumerate(responseTimes):
        if index == 0: 
            previus_array.append(response)
            print(previus_array)
        elif index<(len(responseTimes)): 
            previus_array.append(response)
            print (f"average{ average(previus_array)}")
            if response > average(previus_array):
                count +=1
                print (f"average{ average(previus_array)}")
                print(count)
    return count
                
        

def average(array_of_numbers):
    print(f"len array: {len(array_of_numbers)}")
    if len(array_of_numbers) == 1: 
        return array_of_numbers[0]
    else:  
        total = 0
        for number in array_of_numbers:
            total+=number
        average = total/len(array_of_numbers)
        return average
    
countResponseTimeRegressions(responseTimes)