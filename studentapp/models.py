from django.db import models

# Create your models here.  

class Stud_Sub(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
     
    class Meta:
        db_table = 'student subjects'
        verbose_name_plural = 'Student_subject'

    def __str__(self):
        return self.subject


class Teacher(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'TEACHERS'
        verbose_name_plural = 'TEACHERS'

    def __str__(self):
        return self.name 



class Stud_Data(models.Model):
    name = models.CharField(max_length=100, null = True, blank = False)
    roll_number = models.IntegerField( null = True, blank = False)
    subject = models.ForeignKey(Stud_Sub,blank = False, null = True ,on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher,blank = False, null = True ,on_delete = models.CASCADE)
     
    class Meta:
        db_table = 'student record'
        verbose_name_plural = 'Student_data'

    def __str__(self):
        return self.name



class Stud_Fee(models.Model):
    name = models.ForeignKey(Stud_Data, on_delete = models.CASCADE)
    FEE = models.IntegerField(null = True, blank = False)

    #choices = [('PYTHON', 'python'),
    #        ('DJANGO' ,'django')]
    class Meta:
        db_table = 'student Fees'
        verbose_name_plural = 'student Fees'

    def __str__(self):
        return self.name.name



class Stud_Games(models.Model):
    name = models.ForeignKey(Stud_Data, on_delete=models.CASCADE)

    choices = [('Paintball', 'Paintball'),
            ('Baseball' ,'Baseball'), 
            ('Polo' ,'Polo'),
            ('Golf' ,'Golf') ]
    Games = models.CharField(max_length=100,choices = choices, null=True, blank=True)

    class Meta:
        db_table = 'student games'
        verbose_name_plural = 'student games'

    def __str__(self):
        return self.Games 
    

class Job_Details(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    company = models.CharField(max_length=150, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)    
    salary = models.IntegerField(null=False, blank=False)
    description = models.CharField(max_length=250, null=True, blank=True)
    class Meta:
        db_table = 'JOB DETAILS'
        verbose_name_plural = ("JOB DETAILS")

    def __str__(self):
        return self.name


