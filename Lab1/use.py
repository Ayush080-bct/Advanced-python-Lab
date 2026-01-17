import datasample as ds
sample=ds.data_sample("sample 1",[10,20,30,40,50])#data_sample is class name in case of c++
#we defined datatype in compile time like data_sample sample= ,
# but in python datatype is defined in runtime.
#Create an object of class data_sample 
# (defined inside module datasample) and bind it to variable sample”
sample.display()
print(sample.summary())
