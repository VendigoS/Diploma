import hashlib
import json
import time

import pymongo
from bson import json_util

from default_data import pytokens, pyrules, sharp_tokens, severity, priority, first_persons
from utils import Token, Border, Rule, Bug


def login(login, passwd, mongo_address="mongodb://localhost:27017/", mongo_db="bug_tracking",
          mongo_collection="persons", hint_field='login', logfile=None):
    try:
        result = None
        client = pymongo.MongoClient(mongo_address)
        db = client[mongo_db]
        collection = db[mongo_collection]
        user = collection.find_one({hint_field: login})
        if not user:
            result = None
        else:
            password = user['password']
            if not password:
                result = None
            else:
                if hashlib.md5(passwd.encode('utf-8')).hexdigest() == password:
                    result = user
                else:
                    result = False

    except Exception as ex:
        print('The error has occured')
        print(ex)

    finally:
        if client:
            client.close()
        if result:
            return result


def change_mongo(search_by, change_fields, mongo_address="mongodb://localhost:27017/", mongo_db="", mongo_collection="",
                 logfile=None):
    try:
        result = None
        client = pymongo.MongoClient(mongo_address)
        db = client[mongo_db]
        collection = db[mongo_collection]

        collection.update(search_by, {"$set": change_fields})
        result = True

    except Exception as ex:
        print('The error has occured')
        print(ex)

    finally:
        if client:
            client.close()
        return result


def make_dump_mongo(mongo_address="mongodb://localhost:27017/", mongo_db="python", mongo_collection="tokens",
                    filename="dump_mongo_python_tokens.json", logfile=None):
    '''
    The method get address of mongo db with adres of host and name of collection and name of file to dump in this collection.
    '''
    try:
        client = pymongo.MongoClient(mongo_address)
        db = client[mongo_db]
        collection = db[mongo_collection]
        filename = time.strftime("%Y-%m-%d") + "-" + filename

        count = collection.count()
        current_count = 0

        with open(filename, 'w') as f:
            f.write('[')
            for doc in collection.find({}):
                current_count += 1
                f.write(json.dumps(doc, default=json_util.default))
                if (current_count != count):
                    f.write(',')
            f.write(']')
        print('Dump was created!')

    except Exception as ex:
        print('The error has occured')
        print(ex)

    finally:
        if client:
            client.close()


def load_dump_mongo(mongo_address="mongodb://localhost:27017/", mongo_db="python", mongo_collection="tokens",
                    filename="dump_mongo_python_tokens.json", rewrite=False, logfile=None):
    '''
    Load data from file to defined collection.
    '''
    try:
        client = pymongo.MongoClient(mongo_address)
        db = client[mongo_db]
        collection = db[mongo_collection]

        if collection.count() != 0 and rewrite:
            collection.remove()
            print('Collection was successfully removed!')

        with open(filename, 'r') as f:
            file_data = json_util.loads(f.read(), object_hook=json_util.object_hook)
            collection.insert_many(file_data)
        print('Collection was successfully set!')

    except ZeroDivisionError as ex:
        print('The error has occured')
        print(ex)

    finally:
        if client:
            client.close()


def get_mongo(mongo_address="mongodb://localhost:27017/", mongo_db="python", mongo_collection="tokens", logfile=None):
    try:
        client = pymongo.MongoClient(mongo_address)
        db = client[mongo_db]
        collection = db[mongo_collection]

        current = []

        if mongo_collection == "tokens":
            for x in collection.find():
                left = None
                right = None
                if 'leftborder' in x and x['leftborder']:
                    if 'allow_symbols' in x['leftborder']:
                        left = Border(x['leftborder']['allow_symbols'])
                    if 'their_dict' in x['leftborder']:
                        left.their_dict = x['leftborder']['their_dict']
                if 'rightborder' in x and x['rightborder']:
                    if 'allow_symbols' in x['rightborder']:
                        right = Border(x['rightborder']['allow_symbols'])
                    if 'their_dict' in x['rightborder']:
                        right.their_dict = x['rightborder']['their_dict']

                current.append(Token(x['prior'], x['reg'], x['name'], left, right))
        elif mongo_collection == "rules":
            for x in collection.find():
                role = []
                ignore_symbols = {}
                visa_verse = []
                visa_verse_tokens = []
                use_parent_final_words = False
                inner = False
                could_be_end = None
                check_could_be_end = None
                if 'role' in x:
                    role = x['role']
                if 'ignore_symbols' in x:
                    ignore_symbols = x['ignore_symbols']
                if 'inner' in x:
                    inner = x['inner']
                if 'visa_verse' in x:
                    visa_verse = x['visa_verse']
                if 'visa_verse_tokens' in x:
                    visa_verse_tokens = x['visa_verse_tokens']
                if 'use_parent_final_words' in x:
                    use_parent_final_words = x['use_parent_final_words']
                if 'check_could_be_end' in x:
                    check_could_be_end = x['check_could_be_end']
                if 'could_be_end' in x:
                    could_be_end = x['could_be_end']
                current.append(
                    Rule(x['keyword'], x['allow_tokens'], x['final_words'], role, ignore_symbols, inner, visa_verse,
                         visa_verse_tokens, use_parent_final_words, could_be_end, check_could_be_end))
        elif mongo_collection == "bugs":
            for x in collection.find():
                id = 0
                object = ""
                line = 0
                column = 0
                description = ""
                priority = 1
                important = 1
                type = ""
                date = ""
                author = ""
                program = ""
                version = "1.0.0"
                state = "Open"
                manage_by = ""
                possible_decision = ""
                if 'id' in x:
                    id = x['id']
                if 'object' in x:
                    object = x['object']
                if 'line' in x:
                    line = x['line']
                if 'column' in x:
                    column = x['column']
                if 'description' in x:
                    description = x['description']
                if 'priority' in x:
                    priority = x['priority']
                if 'important' in x:
                    important = x['important']
                if 'type' in x:
                    type = x['type']

                if 'date' in x:
                    date = x['date']
                if 'author' in x:
                    author = x['author']
                if 'program' in x:
                    program = x['program']
                if 'version' in x:
                    version = x['version']
                if 'state' in x:
                    state = x['state']
                if 'manage_by' in x:
                    manage_by = x['manage_by']
                if 'possible_decision' in x:
                    possible_decision = x['possible_decision']
                current.append(
                    Bug(id, object, line, column, description, priority, important, type, date, author, program,
                        version, state, manage_by, possible_decision))

    except Exception as ex:
        print('The error has occured')
        print(ex)

    finally:
        if client:
            client.close()
        if current:
            return current


