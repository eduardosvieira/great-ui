
# 
# class RegisterForm(Form):
#     name = StringField('Nome',[validators.length(min=1, max=50)])
#     username = StringField('Usuário',[validators.length(min=4, max=25)])
#     email = StringField('Email',[validators.length(min=6, max=50)])
#     password = PasswordField('Senha',[
#     validators.DataRequired(),
#     validators.EqualTo('confirm', message="Password do not match")
#     ])
#     confirm = PasswordField('Confirm Password')
