"""
Entity api file
"""
from flask import Blueprint, request, current_app, jsonify
from chatbot_server.extensions import db
from chatbot_server.utils import database_utils as dbu
from chatbot_server.utils import data_utils as du
from chatbot_server.models.general import Entity
from chatbot_server.blueprints.general import general_bp


@general_bp.route('/entity/query', methods=['POST'])
def get_entitys():
    """获取列表"""
    params = request.get_json(force=True)["list_query"]
    du.time_start_end(params, "create_time")
    try:
        model_filter = dbu.build_filter("Entity", params)
    except Exception as e:
        current_app.logger.warning(e)
        return dbu.inner_error("查询失败")

    query = Entity.query.filter(*model_filter)
    return dbu.paginate_data(query, params)


@general_bp.route('/entity/<string:entity_id>', methods=['GET'])
def get_entity(entity_id: str):
    """获取单个数据"""
    entity = Entity.query.filter(
        Entity.entity_id == entity_id
    ).first()

    if not entity:
        return dbu.inner_error("该不存在或已被删除")
    return jsonify({"code": 200, "data": entity})


@general_bp.route('/entity', methods=['POST'])
def add_entity():
    """新增"""
    data = request.get_json()

    entity = Entity()
    dbu.update(entity, data)
    db.session.add(entity)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("新增失败")
    return jsonify(
        {
            "data": {"entity_id": entity.entity_id},
            "code": 200,
            "msg": "新增成功"
        }
    )

@general_bp.route('/entity/<string:entity_id>', methods=['PUT'])
def update_entity(entity_id: str):
    """更新"""
    data: dict = request.get_json()

    entity = Entity.query.filter(
        Entity.entity_id == entity_id
    ).first()

    if not entity:
        return dbu.inner_error("该不存在或已被删除")

    dbu.update(entity, data)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("更新失败")
    return jsonify(
        {"data":
             {"entity_id": entity.entity_id},
         "code": 200,
         "msg": "更新角色成功"
         }
    )


@general_bp.route('entity/<string:entity_id>', methods=['DELETE'])
def delete_entity(entity_id: str):
    """删除"""
    entity = Entity.query.filter(
        Entity.entity_id == entity_id
    ).first()

    if not entity:
        return dbu.inner_error("该不存在或已被删除")

    db.session.delete(entity)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return dbu.inner_error("删除失败")
    return jsonify({"data": {"entity_id": entity_id}, "code": 200, "msg": "删除角色成功"})