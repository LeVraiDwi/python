ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[ft_list.index("tata!")] = "World!"
ft_tuple = "Hello", "France!"
ft_secondSet = {"Paris!", "tutu!"}
ft_set = ft_secondSet.symmetric_difference(ft_set)
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
