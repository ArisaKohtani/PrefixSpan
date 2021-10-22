from postfix import postfix 

def project(DB,a):
    projectedDB = []
    for i in DB:
        projectedDB.append(postfix(i,a))
    return projectedDB

