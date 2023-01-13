from django.db import models

# Create your models here.
# declare a new model with a name "GeeksModel"

# declare a new model with a name "GeeksModel"

class UserDetail(models.Model):
    # fields of the model
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    last_modified = models.DateTimeField(auto_now_add=True)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name
