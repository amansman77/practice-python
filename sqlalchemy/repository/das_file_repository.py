from entity.model import DasFile
from flask import Flask
from sqlalchemy.orm import aliased
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import joinedload

class DasFileRepository:

    @classmethod
    def find_das_files_by_related_id(cls, file_id):
        result = DasFile.query.filter(DasFile.file_id == file_id).options(joinedload(DasFile.prev_file)).options(joinedload(DasFile.next_file)).first()
        return cls.__get_target_files(result)

    @classmethod
    def __get_target_files(cls, source_file):
        targets = []
        prev_start = source_file.prev_file
        next_start = source_file.next_file
        while(len(prev_start) != 0):
            targets.insert(0, prev_start[0])
            prev_start = prev_start[0].prev_file
        targets.append(source_file)
        while(len(next_start) != 0):
            targets.append(next_start[0])
            next_start = next_start[0].next_file
        return targets
