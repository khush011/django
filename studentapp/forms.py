from django import forms


class Loginpy(forms.Form):
    n = forms.CharField(label='Name', max_length=100) 
     
    p = forms.CharField(label='password', widget = forms.PasswordInput())

    t = forms.CharField(label='Description', widget = forms.Textarea(attrs={'rows': 3}))

    e = forms.EmailField(label="E-mail")

    dob = forms.DateField(widget= forms.DateInput(attrs={'type': 'date'}))

    c = forms.ChoiceField(label='Colors' ,choices = [('pblue', 'BLUE'),
                                      ('pgreen', 'GREEN'),
                                      ('pred', 'RED')])

    g = forms.ChoiceField(label='Gender' ,choices = [('MALE', 'male'),
                                                     ('FEMALE', 'female')], widget = forms.RadioSelect())
                                                     
    m = forms.MultipleChoiceField(label = 'COURSES' ,widget = forms.CheckboxSelectMultiple(),choices = [('PYTHON', 'python'),
                                                                                                     ('DJANGO' ,'django')])


                                                                                                     
                                                                                            