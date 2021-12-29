"""
RegexExtractor api file
"""
from flask import Blueprint, request, current_app, jsonify
from chatbot_server.extensions import db
from chatbot_server.utils import database_utils as dbu
from chatbot_server.utils import data_utils as du
from chatbot_server.models.general import RegexExtractor
from chatbot_server.blueprints.general import general_bp


@general_bp.route('/regex_extractor/query', methods=['POST'])
def get_regex_extractors():
    """获取列表"""
    params = request.get_json(force=True)["list_query"]
    du.time_start_end(params, "create_time")
    try:
        model_filter = dbu.build_filter("RegexExtractor", params)
    except Exception as e:
        current_app.logger.warning(e)
        return dbu.inner_error("查询失败")

    query = RegexExtractor.query.filter(*model_filter)
    return dbu.paginate_data(query, params)


@general_bp.route('/regex_extractor/<int:regex_extractor_id>', methods=['GET'])
def get_regex_extractor(regex_extractor_id: int):
    """获取单个数据"""
    regex_extractor = RegexExtractor.query.filter(
        RegexExtractor.regex_extractor_id == regex_extractor_id
    ).first()

    if not regex_extractor:
        return dbu.inner_error("该不存在或已被删除")
    return jsonify({"code": 200, "data": regex_extractor})


@general_bp.route('/regex_extractor', methods=['POST'])
def add_regex_extractor():
    """新增"""
    data = request.get_json()

    regex_extractor = RegexExtractor()
    dbu.update(regex_extractor, data)
    db.session.add(regex_extractor)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("新增失败")
    return jsonify(
        {
            "data": {"regex_extractor_id": regex_extractor.regex_extractor_id},
            "code": 200,
            "msg": "新增成功"
        }
    )

@general_bp.route('/regex_extractor/<int:regex_extractor_id>', methods=['PUT'])
def update_regex_extractor(regex_extractor_id: int):
    """更新"""
    data: dict = request.get_json()

    regex_extractor = RegexExtractor.query.filter(
        RegexExtractor.regex_extractor_id == regex_extractor_id
    ).first()

    if not regex_extractor:
        return dbu.inner_error("该不存在或已被删除")

    dbu.update(regex_extractor, data)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("更新失败")
    return jsonify(
        {"data":
             {"regex_extractor_id": regex_extractor.regex_extractor_id},
         "code": 200,
         "msg": "更新角色成功"
         }
    )


@general_bp.route('regex_extractor/<int:regex_extractor_id>', methods=['DELETE'])
def delete_regex_extractor(regex_extractor_id: int):
    """删除"""
    regex_extractor = RegexExtractor.query.filter(
        RegexExtractor.regex_extractor_id == regex_extractor_id
    ).first()

    if not regex_extractor:
        return dbu.inner_error("该不存在或已被删除")

    db.session.delete(regex_extractor)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("删除失败")
    return jsonify({"data": {"regex_extractor_id": regex_extractor_id}, "code": 200, "msg": "删除角色成功"})