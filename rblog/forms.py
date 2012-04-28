#!/usr/bin/env python
#-*-coding:utf-8-*-
#forms.py

from web import form

vauthor = form.regexp(r".+", "Name can not be empty!")
vemail  = form.regexp(r".*@.*", "Email address is empty or not valid")
vcomment= form.regexp(r".+", "Comment cn not be empty!")

comment_form = form.Form(
    form.Textbox("author", vauthor, size="22",  tabindex="1", value="", class_="comment"),
    form.Textbox("email", vemail,   size="22",  tabindex="2", value="", class_="comment"),
    form.Textbox("url",             size="22", tabindex="3", value="", class_="comment"),
    form.Textarea("comment", vcomment, cols="100%", rows="10", tabindex="4", value="", class_="comment"),
    form.Button("submit", class_="comment", type="submit", tabindex="5",
        html="Submit Comment", title="Pleas review your comment before you submit"),
)

settings_form = form.Form(
    form.Textbox("title",       maxlength="200", tabindex="1", value="", class_="comment"),
    form.Textbox("subtitle",    maxlength="200", tabindex="2", value="", class_="comment"),
    form.Textarea("notice",     rows="10",cols="100%", tabindex="3", value="", class_="comment"),
    form.Textbox("keywords",    maxlength="200", tabindex="4", value="", class_="comment"),
    form.Textbox("description", maxlength="200", tabindex="5", value="", class_="comment"),
    form.Textbox("email", vemail, maxlength="200", tabindex="6", value=""),
    form.Textbox("email", vemail, maxlength="200", tabindex="6", value=""),
    form.Button("submit", type="submit", class_="button-primary", html="Save changes")
)
