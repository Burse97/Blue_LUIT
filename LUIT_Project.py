#! /usr/bin/env python3.7

#1. The list should be empty initially.
my_list = [ ]

#2. Populate the list using append or insert.
my_list.append('S3')
my_list.append('Lambda')
my_list.append('EC2')
my_list.append('Cloudfront')

#3. Print the list and the length of the list.
print("The AWS list is: ", my_list)
print("The length of the list is ", len(my_list))

#4. Remove two specific services from the list by name or by index.
del my_list[1]
del my_list[2]

#5. Print the new list and the new length of the list.
print("The AWS list is: ", my_list)
print("The length of the list is: ", len(my_list))
