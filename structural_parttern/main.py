# def execute_command(command: str) -> None:
#     if command == 'ls':
#         print('$ listing files')
#     elif command == 'cd':
#         print('$ changing directory')
#     else:
#         print('$ comando not implemented')

# execute_command('ls')

# def execute_command(command: str) -> None:
#     match command:
#         case 'ls':
#             print('$ listing files')
#         case 'cd':
#             print('$ changing directory')
#         case _: # Não obrigatorio
#             print('$ comando not implemented')

# execute_command('cd')

# def execute_command(command: str) -> None:
#     match command.split():
#         case ['ls', *directorys]:
#             for direct in directorys:
#                 print('$ listing files ' + direct)
#         case ['cd', path]:
#             print('$ changing directory to ' + path) 
#         case _: # Não obrigatorio
#             print('$ comando not implemented')

# execute_command('ls all')

# def execute_command(command: str) -> None:
#     match command.split():
#         case ['ls' | 'list', *directorys]:
#             for direct in directorys:
#                 print('$ listing files ' + direct)
#         case ['ls' | 'list', *directorys, 'force']:
#             for direct in directorys:
#                 print('$ listing FORCED files ' + direct)
#         case ['cd', path]:
#             print('$ changing directory to ' + path) 
#         case _: # Não obrigatorio
#             print('$ comando not implemented')

# execute_command('ls /Home /C /Hello')
# execute_command('list /Home /C /Hello force')
# execute_command('cd /Home /C /Hello')

# def execute_command(command: str) -> None:
#     match command.split():
#         case ['ls' | 'list', *directorys] if len(directorys) > 1:
#             for direct in directorys:
#                 print('$ listing files ' + direct )
#         case ['cd', path]:
#             print('$ changing directory to ' + path) 
#         case _: # Não obrigatorio
#             print('$ comando not implemented')

# execute_command('ls /Home /C /Hello')
# execute_command('ls')

# def execute_command(command: str) -> None:
#     match command.split():
#         case ['ls' | 'list' as the_command, *directorys] as the_list if len(directorys) > 1:
#             for direct in directorys:
#                 print('$ listing files ' + direct )
#             print(f'The command {the_command=}, {the_list=}') 
#         case ['cd', path]:
#             print('$ changing directory to ' + path) 
#         case _: # Não obrigatorio
#             print('$ comando not implemented')

# execute_command('ls /Home /C /Hello')
# execute_command('ls')

# def execute_command(command: str) -> None:
#     match command:
#         case {'command': _, 'directories': [_, *_]}:
#             for directory in command['directories']:
#                 print(f'lista todos os diretorios {directory}')
#         case _:
#             print('Não encontrado')

# execute_command({'command': 'ls', 'directories': []})
# # execute_command('ls')
# # execute_command({'ls', 'ola'})

