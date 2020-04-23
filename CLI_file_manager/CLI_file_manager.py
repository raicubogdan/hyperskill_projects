# CLI file manager that recursively copies, cuts, deletes
# and renames files in and from a directory or directory tree


from operations import copy, cut, delete, rename


print('\n---CLI File manager---')
print('\nYou will be prompted to type the appropriate information\n'
      '(root folder, destination folder,file extension, file name, etc)\n'
      'after you choose an option.')

while True:
    option = input('\nWhat do you want to do?\n'
                   '1. Copy (by extension)\n'
                   '2. Cut (by extension)\n'
                   '3. Delete\n'
                   '4. Rename\n'
                   '5. Exit\n>> ')

    if option == '1':
        copy()

    elif option == '2':
        cut()

    elif option == '3':
        delete()

    elif option == '4':
        rename()

    elif option == '5':
        exit()

    else:
        print('\nInvalid input')
