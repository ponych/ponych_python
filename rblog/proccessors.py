#proccessors.py
import web
from sqlalchemy.orm import scoped_session, sessionmaker
from models import engine

def load_sqla(handler):
    web.ctx.org = scoped_session(sessionmaker(bind=engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()

        # if the above alone doesnt work,uncomment the following line
        # web.ctx.org.expunge_all()
        web.ctx.orm.close()