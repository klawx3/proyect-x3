from django.db import models

class Tag(models.Model):
    name        =   models.CharField(max_length=50)

    def __str__(self):
        return "[name={}]".format(self.name)


class User(models.Model):
    username    =   models.CharField(max_length=50, unique=True)
    password    =   models.CharField(max_length=100)
    email       =   models.EmailField(max_length=100, unique=True)
    active      =   models.BooleanField()
    created     =   models.DateTimeField()
    lastvisit   =   models.DateTimeField()
    admin       =   models.BooleanField()
    

    def __str__(self):
        return "[username={},password={},email={},active={}, \
        created={},lastvisit={},admin={}]".format(self.username,self.password,
        self.email,self.active,self.created,self.lastvisit,self.admin)


class Post(models.Model):
    user        =   models.ForeignKey(User, on_delete=models.CASCADE)
    text        =   models.TextField()
    date        =   models.DateTimeField()
    tags        =   models.ManyToManyField(Tag)

    def __str__(self):
        return "[user={},text={},date={},tags={}]".format(self.user,self.text,
        self.date,self.tags)



    