def get_mongo_param(mongo_address="mongodb://localhost:27017/", mongo_db="bug_tracking", mongo_collection="bugs",
                    help_fields={"program": ""}, hint_field="id", model=-1, logfile=None):
    try:
        result = None
        client = pymongo.MongoClient(mongo_address)
        db = client[mongo_db]
        collection = db[mongo_collection]
        res = collection.find(help_fields).sort([(hint_field, model)])
        result = res[0][hint_field]

    except Exception as ex:
        print('The error has occured')
        print(ex)

    finally:
        if client:
            client.close()
        if result:
            return result


def get_mongo_by_fields(mongo_address="mongodb://localhost:27017/", mongo_db="", mongo_collection="", hint_fields={},
                        logfile=None):
    try:
        result = None
        client = pymongo.MongoClient(mongo_address)
        db = client[mongo_db]
        collection = db[mongo_collection]
        result = collection.find(hint_fields)

    except Exception as ex:
        print('The error has occured')
        print(ex)

    finally:
        if client:
            client.close()
        if result:
            return result


def set_mongo(mongo_address="mongodb://localhost:27017/", mongo_db="python", mongo_collection="tokens",
              collection_to_read=pytokens, rewrite=False, check_on_rewrite=[], hint_fields={}, logfile=None):
    try:
        client = pymongo.MongoClient(mongo_address)
        db = client[mongo_db]
        collection = db[mongo_collection]

        if collection.count() != 0 and rewrite:
            collection.remove()
            print('Collection was successfully removed!')

        check_collection = None
        if check_on_rewrite:
            check_collection = collection.find(hint_fields)

        for item in collection_to_read:
            if not type(item) is dict:
                item = vars(item)
            checks = True

            if check_collection:
                for sub_item in check_collection:
                    for check_field in check_on_rewrite:
                        if sub_item[check_field] == item[check_field]:
                            checks = False
                            break
                    if not checks:
                        break
            if checks:
                collection.insert_one(item)
        print('Collection was successfully set!')

    except Exception as ex:
        print('The error has occured')
        print(ex)

    finally:
        if client:
            client.close()


if __name__ == "__main__":
    set_mongo(rewrite=True)
    set_mongo(mongo_collection="rules", collection_to_read=pyrules, rewrite=True)
    set_mongo(mongo_db="sharp", mongo_collection="tokens", collection_to_read=sharp_tokens, rewrite=True)
    set_mongo(mongo_db="bug_tracking", mongo_collection="severity", collection_to_read=severity, rewrite=True)
    set_mongo(mongo_db="bug_tracking", mongo_collection="priority", collection_to_read=priority, rewrite=True)
    set_mongo(mongo_db="bug_tracking", mongo_collection="persons", collection_to_read=first_persons, rewrite=True)
    # if change_mongo({'login':'someone'}, {'role': 'something'}, mongo_db='bug_tracking', mongo_collection='persons'):
    #     print(login('someone', '123'))
    #
    # test = get_mongo(mongo_db="bug_tracking", mongo_collection="bugs")
    # for item in test:
    #     print(item.id, item.object)
    # make_dump_mongo()
    # load_dump_mongo(filename="2019-05-04-dump_mongo_python_tokens.json", rewrite=True)
