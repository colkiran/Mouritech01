
import O04SqlalcmCreateDB as db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

# tr = db.Player('PLY001', 'Sachin Tendulkar', 'Cricket', '100 centuries')
# tr = db.Player('PLY002', 'Mike Tyson', 'Boxing', '82 knockouts')
# tr = db.Player('PLY003', 'Lionel Messi', 'Football', '3 golden boot')
# tr = db.Player('PLY004', 'Roger Fedrer', 'Tennis', '25 Grandslams')
tr = db.Player('PLY005', 'Lewis Hamilton', 'Formula-1', '5 championships')

session.add(tr)

session.commit()
