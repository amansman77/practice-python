from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from entity import sql_db


class DasFile(sql_db.Model):
    __tablename__ = 'das_files'
    file_id = sql_db.Column(sql_db.Integer, primary_key=True)
    next_file_id = sql_db.Column(sql_db.Integer, sql_db.ForeignKey("das_files.file_id"))
    prev_file_id  = sql_db.Column(sql_db.Integer, sql_db.ForeignKey("das_files.file_id"))
    
    file_status = sql_db.Column(sql_db.String)
    time_data_size = sql_db.Column(sql_db.Integer)
    point_data_size = sql_db.Column(sql_db.Integer)
    begin_time = sql_db.Column(sql_db.Time)
    end_time = sql_db.Column(sql_db.Time)
    start_position = sql_db.Column(sql_db.Float)
    end_position = sql_db.Column(sql_db.Float)
    bucket_name = sql_db.Column(sql_db.String)
    key_name = sql_db.Column(sql_db.String)
    value_id = sql_db.Column(sql_db.String)

    next_file = sql_db.relationship("DasFile", foreign_keys='DasFile.prev_file_id', lazy='joined')
    prev_file = sql_db.relationship('DasFile', foreign_keys='DasFile.next_file_id', lazy='joined')
