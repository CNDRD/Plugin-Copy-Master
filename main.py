import os, shutil

ABS_PATH_VOLUMES = '/var/lib/pterodactyl/volumes'

def main():
    operation = getOperation()
    src_file_path = getSrcFile(operation)
    count = doTheThings(operation, src_file_path)
    end(operation, src_file_path, count)





def getOperation():
    while(True):
        amogus = input('Operation (copy/del): ')
        if amogus.lower() == 'copy' or amogus.lower() == 'del':
            return amogus.lower()


def getSrcFile(operation):
    switch = {
        'copy':'Enter an absolute plugin filepath: ',
        'del':'Enter the plugin filename: '
    }

    while(True):
        huh = input(switch[operation])
        if huh and huh.endswith('.jar'):
            return huh.replace('\\', '/')


def doTheThings(op, src):
    count = 0
    for destination in os.listdir(ABS_PATH_VOLUMES):
        dest_plugins_path = f'{ABS_PATH_VOLUMES}/{destination}/plugins/'

        if op == 'copy':
            shutil.copy(src, dest_plugins_path)
            count += 1
        elif op == 'del':
            os.remove(f'{dest_plugins_path}/{src}')
            count += 1
    return count


def end(op, file, count):
    the_ol_switcharoo = {
        'copy':f'Succesfully copied all files to all {count} destinations!',
        'del':f'Succesfully deleted \'{file}\' from {count} destinations!'
    }
    print(the_ol_switcharoo[op])


if __name__ == '__main__':
    main()
