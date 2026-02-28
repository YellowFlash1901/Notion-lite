from pydantic import BaseModel


class Pagebase(BaseModel):
    title : str
    content: str

class CreatePage(Pagebase):
    pass

class PageResponse(Pagebase):
    id : str