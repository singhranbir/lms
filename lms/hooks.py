# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lms"
app_title = "LMS"
app_publisher = "Frappe"
app_description = "LMS"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "school@frappe.io"
app_license = "AGPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lms/css/lms.css"
# app_include_js = "/assets/lms/js/lms.js"

# include js, css files in header of web template
web_include_css = "/assets/css/lms.css"
# web_include_css = "/assets/lms/css/lms.css"
#web_include_js = "website.bundle.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lms.install.before_install"
# after_install = "lms.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"User": "lms.overrides.user.CustomUser",
	"Web Template": "lms.overrides.web_template.CustomWebTemplate"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {

}

# Scheduled Tasks
# ---------------
#scheduler_events = {
#	"daily": [
#		"erpnext.stock.reorder_item.reorder_item"
#	]
#}

fixtures = ["Custom Field"]

# Testing
# -------

# before_tests = "lms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "lms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Add all simple route rules here
website_route_rules = [
	{"from_route": "/sketches/<sketch>", "to_route": "sketches/sketch"},
	{"from_route": "/courses/<course>", "to_route": "courses/course"},
	{"from_route": "/courses/<course>/<certificate>", "to_route": "courses/certificate"},
	{"from_route": "/hackathons/<hackathon>", "to_route": "hackathons/hackathon"},
	{"from_route": "/hackathons/<hackathon>/<project>", "to_route": "hackathons/project"},
	{"from_route": "/courses/<course>/learn", "to_route": "batch/learn"},
	{"from_route": "/courses/<course>/learn/<int:chapter>.<int:lesson>", "to_route": "batch/learn"},
	{"from_route": "/courses/<course>/progress", "to_route": "batch/progress"},
	{"from_route": "/courses/<course>/join", "to_route": "batch/join"},
	{"from_route": "/users/<string(minlength=4):username>", "to_route": "profiles/profile"}
]

website_redirects = [
	{"source": "/update-profile", "target": "/edit-profile"},
]

update_website_context = [
    'lms.widgets.update_website_context',
]

## Specify the additional tabs to be included in the user profile page.
## Each entry must be a subclass of lms.lms.plugins.ProfileTab
# profile_tabs = []

## Specify the extension to be used to control what scripts and stylesheets
## to be included in lesson pages. The specified value must be be a
## subclass of lms.plugins.PageExtension
# lms = None

#lms_lesson_page_extensions = [
#	"lms.plugins.LiveCodeExtension"
#]

## Markdown Macros for Lessons
lms_markdown_macro_renderers = {
    "Exercise": "lms.plugins.exercise_renderer",
    "Quiz": "lms.plugins.quiz_renderer",
    "YouTubeVideo": "lms.plugins.youtube_video_renderer",
    "Video": "lms.plugins.video_renderer"
}

# set this to "/" to have profiles on the top-level
profile_url_prefix = "/users/"
