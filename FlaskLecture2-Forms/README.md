# Flask Forms

Defining a form which takes in a field of data and has a set of rules to validate the input 

```python
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
```

We can recieve input from the user and make it a new form in which we validate the input 
```python
	form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
```


# Try it yourself
 1. Add a new value to the form and render it on the page.  