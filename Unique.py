import numpy as np

survey_responses=np.array(["bueno","excelente","malo","bueno","excelente","malo"])

print("Respuestas únicas:")
print(np.unique(survey_responses))

print("Respuestas únicas y sus conteos:")
unique, counts = np.unique(survey_responses, return_counts=True)
print(unique)
print(counts)

#crear copias
array_x =np.arange(10)
copy_x = array_x[[1,2]]
print("Array original:")
print(array_x)
print("Copia del array:")
print(copy_x)
