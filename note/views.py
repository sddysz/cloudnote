# -*- coding: utf-8 -*-

from datetime import datetime

from flask import Blueprint, flash, redirect, url_for, request, render_template,redirect,jsonify,json
from flask_login import current_user, login_user, login_required,logout_user, confirm_login, login_fresh
from flask_babelplus import gettext as _
from exceptions import AuthenticationError
from home.user import User
from notebook.models import Notebook
from note.models import Note,NoteContent


note = Blueprint("note", __name__)


@auth.route("/", methods=["GET"])
def index():
    #Logs the user in.
    userInfo = current_user
    userId = current_user.id
    # 没有登录
    if userId == ''
        redirect(url_for("auth.views.login"))
    # 已登录了, 那么得到所有信息
	notebooks = Notebook.getNotebooks(userId)
	#shareNotebooks, sharedUserInfos := shareService.GetShareNotebooks(userId)

    # 还需要按时间排序(DESC)得到notes
	notes = {}
	noteContent = {}
   
    if len(notebooks) > 0 {
		# noteId是否存在
		# 是否传入了正确的noteId
		hasRightNoteId = false
		if noteId is not None
			note = note.GetNoteById(noteId)

			if note.NoteId != ""
				noteOwner = note.UserId
				noteContent = NoteContent.getNoteContent(noteId, noteOwner)

				hasRightNoteId = true
				# 打开的是共享的笔记, 那么判断是否是共享给我的默认笔记
				if noteOwner != current_user.id()
					'''if shareService.HasReadPerm(noteOwner, c.GetUserId(), noteId) {
						// 不要获取notebook下的笔记
						// 在前端下发请求
						c.ViewArgs["curSharedNoteNotebookId"] = note.NotebookId.Hex()
						c.ViewArgs["curSharedUserId"] = noteOwner
						// 没有读写权限
					} else {
						hasRightNoteId = false
					}'''
                    hasRightNoteId = false
				else
					notes = noteService.ListNotes(c.GetUserId(), note.NotebookId.Hex(), false, c.GetPage(), 50, defaultSortField, false, false)

					// 如果指定了某笔记, 则该笔记放在首位
					lenNotes := len(notes)
					if lenNotes > 1 {
						notes2 := make([]info.Note, len(notes))
						notes2[0] = note
						i := 1
						for _, note := range notes {
							if note.NoteId.Hex() != noteId {
								if i == lenNotes { // 防止越界
									break
								}
								notes2[i] = note
								i++
							}
						}
						notes = notes2
					}
				}
			}

			// 得到最近的笔记
			_, latestNotes := noteService.ListNotes(c.GetUserId(), "", false, c.GetPage(), 50, defaultSortField, false, false)
			c.ViewArgs["latestNotes"] = latestNotes
		}
