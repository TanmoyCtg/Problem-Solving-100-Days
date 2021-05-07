import  json

file = open('SUPGE.json')


with file as f:

    d = json.load(f)
    for i in d:
        # print(i.get('id'))
        if i.get('status') =='document.production':
            print (i.get('id'))
        # print(i.get('status'))