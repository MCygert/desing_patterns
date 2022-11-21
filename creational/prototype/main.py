import datetime

from prototype import Shopkeeper

if __name__== "__main__":
    # print('Starting to create a Shopkeeper NPC: ', datetime.datetime.now().time())
    # shopkeeper = Shopkeeper(180, 22, 5, 8)
    # print('Finished creating a Shopkeeper NPC: ', datetime.datetime.now().time())
    # print('Attributes: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

    print('Instantiating trader guild at: ', datetime.datetime.now().time())
    shopkeeper_template = Shopkeeper(180, 22, 5, 8)
    for i in range(5):
        shopkeeper_clone = shopkeeper_template.clone()
        print(f'Finished creating a Shopkeeper clone {i} at: ', datetime.datetime.now().time())
    print('Finished instantiating trader guild at: ', datetime.datetime.now().time())