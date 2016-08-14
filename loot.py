#/usr/bin/python
from click import echo, style, group, command, option, argument, prompt
import requests
import json
import pprint
from os.path import join, expanduser
import base64

try:
    # python 2
    import ConfigParser as configparser
    def bytes(string, encoding=None):
        return str(string)
except:
    # python 3
    import configparser


config = configparser.ConfigParser()
config.readfp(open(join(expanduser('~'), '.loot.conf')))
USERNAME = config.get('loot', 'username')
PASSWORD = config.get('loot', 'password')


@group()
def cli():
    """loot helps you work with github in terminal without 
    pain, use `loot --help` to check supported commands"""
    pass

@command()
@option('--username', '-u', help='Specify github user\' which you want to \
                                    check or download')
@option('--password', '-p', help='account password')
@option('--keyword', '-k', help='Keyword you want to search')
@option('--pprint', is_flag=True, help="Pretty print")
@option('--create', '-c', is_flag=True, help="create gist")
@option('--path', '-p', help='path of the file that you want to create as gist')
def gist(username, password, keyword, prettyprint, create):
    """check gist information"""
    if not user and not create:
        echo('please use `loot gist --help to check supported options`')
    elif create:
        if not path:
            echo('please specify the path of file that you want to create as gist')
        else:
            gist_filename = path.split('/')[-1]
            with open(path, 'rb') as gist_file:
                content = gist_file.read()
            description = prompt('Description of this gist: ')
            public = prompt('Do you want to make it public? (y/n)', default='y').lower()

            username = username or USERNAME
            password = password or PASSWORD

            basic_auth_token = base64.b64encode(bytes('{0}:{1}'.
                format(username, password), 'utf-8')).encode('ascii')
            authorization = 'Basic {0}'.format(basic_auth_token)
            headers = {
                'Authorization': authorization
            }
            data = {
                "description": description,
                "public": public,
                "files": {
                    
                }
            }

        
    else:
        r = requests.get('https://api.github.com/users/{0}/gists'.format(user))
        json_res = r.json()
        result = []
        for r in json_res:
            id = r['id']
            files = r['files']
            description = r['description']
            file_result = []
            for file in files:
                file_name = file
                language = files[file]['language']
                raw_url = files[file]['raw_url']
                file_dict = {
                    'file_name': file_name,
                    'language': language,
                    'raw_url': raw_url
                }

                # search in by filename and description
                if keyword:
                    if keyword in file_dict['file_name'] or keyword in description:
                        file_result.append(file_dict)
                    else:
                        continue
                else:
                    file_result.append(file_dict)
            
            if len(file_result) > 0:
                single_result = {
                    'id': id,
                    'description': description,
                    'files': file_result
                }
            else:
                continue
            result.append(single_result)

        if prettyprint:
            echo(json.dumps(result, indent=4, sort_keys=True))
        else:
            echo(result)

@command()
@argument('gist_id')
@option('--dir', '-d', default='.', help='directory to store downloaded gist file')
def clone(gist_id, dir):
    """download gist"""
    r = requests.get('https://api.github.com/gists/{}'.format(gist_id))
    json_res = r.json()
    files = json_res['files']
    description = json_res['description']
    files_count = len(files)
    echo(style('{0} files in this gist\n'.format(files_count), fg='green'))
    echo(style('Description: {0}\n'.format(description), fg='cyan'))
    echo(style('List files: \n'))
    gists = []
    for file in files:
        gist_file_info = files[file]
        filename = gist_file_info['filename']
        echo(style("        {0}\n".format(filename), fg='red'))

        raw_url = gist_file_info['raw_url']
        gists.append({
            'filename': filename,
            'raw_url': raw_url 
        })

    value = 'y'
    if files_count > 1:
        value = prompt('Download them all? (y/n)', default='y').lower()
    if value == 'y' or value == '':
        for gist in gists:
            filename = gist['filename']
            raw_url = gist['raw_url']
            path = join(dir, filename)
            with open(path, 'wb') as gist_file:
                echo('downloading {0}'.format(filename))
                content = requests.get(raw_url).content
                gist_file.write(content)
        echo('done...')
    elif value == 'n':
        pass


cli.add_command(gist)
cli.add_command(clone)
