from typing import Annotated
from fastapi import Depends

from .schemas import ProductFullResp, ProjectCreateReq


lst: list[ProductFullResp] = [
    ProductFullResp(id=1, key='P1', name='First proj', description='This is the first project'),
    ProductFullResp(id=2, key='P2', name='Second proj', description='This is the second project'),
    ProductFullResp(id=3, key='P3', name='Third proj', description='This is the third project'),
    ProductFullResp(id=5, key='P5', name='Fifth proj', description='This is the fifth project'),
]


class ProjectRepo():
    def get_list(self) -> list[ProductFullResp]:
        return lst

    def get_by_id(self, pid: int) -> ProductFullResp | None:
        result = list(filter(lambda x: x.id == pid, lst))
        return result[0] if len(result) else None

    def set_item(self, data: ProjectCreateReq) -> ProductFullResp:
        max_id = 0
        for i in lst:
            if i.id > max_id:
                max_id = i.id
        candidate = ProductFullResp(id=(max_id + 1), name=data.name, key=f'P{max_id + 1}', description=data.description)
        lst.append(candidate)
        return candidate

    def del_item(self, pid: int) -> bool:
        flag = False
        for i, item in enumerate(lst):
            if item.id == pid:
                del lst[i]
                flag = True
                break
        return flag


def get_project_repo():
    return ProjectRepo()

ProjectRepoDeps = Annotated[
    ProjectRepo,
    Depends(get_project_repo),
]
