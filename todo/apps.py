from django.apps import AppConfig
if os.path.exists("env.py"):
    import env



class TodoConfig(AppConfig):
    name = 'todo'
