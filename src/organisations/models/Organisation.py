from config.database import Model


class Organisation(Model):
    __fillable__ = ["name"]
