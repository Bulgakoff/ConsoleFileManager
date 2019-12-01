import sys
from core import create_file, create_folder, del_ff, info_path, copy_ff, save_data
save_data('Start')
command = sys.argv[1]

if command == 'info':
    info_path()
elif command == 'create_f':
    try:
        name = sys.argv[2]
    except IndexError as a:
        print(f'====>{a}')
    else:
        print('all right  create_file!!!!!!!')
        create_file(name)
elif command == 'create_ff':
    name = sys.argv[2]
    create_folder(name)
elif command == 'del':
    name = sys.argv[2]
    del_ff(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError as d:
        print(f'----> {d}')
    else:
        print('all right !!!')
        copy_ff(name, new_name)

elif command == 'help':
    print('помощь')

save_data('FInish ')