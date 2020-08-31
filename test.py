class Eleve(models.Model):

    #Here are the fields created by django-assistant make sure to complete the parenthesis properly
    
    name = CharField("name")
    test = BooleanField("test")
    test2 = EmailField("test2")

    #For now the assistant assign the default model name
    class Meta:
        verbose_name = "Eleve"

    #By default this return the first field you created
    def __str__(self):
        return self.name