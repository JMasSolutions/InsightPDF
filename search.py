from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os
from env.config import INDEX_DIR

def create_search_index():
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR)
        schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(stored=True, unique=True))
        ix = index.create_in(INDEX_DIR, schema)
    else:
        ix = index.open_dir(INDEX_DIR)
    return ix

def index_document(ix, doc):
    writer = ix.writer()
    writer.add_document(title=doc['title'], content=doc['content'], path=doc['path'])
    writer.commit()

def search_index(ix, query_str):
    qp = QueryParser("content", schema=ix.schema)
    q = qp.parse(query_str)
    results_list = []
    with ix.searcher() as searcher:
        results = searcher.search(q, limit=None)
        for result in results:
            results_list.append({'title': result['title'], 'path': result['path'], 'content': result['content']})
    return results_list