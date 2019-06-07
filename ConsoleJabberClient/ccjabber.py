from twisted.words.protocols.jabber import client, jid, xmlstream
from twisted.words.xish import domish
from twisted.internet import reactor

name = None
server = None
resource = None
password = None
me = None

thexmlstream = None


def in_online(xmlstream):
    global factory
    print('Initializing...Good')
    xmlstream.addObserver('/message', gotMessage)
    xmlstream.addObserver('/*', gotSomething)
    print("If you want send new message press 'y' : or 'Enter' to continue")
    s = input()
    if s == 'y':
        to_ = input('Input ID : ')
        if len(to_) == 0:
            to_ = input('Input ID : ')
        send(me, to_)
    else:
        print('Continue. We are online')


def authentification(xmlstream):
    global thexmlstream
    thexmlstream = xmlstream
    print("Authorized!")

    presence = domish.Element(('jabber:client', 'presence'))
    presence.addElement('status').addContent('Online')
    xmlstream.send(presence)

    in_online(xmlstream)


def send(author, to):
    global thexmlstream
    message = domish.Element(('jabber:client', 'message'))
    message["to"] = jid.JID(to).full()
    message["from"] = jid.JID(author).full()
    message["type"] = "chat"
    ans = input('Input message or Enter to continue: ')
    message.addElement("body", "jabber:client", ans)

    thexmlstream.send(message)


def gotMessage(el):
    global me
    from_id = el["from"]

    body = "empty"
    for e in el.elements():
        if e.name == "body":
            body = e.__str__()
        break
    print('New massage from: ', from_id, ' . Text message: ', body)
    send(me, from_id)


def gotSomething(el):
    pass


def authfailedEvent(xmlstream):
    global reactor
    print('Auth failed!')
    reactor.stop()


def invaliduserEvent(xmlstream):
    print("Invalid User")


def registerfailedEvent(xmlstream):
    print('Register failed!')

def serv_id(path):
    cur = 0
    for _ in path:
        cur += 1
        if _ == '@':
            new_id = path[cur:]
            return new_id


if __name__ == '__main__':
    id_ = input("Input ID: ")
    PASSWORD = input('Input password: ')

    myJid = jid.JID(id_)
    me = id_
    factory = client.XMPPClientFactory(myJid, PASSWORD)


    factory.addBootstrap(xmlstream.STREAM_AUTHD_EVENT, authentification)
    factory.addBootstrap(client.BasicAuthenticator.INVALID_USER_EVENT, invaliduserEvent)
    factory.addBootstrap(client.BasicAuthenticator.AUTH_FAILED_EVENT, authfailedEvent)
    factory.addBootstrap(client.BasicAuthenticator.REGISTER_FAILED_EVENT, registerfailedEvent)

    reactor.connectTCP(serv_id(me), 5222, factory)
    reactor.run()
