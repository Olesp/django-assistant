import os, pathlib, timeit, glob
from jinja2 import Environment, FileSystemLoader

def main():
    os.system('clear')
    welcome()
    apps = scan_for_apps()
    while True:
        print('Here\'s the list of avaible options')
        main_menu()
        os.system('clear')


def welcome():
    print('Welcome to Django Assistant. This CLI will help you with common tasks.')


def get_choices_str(choices_list):
    choices_str = ''

    count = 1
    for choice in choices_list:
        choices_str += str(count) + '.' + choice + '\n'
        count += 1

    return choices_str


def main_menu():
    choices_functions = {
        1: new_model,
        2: new_form,
    }
    choices_list = {
            '1':'Create a model',
            '2':'Create a form'
        }
    for key, value in choices_list.items():
        print(key, ' : ', value)
    is_valid_choice = False
    while not is_valid_choice:
        choice = input('Enter your choice (press ? to list choices again) : ')
        if choice == '?':
            for key, value in choices_list.items():
                print(key, ' : ', value)
        is_valid_choice = False
        if choice in choices_list:
            is_valid_choice = True
    os.system('clear')
    choices_functions[int(choice)]()

def create_model(user_model):
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('model_template.py.jinja')
    model_str = template.render(user_model)


    with open("test.py","w") as fh:
        fh.write(model_str)
    input('Model saved')

def new_model():
    '''
    Start the process of creation for a new model class.
    It will call functions to create the fields and save the model class to the models file
    '''
    model_name = input('Please enter a name for the model (eg : Post) : ').capitalize()
    model_name = model_name.capitalize()
    fields = create_model_fields()
    user_model = {
        'model_name':model_name,
        'model_verbose_name':model_name,
        'fields':fields
    }
    create_model(user_model)

def create_model_fields():
    '''
    Create the fields list. It will be returned to be passed to the templating system
    '''
    fields_list = []

    avaiable_types = {
            'bool':'BooleanField',
            'char':'CharField',
            'date':'DateField',
            'datetime':'DateTimeField',
            'mail':'EmailField'
        }

    is_finished = False
    while not is_finished:
        field_name = input('Enter the name of the field or press <return> to stop adding fields (one field at least is required) : ')
        if field_name == '':
            is_finished = True
        else:
            is_correct_type = False
            while not is_correct_type:
                field_type = input('Field type (enter ? to see all types) : ')
                if field_type == '?':
                    for key, value in avaiable_types.items():
                        print(key, ' : ', value)
                elif field_type in avaiable_types :
                    is_correct_type = True
        if not is_finished:
            fields_list.append({'name':field_name, 'type':avaiable_types[field_type]})
    return fields_list

def new_form():
    '''
    Start the process of creation for a new form class.
    It will call functions to create the fields and save the form class to the forms file
    '''
    form_name = input('Please enter a name for you form (eg : Contact -> ContactForm will be created) :')
    form_name = form_name.capitalize()
    print(form_name)
    fields = create_form_fields()
    user_form = {
        'form_name':form_name,
        'fields':fields
    }
    create_form(user_form)


def create_form(user_form):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('form_template.py.jinja')
    form_str = template.render(user_form)


    with open("test.py","w") as fh:
        fh.write(form_str)
    input('Form saved')

def create_form_fields():
    fields_list = []

    avaiable_types = {
            'bool':'BooleanField',
            'char':'CharField',
            'date':'DateField',
            'datetime':'DateTimeField',
            'mail':'EmailField'
        }

    is_finished = False
    while not is_finished:
        field_name = input('Enter the name of the field or press <return> to stop adding fields (one field at least is required) : ')
        if field_name == '':
            is_finished = True
        else:
            is_correct_type = False
            while not is_correct_type:
                field_type = input('Field type (enter ? to see all types) : ')
                if field_type == '?':
                    for key, value in avaiable_types.items():
                        print(key, ' : ', value)
                elif field_type in avaiable_types :
                    is_correct_type = True
        if not is_finished:
            fields_list.append({'name':field_name, 'type':avaiable_types[field_type]})
    return fields_list

def scan_for_apps():
    path = r"."
    app_list = [f.name for f in os.scandir(path) if f.is_dir() and os.path.isfile(f.path+'/models.py')]
    return app_list

if __name__ == "__main__":
    main()
