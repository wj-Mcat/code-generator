"""
create a light server to support restful api

"""
from __future__ import annotations
from typing import Any
import os
from flask import Flask, request, jsonify, render_template_string, send_file
from flask_cors import CORS

# pylint: disable=invalid-name
app = Flask(__name__)
CORS(app=app)


def success(msg: Any):
    """
    return the success msg
    """
    return jsonify({
        'code': 200,
        'msg': msg
    })


def error(msg: str):
    """
    return the errror msg
    """
    return jsonify({
        'code': 500,
        'msg': msg
    })


@app.route('/')
def index():
    """
    get the web tool page
    """
    dirname, filename = os.path.split(os.path.abspath(__file__))
    html = open(os.path.join(dirname, 'templates/vue/dist/index.html'))
    return html.read()

@app.route('/manifest.js')
@app.route('/vendor.js')
@app.route('/index.js')
def get_javascript_file():
    dirname, filename = os.path.split(os.path.abspath(__file__))

    print(request.url)
    filename = ''
    if 'manifest.js' in request.url:
        filename = os.path.join(dirname, 'templates/vue/dist/manifest.js')
    elif 'vendor.js' in request.url:
        filename = os.path.join(dirname, 'templates/vue/dist/vendor.js')
    elif 'index.js' in request.url:
        filename = os.path.join(dirname, 'templates/vue/dist/index.js')

    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/generate', methods=['POST'])
def generate():
    """
    generate the code
    """
    from .main import render_from_server
    config = request.get_json()
    print(config)
    render_from_server(config)
    return success('生成成功！')

@app.route('/render')
def render():
    """
    render the page
    """
    data = request.get_json()
    return data


@app.route('/plugins_templates')
def read_plugins_templates():
    """
    read the plugins and templates to the front page
    """
    # read the plugins
    plugins = {}
    plugins_path = os.path.join(os.getcwd(), 'plugins')
    if os.path.isdir(plugins_path):
        for file in os.listdir(plugins_path):
            if os.path.isfile(os.path.join(plugins_path, file)):
                content = open(os.path.join(plugins_path, file)).read()
                plugins[file] = content

    # read the templates
    templates = {}
    templates_path = os.path.join(os.getcwd(), 'templates')
    if os.path.isdir(templates_path):
        for file in os.listdir(templates_path):
            if os.path.isfile(os.path.join(templates_path, file)):
                content = open(os.path.join(templates_path, file)).read()
                templates[file] = content

    # return the result of plugins & templates
    return success(
        {
            'plugins': plugins,
            'templates': templates
        }
    )


def run_light_server():
    """
    using flask to run light server
    """
    app.run()
