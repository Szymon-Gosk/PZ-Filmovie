"""Forms definitions for user app"""
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from users.models import Profile


def valid_user_name(name):
    """Defining all the usernames the user can't use in account creator"""
    special_characters =['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    forbidden_user_names = ['about', 'access', 'account', 'accounts', 'add', 'address', 'adm', 'admin', 'administration', 'adult',
      'advertising', 'affiliate', 'affiliates', 'ajax', 'analytics', 'android', 'anon', 'anonymous', 'api',
      'app', 'apps', 'archive', 'atom', 'auth', 'authentication', 'avatar',
      'backup', 'banner', 'banners', 'bin', 'billing', 'blog', 'blogs', 'board', 'bot', 'bots', 'business',
      'chat', 'cache', 'cadastro', 'calendar', 'campaign', 'careers', 'cgi', 'client', 'cliente', 'code', 'comercial',
      'compare', 'config', 'connect', 'contact', 'contest', 'create', 'code', 'compras', 'css',
      'dashboard', 'data', 'db', 'design', 'delete', 'demo', 'design', 'designer', 'dev', 'devel', 'dir', 'directory',
      'doc', 'docs', 'domain', 'download', 'downloads', 'edit', 'editor', 'email', 'ecommerce',
      'forum', 'forums', 'faq', 'favorite', 'feed', 'feedback', 'flog', 'follow', 'file', 'files', 'free', 'ftp',
      'gadget', 'gadgets', 'games', 'guest', 'group', 'groups',
      'help', 'home', 'homepage', 'host', 'hosting', 'hostname', 'html', 'http', 'httpd', 'https', 'hpg',
      'info', 'information', 'image', 'img', 'images', 'imap', 'index', 'invite', 'intranet', 'indice', 'ipad', 'iphone', 'irc',
      'java', 'javascript', 'job', 'jobs', 'js',
      'knowledgebase', 'log', 'login', 'logs', 'logout', 'list', 'lists',
      'mail', 'mail1', 'mail2', 'mail3', 'mail4', 'mail5', 'mailer', 'mailing', 'mx', 'manager', 'marketing', 'master', 'me', 'media', 'message',
      'microblog', 'microblogs', 'mine', 'mp3', 'msg', 'msn', 'mysql', 'messenger', 'mob', 'mobile', 'movie', 'movies', 'music', 'musicas', 'my',
      'name', 'named', 'net', 'network', 'new', 'news', 'newsletter', 'nick', 'nickname', 'notes', 'noticias', 'ns', 'ns1', 'ns2', 'ns3', 'ns4',
      'old', 'online', 'operator', 'order', 'orders',
      'page', 'pager', 'pages', 'panel', 'password', 'perl', 'pic', 'pics', 'photo', 'photos', 'photoalbum', 'php', 'plugin', 'plugins', 'pop', 'pop3', 'post',
      'postmaster', 'postfix', 'posts', 'profile', 'project', 'projects', 'promo', 'pub', 'public', 'python',
      'random', 'register', 'registration', 'root', 'ruby', 'rss',
      'sale', 'sales', 'sample', 'samples', 'script', 'scripts', 'secure', 'send', 'service', 'shop', 'sql', 'signup', 'signin', 'search', 'security',
      'settings', 'setting', 'setup', 'site', 'sites', 'sitemap', 'smtp', 'soporte', 'ssh', 'stage', 'staging', 'start', 'subscribe', 'subdomain',
      'suporte', 'support', 'stat', 'static', 'stats', 'status', 'store', 'stores', 'system',
      'tablet', 'tablets', 'tech', 'telnet', 'test', 'test1', 'test2', 'test3', 'teste', 'tests', 'theme', 'themes', 'tmp', 'todo', 'task', 'tasks', 'tools', 'tv', 'talk',
      'update', 'upload', 'url', 'user', 'username', 'usuario', 'usage',
      'vendas', 'video', 'videos', 'visitor',
      'win', 'ww', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'www6', 'www7', 'wwww', 'wws', 'wwws', 'web', 'webmail', 'website', 'websites', 'webmaster', 'workshop',
      'xxx', 'xpg', 'you', 'yourname', 'yourusername', 'yoursite', 'yourdomain']

    if name.lower() in forbidden_user_names:
        raise ValidationError('Invalid username!')
    
    if any(x in special_characters for x in name):
        raise ValidationError('You cannot add special symbol in your username')
    
    if User.objects.filter(username__iexact=name).exists():
        raise ValidationError('This username is already taken')

def unique_email(mail):
    """Returning the error if user uses an email that is already in database in account creator"""
    if User.objects.filter(email__iexact=mail).exists():
        raise ValidationError('User with this email already exists')

class SignupForm(forms.ModelForm):
    """Defining the registration form"""
    username = forms.CharField(max_length=25, required=True)
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    email = forms.CharField(widget=forms.EmailInput(), max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Confirm your password')

    class Meta:
        model = User
        fields=('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

    def __init__(self, *args, **kwargs):
        """Appending all validating functions to specific fields"""
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(valid_user_name)
        self.fields['email'].validators.append(unique_email)

    def clean(self):
        super(SignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self._errors['password'] = self.error_class(['Passwords do not match!'])

        return self.cleaned_data

class ChangePasswordForm(forms.ModelForm):
    """Defines the change password form"""
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(widget=forms.PasswordInput(), label='Old password', required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(), label='New password', required=True)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm new password', required=True)

    class Meta:
        model = User
        fields = ('id', 'old_password', 'new_password', 'confirm_new_password')

    def clean(self):
        super(ChangePasswordForm, self).clean()
        id = self.cleaned_data.get('id')
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        user = User.objects.get(pk=id)

        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class(['Old password do not match'])

        if new_password != confirm_new_password:
            self._errors['new_password'] = self.error_class(['Passwords do not match'])

        return self.cleaned_data


class EditProfileForm(forms.ModelForm):
    """Defines the edit profile form"""
    picture = forms.ImageField(required=False)
    background = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=25, required=False)
    last_name = forms.CharField(max_length=25, required=False)
    bio = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Profile
        fields = ('picture', 'background', 'first_name', 'last_name', 'bio')
