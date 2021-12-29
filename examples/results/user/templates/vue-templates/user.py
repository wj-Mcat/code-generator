"""
User api file
"""
from flask import Blueprint, request, current_app, jsonify
from chatbot_server.extensions import db
from chatbot_server.utils import database_utils as dbu
from chatbot_server.utils import data_utils as du
from chatbot_server.models.general import User
from chatbot_server.blueprints.general import general_bp


@general_bp.route('/user/query', methods=['POST'])
def get_users():
    """获取列表"""
    params = request.get_json(force=True)["list_query"]
    du.time_start_end(params, "create_time")
    try:
        model_filter = dbu.build_filter("User", params)
    except Exception as e:
        current_app.logger.warning(e)
        return dbu.inner_error("查询失败")

    query = User.query.filter(*model_filter)
    return dbu.paginate_data(query, params)


@general_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    """获取单个数据"""
    user = User.query.filter(
        User.user_id == user_id
    ).first()

    if not user:
        return dbu.inner_error("该不存在或已被删除")
    return jsonify({"code": 200, "data": user})


@general_bp.route('/user', methods=['POST'])
def add_user():
    """新增"""
    data = request.get_json()

    user = User()
    dbu.update(user, data)
    db.session.add(user)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("新增失败")
    return jsonify(
        {
            "data": {"user_id": user.user_id},
            "code": 200,
            "msg": "新增成功"
        }
    )

@general_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    """更新"""
    data: dict = request.get_json()

    user = User.query.filter(
        User.user_id == user_id
    ).first()

    if not user:
        return dbu.inner_error("该不存在或已被删除")

    dbu.update(user, data)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("更新失败")
    return jsonify(
        {"data":
             {"user_id": user.user_id},
         "code": 200,
         "msg": "更新角色成功"
         }
    )


@general_bp.route('user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    """删除"""
    user = User.query.filter(
        User.user_id == user_id
    ).first()

    if not user:
        return dbu.inner_error("该不存在或已被删除")

    db.session.delete(user)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("删除失败")
    return jsonify({"data": {"user_id": user_id}, "code": 200, "msg": "删除角色成功"})