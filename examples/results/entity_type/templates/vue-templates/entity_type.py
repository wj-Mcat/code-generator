"""
EntityType api file
"""
from flask import Blueprint, request, current_app, jsonify
from chatbot_server.extensions import db
from chatbot_server.utils import database_utils as dbu
from chatbot_server.utils import data_utils as du
from chatbot_server.models.general import EntityType
from chatbot_server.blueprints.general import general_bp


@general_bp.route('/entity_type/query', methods=['POST'])
def get_entity_types():
    """获取列表"""
    params = request.get_json(force=True)["list_query"]
    du.time_start_end(params, "create_time")
    try:
        model_filter = dbu.build_filter("EntityType", params)
    except Exception as e:
        current_app.logger.warning(e)
        return dbu.inner_error("查询失败")

    query = EntityType.query.filter(*model_filter)
    return dbu.paginate_data(query, params)


@general_bp.route('/entity_type/<int:entity_type_id>', methods=['GET'])
def get_entity_type(entity_type_id: int):
    """获取单个数据"""
    entity_type = EntityType.query.filter(
        EntityType.entity_type_id == entity_type_id
    ).first()

    if not entity_type:
        return dbu.inner_error("该不存在或已被删除")
    return jsonify({"code": 200, "data": entity_type})


@general_bp.route('/entity_type', methods=['POST'])
def add_entity_type():
    """新增"""
    data = request.get_json()

    entity_type = EntityType()
    dbu.update(entity_type, data)
    db.session.add(entity_type)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("新增失败")
    return jsonify(
        {
            "data": {"entity_type_id": entity_type.entity_type_id},
            "code": 200,
            "msg": "新增成功"
        }
    )

@general_bp.route('/entity_type/<int:entity_type_id>', methods=['PUT'])
def update_entity_type(entity_type_id: int):
    """更新"""
    data: dict = request.get_json()

    entity_type = EntityType.query.filter(
        EntityType.entity_type_id == entity_type_id
    ).first()

    if not entity_type:
        return dbu.inner_error("该不存在或已被删除")

    dbu.update(entity_type, data)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("更新失败")
    return jsonify(
        {"data":
             {"entity_type_id": entity_type.entity_type_id},
         "code": 200,
         "msg": "更新角色成功"
         }
    )


@general_bp.route('entity_type/<int:entity_type_id>', methods=['DELETE'])
def delete_entity_type(entity_type_id: int):
    """删除"""
    entity_type = EntityType.query.filter(
        EntityType.entity_type_id == entity_type_id
    ).first()

    if not entity_type:
        return dbu.inner_error("该不存在或已被删除")

    db.session.delete(entity_type)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("删除失败")
    return jsonify({"data": {"entity_type_id": entity_type_id}, "code": 200, "msg": "删除角色成功"})