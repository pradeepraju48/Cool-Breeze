'''
first check for palindrome
have twopointers
move pointer by one and compare str and rev(str) if true add to temp list


def palindromecheck(str1):
    temp = list()
    for i in range(0,len(str1)):
        for j in range(i,len(str1)):
            temp1 = str1[i:j+1]
            temp2 = temp1[::-1]
            if(temp1 == temp2):
                if(temp1 not in temp):
                    temp.append(temp1)

    print(temp)





if __name__ == '__main__':

    str1 = "abbbaberrtrrabarrt"
    palindromecheck(str1)
'''
'''

'''

def longconnum(abc):
    temp = []
    j = 0
    count = 0
    for i in range(0,len(abc)):
        curreindex = i
        if( i == 0):
            continue
        if(abc[i] != abc[i-1]+1 or i == len(abc)-1):
            if(len(abc[j:i])>=len(temp)):
                temp  = abc[j:i]
                j = curreindex
        else:
            continue
        count = 0

    print(temp)

if __name__ == '__main__':
    list1 = [1,11,3,0,15,5,2,4,10,7,12,6,13,14,16,17,18]
    list1.sort()
    longconnum(list1)



# Write a program that will take an input string. This will be a directory path. Recursively list out the paths of all the files and directories within the input path. This should be an OS agnostic approach.

        # Ex : \a\b\c
        #            f1
        #            f2
        #            d1
        f4
        d3
        d5
        f5

o / p:
f1, f2, d1, f4, d3, d5

\a\b\c\f1
\a\b\c\f2
\a\b\c\d1
\a\b\c\d1\f4
\a\b\c\d1\d3

os.listdir(path) - returns a list of files and directories under the given path
os.path.join(a, b) - joins two paths with the os specific path seperator
os.path.isdir(path) - returns true if the given path is a directory



def listfiledir(str1):
    lst = os.listdir(str1)
    print("files under", str1, "--", [files for files in lst if (!os.path.isdir(file))])
    for x in lst:
        if (os.path.isdir(x)):
            listfiledir(x)
        else:
            print(str1 + x)


if __name__ == '__main__':
    str1 = input()
    listfiledir(str1)

++++++++++++++++++++++


class clientcon():
    timeout = 1800


def __init__(self, username, password):
    self.username = username
    self.password = password
    self.ipaddress = ipaddress


def Connect(self, user: username, Pass: password, **adddic):
    # use ssh to establish ssh connection

    def Disconnect(self, )

    # use disconnect

    def execute(self, cmd: command):
        use
        ssh
        object
        to
        execute
        command.


if __name__ == '__main__':
    cl = clientcon(username, apssword)
