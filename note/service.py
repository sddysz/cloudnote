# -*- coding: utf-8 -*-
from exceptions import AuthenticationError



def getNoteById(noteId):
    userInfo = current_user
    userId = current_user.id