from django import forms
from django.contrib.auth.forms import UserCreationForm
from auth_app.models import CustomUser  # Assurez-vous d'importer votre modèle CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255,
        help_text='Required. Enter a valid email address.'
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser  # Spécifiez le modèle CustomUser que vous utilisez
        fields = UserCreationForm.Meta.fields + ("email", "password1", "password2")

    def email(self):
        # Validez que l'e-mail est unique dans la base de données
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        # Enregistrez l'utilisateur dans la base de données
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
