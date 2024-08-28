#String Methods
#isdigit()#True if all the characters are digits. Otherwise, False
is_digit = "4748"
result=is_digit.isdigit()
print(result)#true


#Replace()-Gives a new string after replacing all the occurrences of the old substring with the new substring.
sentence = "teh cat and teh dog"
sentence = sentence.replace("teh","the")
print(sentence)#the cat and the dog


#Startswith()-True if the string starts with the specified value. Otherwise, False
url = "https://google.com"
is_secure_url = url.startswith("https://")
print(is_secure_url)#True


#Endswith()-True if the string ends with the specified value. Otherwise, False
gmail_id = "rahul123@gmail.com"
is_gmail = gmail_id.endswith("@gmail.com")
print(is_gmail)#True


#Lower()-Gives a new string by converting each character of the given string to lowercase.
name = "RAVI"
print(name.lower())#ravi


#Upper()-Gives a new string by converting each character of the given string to uppercase.
name = "ravi"
print(name.upper())#RAVI


#Join()-Takes all the items in a sequence of strings and joins them into one string.
list_a = ['Python is ', ' progr', 'mming l', 'ngu', 'ge']
string_a = "a".join(list_a)
print(string_a)#Python is a programming language


#Swapcase()-upper case to lowerr case and lower case to upper case
name="RAMA krishna"
result=name.swapcase()
print(result)#rama KRISHNA


#title()-1ST CHARACTER OF WOARD IS CAPITAL 
name="kEY boARD"
result=name.title()
print(result)#Key Board


#capitalize()-in character 1st word only becomes capital
name="blue shirt e"
result=name.capitalize()
print(result)#Blue shirt e


#isalnum()_in character alphabets and integers are consists means it gives true ,any special character is there means it will give the out put false.
name="rajeshgmail1410"
result=name.isalnum()
print(result)#true


#isalpha()-only alphabets it will give the out put true other wise false.
name="rakesh"
result=name.isalpha()
print(result)#True


#isdigit()-only integers it will give the out put true other wise false.
name="64578667574"
result=name.isdigit()
print(result)#True


#isupper()-only upper case letters it will give the out put true other wise false.
name="KOWSHIK"
result=name.isupper()
print(result)#True


#islower()-only lower case letters it will give the out put true other wise false.
name="mousE"
result=name.islower()
print(result)#false


#istitle()-only characters starting letter is capital it will give the out put true other wise false.
name="Bed SheeT"
result=name.istitle()
print(result)#false


#isspace()-only space with out character it will give the out put true other wise false.
name="      "
result=name.isspace()
print(result)#true



