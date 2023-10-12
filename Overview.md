## 1. Which package/library did you select?

I selected the BCrypt library for Python.[ref](https://pypi.org/project/bcrypt/)

## 2. What is the package/library?
### • What purpose does it serve?
The BCrypt library serves as a way to hash values with salt to allow for them to be stores in a format that cannot be easily brute forced or guessed even in the case that someone is able to gain access to the database or file that the passwords are stored in.[ref](https://www.tutorialspoint.com/hashing-passwords-in-python-with-bcrypt) The benefit to using BCrypt is the ability to salt the password in addition to simply hashing the password and calling that good enough. Rainbow tables are utilitized to speed up the process of brute forcing passwords by calculating the hashes of many common passwords in advance.[ref](https://www.howtogeek.com/devops/how-to-properly-store-passwords-salting-hashing-and-pbkdf2/) There are websites that have massive rainbow tables readily available to utilize in case you might have access to a large amount of unsalted passwords.[ref](https://crackstation.net/) Being able to protect against the use of rainbow tables is detrimental to properly storing passwords, and salting passwords is an excellent way to do so. Of course a better way to protect against password attacks is to not bother with storing passwords at all and use OAuth if applicable. 
### • How do you use it?
To use BCrypt in Python, you must of course import the libary followed by the input or creation of a password. 
    import bcrypt 

    # example password 
    password = 'password123'

Then you must convert the password string into an array of bytes.

    # converting password to array of bytes 
    bytes = password.encode('utf-8') 

Next the salt is generated using the bcrypt library. In theory you could create your own salt and refer to it again for checking the password later. 

    # generating the salt 
    salt = bcrypt.gensalt() 

Next the encoded password is hashed using the salt.     

    # Hashing the password 
    hash = bcrypt.hashpw(bytes, salt) 

[ref](https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/)

To check the password we use .checkpw to compare an encoded password against the previous password. This can only be done if the salt is known for the "randomUserPass" in this example. If a stored hash is attempted to be checked, this will fail due to the salt not being correct.

    guessPass = input("Enter a passwork to guess")
            encodedGuess = guessPass.encode('utf-8')
            result = bcrypt.checkpw(encodedGuess, randomUserPass)

## 3. What are the functionalities of the package/library?

Salt generation.

    salt = bcrypt.gensalt()

Password checking or comparison.

    if bcrypt.checkpw(password, hashed):
        print("It Matches!")
    else:
        print("It Does not Match :(")
    [ref](https://github.com/pyca/bcrypt)

Hashing psaswords:

    hash = bcrypt.hashpw(bytes, salt) 

## 4. When was it created?
BCrypt itself was created in 1999, however the Python libary was released on May 11, 2013. [ref](https://pypi.org/project/bcrypt/#history)

## 5. Why did you select this package/library?
This library enables programmers with relative ease to securely store passwords or other important data. While having previous knowledge of how salting and hashing works, you could explain these requiresments to someone with little to no knowledge of encryption or cryptography and they would be able to understand why this is important. Simply storing the passwords in plaintext obviously does not meet necessary requirements for security in any sense, and hashing passwords for storage may act as a simple way to add some security. However hashing and using salt to hash passwords provides an additional element of security that makes BCrypt an incredibly useful libary if you need a way to securely store information. 

## 6. How did learning the package/library influence your learning of the language?
Specifically learning about encoding in utf-8 and realizing that BCrypt cannot operate on simply strings themselves in Python made sense after trying to accomplish hashing a password incorrectly. While Python may have some loose requirements and uses plain language in many cases, in cryptography knowing what exact encoding characters use is important due to the way hashes are generated. [ref](https://www.w3schools.com/charsets/ref_html_utf8.asp)

## 7. How was your overall experience with the package/library?
### • When would you recommend this package/library to someone?
I would recommend this library to anyone who needs a quick and simple way to salt and hash a value in Python. 
### • Would you continue using this package/library? Why or why not?
While this library accomplishes what it needs to by hashing passwords effectively, I would want to avoid using it as much as possible since the idea of programming a secure interface to store passwords seems daunting. If I could avoid programming something like this in a workplace setting for example, I'd alternatively use OAuth. However if a simple program is required and the use of OAuth is too expensive or simply does not make sense for the scale of the program required or if Internet access is not an option, BCrypt is a viable solution. The sample program for example due to the game nature of it would make no sense to use OAuth. 




