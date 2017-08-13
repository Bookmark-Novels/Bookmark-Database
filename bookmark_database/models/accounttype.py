from sqlalchemy import Column, Integer, String

from ..db import BaseModel, Model

class AccountType(BaseModel, Model):
    """
    Represents various Bookmark account types.
    """
    __tablename__ = 'bookmark_account_types'

    id = Column(Integer, primary_key=True)
    display_name = Column(String(50))

class Types(object):
    """
    Enum for Account types.
    """
    Admin = 1
    Native = 2
    Novel_Updates = 3
    Global_Moderator = 4
    Engineer = 5
