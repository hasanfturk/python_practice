#list ve set veri yapılarını kullanarak tekrar eden elemanları silip,aynı isimde bu sefer tekrar eden elemanı olmayan liste

numbers_list = [1,2,3,2,4,5,3,6,2,7,5,8]

#numbers_set = set() # boş set oluşturur

numbers_set = set(numbers_list)
print(numbers_set)
numbers_list = list(numbers_set)
print(numbers_list)