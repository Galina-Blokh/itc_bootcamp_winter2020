import json

FILE_NAME = 'incident.json'
COMPANY_NAME = 'Microsoft Corporation'


def name_of_every_process(json_dict, company_name):
    """ A recursive function, explore the tree in the file incident.json (Image 1)
    and print the name of every process signed by Microsoft Corporation and its parent’s name
    """
    for elem in json_dict['children']:
        if elem['sig_company'] == company_name:
            print('{} with {} as parent'.format(elem['name'], json_dict['name']))
        name_of_every_process(elem, company_name)


def main():
    json_dict = json.load(open(FILE_NAME))
    name_of_every_process(json_dict, COMPANY_NAME)


if __name__ == '__main__':
    main()
